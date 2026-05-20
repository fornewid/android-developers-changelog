---
title: https://developer.android.com/topic/performance/memory-leaks
url: https://developer.android.com/topic/performance/memory-leaks
source: md.txt
---

A memory leak occurs when an object is no longer needed, but another object
retains a strong reference to it. This prevents the garbage collector from
reclaiming the leaked object's memory. In Android, this typically happens when a
longer-lived object retains a reference to an object with a shorter lifecycle,
such as an activity, a fragment view, or screen-owned UI state. Implementing
lifecycle-aware design is the primary defense against memory leaks.

This document categorizes memory leak examples by their underlying architectural
patterns. It focuses on common scenarios in which an object remains strongly
reachable after its lifecycle has ended.

While the APIs might differ, the underlying issue is usually the same: a
reference outlives the object it points to. When the owner of a reference is
clear, the correct cleanup point is usually clear as well.

Each example in this document is structured to include approaches to avoid and
the corresponding recommended approach.

> [!NOTE]
> **Note:** These examples demonstrate commonly observed common memory leaks; they are not intended to be indicative of modern recommended architecture patterns.

## Pattern 1: UI objects retained beyond lifecycle

This pattern occurs when a screen, view, or binding is retained by a component
that outlives the UI itself.

### Example 1: Repository retains a UI callback

If unmanaged, the repository continues to hold a reference to the callback even
after the fragment view is destroyed.

#### Approach to avoid

The callback references the binding, and the binding references the fragment
view. As long as the repository retains the callback, the fragment view remains
in memory after `onDestroyView()` is called.

    class UserRepository {
        private var listener: ((User) -> Unit)? = null

        fun fetchUser(callback: (User) -> Unit) {
            // The repository retains the callback beyond the view lifecycle.
            listener = callback
            api.getUser { user ->
                listener?.invoke(user)
            }
        }
    }

    // In the Fragment/UI layer:
    repository.fetchUser { user ->
        binding.name.text = user.name
    }

The retention chain is `UserRepository` -\> `callback` -\> `binding` -\> `fragment
view`.

#### Recommended approach

Ensure data fetching is asynchronous to prevent long-lived layers from holding
onto callback references. Use Kotlin coroutines to achieve this without coupling
your layers to callback states.

    class UserRepository {
        suspend fun fetchUser(): User {
            return api.getUser()
        }
    }

    // In the Fragment/UI layer:
    viewLifecycleOwner.lifecycleScope.launch {
        val user = repository.fetchUser()
        binding.name.text = user.name
    }

**Key takeaway:** Long-lived architectural layers should not store callbacks
that directly interact with or update UI objects.

### Example 2: Singleton depends on a UI-scoped object

In this example, the app-scoped singleton references an object that holds a
direct, strong reference to an `Activity`.

#### Approach to avoid

The singleton lives for the lifetime of the app. By injecting an
activity-scoped dependency, the `Activity` remains reachable in memory after it
is destroyed.

    @Singleton
    class ImageLoader @Inject constructor(
        private val activityImagePicker: ActivityImagePicker
    )

    class ActivityImagePicker @Inject constructor(
        // Injecting Activity here makes this dependency activity-scoped.
        private val activity: Activity
    )

The retention chain is `ImageLoader(Singleton)` -\> `ActivityImagePicker` -\>
`Activity`.

#### Recommended approach

To resolve this, either pass the short-lived `Activity` dynamically as a
function parameter, or if only non-UI system services are needed inject the
`@ApplicationContext` instead.

    // Option 1: Pass the Activity dynamically for UI-scoped tasks
    // (like image picking)
    @Singleton
    class ImageLoader @Inject constructor() {
        fun pickImage(activity: Activity) { /* ... */ }
    }

    // Option 2: Inject Application Context for non-UI/background tasks
    // (like disk caching or sharedPreferences)
    @Singleton
    class ImageLoader @Inject constructor(
        @ApplicationContext private val context: Context
    )

**Key takeaway:** A longer-lived dependency must not depend on a shorter-lived
dependency.

## Pattern 2: Background work outlives the UI

This issue occurs when an asynchronous task or stream continues to execute after
its associated UI component (`Activity`, `Fragment`, `View`, or `Composable`)
has been destroyed or recomposed.

### Example 1: Fragment collects flow with the incorrect lifecycle

The coroutine continues to reference the binding after the fragment view is
destroyed.

#### Approach to avoid

When a fragment goes into the backstack, its view gets destroyed but the
fragment instance stays alive. Because `lifecycleScope` is tied to the fragment
and not its view, it keeps a reference to the old view, leaking the entire
layout in memory.

    class UserFragment : Fragment(R.layout.user_fragment) {
        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            val binding = UserFragmentBinding.bind(view)

            lifecycleScope.launch {
                // This coroutine is tied to the fragment lifecycle, not the view
                // lifecycle.
                viewModel.user.collect { user ->
                    binding.name.text = user.name
                }
            }
        }
    }

The retention chain is `Fragment.lifecycleScope coroutine` -\> `binding` -\>
`destroyed fragment view`.

#### Recommended approach

Tie UI collection in a fragment strictly to the `viewLifecycleOwner`.

    class UserFragment : Fragment(R.layout.user_fragment) {
        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            val binding = UserFragmentBinding.bind(view)

            viewLifecycleOwner.lifecycleScope.launch {
                viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                    viewModel.user.collect { user ->
                        binding.name.text = user.name
                    }
                }
            }
        }
    }

**Key takeaway:** UI data collection must always be bound to the lifecycle of
the active UI view, rather than the lifespans of their host instances (such as
fragments or parent compositions).

### Example 2: Delayed work captures an `Activity`

