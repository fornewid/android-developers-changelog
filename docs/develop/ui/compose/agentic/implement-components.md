---
title: https://developer.android.com/develop/ui/compose/agentic/implement-components
url: https://developer.android.com/develop/ui/compose/agentic/implement-components
source: md.txt
---

In the A2UI architecture, every surface is driven by a [component catalog](https://a2ui.org/concepts/catalogs/).
Rather than having an AI agent invent its own UI primitives or generate
arbitrary code, your catalog declares the components, property schemas, and
capabilities available to the agent. The agent then uses these components to
construct a user interface.

When you [build a custom catalog](https://developer.android.com/develop/ui/compose/agentic/manage-catalogs) for your app's design system, you
implement components that map those catalog definitions into concrete Jetpack
Compose UI elements. Each A2UI component (`A2uiComponent`) defines its property
schema contract, evaluates readiness as dynamic data arrives, binds reactive
properties from the data model, emits Compose UI, and dispatches user
interaction actions back to the agent.

The Compose UI renderer (`androidx.a2ui.compose:compose-ui`) provides the
interfaces and receiver scopes needed to implement custom components, which
follow your app's design system.

## Declare statically typed component properties

Before rendering, declare the properties that a component expects from the
agent. The runtime layer provides statically typed `A2uiProperty` APIs used
for both JSON schema generation and extracting values at runtime:

    // Define static properties, dynamic bindings, and component references
    val textProp = A2uiProperty.dynamicString("text", required = true)
    val variantProp = A2uiProperty.stringEnum("variant", enumValues = listOf("body", "title"))
    val childProp = A2uiProperty.componentId("child", required = true)
    val actionProp = A2uiProperty.action("action", required = true)

## Implement the A2uiComponent interface

Implement the `A2uiComponent` interface to define a component's schema and map
properties received from the agent onto Compose UI:

    object CustomTextComponent : A2uiComponent {
        private val textProp = A2uiProperty.dynamicString("text", required = true)
        private val variantProp = A2uiProperty.stringEnum(
            "variant",
            enumValues = listOf("body", "title"),
        )

        override val name = "Text"
        override val description = "Displays dynamic text."
        override val properties = listOf(textProp, variantProp)

        @Composable
        override fun A2uiComponentScope.isReady(properties: A2uiComponentProperties): Boolean {
            // The component does not become ready until dynamic text data arrives
            return properties.bind(textProp) != null
        }

        @Composable
        override fun A2uiComponentScope.Content(
            properties: A2uiComponentProperties,
            modifier: Modifier,
        ) {
            // Reactively resolve dynamic data binding and subscribe to updates
            val text = properties.bind(textProp) ?: ""

            // Read the static configuration property
            val variant = properties[variantProp] ?: "body"
            val textStyle = if (variant == "title") {
                MaterialTheme.typography.titleLarge
            } else {
                MaterialTheme.typography.bodyLarge
            }

            Text(
                text = text,
                style = textStyle,
                modifier = modifier,
            )
        }
    }

## Resolve regular and two-way data model bindings

Component implementations use `A2uiComponentScope` to resolve dynamically bound
properties. For regular dynamic properties, `bind` returns the current value and
automatically subscribes to data model updates.

For interactive input components, `bindUpdater` returns a stable updater lambda.
If the agent provided a literal string instead of a writable data path, the
updater lambda is `null`, signaling that the field is read-only:

    val labelProp = A2uiProperty.dynamicString("label", required = true)
    val valueProp = A2uiProperty.dynamicBoolean("value")

    @Composable
    fun A2uiComponentScope.CustomCheckbox(properties: A2uiComponentProperties) {
        // Read a dynamic property from the data model subscribing to updates
        val label = properties.bind(labelProp) ?: ""

        // Bind a property value and its updater to handle two-way data binding
        val checked = properties.bind(valueProp) ?: false
        val onCheckedChange = properties.bindUpdater(valueProp)

        Row(verticalAlignment = Alignment.CenterVertically) {
            Checkbox(
                checked = checked,
                onCheckedChange = onCheckedChange,
                enabled = (onCheckedChange != null), // Read-only if no writable path was bound
            )
            Text(text = label)
        }
    }

## Dispatch user actions to the agent

Interactive components use `A2uiComponentScope.dispatchAction` to send user
events back to the agent:

    object CustomButtonComponent : A2uiComponent {
        private val childProp = A2uiProperty.componentId("child", required = true)
        private val actionProp = A2uiProperty.action("action", required = true)

        override val name = "Button"
        override val description = "A clickable button."
        override val properties = listOf(childProp, actionProp)

        @Composable
        override fun A2uiComponentScope.Content(
            properties: A2uiComponentProperties,
            modifier: Modifier,
        ) {
            val actionDefinition = properties[actionProp]
            val childId = properties[childProp] ?: return
            val currentAction by rememberUpdatedState(actionDefinition)
            val onClick: () -> Unit = remember {
                { currentAction?.let { dispatchAction(it) } }
            }

            Button(onClick = onClick, modifier = modifier) {
                val childState = observeA2uiComponentState(id = childId)
                when (childState) {
                    is A2uiComponentState.Loading -> CircularProgressIndicator()
                    is A2uiComponentState.Error -> Text("Error")
                    is A2uiComponentState.Success -> A2uiComponent(childState.component)
                }
            }
        }
    }

## Handle child components and progressive rendering

Components supporting nested children use `observeA2uiComponentState(id)` to
observe child states. This enables progressive rendering where a parent
container renders its shell while child components load independently:

    val headerChildProp = A2uiProperty.componentId("headerId", required = true)

    @Composable
    fun A2uiComponentScope.CustomCompositeContent(
        properties: A2uiComponentProperties,
    ) {
        val headerId = properties[headerChildProp] ?: return

        val headerState = observeA2uiComponentState(id = headerId)
        when (headerState) {
            is A2uiComponentState.Loading -> {
                // Render a localized loading placeholder
                LinearProgressIndicator()
            }
            is A2uiComponentState.Error -> {
                // Render a localized error fallback
                Text("Failed to load header")
            }
            is A2uiComponentState.Success -> {
                // Forward the resolved child component to the visual UI router
                A2uiComponent(headerState.component)
            }
        }
    }

To handle collections or lists of children (such as items in a column, row, or
list), declare a property using `A2uiProperty.childList` and resolve the
children with `bindChildReferences`:

    val childrenProp = A2uiProperty.childList("children", required = true)

    @Composable
    fun A2uiComponentScope.CustomColumn(
        properties: A2uiComponentProperties,
        modifier: Modifier = Modifier,
    ) {
        // Resolve child references (supports both static ID arrays and dynamic data templates)
        val childReferences = properties.bindChildReferences(childrenProp) ?: return

        Column(modifier = modifier) {
            childReferences.forEach { reference ->
                key(reference.id, reference.baseDataPath) {
                    val childState = observeA2uiComponentState(reference)
                    when (childState) {
                        is A2uiComponentState.Loading -> CircularProgressIndicator()
                        is A2uiComponentState.Error -> Text("Failed to load child")
                        is A2uiComponentState.Success -> A2uiComponent(childState.component)
                    }
                }
            }
        }
    }

## Integrate native media rendering in the Basic Catalog

When using the provided Basic Catalog implementation
(`androidx.compose.material3:material3-a2ui`), you can plug your preferred media
libraries (such as Coil for images or ExoPlayer for video) into the Basic
Catalog's media components:

    // Configure an Image component for the Basic Catalog using Coil
    val coilImage = MaterialA2uiBasicCatalogV1Defaults.image { url, desc, scale, modifier, onError ->
        AsyncImage(
            model = url,
            contentDescription = desc,
            contentScale = scale,
            modifier = modifier,
            onError = { state -> onError(state.result.throwable) },
        )
    }

## Implementation details

The following sections explain recursive UI emission, dynamic property
evaluation, and error reporting.

The component implementation user journeys introduce the following key APIs:

- `A2uiComponent`: Interface defining component metadata, property schemas, readiness checks (`isReady`), and rendering emission (`Content`).
- `A2uiProperty`: A statically typed property declaration used for JSON schema generation and runtime value resolution.
- `A2uiComponentScope`: A receiver scope providing contextual capabilities (such as data binding, action dispatching, and child state observation) to component implementations.
- `A2uiComponentProperties`: A container for component properties received from the agent that provides type-safe property access.
- `A2uiComponentState`: Represents the reactive loading, success, or error resolution state of a component.

### Recursive UI emission and dynamic routing

The root state hoisted by the caller (or child component state resolved within a
parent) kicks off recursive component rendering through the `A2uiComponent`
composable function. Rather than tightly coupling the resolved state to a
specific UI implementation, this function acts as a dynamic router.