---
title: https://developer.android.com/ai/appfunctions/create-manage-connected-apps
url: https://developer.android.com/ai/appfunctions/create-manage-connected-apps
source: md.txt
---

Use Google Connected Console to integrate your Android app's on-device
AppFunctions with Gemini on Android. By creating a connected app with the
Android MCP connection type and linking it to your Play app, you enable Gemini
on Android to trigger actions and complete tasks directly in your app on behalf
of users.

This guide walks you through the end-to-end self-service workflow in Google
Connected Console, including connected app creation, Play app linking, public
app card configuration, app bundle upload and submission, on-device preview
testing, and production publishing.

> [!NOTE]
> **Note:** By default, Google Connected Console sends release notification emails to users in your developer account who have permissions to manage your Play production releases. Use a dedicated test Play app during early development if you want to keep test activity separate from your production Play app.

## Prerequisites

Before you begin, make sure you have the following:

- **Access to a registered developer account in
  [Google Connected Console](https://connected.google.com/console)** :
  - **Terms of Service acceptance**: The first time your organization accesses Connected Apps in Google Connected Console, an account owner or admin must review and accept the Connected Apps Terms of Service before team members can create Connected Apps.
  - **User permissions** : If you were invited to an existing Connected Console developer account but can't create Connected Apps, ask your account owner or admin to grant you the **View Connected Apps** or **Create and manage Connected Apps** permission on the **Users and
    permissions** page. You also need release management permissions for your relevant Play app to upload app bundles and manage releases.
- **An existing Play app in your Google Connected Console account** :
  - Your Play app must already exist in the same developer account so you can link it to your connected app. Each Play app can only be linked to a single Android MCP connected app.
  - Ensure your Play app has a default store listing configured with an app icon and supported languages. Your Play app's store listing languages and country targeting determine where your Android MCP connected app is available.
- **An Android App Bundle (`.aab`) with implemented AppFunctions** :
  - Configure your app bundle to target Android mobile devices, which is the supported platform for on-device Gemini app integration.
- **Connected app category and public-facing metadata** : Prepare the assets and details that make up your connected app's public presence:
  - **Connected app category**: The domain or industry category for your connected app. Each category defines baseline capability requirements and can't be changed after creation.
  - **App name** : The display name for your connected app shown to users across Google products, and used when users mention your app with `@` in Gemini.
  - **Connected app icon**: A 512 px x 512 px app icon in JPEG or PNG format, with a maximum file size of 1 MB (1,024 KB).
  - **App description**: A concise summary describing what your connected app can do for users.
  - **App capabilities**: At least three custom capabilities that show users what your app can do when deciding whether to connect, in addition to any default capabilities defined by your app's category.
  - **Example prompts**: At least three sample prompts that teach users how to invoke your app in Gemini, and help them understand what they can ask.
  - **Policy URL**: A publicly accessible URL for your Privacy Policy.
  - **Terms of Service URL**: A publicly accessible URL for your Terms of Service.
  - **Website URL** *(optional)*: A publicly accessible URL pointing to your website for attribution.

## Register, test, and publish AppFunctions with Gemini

Once you have met the prerequisites, complete the following steps to register
your Android MCP connected app, link your Play app, populate your app details,
upload and submit your AppFunctions, test on-device, and publish to production.

### Step 1: Create an Android MCP connected app and link it to your Play app

To create a connected app and link it to your Play app, follow these steps:

1. Sign in to [Google Connected Console](https://play.google.com/console/developers).
2. On the **Home** page, select **Create app**.
3. In the **Choose what to create** dialog:
   - If prompted to accept the Connected Apps Terms of Service, select **View
     terms** , review and accept the agreement, and then select **Create**. Only an account admin can accept the agreement.
   - Otherwise, select **Create** in the **Connected app** card.
4. In the **Give your connected app a name** dialog, type a name for your connected app. This is the name that displays your connected app across Google products, and is how users mention your connected app using `@`. Select **Next**.
5. In the **Select a connected app category** dialog, select your app's domain,
   category, or industry from the **Select a category** menu.

   > [!NOTE]
   > **Note:** Your connected app category defines baseline capability requirements and can't be changed later. To use a different category later, you must create a new connected app.

6. In the **Choose connection type** dialog, choose **Android MCP**.

   For a detailed walkthrough on setting up an MCP server connected app, see
   the [Google Play Console integration guide](https://developer.android.com/connected-apps/gpc). For now, you can only
   choose one connection type per connected app, and you can't change it later.
7. Select **Create connected app**.

8. In the **Select app** dialog, find the Play app that contains (or will
   contain) your AppFunctions, and select it. You can filter the list using the
   search.

   - Play apps that are already linked to another connected app can't be selected.
   - Make sure to select the correct Play app you want to link. Once you select a Play app, it can't be changed.

This opens the management overview page for your connected app, where you can
continue to configure your connected app details, track your connected app
versions, and manage testers.

### Step 2: Provide your connected app details

Before uploading any app bundles containing AppFunctions, configure how your
connected app appears to users in Gemini.

> [!IMPORTANT]
> **Important:** You must populate and save your connected app's **App details** before uploading an app bundle that contains AppFunctions. Google Connected Console only generates an Android MCP version from an uploaded app bundle when required connected app details are already provided. If you upload your app bundle before providing these details, complete **App details** first and then either delete and re-upload your app bundle, or upload a new app bundle with an incremented version code.

Follow these steps to provide your connected app details:

1. On your connected app's management page, inside the **Android MCP** card under **Add connected app details** , select **Add app details** (or **Manage** if updating existing details).
2. At the top of the **App details** page, verify the **Connected app name** field. You can update the name if needed. This is shown to users across Google products, and used when users mention your app with `@`.
3. In the **Public details** section, under **Icon**, upload your app icon (JPG or PNG, up to 1 MB, and 512 px x 512 px).
4. Complete the following fields:

   - **Description**: Enter a concise, single-sentence summary (under 30 words) describing the main features of your connected app and what it can do. This text is displayed to users, and isn't used as model instructions.
   - **Capabilities** : Enter at least three high-value tasks that your connected app can perform. Select **Add capability** to add more entries. Don't include numbers at the beginning of your capabilities. Include only a single capability per entry. If your connected app category includes predefined capabilities, they appear at the top of the list and can't be modified.
   - **Example prompts** : Enter at least three example prompts that help users understand what they can ask. Select **Add example prompt** to add entries.
     - Start at least **two prompts** with `@<YourAppName>` (for example, `@Order Tracker where is my last order?`).
     - Mention `<YourAppName>` **naturally in at least one prompt** without starting with your app name (for example, `Track my recent order on
       Order Tracker`).
     - Don't include numbered prefixes (`1.`, `2.`, `3.`) or wrap prompts in quotation marks (`"..."`).
   - **Multi-language localization** : To provide translations for
     **Description** , **Capabilities** , and **Example prompts**, wrap each
     locale's text in language tags within the input field. For example:

         <en-US>
         Play music, manage playlists, and discover artists
         </en-US>
         <es-ES>
         Reproduce música, gestiona listas y descubre artistas
         </es-ES>

     Connected Console automatically validates your tags and displays the
     detected locales under each field (for example, `Found translations for
     2 languages: en-US, es-ES`).
   - **Terms of Service URL** : Enter a valid `https://` or `http://` link to
     your Terms of Service.

   - **Policy URL** : Enter a valid `https://` or `http://` link to your
     Privacy Policy.

   - **Website URL** *(optional)*: Enter a link to your website for
     attribution purposes.

### Step 3: Upload an app bundle containing your AppFunctions and submit your connected app

After saving your connected app details, upload an Android App Bundle containing
your AppFunctions to your linked Play app and submit the connected app version
for testing.

To upload an app bundle containing your AppFunctions, follow these steps:

1. On your connected app's management page, in the **Android MCP** card under **Upload an app bundle that contains your AppFunctions** , select **Upload
   app bundle** to go to your linked Play app's **Test and release** overview.
2. Alternatively, open your linked Play app directly in Google Connected Console. In your Play app's left navigation menu, go to **Testing \> Internal
   testing** (or another test track) and select **Create new release** (or **Edit release** if you already have a draft release).
3. Under **App bundles** , select **Upload** to upload your `.aab` bundle with AppFunctions, or select **Add from library** if you uploaded the bundle after completing [Step 2](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-2-provide-details).
4. Once the upload finishes, go to the **App functions were detected in your
   app bundle** section on the release page. Confirm that your connected app name, bundle version code, detected tool count, language count, and Play app country targeting appear as expected, and verify that automated checks report no issues. (If any validation errors appear, follow the instructions in [Troubleshoot issues related to AppFunctions](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#troubleshoot-appfunctions) before continuing.)
5. At the bottom of the release page, select **Submit connected app and
   continue**.

Selecting **Submit connected app and continue** submits your AppFunctions
version to Gemini for preview testing and advances your Play release to the
release preview page. If you want to iterate on AppFunctions using local builds
without incrementing your app bundle's version code, **leave the Play release in
a Draft state** and don't select **Save and publish**. Publishing a Play release
locks that bundle version code so it can no longer be deleted and re-uploaded.
Any subsequent changes require an incremented app bundle version code. (If your
testers install the app directly from Google Play's internal testing track
rather than sideloading, complete the internal testing rollout and increment
your version code on future uploads.)

### Step 4: Verify your connected app version

After submitting your connected app from the Play release page, verify that the
connected app version is ready for preview:

1. On your connected app's management page, in the **Android MCP** card, next to **Versions** , select **View**.
2. On the **Versions** page, confirm that your submitted version appears in the **Available to testers** section (displaying `Version <N> • Submitted
   <Date> • Using AppFunctions from app bundle <versionCode>`).
   - Select **View** on any version row to inspect the detected **AppFunctions** and the read-only **App details** snapshot captured for that version.
   - Versions created from an uploaded app bundle where you haven't yet selected **Submit connected app and continue** appear under **Pending
     submission**.

### Step 5: Test your connected app

To make your connected app available to testers, you must add them on the
**Manage testers** page. Only users you add to your testers list can see and
interact with your unpublished connected app. You can only add testers with an
`@gmail.com` account.

1. On your connected app's overview page, in the **Test your app** card, select **Add testers** (or **Manage testers** if you've already added some).
2. On the **Manage testers** page, select existing email lists or select **Create email list** to add the Google Accounts authorized to test your integration. Make sure to include your own email address if you want to test the app yourself.
3. Select **Save**.

   > [!NOTE]
   > **Note:** Once you add testers, it can take up to 10 minutes for your connected app to become visible to those accounts.

4. Testers in the Gemini app can invoke your connected app by typing `@`
   followed by your connected app's name and selecting it from the menu. You
   can also view and connect your app in Gemini by navigating to **Settings \&
   help \> Connected apps** in the left navigation bar.

Before testing on-device, confirm that each tester meets the following
requirements:

- Signed in on an Android mobile phone or tablet using a Google Account included in the email list configured in [Step 5](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-5-test-connected-app).
- Running the exact Android app build whose bundle version code matches the version submitted in [Step 4](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-4-verify-version).

We recommend thoroughly testing your integration:

- Try all of your **Example prompts**.
- Test both explicit `@<AppName>` invocations and natural-language queries.
- Verify tool parameter handling, confirmation prompts, and end-to-end execution across your AppFunctions.

> [!NOTE]
> **Note:** You can also debug your connected app in Gemini Developer Mode, where you can interactively test your Model Context Protocol (MCP) server, diagnose schema or runtime errors, and benchmark tool quality before submitting your connected app for review in Google Connected Console. Make sure you are signed into Gemini with an account.

When you are satisfied with your testing, you are ready to submit your connected
app to Google for review.

### Step 6: Publish your connected app to users

Unlike server-hosted MCP integrations, an **Android MCP** connected app doesn't
require a separate review or publish action on the Connected app management
page. Instead, your connected app version is reviewed by Google and published
automatically when you release the Play app version containing your AppFunctions
app bundle to production.

When you have completed testing and are ready to launch to users:

1. In Google Connected Console, open your linked Play app and navigate to **Release \> Production** in the left navigation menu (or promote your tested release from a testing track to **Production**).
2. Select **Create new release** (or edit an existing draft production release) and add the app bundle containing your verified AppFunctions using **Add
   from library** or **Upload**.
3. Go to the **AppFunctions were detected in your app bundle** section to confirm your connected app version, tool count, store listing language count, and Play app country targeting, and ensure automated checks show no blocking issues.
4. Select **Submit connected app and continue**, complete your release details, and submit your Play app production release for review and rollout.

> [!NOTE]
> **Note:** Connected Apps are reviewed by Google alongside your Play app release, which may increase the time it takes to review your Play app. Until your production release is approved and rolled out, your connected app integration remains visible only to the testers configured on your connected app.

Once your Play app production release is approved and rolled out:

- Your Android MCP connected app becomes available in Gemini on Android to users in the countries and languages targeted by your Play app.
- On your connected app's management page (**Connected Apps \> Manage** ), the **Connected app status** card updates to **Published** , displaying the live app bundle version code and publication date, and the version appears under **Published** on the **Versions** page.
- To ship updated AppFunctions tools later, build a new app bundle with an incremented version code, test it using a test track, and publish a new **Production** Play release. If you also want to update your connected app's public metadata (such as capabilities or example prompts), save those edits under **Connected Apps \> Manage \> App details** before uploading your new app bundle.

## Update your app bundle to adjust AppFunctions

If you want to iterate on AppFunctions during internal testing without
incrementing your Android app's version code, you can remove and delete an
unpublished draft app bundle before re-uploading:

1. Update the AppFunctions implementation in your Android project and generate a new `.aab` app bundle.
2. Remove the previous app bundle from any draft release where you added it:
   1. Open your linked Play app in Google Connected Console and select **Internal testing** (or the track containing your draft release) in the left navigation menu.
   2. On your draft release, select **Edit release**.
   3. Locate the app bundle, select the three-dots menu (**⋮** ), and select **Remove app bundle**.
   4. Select **Save as draft**.
3. Delete the unused app bundle from your library:
   1. In your Play app's left navigation menu, select **Latest releases and
      bundles** (if you don't see the bundle listed, select **View all app
      bundles**).
   2. Open your app bundle's details and, if the **Delete app bundle** button is available, select **Delete app bundle**. This frees the version code so you can upload the updated app bundle without incrementing the version code.
4. If **Delete app bundle** is unavailable (for example, because the release was already published to a track), increment the `versionCode` in your app build configuration, generate a new app bundle, and upload and submit the new version as described in [Step 4](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-4-verify-version).

## Troubleshoot issues related to AppFunctions

Use the following guidance to resolve automated check errors and common setup
issues.

### Resolve automated check errors on a release

Any issues identified by automated AppFunctions checks appear on the release
preparation page (such as **Create internal testing release** ) and under the
**Failed** section (with a **Fix issues to publish** badge) on your connected
app's **Versions** page.

If automated checks report issues with your app bundle, perform the following
steps:

1. Fix the underlying AppFunctions issues in your Android app code and build an updated app bundle.
2. If your previous release is still a draft and you want to reuse the same version code:
   1. In your Play app's left navigation menu, select **Internal testing** (or the relevant track) and select **Edit release** on your draft release.
   2. Select the three-dots menu (**⋮** ) next to the app bundle and select **Remove app bundle**.
   3. Select **Save as draft**.
   4. In the left navigation menu, select **Latest releases and bundles** (select **View all app bundles** if needed), select the bundle, and select **Delete app bundle**.
   5. Return to your draft release, upload the fixed app bundle, and select **Submit connected app and continue**.
3. If the previous bundle can't be deleted, increment your app bundle's `versionCode`, upload the new bundle to your release, and select **Submit
   connected app and continue**.

### Common setup and integration issues

The following table describes common issues you might encounter during connected
app setup, bundle upload, or testing, along with their causes and resolutions:

| Issue | Console message or symptom | Cause | Resolution |
|---|---|---|---|
| **App bundle uploaded before creating or linking a connected app** | Release page shows **Create or link connected app**. | The uploaded `.aab` contains AppFunctions, but the Play app isn't yet linked to an Android MCP connected app. | Complete [Step 1](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-1-create-connected-app) through [Step 3](https://developer.android.com/ai/appfunctions/create-manage-connected-apps#step-3-upload-and-submit) to create a connected app, select **Android MCP** , link your Play app, and save **App details** . Then either delete and re-upload the app bundle or upload a new bundle with an incremented `versionCode`. |
| **App bundle uploaded before saving connected app details** | Release page shows **Connected app details required** and a **Provide connected app details** button. | The Play app is linked to an Android MCP connected app, but required fields on the **App details** page weren't saved before the bundle was uploaded. | Select **Provide connected app details** (or go to **Connected Apps \> Manage \> Add app details** ), complete and save all required fields, and then delete and re-upload the bundle or upload a new bundle with an incremented `versionCode`. |
| **Play app can't be selected when linking** | Target Play app shows an **Already linked** badge or doesn't appear in the **Select app** dialog. | Each Play app can only be linked to one Android MCP connected app, or the Play app hasn't been created in this developer account yet. | Check existing entries under **Connected apps** to see if another connected app already links to your Play app, or create the Play app in Google Connected Console first before linking. |
| **Can't create a connected app** | The option to create a connected app doesn't exist, or creating a connected app displays a permissions or Terms of Service warning. | Your user account lacks connected apps permissions, or an account owner or admin hasn't yet accepted the Connected Apps Terms of Service. | Ask an account owner or admin to accept the Connected Apps Terms of Service and grant your account **View Connected Apps** or **Create and manage Connected Apps** on the **Users and permissions** page. |
| **Connected app version stuck in "Pending submission"** | On **Connected Apps \> Manage \> Versions** , your bundle version appears under **Pending submission** instead of **Available to testers**. | Google Connected Console detected AppFunctions in your uploaded bundle, but the connected app version hasn't been submitted from the release page. | Open the Play app release containing that bundle and select **Submit connected app and continue** so testers can preview it. |
| **Example prompts validation error on App details page** | **Public app card** form can't be saved and displays an error under **Example prompts**. | Prompts don't meet formatting or mention rules, or **App name** was edited after writing prompts. | Provide three to four prompts total: start at least two with `@<YourAppName>`, mention `<YourAppName>` naturally without `@` in at least one, and remove numbered prefixes (`1.`, `2.`) or surrounding quotes (`"..."`). |
| **Connected app not visible to testers in Gemini on Android** | Testers can't find the connected app under **Connected Apps** or using an `@` mention in the Android Gemini app. | Propagation is still in progress, the tester account isn't eligible, or the installed app version doesn't match. | Wait about 20 minutes after submission (and up to 10 minutes after saving testers). Confirm the tester uses a personal `@gmail.com` account on the saved email list, uses an Android phone or tablet, and has installed the exact submitted bundle version. |