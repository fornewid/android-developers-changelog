---
title: https://developer.android.com/develop/ui/compose/agentic/render-surfaces
url: https://developer.android.com/develop/ui/compose/agentic/render-surfaces
source: md.txt
---

When using the Jetpack Compose agent-to-UI (A2UI) renderer, an AI agent sends
messages that describe UI structures, component properties, and data updates.
To display these interfaces natively in your app, you host and render an
A2UI surface within your app's Jetpack Compose hierarchy.

The Compose A2UI renderer coordinates message parsing, reactive snapshot state
management, and animated surface state transitions. While the core renderer is
independent of any specific design system, it offers out-of-the-box integration
with Material Design 3 through the provided Basic Catalog.

## Initialize the Compose-backed data layer

The A2UI renderer supports snapshot-aware state in your app's data layer, which
lets your app's UI react to incremental updates from the agent. To add this
support, initialize the parser and processor using the `A2uiMessageParser` and
`A2uiMessageProcessor` factory functions in your [`ViewModel`](https://developer.android.com/reference/kotlin/androidx/lifecycle/ViewModel), as
shown in the following code snippet:

    class AgenticUiViewModel : ViewModel() {
        // Create a parser that leverages the built-in JSON parser.
        private val parser = A2uiMessageParser()

        // Create an A2UI message processor with your catalog and optional
        // action interceptor (implementing A2uiActionInterceptor).
        private val processor = A2uiMessageProcessor(
            // You can also use the provided Material catalog instead of
            // a custom one.
            catalogs = listOf(CustomDesignSystemCatalog)
        )

        // Expose active surfaces to the UI as a StateFlow.
        val a2uiSurfaces: StateFlow<List<A2uiSurfaceModel>> =
            processor.activeSurfaces

        init {
            // Collect messages on a background thread tied to the ViewModel lifecycle.
            viewModelScope.launch(Dispatchers.Default) {
                processor.collectMessages()
            }

            // Add support for two-way communication with the agent.
            viewModelScope.launch(start = CoroutineStart.UNDISPATCHED) {
                processor.outboundEvents.collect(::handleOutboundA2uiEvent)
            }
        }

        // Called by your app's networking layer or business logic whenever
        // a new A2UI protocol message arrives from the AI agent.
        fun onNetworkMessage(json: String) {
            processor.processInput(parser, json)
        }
    }

## Render surfaces using the Basic Catalog (Material 3)

When rendering surfaces using the provided Basic Catalog implementation
(`androidx.compose.material3:material3-a2ui`), you can render a fully styled
Material 3 surface, including built-in support for loading indicators, error
boundaries, and animated transitions. To do so, use the `A2uiSurface`
composable entry point:

    @Composable
    fun AgenticUiScreen(viewModel: AgenticUiViewModel) {
        // Observe active surfaces managed by the data layer.
        val surfaces by viewModel.a2uiSurfaces.collectAsStateWithLifecycle()

        Column(Modifier.fillMaxSize()) {
            surfaces.forEach { surface ->
                key(surface.id) {
                    A2uiSurface(
                        surfaceModel = surface,
                        // Add your surface's custom modifiers here.
                    )
                }
            }
        }
    }

## Handle surface states and animated transitions

`A2uiSurface` coordinates root component state resolution and applies
[`AnimatedContent`](https://developer.android.com/develop/ui/compose/animation/composables-modifiers#animatedcontent) transitions across loading, error, and success states:

    @Composable
    fun CustomStyledSurface(surface: A2uiSurfaceModel) {
        A2uiSurface(
            surfaceModel = surface,
            modifier = Modifier.fillMaxSize(),
            loadingContent = {
                Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                    CircularProgressIndicator()
                }
            },
            errorContent = { exception ->
                Text(
                    text = "Failed to load: ${exception.message}",
                    color = MaterialTheme.colorScheme.error,
                    // Add your custom error styling, such as modifiers, here.
                )
            },
            transitionSpec = {
                (fadeIn(animationSpec = tween(600)) togetherWith
                        fadeOut(animationSpec = tween(600)))
                    .using(SizeTransform(clip = false))
            },
        )
    }

## Low-level surface rendering with custom routers

> [!NOTE]
> **Note:** This customization is meant for apps that use alternative or custom design systems, as well as apps that otherwise require low-level control.

You can observe the surface root component state directly with
`observeA2uiComponentState` and delegate rendering to `A2uiComponent`:

    @Composable
    fun RawSurfaceCoordinator(surface: A2uiSurfaceModel) {
        // Extract the catalog to provide its readiness evaluator to the
        // composition. This lets components wait for their dynamic data bindings
        // before they're rendered.
        val coreSurface = surface as? A2uiCoreSurfaceModel
            ?: throw IllegalArgumentException(
                "Surface must implement A2uiCoreSurfaceModel")
        val composeCatalog = coreSurface.catalog as? A2uiCatalog
            ?: throw IllegalArgumentException("Catalog must implement A2uiCatalog")
        val readinessEvaluator = remember(composeCatalog) {
            composeCatalog.asReadinessEvaluator() }

        CompositionLocalProvider(
            LocalA2uiReadinessEvaluator provides readinessEvaluator
        ) {
            val rootState = observeA2uiComponentState(surface = surface)
            when (rootState) {
                is A2uiComponentState.Loading -> {
                    LoadingSpinner()
                }
                is A2uiComponentState.Error -> {
                    ErrorBanner(rootState.exception)
                }
                is A2uiComponentState.Success -> {
                    // Delegate component routing to the Compose A2UI router.
                    A2uiComponent(
                        component = rootState.component,
                        // Add your custom modifiers here.
                    )
                }
            }
        }
    }

## Implementation details

The agent-to-UI renderer handles surface state resolution and defensive error
boundaries.

### Defensive error boundaries and agent hallucination handling

Because A2UI surfaces are driven by generative LLM agents, incoming payloads can
be malformed or reference unknown component types.

The renderer establishes the following defensive boundaries to minimize the
likelihood of crashes:

- **Error dispatch for agent self-correction**: Errors are dispatched as outbound client messages, allowing the agent to self-correct in subsequent interaction turns. There's also an API that lets component implementations dispatch errors to the agent in cases where the API detects component-specific errors at render time.
- **Unknown components**: When an unrecognized component type is encountered, it's intercepted before reaching the UI tree, marked as an error state, and reported back to the agent for self-correction.
- **Schema validation failures** : Payloads are validated against component schemas (`A2uiSchema`). Malformed properties should never reach Compose UI layouts.
- **Sparse-array protection**: When very large list indexes are received, the data model transitions from a dense list to an adaptive sparse map, preventing out-of-memory errors.