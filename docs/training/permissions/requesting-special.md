---
title: https://developer.android.com/training/permissions/requesting-special
url: https://developer.android.com/training/permissions/requesting-special
source: md.txt
---

A *special permission* guards access to system resources that are particularly
sensitive or not directly related to user privacy. These permissions are
different than [install-time permissions](https://developer.android.com/guide/topics/permissions/overview#install-time) and [runtime permissions](https://developer.android.com/guide/topics/permissions/overview#runtime).  
![Android system settings 'Special app access' screen, showing a list of apps and their special permission statuses.](https://developer.android.com/static/images/training/permissions/special-app-access.svg) **Figure 1.** The **Special app access** screen in system settings.

Some examples of special permissions include:

- Scheduling exact alarms.
- Displaying and drawing over other apps.
- Accessing all storage data.

Apps that declare a special permission are shown in the **Special app access**
page in system settings (figure 1). To grant a special permission to the app, a
user must navigate to this page: **Settings \> Apps \> Special app access**.
| **Note:** Use special permissions only in specific use cases. There may be policy implications to adding them in your app.

## Workflow

To request a special permission, do the following:

1. In your app's manifest file, [Declare the special permissions](https://developer.android.com/training/permissions/declaring) that your app might need to request.
2. Design your app's user experience (UX) so that specific actions in your app are associated with specific special permissions. Let users know which actions might require them to grant permission for your app to access private user data.
3. [Wait for the user to invoke the task or action](https://developer.android.com/training/permissions/requesting#principles) in your app that requires access to specific private user data. At that time, your app can request the special permission that's required for accessing that data.
4. Check whether the user has already granted the special permission that your app requires. To do so, use each permission's [custom checking
   function](https://developer.android.com/training/permissions/requesting-special#check-method). If granted, your app can access the private user data. If not, continue to the next step. Note: You must check whether you have the permission every time you perform an operation that requires that permission.
5. Present a rationale to the user in a UI element that clearly explains what data your app is trying to access and what benefits the app can provide to the user if they grant the special permission. In addition, since your app sends users to system settings to grant the permission, also include brief instructions that explain how users can grant the permission there. The rationale UI should provide a clear option for the user to opt-out of granting the permission. After the user acknowledges the rationale, continue to the next step.
6. Request the special permission that your app requires to access the private user data. This likely involves an intent to the corresponding page in system settings where the user can grant the permission. Unlike [runtime
   permissions](https://developer.android.com/guide/topics/permissions/overview#runtime), there is no permission dialog.
7. Check the user's response -- whether they chose to grant or deny the special permission -- in the `onResume()` method.
8. If the user granted the permission to your app, you can access the private user data. If the user denied the permission, [gracefully degrade your app
   experience](https://developer.android.com/training/permissions/requesting#handle-denial) so that your app provides functionality to the user without the information that's protected by that permission.

![Diagram illustrating the workflow for declaring and requesting special permissions on Android, from manifest declaration to user rationale, system settings redirection, and handling the user's decision.](https://developer.android.com/static/images/training/permissions/workflow-special.svg) **Figure 2.** Workflow for declaring and requesting special permissions on Android.

## Request special permissions

Unlike [runtime permissions](https://developer.android.com/guide/topics/permissions/overview#runtime), the user must grant special permissions from
the **Special App Access** page in system settings. Apps can send users there
using an intent, which pauses the app and launches the corresponding settings
page for a given special permission. After the user returns to the app, the app
can check if the permission has been granted in the `onResume()` function.

The following sample code shows how to request the
[`SCHEDULE_EXACT_ALARMS`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM) special permission from users:  

    val alarmManager = getSystemService<AlarmManager>()!!
    when {
       // if permission is granted, proceed with scheduling exact alarms...
       alarmManager.canScheduleExactAlarms() -> {
           alarmManager.setExact(...)
       }
       else -> {
           // ask users to grant the permission in the corresponding settings page
           startActivity(Intent(ACTION_REQUEST_SCHEDULE_EXACT_ALARM))
       }
    }

Sample code to check the permission and handle user decisions in `onResume()`:  

    override fun onResume() {
        // ...

        if (alarmManager.canScheduleExactAlarms()) {
            // proceed with the action (setting exact alarms)
            alarmManager.setExact(...)
        }
        else {
            // permission not yet approved. Display user notice and gracefully
            // degrade your app experience.
            alarmManager.setWindow(...)
        }
    }

## Tips for requesting special permissions

The following sections provide considerations and tips when requesting special
permissions.

### Each permission has its own check method

Special permissions operate differently than [runtime permissions](https://developer.android.com/training/permissions/requesting#request-permission). Instead,
refer to the [permissions API reference page](https://developer.android.com/reference/android/Manifest.permission) and use the custom access check
functions for each special permission. Examples include
[`AlarmManager#canScheduleExactAlarms()`](https://developer.android.com/reference/android/app/AlarmManager#canScheduleExactAlarms()) for the
[`SCHEDULE_EXACT_ALARMS`](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM) permission and
[`Environment#isExternalStorageManager()`](https://developer.android.com/reference/android/os/Environment#isExternalStorageManager()) for the
[`MANAGE_EXTERNAL_STORAGE`](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE) permission.

### Request in-context

Similar to runtime permissions, apps should request special permissions
in-context when the user requests a specific action that requires the
permission. For example, wait to request the `SCHEDULE_EXACT_ALARMS` permission
until the user schedules an email to be sent at a specific time.

### Explain the request

Provide a rationale before redirecting to system settings. Since users leave the
app temporarily to grant special permissions, show an in-app UI before you
launch the intent to the **Special App Access** page in system settings. This UI
should clearly explain why the app needs the permission and how the user should
grant it on the settings page.