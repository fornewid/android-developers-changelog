---
title: https://developer.android.com/guide/slices/getting-started
url: https://developer.android.com/guide/slices/getting-started
source: md.txt
---

# Getting started

This page shows you how to set up your environment and build[Slices](https://developer.android.com/guide/slices)in your app.

**Note**: Android Studio 3.2 or later contains additional tools and functionality that can help you with Slice development:

- AndroidX refactoring tool: required if you're working in a project that uses AndroidX libraries.
- Slices lint checks: catches common anti-practices when building Slices
- `SliceProvider`template: handles the boilerplate when building a`SliceProvider`

<br />

## Download and install the Slice Viewer

Download the latest sample[Slice Viewer APK release](https://github.com/android/user-interface-samples/releases)that you can use to test your Slices without implementing the[`SliceView`](https://developer.android.com/reference/androidx/slice/widget/SliceView)API.
| **Note:** Slice Viewer requires Android 4.4 (API level 19) or later.

If ADB is not set up properly in your environment, see the[ADB guide](https://developer.android.com/studio/command-line/adb)for more information.

Install the Slice Viewer on your device by running the following command in the same directory as the downloaded`slice-viewer.apk`:  

    adb install -r -t slice-viewer.apk

## Run the Slice Viewer

You can launch the Slice Viewer either from your Android Studio project or from the command line:

### Launch Slice Viewer from your Android Studio project

1. In your project, select**Run \> Edit Configurations...**
2. In the top-left corner, click the green plus sign
3. Select**Android App**

   ![](https://developer.android.com/static/guide/slices/images/sliceviewer-setup-1.png)
4. Enter*slice*in the name field

5. Select your app module in the**Module**dropdown

6. Under**Launch Options** , select**URL** from the**Launch**dropdown

7. Enter`slice-<your slice URI>`in the URL field

   Example:`slice-content://com.example.your.sliceuri`

   ![](https://developer.android.com/static/guide/slices/images/sliceviewer-setup-2.png)
8. Click**OK**

| **Note:** You can use the configuration you've just created the next time you want to launch the Slice Viewer to view your Slice

### Launch the Slice Viewer tool via ADB (command line)

Run your app from Android Studio:  

    adb install -t -r <yourapp>.apk

View your Slice by running the following command:  

    adb shell am start -a android.intent.action.VIEW -d slice-<your slice URI>

![](https://developer.android.com/static/guide/slices/images/sliceviewer-1.png)

*Slice Viewer showing a single WiFi Slice*

### View all of your Slices in one place

In addition to launching a single Slice, you can view a persistent list of your Slices.

- Use the search bar to manually search for your Slices via URI (for example,`content://com.example.android.app/hello`). Each time you search, the Slice is added to the list.
- Any time you launch the Slice Viewer tool with a Slice URI, the Slice is added to the list.
- You can swipe a Slice to remove it from the list.
- Tap the URI of the Slice to see a page containing only that Slice. This has the same effect as launching Slice Viewer with a Slice URI.

| **Note:** Slice scrolling is disabled while displayed in the list. Launch your Slice into the single Slice Viewer to test your scrollability.

![](https://developer.android.com/static/guide/slices/images/sliceviewer-2.png)

*Slice Viewer showing a list of Slices*

### View the Slice in different modes

An app that presents a Slice can modify the[`SliceView#mode`](https://developer.android.com/reference/androidx/slice/widget/SliceView#MODE_LARGE)at runtime, so you should make sure your Slice looks as expected in each mode. Select the menu icon in the top-right area of the page to change the mode.

![](https://developer.android.com/static/guide/slices/images/sliceviewer-3.png)

*Single Slice viewer with mode set to "small"*

## Build your first Slice

To build a Slice, open your Android Studio project, right-click your`src`package, and select**New... \> Other \> Slice Provider** . This creates a class that extends[`SliceProvider`](https://developer.android.com/reference/androidx/slice/SliceProvider), adds the required provider entry to your`AndroidManifest.xml`, and modifies your`build.gradle`to add the required Slice dependencies.

The modification to`AndroidManifest.xml`is shown below:  

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.app">
    ...
    <application>
        ...
        <provider android:name="MySliceProvider"
            android:authorities="com.example.android.app"
            android:exported="true" >
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.app.slice.category.SLICE" />
            </intent-filter>
        </provider>
        ...
    </application>

</manifest>
```
| **Note:** You can safely export`SliceProvider`s, as all permission checks are handled internally.

The following dependencies are added to your`build.gradle`:  

### Kotlin

```kotlin
dependencies {
// ...
    implementation "androidx.slice:slice-builders-ktx:(latest version)"
// ...
}
```

### Java

```java
dependencies {
// ...
    implementation "androidx.slice:slice-builders:(latest version)"
// ...
}
```
| **Note:** The`SliceProvider`template points to the AndroidX libraries by default. If your project uses the legacy support libraries, make sure you modify the`build.gradle`file to point to`com.android.support:slices-builders:(latest version)`instead of the AndroidX equivalent.
| **Note:** If you're using Kotlin, note that`slice-builders-ktx`is available only in AndroidX. If you are using the legacy support library, use the standard`com.android.support:slices-builders:(latest version)`library instead.

Each Slice has an associated URI. When a surface wants to display a Slice, it sends a binding request to your app with this URI. Your app then handles this request and dynamically builds the Slice via the[`onBindSlice`](https://developer.android.com/reference/androidx/slice/SliceProvider#onBindSlice(android.net.Uri,%20java.util.List%3Candroid.app.slice.SliceSpec%3E))method. The surface can then display the Slice when appropriate.

Below is an example of an`onBindSlice`method that checks for the`/hello`URI path and returns a**Hello World**Slice:  

### Kotlin

```kotlin
override fun onBindSlice(sliceUri: Uri): Slice? {
    val activityAction = createActivityAction()
    return if (sliceUri.path == "/hello") {
        list(context, sliceUri, ListBuilder.INFINITY) {
            row {
                primaryAction = activityAction
                title = "Hello World."
            }
        }
    } else {
        list(context, sliceUri, ListBuilder.INFINITY) {
            row {
                primaryAction = activityAction
                title = "URI not recognized."
            }
        }
    }
}
```

### Java

```java
@Override
public Slice onBindSlice(Uri sliceUri) {
    if (getContext() == null) {
        return null;
    }
    SliceAction activityAction = createActivityAction();
    ListBuilder listBuilder = new ListBuilder(getContext(), sliceUri, ListBuilder.INFINITY);
    // Create parent ListBuilder.
    if ("/hello".equals(sliceUri.getPath())) {
        listBuilder.addRow(new ListBuilder.RowBuilder()
                .setTitle("Hello World")
                .setPrimaryAction(activityAction)
        );
    } else {
        listBuilder.addRow(new ListBuilder.RowBuilder()
                .setTitle("URI not recognized")
                .setPrimaryAction(activityAction)
        );
    }
    return listBuilder.build();
}
```

Use the**slice** run configuration that you created in the Slice Viewer section above, passing in your Slice URI (for example,`slice-content://com.android.example.slicesample/hello`) of the**Hello World**Slice to view it in the Slice Viewer.

![](https://developer.android.com/static/guide/slices/images/slice-1-helloworld.png)

## Interactive Slices

Similar to notifications, you can handle clicks within your Slice by attaching[`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent)objects that are triggered on user interaction. The example below starts an[`Activity`](https://developer.android.com/reference/android/app/Activity)that can receive and handle those intents:  

### Kotlin

```kotlin
fun createSlice(sliceUri: Uri): Slice {
    val activityAction = createActivityAction()
    return list(context, sliceUri, INFINITY) {
        row {
            title = "Perform action in app"
            primaryAction = activityAction
        }
    }
}

fun createActivityAction(): SliceAction {
    val intent = Intent(context, MainActivity::class.java)
    return SliceAction.create(
        PendingIntent.getActivity(context, 0, Intent(context, MainActivity::class.java), 0),
        IconCompat.createWithResource(context, R.drawable.ic_home),
        ListBuilder.ICON_IMAGE,
        "Enter app"
    )
}
```

### Java

```java
public Slice createSlice(Uri sliceUri) {
    if (getContext() == null) {
        return null;
    }
    SliceAction activityAction = createActivityAction();
    return new ListBuilder(getContext(), sliceUri, ListBuilder.INFINITY)
            .addRow(new ListBuilder.RowBuilder()
                    .setTitle("Perform action in app.")
                    .setPrimaryAction(activityAction)
            ).build();
}

public SliceAction createActivityAction() {
    if (getContext() == null) {
        return null;
    }
    return SliceAction.create(
            PendingIntent.getActivity(
                    getContext(),
                    0,
                    new Intent(getContext(), MainActivity.class),
                    0
            ),
            IconCompat.createWithResource(getContext(), R.drawable.ic_home),
            ListBuilder.ICON_IMAGE,
            "Enter app"
    );
}
```

![](https://developer.android.com/static/guide/slices/images/slice-2-toast.png)

Slices also support other input types, such as toggles, that include state in the intent that is sent to the app.  

### Kotlin

```kotlin
fun createBrightnessSlice(sliceUri: Uri): Slice {
    val toggleAction =
        SliceAction.createToggle(
            createToggleIntent(),
            "Toggle adaptive brightness",
            true
        )
    return list(context, sliceUri, ListBuilder.INFINITY) {
        row {
            title = "Adaptive brightness"
            subtitle = "Optimizes brightness for available light"
            primaryAction = toggleAction
        }
        inputRange {
            inputAction = (brightnessPendingIntent)
            max = 100
            value = 45
        }
    }
}

fun createToggleIntent(): PendingIntent {
    val intent = Intent(context, MyBroadcastReceiver::class.java)
    return PendingIntent.getBroadcast(context, 0, intent, 0)
}
```

### Java

```java
public Slice createBrightnessSlice(Uri sliceUri) {
    if (getContext() == null) {
        return null;
    }
    SliceAction toggleAction = SliceAction.createToggle(
            createToggleIntent(),
            "Toggle adaptive brightness",
            true
    );
    ListBuilder listBuilder = new ListBuilder(getContext(), sliceUri, ListBuilder.INFINITY)
            .addRow(new ListBuilder.RowBuilder()
                    .setTitle("Adaptive brightness")
                    .setSubtitle("Optimizes brightness for available light.")
                    .setPrimaryAction(toggleAction)
            ).addInputRange(new ListBuilder.InputRangeBuilder()
                    .setInputAction(brightnessPendingIntent)
                    .setMax(100)
                    .setValue(45)
            );
    return listBuilder.build();
}

public PendingIntent createToggleIntent() {
    Intent intent = new Intent(getContext(), MyBroadcastReceiver.class);
    return PendingIntent.getBroadcast(getContext(), 0, intent, 0);
}
```

The receiver can then check the state that it receives:  

### Kotlin

```kotlin
class MyBroadcastReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.hasExtra(Slice.EXTRA_TOGGLE_STATE)) {
            Toast.makeText(context, "Toggled:  " + intent.getBooleanExtra(
                    Slice.EXTRA_TOGGLE_STATE, false),
                    Toast.LENGTH_LONG).show()
        }
    }

    companion object {
        const val EXTRA_MESSAGE = "message"
    }
}
```

### Java

```java
public class MyBroadcastReceiver extends BroadcastReceiver {

    public static String EXTRA_MESSAGE = "message";

    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.hasExtra(EXTRA_TOGGLE_STATE)) {
            Toast.makeText(context, "Toggled:  " + intent.getBooleanExtra(
                    EXTRA_TOGGLE_STATE, false),
                    Toast.LENGTH_LONG).show();
        }
    }
}
```

![](https://developer.android.com/static/guide/slices/images/slice-3-switch.png)

## Dynamic Slices

Slices can also contain dynamic content. In the following example, the Slice now includes the number of broadcasts received in its content:  

### Kotlin

```kotlin
fun createDynamicSlice(sliceUri: Uri): Slice {
    return when (sliceUri.path) {
        "/count" -> {
            val toastAndIncrementAction = SliceAction.create(
                createToastAndIncrementIntent("Item clicked."),
                actionIcon,
                ListBuilder.ICON_IMAGE,
                "Increment."
            )
            list(context, sliceUri, ListBuilder.INFINITY) {
                row {
                    primaryAction = toastAndIncrementAction
                    title = "Count: ${MyBroadcastReceiver.receivedCount}"
                    subtitle = "Click me"
                }
            }
        }

        else -> {
            list(context, sliceUri, ListBuilder.INFINITY) {
                row {
                    primaryAction = createActivityAction()
                    title = "URI not found."
                }
            }
        }
    }
}
```

### Java

```java
public Slice createDynamicSlice(Uri sliceUri) {
    if (getContext() == null || sliceUri.getPath() == null) {
        return null;
    }
    ListBuilder listBuilder = new ListBuilder(getContext(), sliceUri, ListBuilder.INFINITY);
    switch (sliceUri.getPath()) {
        case "/count":
            SliceAction toastAndIncrementAction = SliceAction.create(
                    createToastAndIncrementIntent("Item clicked."),
                    actionIcon,
                    ListBuilder.ICON_IMAGE,
                    "Increment."
            );
            listBuilder.addRow(
                    new ListBuilder.RowBuilder()
                            .setPrimaryAction(toastAndIncrementAction)
                            .setTitle("Count: " + MyBroadcastReceiver.sReceivedCount)
                            .setSubtitle("Click me")
            );
            break;
        default:
            listBuilder.addRow(
                    new ListBuilder.RowBuilder()
                            .setPrimaryAction(createActivityAction())
                            .setTitle("URI not found.")
            );
            break;
    }
    return listBuilder.build();
}

public PendingIntent createToastAndIncrementIntent(String s) {
    Intent intent = new Intent(getContext(), MyBroadcastReceiver.class)
            .putExtra(MyBroadcastReceiver.EXTRA_MESSAGE, s);
    return PendingIntent.getBroadcast(getContext(), 0, intent, 0);
}
```

In this example, while the count is shown, it doesn't update on its own. You can modify your broadcast receiver to notify the system that a change has occurred by using[`ContentResolver#notifyChange`](https://developer.android.com/reference/android/content/ContentResolver#notifychange).  

### Kotlin

```kotlin
class MyBroadcastReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.hasExtra(Slice.EXTRA_TOGGLE_STATE)) {
            Toast.makeText(
                context, "Toggled:  " + intent.getBooleanExtra(
                    Slice.EXTRA_TOGGLE_STATE, false
                ),
                Toast.LENGTH_LONG
            ).show()
            receivedCount++;
            context.contentResolver.notifyChange(sliceUri, null)
        }
    }

    companion object {
        var receivedCount = 0
        val sliceUri = Uri.parse("content://com.android.example.slicesample/count")
        const val EXTRA_MESSAGE = "message"
    }
}
```

### Java

```java
public class MyBroadcastReceiver extends BroadcastReceiver {

    public static int sReceivedCount = 0;
    public static String EXTRA_MESSAGE = "message";

    private static Uri sliceUri = Uri.parse("content://com.android.example.slicesample/count");

    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent.hasExtra(EXTRA_TOGGLE_STATE)) {
            Toast.makeText(context, "Toggled:  " + intent.getBooleanExtra(
                    EXTRA_TOGGLE_STATE, false),
                    Toast.LENGTH_LONG).show();
            sReceivedCount++;
            context.getContentResolver().notifyChange(sliceUri, null);
        }
    }
}
```

![](https://developer.android.com/static/guide/slices/images/slice-4-count.png)

## Templates

Slices support a variety of templates. For more details on template options and behaviors, see[Templates](https://developer.android.com/guide/slices/templates).