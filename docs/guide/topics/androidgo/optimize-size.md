---
title: https://developer.android.com/guide/topics/androidgo/optimize-size
url: https://developer.android.com/guide/topics/androidgo/optimize-size
source: md.txt
---

# Reduce app size

Small app size is directly related to download success, particularly in emerging markets with poor network device connections or low network speeds. This can result in lower app usage rates, which in turn lowers the scope and reach of your audience. However, there are multiple ways to help reduce the size of your app.

## Best practices

### Upload app as Android App Bundle

The easiest way to gain immediate app size savings when publishing to Google Play is by uploading your app as an[Android App Bundle](https://developer.android.com/guide/app-bundle), which is a new publishing format that includes all your app's compiled code and resources, and defers APK generation and signing to Google Play.

### Reduce runtime code size

Check for code that your app doesn't use at runtime, for example any large classes or auto-generated code. Code optimizers like[R8](https://developer.android.com/studio/build/shrink-code)can help optimize and shrink code size, but they can't deal with code guarded by runtime-constants. Replace the check flags with compile-time constants to make the best use of various optimization tools. You can enable code and resource shrinking in your gradle configuration file:  

    android {
        buildTypes {
            getByName("release") {
                isMinifyEnabled = true
                isShrinkResources = true
            }
        }
    }

### Remove unnecessary layouts

Merge unused layouts with small UI changes and remove any unnecessary layouts to reduce overall app code size. Additionally, you can dynamically render layouts and views wherever possible. This lets you avoid drawing static templates and apply alternate layouts without the technical overhead.

### Re-evaluate infrequently used features

Specifically optimize for Android (Go edition) by disabling features that have low daily active user (DAU) metrics. Examples of this include removing complex animations, large GIF files, or any other aesthetic additions not necessary for app success.

### Utilize dynamic delivery

[Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)uses advanced capabilities of app bundles, allowing certain features of your app to be delivered conditionally or downloaded on demand. You can use feature modules for custom delivery. A unique benefit of feature modules is the ability to customize how and when different features of your app are downloaded onto devices running Android 5.0 (API level 21) or higher.

### Reduce translatable string size

You can use the Android Gradle`resConfigs`property to remove alternative resource files that your app doesn't need. If you're using a library that includes language resources (such as AppCompat or Google Play Services), then your app includes all translated language strings for library messages, regardless of app translation. If you'd like to keep only the languages that your app officially supports, you can specify those languages using the`resConfig`property. Any resources for languages not specified are removed.

To limit your language resources to just English and French, you can edit`defaultConfig`as shown below:  


    android {
        defaultConfig {
            ...
            resConfigs "en", "fr"
        }
    }

### Use selective translation

If a given string isn't visible in the app's UI, then you don't have to translate it. Strings for the purpose of debugging, exception messages, or URLs should be string literals in code, not resources.

For example, don't bother translating URLs.  

    <string name="car_frx_device_incompatible_sol_message">
      This device doesn\'t support Android Auto.\n
      &lt;a href="https://support.google.com/androidauto/answer/6395843"&gt;Learn more&lt;/a&gt;
    </string>

You may recognize`&lt;`and`&gt`, as these are escape characters for`<`and`>`. They're needed here because if you were to put an`<a>`tag inside of a`<string>`tag, then the Android resource compiler drops them since it doesn't recognize the tag. However, this means that you're translating the HTML tags and the URL to 78 languages. Instead, you can remove the HTML:  

    <string name="car_frx_device_incompatible_sol_message">
             This device doesn\'t support Android Auto.
    </string>

### Combine native binaries with common dependencies

If your app has different Java Native Interface (JNI) implementations with common underlying dependencies, then the various binaries are increasing the APK size with redundant components. You can combine several JNI binaries into a single JNI binary file while keeping the Java and JNI files separate. This can reduce your APK size quite dramatically.