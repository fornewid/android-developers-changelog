---
title: https://developer.android.com/guide/topics/ui/accessibility/testing
url: https://developer.android.com/guide/topics/ui/accessibility/testing
source: md.txt
---

# Test your app&#39;s accessibility

Testing for accessibility lets you experience your app from the user's perspective and find usability issues that you might miss. Accessibility testing can reveal opportunities to make your app more powerful and versatile for all users, including those with disabilities.

For the best results, use all of the approaches described in this document:

- **Manual testing:**interact with your app using Android accessibility services.
- **Testing using analysis tools:**use tools to discover opportunities to improve your app's accessibility.
- **Automated testing:**turn on accessibility testing in Espresso and Robolectric.
- **User testing:**get feedback from people who interact with your app.

## Manual testing

Manual testing puts you in the shoes of your user. Android[`AccessibilityService`](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)objects change the way your app's content is presented to the user and how the user interacts with the content. By interacting with your app using accessibility services, you can experience your app as your users do.

### TalkBack

TalkBack is Android's built-in screen reader. When TalkBack is on, users can interact with their Android-powered device without seeing the screen. Users with visual impairments might rely on TalkBack to use your app.

#### Turn on TalkBack

1. Open your device's Settings app.
2. Navigate to**Accessibility** and select**TalkBack**.
3. At the top of the TalkBack screen, press**On/Off**to turn on TalkBack.
4. In the confirmation dialog, select**OK**to confirm permissions.

| **Note:** The first time you enable TalkBack, a tutorial launches. To open the tutorial again in the future, navigate to**Settings \> Accessibility \> TalkBack \> Settings \> Launch TalkBack tutorial**.

#### Explore your app with TalkBack

Once TalkBack is on, there are two common ways to navigate:

- **Linear navigation:**quickly swipe right or left to navigate through screen elements in sequence. Double-tap anywhere to select the current screen element.
- **Explore by tapping:**drag your finger over the screen to hear what's under your finger. Double-tap anywhere to select the current element.

To explore your app with TalkBack, complete these steps:

