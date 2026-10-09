---
title: https://developer.android.com/develop/adaptive-apps/guides/googlebook/cross-device-continuity
url: https://developer.android.com/develop/adaptive-apps/guides/googlebook/cross-device-continuity
source: md.txt
---

Users frequently begin tasks on their Android phone---such as reviewing a
document, triaging messages, or browsing an assortment of items---and then
want to move to a Googlebook with its larger display, physical keyboard, and
multi-window workspace.

The [Continue On](https://developer.android.com/develop/better-together/continue-on) feature in Android 17 (API level 37) and higher enables the
Googlebook taskbar to display an app icon (called a *suggestion*) for the
activity a user is running on their nearby phone. With a single click, users
can continue their activity on their Googlebook.

Implementation of cross-device handoff lets your app transfer activity context
so the user resumes their workflow, either in your adaptive Android app or in
the desktop browser, at the exact place they left off on their phone.

## Choose a handoff flow

Before enabling cross-device handoff, decide how each activity in your phone app
should open when a user selects the Continue On suggestion on Googlebook:

| Handoff flow | Target on Googlebook | Best for | Key API |
|---|---|---|---|
| **App-to-app handoff** | Native Android app running in a desktop window | Apps optimized for large screens and desktop windowing on Google Play | [`HandoffActivityData.Builder`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder) |
| **App-to-app handoff with web fallback** | Native Android app if installed; otherwise, a URL in the default desktop browser | Apps optimized for a native desktop window experience but requiring a reliable browser fallback when the app isn't installed on the Googlebook | [`setFallbackUri`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder#setFallbackUri(android.net.Uri)) |
| **Direct-to-web handoff** | URL in the default desktop browser (or intercepted by the native app if configured for [Android App Links](https://developer.android.com/training/app-links)) | Workflows where your web application is the primary desktop experience | [`HandoffActivityData.createWebHandoff`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData#createWebHandoff(android.net.Uri)) |

## Enable handoff for an activity

Continue On is disabled by default and is configured per activity. Follow these
steps in each sending activity on the phone:

1. Call [`setHandoffEnabled`](https://developer.android.com/reference/kotlin/android/app/Activity#setHandoffEnabled(kotlin.Boolean,%20android.app.HandoffActivityParams)) and pass `true` once the activity has loaded the state required for handoff. Once enabled, the system can request handoff data while the activity is in the foreground or moving to the background.
2. Override [`onHandoffActivityDataRequested`](https://developer.android.com/reference/kotlin/android/app/Activity#onHandoffActivityDataRequested(android.app.HandoffActivityDataRequestInfo)) to return a non-null [`HandoffActivityData`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData) object. You can query [`isHandoffEnabled`](https://developer.android.com/reference/kotlin/android/app/Activity#isHandoffEnabled()) at any time to check whether handoff is active for the activity.

    import android.app.Activity
    import android.app.HandoffActivityData
    import android.app.HandoffActivityDataRequestInfo
    import android.os.Bundle
    import android.os.PersistableBundle

    class DocumentEditorActivity : Activity() {

        private var documentId: String = "doc_42"
        private var scrollOffsetPx: Int = 0

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            // Enable handoff once the activity is ready to transfer state.
            setHandoffEnabled(true, null)
        }

        override fun onHandoffActivityDataRequested(
            handoffRequestInfo: HandoffActivityDataRequestInfo
        ): HandoffActivityData {
            val extras = PersistableBundle().apply {
                putString(EXTRA_DOCUMENT_ID, documentId)
                putInt(EXTRA_SCROLL_OFFSET, scrollOffsetPx)
            }

            return HandoffActivityData.Builder(getComponentName())
                .setExtras(extras)
                .build()
        }

        companion object {
            const val EXTRA_DOCUMENT_ID = "extra_document_id"
            const val EXTRA_SCROLL_OFFSET = "extra_scroll_offset"
        }
    }

## Package activity state for handoff

The system calls [`onHandoffActivityDataRequested`](https://developer.android.com/reference/kotlin/android/app/Activity#onHandoffActivityDataRequested(android.app.HandoffActivityDataRequestInfo)) in two scenarios:

- **Foreground handoff:** The activity is in the foreground on the phone, and the user initiates a handoff from the Googlebook taskbar.
- **Background state capture:** The activity moves to the background on the phone, and the system caches its handoff payload in case the user selects the suggestion on Googlebook later.

### Check whether the handoff request is active

Inspect [`HandoffActivityDataRequestInfo`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo) using [`isActiveRequest`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo#isActiveRequest()) to
distinguish between an active user-initiated handoff and a background save:

- If `isActiveRequest` returns `true`, the user has actively requested to continue on another device while the activity is visible.
- If `isActiveRequest` returns `false`, the system is caching state as the activity stops.

If you display a visual indicator on the phone confirming that the task is
moving to Googlebook, schedule the UI update asynchronously so that
`onHandoffActivityDataRequested` returns without delay.

### Attach state extras and a web fallback

A [`HandoffActivityData`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData) payload contains the following information:

- **Target component** (required for app-to-app handoff): Pass `this.getComponentName()` (the activity's [`ComponentName`](https://developer.android.com/reference/kotlin/android/content/ComponentName)) or an explicit `ComponentName(this, TargetActivity::class.java)` to [`HandoffActivityData.Builder`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder) to designate which activity launches on Googlebook.
- **Extras** (optional): Pass a [`PersistableBundle`](https://developer.android.com/reference/kotlin/android/os/PersistableBundle) to `setExtras()` containing identifiers and UI coordinates (for example, open document IDs, active tab keys, or scroll positions). The bundle must be smaller than 50 KB.
- **Fallback URI** (optional): Pass a web [`Uri`](https://developer.android.com/reference/kotlin/android/net/Uri) to [`setFallbackUri`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder#setFallbackUri(android.net.Uri)) so Googlebook can open the task in the default browser if your Android app isn't installed.

> [!NOTE]
> **Note:** To show the Continue On suggestion when your app isn't installed on the Googlebook, pass a [`HandoffActivityParams`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams) instance with [`setAllowHandoffWithoutPackageInstalled`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityParams.Builder#setAllowHandoffWithoutPackageInstalled(kotlin.Boolean)) set to `true` when calling `setHandoffEnabled`.

> [!CAUTION]
> **Caution:** Because `HandoffActivityData` is transmitted between devices, don't place sensitive or personally identifiable information (such as authentication tokens, passwords, or private keys) in the `PersistableBundle` or fallback URI. Instead, pass content identifiers and verify user authentication on the receiving Googlebook.

    import android.app.Activity
    import android.app.HandoffActivityData
    import android.app.HandoffActivityDataRequestInfo
    import android.app.HandoffActivityParams
    import android.net.Uri
    import android.os.Bundle
    import android.os.PersistableBundle

    class ArticleReaderActivity : Activity() {

        private var articleId: String = "android-desktop-windowing"
        private var readingProgressPercent: Int = 45

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            setHandoffEnabled(
                true,
                HandoffActivityParams.Builder()
                    .setAllowHandoffWithoutPackageInstalled(true)
                    .build()
            )
        }

        override fun onHandoffActivityDataRequested(
            handoffRequestInfo: HandoffActivityDataRequestInfo
        ): HandoffActivityData {
            if (handoffRequestInfo.isActiveRequest()) {
                window.decorView.post {
                    onHandoffStartedToSecondaryDevice()
                }
            }

            val extras = PersistableBundle().apply {
                putString(EXTRA_ARTICLE_ID, articleId)
                putInt(EXTRA_READING_PROGRESS, readingProgressPercent)
            }

            val fallbackWebUri = Uri.Builder()
                .scheme("https")
                .authority("example.com")
                .appendPath("articles")
                .appendPath(articleId)
                .appendQueryParameter("progress", readingProgressPercent.toString())
                .build()

            return HandoffActivityData.Builder(getComponentName())
                .setExtras(extras)
                .setFallbackUri(fallbackWebUri)
                .build()
        }

        private fun onHandoffStartedToSecondaryDevice() {
            // Save local drafts and update phone UI without blocking handoff.
        }

        companion object {
            const val EXTRA_ARTICLE_ID = "extra_article_id"
            const val EXTRA_READING_PROGRESS = "extra_reading_progress"
        }
    }

### Configure direct-to-web handoff

If your primary desktop experience on Googlebook is a web application, pass
`HandoffActivityParams` with `setAllowHandoffWithoutPackageInstalled(true)` to
`setHandoffEnabled`, and call [`HandoffActivityData.createWebHandoff`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData#createWebHandoff(android.net.Uri)) instead
of using `HandoffActivityData.Builder`:

    import android.app.Activity
    import android.app.HandoffActivityData
    import android.app.HandoffActivityDataRequestInfo
    import android.app.HandoffActivityParams
    import android.net.Uri
    import android.os.Bundle

    class WebDashboardActivity : Activity() {

        private var projectId: String = "proj_901"

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            setHandoffEnabled(
                true,
                HandoffActivityParams.Builder()
                    .setAllowHandoffWithoutPackageInstalled(true)
                    .build()
            )
        }

        override fun onHandoffActivityDataRequested(
            handoffRequestInfo: HandoffActivityDataRequestInfo
        ): HandoffActivityData {
            val webUri = Uri.Builder()
                .scheme("https")
                .authority("app.example.com")
                .appendPath("projects")
                .appendPath(projectId)
                .build()

            return HandoffActivityData.createWebHandoff(webUri)
        }
    }

## Receive and restore state on Googlebook

When the user selects the Continue On suggestion in the Googlebook taskbar, the
system launches the target `ComponentName` in a desktop window and attaches the
`PersistableBundle` extras to the launch [`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent).

On Googlebook, handle the incoming handoff with desktop windowing and multi-pane
layouts in mind:

1. **Extract handoff extras:** In both the `onCreate` and `onNewIntent` methods of the receiving activity, retrieve the extras from the incoming `Intent`. Handling `onNewIntent` ensures that if your activity uses `singleTop` launch mode or routes to an existing desktop window, the window updates to the handed-off item.
2. **Adapt state to multi-pane layouts:** A state that occupied a full-screen detail view on a phone often maps to a selected item inside a list-detail or supporting-pane layout on Googlebook. Populate both the primary list selection and the detail pane so the desktop window has complete context.
3. **Preserve restored state across window resizing:** Store the handed-off state in a `ViewModel` (`SavedStateHandle`) or `rememberSaveable` in Jetpack Compose so that free-form window resizing on Googlebook does not reset the restored session.

    import android.app.Activity
    import android.content.Intent
    import android.os.Bundle

    class DocumentEditorReceiverActivity : Activity() {

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)

            // Restore from the handoff intent only on initial launch so subsequent
            // desktop window configuration changes use saved instance state.
            if (savedInstanceState == null) {
                handleHandoffIntent(intent)
            }
        }

        override fun onNewIntent(intent: Intent) {
            super.onNewIntent(intent)
            setIntent(intent)
            handleHandoffIntent(intent)
        }

        private fun handleHandoffIntent(incomingIntent: Intent?) {
            val documentId = incomingIntent?.getStringExtra(EXTRA_DOCUMENT_ID)
                ?: return
            val scrollOffsetPx = incomingIntent.getIntExtra(EXTRA_SCROLL_OFFSET, 0)

            openDocumentInDesktopWorkspace(
                documentId = documentId,
                initialScrollOffsetPx = scrollOffsetPx
            )
        }

        private fun openDocumentInDesktopWorkspace(
            documentId: String,
            initialScrollOffsetPx: Int
        ) {
            // Load the document into the list-detail layout and restore scroll position.
        }

        companion object {
            const val EXTRA_DOCUMENT_ID = "extra_document_id"
            const val EXTRA_SCROLL_OFFSET = "extra_scroll_offset"
        }
    }

## Test handoff between a phone and Googlebook

To verify your implementation end to end:

1. **Prepare both devices**
   - Sign in to the same Google Account on both your Android phone (running Android 17 or higher) and your Googlebook (or a test device running in desktop windowing mode).
   - Turn on Bluetooth and connect both devices to the same Wi-Fi network.
   - On both devices, open **Settings \> Connected devices \> Connection
     preferences \> Cross-device services \> Continue activity** , follow the setup prompts, and enable **Tasks** . For full environment prerequisites, see [Setup and test](https://developer.android.com/develop/better-together/continue-on/setup).
2. **Install your app**
   - For **app-to-app handoff**, install your build on both the phone and the Googlebook.
   - For **web fallback** or **direct-to-web handoff**, install your build on the phone and leave the app uninstalled on the Googlebook so you can verify that the browser opens the expected URL.
3. **Trigger the handoff**
   - On the phone, open your app and navigate to the activity that enables handoff (calling `setHandoffEnabled(true, null)` for app-to-app handoff, or passing `HandoffActivityParams` with `setAllowHandoffWithoutPackageInstalled(true)` when testing with the app uninstalled on the Googlebook).
   - On the Googlebook, check the right side of the taskbar for your app icon with the Continue On badge and select it.
4. **Verify desktop restoration**
   - Confirm that your app opens in a desktop window (or browser tab) at the exact item and scroll position from the phone.
   - Resize the app window on Googlebook and verify that the restored content and selection persist across window size class transitions.

## Additional resources

- [Build adaptive apps for Googlebook](https://developer.android.com/develop/adaptive-apps/guides/googlebook/overview)
- [About the Continue On feature](https://developer.android.com/develop/better-together/continue-on)
- [Enable and customize cross-device handoff](https://developer.android.com/develop/better-together/continue-on/enable-support)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)