---
title: https://developer.android.com/develop/better-together/continue-on/enable-support
url: https://developer.android.com/develop/better-together/continue-on/enable-support
source: md.txt
---

Continue On introduces new methods and classes for you to indicate support for
the feature and provide the necessary data that gets passed along. This allows
you to properly resume the user experience on the receiving device.

## Enable support

Support for Continue On (off by default) must be implemented on a per-activity
basis. To enable the feature, call [`setHandoffEnabled()`](https://developer.android.com/reference/kotlin/android/app/Activity#setHandoffEnabled(kotlin.Boolean,%20android.app.HandoffActivityParams)) to denote the
current activity as handoff ready. Once `setHandoffEnabled(true)` is called,
handoff can happen at any point for the activity, so only call it when the
activity is ready to be handed off.

You can check whether the activity has enabled Continue On with
[`isHandoffEnabled()`](https://developer.android.com/reference/kotlin/android/app/Activity#isHandoffEnabled()). If an activity has enabled handoff, it must also
implement [`onHandoffActivityDataRequested()`](https://developer.android.com/reference/kotlin/android/app/Activity#onHandoffActivityDataRequested(android.app.HandoffActivityDataRequestInfo)) to ensure it returns a
non-null [`HandoffActivityData`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData), as no default behavior is implemented.

    class MyHandoffActivity : Activity() {

        ...

      override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Do stuff
        ...
        // Enable handoff
        setHandoffEnabled(true, null)
      }

      // Override and implement onHandoffActivityDataRequested
      override fun onHandoffActivityDataRequested(handoffRequestInfo: HandoffActivityDataRequestInfo) : HandoffActivityData {
        // Create and return handoff data
      }
    }

You configure the `HandoffActivityData` object with any relevant extras and a
fallback URI to inform Continue On about how to perform the handoff to the
receiving device.

There are two situations when this data is needed by the system:

- The activity is going into the background, and relevant data must be saved.
- The activity is in the foreground, and handoff has been requested. You can check the status of a handoff request.

## Check status

The [`HandoffActivityDataRequestInfo`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo) class provides information about the
current request to hand off an activity. Use [`isActiveRequest()`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityDataRequestInfo#isActiveRequest()) to
determine whether the request is currently active. If the method returns

- true, the current activity is in the foreground and the user has requested to Continue On another device, however if
- false, the activity has stopped and is in the background, but the user may request a handoff in the future.

On the sending device, if you'd like to show UI to indicate to your user that a
handoff has occurred or is in progress, you can check `isActiveRequest()` for an
active request. However, do not execute this code synchronously as part of
`onHandoffActivityDataRequested()`. Instead, queue up any code to run
asynchronously so as not to block or delay the handoff.

    // Override and implement onHandoffActivityDataRequested
    override fun onHandoffActivityDataRequested(handoffRequestInfo: HandoffActivityDataRequestInfo) : HandoffActivityData {

      // Check whether the handoff request is active
      if (handoffRequestInfo.isActiveRequest()) {
        // Asynchronously show UI to let users know a handoff is in progress
      }

      // Create and return handoff data
    }

## Create handoff data

To ensure all relevant and necessary data is passed along during handoff with
the Continue On feature, you must include the data in the `HandoffActivityData`
object.

The `HandoffActivityData` class represents the handoff data associated with an
activity. `HandoffActivityData` informs Continue On about how to handle and
recreate an activity on the receiving device. The handoff data includes:

- **Component name** (required): The [`ComponentName`](https://developer.android.com/reference/kotlin/android/content/ComponentName) of a corresponding activity to launch on the receiving device to resume the user's journey after handoff. In most cases and for exact activity replication, this will be the component name for the same activity creating the `HandoffActivityData`.
- **Extras** (optional): You can specify extras that will be included in the start [`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent) of the activity. This is a [`PersistableBundle`](https://developer.android.com/reference/kotlin/android/os/PersistableBundle) that can be used to provide additional information to the component. Extras must be less than 50KB.

> [!IMPORTANT]
> **Important:** Because `HandoffActivityData` is passed between devices, DO NOT include sensitive or personally identifiable information (for example, user credentials).

To create `HandoffActivityData` objects, use the builder class,
[`HandoffActivityData.Builder`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder). You can construct a new builder with either
the [`Activity`](https://developer.android.com/reference/kotlin/android/app/Activity) or `ComponentName` of the activity that should receive the
handoff. Then use the `setExtras()` method to optionally specify extras. Lastly,
call `build()` to create the `HandoffActivityData` object.

    // Override and implement onHandoffActivityDataRequested
    override fun onHandoffActivityDataRequested(handoffRequestInfo: HandoffActivityDataRequestInfo) : HandoffActivityData {

      // Check whether the handoff request is active
      if (handoffRequestInfo.isActiveRequest()) {
        // Asynchronously show UI to let users know a handoff is in progress
      }

      val extras: PersistableBundle = PersistableBundle()
      // Put relevant and necessary values into extras (e.g. scroll position)
      extras.putString("data_id", getDataId())
      extras.putInt("scroll_position", getScrollPosition())

      // Create and return handoff data
      return HandoffActivityData.Builder(this) // Designate handoff to the same activity
        .setExtras(extras)
        .build()
    }

## Set web fallback option

In the event that the specified activity cannot be started on the receiving
device, you can additionally use [`setFallbackUri()`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData.Builder#setFallbackUri(android.net.Uri)) to optionally set a
fallback URL that's opened on the device in the user's default browser.

    val fallbackWebLink: Uri = Uri.parse("https://myapp.com/fallback?query=" + paramVal)

    val handoffData: HandoffActivityData = HandoffActivityData.Builder(this)
      .setExtras(extras)
      .setFallbackUri(fallbackWebLink)
      .build()

## Implement direct to web

Alternatively, to implement direct-to-web handoff, use the
[`HandoffActivityData.createWebHandoff()`](https://developer.android.com/reference/kotlin/android/app/HandoffActivityData#createWebHandoff(android.net.Uri)) method to generate the
`HandoffActivityData`.

    val webHandoffLink: Uri = Uri.parse("https://myapp.com/handoff?query=" + paramVal)

    val handoffData: HandoffActivityData = HandoffActivityData.createWebHandoff(webHandoffLink)

## Receive and handle handoff intent

On the receiving device, your app must handle the handoff and recreate the
user's experience from the sending device. Specifically, in the activity that
you specified in the `HandoffActivityData` returned by
`onHandoffActivityDataRequested()`, you need to handle the intent and retrieve
the extras that have information about how to recreate the activity
appropriately.

If you're specifying the handoff to the same activity, you can receive the
intent in the `onCreate()` method of the activity so that the data can be
retrieved and appropriately pre-populated for the user.

    class MyHandoffActivity : Activity() {

        ...

      override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Do stuff
        ...

        // Get the launch intent and retrieve extras
        val intent: Intent = getIntent()
        if (intent != null && intent.hasExtra("data_id")) {
          val dataID: String = intent.getStringExtra("data_id")
          // Retrieve the data that corresponds to the data ID
          ...
          // Populate activity UI with relevant data
          ...

          if (intent.hasExtra("scroll_position")) {
            val scrollPosition: Int = intent.getIntExtra("scroll_position"
            // Move the page to the scroll position
            ...
          }
        }
      }
    }