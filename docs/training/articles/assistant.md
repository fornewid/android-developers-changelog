---
title: https://developer.android.com/training/articles/assistant
url: https://developer.android.com/training/articles/assistant
source: md.txt
---

# Optimizing Contextual Content for the Assistant

Android 6.0 Marshmallow introduces a new way for users to engage with apps through assistant apps, such as the[Google Assistant](https://play.google.com/store/apps/details?id=com.google.android.apps.googleassistant). The assistant is a top-level window that users can view to obtain contextually relevant actions for the current activity. These actions might include deep links to other apps on the device.

Users activate the assistant with a long press on the Home button or by saying a[keyphrase](https://developer.android.com/reference/android/service/voice/AlwaysOnHotwordDetector). In response, the system opens a top-level window that displays contextually relevant actions.

An assistant app, such as Google Assistant, implements the assistant overlay window through a feature called Now on Tap, which works with the Android platform-level functionality. The system allows the user to select an assistant app, which obtains contextual information from your app using Android's Assist API.

This guide explains how Android apps use Android's Assist API to improve the assistant user experience. To learn how to create a media app so that the Assistant can launch and control, see[Google Assistant and media apps](https://developer.android.com/media/implement/assistant).

## Using Assistants

Figure 1 illustrates a typical user interaction with the assistant. When the user long-presses the Home button, the Assist API callbacks are invoked in the*source* app (step 1). The assistant renders the overlay window (steps 2 and 3), and then the user selects the action to perform. The assistant executes the selected action, such as firing an intent with a deep link to the (*destination*) restaurant app (step 4).  
![](https://developer.android.com/static/images/training/assistant/image01.png)

Figure 1. Assistant interaction example with the Now on Tap feature of the Google App

Users can configure the assistant by selecting**Settings \> Apps \> Default Apps \> Assist \& voice input**. Users can change system options such as accessing the screen contents as text and accessing a screenshot, as shown in Figure 2.  
![](https://developer.android.com/static/images/training/assistant/image02.png)

Figure 2. Assist \& voice input settings

### Source app

To ensure that your app works with the assistant as a source of information for the user, you need only follow[accessibility best practices](https://developer.android.com/guide/topics/ui/accessibility/apps). This section describes how to provide additional information to help improve the assistant user experience as well as scenarios that need special handling, such as custom Views.

#### Share additional information with the assistant

In addition to the text and the screenshot, your app can share other information with the assistant. For example, your music app can choose to pass current album information so that the assistant can suggest smarter actions tailored to the current activity. Note that the Assist APIs do not provide media controls. To add media controls see[Google Assistant and media apps](https://developer.android.com/media/implement/assistant).

To provide additional information to the assistant, your app provides*global application context*by registering an app listener and supplies activity-specific information with activity callbacks as shown in Figure 3:  
![](https://developer.android.com/static/images/training/assistant/image03.png)

Figure 3. Assist API lifecycle sequence diagram

To provide global application context, the app creates an implementation of[Application.OnProvideAssistDataListener](https://developer.android.com/reference/android/app/Application.OnProvideAssistDataListener)and registers it using[registerOnProvideAssistDataListener()](https://developer.android.com/reference/android/app/Application#registerOnProvideAssistDataListener(android.app.Application.OnProvideAssistDataListener)). To provide activity-specific contextual information, the activity overrides[onProvideAssistData()](https://developer.android.com/reference/android/app/Activity#onProvideAssistData(android.os.Bundle))and[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent)). The two activity methods are called*after* the optional global callback is invoked. Because the callbacks execute on the main thread, they should complete[promptly](https://developer.android.com/training/articles/perf-anr). The callbacks are invoked only when the activity is[running](https://developer.android.com/reference/android/app/Activity#ActivityLifecycle).

##### Providing context

When the user activates the assistant,[onProvideAssistData()](https://developer.android.com/reference/android/app/Activity#onProvideAssistData(android.os.Bundle))is called to build a full[ACTION_ASSIST](https://developer.android.com/reference/android/content/Intent#ACTION_ASSIST)Intent with all of the context of the current application represented as an instance of the[AssistStructure](https://developer.android.com/reference/android/app/assist/AssistStructure). You can override this method to place anything you like into the bundle to appear in the[EXTRA_ASSIST_CONTEXT](https://developer.android.com/reference/android/content/Intent#EXTRA_ASSIST_CONTEXT)part of the assist intent.

##### Describing content

Your app can implement[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent))to improve the assistant user experience by providing content-related references related to the current activity. You can describe the app content using the common vocabulary defined by[Schema.org](https://schema.org)through a JSON-LD object. In the example below, a music app provides structured data to describe the music album that the user is currently viewing:  

### Kotlin

```kotlin
override fun onProvideAssistContent(assistContent: AssistContent) {
    super.onProvideAssistContent(assistContent)

    val structuredJson: String = JSONObject()
            .put("@type", "MusicRecording")
            .put("@id", "https://example.com/music/recording")
            .put("name", "Album Title")
            .toString()

    assistContent.structuredData = structuredJson
}
```

### Java

```java
@Override
public void onProvideAssistContent(AssistContent assistContent) {
  super.onProvideAssistContent(assistContent);

  String structuredJson = new JSONObject()
       .put("@type", "MusicRecording")
       .put("@id", "https://example.com/music/recording")
       .put("name", "Album Title")
       .toString();

  assistContent.setStructuredData(structuredJson);
}
```

You can also improve the user experience with custom implementations of[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent)), which can provide the following benefits:

- [Adjusts the provided content intent](https://developer.android.com/reference/android/app/assist/AssistContent#setIntent(android.content.Intent))to better reflect the top-level context of the activity.
- [Supplies the URI](https://developer.android.com/reference/android/app/assist/AssistContent#setWebUri(android.net.Uri))of the displayed content.
- Fills in[setClipData()](https://developer.android.com/reference/android/app/assist/AssistContent#setClipData(android.content.ClipData))with additional content of interest that the user is currently viewing.

**Note:** Apps that use a custom text selection implementation likely need to implement[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent))and call[setClipData()](https://developer.android.com/reference/android/app/assist/AssistContent#setClipData(android.content.ClipData)).

#### Default implementation

If neither the[onProvideAssistData()](https://developer.android.com/reference/android/app/Activity#onProvideAssistData(android.os.Bundle))nor the[onProvideAssistContent()](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent))callback is implemented, the system still proceeds and passes the automatically collected information to the assistant unless the current window is flagged as[secure](https://developer.android.com/training/articles/assistant#excluding_views). As shown in Figure 3, the system uses the default implementations of[onProvideStructure()](https://developer.android.com/reference/android/view/View#onProvideStructure(android.view.ViewStructure))and[onProvideVirtualStructure()](https://developer.android.com/reference/android/view/View#onProvideVirtualStructure(android.view.ViewStructure))to collect text and view hierarchy information. If your view implements custom text drawing, override[onProvideStructure()](https://developer.android.com/reference/android/view/View#onProvideStructure(android.view.ViewStructure))to provide the assistant with the text shown to the user by calling[setText(CharSequence)](https://developer.android.com/reference/android/view/ViewStructure#setText(java.lang.CharSequence)).

*In most cases, implementing accessibility support enables the assistant to obtain the information it needs.* To implement accessibility support, observe the best practices described in[Making Applications Accessible](https://developer.android.com/guide/topics/ui/accessibility/apps), including the following:

- Provide[android:contentDescription](https://developer.android.com/reference/android/R.attr#contentDescription)attributes.
- Populate[AccessibilityNodeInfo](https://developer.android.com/reference/android/view/accessibility/AccessibilityNodeInfo)for custom views.
- Make sure that custom[ViewGroup](https://developer.android.com/reference/android/view/ViewGroup)objects correctly[expose](https://developer.android.com/reference/android/view/ViewGroup#getChildAt(int))their children.

#### Excluding views from assistants

To handle sensitive information, your app can exclude the current view from the assistant by setting the[FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)layout parameter of the[WindowManager](https://developer.android.com/reference/android/view/WindowManager). You must set[FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)explicitly for every window created by the activity, including dialogs. Your app can also use[setSecure()](https://developer.android.com/reference/android/view/SurfaceView#setSecure(boolean))to exclude a surface from the assistant. There is no global (app-level) mechanism to exclude all views from the assistant. Note that[FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)does not cause the Assist API callbacks to stop firing. The activity that uses[FLAG_SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)can still explicitly provide information to an assistant app using the callbacks described earlier this guide.

**Note:** For enterprise accounts (Android for Work), the administrator can disable the collection of assistant data for the work profile by using the[setScreenCaptureDisabled()](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setScreenCaptureDisabled(android.content.ComponentName, boolean))method of the[DevicePolicyManager](https://developer.android.com/reference/android/app/admin/DevicePolicyManager)API.

#### Voice interactions

Assist API callbacks are also invoked upon[keyphrase detection](https://developer.android.com/reference/android/service/voice/AlwaysOnHotwordDetector). For more information, see the[Voice Actions](https://developers.google.com/voice-actions/)documentation.

#### Z-order considerations

An assistant uses a lightweight overlay window displayed on top of the current activity. Because the user can activate the assistant at any time, don't create permanent[system alert](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)windows that interfere with the overlay window, as shown in Figure 4.  
![](https://developer.android.com/static/images/training/assistant/image04.png)

Figure 4. Assist layer Z-order

If your app uses[system alert](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)windows, remove them promptly because leaving them on the screen degrades the user experience.

### Destination app

Assistant apps typically take advantage of deep linking to find destination apps. To make your app a potential destination app, consider adding[deep linking](https://developer.android.com/training/app-indexing/deep-linking)support. The matching between the current user context and deep links or other potential actions displayed in the overlay window (shown in step 3 in Figure 1) is specific to Google Assistant's implementation. For example, the Google Assistant App uses deep linking and[App Links](https://developer.android.com/training/app-links)in order to drive traffic to destination apps.

## Implementing Your Own Assistant

You may wish to implement your own assistant. As shown in[Figure 2](https://developer.android.com/training/articles/assistant#assist-input-settings), the user can select the active assistant app. The assistant app must provide an implementation of[VoiceInteractionSessionService](https://developer.android.com/reference/android/service/voice/VoiceInteractionSessionService)and[VoiceInteractionSession](https://developer.android.com/reference/android/service/voice/VoiceInteractionSession)as shown in[this`VoiceInteraction`example](https://android.googlesource.com/platform/frameworks/base/+/marshmallow-release/tests/VoiceInteraction/). It also requires the[BIND_VOICE_INTERACTION](https://developer.android.com/reference/android/Manifest.permission#BIND_VOICE_INTERACTION)permission. The assistant can then receive the text and view hierarchy represented as an instance of the[AssistStructure](https://developer.android.com/reference/android/app/assist/AssistStructure)in[onHandleAssist()](https://developer.android.com/reference/android/service/voice/VoiceInteractionSession#onHandleAssist(android.os.Bundle, android.app.assist.AssistStructure, android.app.assist.AssistContent)). It receives the screenshot through[onHandleScreenshot()](https://developer.android.com/reference/android/service/voice/VoiceInteractionSession#onHandleScreenshot(android.graphics.Bitmap)).