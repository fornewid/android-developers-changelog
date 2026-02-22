---
title: https://developer.android.com/topic/libraries/architecture/paging/v3-overview
url: https://developer.android.com/topic/libraries/architecture/paging/v3-overview
source: md.txt
---

# Paging library overview
Part of [Android Jetpack](https://developer.android.com/jetpack).

The Paging library helps you load and display pages of data from a larger
dataset from local storage or over a network. This approach lets your app use
both network bandwidth and system resources more efficiently. The components of
the Paging library are designed to fit into the recommended [Android app
architecture](https://developer.android.com/jetpack/docs/guide), integrate cleanly with other
[Jetpack](https://developer.android.com/jetpack) components, and provide first-class Kotlin support.

## Benefits of using the Paging library

The Paging library includes the following features:

- In-memory caching for your paged data. This helps ensure that your app uses system resources efficiently while working with paged data.
- Built-in request deduplication, which helps ensure that your app uses network bandwidth and system resources efficiently.
- Configurable [`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView) adapters that automatically request data as the user scrolls toward the end of the loaded data.
- First-class support for Kotlin coroutines and flows as well as [`LiveData`](https://developer.android.com/reference/kotlin/androidx/lifecycle/LiveData) and RxJava.
- Built-in support for error handling, including refresh and retry capabilities.

## Provide feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues
or have ideas for improving this library. Check the
[existing issues](https://issuetracker.google.com/issues?q=componentid:413106+status:open)
for this library before you create a new one. You can add your vote to an
existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=413106&template=1096385)

See the [Issue Tracker
documentation](https://developers.google.com/issue-tracker) for more
information about submitting feedback.

## Setup

To import Paging components into your Android app, add the following
dependencies to your app's `build.gradle` file:

### Groovy

```groovy
dependencies {
  def paging_version = "3.4.1"

  implementation "androidx.paging:paging-runtime:$paging_version"

  // alternatively - without Android dependencies for tests
  testImplementation "androidx.paging:paging-common:$paging_version"

  // optional - RxJava2 support
  implementation "androidx.paging:paging-rxjava2:$paging_version"

  // optional - RxJava3 support
  implementation "androidx.paging:paging-rxjava3:$paging_version"

  // optional - Guava ListenableFuture support
  implementation "androidx.paging:paging-guava:$paging_version"

  // optional - Jetpack Compose integration
  implementation "androidx.paging:paging-compose:3.4.1"
}
```

### Kotlin

```kotlin
dependencies {
  val paging_version = "3.4.1"

  implementation("androidx.paging:paging-runtime:$paging_version")

  // alternatively - without Android dependencies for tests
  testImplementation("androidx.paging:paging-common:$paging_version")

  // optional - RxJava2 support
  implementation("androidx.paging:paging-rxjava2:$paging_version")

  // optional - RxJava3 support
  implementation("androidx.paging:paging-rxjava3:$paging_version")

  // optional - Guava ListenableFuture support
  implementation("androidx.paging:paging-guava:$paging_version")

  // optional - Jetpack Compose integration
  implementation("androidx.paging:paging-compose:3.4.1")
}
```

## Library architecture

The Paging library's components operate in three
layers of your app:

- The repository layer
- The `ViewModel` layer
- The UI layer

![An image showing paged data flows from the PagingSource or RemoteMediator components in the repository layer to the Pager component in the ViewModel layer.
Then the Pager component exposes a Flow of PagingData to the
PagingDataAdapter in the UI layer.](https://developer.android.com/static/topic/libraries/architecture/images/paging3-library-architecture.svg) **Figure 1.** An example of how the Paging library fits into your app architecture.

This section describes the Paging library components that operate at each layer
and how they work together to load and display paged data.

### Repository layer

The primary Paging library component in the repository layer is
[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource). Each
`PagingSource` object defines a source of data and how to retrieve data from
that source. A `PagingSource` object can load data from any single source,
including network sources and local databases.

Another Paging library component that you might use is
[`RemoteMediator`](https://developer.android.com/reference/kotlin/androidx/paging/RemoteMediator). A
`RemoteMediator` object handles paging from a layered data source, such as a
network data source with a local database cache.

### ViewModel layer

The [`Pager`](https://developer.android.com/reference/kotlin/androidx/paging/Pager) component provides a
public API for constructing instances of `PagingData` that are exposed in
reactive streams, based on a `PagingSource` object and a
[`PagingConfig`](https://developer.android.com/reference/kotlin/androidx/paging/PagingConfig) configuration
object.

The component that connects the `ViewModel` layer to the UI is
[`PagingData`](https://developer.android.com/reference/kotlin/androidx/paging/PagingData). A `PagingData`
object is a container for a snapshot of paginated data. It queries a
[`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) object and
stores the result.

### UI layer

The primary Paging library component in the UI layer is
[`PagingDataAdapter`](https://developer.android.com/reference/kotlin/androidx/paging/PagingDataAdapter), a
[`RecyclerView`](https://developer.android.com/reference/kotlin/androidx/recyclerview/widget/RecyclerView)
adapter that handles paginated data.

Alternatively, you can use the included
[`AsyncPagingDataDiffer`](https://developer.android.com/reference/kotlin/androidx/paging/AsyncPagingDataDiffer)
component to build your own custom adapter.
| **Note:** If your app uses [Compose](https://developer.android.com/jetpack/compose) for its UI, use the [`androidx.paging:paging-compose`](https://developer.android.com/reference/kotlin/androidx/paging/compose/package-summary) artifact to integrate Paging with your UI layer instead. To learn more, see the API documentation for [`collectAsLazyPagingItems()`](https://developer.android.com/reference/kotlin/androidx/paging/compose/package-summary#collectaslazypagingitems).

## Additional resources

To learn more about the Paging library, see the following additional resources:

### Codelabs

- [Android Paging Basics codelab](https://developer.android.com/codelabs/android-paging-basics)
- [Android Paging Advanced codelab](https://codelabs.developers.google.com/codelabs/android-paging)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [Migrate to Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-migration)
- [Page from network and database](https://developer.android.com/topic/libraries/architecture/paging/v3-network-db)