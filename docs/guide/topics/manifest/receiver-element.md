---
title: https://developer.android.com/guide/topics/manifest/receiver-element
url: https://developer.android.com/guide/topics/manifest/receiver-element
source: md.txt
---

# &lt;receiver>

syntax:
:

    ```xml
    <receiver android:directBootAware=["true" | "false"]
              android:enabled=["true" | "false"]
              android:exported=["true" | "false"]
              android:icon="drawable resource"
              android:label="string resource"
              android:name="string"
              android:permission="string"
              android:process="string" >
        ...
    </receiver>
    ```

contained in:
:   [<application>](https://developer.android.com/guide/topics/manifest/application-element)

can contain:
:   [<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)  
    [<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element)

description:
:   Declares a broadcast receiver, a[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)subclass, as one of the application's components. Broadcast receivers enable applications to receive intents that are broadcast by the system or by other applications, even when other components of the application aren't running.

    There are two ways to make a broadcast receiver known to the system. One is to declare it in the manifest file with this element. The other is to create the receiver dynamically in code and register it with the[Context.registerReceiver()](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,%20android.content.IntentFilter))method or one of its overloaded versions.

    For more information about how to dynamically create receivers, see the[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)class description.

    If this receiver handles non-system broadcasts, specify a value for`android:exported`. Set this value to`"true"`if you want your receiver to be able to receiver broadcasts from other applications or`"false"`if you only want your receiver to be able to receive broadcasts from your own app.

    You don't have to remove the`android:permission`attribute if you already declared it.

    **Warning:** Limit how many broadcast receivers you set in your app. Having too many broadcast receivers can affect your app's performance and the battery life of users' devices. For more information about APIs you can use instead of the`BroadcastReceiver`class for scheduling background work, see[Background optimization](https://developer.android.com/topic/performance/background-optimization).

attributes:
:

    `android:directBootAware`

    :   Whether the broadcast receiver is*Direct-Boot aware*, that is, whether it can run before the user unlocks the device.

        **Note:** During[Direct Boot](https://developer.android.com/training/articles/direct-boot), a broadcast receiver in your application can only access the data that is stored in*device protected*storage.

        The default value is`"false"`.

    `android:enabled`
    :   Whether the broadcast receiver can be instantiated by the system. It's`"true"`if it can be, and`"false"`if not. The default value is`"true"`.

        The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element has its own[enabled](https://developer.android.com/guide/topics/manifest/application-element#enabled)attribute that applies to all application components, including broadcast receivers. The`<application>`and`<receiver>`attributes must both be`"true"`for the broadcast receiver to be enabled. If either is`"false"`, it's disabled and can't be instantiated.

    `android:exported`
    :   Whether the broadcast receiver can receive messages from non-system sources outside its application. It's`"true"`if it can, and`"false"`if not. If`"false"`, the only messages the broadcast receiver receives are those sent by the system, components of the same application, or applications with the same user ID.

        If unspecified, the default value depends on whether the broadcast receiver contains intent filters. If the receiver contains at least one intent filter, then the default value is`"true"`. Otherwise, the default value is`"false"`.

        This attribute is not the only way to limit a broadcast receiver's external exposure. You can also use a permission to limit the external entities that can send it messages. See the[permission](https://developer.android.com/guide/topics/manifest/receiver-element#prmsn)attribute.

    `android:icon`
    :   An icon representing the broadcast receiver. This attribute is set as a reference to a drawable resource containing the image definition. If it isn't set, the icon specified for the application as a whole is used instead. See the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[icon](https://developer.android.com/guide/topics/manifest/application-element#icon)attribute.

        The broadcast receiver's icon, whether set here or by the`<application>`element, is also the default icon for all the receiver's intent filters. See the[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)element's[icon](https://developer.android.com/guide/topics/manifest/intent-filter-element#icon)attribute.

    `android:label`
    :   A user-readable label for the broadcast receiver. If this attribute isn't set, the label set for the application as a whole is used instead. See the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[label](https://developer.android.com/guide/topics/manifest/application-element#label)attribute.

        The broadcast receiver's label, whether set here or by the`<application>`element, is also the default label for all the receiver's intent filters. See the[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)element's[label](https://developer.android.com/guide/topics/manifest/intent-filter-element#label)attribute.

        The label is set as a reference to a string resource, so that it can be localized like other strings in the user interface. However, as a convenience while you're developing the application, it can also be set as a raw string.

    `android:name`
    :   The name of the class that implements the broadcast receiver, a subclass of[BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver). This is a fully qualified class name, such as`"com.example.project.ReportReceiver"`. However, as a shorthand, if the first character of the name is a period, for example,`".ReportReceiver"`, it is appended to the package name specified in the[<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)element.

        Once you publish your application,[don't change this name](http://android-developers.blogspot.com/2011/06/things-that-cannot-change.html), unless you set[android:exported](https://developer.android.com/guide/topics/manifest/receiver-element#exported)`="false"`.

        There is no default. The name must be specified.

    `android:permission`
    :   The name of a permission that broadcasters need in order to send a message to the broadcast receiver. If this attribute isn't set, the permission set by the[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[permission](https://developer.android.com/guide/topics/manifest/application-element#prmsn)attribute applies to the broadcast receiver. If neither attribute is set, the receiver isn't protected by a permission.

        For more information about permissions, see the[Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)section in the app manifest overview and[Security tips](https://developer.android.com/guide/topics/security/security).

    `android:process`

    :   The name of the process in which the broadcast receiver runs. Normally, all components of an application run in the default process created for the application. It has the same name as the application package.<br />

        The[<application>](https://developer.android.com/guide/topics/manifest/application-element)element's[process](https://developer.android.com/guide/topics/manifest/application-element#proc)attribute can set a different default for all components. But each component can override the default with its own`process`attribute, letting you spread your application across multiple processes.

        If the name assigned to this attribute begins with a colon (`:`), a new process, private to the application, is created when it's needed, and the broadcast receiver runs in that process.

        If the process name begins with a lowercase character, the receiver runs in a global process of that name, provided that it has permission to do so. This lets components in different applications share a process, reducing resource usage.

introduced in:
:   API level 1