---
title: Show confirmations on Wear  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/views/confirm
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Show confirmations on Wear Stay organized with collections Save and categorize content based on your preferences.



Try the Compose way

Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS.

[Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose)

![](/static/images/android-compose-ui-logo.png)

Confirmation animations give users visual feedback when they complete an action.
They cover the entire screen to ensure that users can see these confirmations at a glance.

In most cases, you won't need to use a separate confirmation animation. Review
[Design principles](/training/wearables/design/design-principles) for more information.

The Jetpack Wearable UI Library provides
`ConfirmationActivity`
to display a confirmation animation in your apps.

### Show confirmation animations

`ConfirmationActivity` is used to display confirmation animations after the user
completes an action on the wearable.

There are three types of confirmations:

* **Success**: the action was completed successfully on the wearable.
* **Failure**: the action failed to complete.
* **Open on Phone**: the action has caused something to display on the phone, or in
  order to complete the action, the user needs to go to their phone to continue.

To show a confirmation animation when users complete an action in your app, create an intent that
starts `ConfirmationActivity` from one of your activities. Set the
`EXTRA_ANIMATION_TYPE`
to one of the following values:

* `SUCCESS_ANIMATION`
* `FAILURE_ANIMATION`
* `OPEN_ON_PHONE_ANIMATION`

To use `ConfirmationActivity` in your app, first declare this activity in your
manifest file, as shown in the following example:

```
<manifest>
  <application>
    ...
    <activity
        android:name="androidx.wear.activity.ConfirmationActivity">
    </activity>
  </application>
</manifest>
```

Determine the result of the user action, start the activity with an intent, and
add a message that appears under the confirmation icon, as shown in the following example:

```
val intent = Intent(this, ConfirmationActivity::class.java).apply {
    putExtra(ConfirmationActivity.EXTRA_ANIMATION_TYPE, ConfirmationActivity.SUCCESS_ANIMATION)
    putExtra(ConfirmationActivity.EXTRA_MESSAGE, getString(R.string.msg_sent))
}
startActivity(intent)
```

After showing the confirmation animation, the
`ConfirmationActivity` finishes and your activity resumes.