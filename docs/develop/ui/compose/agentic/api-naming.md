---
title: https://developer.android.com/develop/ui/compose/agentic/api-naming
url: https://developer.android.com/develop/ui/compose/agentic/api-naming
source: md.txt
---

The Jetpack Compose A2UI renderer defines a layered architecture that lets you
choose the right layer to build on. In addition to semantic layering, a clear
naming scheme communicates API intent and controls visibility to avoid
polluting your classpath with unnecessary internal types.

APIs are organized into two primary categories based on use case and visibility:

1. **APIs for app and component developers** : Public APIs intended for direct use have clean, concise names with the `A2ui` prefix (or design-system and testing prefixes such as `MaterialA2ui` and `A2uiTest`). Examples include `A2uiCatalog`, `A2uiComponent`, and `A2uiException`.
2. **APIs for UI framework integrators** : APIs used by libraries bridging the core data layer and UI frameworks have descriptive names prefixed with `A2uiCore`. These APIs aren't intended for direct application reference and remain hidden from standard application code. Examples include `A2uiCoreCatalog`, `A2uiCoreDataModel`, and `A2uiCoreSurfaceModel`.

Because the core data layer contains types from both categories, it's
distributed across two separate artifacts: `androidx.a2ui:a2ui-model` (for app
developers) and `androidx.a2ui:a2ui-engine` (for framework integrators). This
structure allows framework libraries to depend on `a2ui-engine` as an
implementation dependency, preventing `A2uiCore` types from polluting public app
classpaths.

## Category 1: App developer APIs

The following tables list public APIs intended for application and component
developers.

### androidx.a2ui:a2ui-model

| Type | Description |
|---|---|
| `A2uiSurfaceModel` | Read-only interface representing a UI surface |
| `A2uiMessageProcessor` | Entry-point type for processing incoming messages |
| `A2uiMessageParser` | Parser interface for protocol messages |
| `A2uiServerToClientMessage` | Incoming message payload |
| `A2uiSchema` | Types used to define component property schemas |
| `A2uiException` | Exceptions thrown and handled across layers |
| `A2uiUserAction` | Action payload created as a result of user interactions |
| `A2uiClientToServerMessage` | Base type for all outbound message payloads |
| `A2uiActionInterceptor` | Data-layer-level user action interceptor |
| `A2uiFunctionDefinition` | Definition of a local client function |
| `A2uiDataPath` | JSON pointer path representation |

### androidx.a2ui.compose:compose-runtime

| Type | Description |
|---|---|
| `a2uiRuntimeMessageProcessor` | Extension constructor for the message processor |
| `A2uiMessageParser` | Extension constructor for the message parser |
| `A2uiComponentState` | Interface representing reactive component state |
| `A2uiComponentModel` | Data model for a successfully resolved component |
| `A2uiComponentProperties` | Stable property container optimizing recompositions |
| `A2uiProperty` | Strongly typed component property definition |
| `A2uiComponentScope` | Receiver scope for evaluating bindings and child components |
| `A2uiComponentReference` | Pointer for resolving nested child components |

### androidx.a2ui.compose:compose-ui

| Type | Description |
|---|---|
| `A2uiCatalog` | Interface and extension constructor for defining catalogs |
| `A2uiComponent` | Interface for defining Compose component implementations |
| `A2uiComponent` (composable) | Composable function that emits UI for a component |

### androidx.compose.material3:material3-a2ui

| Type | Description |
|---|---|
| `A2uiSurface` | Composable entry point that renders a surface |
| `materialA2uiBasicCatalogV1` | Factory function for creating an instance of the Basic Catalog that uses Material 3 components |
| `MaterialA2uiBasicCatalogV1Defaults` | Default Material 3 implementations of the Basic Catalog |

### androidx.a2ui.compose:compose-ui-testing

| Type | Description |
|---|---|
| `A2uiTestController` | Test controller for orchestrating test execution |
| `A2uiComponentStub` | Stubbed or overridden component implementation |
| `A2uiTestSurface` | Composable function that renders a test surface |

## Category 2: Framework integrator APIs

The following table lists APIs intended for framework integrators.

### androidx.a2ui:a2ui-engine

| Type | Description |
|---|---|
| `A2uiCoreCatalog` | Contains a set of `A2uiCoreComponentDefinition` objects |
| `A2uiCoreCatalogSerializer` | Serializer for A2UI catalogs |
| `A2uiCoreComponentDefinition` | Contains metadata defining a component |
| `A2uiCoreSurfaceModel` | Implements `A2uiSurfaceModel`, exposes registries |
| `A2uiCoreSurfaceGroupModel` | Implements `A2uiSurfaceGroupModel` |
| `A2uiCoreMessageProcessor` | Implements `A2uiMessageProcessor` |
| `A2uiCoreDataModel` | Reactive data model holder |
| `A2uiCoreComponentRegistry` | Component registry |
| `A2uiCoreValueResolver` | Data accessor for use in the dynamic evaluator |
| `A2uiCoreSchemaValidator` | Component schema validator |