1. Open your app.
2. Swipe through each element in sequence.
3. As you navigate, look for the following issues:

   - Does the spoken feedback for each element convey its content or purpose appropriately? Learn how to[write meaningful labels](https://m3.material.io/foundations/accessible-design/accessibility-basics#c1dcafdc-c001-4a1d-ab51-c76a99b7f497). \* Are announcements succinct, or are they needlessly verbose?
   - Can you complete the main workflows easily?
   - Can you reach every element by swiping?
   - If alerts or other temporary messages appear, are they read aloud?

For more information and tips, refer to the[TalkBack user documentation](https://support.google.com/accessibility/android/answer/6006589).

#### Optional: TalkBack developer settings

TalkBack developer settings make it easier for you to test your app with TalkBack.

To view or change developer settings, complete these steps:

1. Open your device's Settings app.
2. Navigate to**Accessibility** and select**TalkBack**.
3. Select**Settings \> Advanced settings \> Developer settings**:

   1. **Log output level:** select**VERBOSE**.
   2. **Display speech output:**turn on this setting to view TalkBack speech output on the screen.

### Switch Access

Switch Access lets users interact with Android-powered devices using a switch instead of the touch screen. There are several kinds of switches: assistive technology devices such as those sold by AbleNet, Enabling Devices, RJ Cooper, or Tecla\*; external keyboard keys; or buttons. This service can be helpful for users with motor impairments.

\**Google doesn't endorse these companies or their products.*

#### Turn on Switch Access

One way to configure Switch Access is with two switches. One switch is designated as the "Next" switch and moves focus around the screen, and a second "Select" switch selects the focused element. To use this two-switch method, you can use any pair of hardware keys.
| **Note:**Your experience with Switch Access might vary, depending on the tools and software you use.
|
| - If you use an external switch, such as a keyboard, there are additional setup steps. For example, you need to re-enable the soft keyboard. For more information, refer to the[Switch Access user documentation.](https://support.google.com/accessibility/android/answer/6301497)
| - If you're using TalkBack 5.1 or later, a setup wizard is available to configure Switch Access. To use this wizard instead of the following steps, go to**Settings \> Accessibility \> Switch Access \> Settings \> Open Switch Access setup**.

To set up Switch Access using the volume down key as the "Next" switch and the volume up key as the "Select" switch, complete the following steps:

1. Make sure TalkBack is turned off.
2. Open your device's Settings app.
3. Navigate to**Accessibility** and select**Switch Access** , then select**Settings**.
4. On the Switch Access Preferences screen, make sure**Auto-scan**is off.
5. Use the volume down key as your "Next" switch:

   1. Tap**Assign Keys for Scanning \> Next**.
   2. When the dialog opens, press the volume down key. The dialog shows KEYCODE_VOLUME_DOWN.
   3. Tap**OK**to confirm and exit the dialog.
6. Use the volume up key as your "Select" switch:

   1. Tap Select.
   2. When the dialog opens, press the volume up key. The dialog shows KEYCODE_VOLUME_UP.
   3. Tap**OK**to confirm and exit the dialog.
7. Return to Switch Access Preferences by tapping the back button.

8. Optional: If you're using TalkBack 5.1 or later, you can select**Spoken feedback**to turn on spoken feedback.

9. Return to the main Switch Access screen by tapping the back button.

10. At the top of the Switch Access screen, press**On/Off**to turn on Switch Access.

11. In the confirmation dialog, select**OK**to confirm permissions.

#### Explore your app using Switch Access

To explore your app with Switch Access, complete these steps:

1. Open your app.
2. Start scanning by pressing your "Next" key (the volume down button).
3. Continue pressing "Next" until you reach the item you want to select.
4. Select the highlighted item by pressing your "Select" key (the volume up button).
5. As you navigate, look for the following issues:

   - Can you complete the main workflows easily?
   - If you have text or other inputs, can you add and edit content easily?
   - Are items highlighted only if you can perform an action with them?
   - Is each item highlighted only once?
   - Is all functionality that's available through touch screen gestures also available as selectable controls or custom actions within Switch Access?
   - If you're using TalkBack 5.1 or later and you've turned on spoken feedback, does the spoken feedback for each element convey its content or purpose appropriately? Learn how to[write meaningful labels](https://m3.material.io/foundations/accessible-design/accessibility-basics#c1dcafdc-c001-4a1d-ab51-c76a99b7f497).

#### Optional: Use group selection to see all scannable items

Group selection is a Switch Access navigation method that lets you see all scannable items at once. This option lets you perform a quick check to see whether the correct elements on the screen are highlighted.

To turn on group selection, complete these steps:

1. Open your device's Settings app.
2. Navigate to**Accessibility** and select**Switch Access** , then select**Settings**.
3. On the Switch Access Preferences screen, make sure**Auto-scan**is off.
4. Select**Scanning method \> Group selection**.
5. Tap**Assign switches for scanning**.
6. Make sure the text under**Group selection switch 1** and**Group selection switch 2** shows that a switch is assigned to each. If you follow the steps in this document to[turn on Switch Access](https://developer.android.com/guide/topics/ui/accessibility/testing#turn-on-switch-access), the volume buttons are already assigned.

To explore your app with Switch Access using group selection, complete these steps:

1. Press the "Select" key (the volume up button) to highlight all actionable items on the current screen. Look for the following issues:

   - Are only actionable items highlighted?
   - Are all actionable items highlighted?
   - Does the density of highlighted items make sense?
2. Navigate to a different screen to clear the highlight.

To learn more about how users can navigate with group selection, see[Tips for using Switch Access](https://support.google.com/accessibility/android/answer/6395627).

### Voice Access

[Voice Access](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.voiceaccess)lets users control an Android-powered device with spoken commands. Voice Access is available on devices running Android 5.0 (API level 21) and higher. To test your app with Voice Access, learn how to[get started with Voice Access](https://support.google.com/accessibility/android/answer/6151848).

## Testing using analysis tools

Analysis tools can uncover opportunities to improve accessibility that you might miss with manual testing.

### Compose UI Check

Activate Compose UI Check mode![](https://developer.android.com/static/studio/images/buttons/compose-ui-check-mode-icon.png)on a Compose Preview to enable Android Studio to automatically audit your Compose UI for accessibility issues. Android Studio checks that your UI works across different screen sizes by highlighting issues such as text stretched on large screens or low color contrast in the problems panel.
![](https://developer.android.com/static/studio/images/design/compose-ui-check-entry.png)Click the Compose UI Check mode button to activate the check.![](https://developer.android.com/static/studio/images/design/compose-ui-check.png)Compose UI Check mode activated with details in the problems panel.![](https://developer.android.com/static/studio/images/design/compose-ui-check-colorblind.png)Compose UI Check shows how your UI looks with different types of color vision deficiencies.

### Accessibility Scanner

The[Accessibility Scanner](https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor)app scans your screen and suggests ways to improve the accessibility of your app. Accessibility Scanner uses the[Accessibility Test Framework](https://github.com/google/Accessibility-Test-Framework-for-Android)and provides specific suggestions after looking at content labels, clickable items, contrast, and more.

The Android Accessibility Test Framework is integrated in Android Studio to help you find accessibility issues in your layouts. To launch the panel, click the error report button[!](https://developer.android.com/static/studio/images/buttons/toggle-issue-panel-button.png)in the Layout Editor.

![Demo of the Accessibility Scanner](https://developer.android.com/static/studio/images/releases/atf-scanner.gif)**Figure 1.**Demo of the Accessibility Scanner.

To learn more, refer to the following resources:

- [Get started with Accessibility Scanner](https://support.google.com/accessibility/android/answer/6376570)
- [Accessibility Scanner results](https://support.google.com/accessibility/android/answer/6376559)

| **Note:** Keep in mind that the Android Accessibility Test Framework in Android Studio can't detect issues that occur when the app is running on a device.

### Pre-launch report on Google Play

If you distribute your app on Google Play, you have access to a[pre-launch report](https://support.google.com/googleplay/android-developer/answer/7002270)for your app. Google Play generates this report shortly after you[upload an app](https://support.google.com/googleplay/android-developer/answer/113469)to a release channel using the Google Play Console. The pre-launch report, which is also available in the Google Play Console, displays the results of tests that Google Play performs on your app.

In particular, Google Play runs accessibility tests using the[Accessibility Test Framework](https://github.com/google/Accessibility-Test-Framework-for-Android). The results of these tests appear in a table on the**Accessibility**tab of your app's pre-launch report.

The table organizes opportunities for improvement into the following categories:

Touch target size
:   Interactive elements in your app that have a focusable area, or[touch target size](https://developer.android.com/guide/topics/ui/accessibility/apps#large-controls), that is smaller than recommended.

Low contrast
:   Instances where the pair of colors used for a text element and the background behind that element has a lower[color contrast ratio](https://developer.android.com/guide/topics/ui/accessibility/apps#text-visibility)than recommended.

Content labeling
:   UI elements that don't have a[label that describes the elements' purpose](https://developer.android.com/guide/topics/ui/accessibility/apps#describe-ui-element).

Implementation
:   Attributes assigned to UI elements that make it more difficult for the system's accessibility services to interpret the elements correctly. Examples include defining a description for an[editable`View`label](https://support.google.com/accessibility/android/answer/6378120)and using an element[traversal order](https://support.google.com/accessibility/android/answer/7664232)that doesn't match the elements' logical arrangement.

Following the table, the pre-launch report shows snapshots of your app. These snapshots represent the top opportunities to improve your app's accessibility in each category. Select a screenshot to view more details, including a suggested improvement and a more complete list of places in your app where you can apply the same improvement.

Figure 2 shows an example of the table that appears on the**Accessibility** tab of a pre-launch report within Google Play. This figure also includes one of the app's snapshots, showing that the**Next**button has a touch target size that is smaller than recommended.
![An image showing the Pre-launch Accessibility report](https://developer.android.com/static/images/guide/topics/ui/accessibility/pre-launch-report.svg)**Figure 2.** Example summary table (left) and screenshot (right) from the**Accessibility**tab of a pre-launch report.

### UI Automator Viewer

The`uiautomatorviewer`tool provides a convenient GUI to scan and analyze the UI components currently displayed on an Android-powered device. You can use UI Automator to inspect the layout hierarchy and view the properties of UI components that are visible on the foreground of the device. This information lets you create more fine-grained tests, for example by creating a UI selector that matches a specific visible property. The tool is located in the`tools`directory of the Android SDK.

In accessibility testing, this tool is useful for debugging issues found using other testing methods. For example, if manual testing reveals that a view doesn't have the speakable text it requires or a view receives focus when it must not, you can use the tool to help locate the source of the issue.

To learn more about UI Automator Viewer, see[Write automated tests with UI Automator](https://developer.android.com/training/testing/ui-testing/uiautomator-testing).

### Lint

Android Studio shows lint warnings for various accessibility issues and provides links to the relevant places in your source code. In the following example, an image is missing a`contentDescription`attribute. The missing content description results in the following message:  

```
[Accessibility] Missing 'contentDescription' attribute on image
```

Figure 3 shows an example of how this message appears in Android Studio:
![An image showing Android Studio reporting a missing content description on some images.](https://developer.android.com/static/images/guide/topics/ui/accessibility/studio-missing-content-description.svg)**Figure 3.** Message in Android Studio showing missing`contentDescription`attribute.

## Automated testing

The Android platform supports several testing frameworks, such as Espresso, which lets you create and run automated tests that evaluate the accessibility of your app.

### Espresso

[Espresso](https://developer.android.com/training/testing/espresso)is an Android testing library designed to make UI testing fast and easy. It lets you interact with UI components under test in your app and assert that certain behaviors occur or that specific conditions are met.

To see a video overview of accessibility testing with Espresso, watch the following video from minute 31:54 to 34:19:[Inclusive design and testing: Making your app more accessible - Google I/O 2016](https://www.youtube.com/watch?v=SOZwfQO4rVM&t=31m54s).

This section describes how to run accessibility checks using Espresso.

#### Enable checks

You can enable and configure accessibility testing using the[`AccessibilityChecks`](https://developer.android.com/reference/androidx/test/espresso/accessibility/AccessibilityChecks)class:  

### Kotlin

```kotlin
import androidx.test.espresso.accessibility.AccessibilityChecks

@RunWith(AndroidJUnit4::class)
@LargeTest
class MyWelcomeWorkflowIntegrationTest {
    init {
        AccessibilityChecks.enable()
    }
}
```

### Java

```java
import androidx.test.espresso.accessibility.AccessibilityChecks;

@RunWith(AndroidJUnit4.class)
@LargeTest
public class MyWelcomeWorkflowIntegrationTest {
    @BeforeClass
    public void enableAccessibilityChecks() {
        AccessibilityChecks.enable();
    }
}
```

By default, the checks run when you perform any view action defined in[`ViewActions`](https://developer.android.com/reference/androidx/test/espresso/action/ViewActions). Each check includes the view on which the action is performed as well as all descendant views. You can evaluate the entire view hierarchy of a screen during each check by passing`true`into[`setRunChecksFromRootView()`](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/integrations/espresso/AccessibilityValidator.java#L82), as shown in the following code snippet:  

### Kotlin

```kotlin
AccessibilityChecks.enable().setRunChecksFromRootView(true)
```

### Java

```java
AccessibilityChecks.enable().setRunChecksFromRootView(true);
```

#### Suppress subsets of results

After Espresso runs accessibility checks on your app, you might find several opportunities to improve your app's accessibility that you cannot address immediately. In order to stop Espresso tests from continually failing because of these results, you can ignore them temporarily. The Accessibility Test Framework (ATF) provides this functionality using the[`setSuppressingResultMatcher()`](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/integrations/espresso/AccessibilityValidator.java#L95)method, which instructs Espresso to suppress all results that satisfy the given matcher expression.

When you make changes to your app that address one aspect of accessibility, it's beneficial for Espresso to show results for as many other aspects of accessibility as possible. For this reason, it's best to suppress only specific known opportunities for improvement.

When you temporarily suppress accessibility test findings that you plan to address later, it's important to not accidentally suppress similar findings. For this reason, use matchers that are narrowly scoped. To do so, choose a[matcher](http://hamcrest.org/JavaHamcrest/tutorial#a-tour-of-common-matchers)so that Espresso suppresses a given result only if it satisfies**each**of the following accessibility checks:

1. Accessibility checks of a certain type, such as those that check for touch target size.
2. Accessibility checks that evaluate a particular UI element, such as a button.

The[ATF defines several matchers](https://github.com/google/Accessibility-Test-Framework-for-Android/blob/a6117fe0059c82dd764fa628d3817d724570f69e/src/main/java/com/google/android/apps/common/testing/accessibility/framework/AccessibilityCheckResultUtils.java)to help you define which results to show in your Espresso tests. The following example suppresses the results of checks that relate to a single`TextView`element's color contrast. The element's ID is`countTV`.  

### Kotlin

```kotlin
AccessibilityChecks.enable().apply {
        setSuppressingResultMatcher(
                allOf(
                    matchesCheck(TextContrastCheck::class.java),
                    matchesViews(withId(R.id.countTV))
                )
        )
}
```

### Java

```java
AccessibilityValidator myChecksValidator =
    AccessibilityChecks.enable()
        .setSuppressingResultMatcher(
            allOf(
                matchesCheck(TextContrastCheck.class),
                matchesViews(withId(R.id.countTV))));
```

## User testing

Along with the other testing methods in this guide, user testing can provide specific and valuable insights about the usability of your app.

To find users who can test your app, use methods such as the following:

1. Reach out to local organizations, colleges, or universities that provide training for people with disabilities.
2. Ask your social circle. There might be people with disabilities who are willing to help.
3. Ask a user testing service, such as[usertesting.com](https://www.usertesting.com/), if they can test your app and include users with disabilities.
4. Join an accessibility forum, such as[Accessible](https://groups.google.com/forum/#!forum/accessible), and ask for volunteers to try your app.

For more tips, watch the user testing section of the following video, from minute 31:10 to 44:51:[Behind the scenes: What's new in Android accessibility - Google I/O 2016](https://www.youtube.com/watch?v=QlhU0YioJks&t=31m10s).