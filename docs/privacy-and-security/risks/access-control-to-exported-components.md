---
title: https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components
url: https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components
source: md.txt
---

# Permission-based access control to exported components

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

An Android permission is a string identifier declared in the app's manifest to request access to restricted data or actions, enforced at runtime by the Android framework.

[Android permission levels](https://developer.android.com/guide/topics/manifest/permission-element#plevel)indicate the potential risk associated with the permission:

- **Normal**: Low-risk permissions, automatically granted at install time
- **Dangerous**: High-risk permissions that could allow access to sensitive user data, requiring explicit user approval at runtime
- **Signature**: Granted only to apps signed with the same certificate as the app declaring the permission, typically used for system apps or interactions between apps from the same developer

Vulnerabilities related to permission-based access controls occur when an app's component (such as[activity](https://developer.android.com/reference/android/app/Activity),[receiver](https://developer.android.com/privacy-and-security/security-tips#broadcast-receivers),[content provider](https://developer.android.com/privacy-and-security/security-tips#content-providers), or[service](https://developer.android.com/privacy-and-security/security-tips#services)) meets all of the following criteria:

- The component is not associated with any`android:permission`in the`Manifest`;
- The component performs a sensitive task for which a permission exists that the user has already approved;
- The component is exported;
- The component does not perform any manual (manifest or code-level) permission checks;

When this happens, a malicious app can perform sensitive actions by abusing the privileges of the vulnerable component, proxying the vulnerable app's privileges to the malicious app.

## Impact

Exporting vulnerable components can be used to gain access to sensitive resources or to perform sensitive actions. The impact of this unwanted behavior depends on the context of the vulnerable component and its privileges.

## Mitigations

### Require permissions for sensitive tasks

When exporting a component with sensitive permissions, require those same permissions for any incoming request. The Android Studio IDE has lint checks for[receivers](https://googlesamples.github.io/android-custom-lint-rules/checks/ExportedReceiver.md.html)and[services](https://googlesamples.github.io/android-custom-lint-rules/checks/ExportedService.md.html)to spot this vulnerability and recommend requiring the appropriate permissions.

Developers can require permissions for incoming requests either by declaring them in the`Manifest`file or at code-level when implementing the service, as in the following examples.  

### Xml

    <manifest ...>
        <uses-permission android:name="android.permission.READ_CONTACTS" />

        <application ...>
            <service android:name=".MyExportService"
                     android:exported="true"
                     android:permission="android.permission.READ_CONTACTS" />

            </application>
    </manifest>

### Kotlin

    class MyExportService : Service() {

        private val binder = MyExportBinder()

        override fun onBind(intent: Intent): IBinder? {
            // Enforce calling app has the required permission
            enforceCallingPermission(Manifest.permission.READ_CONTACTS, "Calling app doesn't have READ_CONTACTS permission.")
            // Permission is enforced, proceed with export logic
            return binder
        }

        // Inner class for your Binder implementation
        private inner class MyExportBinder : Binder() {
            // Permission is enforced, proceed with export logic
        }
    }

### Java

    public class MyExportService extends Service {

        @Override
        public IBinder onBind(Intent intent) {
            // Enforce calling app has the required permission
            enforceCallingPermission(Manifest.permission.READ_CONTACTS, "Calling app doesn't have READ_CONTACTS permission.");

            return binder;

        }

        // Inner class for your Binder implementation
        private class MyExportBinder extends Binder {
            // Permission is enforced, proceed with export logic

        }
    }

### Don't export the component

Avoid exporting components with access to sensitive resources unless absolutely necessary. You can achieve this by setting the`android:exported`in the`Manifest`file to`false`for your component. From[API level 31](https://developer.android.com/about/versions/12/behavior-changes-12#exported)and beyond, this attribute is set to`false`by default.  

### Xml

    <activity
        android:name=".MyActivity"
        android:exported="false"/>

### Apply signature-based permissions

When sharing data between two apps that you control or own, use signature-based permissions. These permissions don't require user confirmation and, instead, check that the apps accessing the data is signed using the same signing key. This setup offers a more streamlined, secure user experience. If you declare custom permissions do consider the[corresponding security guidelines](https://developer.android.com/privacy-and-security/risks).  

### Xml

    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.example.myapp">
        <permission android:name="my_custom_permission_name"
                    android:protectionLevel="signature" />

### Single-task endpoints

Implement your app by following the[Separation of Concerns](https://developer.android.com/topic/architecture#separation-of-concerns)design principle. Each endpoint should only perform a small set of specific tasks with specific privileges. This good design practice also allows the developer to apply granular permissions for each endpoint. For example, avoid creating a single endpoint that serves both calendar and contacts.

## Resources

- [Android Access to app protected components from the Oversecured blog](https://blog.oversecured.com/Android-Access-to-app-protected-components/)
- [Content Provider Best Practices](https://developer.android.com/privacy-and-security/security-tips#content-providers)
- [Runtime (Dangerous) Permissions](https://developer.android.com/guide/topics/permissions/overview#runtime)
- [Separation of Concerns design principle](https://developer.android.com/topic/architecture#separation-of-concerns)
- [Android permissions documentation](https://developer.android.com/guide/topics/manifest/permission-element#plevel)
- [Android broadcast receivers security tips](https://developer.android.com/privacy-and-security/security-tips#broadcast-receivers)
- [Android services security tips](https://developer.android.com/privacy-and-security/security-tips#services)
- [Android 12 (API 31) exported default set to "false"](https://developer.android.com/about/versions/12/behavior-changes-12#exported)
- [Lint Check: Exported PreferenceActivity shouldn't be exported](https://googlesamples.github.io/android-custom-lint-rules/checks/ExportedPreferenceActivity.md.html)
- [Lint Check: Exported Receiver doesn't require permission](https://googlesamples.github.io/android-custom-lint-rules/checks/ExportedReceiver.md.html)
- [Lint Check: Exported Service doesn't require permission](https://googlesamples.github.io/android-custom-lint-rules/checks/ExportedService.md.html)