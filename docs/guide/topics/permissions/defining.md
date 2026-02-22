---
title: https://developer.android.com/guide/topics/permissions/defining
url: https://developer.android.com/guide/topics/permissions/defining
source: md.txt
---

This document describes how app developers can use the
security features provided by Android to define their own permissions. By
defining custom permissions, an app can share its resources and capabilities
with other apps. For more information about permissions, see the [permissions overview](https://developer.android.com/guide/topics/permissions/requesting).

## Background


Android is a privilege-separated operating system, in which each
app runs with a distinct system identity (Linux user ID and group
ID). Parts of the system are also separated into distinct identities.
Linux thereby isolates apps from each other and from the system.


Apps can expose their functionality to other apps by defining permissions
that other apps can request. They can also define permissions that
are automatically made available to any other apps that are signed with the
same certificate.

### App signing


All APKs must be [signed with a certificate](https://developer.android.com/studio/publish/app-signing#certificates-keystores)
whose private key is held by their developer. The certificate does *not*
need to be signed by a certificate authority. It's allowable, and
typical, for Android apps to use self-signed certificates. The purpose of
certificates in Android is to distinguish app authors. This lets
the system grant or deny apps access to [signature-level
permissions](https://developer.android.com/guide/topics/manifest/permission-element#plevel) and grant or deny an app's [request to be given
the same Linux identity](https://developer.android.com/guide/topics/manifest/manifest-element#uid) as another app.

#### Grant signature permissions after device manufacturing time

Starting in Android 12 (API level 31), the
[`knownCerts`](https://developer.android.com/reference/android/R.attr#knownCerts) attribute for
signature-level permissions lets you refer to the digests of known signing
certificates at declaration
time.

You can declare the `knownCerts` attribute and use the `knownSigner` flag
in your app's [`protectionLevel`](https://developer.android.com/reference/android/R.attr#protectionLevel)
attribute
for a particular signature-level permission. Then, the system
grants that permission to a requesting app if any signer in the requesting app's
signing lineage, including the current signer, matches one of the digests that's
declared with the permission in the `knownCerts` attribute.

The `knownSigner` flag lets devices and apps grant signature permissions to
other apps without having to sign the apps at the time of device manufacturing
and shipment.

### User IDs and file access


At install time, Android gives each package a distinct Linux user ID. The
identity remains constant for the duration of the package's life on that
device. On a different device, the same package might have a different
UID---what matters is that each package has a distinct UID on a given
device.


Because security enforcement happens at the
process level, the code of any two packages can't normally
run in the same process, since they need to run as different Linux users.


Any data stored by an app is assigned that app's user
ID and isn't normally accessible to other packages.


For more information about Android's security model, see [Android Security
Overview](https://source.android.com/tech/security/index.html).
| **Warning:** The `https://developer.android.com/guide/topics/manifest/manifest-element#uid` attribute in the `AndroidManifest.xml` file's [`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element) tag for each package can be used to have multiple packages assigned the same user ID. However, shared user IDs cause non-deterministic behavior within the package manager. As such, their use is strongly discouraged and may be removed in a future version of Android. Instead, apps should use proper communication mechanisms, such as services and content providers, to facilitate interoperability between shared components. Note that existing apps can't remove this value, because migrating off a shared user ID is not supported.

## Define and enforce permissions


To enforce your own permissions, you must first declare them in your
`AndroidManifest.xml` using one or more [`<permission>`](https://developer.android.com/guide/topics/manifest/permission-element) elements.

### Naming convention

The system doesn't allow multiple packages to declare
a permission with the same name unless all the packages are signed with the
same certificate. If a package declares a permission, the system also doesn't
permit the user to install other packages with the same permission name, unless
those packages are signed with the same certificate as the first package.

We recommend prefixing permissions with an app's package name, using
reverse-domain-style naming, followed by `.permission.`
and then a description of the capability that the permission represents, in
upper SNAKE_CASE. For example,
`com.example.myapp.permission.ENGAGE_HYPERSPACE`.

Following this recommendation avoids naming collisions and helps clearly
identify the owner and intention of a custom permission.

### Example


For example, an app that needs to control which other apps can start one
of its activities can declare a permission for this operation as follows:

```xml
<manifest
  xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.myapp" >
    
    <permission
      android:name="com.example.myapp.permission.DEADLY_ACTIVITY"
      android:label="@string/permlab_deadlyActivity"
      android:description="@string/permdesc_deadlyActivity"
      android:permissionGroup="android.permission-group.COST_MONEY"
      android:protectionLevel="dangerous" />
    ...
</manifest>
```


The `https://developer.android.com/guide/topics/manifest/permission-element#plevel` attribute is required and tells the system how to
inform users of apps requiring the permission or what apps can
hold the permission, as described in the linked documentation.

The [`android:permissionGroup`](https://developer.android.com/guide/topics/manifest/permission-group-element)
attribute is optional and only used to help the system display permissions
to the user. In most cases, you set this to a standard system
group (listed in `https://developer.android.com/reference/android/Manifest.permission_group`),
although you can define a group yourself, as described in the following section.
We recommend using an existing group, because this simplifies the
permission UI shown to the user.


You need to supply both a label and description for the
permission. These are string resources that the user can see when
they are viewing a list of permissions
([`android:label`](https://developer.android.com/guide/topics/manifest/permission-element#label))
or details on a single permission
([`android:description`](https://developer.android.com/guide/topics/manifest/permission-element#desc)).
The label is short: a few words describing the key piece of
functionality the permission is protecting. The description is a
couple of sentences describing what the permission lets a holder do. Our
convention is a two-sentence description where the first sentence describes
the permission and the second sentence warns the user of the type of things
that can go wrong if an app is granted the permission.


Here is an example of a label and description for the
`https://developer.android.com/reference/android/Manifest.permission#CALL_PHONE`
permission:

```xml
<string name="permlab_callPhone">directly call phone numbers</string>
<string name="permdesc_callPhone">Allows the app to call non-emergency
phone numbers without your intervention. Malicious apps may cause unexpected
calls on your phone bill.</string>
```

### Create a permission group

As shown in the previous section, you can use the
[`android:permissionGroup`](https://developer.android.com/guide/topics/manifest/permission-group-element) attribute to help the system describe
permissions to the user. In most cases, you set this to a standard
system group (listed in
`https://developer.android.com/reference/android/Manifest.permission_group`),
but you can also define your own group with
`https://developer.android.com/guide/topics/manifest/permission-group-element`.

The `<permission-group>` element defines a label for a set
of permissions---both those declared in the manifest with
`https://developer.android.com/guide/topics/manifest/permission-element`
elements and those declared elsewhere. This affects only how the permissions are
grouped when presented to the user. The
`<permission-group>`
element doesn't specify the permissions that belong to the group, but
it gives the group a name.

You can place a permission in the group by assigning the group name to the
`https://developer.android.com/guide/topics/manifest/permission-element`
element's
`https://developer.android.com/guide/topics/manifest/permission-element#pgroup`
attribute.

The
`https://developer.android.com/guide/topics/manifest/permission-tree-element`
element declares a namespace for a group of permissions that are defined in
code.

### Custom permission recommendations


You can define custom permissions for your apps and request custom permissions
from other apps by defining [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) elements.
However, carefully assess whether it is necessary to do so.

- If you are designing a suite of apps that expose functionality to one another, try to design the apps so that each permission is defined only once. You must do this if the apps aren't all signed with the same certificate. Even if the apps are all signed with the same certificate, it's a best practice to define each permission only once.
- If the functionality is only available to apps signed with the same signature as the providing app, you might be able to avoid defining custom permissions by using signature checks. When one of your apps makes a request of another of your apps, the second app can verify that both apps are signed with the same certificate before complying with the request.

If a custom permission is necessary, consider whether only applications signed
by the same developer as the application performing the permission check need to
access it---such as when implementing secure interprocess communications
between two applications from the same developer. If so, we recommend using
[signature permissions](https://developer.android.com/guide/topics/permissions/overview#signature).
Signature permissions are transparent to the user and avoid user-confirmed
permissions, which can be confusing to users.

### Continue reading about:

[`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
:   API reference for the manifest tag that declares your app's required system permissions.

### You might also be interested in:

[Android Security Overview](https://source.android.com/devices/tech/security/index.html)
:   A detailed discussion about the Android platform's security model.