---
title: https://developer.android.com/guide/components/activities/testing
url: https://developer.android.com/guide/components/activities/testing
source: md.txt
---

Activities serve as containers for every user interaction within your app, so it's important to test how your app's activities behave during device-level events such as the following:

- Another app, such as the device's phone app, interrupts your app's activity.
- The system destroys and recreates your activity.
- The user places your activity in a new windowing environment, such as picture-in-picture (PIP) or multi-window.

In particular, it's important to ensure that your activity behaves correctly in response to the events described in[The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle).

This guide describes how to evaluate your app's ability to maintain data integrity and a good user experience as your app's activities transition through different states in their lifecycles.

## Drive an activity's state

One key aspect of testing your app's activities involves placing your app's activities in particular states. To define this "given" part of your tests, use instances of[`ActivityScenario`](https://developer.android.com/reference/androidx/test/core/app/ActivityScenario), part of the[AndroidX Test](https://developer.android.com/training/testing)library. Using this class, you can place your activity in states that simulate device-level events.

`ActivityScenario`is a cross-platform API that you can use in local unit tests and on-device integration tests alike. On a real or virtual device,`ActivityScenario`provides thread safety, synchronizing events between your test's instrumentation thread and the thread that runs your activity under test.

The API is particularly well suited for evaluating how an activity under test behaves when it's destroyed or created. This section presents the most common use cases associated with this API.

### Create an activity

To create the activity under test, add the code shown in the following snippet:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
       launchActivity<MyActivity>().use {
       }
    }
}
```

After creating the activity,`ActivityScenario`transitions the activity to the`RESUMED`state. This state indicates that your activity is running and is visible to users. In this state, you're free to interact with your activity's`View`elements using[Espresso UI tests](https://developer.android.com/training/testing/espresso).

Google recommends that you call`close`on the activity when the test completes. This cleans up the associated resources and improves the stability of your tests.`ActivityScenario`implements`Closeable`, so you can apply the`use`extension, or`try-with-resources`in the Java programming language, so that the activity closes automatically.

Alternatively, you can use`ActivityScenarioRule`to automatically call`ActivityScenario.launch`before each test and`ActivityScenario.close`at test teardown. The following example shows how to define a rule and get an instance of a scenario from it:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @get:Rule var activityScenarioRule = activityScenarioRule<MyActivity>()

    @Test fun testEvent() {
        val scenario = activityScenarioRule.scenario
    }
}
```

### Drive the activity to a new state

To drive the activity to a different state, such as`CREATED`or`STARTED`, call`moveToState()`. This action simulates a situation where your activity is stopped or paused, respectively, because it's interrupted by another app or a system action.

An example usage of`moveToState()`appears in the following code snippet:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
        launchActivity<MyActivity>().use { scenario ->
            scenario.moveToState(State.CREATED)
        }
    }
}
```
| **Caution:** If you try to transition your activity under test to its current state,`ActivityScenario`treats this request as a no-op, not an exception.

### Determine the current activity state

To determine the current state of an activity under test, get the value of the`state`field within your`ActivityScenario`object. It's particularly helpful to check the state of an activity under test if the activity redirects to another activity or finishes itself, as demonstrated in the following code snippet:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
        launchActivity<MyActivity>().use { scenario ->
            scenario.onActivity { activity ->
              startActivity(Intent(activity, MyOtherActivity::class.java))
            }

            val originalActivityState = scenario.state
        }
    }
}
```

### Recreate the activity

When a device is low on resources, the system might destroy an activity, requiring your app to recreate that activity when the user returns to your app. To simulate these conditions, call`recreate()`:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
        launchActivity<MyActivity>().use { scenario ->
            scenario.recreate()
        }
    }
}
```

The`ActivityScenario`class maintains the activity's saved instance state and any objects annotated using`@NonConfigurationInstance`. These objects load into the new instance of your activity under test.

### Retrieve activity results

To get the result code or data associated with a finished activity, get the value of the`result`field within your`ActivityScenario`object, as shown in the following code snippet:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testResult() {
        launchActivity<MyActivity>().use {
            onView(withId(R.id.finish_button)).perform(click())

            // Activity under test is now finished.

            val resultCode = scenario.result.resultCode
            val resultData = scenario.result.resultData
        }
    }
}
```

### Trigger actions in the activity

All methods within`ActivityScenario`are blocking calls, so the API requires you to run them in the instrumentation thread.

To trigger actions in your activity under test, use Espresso view matchers to interact with elements in your view:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
        launchActivity<MyActivity>().use {
            onView(withId(R.id.refresh)).perform(click())
        }
    }
}
```

If you need to call a method on the activity itself, however, you can do so safely by implementing`ActivityAction`:  

```kotlin
@RunWith(AndroidJUnit4::class)
class MyTestSuite {
    @Test fun testEvent() {
        launchActivity<MyActivity>().use { scenario ->
            scenario.onActivity { activity ->
              activity.handleSwipeToRefresh()
            }
        }
    }
}
```
| **Note:** In your test class, don't keep references to the objects that you pass into`onActivity()`. These references consume system resources, and the references themselves might be stale because the framework can recreate an activity that's passed into the callback method.