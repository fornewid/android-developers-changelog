---
title: https://developer.android.com/develop/ui/compose/agentic/testing
url: https://developer.android.com/develop/ui/compose/agentic/testing
source: md.txt
---

The `androidx.a2ui.compose:compose-ui-testing` testing library provides testing
APIs that use a controller pattern idiomatic to Jetpack testing libraries, such
as Navigation's `TestNavHostController`.

Unlike standard Jetpack Compose components that take static parameters and emit
UI, A2UI components are contextual. They rely on `A2uiComponentScope` to
evaluate dynamic data bindings, dispatch outbound actions to the agent, write
back to two-way data bindings, and inflate dynamic child templates.

The testing APIs simplify test setup while provisioning real
`A2uiMessageProcessor` instances, running their coroutines bound to the Compose
test environment.

## Isolated components

You can verify that an individual component resolves its data, dispatches
actions, and renders correctly within your design system theme:

    @Test
    fun button_resolvesStubChildAndDispatchesAction() = runComposeUiTest {
        // 1. Create the test controller
        val controller = A2uiTestController(
            // Provide a catalog containing the component under test
            catalog = CustomComponentCatalog,
            // Configure the component under test with concrete properties
            initialComponents = listOf(
                A2uiComponentPayload(
                    id = "root",
                    type = "Button",
                    properties = mapOf(
                        "child" to "btn_text",
                        "variant" to "primary",
                        "action" to mapOf(
                            "event" to mapOf(
                                "name" to "submit_form",
                                "context" to mapOf("username" to mapOf("path" to "/user/name")),
                            ),
                        ),
                    ),
                ),
                A2uiComponentPayload("btn_text"),
            ),
            // Stub the required child component
            componentStubs = listOf(
                A2uiComponentStub.withId("btn_text") { _, modifier ->
                    Text("Submit", modifier = modifier)
                },
            ),
            // Provide initial dynamic data
            initialData = mapOf("user" to mapOf("name" to "Test User")),
        )

        // 2. Start background processing and initialize the surface
        val surface = controller.start()

        // 3. Mount the UI
        setContent {
            A2uiTestSurface(surface)
        }

        // 4. Interact using standard Compose UI semantics
        onNodeWithText("Submit").performClick()

        // 5. Wait for Compose and A2UI background processes to settle
        waitForIdle()
        controller.waitForIdle()

        // 6. Assert outbound actions were correctly evaluated and intercepted
        val action = controller.dispatchedActions.single() as A2uiEventAction
        assertEquals("submit_form", action.eventName)
        assertEquals("Test User", action.context["username"])
    }

## Surface states

You can test surface hosts such as `A2uiSurface`, including their states
and transitions:

    @Test
    fun surface_displaysLoading_thenTransitionsToContent() = runComposeUiTest {
        // 1. Create an empty controller to simulate a pending network request
        val controller = A2uiTestController(
            catalog = CustomComponentCatalog,
            // Pre-register a stub for the expected root component type
            componentStubs = listOf(
                A2uiComponentStub.withType("RootLayout") { _, modifier ->
                    Text("Content Ready", modifier = modifier)
                },
            ),
        )
        val surface = controller.start()

        // 2. Mount the surface UI
        setContent {
            A2uiSurface(surfaceModel = surface)
        }

        // 3. Assert the loading placeholder is active
        onNode(hasProgressBarRangeInfo(ProgressBarRangeInfo.Indeterminate)).assertExists()

        // 4. Simulate the agent pushing the layout payload over the network
        controller.updateComponent(
            id = "root",
            type = "RootLayout",
            properties = emptyMap(),
        )

        // 5. Wait for the data layer and animation to settle
        controller.waitForIdle()
        waitForIdle()

        // 6. Assert the loading state is gone and content is visible
        onNode(hasProgressBarRangeInfo(ProgressBarRangeInfo.Indeterminate)).assertDoesNotExist()
        onNodeWithText("Content Ready").assertIsDisplayed()
    }

## Two-way binding

You can test components like text fields that write back to the data model
during user input and verify reactive updates when the agent mutates the data
model:

    @Test
    fun textField_writesToDataModelAndReactsToAgent() = runComposeUiTest {
        val controller = A2uiTestController(
            catalog = CustomComponentCatalog,
            initialComponents = listOf(
                A2uiComponentPayload(
                    id = "root",
                    type = "TextField",
                    properties = mapOf(
                        "label" to "Username",
                        "value" to mapOf("path" to "/form/username"),
                    ),
                ),
            ),
            initialData = mapOf("form" to mapOf("username" to "Initial")),
        )
        val surface = controller.start()

        setContent {
            A2uiTestSurface(surface)
        }

        // 1. User interaction updates the global DataModel locally
        onNodeWithText("Initial").performTextReplacement("LocallyTyped")
        waitForIdle()

        // 2. Assert the component wrote back to the DataModel
        assertEquals("LocallyTyped", controller.getData<String>("/form/username"))

        // 3. Simulate the agent pushing a data update for the same path
        controller.updateData("/form/username", "ServerOverridden")
        controller.waitForIdle()

        // 4. Assert the component reactively updated the UI
        onNodeWithText("ServerOverridden").assertIsDisplayed()
    }

## Components with templated children

