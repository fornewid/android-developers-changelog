---
title: https://developer.android.com/training/testing/other-components/ui-automator-legacy
url: https://developer.android.com/training/testing/other-components/ui-automator-legacy
source: md.txt
---

> [!NOTE]
> **Note:** A [new version of UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) provides a modern API. We strongly recommended you use the new API for any new UI Automator development.

UI Automator is a UI testing framework suitable for cross-app functional UI
testing across system and installed apps. The UI Automator APIs let you interact
with visible elements on a device, regardless of which [`Activity`](https://developer.android.com/reference/android/app/Activity) is in
focus, so it allows you to perform operations such as opening the Settings menu
or the app launcher in a test device. Your test can look up a UI component by
using convenient descriptors such as the text displayed in that component or its
content description.

> [!NOTE]
> **Note:** This framework requires Android 4.3 (API level 18) or higher.

The UI Automator testing framework is an instrumentation-based API and works
with the [`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) test runner. It's well-suited for writing
opaque box-style automated tests, where the test code does not rely on internal
implementation details of the target app.

The key features of the UI Automator testing framework include the following:

- An API to retrieve state information and perform operations on the target device. For more information, see [Accessing device state](https://developer.android.com/training/testing/other-components/ui-automator-legacy#accessing-device-state).
- APIs that support cross-app UI testing. For more information, see [UI
  Automator APIs](https://developer.android.com/training/testing/other-components/ui-automator-legacy#ui-automator).

> [!NOTE]
> **Note:** UI Automator and Espresso have some feature overlap but Espresso has more synchronization mechanisms so it's preferred for common UI tests.

## Accessing device state

The UI Automator testing framework provides a [`UiDevice`](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice) class to access
and perform operations on the device on which the target app is running. You can
call its methods to access device properties such as current orientation or
display size. The `UiDevice` class also let you perform the following
actions:

1. Change the device rotation.
2. Press hardware keys, such as "volume up".
3. Press the Back, Home, or Menu buttons.
4. Open the notification shade.
5. Take a screenshot of the current window.

For example, to simulate a Home button press, call the `UiDevice.pressHome()`
method.

## UI Automator APIs

The UI Automator APIs allow you to write robust tests without needing to know
about the implementation details of the app that you are targeting. You can use
these APIs to capture and manipulate UI components across multiple apps:

- [`UiObject2`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2): Represents a UI element that is visible on the device.
- [`BySelector`](https://developer.android.com/reference/androidx/test/uiautomator/BySelector): Specifies criteria for matching UI elements.
- [`By`](https://developer.android.com/reference/androidx/test/uiautomator/By): Constructs [`BySelector`](https://developer.android.com/reference/androidx/test/uiautomator/BySelector) in a concise manner.
- [`Configurator`](https://developer.android.com/reference/androidx/test/uiautomator/Configurator): Lets you set key parameters for running UI Automator tests.

> [!NOTE]
> **Note:** Some existing APIs, including [`UiCollection`](https://developer.android.com/reference/androidx/test/uiautomator/UiCollection), [`UiObject`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject), [`UiScrollable`](https://developer.android.com/reference/androidx/test/uiautomator/UiScrollable), and [`UiSelector`](https://developer.android.com/reference/androidx/test/uiautomator/UiSelector) are being deprecated in a future release. For continued support, you should instead use only the APIs mentioned in this document.

For example, the following code shows how you can write a test script that
opens a Gmail app in the device:

### Kotlin

    device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
    device.pressHome()

    val gmail: UiObject2 = device.findObject(By.text("Gmail"))
    // Perform a click and wait until the app is opened.
    val opened: Boolean = gmail.clickAndWait(Until.newWindow(), 3000)
    assertThat(opened).isTrue()

### Java

    device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
    device.pressHome();

    UiObject2 gmail = device.findObject(By.text("Gmail"));
    // Perform a click and wait until the app is opened.
    Boolean opened = gmail.clickAndWait(Until.newWindow(), 3000);
    assertTrue(opened);

## Set up UI Automator

Before building your UI test with UI Automator, make sure to configure your test
source code location and project dependencies, as described in [Set up project
for AndroidX Test](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/test-setup).

In the `build.gradle` file of your Android app module, you must set a dependency
reference to the UI Automator library:

### Kotlin


`dependencies {
...
androidTestImplementation("androidx.test.uiautomator:uiautomator:2.3.0")
}`

### Groovy


`dependencies {
...
androidTestImplementation "androidx.test.uiautomator:uiautomator:2.3.0"
}`

> [!NOTE]
> **Note:** **See [release notes](https://developer.android.com/jetpack/androidx/releases/test-uiautomator) for the latest updates.**

To optimize your UI Automator testing, you should first inspect the target app's
UI components and ensure that they are accessible. These optimization tips are
described in the next two sections.

### Inspect the UI on a device

Before designing your test, inspect the UI components that are visible on the
device. To ensure that your UI Automator tests can access these components,
check that these components have visible text labels,
[`android:contentDescription`](https://developer.android.com/reference/android/view/View#attr_android:contentDescription) values, or both.

The `uiautomatorviewer` tool provides a convenient visual interface to inspect
the layout hierarchy and view the properties of UI components that are visible
on the foreground of the device. This information lets you create more
fine-grained tests using UI Automator. For example, you can create a UI selector
that matches a specific visible property.

To launch the `uiautomatorviewer` tool:

1. Launch the target app on a physical device.
2. Connect the device to your development machine.
3. Open a terminal window and navigate to the `<android-sdk>/tools/` directory.
4. Run the tool with this command:

     $ uiautomatorviewer

To view the UI properties for your application:

1. In the `uiautomatorviewer` interface, click the **Device Screenshot** button.
2. Hover over the snapshot in the left-hand panel to see the UI components identified by the `uiautomatorviewer` tool. The properties are listed in the lower right-hand panel and the layout hierarchy in the upper right-hand panel.
3. Optionally, click on the **Toggle NAF Nodes** button to see UI components that are non-accessible to UI Automator. Only limited information might be available for these components.

To learn about the common types of UI components provided by Android, see [User
Interface](https://developer.android.com/guide/topics/ui).

### Ensure your activity is accessible

The UI Automator test framework performs better on apps that have implemented
Android accessibility features. When you use UI elements of type [`View`](https://developer.android.com/reference/android/view/View), or
a subclass of `View` from the SDK, you don't need to implement accessibility
support, as these classes have already done that for you.

Some apps, however, use custom UI elements to provide a richer user experience.
Such elements won't provide automatic accessibility support. If your app
contains instances of a subclass of `View` that isn't from the SDK, make
sure that you add accessibility features to these elements by completing the
following steps:

1. Create a concrete class that extends [ExploreByTouchHelper](https://developer.android.com/reference/androidx/customview/widget/ExploreByTouchHelper).
2. Associate an instance of your new class with a specific custom UI element by calling [setAccessibilityDelegate()](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,%20android.support.v4.view.AccessibilityDelegateCompat)).

For additional guidance on adding accessibility features to custom view
elements, see [Building Accessible Custom Views](https://developer.android.com/guide/topics/ui/accessibility/custom-views). To learn more about
general best practices for accessibility on Android, see [Making Apps More
Accessible](https://developer.android.com/reference/android/app/Instrumentation).

## Create a UI Automator test class

Your UI Automator test class should be written the same way as a JUnit 4 test
class. To learn more about creating JUnit 4 test classes and using JUnit 4
assertions and annotations, see [Create an Instrumented Unit Test Class](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#build).

Add the @RunWith(AndroidJUnit4.class) annotation at the beginning of your test
class definition. You also need to specify the [AndroidJUnitRunner](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) class,
provided in AndroidX Test, as your default test runner. This step is described
in more detail in [Run UI Automator tests on a device or emulator](https://developer.android.com/training/testing/ui-testing/uiautomator-testing#run).

Implement the following programming model in your UI Automator test class:

1. Get a `UiDevice` object to access the device you want to test, by calling the [getInstance()](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice#getInstance(android.app.Instrumentation)) method and passing it an [Instrumentation](https://developer.android.com/reference/android/app/Instrumentation) object as the argument.
2. Get a [`UiObject2`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2) object to access a UI component that is displayed on the device (for example, the current view in the foreground), by calling the [findObject()](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice#findObject(androidx.test.uiautomator.UiSelector)) method.
3. Simulate a specific user interaction to perform on that UI component, by calling a `UiObject2` method; for example, call [scrollUntil()](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#scrollUntil(androidx.test.uiautomator.Direction,androidx.test.uiautomator.Condition%3C?%20super%20androidx.test.uiautomator.UiObject2,U%3E)) to scroll, and [setText()](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#setText(java.lang.String)) to edit a text field. You can call on the APIs in steps 2 and 3 repeatedly as necessary to test more complex user interactions that involve multiple UI components or sequences of user actions.
4. Check that the UI reflects the expected state or behavior, after these user interactions are performed.

These steps are covered in more detail in the sections below.

### Access UI components

The [`UiDevice`](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice) object is the primary way you access and manipulate the
state of the device. In your tests, you can call `UiDevice` methods to check for
the state of various properties, such as current orientation or display size.
Your test can use the `UiDevice` object to perform device-level actions,
such as forcing the device into a specific rotation, pressing D-pad hardware
buttons, and pressing the Home and Menu buttons.

It's good practice to start your test from the Home screen of the device. From
the Home screen (or some other starting location you've chosen in the device),
you can call the methods provided by the UI Automator API to select and interact
with specific UI elements.

The following code snippet shows how your test might get an instance of
`UiDevice` and simulate a Home button press:

### Kotlin

    import org.junit.Before
    import androidx.test.runner.AndroidJUnit4
    import androidx.test.uiautomator.UiDevice
    import androidx.test.uiautomator.By
    import androidx.test.uiautomator.Until
    ...

    private const val BASIC_SAMPLE_PACKAGE = "com.example.android.testing.uiautomator.BasicSample"
    private const val LAUNCH_TIMEOUT = 5000L
    private const val STRING_TO_BE_TYPED = "UiAutomator"

    @RunWith(AndroidJUnit4::class)
    @SdkSuppress(minSdkVersion = 18)
    class ChangeTextBehaviorTest2 {

    private lateinit var device: UiDevice

    @Before
    fun startMainActivityFromHomeScreen() {
      // Initialize UiDevice instance
      device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())

      // Start from the home screen
      device.pressHome()

      // Wait for launcher
      val launcherPackage: String = device.launcherPackageName
      assertThat(launcherPackage, notNullValue())
      device.wait(
        Until.hasObject(By.pkg(launcherPackage).depth(0)),
        LAUNCH_TIMEOUT
      )

      // Launch the app
      val context = ApplicationProvider.g<etAppli>cationContextContext()
      val intent = context.packageManager.getLaunchIntentForPackage(
      BASIC_SAMPLE_PACKAGE).apply {
        // Clear out any previous instances
        addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
      }
      context.startActivity(intent)

      // Wait for the app to appear
      device.wait(
        Until.hasObject(By.pkg(BASIC_SAMPLE_PACKAGE).depth(0)),
        LAUNCH_TIMEOUT
        )
      }
    }

### Java

    import org.junit.Before;
    import androidx.test.runner.AndroidJUnit4;
    import androidx.test.uiautomator.UiDevice;
    import androidx.test.uiautomator.By;
    import androidx.test.uiautomator.Until;
    ...

    @RunWith(AndroidJUnit4.class)
    @SdkSuppress(minSdkVersion = 18)
    public class ChangeTextBehaviorTest {

      private static final String BASIC_SAMPLE_PACKAGE
      = "com.example.android.testing.uiautomator.BasicSample";
      private static final int LAUNCH_TIMEOUT = 5000;
      private static final String STRING_TO_BE_TYPED = "UiAutomator";
      private UiDevice device;

      @Before
      public void startMainActivityFromHomeScreen() {
        // Initialize UiDevice instance
        device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());

        // Start from the home screen
        device.pressHome();

        // Wait for launcher
        final String launcherPackage = device.getLauncherPackageName();
        assertThat(launcherPackage, notNullValue());
        device.wait(Until.hasObject(By.pkg(launcherPackage).depth(0)),
        LAUNCH_TIMEOUT);

        // Launch the app
        Context context = ApplicationProvider.getApplicationContext();
        final Intent intent = context.getPackageManager()
        .getLaunchIntentForPackage(BASIC_SAMPLE_PACKAGE);
        // Clear out any previous instances
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
        context.startActivity(intent);

        // Wait for the app to appear
        device.wait(Until.hasObject(By.pkg(BASIC_SAMPLE_PACKAGE).depth(0)),
        LAUNCH_TIMEOUT);
        }
    }

In the example, the @SdkSuppress(minSdkVersion = 18) statement helps to ensure
that tests will only run on devices with Android 4.3 (API level 18) or higher,
as required by the UI Automator framework.

Use the `findObject()` method to retrieve a `UiObject2` which represents
a view that matches a given selector criteria. You can reuse the `UiObject2`
instances that you have created in other parts of your app testing, as needed.
Note that the UI Automator test framework searches the current display for a
match every time your test uses a `UiObject2` instance to click on a UI
element or query a property.

The following snippet shows how your test might construct `UiObject2`
instances that represent a Cancel button and a OK button in an app.

### Kotlin

    val okButton: UiObject2 = device.findObject(
        By.text("OK").clazz("android.widget.Button")
    )

    // Simulate a user-click on the OK button, if found.
    if (okButton != null) {
        okButton.click()
    }

### Java

    UiObject2 okButton = device.findObject(
        By.text("OK").clazz("android.widget.Button")
    );

    // Simulate a user-click on the OK button, if found.
    if (okButton != null) {
        okButton.click();
    }

#### Specify a selector

If you want to access a specific UI component in an app, use the
[`By`](https://developer.android.com/reference/androidx/test/uiautomator/By) class to construct a [`BySelector`](https://developer.android.com/reference/androidx/test/uiautomator/BySelector) instance. `BySelector`
represents a query for specific elements in the displayed UI.

If more than one matching element is found, the first matching element in the
layout hierarchy is returned as the target `UiObject2`. When constructing a
`BySelector`, you can chain together multiple properties to refine your
search. If no matching UI element is found, a `null` is returned.

You can use the [`hasChild()`](https://developer.android.com/reference/androidx/test/uiautomator/By#hasChild(androidx.test.uiautomator.BySelector)) or [`hasDescendant()`](https://developer.android.com/reference/androidx/test/uiautomator/By#hasDescendant(androidx.test.uiautomator.BySelector)) method to nest
multiple `BySelector` instances. For example, the following code example shows
how your test might specify a search to find the first [`ListView`](https://developer.android.com/reference/android/widget/ListView) that
has a child UI element with the text property.

### Kotlin

    val listView: UiObject2 = device.findObject(
        By.clazz("android.widget.ListView")
            .hasChild(
                By.text("Apps")
            )
    )

### Java

    UiObject2 listView = device.findObject(
        By.clazz("android.widget.ListView")
            .hasChild(
                By.text("Apps&quot;)
            )
    );

It can be useful to specify the object state in your selector criteria. For
example, if you want to select a list of all checked elements so that you can
clear them, call the [`checked()`](https://developer.android.com/reference/androidx/test/uiautomator/By#checked(boolean)) method with the argument set to true.

### Perform actions

Once your test has obtained a `UiObject2` object, you can call the methods in
the `UiObject2` class to perform user interactions on the UI component
represented by that object. You can specify such actions as:

- [`click()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#click()) : Clicks the center of the visible bounds of the UI element.
- [`drag()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#drag(android.graphics.Point,int)) : Drags this object to arbitrary coordinates.
- [`setText()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#setText(java.lang.String)) : Sets the text in an editable field, after clearing the field's content. Conversely, the [`clear()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#clear()) method clears the existing text in an editable field.
- [`swipe()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#swipe(androidx.test.uiautomator.Direction,float)) : Performs the swipe action toward specified direction.
- [`scrollUntil()`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#scrollUntil(androidx.test.uiautomator.Direction,androidx.test.uiautomator.Condition%3C?%20super%20androidx.test.uiautomator.UiObject2,U%3E)): Performs the scroll action toward specified direction until [`Condition`](https://developer.android.com/reference/androidx/test/uiautomator/Condition) or [`EventCondition`](https://developer.android.com/reference/androidx/test/uiautomator/EventCondition) is satisfied.

The UI Automator testing framework lets you send an [Intent](https://developer.android.com/reference/android/content/Intent) or launch
an [Activity](https://developer.android.com/reference/android/app/Activity) without using shell commands, by getting a [Context](https://developer.android.com/reference/android/content/Context)
object through [`getContext()`](https://developer.android.com/reference/android/app/Instrumentation#getContext()).

The following snippet shows how your test can use an [Intent](https://developer.android.com/reference/android/content/Intent) to launch the
app under test. This approach is useful when you are only interested in testing
the calculator app, and don't care about the launcher.

### Kotlin

    fun setUp() {
    ...

      // Launch a simple calculator app
      val context = getInstrumentation().context
      val intent = context.packageManager.getLaunchIntentForPackage(CALC_PACKAGE).apply {
        addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
      }
      // Clear out any previous instances
      context.startActivity(intent)
      device.wait(Until.hasObject(By.pkg(CALC_PACKAGE).depth(0)), TIMEOUT)
    }

### Java

    public void setUp() {
    ...

      // Launch a simple calculator app
      Context context = getInstrumentation().getContext();
      Intent intent = context.getPackageManager()
      .getLaunchIntentForPackage(CALC_PACKAGE);
      intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);

      // Clear out any previous instances
      context.startActivity(intent);
      device.wait(Until.hasObject(By.pkg(CALC_PACKAGE).depth(0)), TIMEOUT);
    }

### Verify results

The [InstrumentationTestCase](https://developer.android.com/reference/android/test/InstrumentationTestCase) extends [TestCase](https://developer.android.com/reference/junit/framework/TestCase), so you can use
standard JUnit [Assert](http://junit.org/javadoc/latest/org/junit/Assert.html) methods to test that UI components in the app return
the expected results.

The following snippet shows how your test can locate several buttons in a
calculator app, click on them in order, then verify that the correct result is
displayed.

### Kotlin

    private const val CALC_PACKAGE = "com.myexample.calc"

    fun testTwoPlusThreeEqualsFive() {
      // Enter an equation: 2 + 3 = ?
      device.findObject(By.res(CALC_PACKAGE, "two")).click()
      device.findObject(By.res(CALC_PACKAGE, "plus")).click()
      device.findObject(By.res(CALC_PACKAGE, "three")).click()
      device.findObject(By.res(CALC_PACKAGE, "equals")).click()

      // Verify the result = 5
      val result: UiObject2 = device.findObject(By.res(CALC_PACKAGE, "result"))
      assertEquals("5", result.text)
    }

### Java

    private static final String CALC_PACKAGE = "com.myexample.calc";

    public void testTwoPlusThreeEqualsFive() {
      // Enter an equation: 2 + 3 = ?
      device.findObject(By.res(CALC_PACKAGE, "two")).click();
      device.findObject(By.res(CALC_PACKAGE, "plus")).click();
      device.findObject(By.res(CALC_PACKAGE, "three")).click();
      device.findObject(By.res(CALC_PACKAGE, "equals")).click();

      // Verify the result = 5
      UiObject2 result = device.findObject(By.res(CALC_PACKAGE, &quot;result"));
      assertEquals("5", result.getText());
    }

## Run UI Automator tests on a device or emulator

You can run UI Automator tests from [Android Studio](https://developer.android.com/studio) or from the
command-line. Make sure to specify `AndroidJUnitRunner` as the default
instrumentation runner in your project.

## More examples

### Interact with the System UI

UI Automator can interact with everything on the screen, including system
elements outside of your app, as shown in the following code snippets:

### Kotlin

```kotlin
// Opens the System Settings.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
device.executeShellCommand("am start -a android.settings.SETTINGS")
```

### Java

```java
// Opens the System Settings.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
device.executeShellCommand("am start -a android.settings.SETTINGS");
```

### Kotlin

```kotlin
// Opens the notification shade.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
device.openNotification()
```

### Java

```java
// Opens the notification shade.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
device.openNotification();
```

### Kotlin

```kotlin
// Opens the Quick Settings shade.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
device.openQuickSettings()
```

### Java

```java
// Opens the Quick Settings shade.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
device.openQuickSettings();
```

### Kotlin

```kotlin
// Get the system clock.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
UiObject2 clock = device.findObject(By.res("com.android.systemui:id/clock"))
print(clock.getText())
```

### Java

```java
// Get the system clock.
device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
UiObject2 clock = device.findObject(By.res("com.android.systemui:id/clock"));
print(clock.getText());
```

### Wait for transitions

![Turn off disturb](https://developer.android.com/static/images/testing/uiautomator_turn_off_disturb.gif) **Figure 1.** UI Automator turns off Do Not Disturb mode on a test device.

Screen transitions can take time and predicting their duration is unreliable, so
you should have UI Automator wait after performing operations. UI Automator
provides multiple methods for this:

- [`UiDevice.performActionAndWait(Runnable action, EventCondition<U> condition, long timeout)`](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice#performActionAndWait(java.lang.Runnable,androidx.test.uiautomator.EventCondition%3CU%3E,long)): For example, to click a button and wait until a new window appears, call `device.performActionAndWait(() -> button.click(), Until.newWindow(), timeout)`
- [`UiDevice.wait(Condition<Object, U> condition, long timeout)`](https://developer.android.com/reference/androidx/test/uiautomator/UiDevice#wait(androidx.test.uiautomator.Condition%3C?%20super%20androidx.test.uiautomator.UiDevice,U%3E,long)): For example, to wait until there is a certain `UiObject2` on device, call `device.wait(Until.hasObject(By.text("my_text")), timeout);`
- [`UiObject2.wait(@NonNull Condition<Object, U> condition, long timeout)`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#wait(androidx.test.uiautomator.Condition%3C?%20super%20androidx.test.uiautomator.UiObject2,U%3E,long)): For example, to wait until a checkbox is checked, call `checkbox.wait(Until.checked(true), timeout);`
- [`UiObject2.clickAndWait(@NonNull EventCondition<U> condition, long timeout)`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#clickAndWait(androidx.test.uiautomator.EventCondition%3CU%3E,long)): For example to click a button and wait until a new window appears, call `button.clickAndWait(Until.newWindow(), timeout);`
- [`UiObject2.scrollUntil(@NonNull Direction direction, @NonNull Condition<Object, U> condition)`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#scrollUntil(androidx.test.uiautomator.Direction,androidx.test.uiautomator.Condition%3C?%20super%20androidx.test.uiautomator.UiObject2,U%3E)): For example to scroll down until a new object appears, call `object.scrollUntil(Direction.DOWN, Until.hasObject(By.text('new_obj')));`
- [`UiObject2.scrollUntil(@NonNull Direction direction, @NonNull EventCondition<U> condition)`](https://developer.android.com/reference/androidx/test/uiautomator/UiObject2#scrollUntil(androidx.test.uiautomator.Direction,androidx.test.uiautomator.EventCondition%3CU%3E)): For example to scroll down to the bottom, call `object.scrollUntil(Direction.DOWN, Until.scrollFinished(Direction.DOWN));`

The following code snippet shows how to use UI Automator to turn off Do Not
Disturb mode in System settings using the `performActionAndWait()` method that
waits for transitions:

### Kotlin

```kotlin
@Test
@SdkSuppress(minSdkVersion = 21)
@Throws(Exception::class)
fun turnOffDoNotDisturb() {
    device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())
    device.performActionAndWait({
        try {
            device.executeShellCommand("am start -a android.settings.SETTINGS")
        } catch (e: IOException) {
            throw RuntimeException(e)
        }
    }, Until.newWindow(), 1000)
    // Check system settings has been opened.
    Assert.assertTrue(device.hasObject(By.pkg("com.android.settings")))

    // Scroll the settings to the top and find Notifications button
    var scrollableObj: UiObject2 = device.findObject(By.scrollable(true))
    scrollableObj.scrollUntil(Direction.UP, Until.scrollFinished(Direction.UP))
    val notificationsButton = scrollableObj.findObject(By.text("Notifications"))

    // Click the Notifications button and wait until a new window is opened.
    device.performActionAndWait({ notificationsButton.click() }, Until.newWindow(), 1000)
    scrollableObj = device.findObject(By.scrollable(true))
    // Scroll down until it finds a Do Not Disturb button.
    val doNotDisturb = scrollableObj.scrollUntil(
        Direction.DOWN,
        Until.findObject(By.textContains("Do Not Disturb"))
    )
    device.performActionAndWait({ doNotDisturb.click() }, Until.newWindow(), 1000)
    // Turn off the Do Not Disturb.
    val turnOnDoNotDisturb = device.findObject(By.text("Turn on now"))
    turnOnDoNotDisturb?.click()
    Assert.assertTrue(device.wait(Until.hasObject(By.text("Turn off now")), 1000))
}
```

### Java

```java
@Test
@SdkSuppress(minSdkVersion = 21)
public void turnOffDoNotDisturb() throws Exception{
    device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());
    device.performActionAndWait(() -> {
        try {
            device.executeShellCommand("am start -a android.settings.SETTINGS");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }, Until.newWindow(), 1000);
    // Check system settings has been opened.
    assertTrue(device.hasObject(By.pkg("com.android.settings")));

    // Scroll the settings to the top and find Notifications button
    UiObject2 scrollableObj = device.findObject(By.scrollable(true));
    scrollableObj.scrollUntil(Direction.UP, Until.scrollFinished(Direction.UP));
    UiObject2 notificationsButton = scrollableObj.findObject(By.text("Notifications"));

    // Click the Notifications button and wait until a new window is opened.
    de>vice.performActionAndWait(() - notificationsButton.click(), Until.newWindow(), 1000);
    scrollableObj = device.findObject(By.scrollable(true));
    // Scroll down until it finds a Do Not Disturb button.
    UiObject2 doNotDisturb = scrollableObj.scrollUntil(Direction.DOWN,
            Until.findObject(By.textContains("Do Not Disturb">)));
    device.performActionAndWait(()- doNotDisturb.click(), Until.newWindow(), 1000);
    // Turn off the Do Not Disturb.
    UiObject2 turnOnDoNotDisturb = device.findObject(By.text("Turn on now"));
    if(turnOnDoNotDisturb != null) {
        turnOnDoNotDisturb.click();
    }
    assertTrue(device.wait(Until.hasObject(By.text("Turn off now")), 1000));
}
```

## Additional resources

For more information about using UI Automator in Android tests, consult the
following resources.

### Reference documentation:

- [UI Automator API Reference](https://developer.android.com/reference/androidx/test/uiautomator/package-summary)

### Samples

- [BasicSample](https://github.com/android/testing-samples/tree/main/ui/uiautomator/BasicSample): Basic UI Automator sample.