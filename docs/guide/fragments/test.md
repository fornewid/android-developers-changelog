---
title: https://developer.android.com/guide/fragments/test
url: https://developer.android.com/guide/fragments/test
source: md.txt
---

This topic describes how to include framework-provided APIs in tests
that evaluate each fragment's behavior.

Fragments serve as reusable containers within your app, allowing you to
present the same user interface layout in a variety of activities and
layout configurations. Given the versatility of fragments, it's important
to validate that they provide a consistent and resource-efficient experience.
Note the following:

- Your fragment shouldn't be dependent on a specific parent activity or fragment.
- You shouldn't create a fragment's view hierarchy unless the fragment is visible to the user.

To help set up the conditions for performing these tests, the AndroidX
`fragment-testing` library provides the
[`FragmentScenario`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario)
class to create fragments and change their
[`Lifecycle.State`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State).
| **Note:** To successfully run tests that contain `FragmentScenario` objects, run each of the API's methods in your test's instrumentation thread. To learn more about different threads used in Android tests, see [Understand threads in tests](https://developer.android.com/training/testing/fundamentals#threads).

## Declaring dependencies

To use `FragmentScenario` define the `fragment-testing-manifest` artifact in your
app's `build.gradle` file using `debugImplementation`, and the `fragment-testing` artifact using `androidTestImplementation` as shown in the
following example:  

### Groovy

```groovy
dependencies {
    def fragment_version = "1.8.9"

    debugImplementation "androidx.fragment:fragment-testing-manifest:$fragment_version"

    androidTestImplementation "androidx.fragment:fragment-testing:$fragment_version"
}
```

### Kotlin

```kotlin
dependencies {
    val fragment_version = "1.8.9"

    debugImplementation("androidx.fragment:fragment-testing-manifest:$fragment_version")

    androidTestImplementation("androidx.fragment:fragment-testing:$fragment_version")
}
```
| **Note:** `debugImplementation` is used here so that the empty activity definition that `FragmentScenario` relies on is accessible by the test target process.

Testing examples on this page use assertions from the
[Espresso](https://developer.android.com/training/testing/espresso) and
[Truth](https://truth.dev/) libraries. For information on
other available testing and assertion libraries, see
[Set up project for AndroidX Test](https://developer.android.com/training/testing/set-up-project#android-test-dependencies).

## Create a fragment

`FragmentScenario` includes the following methods for launching fragments
in tests:

- [`launchInContainer()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario#launchInContainer(java.lang.Class%3CF%3E)), for testing a fragment's user interface. `FragmentScenario` attaches the fragment to an activity's root view controller. This containing activity is otherwise empty.
- [`launch()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario#launch(java.lang.Class%3CF%3E)), for testing without the fragment's user interface. `FragmentScenario` attaches this type of fragment to an *empty activity*, one that doesn't have a root view.

After launching one of these fragment types, `FragmentScenario` drives the
fragment under test to a specified state. By default this state is `RESUMED`,
but you can override this with the `initialState` argument. The `RESUMED` state
indicates that the fragment is running and visible to the user. You can evaluate
information about its UI elements using [Espresso UI
tests](https://developer.android.com/training/testing/espresso).

The following code examples show how to launch your fragment using each method:
| **Note:** Your fragment might require a theme that the test activity doesn't use by default. You can provide your own theme as an additional argument to `launch()` and `launchInContainer()`.

**launchInContainer() example**  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            // The "fragmentArgs" argument is optional.
            val fragmentArgs = bundleOf("selectedListItem" to 0)
            val scenario = launchFragmentInContainer<EventFragment>(fragmentArgs)
            ...
        }
    }

**launch() example**  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            // The "fragmentArgs" arguments are optional.
            val fragmentArgs = bundleOf("numElements" to 0)
            val scenario = launchFragment<EventFragment>(fragmentArgs)
            ...
        }
    }

## Provide dependencies

If your fragments have dependencies, you can provide test versions of
these dependencies by providing a custom `FragmentFactory` to the
`launchInContainer()` or `launch()` methods.  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            val someDependency = TestDependency()
            launchFragmentInContainer {
                EventFragment(someDependency)
            }
            ...
        }
    }