Passing a lifecycle-bound callback (such as an anonymous interface or lambda
that references an `Activity`) into a long-lived singleton, and executing it
within a custom, non-cancelled `CoroutineScope`.

#### Approach to avoid

Because a custom scope in a singleton doesn't know when an `Activity` is
destroyed, any delayed work inside it will keep holding onto the `Activity`
reference until the coroutine completes.

    // Singleton scope accepts a UI-bound callback
    object UserRepository {
        private val repositoryScope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

        // Accepts a callback that might capture a destroyed UI Context
        fun fetchUserDataWithDelay(onComplete: (String) -> Unit) {
            repositoryScope.launch {
                delay(5_000) // This delay emulates the network response latency
                onComplete("User Data") // If onComplete references the Activity, it
                // leaks
            }
        }
    }

    class MainActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            // The trailing lambda implicitly captures 'this' (MainActivity) to
            // update the title
            UserRepository.fetchUserDataWithDelay { data ->
                title = data
            }
        }
    }

The retention chain is `SingletonRepository` -\> `custom CoroutineScope` -\>
`suspended coroutine` -\> `captured Activity callback`.

#### Recommended approach: Use streams instead of long-lived callbacks

Instead of passing callbacks into long-lived scopes, have your singleton expose
a cold `Flow`. The UI can then safely collect this stream within its own
lifecycle-aware scope (`lifecycleScope` or `repeatOnLifecycle`), ensuring that
all operations are cancelled the moment the screen is destroyed.

    //  Expose data as a Flow and let the UI handle the lifecycle scope
    object UserRepository {
        // A clean, stateless flow with no callback parameters
        fun getUserData(): Flow<String> = flow {
            delay(5_000) // This delay emulates the network response latency
            emit("User Data")
        }
    }

    class MainActivity : AppCompatActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            // Automatically cancels collection and releases MainActivity when
            // destroyed
            lifecycleScope.launch {
                UserRepository.getUserData().collect { data ->
                    title = data
                }
            }
        }
    }

**Key takeaway:** Avoid passing callbacks or lambdas from UI components into
long-lived singletons or custom scopes. Instead, expose data streams (such as
`Flow`) and allow the UI to safely handle collection within its own
lifecycle-aware scope.

## Pattern 3: Unreleased external registrations

This pattern occurs when a UI component registers a listener, observer, or
callback with an object managed outside its own lifecycle (such as a system
service) and fails to unregister it during teardown.

### Example 1: Compose registers a system service listener without cleanup

The system-level service continues to hold a strong reference to the callback
lambda after the Composable leaves the screen.

#### Approach to avoid

Since the registration is made to an external platform service, Compose has no
way of knowing it needs to be torn down when the Composable leaves the screen.
The callback remains active, trapping the captured Compose state and surrounding
memory structures

    // Registering a platform listener without an unregistration mechanism
    @Composable
    fun LocationScreen(locationManager: LocationManager) {
        var locationText by remember { mutableStateOf("Locating...") }

        // This registers the listener when entering composition, but leaves it
        // attached to the OS when leaving
        remember(locationManager) {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000L, 1f) { location ->
                locationText = "Lat: ${location.latitude}, Lng: ${location.longitude}"
            }
        }

        Text(text = locationText)
    }

The retention chain is `LocationManager` -\> `registered LocationListener
instance` -\> `lambda closure` -\> `Compose state slot`.

#### Recommended approach

Use `DisposableEffect` when interacting with external APIs that require
imperative setup and teardown. The `onDispose` block ensures that the system
listener is explicitly unregistered the exact moment the Composable leaves the
screen.

    @Composable
    fun LocationScreen(locationManager: LocationManager) {
        var locationText by remember { mutableStateOf("Locating...") }

        // DisposableEffect provides an onDispose block for mandatory cleanup
        DisposableEffect(locationManager) {
            val listener = LocationListener { location ->
                locationText = "Lat: ${location.latitude}, Lng: ${location.longitude}"
            }

            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 1000L, 1f, listener)

            // Automatically executed when this Composable leaves the screen
            onDispose {
                locationManager.removeUpdates(listener)
            }
        }

        Text(text = locationText)
    }

**Key takeaway:** While Compose manages Compose-owned work, external
registrations require explicit teardown logic.

### Example 2: Fragment view binding is not cleared

The fragment continues to hold the binding field after the view is destroyed.

#### Approach to avoid

When a fragment goes into the backstack, its view is destroyed but the fragment
instance remains alive. Holding onto the binding field without nullifying it
traps the entire old view hierarchy in memory until the user completely
navigates away from the fragment.

    class UserFragment : Fragment() {
        private var binding: UserFragmentBinding? = null

        override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
        ): View {
            // The fragment keeps this binding field until it is cleared.
            binding = UserFragmentBinding.inflate(inflater, container, false)
            return binding!!.root
        }
    }

The retention chain is `fragment` -\> `binding field` -\> `destroyed fragment
view`.

#### Recommended approach

Nullify the binding reference inside `onDestroyView()`. By separating your
binding into a nullable property (_binding) for cleanup and a non-null property
(binding) for usage, you keep your layout code clean without sacrificing memory
safety.

    class UserFragment : Fragment() {
        private var _binding: UserFragmentBinding? = null
        // This property simplifies using the binding without constantly checking for null
        private val binding get() = _binding!!

        override fun onCreateView(
            inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?
        ): View {
            _binding = UserFragmentBinding.inflate(inflater, container, false)
            return binding.root
        }

        override fun onDestroyView() {
            _binding = null // Explicitly releases the view hierarchy from memory
            super.onDestroyView()
        }
    }

**Key takeaway:** References to a fragment view must be explicitly cleared when
the view lifecycle ends.