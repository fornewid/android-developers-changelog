---
title: https://developer.android.com/topic/libraries/architecture/saving-states
url: https://developer.android.com/topic/libraries/architecture/saving-states
source: md.txt
---

This guide discusses user expectations about UI state, and the options available
for preserving state.

Saving and restoring an activity's UI state quickly after the
system destroys activities or applications is essential for a good user
experience. Users expect the UI state to stay the same, but the system might
destroy the activity and its stored state.

To bridge the gap between user expectations and system behavior, use a
combination of the following methods:

- [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) objects.
- Saved instance states within the following contexts:
  - Jetpack Compose: [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)).
  - Views: [`onSaveInstanceState()`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) API.
  - ViewModels: [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate).
- Local storage to persist the UI state during app and activity transitions.

The optimal solution depends on your UI data's complexity, your app's use
cases, and finding a balance between data access speed and memory use.

Make sure your app meets users' expectations and offers a fast, responsive
interface. Avoid delays when loading data into the UI, particularly after common
configuration changes like rotation.

## User expectations and system behavior

Depending upon the action a user takes, they either expect that activity state
to be cleared or the state to be preserved. In some cases the system
automatically does what is expected by the user. In other cases the system does
the opposite of what the user expects.

### User-initiated UI state dismissal

The user expects that when they start an activity, the transient UI state of
that activity remains the same until the user completely dismisses the activity.
The user can completely dismiss an activity by doing the following:

- Swiping the activity off of the Overview (Recents) screen.
- Killing or force-quitting the app from the Settings screen.
- Rebooting the device.
- Completing some sort of "finishing" action (which is backed by `Activity.finish()`).

The user's assumption in these complete dismissal cases is that they have
permanently navigated away from the activity, and if they re-open the activity
they expect the activity to start from a clean state. The underlying system
behavior for these dismissal scenarios matches the user expectation - the
activity instance will get destroyed and removed from memory, along with any
state stored in it and any saved instance state record associated with the
activity.

There are some exceptions to this rule about complete dismissal---for example a
user might expect a browser to take them to the exact webpage they were looking
at before they exited the browser using the back button.

### System-initiated UI state dismissal

