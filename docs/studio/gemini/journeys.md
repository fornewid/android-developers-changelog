---
title: https://developer.android.com/studio/gemini/journeys
url: https://developer.android.com/studio/gemini/journeys
source: md.txt
---

> [!WARNING]
> **Preview:** Journeys for Android Studio are available as a Studio Labs feature starting from Android Studio Otter 3 Feature Drop \| 2025.2.3. To enable it, go to **Studio Labs** in the settings menu.

Journeys for Android Studio leverages the vision and reasoning capabilities of
AI to navigate and test your app based on your natural language instructions.
Your set of instructions, called a journey, are converted into actions that AI
performs on your app. Additionally, you can write and describe more complex
assertions, which AI evaluates based on what it sees on the device.
![Journeys for Android Studio.](https://developer.android.com/static/studio/gemini/images/journey-animation.gif) Journeys for Android Studio.

And because Gemini reasons about which actions to perform to satisfy the goals,
journeys are more resilient to subtle changes to your app's layout or behavior,
resulting in fewer flaky tests when running against different versions of your
app and different device configurations.

You can write and run journeys right from Android Studio or from the command
line against any local or remote Android-powered device. The IDE provides a new
editor experience for crafting journeys as well as rich results that help you
better follow Gemini's reasoning and execution of your journey.

> [!NOTE]
> **Note:** Before you get started, sign into your developer account and [enable
> Gemini in Android Studio](https://developer.android.com/studio/gemini/get-started).

## Write a journey

Android Studio provides a file template and new editor experience that makes
creating and editing journeys easier. Journeys are written using the XML syntax
to organize your journey description and steps.

> [!NOTE]
> **Note:** To run a journey, your project needs to use Android Gradle Plugin 9.0.0 or higher. If you're unable to upgrade your project, you can [run journeys against pre-installed apps](https://developer.android.com/studio/gemini/journeys#pre-installed-apk) on your test device.

![The journey editor in Android Studio, showing an XML file with
journey steps.](https://developer.android.com/static/studio/gemini/images/journey-editor.png)

To create and start editing a journey, do the following:

1. From the **Project** panel in Android Studio, right-click on the app module for which you want to write a journey.
2. Select **New \> Journey Test**.
3. In the dialog that appears, provide the name and description of your journey.

   ![A dialog in Android Studio you use to create a journey file.](https://developer.android.com/static/studio/gemini/images/journey-template.png) A dialog in Android Studio you use to create a journey file.

   <br />

   > [!NOTE]
   > **Note:** If it's the first time you're adding journeys to your project, the template will also add support for Android Gradle Plugin Test Suites to your project, which is required to run journeys.

4. Click **Finish** . Android Studio creates an XML file for your journey with
   the name you chose. You can use either the **Code** view to edit the XML
   directly, or the **Design** view for a simplified editing experience.

5. When viewing your journey in the **Design** view, use the text field to
   describe each step of your journey. Each step can include descriptive actions
   you want Gemini to perform or assertions that you want Gemini to evaluate.

6. Press <kbd>Enter</kbd> on your keyboard to start a new step in the same
   journey. You can repeat this as needed for each step of the journey you want
   to define.

### Configure build variants

Journeys runs against specific build variants of your app. When you first create
a journey using the wizard, the generated test suite is configured to run
against the build variant that is active in Android Studio.

However, if you later switch the active build variant in Android Studio (for
example, to a different product flavor like `demoDebug`) without updating the
configuration, running the journey will fail. To fix this, you must add the new
variant to the `targetVariants` property in the `testSuites` block of your
module-level `build.gradle.kts` (or `build.gradle`) file.

For example, to configure the `journeysTest` suite for the `demoDebug` variant:

    android {
        // ...
        testSuites {
            create("journeysTest") {
                // ...
                targetVariants += listOf("demoDebug")
            }
        }
    }

### Tips for writing journeys

Although the AI is capable of understanding most steps written in supported
languages, following these tips for writing journeys can lead to more accurate
and expected results:

- **Assume your app is already in the foreground:** Running a journey automatically launches your app. The steps of your journey should begin *after* the app has fully launched. That is, you don't need to include "launch app" as a step.
- **Use unambiguous language:** Being precise minimizes misinterpretation and improves reliability.

| Instead of | Do this |
|---|---|
| "Select the dismiss button" | "Tap 'Dismiss'" or just "Dismiss" |
| "Type 'celery'" | "Type 'celery' in the search bar at the top of the home screen" |
| "Swipe to dismiss" | "Swipe left to dismiss, the card should then no longer be visible" |

- **Include the success criteria as part of the step:** This helps Gemini better understand your intention and clarifies when the action is complete and the next action can start.

| Instead of | Do this |
|---|---|
| "Select the send button" | "Send the email by tapping the submit button. This should close the email and return you to the inbox." |
| "Go to the shopping cart" | "Tap on the shopping cart icon which will take you to the shopping cart page. Verify it contains zero items" |
| "Click the first video" | "Click the first video and wait for it to fully load" |

- **Refine your journey:** If your journey isn't executing as expected, you can [view the results](https://developer.android.com/studio/gemini/journeys#results) and inspect 'Action Taken' and corresponding 'Reasoning' to understand why Gemini might not have executed the steps as you expected. Use this information to provide additional clarity to your instructions.
- **Break down your journey into more specific steps:** Although the AI can interpret multi-action steps, sometimes more granular discrete steps may improve the accuracy and reproducibility of the journey.
  - **"Error: Could not successfully complete the action in max allowed
    attempt"**: If you encounter this error, try breaking up the failing steps into two or more smaller steps. That's because this error occurs if the AI is unable to complete the action after attempting a max number of interactions with your app.

### Supported and unsupported capabilities

Here's an overview of the supported and not yet fully supported
capabilities when writing journeys. The following lists aren't exhaustive.

The following actions are **supported** within journeys:

- **Tap** on UI elements.
- **Type** to input text into text fields.
- **Swipe/Scroll** in a certain direction to navigate the UI.

The following capabilities are **not fully supported** at this time or may
perform inconsistently:

- **Multi-finger gestures (for example, pinch to zoom)** - Interactions requiring two or more points of contact on the screen simultaneously, such as pinching to zoom in or out, or swiping with two-fingers.
- **Long-press** - Pressing and holding a finger down for a duration longer than a standard tap.
- **Double tap** - Quickly tapping the same location on the screen twice in rapid succession.
- **Screen rotation/folding** - Handling changes in device orientation (for example, between portrait and landscape) or the physical state of foldable devices (for example, opening or closing).
- **Memory** - Retaining and recalling specific information, context, or user inputs across prior interactions or steps.
- **Counting** - Accurately tracking quantities, frequencies, or progress.
- **Conditional statements** - Executing actions based on whether other specified conditions are met.

Features and capabilities are constantly improving. We suggest checking this page
later to learn about additional features and capabilities. To help us improve
Journeys, [share your feedback](https://developer.android.com/studio/report-bugs).

## Run your journey

You can run your journey on any available local or remote device, similar to any
other instrumented test, and Android Studio generates rich results that help you
understand the execution of your journey.

To test a journey, do the following:

1. Select a target device from the main toolbar, like you would when running an instrumented test.
2. Navigate to the journey XML file that you would like to test and open it in the editor.
3. In the editor, do one of the following:
   1. If you're in the **Design** view, click ![](https://developer.android.com/static/studio/preview/gemini/images/run-journey-icon.png) **Run Journey**.
   2. If you're in the **Code** view, click ![](https://developer.android.com/static/studio/preview/gemini/images/run-test-icon.png) **Run 'test'** in the gutter next to where the name of the journey is defined in the XML.

Android Studio creates a **Journeys Test** configuration for you and runs it on
the target device. During execution, Android Studio builds and deploys your app,
and connects to Gemini to determine which actions to take for each step of your
journey.
![The journey test results panel in Android Studio, displaying step
details and Gemini's reasoning.](https://developer.android.com/static/studio/gemini/images/journey-results.png) The journey test results panel in Android Studio, displaying step details and Gemini's reasoning.

#### Run journeys against any pre-installed app

You can run a journey on a pre-installed app on your test device. This is useful
if you want to test a production version of your app, or if you haven't yet
updated your app to Android Gradle Plugin 9.0.0 or higher.

1. Open or [create a new project](https://developer.android.com/studio/projects/create-project) that is updated to Android Gradle Plugin 9.0.0 or higher.
2. [Write a journey](https://developer.android.com/studio/gemini/journeys#write).
3. [Edit the run configuration](https://developer.android.com/studio/run/rundebugconfig#editing) for the journey and add the following environment variables. A run configuration is created automatically when you attempt to run a journey from Android Studio.
   - Set `JOURNEYS_CUSTOM_APP_ID` to the target app's package ID.
4. Run the journey that you edited. Android Studio should execute the steps of the journey on the target app you specified.

### Run a journey from the command line

You can also run a journey from the command line as a Gradle task.

#### Setup

You will need to authenticate to Google Cloud to use Journeys from the command
line.

**Note:** These steps use the gcloud CLI to provide user credentials, which
might not apply to all development environments. For more information about what
authentication process to use for your needs, see
[How Application Default Credentials works](https://cloud.google.com/docs/authentication/application-default-credentials).

To install the Google Cloud CLI, follow the steps at
[Install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

You also need to make sure that the **IAM Service Account Credentials API** is
enabled for your Google Cloud project. Then, authenticate using one of the
following methods:

**For user credentials**

You can authorize manually by using the following terminal command:

    gcloud auth application-default login

**For service account credentials**

If you haven't already done so, follow the guide to
[create service account credentials](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#service-account) for your project.

- Make sure that your admin user and your service account have the `Service Account Token Creator` permission granted.

To authenticate, run the following command:

    gcloud auth application-default login --impersonate-service-account SERVICE_ACCOUNT_EMAIL

#### Run as a Gradle task

Run journeys by directly executing the Gradle task on the command line. After
running the task, test results will appear in the logs, and HTML and XML test
result files will be generated.

**To run all journeys**
You can run all journeys in the test suite with the following command.

    ./gradlew :app:testJourneysTestDefaultDebugTestSuite

**To run a single journey**
Use the `JOURNEYS_FILTER` to specify the name of the journey you want to run,
as follows:

    JOURNEYS_FILTER=your_journey_name.journey.xml ./gradlew :app:testJourneysTestDefaultDebugTestSuite

**To run all journeys in a subdirectory**
Set the `JOURNEYS_FILTER` to the subdirectory name. For example, the following
command runs all journeys in the `home` subdirectory within the test suite root
directory.

    JOURNEYS_FILTER=home ./gradlew :app:testJourneysTestDefaultDebugTestSuite

## View results

When Android Studio completes testing your journey, the test results panel
appears automatically to show you the results.
![The journey test results panel in Android Studio, displaying step
details and Gemini's reasoning.](https://developer.android.com/static/studio/gemini/images/journey-results.png) The journey test results panel in Android Studio, displaying step details and Gemini's reasoning.

Compared to other instrumented tests you might run in Android Studio,
there are some differences in how results for journeys are displayed.

- The **Tests** panel breaks down the journey into the discrete steps. You can click each step to find out more information about how Gemini executed it.
- The **Results** panel shows rich information to help you understand how Gemini understood and reasoned about your journey, and how it was executed.
  - The screenshots that were sent to Gemini are shown for visual aid at each action in the step.
  - Each action taken and Gemini's reasoning for why it took that action are described next to each screenshot.
  - Each action in the step is numbered.

## Known issues

- When testing a journey, all permissions for your app are granted by default.
- When testing a journey on a device running Android 15 (API level 35), you might see a warning on the device that says "**Unsafe App Blocked** " for "**AndroidX Crawler** ". You can click **Install anyway** to bypass this check. Alternatively, you can [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options) and disable the option to **Verify apps over USB**.