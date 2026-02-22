---
title: https://developer.android.com/docs/quality-guidelines/wear-app-quality
url: https://developer.android.com/docs/quality-guidelines/wear-app-quality
source: md.txt
---

The checklists on this page show various requirements to help you assess the
quality of your Wear OS app and follow the
[Principles of Wear OS development](https://developer.android.com/training/wearables/principles). Each requirement has a unique ID which
you might find helpful to use when you communicate with your team. Failing to
comply with all of the requirements might lead to rejection of your app
submission from the Play Store.

The [version history](https://developer.android.com/docs/quality-guidelines/wear-app-quality#version-history) section on this page shows how the checklist has
changed over time.

## Requirements

To publish on the Play Store, your watch app must satisfy all the applicable
requirements. In addition, your mobile app should [satisfy the
core app quality requirements](https://developer.android.com/docs/quality-guidelines/core-app-quality). To filter for guidelines that are relevant
to your app, select the **Apps** and **Watch faces** items
in the following interactive checklist:

| Quality requirement categories |
|---|
| Apps |
| Watch Faces |

### Target SDK version

> [!CAUTION]
> **Caution:** As of August 31, 2025, all new apps [must target Android 14 (API level
> 34) or higher](https://support.google.com/googleplay/android-developer/answer/11926878) to be submitted to Google Play. [Wear OS 5](https://developer.android.com/training/wearables/versions/5) is based on this version.  
>
> Also, as of the same date, apps targeting Android 12 (API level 31) or lower aren't discoverable from the Play Store on devices that run Wear OS versions higher than your app's target API level.

#### Test your app

Test your app and make sure it works on a watch running Wear OS 3.0 or
higher. If you pair your mobile device or emulator with a Wear OS emulator for
testing, check how your app behaves on each of these emulators:

- Wear OS small round 1.2" (192dp)
- Wear OS large round 1.39" (227dp)

Additionally, you can use [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to run tests written for your
standalone Wear OS app on physical Google Pixel Watch devices. Learn more about
the [supported physical Android devices](https://firebase.google.com/docs/test-lab/android/available-testing-devices) in Firebase Test Lab.

### Watch Face Format

**Note:**As of January 2026, the Watch Face Format is required for
installing watch faces on all Wear OS devices.

Learn more about the user-facing changes in this
[Help Center
article](https://support.google.com/wearos/thread/284572445).

### Visual experience

The following requirements let your app follow critical design and interaction
patterns to create a consistent, intuitive, and enjoyable user experience on
Wear OS:

| Area | Requirement | ID | Benchmark |
|---|---|---|---|
| Accessibility | User configured font size | `WO-V1` | Your app must [conform to the font size set by the user](https://developer.android.com/training/wearables/accessibility#support-user-font-size) in system settings. If the user selects a larger font size, ensure that text and controls do not overlap, and are not cut off by screen edges. |
| Accessibility | Touch targets | `WO-V2` | Provide a minimum of 48x48dp touch targets on your app. For more information, see [Accessibility on Wear OS](https://developer.android.com/training/wearables/accessibility#set-minimum). |
| Navigation | Back navigation | `WO-V3` | Allow users to swipe to close from almost all screens. Ongoing fitness activities or panning screens, such as an interactive map view, are exempt from this requirement, but you must provide a clear call to action to close the view. For more information, see the [Swipe to dismiss](https://developer.android.com/design/ui/wear/guides/components/swipe-to-dismiss) page. |
| Navigation | Ongoing activity | `WO-V4` | When a user has an [ongoing activity](https://developer.android.com/training/wearables/notifications/ongoing-activity), you must do the following: - Show the ongoing activity indicator on the watch face. - Update recent apps with the appropriate app launcher chip for the ongoing activity. - Reference the ongoing activity from the tile. (For more information, see [Ongoing activity tiles](https://developer.android.com/design/ui/wear/guides/surfaces/tiles#ongoing-activities).) |
| Navigation | Preserve app state | `WO-V5` | Preserve user or app-state when leaving the foreground and prevent accidental data loss due to back-navigation and other state changes. When your app is resumed within minutes of last use, such as from the recent app switcher, then restore the app state as close as possible to its previous state. |
| Navigation | App launcher | `WO-V6` | In the app launcher, correctly represent the app's icon and name, consistent with device implementation. For more information, see [Appear in recents and app resume](https://developer.android.com/training/wearables/apps/launcher). |
| N/A | N/A | `WO-V7` | *This is no longer a quality requirement for Wear OS apps.* |
| Navigation | Scroll bar | `WO-V8` | Display the scroll bar when the user interacts with a scrollable view. For more information, see [Show the scrollbar](https://developer.android.com/design/ui/wear/guides/surfaces/apps#show-scrollbar). |
| Tiles | Signed out state | `WO-V9` | If you include a tile with your app and the user is signed out, prompt the user to sign in when they open the tile. For more information, see [Empty states](https://developer.android.com/design/ui/wear/guides/surfaces/tiles#empty_states). |
| Tiles | Previews | `WO-V10` | If you include a tile with your app, add a tile preview to help your user see what content is shown in the tile manager on their watch and phone. For preview asset specifications see [Tiles design guidelines](https://developer.android.com/design/ui/wear/guides/surfaces/tiles#tile-previews). |
| N/A | N/A | `WO-V11` | *This is no longer a quality requirement for Wear OS apps.* |
| Visual quality | Show time (watch faces) | `WO-V12` | Display the time of day clearly on the watch face. |
| Visual quality | Black background | `WO-V13` | Use a black background for all apps and tiles. For more information, see [Color](https://developer.android.com/design/ui/wear/guides/styles/color). |
| Visual quality | Font size | `WO-V14` | Use a minimum font size of 12sp for essential text and 10sp for non-essential text. This allows the app text to be large enough to be read at a glance. For more information, see [Typography](https://developer.android.com/design/ui/wear/guides/styles/typography). |
| Visual quality | Splash screen | `WO-V15` | Show a 48x48dp app icon on a black background during app startup. The splash screen icon must match the app launcher icon. For more information, see [Branded launch](https://developer.android.com/design/ui/wear/guides/behaviors-and-patterns/launch#branded). |
| Visual quality | Watch shapes | `WO-V16` | App content must meet the following visual quality requirements: - Fits within the physical display area. - No text or controls overlap with each other. - No text or controls are cut off by the screen edges. - Larger or equal to a 192dp circle. For more information, see [Handle different watch shapes](https://developer.android.com/training/wearables/views/layouts). |

### Performance and functionality

Follow these requirements to configure your app correctly and provide the
expected performance and functional behavior:

| Area | Requirement | ID | Benchmark |
|---|---|---|---|
| SDK | Target API level | `WO-P1` | Ensure that your app meets Google Play's [target API level requirements](https://developer.android.com/google/play/requirements/target-sdk). |
| Stability | Basic user experience (apps) | `WO-P2` | Ensure that your app installs, launches, and completes necessary tasks without crashing. |
| Stability | Basic user experience (watch faces) | `WO-P3` | Ensure that the user can install, set, and personalize the watch face without crashing, including adding complications when applicable. |
| N/A | N/A | `WO-P4` | *This is no longer a quality requirement for Wear OS apps.* |
| Companion app | Companion app | `WO-P5` | For [non-standalone apps](https://developer.android.com/training/wearables/apps/standalone-apps), ensure that the companion app can connect with the Wear app and allows the user to use the Wear app as expected. For more information, see [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality). |
| Identity | Authentication | `WO-P6` | Your app must not ask the user to input a username or password directly on the Wear OS device. For more information about best practices, see [Authentication on wearables](https://developer.android.com/training/wearables/apps/auth-wear#auth-methods). |
| Battery | Always on Display - Watch Face Format | `WO-P7` | Has an Always on Display mode and illuminates no more than 15% of pixels. This is calculated as the average value across the watch face, with an fully-opaque white pixel having a value of 100% and a black pixel 0%. RGB colors are interpolated linearly between these two values. This check is repeated at approximately 10 minute intervals from the start to the end of a whole day, and every calculation must satisfy the 15% limit. |
| Performance | Memory Usage - Watch Face Format | `WO-P8` | Assets do not exceed the memory budget of 10 MB in ambient mode, and 100 MB in interactive mode. |
| N/A | N/A | `WO-P9` | *This is no longer a quality requirement for Wear OS apps.* |
| Complications | Complications - Watch Face Format | `WO-P10` | The watch face must have no more than 8 complication slots. |

### Google Play

Follow these requirements to configure your app consistently with other listings
and classifications on Google Play:

| Area | Requirement | ID | Benchmark |
|---|---|---|---|
| Play policies | Play policies | `WO-G1` | Your app must follow the [Play Developer Policy Center requirements](https://play.google.com/about/developer-content-policy/). |
| App details page | Play listing description | `WO-G2` | Your app listing on Google Play Store must adhere to the following: - List main features of the app. - Mention Wear OS. - Do not mention Android Wear. - Mention tile or complication if the respective surface is included in your app. - Be localized in languages offered by the app. |
| App details page | Play listing icons (apps) | `WO-G3` | Use the [Google Play icon design specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) for creating app icons. |
| App details page | Play listing icons (watch faces) | `WO-G4` | For single watch faces, the icon must do the following: - Accurately represent the watch face. - Not include text, graphics, or device frames that are not part of the watch face experience. Apps that include more than one watch face, or apps that are not solely watch faces, are exempt from this requirement. However, apps are more discoverable on the Play Store if they only have a single watch face. Use the [Google Play icon design specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) for creating app icons. |
| App details page | Play listing screenshots (apps) | `WO-G5` | Your app listing on Google Play Store must do the following: - Contain at least one screenshot that accurately depicts the current version of the app on Wear OS. - Provide screenshots showing only the app interface. - Not include transparent backgrounds or masking. - Not position the screenshots within device frames, or include additional text or graphics that are not part of the interface of the app. - Include screenshots with a 1:1 aspect ratio. If your app offers Tiles, then we recommend sharing a screenshot of Tiles functionality. For more information, see [Add preview assets to showcase your app](https://support.google.com/googleplay/android-developer/answer/9866151). **Note:** Android Studio (Hedgehog onwards) provides [Play-compatible screenshot functionality](https://developer.android.com/studio/run/emulator-take-screenshots). In the **Take screenshot** dialog, select **Play Store Compatible** in the drop-down menu to provide compatible screenshots for your app's review. |
| App details page | Play listing screenshots (watch faces) | `WO-G6` | Your watch face listing on Google Play Store must do the following: - Contain at least one screenshot that accurately depicts the current version of the watch face. - Show more than one of the available permutations, if the watch face is customizable. - Provide screenshots showing only the watch face experience. - Not position the screenshots within device frames, or include additional text, graphics, or backgrounds that are not part of the interface of the app. - Include screenshots with a 1:1 aspect ratio. For more information, see [Add preview assets to showcase your app](https://support.google.com/googleplay/android-developer/answer/9866151). |
| App publishing | App packaging | `WO-G7` | If your Wear OS app has an accompanying phone app, you must use the same package name and app signing key for your Wear app and phone app. For more information, see [Package and distribute Wear apps](https://developer.android.com/training/wearables/packaging#specifying-app-as-standalone). |
| App publishing | Login credentials | `WO-G8` | For apps with paid features, you must provide login credentials in the Google Play Console for testing of the full app experience. For more information, see **App Access** in [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455). |
| App publishing | Category tag | `WO-G9` | Self tag all watch face submissions on the Google Play Console with the appropriate categories that accurately represent the watch face. For more information, see [Self-tag watch faces](https://developer.android.com/training/wearables/watch-faces/self-tag). |
| App publishing | Number of watch face shapes declared | `WO-G10` | If you use a `watch_face_shapes.xml` file, it can contain only 10 distinct `<WatchFace>` elements, representing the different [watch face shapes](https://developer.android.com/training/wearables/wff/setup#declare-shape-support) that your watch face design supports. |
| App publishing | Source file size | `WO-G11` | The total size of the XML source file that defines your watch face design cannot exceed 10 MB. |
| App publishing | Use of up-to-date watch face tooling | `WO-G12` | If you use a watch face design tool, such as Watch Face Studio, the version of this tool must meet the following requirements: - Be compatible with Wear OS version requirements. - Support watch face features of the most recent Wear OS version. |

## Frequently asked questions


**After I submit my app for Wear OS review, how do I find out if my app doesn't meet all
of the requirements for Wear OS?**


If your app does not meet the usability requirements described on this page, the Play Store team
contacts you using the email address specified in the
[Google Play Console](https://play.google.com/console/) account associated with the
app.


**My app targets form factors other than just Wear OS. If my app does not meet the Wear OS
requirements, does my new or updated app still appear on Google Play for other devices?**


Updates to your Google Play store listing can only be published if all changes are approved. If
an update of a form-factor-specific artifact is blocking further updates to your listing for
other devices such as phones or tablets, you may want to remove that artifact by replacing it
with an empty submission until you can address the requirements.

For information about how to publish your Wear OS apps in Google Play, see
[Distribute to Wear OS](https://developer.android.com/distribute/best-practices/launch/distribute-wear).


**How do I manage policy violations and appeals?**


You can learn more about
[managing
policy violations and appeals](https://support.google.com/googleplay/android-developer/answer/9899142) in the Google Play policy center.

## Version history

The following table provides a summary of changed content on this page:

| Date | Description of change |
|---|---|
| May 15, 2024 | Several updates: - Specified a limit to the number of watch face shapes within a watch face source file (`res/xml/watch_face_shapes.xml`). - Clarified the total size limit of a watch face source file. |
| February 14, 2024 | Removed requirement to implement rotary input to scroll through screens in Wear OS apps (WO-V7). |
| January 3, 2024 | Added guidance on how to manage policy violations and appeals. |
| November 21, 2023 | Updated the Google Play Store app listing screenshot (WO-G5) guidelines to clarify that app listing images must not use transparent backgrounds or masking. |
| October 19, 2023 | Updated the accessibility (WO-V1) and watch shapes (WO-V16) guidelines to mention that elements shouldn't overlap with each other. This applies to text elements and content elements. |
| September 21, 2023 | Updated the scroll bar display requirement (WO-V8) to clarify when the scroll bar needs to be visible. |
| September 19, 2023 | Updated the splash screen requirement (WO-V15) to mention that the splash screen icon should match the app launcher icon. |
| August 31, 2023 | Renamed "upcoming requirements" to "requirements," now that they take effect. |
| August 22, 2023 | Updated memory usage requirements for Watch Face Format (WO-P8) to clarify memory budget separately for interactive mode and ambient mode. |
| August 14, 2023 | Removed requirements to set the standalone status in the app manifest, both for full apps (WO-P4) and for watch faces that use the Watch Face Format (WO-P9). |
| August 4, 2023 | Several updates: - Updated "Play listing icons (watch faces)" requirement (WO-G4). Icons must not include device frames that are not part of the watch face experience. - Updated "Play listing description" requirement (WO-G2). Apps don't need to update the Play Store description for every build. Apps must list main features of the app in the Play Store description. |
| July 13, 2023 | Several updates: - Removed requirement to show the time in Wear OS apps (WO-V11). Watch faces are still required to show the time. - Updated "app preserve state" quality requirement (WO-V5). - Updated target SDK version requirement. Apps can now target any version between Android 11 (API level 30) and Android 13 (API level 33), inclusive. |
| May 10, 2023 | Added requirements for apps that use the [Watch Face Format](https://developer.android.com/training/wearables/wff). |
| March 17, 2023 | Added reminder that app listings on Google Play should mention tiles or complications if the app supports them. |
| February 28, 2023 | Several updates: - Updated set of recommended emulators for testing. - Added requirement to target Android 11 (API level 30) or higher. - Added a set of upcoming requirements that take effect on August 31, 2023. |
| February 9, 2023 | Added guideline about self-tagging watch faces. |
| March 8, 2022 | Clarified that independent apps are allowed to use a companion app for login workflows. |
| December 10, 2021 | Added guideline to test apps on Wear OS 3. |
| October 19, 2021 | Added guideline for the icon associated with a watch face (WO-F4). |
| August 20, 2021 | Clarified guidelines around screenshot format and content (WO-F2). |
| May 18, 2021 | Several updates: - Added notification guidelines for channels and priorities, and added a reminder that cross-promotion campaigns aren't allowed in notifications (VX-S1). - Added messaging guidelines for direct reply and direct share ranking (VX-S2). - Suggested several emulators on which to test Wear OS apps. |
| November 9, 2020 | Clarified that independent apps shouldn't require users to install companion apps on mobile devices. |
| March 14, 2017 | Initial version published. |