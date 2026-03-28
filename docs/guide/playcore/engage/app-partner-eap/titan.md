---
title: https://developer.android.com/guide/playcore/engage/app-partner-eap/titan
url: https://developer.android.com/guide/playcore/engage/app-partner-eap/titan
source: md.txt
---

Titan is an automated testing tool for
[Video Discovery API](https://developer.android.com/guide/playcore/engage/tv)
partners that validates the Continue Watching implementation in the following
ways:

- Creating a standardized method of automated testing to help you understand the expected behavior of Continue Watching.
- Allowing both Google and you to perform the same automated test cases, which provides transparency on the tests Google performs.
- Maximizing efficiency by providing an automated testing tool.

Titan is a tool that tests the end-to-end flow for Continue Watching. It doesn't
cover all testing but reduces manual testing. This version is for an external
pilot.

Titan is an APK that contains instrumentation tests. The
instrumentation tests simulate user actions based on the input file you provide.
Input configurations contain a list of deep links and parameters that the tool
uses to validate the Continue Watching behavior. The tool triggers the deep
links when it runs a test on a connected TV device and validates the parameters
of the updated Continue Watching entity.

> [!NOTE]
> **Note:** The TITAN tool is under active development and might have issues during testing. If you encounter any issues or have questions about the tool, contact `tv-titan@google.com`.

## Prerequisites

> [!NOTE]
> **Note:** Titan is licensed under the terms of the Google Trusted Tester Agreement that you or your company agreed to.

Download the following scripts and apps needed for testing:

- Titan APK
- PlaceHolder APK
- EngageVerify APK
- Sample `input_template.txt`
- `json_create.py`
- `titan_fromtext.sh`

TITAN performs testing in two modes:

- **Test Mode**
  - Your app must have `engage.service.ENV=production` removed from its manifest.
- **Production Mode**
  - Your app must include `engage.service.ENV=production` in its manifest.

Google primarily performs production mode tests when evaluating your apps. You
can use **Test Mode** during the implementation stage or for debugging issues.

## Set up your device and app

Follow these steps to set up your device and app to use Titan:

- Set up your device (for example, on a TV):

  - Enable **Stay awake** in [developer options](https://developer.android.com/studio/debug/dev-options#general).
  - Enable USB debugging and connect to the device using `adb`. You can also use wireless and wired IP `adb`.
- Manually install and sign in to your App Under Test (AUT).

- On AUTs with profile support, launch the app and select a user profile before
  running the test.

## Use the tool

Follow these steps to use the Titan tool for testing your Continue Watching
implementation.

### Set up your workstation

1. Place the assets that you downloaded from [Prerequisites](https://developer.android.com/guide/playcore/engage/app-partner-eap/titan#Prerequisites) into one directory.
2. Grant execute permissions to the following scripts by running `chmod u+x`:
   - `json_create.py`
   - `titan_fromtext.sh`

### Modify the input file

Modify `input_template.txt` to add the test content.

The following list describes each field:

- `package_name`: The package name of your app.
- `test_mode`: The test mode you want to use, either `PRODUCTION` or `TEST`.
- `URL`: The deep link that corresponds to the content and directly starts media playback on the device.
- `title`: The title of the content. For episodes, use the episode title, not the show title. The title value must be an exact match.

Episodes also require the following fields. For more details about each field,
see [TvEpisodeEntity](https://developer.android.com/guide/playcore/engage/tv#tvepisodeentity).

- `show_title`: The show title.
- `episode_number`: The episode number within the given season.
- `season_number`: The season number of which this episode is a part.

### Run the test

After you connect to the test device with `adb`, run the following command:

    ./titan_fromtext.sh ./input_template.txt

After the test starts, logs appear on the terminal during the setup phase.
During the test case execution phase, no logs appear until the test completes.
However, the device under test starts to run playback test cases. The tests
typically take about 20 minutes to run.

### Test results

The `Result.json` file is created in the same directory where the
`titan_fromtext.sh` script was executed. This JSON file contains results for
all test cases. If a test case passes, no additional details are available.

If a test case fails, the test result file shows one of the following error
codes:

`UNSPECIFIED_ERROR_CODE`
:   Unknown reason.

`INVALID_URL`

:   The deep link is invalid, and no playback is observed using the deep link.
    Validate the deep link using the following `adb` command:

        adb shell am start -a android.intent.action.VIEW \
                           -d "YOUR_DEEP_LINK" \
                           -p "YOUR_PACKAGE_NAME" \
                           --activity-clear-top \
                           --activity-clear-task

`NO_AUDIO`

:   No audio during playback, suggesting no video playback. Check the content for
    playback issues.

`ACTIVITY_NOT_FOUND`

:   No activity (with the package name) is found on the device. Check that the AUT
    is properly installed on the device.

`NO_ERROR`

:   Test case passed.

`ENGAGE_PARAMETER_MISMATCH`

:   Incorrect parameter detected. If a test fails with
    `ENGAGE_PARAMETER_MISMATCH`, the system also shows all read parameters to help
    you analyze the failure.

`EMPTY_ENGAGE_DATA`

:   No Continue Watching data was passed through. Check that the AUT is sending
    the data correctly using **TEST MODE**.

`TIMEOUT_ERROR`

:   The test case couldn't complete because Continue Watching data wasn't
    received in time. Check that the AUT is sending the data correctly using
    **TEST MODE**.

`INVALID_VIDEO_TYPE`

:   The movie or episode video type wasn't correctly specified. Check the test
    mode inputs.

`INVALID_TEST_MODE`

:   The test mode wasn't selected correctly. Check the test mode setting in the
    input file.