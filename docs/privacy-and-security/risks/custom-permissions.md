---
title: https://developer.android.com/privacy-and-security/risks/custom-permissions
url: https://developer.android.com/privacy-and-security/risks/custom-permissions
source: md.txt
---

# Custom Permissions

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

The risks associated with Custom Permissions arise when either the custom permissions definition is missing or misspelled, or when the corresponding`android:protectionLevel`attribute is misused within the Manifest.

For example, these risks can be exploited by creating a custom permission with the same name, but defined by a malicious app and with different protection levels applied.

Custom permissions are designed to enable sharing resources and capabilities with other apps. Examples of a legitimate use of custom permissions could be the following:

- Controlling inter-process communication (IPC) between two or more apps
- Accessing third-party services
- Restricting access to the shared data of an app

## Impact

The impact of exploiting this vulnerability is that a malicious app could gain access to resources originally intended to be protected. The implications of the vulnerability depend on the resource being protected and the original application service's associated permissions.

## Risk: Custom Permission Typos

A custom permission may be declared in the Manifest, but a different custom permission is used to protect exported Android components, due to a typo. A malicious application can capitalize on applications that have misspelled a permission by either:

- Registering that permission first
- Anticipating the spelling in subsequent applications

This can allow an application unauthorized access to resources or control over the victim application.

For example, a vulnerable app wants to protect a component by using a permission`READ_CONTACTS`but accidentally misspells the permission as`READ_CONACTS`. A malicious app can claim`READ_CONACTS`since it's not owned by any application (or the system) and gain access to the protected component. Another common variant of this vulnerability is`android:permission=True`. Values such as`true`and`false`, regardless of capitalization, are invalid inputs for the permission declaration and are treated similarly to other custom permission declaration typos. To fix this, the value of the`android:permission`attribute should be changed to a valid permission string. For example, if the app needs to access the user's contacts, the value of the`android:permission`attribute should be`android.permission.READ_CONTACTS`.

### Mitigations

#### Android Lint Checks

When declaring custom permissions, use Android lint checks to help you find typos and other potential errors in your code.

#### Naming Convention

Use a consistent naming convention to make typos more noticeable. Carefully check the custom permission declarations in your app's Manifest for typos.

*** ** * ** ***

## Risk: Orphaned Permissions

Permissions are used to guard resources of apps. There are two different locations where an app can declare the permissions required for accessing resources:

- AndroidManifest.xml: Predefined in the AndroidManifest.xml file (if not specified,`<application>`permissions are used), e.g.,[provider permission](https://developer.android.com/guide/topics/manifest/provider-element#prmsn),[receiver permission](https://developer.android.com/guide/topics/manifest/receiver-element#prmsn),[activity permission](https://developer.android.com/guide/topics/manifest/activity-element#prmsn),[service permission](https://developer.android.com/guide/topics/manifest/service-element#prmsn);
- Code: Registered in the runtime code, e.g.,[`registerReceiver()`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter)).

However, sometimes these permissions are not defined by a corresponding`<permission>`tag in a Manifest of an APK on the device. In this case, they are called**orphaned permissions**. This situation can occur for a number of reasons, such as:

- There could be a desync between updates on the Manifest and the code with the permission check
- The APK with the permissions might not be included in the build, or the wrong version could be included
- The permission name in either the check or the Manifest could be spelled incorrectly

A malicious app could define an orphaned permission and acquire it. If this happens, then the privileged applications that trust the orphaned permission to protect a component could be compromised.

In cases where the privileged app uses the permission to protect or restrict any component, this could grant the malicious app access to that component. Examples include launching activities protected by a permission, accessing a content provider, or broadcasting to a broadcast receiver protected by the orphaned permission.

It could also create a situation where the privileged application is tricked into believing the malicious app is a legitimate app and therefore loading files or content.

### Mitigations

Ensure that all custom permissions that your app uses to protect components are also defined in your Manifest.

The app uses the custom permissions`my.app.provider.READ`and`my.app.provider.WRITE`in order to protect access to a content provider:  

