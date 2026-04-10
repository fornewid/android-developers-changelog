---
title: https://developer.android.com/games/pgs/integrate-achievements
url: https://developer.android.com/games/pgs/integrate-achievements
source: md.txt
---

This document explains how to integrate achievements into your game using the
Google Play Console or API calls. It covers
the essential elements and states of achievements, and describes how to create,
import, and manage them.

## Before you begin

- Review the [design high quality achievements](https://developer.android.com/games/pgs/achievements#design-achievements) guidelines.

- Review the terminology in
  [achievements basics](https://developer.android.com/games/pgs/achievements#achievements-basics).

### Create or import new achievements

<br />

To implement achievements from scratch, follow these steps:

#### Add achievements

There are two ways to create achievements for the first time using the
Google Play Console:

- [Create an achievement](https://developer.android.com/games/pgs/integrate-achievements#create-achievement): Add definitions and metadata for each achievement one at a time.
- [Import achievements](https://developer.android.com/games/pgs/integrate-achievements#import-achievements): Import definitions and other metadata for multiple achievements together in a single step.

<br />

> [!NOTE]
> **Note:** Use APIs to [unlock achievements](https://developer.android.com/games/pgs/android/achievements#unlock_achievements) for the signed in player. This will reveal any hidden achievements to the player.

##### Create an achievement

To create an achievement for a new and unpublished game, complete these
steps:

1. In the [Google Play Console](https://play.google.com/console), select a game.
2. In the **Play Games Services - Achievements** page (**Grow users \> Play Games Services \> Setup and management \> Achievements** ), select **Create achievement**.
3. In the **Add achievements** page, complete the form.
4. Click **Save as draft**.
5. After you have created an achievement, you need to [publish your achievements](https://developer.android.com/games/pgs/integrate-achievements#publish-achievements).

##### Import achievements

To add multiple achievements to your game at once, use the following steps:

1. Create a zip file containing your achievements.
2. Upload the file.

For more information about the zip file, see
[Zip file guidelines](https://developer.android.com/games/pgs/integrate-achievements#zip-file).

To import achievements:

1. In the [Google Play Console](https://play.google.com/console), select a game.
2. In the **Play Games Services - Achievements** page (**Grow users \> Play Games Services \> Setup and management \> Achievements** ), select **Import achievements**.
3. In the **Import achievements** page, click **Upload**.
4. Select the zip file to upload.
5. Click **Save as draft**.
6. After you have imported achievements, you need to [publish your game](https://developer.android.com/games/pgs/integrate-achievements#publish-achievements).

#### Zip file guidelines


You can import multiple achievements at once using a zip file. Refer to the
table for the precise filenames to use in your zip file:

| Filename | Required or Optional | Accepted values |
| Filename | Required or Optional | Accepted values |
|---|---|---|
| [`AchievementsMetadata.csv`](https://developer.android.com/games/pgs/integrate-achievements#achievementsmetadatacsv-format) | Required | Metadata for each achievement. See [Attributes](https://developer.android.com/games/pgs/integrate-achievements#attributes). |
| [`AchievementsLocalizations.csv`](https://developer.android.com/games/pgs/integrate-achievements#achievementslocalizationcsv-format) | Optional | Provides translations for achievement names and descriptions. |
| [`AchievementsIconsMappings.csv`](https://developer.android.com/games/pgs/integrate-achievements#achievementsiconsmappingscsv-format) | Optional | Maps achievements to their icon files. |
| [Icon files](https://developer.android.com/games/pgs/integrate-achievements#icon-files) | Optional | Icons in PNG, JPEG, or JPG format. |

Zip file requirements:

- No subdirectories.
- Unique file names.
- Only CSV, PNG, JPEG, or JPG files.
- The CSV files mustn't have a header row.
- Each file must be under 1 MB.
- The zip file shouldn't contain more than 403 files.
- Total zip file size must be under 800MB.

##### AchievementsMetadata.csv format

The `AchievementsMetadata.csv` file contains the metadata for each
achievement. It should include the information as comma-separated values in the
following order:

```
    Name,Description,Incremental value,Steps Needed,Initial State,Points,List Order
```

These fields are described in the following table:

| CSV column headers | Required or Optional | Accepted values |
| CSV column headers | Required or Optional | Accepted values |
|---|---|---|
| Name | Required | Maximum of 100 characters |
| Description | Optional | Maximum of 500 characters |
| Incremental Value | Required | `True` or `False` |
| Steps Needed | Required if `Incremental Value` is `True.` | Number (no fractions or decimals). The maximum value is 10000. |
| Initial State | Required | `Hidden` or `Revealed` |
| Points | Required | Number that is a multiple of 5, and the value must be between 5 and 200 |
| List Order | Optional | Number (no fractions or decimals, and greater than zero) |

AchievementsMetadata.csv file requirements:

- Each row must have seven values. If you want to omit a value, leave it blank.
- The `Name` and `Description` fields are used as the default locale.
- The `Name` field should be unique across all achievements.
- The following fields shouldn't contain commas: `Name` and `Description`.

A sample `AchievementsMetadata.csv` file:

```
  Achievement1,Achievement One,True,100,Hidden,5,20
  Achievement2,Achievement Two,False,,Revealed,10,30
```

##### AchievementsLocalizations.csv format


The `AchievementsLocalizations.csv` file is an optional file that sets
up all the data that is needed to describe each achievement to users in
different locales. Achievements are translated in alignment with the locales
specified for the game.


It should include the information as comma-separated values in the following
order:

```
   Name, Localized name, Localized description, locale
```


These fields are described in the following table:

| CSV column headers | Required or Optional | Description | Accepted values |
| CSV column headers | Required or Optional | Description | Accepted values |
|---|---|---|---|
| Name | Required | Must match the `Name` column from `AchievementsMetadata.csv`. | Maximum of 100 characters |
| Localized name | Required | The localized name for the achievement. | Maximum of 100 characters |
| Localized description | Optional | The localized description for the achievement in the specified locale. | Maximum of 500 characters |
| Locale | Required | The locale code such as `en-US`. | [Add translations](https://developer.android.com/games/pgs/console/enable-features#add_translations) for your game before specifying a locale. Note that you cannot specify the default locale. Supported locale codes can be found in the list of [supported languages](https://support.google.com/googleplay/android-developer/table/4419860). |

`AchievementsLocalizations.csv` file requirements:

- Achievement names within a game must be unique per locale. For example, if a game supports both en-US and fr-FR locales, an achievement
  named "Achievement1" for en-US can also be named "Achievement1" for fr-FR.

- Each row should have four values. If you want to omit the Localized description value, leave it blank.

A sample `AchievementsLocalizations.csv` file:

```
Achievement1,Achievement One,This is the description of achievement one in English.,en-US
Achievement1,Achievement Un,Voici la description de l'achievement un en français.,fr-FR
Achievement2,Achievement Two,Description of achievement two.,en-US
Achievement2,Logro Dos,Descripción del logro dos.,es-ES
Achievement3,Achievement Three,,en-US
Achievement3,Erfolg Drei,,de-DE
```

##### AchievementsIconsMappings.csv format


The `AchievementsIconsMappings.csv` file is an optional file that
is used to map your achievements with the given icon. It should include the
information as comma-separated values in the following order:

```
Name, icon filename
```


These fields are described in the following table

| CSV column headers | Required or Optional | Description |
| CSV column headers | Required or Optional | Description |
|---|---|---|
| Name | Required | Must match the `Name` column from `AchievementsMetadata.csv`. |
| Icon filename | Required | The name of your icon file. |

`AchievementsIconsMappings.csv` file requirements:

- Each row should have two values.
- Icons files can only be in PNG or JPEG formats.

A sample`AchievementsIconsMappings.csv` file:

```
Valid Achievement,valid-achievement-icon.png
Incremental Achievement,incremental-achievement-icon.jpeg
No Description,no-description-icon.png
Hidden Initial State,hidden-initial-state-icon.png
Large Point Value,large-point-value-icon.jpeg
```

#### Icon guidelines

Icons should be created as 512 x 512 PNG, JPEG, or JPG files. You only need to
provide us with the icon for the unlocked achievement. We will generate a
grayscale version for the revealed icon automatically. For that reason, we
recommend your achievement icons include colorful elements, so your users can
distinguish between revealed and unlocked achievements.

When an achievement icon is displayed in an Android
\[toast\]\[a\], the icon is overlaid with a
circle and its outer corners are hidden. Make sure that your icon still looks
good under these circumstances.
![A sample achievement icon.](https://developer.android.com/static/images/games/pgs/achievementIconExample.png) A sample achievement icon.

The same icon is used in all locales, so we recommend against including any
text or localized content in an icon.

##### Icon files

Icons you reference in `AchievementsIconsMappings.csv` file must
exist in the current zip archive you import.

<br />

### Update games with existing achievements

You can add more achievements to a game and update existing ones in the
Google Play Console.

<br />

<br />

#### Add more achievements

If you already have existing achievements and want to add more:

1. In the [Google Play Console](https://play.google.com/console), select a game.
2. In the **Play Games Services - Achievements** page (**Grow users \> Play Games Services \> Setup and management \> Achievements** ), select **Add achievements**.

##### Edit achievements

If you already have existing achievements and want to edit:

1. In the [Google Play Console](https://play.google.com/console), select a game.
2. In the **Play Games Services - Achievements** page (**Grow users \> Play Games Services \> Setup and management \> Achievements**), select an achievement.
3. You can edit any of the fields.
4. Click **Save as draft**.
5. In the **Play Games Services - Achievements** page, the edited achievement is in the "Available to testers" status.
6. After you test the achievement, click **Review and publish** .

   This republishes your game, along with all your updated achievement.

> [!NOTE]
> **Note:** Once an achievement is published, its initial state (hidden or revealed) and its type (incremental or standard) is fixed and can't be changed.

##### Delete an achievement

Once your achievement has been published, it **cannot** be deleted.
You can only delete an achievement in a pre-published state

1. In the **Play Games Services - Achievements** page, select an achievement.
2. To delete the achievement, click **delete achievement**.

##### Reset an achievement

You can only reset player progress data for your draft achievements.

1. In the **Play Games Services - Achievements** page, select an achievement.
2. To reset achievements, click **Reset progress**.
3. To reset achievement data programmatically, call the [Management API `Achievements` methods](https://developer.android.com/games/services/management/api/achievements).

<br />

## Add translations for achievements

You can specify your own translations for achievements that are associated with
your game. Before you do so, first make sure to complete the steps described in
[Adding translations for your game](https://developer.android.com/games/pgs/console/enable-features#add_translations).

There are two ways in which you can add translations for your game:

- You can use the [import achievements](https://developer.android.com/games/pgs/integrate-achievements#import-achievements) option to upload
  translations for many new achievements at once. You cannot use this option to
  upload translations for already existing achievements.

- You can add translations for each achievement in your game.
  To add your own translation for each achievement:

  1. In the Google Play Console open the **Achievements** tab for your game, then select an existing achievement.
  2. In the achievements details page, select the tab for a language that you previously added in the **Game details** tab.
  3. In the achievement details page for that language, edit the form with your translations for that achievement.
  4. Click **Save** to store your translated achievement details.

## Client implementations

To learn how to implement achievements for your platform, see the following
resources:

- [Android](https://developer.android.com/games/pgs/android/achievements)
- [Unity](https://developer.android.com/games/pgs/unity/achievements)
- [Web](https://developer.android.com/games/services/web/api/rest#achievements)

## Testing achievements

> [!NOTE]
> **Note:** During testing, it is normal that the "achievement unlock" popup shows 0 XP gained. This is to prevent interfering with live scoring systems.

To verify that the achievements work as intended, follow the steps to test them:

- Set up an [internal test track](https://support.google.com/googleplay/android-developer/answer/9845334).
- [Add test accounts](https://developer.android.com/games/pgs/console/publish) to your game project for testers.
- Create Play Games Services profile for one of the test account using Play Games App.
- Open the game using the same test account for which you created the Play Games Services profile.
- Verify that Play Games Services "Welcome toast" is shown on the screen as a confirmation of successful automatic authentication on game launch.
- Play the game and complete the required steps to unlock the achievements.
- To verify achievements:

  - Verify that "achievement unlocked" popup is shown on the screen when the
    achievement is completed.

  - Open the **Play Store** app and verify that the achievements section on
    **YouTab** shows completed as well as in-progress achievements (with
    progress details).

### Track achievement performance in Play Console

Here's how to find quick statistics for individual achievements:

- In the [Google Play Console](https://play.google.com/apps/publish/).
- Go to **Settings\> Game projects**.
- Select a game.
- On the left-hand menu, click **Achievements**.
- On your **Achievements** page, you can find statistics to understand whether your players are unlocking the achievements. For those whose achievements are not hidden, you can see what percentage are unlocking them. For early stage achievements, the unlock percentage is typically closer to 100%.

You can also track time series performance of achievements in the
**Grow users \> Play Games Services \> Game statistics** page.

## Publish the achievements

Once you finish testing, you must publish your game.
All of your game's achievements are published with it. Publishing achievements
is a required step for achievements to function properly.

To publish, follow these steps:

1. In the [Google Play Console](https://play.google.com/console), select a game.
2. In the **Play Games Services - Achievements** page (**Grow users \> Play Games Services \> Setup and management \> Achievements** ), click **Review and publish**.
3. In the **Play Games Services - Publishing** page (**Grow users \> Play Games Services \> Setup and management \> Publishing**), review the actions and fix the issues.
4. Click **Publish** .

   All of your game's achievements are published.

## Common mistakes to avoid

These points highlight common mistakes to avoid when implementing achievements
in a game. They emphasize the importance of:

- In the Play Console, go to
  **Grow users \> Play Games Services \> Setup and management \> Achievements**.

  - Before publishing, verify that achievements configured in the Play Console are not in "Draft" state.
  - Don't add achievement ID values from the Play Console to the game code. Use the [client implementations](https://developer.android.com/games/pgs/integrate-achievements#client-implementations) instead.
- Make sure you have also implemented the unlock logic on your client.

  - Players cannot skip the trigger step where the unlock API is called. For example, completing the tutorial is an achievement, but players can skip the tutorial itself.