You can test components designed to display collections of children defined
using A2UI `ChildList` templates:

    @Test
    fun column_rendersDynamicChildTemplates() = runComposeUiTest {
        val controller = A2uiTestController(
            catalog = CustomComponentCatalog,
            initialData = mapOf(
                "catalog" to mapOf(
                    "products" to listOf(
                        mapOf("title" to "Camera"),
                        mapOf("title" to "Laptop"),
                    ),
                ),
            ),
            initialComponents = listOf(
                A2uiComponentPayload(
                    id = "root",
                    type = "Column",
                    properties = mapOf(
                        "children" to mapOf(
                            "path" to "/catalog/products",
                            "componentId" to "product_template",
                        ),
                    ),
                ),
                // Bind the initial properties for the dynamically instantiated
                // template stub.
                A2uiComponentPayload(
                    id = "product_template",
                    properties = mapOf("title" to mapOf("path" to "title")),
                ),
            ),
            componentStubs = listOf(
                A2uiComponentStub.withId(id = "product_template") { props, modifier ->
                    val titleProp = remember { A2uiProperty.dynamicString("title") }
                    val title = props.bind(titleProp) ?: "Unknown"
                    Text(text = "Stubbed: $title", modifier = modifier)
                },
            ),
        )
        val surface = controller.start()
        setContent { A2uiTestSurface(surface) }

        // Verify the template was instantiated twice with relative data
        onNodeWithText("Stubbed: Camera").assertExists()
        onNodeWithText("Stubbed: Laptop").assertExists()

        // Simulate appending a new item to the data model array
        controller.updateData("/catalog/products/-", mapOf("title" to "Tablet"))
        controller.waitForIdle()

        // Verify the Column dynamically instantiated a new child stub
        onNodeWithText("Stubbed: Tablet").assertExists()
    }

## Error fallbacks for agent errors

You can verify that surfaces and components handle agent errors, such as
hallucinations, gracefully:

    @Test
    fun surface_displaysErrorFallback_onAgentHallucination() = runComposeUiTest {
        val controller = A2uiTestController(catalog = CustomComponentCatalog)
        val surface = controller.start()

        // 1. Mount the surface orchestrator with error boundaries
        setContent { A2uiSurface(surfaceModel = surface) }

        // 2. Simulate an agent hallucinating a broken component layout
        controller.failComponent(
            id = "root",
            exception = A2uiException.A2uiValidationException(
                message = "HallucinatedType",
                path = "/components/root"
            ),
        )
        controller.waitForIdle()

        // 3. Assert the surface displayed the fallback error state
        onNodeWithText("Failed to load: HallucinatedType").assertIsDisplayed()

        // 4. Assert the core layer dispatched an error to the server
        val errorMsg = controller.outboundErrors.single()
        assertEquals("VALIDATION_FAILED", errorMsg.code)
    }

## Progressive rendering

You can test intermediate states where a parent component has loaded but child
components are still pending:

    @Test
    fun progressiveRendering_parentRendersWhileChildIsPending() = runComposeUiTest {
        // 1. Mount the parent, omitting the child instance
        val controller = A2uiTestController(
            catalog = CustomComponentCatalog,
            initialComponents = listOf(
                A2uiComponentPayload(
                    id = "root",
                    type = "Button",
                    properties = mapOf(
                        "child" to "delayed_text_id",
                        "action" to mapOf("event" to mapOf("name" to "click")),
                    ),
                ),
            ),
        )
        val surface = controller.start()
        setContent {
            A2uiTestSurface(surface)
        }

        // 2. Initial state: parent is rendered, child displays loading state
        onNodeWithText("Submit").assertDoesNotExist()
        onNode(hasProgressBarRangeInfo(ProgressBarRangeInfo.Indeterminate)).assertExists()

        // 3. Simulate arrival of the child component
        controller.updateComponent(
            id = "delayed_text_id",
            type = "Text",
            properties = mapOf("text" to "Submit"),
        )
        controller.waitForIdle()

        // 4. Assert that progressive rendering completed
        onNode(hasProgressBarRangeInfo(ProgressBarRangeInfo.Indeterminate)).assertDoesNotExist()
        onNodeWithText("Submit").assertIsDisplayed()
    }

## Implementation details

The following sections explain component overrides, schema validation, and
coroutine synchronization in the test framework.

The testing library introduces the following primary APIs:

- `A2uiTestController`: Extension constructor functions and main test controller interface.
- `A2uiComponentStub`: Stubs and overrides for child and catalog components.
- `A2uiTestSurface`: A lightweight composable utility that mounts a test surface.

### Component overrides versus standard mocking

To eliminate heavy third-party mocking frameworks, child components and external
dependencies are bypassed using UI stubs (`A2uiComponentStub`).
`A2uiComponentStub.withId` intercepts a specific component instance by ID, while
`A2uiComponentStub.withType` overrides rendering for an entire catalog type.

### Fail-fast schema validation

The test framework enforces the A2UI protocol contract synchronously. When the
controller initializes or updates components, it runs `A2uiCoreSchemaValidator`
against provided payloads. If an invalid property is set, such as a missing
required field or type mismatch, the test crashes immediately with an
`A2uiValidationException`.

### Coroutine synchronization

`A2uiTestController.start` hooks into the test coroutine context
provided by `runComposeUiTest()`. It extracts `currentCoroutineContext()`, maps
background loops to a detached `Job`, and automatically cancels itself when the
test block completes, preventing dangling test executions. `waitForIdle()`
waits for all pending background coroutines to finish.