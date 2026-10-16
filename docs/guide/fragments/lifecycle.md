---
title: https://developer.android.com/guide/fragments/lifecycle
url: https://developer.android.com/guide/fragments/lifecycle
source: md.txt
---

# Fragment lifecycle

Each[`Fragment`](https://developer.android.com/reference/androidx/fragment/app/Fragment)instance has its own lifecycle. When a user navigates and interacts with your app, your fragments transition through various states in their lifecycle as they are added, removed, and enter or exit the screen.

To manage lifecycle,`Fragment`implements[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner), exposing a[`Lifecycle`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle)object that you can access through the[`getLifecycle()`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner#getLifecycle())method.

Each possible`Lifecycle`state is represented in the[`Lifecycle.State`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State)enum.

- [`INITIALIZED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#INITIALIZED)
- [`CREATED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#CREATED)
- [`STARTED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#STARTED)
- [`RESUMED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#RESUMED)
- [`DESTROYED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#DESTROYED)

By building`Fragment`on top of`Lifecycle`, you can use the techniques and classes available for[Handling Lifecycles with Lifecycle-Aware Components](https://developer.android.com/topic/libraries/architecture/lifecycle). For example, you might display the device's location on the screen using a lifecycle-aware component. This component could automatically start listening when the fragment becomes active and stop when the fragment moves to an inactive state.

As an alternative to using a[`LifecycleObserver`](https://developer.android.com/reference/androidx/lifecycle/LifecycleObserver), the`Fragment`class includes callback methods that correspond to each of the changes in a fragment's lifecycle. These include[`onCreate()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle)),[`onStart()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStart()),[`onResume()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onResume()),[`onPause()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onPause()),[`onStop()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStop()), and[`onDestroy()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onDestroy()).

A fragment's view has a separate`Lifecycle`that is managed independently from that of the fragment's`Lifecycle`. Fragments maintain a[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)for their view, which can be accessed using[`getViewLifecycleOwner()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwner())or[`getViewLifecycleOwnerLiveData()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData()). Having access to the view's`Lifecycle`is useful for situations where a Lifecycle-aware component should only perform work while a fragment's view exists, such as observing[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)that is only meant to be displayed on the screen.

This topic discusses the`Fragment`lifecycle in detail, explaining some of the rules that determine a fragment's lifecycle state and showing the relationship between the`Lifecycle`states and the fragment lifecycle callbacks.

## Fragments and the fragment manager

When a fragment is instantiated, it begins in the`INITIALIZED`state. For a fragment to transition through the rest of its lifecycle, it must be added to a[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager). The`FragmentManager`is responsible for determining what state its fragment should be in and then moving them into that state.

Beyond the fragment lifecycle,`FragmentManager`is also responsible for attaching fragments to their host activity and detaching them when the fragment is no longer in use. The`Fragment`class has two callback methods,`onAttach()`and`onDetach()`, that you can override to perform work when either of these events occur.

The`onAttach()`callback is invoked when the fragment has been added to a`FragmentManager`and is attached to its host activity. At this point, the fragment is active, and the`FragmentManager`is managing its lifecycle state. At this point,`FragmentManager`methods such as[`findFragmentById()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#findFragmentById(int))return this fragment.

`onAttach()`is always called before any[Lifecycle state changes](https://developer.android.com/guide/fragments/lifecycle#states).

The`onDetach()`callback is invoked when the fragment has been removed from a`FragmentManager`and is detached from its host activity. The fragment is no longer active and can no longer be retrieved using[`findFragmentById()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#findFragmentById(int)).

`onDetach()`is always called after any[Lifecycle state changes](https://developer.android.com/guide/fragments/lifecycle#states).

Note that these callbacks are unrelated to the[`FragmentTransaction`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction)methods[`attach()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#attach(androidx.fragment.app.Fragment))and[`detach()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#detach(androidx.fragment.app.Fragment)). For more information on these methods, see[Fragment transactions](https://developer.android.com/guide/fragments/transactions#attach-detach).
| **Caution:** Avoid reusing`Fragment`instances after they are removed from the`FragmentManager`. While the fragment handles its own internal state cleanup, you might inadvertently carry over your own state into the reused instance.

## Fragment lifecycle states and callbacks

When determining a fragment's lifecycle state,`FragmentManager`considers the following:

- A fragment's maximum state is determined by its`FragmentManager`. A fragment cannot progress beyond the state of its`FragmentManager`.
- As part of a`FragmentTransaction`, you can set a maximum lifecycle state on a fragment using[`setMaxLifecycle()`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction#setMaxLifecycle(androidx.fragment.app.Fragment,%20androidx.lifecycle.Lifecycle.State)).
- A fragment's lifecycle state can never be greater than its parent. For example, a parent fragment or activity must be started before its child fragments. Likewise, child fragments must be stopped before their parent fragment or activity.

| **Caution:** Avoid using the`<fragment>`tag to add a fragment using XML, as the`<fragment>`tag allows a fragment to move beyond the state of its`FragmentManager`. Instead, always use[`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView)for adding a fragment using XML.
![fragment lifecycle states and their relation both the fragment's lifecycle callbacks and the fragment's view lifecycle](https://developer.android.com/static/images/guide/fragments/fragment-view-lifecycle.png)**Figure 1.** Fragment`Lifecycle`states and their relation to both the fragment's lifecycle callbacks and the fragment's view`Lifecycle`.

Figure 1 shows each of the fragment's`Lifecycle`states and how they relate to both the fragment's lifecycle callbacks and the fragment's view`Lifecycle`.

As a fragment progresses through its lifecycle, it moves upward and downward through its states. For example, a fragment that is added to the top of the back stack moves upward from`CREATED`to`STARTED`to`RESUMED`. Conversely, when a fragment is popped off of the back stack, it moves downward through those states, going from`RESUMED`to`STARTED`to`CREATED`and finally`DESTROYED`.

### Upward state transitions

When moving upward through its lifecycle states, a fragment first calls the associated lifecycle callback for its new state. Once this callback is finished, the relevant[`Lifecycle.Event`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event)is emitted to observers by the fragment's`Lifecycle`, followed by the fragment's view`Lifecycle`, if it has been instantiated.

#### Fragment CREATED

When your fragment reaches the`CREATED`state, it has been added to a`FragmentManager`and the[`onAttach()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onAttach(android.content.Context))method has already been called.

This would be the appropriate place to restore any saved state associated with the fragment itself through the fragment's[`SavedStateRegistry`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry). Note that the fragment's view has*not*been created at this time, and any state associated with the fragment's view should be restored only after the view has been created.

This transition invokes the[`onCreate()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreate(android.os.Bundle))callback. The callback also receives a`savedInstanceState`[`Bundle`](https://developer.android.com/reference/android/os/Bundle)argument containing any state previously saved by[`onSaveInstanceState()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onSaveInstanceState(android.os.Bundle)). Note that`savedInstanceState`has a`null`value the first time the fragment is created, but it is always non-null for subsequent recreations, even if you do not override`onSaveInstanceState()`. See[Saving state with fragments](https://developer.android.com/guide/fragments/saving-state)for more details.

#### Fragment CREATED and View INITIALIZED

The fragment's view`Lifecycle`is created only when your`Fragment`provides a valid[`View`](https://developer.android.com/reference/android/view/View)instance. In most cases, you can use the[fragment constructors](https://developer.android.com/reference/androidx/fragment/app/Fragment#Fragment(int))that take a`@LayoutId`, which automatically inflates the view at the appropriate time. You can also override[`onCreateView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle))to programmatically inflate or create your fragment's view.

If and only if your fragment's view is instantiated with a non-null`View`, that`View`is set on the fragment and can be retrieved using[`getView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getView()). The[`getViewLifecycleOwnerLiveData()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData())is then updated with the newly`INITIALIZED`[`LifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)corresponding with the fragment's view. The[`onViewCreated()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onViewCreated(android.view.View,%20android.os.Bundle))lifecycle callback is also called at this time.

This is the appropriate place to set up the initial state of your view, to start observing[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)instances whose callbacks update the fragment's view, and to set up adapters on any[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)or[`ViewPager2`](https://developer.android.com/reference/androidx/viewpager2/widget/ViewPager2)instances in your fragment's view.

#### Fragment and View CREATED

After the fragment's view has been created, the previous view state, if any, is restored, and the view's`Lifecycle`is then moved into the`CREATED`state. The view lifecycle owner also emits the[`ON_CREATE`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_CREATE)event to its observers. Here you should restore any additional state associated with the fragment's view.

This transition also invokes the[`onViewStateRestored()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onViewStateRestored(android.os.Bundle))callback.

#### Fragment and View STARTED

It is strongly recommended to tie[Lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/lifecycle)to the`STARTED`state of a fragment, as this state guarantees that the fragment's view is available, if one was created, and that it is safe to perform a`FragmentTransaction`on the child`FragmentManager`of the fragment. If the fragment's view is non-null, the fragment's view`Lifecycle`is moved to`STARTED`immediately after the fragment's`Lifecycle`is moved to`STARTED`.

When the fragment becomes`STARTED`, the[`onStart()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStart())callback is invoked.
| **Note:** Components such as[`ViewPager2`](https://developer.android.com/reference/androidx/viewpager2/widget/ViewPager2)set the maximum`Lifecycle`of offscreen fragments to`STARTED`.

#### Fragment and View RESUMED

When the fragment is visible, all[`Animator`](https://developer.android.com/reference/android/animation/Animator)and[`Transition`](https://developer.android.com/reference/androidx/transition/Transition)effects have finished, and the fragment is ready for user interaction. The fragment's`Lifecycle`moves to the`RESUMED`state, and the[`onResume()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onResume())callback is invoked.

The transition to`RESUMED`is the appropriate signal to indicate that the user is now able to interact with your fragment. Fragments that are not`RESUMED`should not manually set focus on their views or attempt to[handle input method visibility](https://developer.android.com/training/keyboard-input/visibility).

### Downward state transitions

When a fragment moves downward to a lower lifecycle state, the relevant[`Lifecycle.Event`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event)is emitted to observers by the fragment's view`Lifecycle`, if instantiated, followed by the fragment's`Lifecycle`. After a fragment's lifecycle event is emitted, the fragment calls the associated lifecycle callback.

#### Fragment and View STARTED

As the user begins to leave the fragment, and while the fragment is still visible, the`Lifecycle`s for the fragment and for its view are moved back to the`STARTED`state and emit the[`ON_PAUSE`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_PAUSE)event to their observers. The fragment then invokes its[`onPause()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onPause())callback.

#### Fragment and View CREATED

Once the fragment is no longer visible, the`Lifecycle`s for the fragment and for its view are moved into the`CREATED`state and emit the[`ON_STOP`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_STOP)event to their observers. This state transition is triggered not only by the parent activity or fragment being stopped, but also by the saving of state by the parent activity or fragment. This behavior guarantees that the`ON_STOP`event is invoked before the fragment's state is saved. This makes the`ON_STOP`event the last point where it is safe to perform a`FragmentTransaction`on the child`FragmentManager`.

As shown in figure 2, the ordering of the[`onStop()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStop())callback and the saving of the state with`onSaveInstanceState()`differs based on API level. For all API levels prior to API 28,`onSaveInstanceState()`is invoked before[`onStop()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onStop()). For API levels 28 and higher, the calling order is reversed.
![calling order differences for onStop() and onSaveInstanceState()](https://developer.android.com/static/images/guide/fragments/stop-save-order.png)**Figure 2.** Calling order differences for`onStop()`and`onSaveInstanceState()`.

#### Fragment CREATED and View DESTROYED

After all of the exit[animations and transitions](https://developer.android.com/training/basics/fragments/animate)have completed, and the fragment's view has been detached from the window, the fragment's view`Lifecycle`is moved into the`DESTROYED`state and emits the[`ON_DESTROY`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_DESTROY)event to its observers. The fragment then invokes its[`onDestroyView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onDestroyView())callback. At this point, the fragment's view has reached the end of its lifecycle and[`getViewLifecycleOwnerLiveData()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#getViewLifecycleOwnerLiveData())returns a`null`value.

At this point, all references to the fragment's view should be removed, allowing the fragment's view to be garbage collected.

#### Fragment DESTROYED

If the fragment is removed, or if the`FragmentManager`is destroyed, the fragment's`Lifecycle`is moved into the`DESTROYED`state and sends the[`ON_DESTROY`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event#ON_DESTROY)event to its observers. The fragment then invokes its[`onDestroy()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onDestroy())callback. At this point, the fragment has reached the end of its lifecycle.

## Additional resources

For more information related to the fragment lifecycle, see the following additional resources.

### Guides

- [Handling Lifecycles with Lifecycle-Aware Components](https://developer.android.com/topic/libraries/architecture/lifecycle)

### Blogs

- [Fragments: Rebuilding the Internals](https://medium.com/androiddevelopers/fragments-rebuilding-the-internals-61913f8bf48e)