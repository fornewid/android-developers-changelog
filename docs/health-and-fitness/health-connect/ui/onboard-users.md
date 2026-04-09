---
title: https://developer.android.com/health-and-fitness/health-connect/ui/onboard-users
url: https://developer.android.com/health-and-fitness/health-connect/ui/onboard-users
source: md.txt
---

Many apps have a custom onboarding flow such as feature education or asking user
consent. To enable Health Connect to launch your onboarding flow, add the
following to your manifest:  

    <!-- Required to support pre-Android 14 devices with APK Health Connect -->
    <activity
      android:name=".OnboardingActivity"
      android:exported="true"
      android:permission="com.google.android.apps.healthdata.permission.START_ONBOARDING">
      <intent-filter>
        <action android:name="androidx.health.ACTION_SHOW_ONBOARDING"/>
      </intent-filter>
    </activity>
    <!-- Required to support Android 14+ devices with platform Health Connect -->
    <activity-alias
      android:name="UAndAboveOnboardingActivity"
      android:exported="true"
      android:targetActivity=".OnboardingActivity"
      android:permission="android.permission.health.START_ONBOARDING">
      <intent-filter>
        <action android:name="android.health.connect.action.SHOW_ONBOARDING" />
      </intent-filter>
    </activity-alias>

Users may initiate the connection to your app directly from the Health
Connect app, rather than from within your app. If your app requires any
additional interaction beyond being granted permission to read or write data,
provide an onboarding activity.

## Version support

To support both pre-Android 14 and Android 14+ devices:

- **Recommended approach:** Create a single onboarding activity that handles
  both scenarios. Use an activity alias, as shown in the example,to verify
  compatibility across Android versions.

- **Alternative approach:** Export two separate activities,
  one for each Android version. This approach may lead to increased maintenance
  complexity.

## Exported activity requirements

When a user attempts to connect your app to Health Connect, the exported
activity is launched. This activity must do the following:

- Display any relevant user education such as explaining what data is written or read.
- Ask the user to grant consent if required.
- Make a permissions request to Health Connect.
- Carry out any other application specific logic such as scheduling a periodic worker.
- Once complete, allow the user to dismiss the activity.

For apps that *don't* export an onboarding activity, Health Connect instead
brings the user to the **Manage permissions** screen once the user attempts to
connect the app. This may be acceptable for apps where permissions being
granted is the only prerequisite for the integration to function.

Note that the onboarding activity may be launched more than once, for example if
the user later revokes permissions to your app and then reconnects it.