A user expects an activity's UI state to remain the same throughout a
configuration change, such as rotation or switching into multi-window mode.
However, by default the system destroys the activity when such a configuration
change occurs, wiping away any UI state stored in the activity instance. To
learn more about device configurations, see the
[Configuration reference page](https://developer.android.com/reference/android/content/res/Configuration#lfields). Note, it is possible (though not recommended)
to override the default behavior for configuration changes. See [Handling the
configuration change yourself](https://developer.android.com/guide/topics/resources/runtime-changes#HandlingTheChange) for more details.

A user also expects your activity's UI state to remain the same if they
temporarily switch to a different app and then come back to your app later. For
example, the user performs a search in your search activity and then presses the
home button or answers a phone call - when they return to the search activity
they expect to find the search keyword and results still there, exactly as
before.

In this scenario, your app is placed in the background the system does its best
to keep your app process in memory. However, the system may destroy the
application process while the user is away interacting with other apps. In such
a case, the activity instance is destroyed, along with any state stored in it.
When the user relaunches the app, the activity is unexpectedly in a clean state.
To learn more about process death, see [Processes and Application Lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle).

## Options for preserving UI state

When the user's expectations about UI state don't match default system
behavior, you must save and restore the user's UI state to ensure that the
system-initiated destruction is transparent to the user.

Each of the options for preserving UI state vary along the following dimensions
that impact the user experience:

|   | ViewModel | Saved instance state | Persistent storage |
|---|---|---|---|
| Storage location | in memory | in memory | on disk or network |
| Survives configuration change | Yes | Yes | Yes |
| Survives system-initiated process death | No | Yes | Yes |
| Survives user complete activity dismissal/onFinish() | No | No | Yes |
| Data limitations | complex objects are fine, but space is limited by available memory | only for primitive types and simple, small objects such as String | only limited by disk space or cost / time of retrieval from the network resource |
| Read/write time | quick (memory access only) | slow (requires serialization/deserialization) | slow (requires disk access or network transaction) |

| **Note:** Saved instance state in the above table includes the `onSaveInstanceState()` and `rememberSaveable` APIs, and `SavedStateHandle` as part of ViewModels.

## Use ViewModel to handle configuration changes

ViewModel is ideal for storing and managing UI-related data while the user is
actively using the application. It allows quick access to UI data and helps you
avoid refetching data from network or disk across rotation, window resizing, and
other commonly occurring configuration changes. To learn how to implement a
ViewModel, see the [ViewModel guide](https://developer.android.com/topic/libraries/architecture/viewmodel).

ViewModel retains the data in memory, which means it is cheaper to retrieve than
data from the disk or the network. A ViewModel is associated with an activity
(or some other lifecycle owner) - it stays in memory during a configuration
change and the system automatically associates the ViewModel with the new
activity instance that results from the configuration change.

ViewModels are automatically destroyed by the system when your user backs out of
your activity or fragment or if you call `finish()`, which means the state is
cleared as the user expects in these scenarios.

Unlike saved instance state, ViewModels are destroyed during a system-initiated
process death. To reload data after a system-initiated process death in a
ViewModel, use the [`SavedStateHandle` API](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate). Alternatively, if the data is
related to the UI and doesn't need to be held in the ViewModel, use
`onSaveInstanceState()` in the View system or `rememberSaveable` in Jetpack
Compose. If the data is *application data*, then it might be better to persist
it to disk.

If you already have an in-memory solution in place for storing your UI state
across configuration changes, you may not need to use ViewModel.

## Use Saved instance state as backup to handle system-initiated process death

The [`onSaveInstanceState()`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle)) callback in the View system,
[`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)) in Jetpack Compose, and [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate) in
ViewModels store data needed to reload the state of a UI controller, such as an
activity or a fragment, if the system destroys and later recreates that
controller. To learn how to implement saved instance state using
`onSaveInstanceState`, see *Saving and restoring activity state* in the
[Activity Lifecycle guide](https://developer.android.com/guide/components/activities/activity-lifecycle#asem).

Saved instance state bundles persist through both configuration changes and
process death but are limited by storage and speed, because the different APIs
serialize data. Serialization can consume a lot of memory if the objects being
serialized are complicated. Because this process happens on the main thread
during a configuration change, long-running serialization can cause dropped
frames and visual stutter.
| **Key Point:** Saved instance state APIs only save data written to it when the `Activity` is stopped. Writing into it in between this lifecycle state defers the save operation till the next stopped lifecycle event.

Don't use saved instance state to store large amounts of data, such as bitmaps,
nor complex data structures that require lengthy serialization or
deserialization. Instead, store only primitive types and simple, small objects
such as `String`. As such, use saved instance state to store a minimal amount of
data necessary, such as an ID, to re-create the data necessary to restore the UI
back to its previous state should the other persistence mechanisms fail. Most
apps should implement this to handle system-initiated process death.
| **Note:** Android keeps a serialized copy of the data in memory, outside of your process. Depending on various factors, the system might try to optimize this process and leave the same Bundle object in memory without serialization for quicker access. These behaviors however, may change across Android API versions.
| **Warning:** The system can potentially store the data to disk if you use [`PersistableBundle`](https://developer.android.com/reference/android/os/PersistableBundle) instead of [`Bundle`](https://developer.android.com/reference/android/os/Bundle). However, Fragments, Jetpack Compose, and other AndroidX libraries don't support it. Thus, use `Bundle` instead.

Depending on your app's use cases, you might not need to use saved instance
state at all. For example, a browser might take the user back to the exact
webpage they were looking at before they exited the browser. If your activity
behaves this way, you can forego using saved instance state and instead persist
everything locally.
| **Key Point:** Usually, data stored in saved instance state is transient state that depends on user input or navigation. Examples of this can be the scroll position of a list, the id of the item the user wants more detail about, the in-progress selection of user preferences, or input in text fields.

Additionally, when you open an activity from an intent, the bundle of extras is
delivered to the activity both when the configuration changes and when the
system restores the activity. If a piece of UI state data, such as a search
query, were passed in as an intent extra when the activity was launched, you
could use the extras bundle instead of the saved instance state bundle. To learn
more about intent extras, see [Intent and Intent Filters](https://developer.android.com/guide/components/intents-filters).

In either of these scenarios, you should still use a [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) to avoid
wasting cycles reloading data from the database during a configuration change.

In cases where the UI data to preserve is simple and lightweight, you might use
saved instance state APIs alone to preserve your state data.
| **Key Point:** The API to use depends on where the state is held and the logic that it requires. For state that is used in [business logic](https://developer.android.com/architecture/ui-layer/stateholders#logic), hold it in a ViewModel and save it using `SavedStateHandle`. For state that is used in [UI
| logic](https://developer.android.com/architecture/ui-layer/stateholders#logic), use the `onSaveInstanceState` API in the View system or `rememberSaveable` in Compose.
| **Note:** To learn more about `rememberSaveable`, check out the [State and Jetpack
| Compose](https://developer.android.com/jetpack/compose/state#restore-ui-state) documentation.

### Hook into saved state using SavedStateRegistry

Beginning with [Fragment 1.1.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.1.0) or its transitive dependency [Activity
1.0.0](https://developer.android.com/jetpack/androidx/releases/activity#version_100_3), UI controllers, such as an `Activity` or `Fragment`, implement
[`SavedStateRegistryOwner`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistryOwner) and provide a [`SavedStateRegistry`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry) that is
bound to that controller. `SavedStateRegistry` allows components to hook into
your UI controller's saved state to consume or contribute to it. For example,
the [Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate) uses `SavedStateRegistry` to create a
`SavedStateHandle` and provide it to your `ViewModel` objects. You can retrieve
the `SavedStateRegistry` from within your UI controller by calling
[`getSavedStateRegistry()`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistryOwner#getSavedStateRegistry()).

Components that contribute to saved state must implement
[`SavedStateRegistry.SavedStateProvider`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry.SavedStateProvider), which defines a single method
called [`saveState()`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry.SavedStateProvider#saveState()). The `saveState()` method allows your component to
return a `Bundle` containing any state that should be saved from that component.
`SavedStateRegistry` calls this method during the saving state phase of the UI
controller's lifecycle.
**Important:** The `SavedStateHandle` only saves data written to it when the `Activity` is stopped. Writes to `SavedStateHandle` while the `Activity` is stopped aren't saved unless the `Activity` receives `onStart` followed by `onStop` again.  

### Kotlin

```kotlin
class SearchManager : SavedStateRegistry.SavedStateProvider {
    companion object {
        private const val QUERY = "query"
    }

    private val query: String? = null

    ...

    override fun saveState(): Bundle {
        return bundleOf(QUERY to query)
    }
}
```

### Java

```java
class SearchManager implements SavedStateRegistry.SavedStateProvider {
    private static String QUERY = "query";
    private String query = null;
    ...

    @NonNull
    @Override
    public Bundle saveState() {
        Bundle bundle = new Bundle();
        bundle.putString(QUERY, query);
        return bundle;
    }
}
```

To register a `SavedStateProvider`, call [`registerSavedStateProvider()`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry#registerSavedStateProvider(java.lang.String,%20androidx.savedstate.SavedStateRegistry.SavedStateProvider)) on
the `SavedStateRegistry`, passing a key to associate with the provider's data as
well as the provider. The previously saved data for the provider can be
retrieved from the saved state by calling [`consumeRestoredStateForKey()`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry#consumeRestoredStateForKey(java.lang.String))
on the `SavedStateRegistry`, passing in the key associated with the provider's
data.

Within an `Activity` or `Fragment`, you can register a `SavedStateProvider` in
`onCreate()` after calling `super.onCreate()`. Alternatively, you can set a
[`LifecycleObserver`](https://developer.android.com/reference/androidx/lifecycle/LifecycleObserver) on a `SavedStateRegistryOwner`, which implements
[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner), and register the `SavedStateProvider` once the
`ON_CREATE` event occurs. By using a `LifecycleObserver`, you can decouple the
registration and retrieval of the previously saved state from the
`SavedStateRegistryOwner` itself.  

### Kotlin

```kotlin
class SearchManager(registryOwner: SavedStateRegistryOwner) : SavedStateRegistry.SavedStateProvider {
    companion object {
        private const val PROVIDER = "search_manager"
        private const val QUERY = "query"
    }

    private val query: String? = null

    init {
        // Register a LifecycleObserver for when the Lifecycle hits ON_CREATE
        registryOwner.lifecycle.addObserver(LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_CREATE) {
                val registry = registryOwner.savedStateRegistry

                // Register this object for future calls to saveState()
                registry.registerSavedStateProvider(PROVIDER, this)

                // Get the previously saved state and restore it
                val state = registry.consumeRestoredStateForKey(PROVIDER)

                // Apply the previously saved state
                query = state?.getString(QUERY)
            }
        }
    }

    override fun saveState(): Bundle {
        return bundleOf(QUERY to query)
    }

    ...
}

class SearchFragment : Fragment() {
    private var searchManager = SearchManager(this)
    ...
}
```

### Java

```java
class SearchManager implements SavedStateRegistry.SavedStateProvider {
    private static String PROVIDER = "search_manager";
    private static String QUERY = "query";
    private String query = null;

    public SearchManager(SavedStateRegistryOwner registryOwner) {
        registryOwner.getLifecycle().addObserver((LifecycleEventObserver) (source, event) -> {
            if (event == Lifecycle.Event.ON_CREATE) {
                SavedStateRegistry registry = registryOwner.getSavedStateRegistry();

                // Register this object for future calls to saveState()
                registry.registerSavedStateProvider(PROVIDER, this);

                // Get the previously saved state and restore it
                Bundle state = registry.consumeRestoredStateForKey(PROVIDER);

                // Apply the previously saved state
                if (state != null) {
                    query = state.getString(QUERY);
                }
            }
        });
    }

    @NonNull
    @Override
    public Bundle saveState() {
        Bundle bundle = new Bundle();
        bundle.putString(QUERY, query);
        return bundle;
    }

    ...
}

class SearchFragment extends Fragment {
    private SearchManager searchManager = new SearchManager(this);
    ...
}
```
| **Note:** `SavedStateRegistry` stores data in the same `Bundle` as the other saved instance state APIs, therefore the same considerations and data limitations apply.

## Use local persistence to handle process death for complex or large data

Persistent local storage, such as a database or shared preferences, will survive
for as long as your application is installed on the user's device (unless the
user clears the data for your app). While such local storage survives
system-initiated activity and application process death, it can be expensive to
retrieve because it will have to be read from local storage in to memory. Often
this persistent local storage may already be a part of your application
architecture to store all data you don't want to lose if you open and close the
activity.

Neither ViewModel nor saved instance state are long-term storage solutions and
thus are not replacements for local storage, such as a database. Instead you
should use these mechanisms for temporarily storing transient UI state only and
use persistent storage for other app data. See [Guide to App Architecture](https://developer.android.com/topic/libraries/architecture/guide)
for more details about how to leverage local storage to persist your app model
data long term (e.g. across restarts of the device).

## Managing UI state: divide and conquer

You can efficiently save and restore UI state by dividing the work among the
various types of persistence mechanisms. In most cases, each of these mechanisms
should store a different type of data used in the activity, based on the
tradeoffs of data complexity, access speed, and lifetime:

- Local persistence: Stores all the application data you don't want to lose if you open and close the activity.
  - Example: A collection of song objects, which could include audio files and metadata.
- [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel): Stores in memory all the data needed to display the associated UI, the [screen UI state](https://developer.android.com/topic/architecture/ui-layer/stateholders#ui-state).
  - Example: The song objects of the most recent search and the most recent search query.
- Saved instance state: Stores a small amount of data needed to reload UI state if the system stops and then recreates the UI. Instead of storing complex objects here, persist the complex objects in local storage and store a unique ID for these objects in the saved instance state APIs.
  - Example: Storing the most recent search query.

As an example, consider an activity that lets you to search through your
library of songs. Here's how different events should be handled:

When the user adds a song, the [`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel) immediately delegates persisting
this data locally. If this newly added song should be shown in the UI, you
should also update the data in the `ViewModel` object to reflect the addition of
the song. Remember to do all database inserts off of the main thread.

When the user searches for a song, whatever complex song data you load from the
database, it should be immediately stored in the `ViewModel` object as part of
the screen UI state.

When the activity goes into the background and the system calls the saved
instance state APIs, the search query should be stored in saved instance state,
in case the process recreates. Since the information is necessary to load
application data persisted in this, store the search query in the ViewModel
`SavedStateHandle`. This is all the information you need to load the data and
get the UI back into its current state.

## Restore complex states: reassembling the pieces

When it is time for the user to return to the activity, there are two possible
scenarios for recreating the activity:

- The activity is recreated after having been stopped by the system. The system has the query saved in an saved instance state bundle, and the UI should pass the query to the `ViewModel` if `SavedStateHandle` is not used. The `ViewModel` sees that it has no search results cached and delegates loading the search results using the given search query.
- The activity is created after a configuration change. Since the `ViewModel` instance hasn't been destroyed, the `ViewModel` has all the information cached in memory and it doesn't need to re-query the database.

| **Note:** When an activity is initially created, the saved instance state bundle contains no data, and the `ViewModel` object is empty. When you create the `ViewModel` object, you pass an empty query, which tells the `ViewModel` object that there's no data to load yet. Therefore, the activity starts in an empty state.

## Additional resources

To learn more about saving UI states, see the following resources.

- [UI layer documentation](https://developer.android.com/topic/architecture/ui-layer)
- [State and Jetpack Compose documentation](https://developer.android.com/jetpack/compose/state)

### Blogs

- [ViewModels: A simple example](https://medium.com/androiddevelopers/viewmodels-a-simple-example-ed5ac416317e)
- [ViewModels: Persistence, `onSaveInstanceState()`, Restoring UI State and
  Loaders](https://medium.com/androiddevelopers/viewmodels-persistence-onsaveinstancestate-restoring-ui-state-and-loaders-fc7cc4a6c090)
- [Android lifecycle-aware components codelab](https://codelabs.developers.google.com/codelabs/android-lifecycles)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
- [Handling Lifecycles with Lifecycle-Aware Components](https://developer.android.com/topic/libraries/architecture/lifecycle)
- [ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel)