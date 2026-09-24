---
title: https://developer.android.com/develop/ui/compose/agentic/manage-catalogs
url: https://developer.android.com/develop/ui/compose/agentic/manage-catalogs
source: md.txt
---

In the A2UI architecture, every surface is driven by a [component catalog](https://a2ui.org/concepts/catalogs/).
A catalog is a formal contract that defines the UI components, property
schemas, and local client functions available to an AI agent. Rather than
generating arbitrary code or inventing unknown elements, the agent must
construct user interfaces using exclusively the components declared in the
catalog.

In other words: the catalog declares the components, and the agent uses
them to build your app's UI.

When building an Android app with the Jetpack Compose A2UI renderer, you have
flexible options for how you provide catalogs:

- **The Basic Catalog** : The A2UI project defines a standardized, general-purpose specification called the [Basic Catalog](https://a2ui.org/concepts/catalogs/#the-basic-catalog), which includes common elements like buttons, text, text fields, cards, and lists. The AndroidX library `androidx.compose.material3:material3-a2ui` provides an out-of-the-box implementation of this Basic Catalog specification using native Material Design 3 components. The `androidx.a2ui.compose:compose-ui` library also provides a generic schema definition for the Basic Catalog, which helps you implement the Basic Catalog for your own design system.
- **Custom catalogs**: For production applications with their own distinct design systems, you can build a custom catalog from scratch. This restricts the agent to the exact components, styling tokens, and visual language of your app.
- **A subset or hybrid**: You can combine specific component implementations from the provided Basic Catalog with your own custom components, or override individual component implementations within the Basic Catalog suite.

## Use the provided Basic Catalog

To get started quickly without authoring a component schema from scratch, you
can use the provided implementation of the [A2UI Basic Catalog
specification](https://a2ui.org/concepts/catalogs/#the-basic-catalog). The `androidx.compose.material3:material3-a2ui` library
implements the Basic Catalog using Material Design 3 components.

When you instantiate `materialA2uiBasicCatalogV1`, supply renderers
and handlers for the following:

- Media components, such as images, video, and audio players
- URL opener
- Localized message formatting

The A2UI libraries intentionally don't bundle external media and networking
dependencies, such as Coil, Glide, or Media3. Instead, you provide your own
renderers. This prevents dependency conflicts by providing unique libraries. For
example, if your app already uses Coil for image loading or
Media3 for playback, you can plug those existing libraries directly into the
catalog.

The following example demonstrates how to instantiate the Basic Catalog and
wire up your preferred media libraries, URL opener, and message formatter:

    // Instantiate the provided Basic Catalog (implemented with Material 3)
    val basicCatalog = materialA2uiBasicCatalogV1(
        // Example: Wire up Coil for image loading (via AsyncImage)
        image = MaterialA2uiBasicCatalogV1Defaults.image {
                url, description, scale, modifier, onError ->
            AsyncImage(
                model = url,
                contentDescription = description,
                contentScale = scale,
                modifier = modifier,
                onError = { state -> onError(state.result.throwable) },
            )
        },

        // Example: Use ExoPlayer/Media3 for video
        video = MaterialA2uiBasicCatalogV1Defaults.video { url, modifier, onError ->
            // Custom ExoPlayer video integration here
        },

        // Example: Use an audio player
        audioPlayer = MaterialA2uiBasicCatalogV1Defaults.audioPlayer {
                url, description, modifier, onError ->
            // Custom audio integration here
        },

        // Handle outbound URLs, such as using an app navigator or context intents.
        urlOpener = { url ->
            appNavigator.openUrl(url)
        },

        // Handle localized message formatting
        messageFormatter = { pattern, locale, args ->
            MessageFormat.format(context, locale, pattern, args)
        },
        localeProvider = A2uiLocaleProvider.Default,
    )

## Assemble a custom component catalog from scratch

If your app uses a custom design system, you can define your own catalog
containing your own [custom `A2uiComponent` implementations](https://developer.android.com/develop/ui/compose/agentic/implement-components). This approach
gives you full control over the component schemas exposed to the agent and the
native Compose UI emitted:

    // Define a custom catalog that mirrors your app's design system
    val CustomDesignSystemCatalog = A2uiCatalog(
        catalogId = "https://example.com/catalogs/my-design-system/v1/catalog.json",
        components = listOf(
            CustomButtonComponent,
            CustomCardComponent,
            CustomTextFieldComponent,
        ),
        functions = listOf(MyCustomLocalFunction()),
    )

For instructions on defining individual component schemas and their Compose UI
rendering logic, see [Implement custom A2UI components](https://developer.android.com/develop/ui/compose/agentic/implement-components).

## Use a subset of Basic Catalog components with custom components

You don't have to choose strictly between building everything from scratch or
adopting the entire Basic Catalog. You can assemble a catalog that combines
select components from the provided Basic Catalog implementation with your own
custom components:

    // Assemble a catalog using select Basic Catalog components alongside custom components
    val hybridCatalog = A2uiCatalog(
        catalogId = "https://example.com/catalogs/my-app/v1/catalog.json",
        components = listOf(
            // Use provided Basic Catalog components (built with Material 3)
            MaterialA2uiBasicCatalogV1Defaults.text,
            MaterialA2uiBasicCatalogV1Defaults.card,

            // Add proprietary components from your app's design system
            CustomChartComponent,
            CustomProductCardComponent,
        ),
        functions = createBasicCatalogFunctions(...),
    )

Alternatively, you can customize the provided Basic Catalog suite by
overriding specific component slots:

    // Override specific components within the Basic Catalog suite
    val customizedBasicCatalog = materialA2uiBasicCatalogV1(
        // Supply required renderers (such as Coil or ExoPlayer) as shown earlier
        image = MaterialA2uiBasicCatalogV1Defaults.image(myImageRenderer),
        video = MaterialA2uiBasicCatalogV1Defaults.video(myVideoRenderer),
        audioPlayer = MaterialA2uiBasicCatalogV1Defaults
            .audioPlayer(myAudioRenderer),
        urlOpener = { url -> /* Open URL */ },
        messageFormatter = { pattern, _, _ -> pattern },
        localeProvider = A2uiLocaleProvider.Default,
        // Replaces the default button. If you use this, implement the
        // A2uiBasicCatalogV1.Button interface.
        button = MyCustomBrandButtonComponent,
        
    )

## Manage catalog versioning and schema evolution

A2UI catalogs are explicitly versioned based on their JSON schema contract. A
version bump is required when introducing breaking schema changes:

    // Original component (v1 catalog)
    object CustomButtonComponent : A2uiComponent { ... }

    // Unchanged component across versions
    object CustomTextComponent : A2uiComponent { ... }

    // Future breaking schema change (v2 catalog)
    object CustomButtonComponentV2 : A2uiComponent { ... }

    // Assembles the v1 catalog
    fun customCatalogV1(
        button: A2uiComponent = CustomButtonComponent,
        text: A2uiComponent = CustomTextComponent,
    ): A2uiCatalog = A2uiCatalog(
        catalogId = "https://example.com/catalogs/my-app/v1/catalog.json",
        components = listOf(button, text),
    )

    // Assembles the v2 catalog
    fun customCatalogV2(
        button: A2uiComponent = CustomButtonComponentV2,
        text: A2uiComponent = CustomTextComponent,
    ): A2uiCatalog = A2uiCatalog(
        catalogId = "https://example.com/catalogs/my-app/v2/catalog.json",
        components = listOf(button, text),
    )

To enable seamless migrations without downtime, your client can register
multiple supported catalog versions with the message processor simultaneously:

    private val processor = A2uiMessageProcessor(
        catalogs = listOf(
            customCatalogV1(),
            customCatalogV2(),
        ),
    )

During [catalog negotiation](https://a2ui.org/concepts/catalogs/#catalog-negotiation), the agent discovers all supported catalog IDs
and targets the appropriate version for each surface.

## Implementation details

The following sections explain internal catalog validation and schema
negotiation.

The catalog management user journeys introduce the following key APIs:

- `A2uiCatalog`: Interface and top-level factory function for defining component catalogs.
- `materialA2uiBasicCatalogVX`: Versioned factory functions (such as `materialA2uiBasicCatalogV1`) that provide the Material 3 implementation of the standard A2UI Basic Catalog specification.
- `A2uiReadinessEvaluator` and `asReadinessEvaluator()`: `A2uiReadinessEvaluator` is the interface for evaluating component readiness. The `asReadinessEvaluator()` extension function resolves readiness states using the components registered in a catalog.

### A2UI version catalog and component schemas

A catalog schema definition is associated with a specific protocol version.
When the protocol evolves, the catalog definition advances its version.
Component implementations for this next version can use updated renderer APIs
while lower versions remain operational side by side.