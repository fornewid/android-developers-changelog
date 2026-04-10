---
title: https://developer.android.com/guide/topics/manifest/uses-library-element
url: https://developer.android.com/guide/topics/manifest/uses-library-element
source: md.txt
---

# &lt;uses-library>

**Note:** Google Play uses the`<uses-library>`elements declared in your app manifest to filter your app from devices that don't meet its library requirements. For more information about filtering, see[Filters on Google Play](https://developer.android.com/google/play/filters).

syntax:
:

    ```xml
    <uses-library
      android:name="string"
      android:required=["true" | "false"] />
    ```

contained in:
:   `
    `[<application>](https://developer.android.com/guide/topics/manifest/application-element)`
    `

description:

:   Specifies a shared library that the application must be linked against. This element tells the system to include the library's code in the class loader for the package.

    All the`android`packages, such as[android.app](https://developer.android.com/reference/android/app/package-summary),[android.content](https://developer.android.com/reference/android/content/package-summary),[android.view](https://developer.android.com/reference/android/view/package-summary), and[android.widget](https://developer.android.com/reference/android/widget/package-summary), are in the default library that all applications are automatically linked against. However, some packages, such as`maps`, are in separate libraries that aren't automatically linked. Consult the documentation for the packages you're using to determine which library contains the package code.

    The order of`<uses-library>`tags is significant. It affects class lookup and resolution order when the application loads. Some of the libraries might have duplicate classes, and in that case the library that comes first takes priority.

    This element also affects the installation of the application on a particular device and the availability of the application on Google Play. If this element is present and its`android:required`attribute is set to`"true"`, the[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)framework won't let a user install the application unless the library is present on the user's device.

    The`android:required`attribute is described in detail in the following section.

attributes:
:

    `android:name`
    :   The name of the library. The name is provided by the documentation for the package you are using. An example of this is`"android.test.runner"`, a package that contains Android test classes.

    `android:required`
    :   Boolean value that indicates whether the application requires the library specified by`android:name`.

        - `"true"`: the application doesn't function without this library. The system doesn't let the application install on a device that doesn't have the library.
        - `"false"`: the application uses the library if present, but is designed to function without it if necessary. The system lets the application install, even if the library isn't present. If you use`"false"`, you are responsible for checking at runtime that the library is available.

          To check for a library, you can use reflection to determine whether a particular class is available.

        The default is`"true"`.

        Introduced in: API level 7.

introduced in:
:   API Level 1

see also:
:
    - [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)