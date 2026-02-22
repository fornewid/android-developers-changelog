---
title: https://developer.android.com/training/cars/apps/library/request-permissions
url: https://developer.android.com/training/cars/apps/library/request-permissions
source: md.txt
---

If your app needs access to restricted data or actions---for example,
location---the [standard rules of Android permissions](https://developer.android.com/guide/topics/permissions/overview) apply. To request
a permission, you can use the [`CarContext.requestPermissions()`](https://developer.android.com/reference/androidx/car/app/CarContext#requestPermissions(java.util.List%3Cjava.lang.String%3E,%20java.util.concurrent.Executor,%20androidx.car.app.OnRequestPermissionsListener)) method.
| **Warning:** You must update to `androidx.car.app:1.7.0-alpha01` or later for the permissions dialog to show up on the phone screen when your app is used on a device running Android 14 or higher.

The benefit of using `CarContext.requestPermissions()`, as opposed to using
[standard Android APIs](https://developer.android.com/training/permissions/requesting#request-permission), is that you needn't launch your own `Activity` to
create the permissions dialog. Moreover, you can use the same code on both
Android Auto and Android Automotive OS, instead of creating platform-dependent
flows.

## Style the permissions dialog on Android Auto

On Android Auto, the permissions dialog for the user appears on the phone.
By default, there's no background to the dialog.

To set a custom background:

1. To declare a [car app theme](https://developer.android.com/training/cars/apps/library/configure-manifest#custom-theme) in your `AndroidManifest.xml` file
   and set the `carPermissionActivityLayout` attribute for your car app theme:

       <meta-data
          android:name="androidx.car.app.theme"
          android:resource="@style/<var>MyCarAppTheme</var> />

2. To set the `carPermissionActivityLayout` attribute for your car app theme:

       <resources>
        <style name="<var>MyCarAppTheme</var>">
          <item name="carPermissionActivityLayout">@layout/<var>my_custom_background</var></item>
        </style>
       </resources>