For more information about using `FragmentFactory` to provide
dependencies to fragments, see
[Fragment manager](https://developer.android.com/guide/fragments/fragmentmanager).

## Drive the fragment to a new state

In your app's UI tests, it's usually sufficient to launch the fragment
under test and start testing it from a `RESUMED` state. In finer-grained
unit tests, however, you might also evaluate the fragment's behavior
as it transitions from one lifecycle state to another. You can specify the
initial state by passing the `initialState` argument to any of the
`launchFragment*()` functions.

To drive the fragment to a different lifecycle state, call
[`moveToState()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario#moveToState(androidx.lifecycle.Lifecycle.State)).
This method supports the following states as arguments: `CREATED`,
`STARTED`, `RESUMED`, and `DESTROYED`. This method simulates a situation
where the fragment or activity containing your fragment changes its
state for any reason.
| **Note:** If you transition a fragment to the `DESTROYED` state, you can't drive the fragment to another state, and you can't attach the fragment to a different activity.

The following example launches a test fragment in the `INITIALIZED` state and
then moves it to the `RESUMED` state:  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            val scenario = launchFragmentInContainer<EventFragment>(
                initialState = Lifecycle.State.INITIALIZED
            )
            // EventFragment has gone through onAttach(), but not onCreate().
            // Verify the initial state.
            scenario.moveToState(Lifecycle.State.RESUMED)
            // EventFragment moves to CREATED -> STARTED -> RESUMED.
            ...
        }
    }

| **Caution:** If you try to transition your fragment under test to its current state, `FragmentScenario` ignores the request without throwing an exception. In particular, the API allows you to transition your fragment to the `DESTROYED` state multiple times consecutively.

## Recreate the fragment

If your app is running on a device which is low on resources, the system
might destroy the activity containing your fragment. This situation
requires your app to recreate the fragment when the user returns to it.
To simulate this situation, call `recreate()`:  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            val scenario = launchFragmentInContainer<EventFragment>()
            scenario.recreate()
            ...
        }
    }

[`FragmentScenario.recreate()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario#recreate())
destroys the fragment and its host and then recreates them. When the
`FragmentScenario` class recreates the fragment under test, the fragment
returns to the lifecycle state that it was in before it was destroyed.

## Interacting with UI fragments

To trigger UI actions in your fragment under test, use
[Espresso view matchers](https://developer.android.com/reference/kotlin/androidx/test/espresso/matcher/ViewMatchers)
to interact with elements in your view:  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            val scenario = launchFragmentInContainer<EventFragment>()
            onView(withId(R.id.refresh)).perform(click())
            // Assert some expected behavior
            ...
        }
    }

If you need to call a method on the fragment itself, such as responding
to a selection in the options menu, you can do so safely by getting a
reference to the fragment using
[`FragmentScenario.onFragment()`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario#onFragment(androidx.fragment.app.testing.FragmentScenario.FragmentAction%3CF%3E))
and passing in a
[`FragmentAction`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/FragmentScenario.FragmentAction):  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testEventFragment() {
            val scenario = launchFragmentInContainer<EventFragment>()
            scenario.onFragment { fragment ->
                fragment.myInstanceMethod()
            }
        }
    }

| **Note:** Don't keep references to the fragment that is passed into `onFragment()`. These references consume system resources, and the references themselves might be stale, since the framework can recreate the fragment.

## Test dialog actions

`FragmentScenario` also supports testing
[dialog fragments](https://developer.android.com/guide/fragments/dialogs). Though dialog fragments
have UI elements, their layout is populated in a separate window, rather
than in the activity itself. For this reason, use
`FragmentScenario.launch()` to test dialog fragments.

The following example tests the dialog dismissal process:  

    @RunWith(AndroidJUnit4::class)
    class MyTestSuite {
        @Test fun testDismissDialogFragment() {
            // Assumes that "MyDialogFragment" extends the DialogFragment class.
            with(launchFragment<MyDialogFragment>()) {
                onFragment { fragment ->
                    assertThat(fragment.dialog).isNotNull()
                    assertThat(fragment.requireDialog().isShowing).isTrue()
                    fragment.dismiss()
                    fragment.parentFragmentManager.executePendingTransactions()
                    assertThat(fragment.dialog).isNull()
                }
            }

            // Assumes that the dialog had a button
            // containing the text "Cancel".
            onView(withText("Cancel")).check(doesNotExist())
        }
    }