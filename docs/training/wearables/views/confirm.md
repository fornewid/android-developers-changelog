---
title: https://developer.android.com/training/wearables/views/confirm
url: https://developer.android.com/training/wearables/views/confirm
source: md.txt
---

Try the Compose way Jetpack Compose on Wear OS is the recommended UI toolkit for Wear OS. [Try Compose on Wear OS →](https://developer.android.com/training/wearables/compose) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)


Confirmation animations give users visual feedback when they complete an action.
They cover the entire screen to ensure that users can see these confirmations at a glance.


In most cases, you won't need to use a separate confirmation animation. Review
[Design principles](https://developer.android.com/training/wearables/design/design-principles) for more information.


The Jetpack Wearable UI Library provides
`https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity`
to display a confirmation animation in your apps.

### Show confirmation animations


`ConfirmationActivity` is used to display confirmation animations after the user
completes an action on the wearable.


There are three types of confirmations:

- **Success**: the action was completed successfully on the wearable.
- **Failure**: the action failed to complete.
- **Open on Phone**: the action has caused something to display on the phone, or in order to complete the action, the user needs to go to their phone to continue.


To show a confirmation animation when users complete an action in your app, create an intent that
starts `ConfirmationActivity` from one of your activities. Set the
`https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#EXTRA_ANIMATION_TYPE`
to one of the following values:

- `https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#SUCCESS_ANIMATION`
- `https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#FAILURE_ANIMATION`
- `https://developer.android.com/reference/androidx/wear/activity/ConfirmationActivity#OPEN_ON_PHONE_ANIMATION`


To use `ConfirmationActivity` in your app, first declare this activity in your
manifest file, as shown in the following example:

```xml
<manifest><
  application>
    ..<.
    activity
        android:name="androidx.wear.activity.ConfirmationActi<vity"><;
    /activit<y>
  /application>
/manifest>
```

Determine the result of the user action, start the activity with an intent, and
add a message that appears under the confirmation icon, as shown in the following example:

```kotlin
val intent = Intent(this, ConfirmationActivity::class.java).apply {
    putExtra(ConfirmationActivity.EXTRA_ANIMATION_TYPE, ConfirmationActivity.SUCCESS_ANIMATION)
    putExtra(ConfirmationActivity.EXTRA_MESSAGE, getString(R.string.msg_sent))
}
startActivity(intent)
```

After showing the confirmation animation, the
`ConfirmationActivity` finishes and your activity resumes.