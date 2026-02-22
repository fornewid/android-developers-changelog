---
title: https://developer.android.com/training/testing/local-tests/robolectric
url: https://developer.android.com/training/testing/local-tests/robolectric
source: md.txt
---

# Robolectric strategies

[Robolectric](https://robolectric.org/)is an open-source framework maintained by Google that lets you run tests in a simulated Android environment inside a JVM, without the overhead and flakiness of an emulator. It supports all versions of Android since Lollipop (API level 21).

Many big projects use Robolectric to increase the speed and reliability of their tests and reduce the expenses associated with running tests on real devices or emulators. This includes most Google apps which rely heavily on Robolectric.

Robolectric is not a complete replacement for an emulator because it doesn't support all the features and APIs. For example, Robolectric doesn't have a screen like an emulator does, and some APIs are only partially supported. However, it emulates enough parts of Android to run unit tests and most UI tests reliably.

## Testing strategies

There are two types of testing strategies you can pursue with Robolectric: unit testing and UI testing.

### Unit testing

Robolectric was conceived as a way to enable "unit testing" in Android apps. For example, you can simulate the launch of an Activity and test the logic inside it, calling all the lifecycle methods.

You can also use Robolectric's fakes (called shadows) as dependencies for unit tests. For example, if your class uses a Bundle or you need to fake a[Bluetooth](https://github.com/robolectric/robolectric/blob/ae831fccdc10b5808c274fbe519a5a8deae33424/shadows/framework/src/main/java/org/robolectric/shadows/BluetoothConnectionManager.java#L12)connection.

In general, if you implement a[testable architecture](https://developer.android.com/training/testing/fundamentals#architecture)you shouldn't need to use Robolectric for unit testing as your code should be testable in isolation, with no dependencies on the Android framework.
| **Key Point:** In most cases, only use Robolectric for unit testing as a last resort: with legacy code or when using APIs that depend on Android classes. When possible, refactor your code so that it's testable without Robolectric shadows, or test the feature using a different type of test, such as a UI test.

### UI testing

Robolectric can also run[UI tests](https://developer.android.com/training/testing/ui-tests)such as Espresso or Compose tests. You can convert an[instrumented](https://developer.android.com/training/testing/instrumented-tests)test to Robolectric by moving it to the`test`source set and setting up the Robolectric dependencies.  

    android {
      testOptions {
        unitTests {
          isIncludeAndroidResources = true
        }
      }
    }

    dependencies {
      testImplementation("junit:junit:4.13.2")
      testImplementation("org.robolectric:robolectric:4.13")
    }

Any UI test present in the`test`source set runs with Robolectric.  

    import androidx.test.espresso.Espresso.onView

    @RunWith(AndroidJUnit4::class)
    class AddContactActivityTest {
        @Test
        fun inputTextShouldBeRetainedAfterActivityRecreation() {
            // GIVEN
            val contactName = "Test User"
            val scenario = ActivityScenario.launchActivity<AddContactActivity>()

            // WHEN
            // Enter contact name
            onView(withId(R.id.contact_name_text))
                .perform(typeText(contactName))
            // Destroy and recreate Activity
            scenario.recreate()

            // THEN
            // Check contact name was preserved.
            onView(withId(R.id.contact_name_text))
                .check(matches(withText(contactName)))
         }
    }

Most UI tests don't interact with the framework and you can run them on Robolectric. You can run behavior tests on Robolectric as the fidelity needed for it is more than enough. For example, when a Compose test verifies that the UI has changed after clicking a button.

You can run other UI tests with Robolectric, such as screenshot tests. However the fidelity is lower as different devices render screens slightly differently.

You must decide whether Robolectric's implementation is good enough for each use case, but here are some recommendations:

- Use Robolectric for isolated UI behavior tests for components, feature or application tests. In general these tests check the state management and behavior of the UIs and don't interact with external dependencies.
- Use Robolectric to take screenshots when the pixel accuracy is not critical. For example, to test how a component reacts to different font sizes or themes.

**Note**: Robolectric can take screenshots natively, but you need a third-party library to perform screenshot testing with it.

## Robolectric versus device tests

In summary, Robolectric provides enough fidelity to run most UI tests but some cases will still require device tests, for example those related to system UI like edge-to-edge or picture-in-picture, or when relying on unsupported features, like`WebView`.