### Xml

    <provider android:name="my.app.database.CommonContentProvider" android:readPermission="my.app.provider.READ" android:writePermission="my.app.provider.WRITE" android:exported="true" android:process=":myappservice" android:authorities="my.app.database.contentprovider"/>

The app also defines and uses these custom permissions, thus preventing other malicious apps from doing so:  

### Xml

    <permission android:name="my.app.provider.READ"/>
    <permission android:name="my.app.provider.WRITE"/>
    <uses-permission android:name="my.app.provider.READ" />
    <uses-permission android:name="my.app.provider.WRITE" />

*** ** * ** ***

## Risk: Misused android:protectionLevel

This attribute describes the potential risk level in the permission and indicates what procedures the system should follow when deciding whether or not to grant the permission.

### Mitigations

#### Avoid Normal or Dangerous Protection Level

Using a**normal** or**dangerous** `protectionLevel`on your permissions means most apps can request and get the permission:

- "normal" requires only declaring it
- "dangerous" will be approved by many users

Therefore, these`protectionLevels`provide little security.

#### Use Signature Permissions (Android \>= 10)

Use signature protection levels wherever possible. Employing this capability ensures only other apps signed with the same certificate as the app that created the permission can access those protected features. Ensure you are using a dedicated (not reused) signing certificate and store it securely in a[keystore](https://developer.android.com/privacy-and-security/keystore).

Define a custom permission as follows in your Manifest:  

### Xml

    <permission
        android:name="my.custom.permission.MY_PERMISSION"
        android:protectionLevel="signature"/>

Restrict the access to, e.g., an activity, to only those apps which have this custom permission granted, as follows:  

### Xml

    <activity android:name=".MyActivity" android:permission="my.custom.permission.MY_PERMISSION"/>

Any other app that is signed with the same certificate as the app that declared this custom permission will then be granted access to the`.MyActivity`activity and needs to declare it as follows in its Manifest:  

### Xml

    <uses-permission android:name="my.custom.permission.MY_PERMISSION" />

#### Beware of Signature Custom Permissions (Android \< 10)

If your app targets Android \< 10, then whenever your app's custom permissions are removed due to uninstalls or updates there could be malicious apps able to still use those custom permissions and thus bypassing checks. This is due to a privilege escalation vulnerability ([`CVE-2019-2200`](https://nvd.nist.gov/vuln/detail/CVE-2019-2200)) which was[fixed](https://source.android.com/docs/security/bulletin/2020-02-01)in Android 10.

This is one of the reasons (along with the risk of race conditions) why signature checks are recommended over custom permissions.

*** ** * ** ***

## Risk: Race Condition

If a legitimate app`A`defines a signature custom permission that is used by other`X`apps but it is subsequently uninstalled, then a malicious app`B`can define that same custom permission with a different`protectionLevel`, e.g.*normal* . In this way,`B`gains access to all components protected by that custom permission in the`X`apps without any need to be signed with the same certificate as the app`A`.

The same happens if`B`gets installed before`A`.

### Mitigations

If you would like to make a component only available to apps signed with the same signature as the providing app, you might be able to avoid defining custom permissions to restrict access to that component. In this situation you can use signature checks. When one of your apps makes a request for another of your apps, the second app can verify that both apps are signed with the same certificate before complying with the request.

*** ** * ** ***

## Resources

- [Minimize your permission requests](https://developer.android.com/training/permissions/evaluating)
- [Permissions Overview](https://developer.android.com/guide/topics/permissions/overview)
- [Protection levels description](https://developer.android.com/guide/topics/manifest/permission-element#plevel)
- [CustomPermissionTypo Android Lint](https://cs.android.com/android-studio/platform/tools/base/+/mirror-goog-studio-main:lint/libs/lint-checks/src/main/java/com/android/tools/lint/checks/PermissionErrorDetector.kt)
- [How to use an Android Lint](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/androidx-main/docs/lint_guide.md#tips)
- [Research paper with in-depth explanation of Android Permissions and interesting fuzz test findings](https://diaowenrui.github.io/paper/oakland21-li.pdf)