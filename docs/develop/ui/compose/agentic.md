---
title: https://developer.android.com/develop/ui/compose/agentic
url: https://developer.android.com/develop/ui/compose/agentic
source: md.txt
---

The Jetpack Compose agent-to-UI (A2UI) renderer provides an implementation of
the [A2UI protocol](https://a2ui.org/), enabling AI agents to generate rich, interactive
user interfaces that render native Compose components---without executing
arbitrary code. This library maps the A2UI JSON protocol to Compose
primitives while adhering to [idiomatic state management](https://developer.android.com/develop/ui/compose/state) and providing
fine-grained reactivity based on the Compose Snapshot state system.

The Compose A2UI renderer library offers the following capabilities:

- **High-performance reactivity** ([`androidx.a2ui.compose:compose-runtime`](https://developer.android.com/jetpack/androidx/releases/a2ui-compose)): Delivers fine-grained UI updates by leveraging the Compose Snapshot state system, ensuring that only the specific components affected by streaming agent updates or user interactions are recomposed.
- **Flexible component APIs and customization** ([`androidx.a2ui.compose:compose-ui`](https://developer.android.com/jetpack/androidx/releases/a2ui-compose)): Provides a structured pattern for defining catalogs of component implementations that map JSON protocol schemas to your native Compose UI. This lets you build components that support progressive rendering, custom loading states of subcomponents, animated transitions, and two-way data bindings that can send data back to the agent.
- **Design-system agnostic core** : Keeps the runtime and UI rendering layers independent of any specific design system, enabling you to build custom catalogs for your app's design system or adopt the provided [Basic Catalog](https://a2ui.org/specification/v0.9.1-basic-catalog-implementation-guide/).
- **Graceful handling of AI hallucinations** ([`androidx.a2ui:a2ui-model`](https://developer.android.com/jetpack/androidx/releases/a2ui) and [`androidx.a2ui:a2ui-engine`](https://developer.android.com/jetpack/androidx/releases/a2ui)): Provides schema validation to intercept malformed payloads before they reach the state models, graceful error handling through component error states, and automatic error reporting to an agent for self-correction.
- **Built-in Basic Catalog** ([`androidx.compose.material3:material3-a2ui`](https://developer.android.com/jetpack/androidx/releases/compose-material3#compose_material3_a2ui_version_10_2)): Provides a ready-to-use Basic Catalog implementation using Material 3 components, supporting progressive rendering and Material theming on top of the Compose renderer.

<br />

## High-level architecture

Every A2UI interface is driven by a [component catalog](https://a2ui.org/concepts/catalogs/). Rather than having
an agent generate arbitrary UI code or invent unregistered components, the
catalog acts as a contract that defines the specific UI elements, properties,
and functions available to the agent. The catalog declares the components; the
agent uses them to construct user interfaces.

To support this model, the Compose A2UI renderer separates the core,
design-system-agnostic rendering engine from concrete catalog implementations
across the Jetpack artifacts described earlier, and provides dedicated testing
APIs in [`androidx.a2ui.compose:compose-ui-testing`](https://developer.android.com/jetpack/androidx/releases/a2ui-compose).

## Protocol evolution and API compatibility

The Compose A2UI renderer currently supports **version 0.9.1** of the
[A2UI specification](https://a2ui.org/specification/v0.9.1-a2ui/).

The UI (`androidx.a2ui.compose:compose-ui`) and runtime layers
(`androidx.a2ui.compose:compose-runtime`) provide an API surface for your
apps and component catalogs, while the underlying data layer
(`androidx.a2ui:a2ui-model` and `androidx.a2ui:a2ui-engine`) manages
protocol-version-specific parsing and message processing. Because these
libraries are part of AndroidX, strict binary compatibility rules apply. For
example, after the public API reaches the stable version 1.0.0, there are no
breaking changes to public API surfaces, such as classes and interfaces.

The Compose A2UI renderer uses the following strategies to support protocol
evolution.

### Evolve the UI and runtime renderer APIs

As the A2UI protocol evolves or adds new capabilities, the renderer APIs support
those changes through the following approaches:

- **Non-breaking API additions** : When a new capability is introduced, it becomes part of a core public interface (such as `A2uiComponent` or `A2uiCatalog`) with a default implementation. This lets your app's components continue to compile and function without modification.
- **Breaking changes cause older interfaces to become deprecated** : If a future protocol update introduces an incompatible change, old incompatible interfaces (such as `A2uiComponent`) are deprecated, and new interfaces, such as `A2uiComponentV2`, are introduced and supported alongside them.

### Version catalog and component schemas

A catalog schema definition is associated with a specific protocol version.
When the protocol evolves, the catalog definition evolves accordingly and
advances its version. Component implementations for this "next" version can use
the updated renderer APIs.

To help enable seamless migrations, your client can [declare multiple supported
catalog versions](https://developer.android.com/develop/ui/compose/agentic/manage-catalogs#declare-supported-versions), which the agent gets during the capability negotiation
phase.