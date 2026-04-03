---
title: https://developer.android.com/guide/topics/manifest/provider-element
url: https://developer.android.com/guide/topics/manifest/provider-element
source: md.txt
---

syntax:
:

    ```xml
    <provider android:authorities="list"
              android:directBootAware=["true" | "false"]
              android:enabled=["true" | "false"]
              android:exported=["true" | "false"]
              android:grantUriPermissions=["true" | "false"]
              android:icon="drawable resource"
              android:initOrder="integer"
              android:label="string resource"
              android:multiprocess=["true" | "false"]
              android:name="string"
              android:permission="string"
              android:process="string"
              android:readPermission="string"
              android:syncable=["true" | "false"]
              android:writePermission="string" >
        ...
    </provider>
    ```

contained in:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)

can contain:
:   [<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element)  
    [<grant-uri-permission>](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)  
    [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)  
    [<path-permission>](https://developer.android.com/guide/topics/manifest/path-permission-element)

description:
:   Declares a content provider component. A content provider is a subclass of[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)that supplies structured access to data managed by the application. All content providers in your application must be defined in a`<provider>`element in the manifest file. Otherwise, the system is unaware of them and doesn't run them.

    Only declare content providers that are part of your application. Don't declare content providers in other applications that you use in your application.

    The Android system stores references to content providers according to an*authority* string, part of the provider's*content URI* . For example, suppose you want to access a content provider that stores information about health care professionals. To do this, you call the method[ContentResolver.query()](https://developer.android.com/reference/android/content/ContentResolver#query(android.net.Uri, java.lang.String[], android.os.Bundle, android.os.CancellationSignal)), which takes a URI that identifies the provider, among other arguments:  

    ```
    content://com.example.project.healthcareprovider/nurses/rn
    ```

    The`content:`*scheme* identifies the URI as a content URI pointing to an Android content provider. The authority`com.example.project.healthcareprovider`identifies the provider itself. The Android system looks up the authority in its list of known providers and their authorities. The substring`nurses/rn`is a*path*, which the content provider uses to identify subsets of the provider data.

    When you define your provider in the`<provider>`element, you don't include the scheme or the path in the`android:name`argument, only the authority.

    For information about using and developing content providers, see[Content providers](https://developer.android.com/guide/topics/providers/content-providers).

attributes:
:

    `android:authorities`
    :   A list of one or more URI authorities that identify data offered by the content provider. List multiple authorities by separating their names with a semicolon. To avoid conflicts, use a Java-style naming convention for authority names, such as`com.example.provider.cartoonprovider`. Typically, it's the name of the[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)subclass that implements the provider

        There is no default. At least one authority must be specified.

    `android:enabled`
    :   Whether the content provider can be instantiated by the system. It's`"true"`if it can be, and`"false"`if not. The default value is`"true"`.

        The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element has its own[enabled](https://developer.android.com/guide/topics/manifest/application-element#enabled)attribute that applies to all application components, including content providers. The`<application>`and`<provider>`attributes both have to be`"true"`, as they both are by default, for the content provider to be enabled. If either is`"false"`, the provider is disabled. It can't be instantiated.

    `android:directBootAware`

    :   Whether the content provider is*Direct-Boot aware*---that is, whether it can run before the user unlocks the device.

        **Note:** During[Direct Boot](https://developer.android.com/training/articles/direct-boot), a content provider in your application can only access the data that is stored in*device protected*storage.

        The default value is`"false"`.

    `android:exported`
    :   Whether the content provider is available for other applications to use.

        - `"true"`: the provider is available to other applications. Any application can use the provider's content URI to access it, subject to the permissions specified for the provider.
        - `"false"`: the provider isn't available to other applications. Set`android:exported="false"`to limit access to the provider to your applications. Only applications that have the same user ID (UID) as the provider, or applications that are temporarily granted access to the provider through the[`android:grantUriPermissions`](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn)element, have access to it.

        Because this attribute was introduced in API level 17, all devices running API level 16 and lower behave as though this attribute is set`"true"`. If you set[android:targetSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target)to 17 or higher, then the default value is`"false"`for devices running API level 17 and higher.

        You can set`android:exported="false"`and still limit access to your provider by setting permissions with the[permission](https://developer.android.com/guide/topics/manifest/provider-element#prmsn)attribute.

    `android:grantUriPermissions`
    :   Whether those who ordinarily don't have permission to access the content provider's data can be granted permission to do so, temporarily overcoming the restriction imposed by the[readPermission](https://developer.android.com/guide/topics/manifest/provider-element#rprmsn),[writePermission](https://developer.android.com/guide/topics/manifest/provider-element#wprmsn),[permission](https://developer.android.com/guide/topics/manifest/provider-element#prmsn), and[exported](https://developer.android.com/guide/topics/manifest/provider-element#exported)attributes.

        <br />

        It's`"true"`if permission can be granted, and`"false"`if not. If`"true"`, permission can be granted to any of the content provider's data. If`"false"`, permission can be granted only to the data subsets listed in[<grant-uri-permission>](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)subelements, if any. The default value is`"false"`.

        Granting permission is a way of giving an application component one-time access to data protected by a permission. For example, when an email message contains an attachment, the mail application might call on the appropriate viewer to open it, even though the viewer doesn't have general permission to look at all the content provider's data.

        In such cases, permission is granted by[FLAG_GRANT_READ_URI_PERMISSION](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_READ_URI_PERMISSION)and[FLAG_GRANT_WRITE_URI_PERMISSION](https://developer.android.com/reference/android/content/Intent#FLAG_GRANT_WRITE_URI_PERMISSION)flags in the`Intent`object that activates the component. For example, the mail application might put`FLAG_GRANT_READ_URI_PERMISSION`in the`Intent`passed to`Context.startActivity()`. The permission is specific to the URI in the`Intent`.

        If you enable this feature, either by setting this attribute to`"true"`or by defining[<grant-uri-permission>](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)subelements, call[Context.revokeUriPermission()](https://developer.android.com/reference/android/content/Context#revokeUriPermission(android.net.Uri, int))when a covered URI is deleted from the provider.

        See also the[<grant-uri-permission>](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)element.

    `android:icon`
    :   An icon representing the content provider. This attribute is set as a reference to a drawable resource containing the image definition. If it isn't set, the icon specified for the application as a whole is used instead. For more information, see the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[icon](https://developer.android.com/guide/topics/manifest/application-element#icon)attribute.

    `android:initOrder`
    :   The order in which the content provider is instantiated, relative to other content providers hosted by the same process. When there are dependencies among content providers, setting this attribute for each of them makes sure that they are created in the order required by those dependencies. The value is an integer, with higher numbers being initialized first.

    `android:label`
    :   A user-readable label for the content provided. If this attribute isn't set, the label set for the application as a whole is used instead. For more information, see the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[label](https://developer.android.com/guide/topics/manifest/application-element#label)attribute.

        The label is usually set as a reference to a string resource, so that it can be localized like other strings in the user interface. However, as a convenience while you're developing the application, it can also be set as a raw string.

    `android:multiprocess`
    :   If the app runs in multiple processes, this attribute determines whether multiple instances of the content provider are created. If`"true"`, each of the app's processes has its own content provider object. If`"false"`, the app's processes share only one content provider object. The default value is`"false"`.

        Setting this flag to`"true"`can improve performance by reducing the overhead of interprocess communication, but it also increases the memory footprint of each process.

    `android:name`
    :   The name of the class that implements the content provider, a subclass of[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider). This is usually a fully qualified class name, such as`"com.example.project.TransportationProvider"`. However, as a shorthand, if the first character of the name is a period, it is appended to the package name specified in the[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)element.

        There is no default. The name must be specified.

    `android:permission`
    :   The name of a permission that clients must have to read or write the content provider's data. This attribute is a convenient way of setting a single permission for both reading and writing. However, the[readPermission](https://developer.android.com/guide/topics/manifest/provider-element#rprmsn),[writePermission](https://developer.android.com/guide/topics/manifest/provider-element#wprmsn), and[grantUriPermissions](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn)attributes take precedence over this one.

        <br />

        If the`readPermission`attribute is also set, it controls access for querying the content provider. If the`writePermission`attribute is set, it controls access for modifying the provider's data.

        For more information about permissions, see the[Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)section in the app manifest overview and[Security tips](https://developer.android.com/guide/topics/security/security).

    `android:process`

    :   The name of the process in which the content provider runs. Normally, all components of an application run in the default process created for the application. It has the same name as the application package.<br />

        The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[process](https://developer.android.com/guide/topics/manifest/application-element#proc)attribute can set a different default for all components. But each component can override the default with its own`process`attribute, letting you spread your application across multiple processes.

        If the name assigned to this attribute begins with a colon (`:`), a new process, private to the application, is created when it's needed and the activity runs in that process.

        If the process name begins with a lowercase character, the activity runs in a global process of that name, provided that it has permission to do so. This lets components in different applications share a process, reducing resource usage.

    `android:readPermission`

    :   A permission that clients must have to query the content provider.

        If the provider sets[`android:grantUriPermissions`](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn)to`"true"`, or if a given client satisfies the conditions of a[`<grant-uri-permission>`](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)subelement, the client can gain temporary read access to the content provider's data.

        See also the[permission](https://developer.android.com/guide/topics/manifest/provider-element#prmsn)and[writePermission](https://developer.android.com/guide/topics/manifest/provider-element#wprmsn)attributes.

    `android:syncable`
    :   Whether the data under the content provider's control can be synchronized with data on a server. It's`"true"`if it can be, and`"false"`if not.

    `android:writePermission`

    :   A permission that clients need to make changes to the data controlled by the content provider.

        If the provider sets[`android:grantUriPermissions`](https://developer.android.com/guide/topics/manifest/provider-element#gprmsn)to`"true"`, or if a given client satisfies the conditions of a[`<grant-uri-permission>`](https://developer.android.com/guide/topics/manifest/grant-uri-permission-element)subelement, the client can gain temporary write access to modify the content provider's data.

        See also the[permission](https://developer.android.com/guide/topics/manifest/provider-element#prmsn)and[readPermission](https://developer.android.com/guide/topics/manifest/provider-element#rprmsn)attributes.

introduced in:
:   API level 1

see also:
:   [Content providers](https://developer.android.com/guide/topics/providers/content-providers)