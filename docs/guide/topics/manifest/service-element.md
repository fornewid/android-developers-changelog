---
title: https://developer.android.com/guide/topics/manifest/service-element
url: https://developer.android.com/guide/topics/manifest/service-element
source: md.txt
---

# &lt;service>

syntax:
:

    ```xml
    <service android:description="string resource"
             android:directBootAware=["true" | "false"]
             android:enabled=["true" | "false"]
             android:exported=["true" | "false"]
             android:foregroundServiceType=["camera" | "connectedDevice" |
                                            "dataSync" | "health" | "location" |
                                            "mediaPlayback" | "mediaProjection" |
                                            "microphone" | "phoneCall" |
                                            "remoteMessaging" | "shortService" |
                                            "specialUse" | "systemExempted"]
             android:icon="drawable resource"
             android:isolatedProcess=["true" | "false"]
             android:label="string resource"
             android:name="string"
             android:permission="string"
             android:process="string"
             android:stopWithTask=["true" | "false"]>
        ...
    </service>
    ```

contained in:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)

can contain:
:   [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)  
    [<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element)

description:
:   Declares a service, a[Service](https://developer.android.com/reference/android/app/Service)subclass, as one of the application's components. Unlike activities, services lack a visual user interface. They're used to implement long-running background operations or a rich communications API that can be called by other applications.

    All services must be represented by`<service>`elements in the manifest file. Any that aren't declared there aren't seen by the system and never run.

    **Note:** On Android 8.0 (API level 26) and higher, the system limits what your app can do while it's running in the background. For more information, see the guides that discuss[background execution limits](https://developer.android.com/about/versions/oreo/background)and[background location limits](https://developer.android.com/about/versions/oreo/background-location-limits).

attributes:
:

    `android:description`
    :   A user-readable string that describes the service. The description is set as a reference to a string resource, so that it can be localized like other strings in the user interface.

    `android:directBootAware`

    :   Whether the service is*Direct-Boot aware*, that is, whether it can run before the user unlocks the device.

        **Note:** During[Direct Boot](https://developer.android.com/training/articles/direct-boot), a service in your application can only access the data that is stored in*device protected*storage.

        The default value is`"false"`.

    `android:enabled`
    :   Whether the service can be instantiated by the system. It's`"true"`if it can be, and`"false"`if not. The default value is`"true"`.

        The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element has its own[enabled](https://developer.android.com/guide/topics/manifest/application-element#enabled)attribute that applies to all application components, including services. The`<application>`and`<service>`attributes must both be`"true"`, as they both are by default, for the service to be enabled. If either is`"false"`, the service is disabled and can't be instantiated.

    `android:exported`
    :   Whether components of other applications can invoke the service or interact with it. It's`"true"`if they can, and`"false"`if not. When the value is`"false"`, only components of the same application or applications with the same user ID can start the service or bind to it.

        The default value depends on whether the service contains intent filters. The absence of any filters means that it can be invoked only by specifying its exact class name. This implies that the service is intended only for application-internal use, since others don't know the class name. So, in this case, the default value is`"false"`. On the other hand, the presence of at least one filter implies that the service is intended for external use, so the default value is`"true"`.

        This attribute isn't the only way to limit the exposure of a service to other applications. You can also use a permission to limit the external entities that can interact with the service. See the[permission](https://developer.android.com/guide/topics/manifest/service-element#prmsn)attribute.

    `android:foregroundServiceType`

    :   Specifies that the service is a[foreground service](https://developer.android.com/guide/components/services)that satisfies a particular use case. For example, a foreground service type of`"location"`indicates that an app is getting the device's current location, usually to[continue a user-initiated action](https://developer.android.com/training/location/background#continue-user-initiated-action)related to device location.

        You can assign multiple foreground service types to a particular service.

    `android:icon`
    :   An icon representing the service. This attribute is set as a reference to a drawable resource containing the image definition. If it isn't set, the icon specified for the application as a whole is used instead. See the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[icon](https://developer.android.com/guide/topics/manifest/application-element#icon)attribute.

        <br />

        The service's icon, whether set here or by the`<application>`element, is also the default icon for all the service's intent filters. See the[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)element's[icon](https://developer.android.com/guide/topics/manifest/intent-filter-element#icon)attribute.

    `android:isolatedProcess`
    :   If set to`"true"`, this service runs under a special process that is isolated from the rest of the system and has no permissions of its own. The only communication with it is through the Service API, with binding and starting.

    `android:label`
    :   A user-readable name for the service. If this attribute isn't set, the label set for the application as a whole is used instead. See the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[label](https://developer.android.com/guide/topics/manifest/application-element#label)attribute.

        The service's label, whether set here or by the`<application>`element, is also the default label for all the service's intent filters. See the[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)element's[label](https://developer.android.com/guide/topics/manifest/intent-filter-element#label)attribute.

        The label is set as a reference to a string resource, so that it can be localized like other strings in the user interface. However, as a convenience while you're developing the application, it can also be set as a raw string.

    `android:name`
    :   The name of the[Service](https://developer.android.com/reference/android/app/Service)subclass that implements the service. This is a fully qualified class name, such as`"com.example.project.RoomService"`. However, as a shorthand, if the first character of the name is a period, such as`".RoomService"`, it is appended to the package name specified in the[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)element.

        Once you publish your application,[don't change this name](http://android-developers.blogspot.com/2011/06/things-that-cannot-change.html), unless you set[android:exported](https://developer.android.com/guide/topics/manifest/service-element#exported)`="false"`.

        There is no default. The name must be specified.

    `android:permission`
    :   The name of a permission that an entity needs in order to launch the service or bind to it. If a caller of[startService()](https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)),[bindService()](https://developer.android.com/reference/android/content/Context#bindService(android.content.Intent, android.content.ServiceConnection, int)), or[stopService()](https://developer.android.com/reference/android/content/Context#stopService(android.content.Intent))isn't granted this permission, the method doesn't work and the`Intent`object isn't delivered to the service.

        If this attribute isn't set, the permission set by the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[permission](https://developer.android.com/guide/topics/manifest/application-element#prmsn)attribute applies to the service. If neither attribute is set, the service isn't protected by a permission.

        For more information about permissions, see the[Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)section in the app manifest overview and[Security guidelines](https://developer.android.com/privacy-and-security/security-tips).

    `android:process`
    :   The name of the process where the service runs. Normally, all components of an application run in the default process created for the application. It has the same name as the application package. The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[process](https://developer.android.com/guide/topics/manifest/application-element#proc)attribute can set a different default for all components. But a component can override the default with its own`process`attribute, letting you spread your application across multiple processes.

        If the name assigned to this attribute begins with a colon (`:`), a new process, private to the application, is created when it's needed and the service runs in that process.

        If the process name begins with a lowercase character, the service runs in a global process of that name, provided that it has permission to do so. This lets components in different applications share a process, reducing resource usage.

    `android:stopWithTask`
    :   If set to`"true"`, the system automatically stops the service when the user removes a task that is rooted in an activity that the app owns. The default value is`"false"`.

see also:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)  
    [<activity>](https://developer.android.com/guide/topics/manifest/activity-element)

introduced in:
:   API level 1