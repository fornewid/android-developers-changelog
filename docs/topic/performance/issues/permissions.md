---
title: https://developer.android.com/topic/performance/issues/permissions
url: https://developer.android.com/topic/performance/issues/permissions
source: md.txt
---

Most apps require that users grant them certain
[app permissions](https://developer.android.com/guide/topics/permissions/overview) in order to function
properly. However, in some cases, users might not grant the permissions

- They think the permission isn't needed for the app's core functionality.
- They don't use the functionality associated with the permission.
- They are concerned about the permission's impacting device performance.
- They're simply uncomfortable, for example due to sensitivities regarding privacy.

> [!NOTE]
> **Note:** For information on how Android Play Vitals tracks and reports this issue, see [Permission Denials in Android vitals](https://developer.android.com/google/play/vitals/permissions).

## Best practices

Unusually high denial rates suggest that users don't think the additional
exposure of their information is worth the benefits offered in return.
There are a number of ways to make users feel more comfortable using your app.
You might be able to reduce the denial rate if you take
steps such as those outlined in this section. However, you shouldn't
expect to drive denial rates to zero, because users
have diverse personal preferences and some simply don't wish to grant
permissions under any circumstances.

### Avoid requesting unnecessary permissions

Research shows that users prefer apps that request fewer permissions.
Keeping permission requests to the minimum set necessary can help improve user
trust in an app, and drive more installs. Conversely, adding unnecessary
permission requests might negatively impact your app's visibility on the Play
Store. If
specific permissions aren't necessary, you might be able to reduce your app's
number of permission requests through alternative methods. Some common
approaches are outlined in
[App Permissions Best Practices](https://developer.android.com/training/permissions/usage-notes).

### Surface the permission request in context

Non-critical permissions that are less intuitive might benefit from being
explained in context. Doing so improves users' comprehension of the value
derived from the permission. Figure 1 shows an example of educating a user
in context.

![](https://developer.android.com/static/topic/performance/issues/images/educate-in-context.png)


**Figure 1.**
Explaining a permission request in context

<br />

Users understand the value proposition better when the app requests the
permission in the context of the related functionality.
This improved understanding might convince more users to grant permission
requests.

For more information about good guidelines about how to educate users and
request permissions, see the
[material design pattern for permissions](https://material.io/guidelines/patterns/permissions.html#permissions-denied-permissions).

### Explain why your app needs the permission

Consider starting by requesting your permission in-context: Providing an
explanation for less intuitive permissions helps to improve user comprehension
of the permission. The
[`shouldShowRequestPermissionRationale()`](https://developer.android.com/reference/androidx/core/app/ActivityCompat#shouldShowRequestPermissionRationale(android.app.Activity,%20java.lang.String))
utility method returns true
if the user has previously denied the request. Your app can use this method to
determine when to show the explanation.

You can find more details about how to surface explanation strings in
[Request App Permissions](https://developer.android.com/training/permissions/requesting).