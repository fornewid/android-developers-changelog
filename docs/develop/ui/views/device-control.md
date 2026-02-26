---
title: https://developer.android.com/develop/ui/views/device-control
url: https://developer.android.com/develop/ui/views/device-control
source: md.txt
---

In Android 11 and later, the Quick Access Device Controls feature
lets the user quickly view and control external devices such as lights,
thermostats, and cameras from a user affordance within three interactions from a
default launcher. The device OEM chooses what launcher they use. Device
aggregators---for example, Google Home---and third-party vendor apps can
provide devices for display in this space. This page shows you how to surface
device controls in this space and link them to your control app.

> [!NOTE]
> **Note:** To leverage these features, your project's `minSdk` must be `30` or higher.

**Figure 1.** Device control space in the Android UI.

To add this support, create and declare a `ControlsProviderService`. Create the
controls your app supports based on predefined control types, and then create
publishers for these controls.

## User interface

Devices are displayed under **Device controls** as templated widgets. Five
device control widgets are available, as shown in the following figure:

|---|---|---|
| ![Toggle widget](https://developer.android.com/static/images/device-control/device-control-toggle.png) Toggle | ![Toggle with slider widget](https://developer.android.com/static/images/device-control/device-control-toggle-slider.png) Toggle with slider | ![Range widget](https://developer.android.com/static/images/device-control/device-control-range.png) Range (can't be toggled on or off) |
| ![Stateless toggle widget](https://developer.android.com/static/images/device-control/device-control-toggle-stateless.png) Stateless toggle | ![Temperature panel widget (closed)](https://developer.android.com/static/images/device-control/device-control-panel1.png) Temperature panel (closed) |

**Figure 2.** Collection of templated widgets.

Touching \& holding a widget takes you to the app for deeper control. You can
customize the icon and color on each widget, but for the best user experience,
use the default icon and color if the default set matches the device.
![An image showing the temperature panel widget (open)](https://developer.android.com/static/images/device-control/device-control-panel2.png) **Figure 3.** Open temperature panel widget open.

## Create the service

This section shows how to create the
[`ControlsProviderService`](https://developer.android.com/reference/android/service/controls/ControlsProviderService).
This service tells the Android system UI that your app contains device controls
that must be surfaced in the **Device controls** area of the Android UI.

The `ControlsProviderService` API assumes familiarity with reactive streams, as
defined in the [Reactive Streams GitHub
project](https://github.com/reactive-streams/reactive-streams-jvm/blob/v1.0.3/README.md)
and implemented in the [Java 9 Flow
interfaces](https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/Flow.html).
The API is built around the following concepts:

- **Publisher:** your application is the publisher.
- **Subscriber:** the system UI is the subscriber and it can request a number of controls from the publisher.
- **Subscription:** the timeframe during which the publisher can send updates to the System UI. Either the publisher or the subscriber can close this window.

### Declare the service

Your app must declare a service---such as `MyCustomControlService`---in
its app manifest.

The service must include an intent filter for `ControlsProviderService`. This
filter lets applications contribute controls to the system UI.

You also need a `label` that is displayed in the controls in the system UI.

The following example shows how to declare a service:

    <service
        android:name="MyCustomControlService"
        android:label="My Custom Controls"
        android:permission="android.permission.BIND_CONTROLS"
        android:exported="true"
        >
        <intent-filter>
          <action android:name="android.service.controls.ControlsProviderService" />
        </intent-filter>
    </service>

Next, create a new Kotlin file named `MyCustomControlService.kt` and make it
extend `ControlsProviderService()`:

### Kotlin

```kotlin
    class MyCustomControlService : ControlsProviderService() {
        ...
    }
    
```

### Java

```java
    public class MyCustomJavaControlService extends ControlsProviderService {
        ...
    }
    
```

### Select the correct control type

The API provides builder methods to create the controls. To populate the
builder, determine the device you want to control and how the user interacts
with it. Perform the following steps:

1. Pick the type of device the control represents. The [`DeviceTypes`](https://developer.android.com/reference/android/service/controls/DeviceTypes) class is an enumeration of all supported devices. The type is used to determine the icons and colors for the device in the UI.
2. Determine the user-facing name, device location---for example, kitchen---and other UI textual elements associated with the control.
3. Pick the best template to support user interaction. Controls are assigned a [`ControlTemplate`](https://developer.android.com/reference/android/service/controls/templates/ControlTemplate) from the application. This template directly shows the control state to the user as well as the available input methods---that is, the [`ControlAction`](https://developer.android.com/reference/android/service/controls/actions/ControlAction). The following table outlines some of the available templates and the actions they support:

|---|---|---|
| **Template** | **Action** | **Description** |
| `https://developer.android.com/reference/android/service/controls/templates/ControlTemplate#getNoTemplateObject()` | `None` | The application might use this to convey information about the control, but the user can't interact with it. |
| `https://developer.android.com/reference/android/service/controls/templates/ToggleTemplate` | `https://developer.android.com/reference/android/service/controls/actions/BooleanAction` | Represents a control that can be switched between enabled and disabled states. The `BooleanAction` object contains a field that changes to represent the requested new state when the user taps the control. |
| `https://developer.android.com/reference/android/service/controls/templates/RangeTemplate` | `https://developer.android.com/reference/android/service/controls/actions/FloatAction` | Represents a slider widget with specified min, max, and step values. When the user interacts with the slider, send a new `FloatAction` object back to the application with the updated value. |
| `https://developer.android.com/reference/android/service/controls/templates/ToggleRangeTemplate` | `https://developer.android.com/reference/android/service/controls/actions/BooleanAction, https://developer.android.com/reference/android/service/controls/actions/FloatAction` | This template is a combination of the `ToggleTemplate` and `RangeTemplate`. It supports touch events as well as a slider, such as to control dimmable lights. |
| `https://developer.android.com/reference/android/service/controls/templates/TemperatureControlTemplate` | `https://developer.android.com/reference/android/service/controls/actions/ModeAction, https://developer.android.com/reference/android/service/controls/actions/BooleanAction, https://developer.android.com/reference/android/service/controls/actions/FloatAction` | In addition to encapsulating the preceding actions, this template lets the user set a mode, such as heat, cool, heat/cool, eco, or off. |
| `https://developer.android.com/reference/android/service/controls/templates/StatelessTemplate` | `https://developer.android.com/reference/android/service/controls/actions/CommandAction` | Used to indicate a control that provides touch capability but whose state can't be determined, such as an IR television remote. You can use this template to define a routine or macro, which is an aggregation of control and state changes. |

With this information, you can create the control:

- Use the [`Control.StatelessBuilder`](https://developer.android.com/reference/android/service/controls/Control.StatelessBuilder) builder class when the state of the control is unknown.
- Use the [`Control.StatefulBuilder`](https://developer.android.com/reference/android/service/controls/Control.StatefulBuilder) builder class when the state of the control is known.

For example, to control a smart light bulb and a thermostat, add the following
constants to your `MyCustomControlService`:

### Kotlin

```kotlin
    private const val LIGHT_ID = 1234
    private const val LIGHT_TITLE = "My fancy light"
    private const val LIGHT_TYPE = DeviceTypes.TYPE_LIGHT
    private const val THERMOSTAT_ID = 5678
    private const val THERMOSTAT_TITLE = "My fancy thermostat"
    private const val THERMOSTAT_TYPE = DeviceTypes.TYPE_THERMOSTAT
 
    class MyCustomControlService : ControlsProviderService() {
      ...
    }
    
```

### Java

```java
    public class MyCustomJavaControlService extends ControlsProviderService {
 
    private final int LIGHT_ID = 1337;
    private final String LIGHT_TITLE = "My fancy light";
    private final int LIGHT_TYPE = DeviceTypes.TYPE_LIGHT;
    private final int THERMOSTAT_ID = 1338;
    private final String THERMOSTAT_TITLE = "My fancy thermostat";
    private final int THERMOSTAT_TYPE = DeviceTypes.TYPE_THERMOSTAT;
 
    ...
    }
    
```

### Create publishers for the controls

After you create the control, it needs a publisher. The publisher informs the
system UI of the existence of the control. The `ControlsProviderService` class
has two publisher methods that you must override in your application code:

- `createPublisherForAllAvailable()`: creates a [`Publisher`](https://github.com/reactive-streams/reactive-streams-jvm/blob/v1.0.3/api/src/main/java/org/reactivestreams/Publisher.java) for all the controls available in your app. Use `Control.StatelessBuilder()` to build `Control` objects for this publisher.
- `createPublisherFor()`: creates a `Publisher` for a list of given controls, as identified by their string identifiers. Use `Control.StatefulBuilder` to build these `Control` objects, since the publisher must assign a state to each control.

#### Create the publisher

When your app first publishes controls to the system UI, the app doesn't know
the state of each control. Getting the state can be a time-consuming operation
involving many hops in the device-provider's network. Use the
[`createPublisherForAllAvailable()`](https://developer.android.com/reference/android/service/controls/ControlsProviderService#createPublisherForAllAvailable())
method to advertise the available controls to the system. This method uses the
`Control.StatelessBuilder` builder class, since the state of each control is
unknown.

Once the controls appear in the Android UI , the user can select favorite
controls.

To use Kotlin coroutines to create a `ControlsProviderService`, add a new
dependency to your `build.gradle`:

### Groovy

```groovy
dependencies {
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-jdk9:1.6.4"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-jdk9:1.6.4")
}
```

Once you sync your Gradle files, add the following snippet to your `Service` to
implement `createPublisherForAllAvailable()`:

### Kotlin

```kotlin
    class MyCustomControlService : ControlsProviderService() {
 
      override fun createPublisherForAllAvailable(): Flow.Publisher =
          flowPublish {
              send(createStatelessControl(LIGHT_ID, LIGHT_TITLE, LIGHT_TYPE))
              send(createStatelessControl(THERMOSTAT_ID, THERMOSTAT_TITLE, THERMOSTAT_TYPE))
          }
 
      private fun createStatelessControl(id: Int, title: String, type: Int): Control {
          val intent = Intent(this, MainActivity::class.java)
              .putExtra(EXTRA_MESSAGE, title)
              .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
          val action = PendingIntent.getActivity(
              this,
              id,
              intent,
              PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
          )
 
          return Control.StatelessBuilder(id.toString(), action)
              .setTitle(title)
              .setDeviceType(type)
              .build()
      }
 
          override fun createPublisherFor(controlIds: List): Flow.Publisher {
           TODO()
        }
 
        override fun performControlAction(
            controlId: String,
            action: ControlAction,
            consumer: Consumer
        ) {
            TODO()
        }
    }
    
```

### Java

```java
    public class MyCustomJavaControlService extends ControlsProviderService {
 
        private final int LIGHT_ID = 1337;
        private final String LIGHT_TITLE = "My fancy light";
        private final int LIGHT_TYPE = DeviceTypes.TYPE_LIGHT;
        private final int THERMOSTAT_ID = 1338;
        private final String THERMOSTAT_TITLE = "My fancy thermostat";
        private final int THERMOSTAT_TYPE = DeviceTypes.TYPE_THERMOSTAT;
 
        private boolean toggleState = false;
        private float rangeState = 18f;
        private final Map<String, ReplayProcessor> controlFlows = new HashMap<>();
 
        @NonNull
        @Override
        public Flow.Publisher createPublisherForAllAvailable() {
            List controls = new ArrayList<>();
            controls.add(createStatelessControl(LIGHT_ID, LIGHT_TITLE, LIGHT_TYPE));
            controls.add(createStatelessControl(THERMOSTAT_ID, THERMOSTAT_TITLE, THERMOSTAT_TYPE));
            return FlowAdapters.toFlowPublisher(Flowable.fromIterable(controls));
        }
 
        @NonNull
        @Override
        public Flow.Publisher createPublisherFor(@NonNull List controlIds) {
            ReplayProcessor updatePublisher = ReplayProcessor.create();
 
            controlIds.forEach(control -> {
                controlFlows.put(control, updatePublisher);
                updatePublisher.onNext(createLight());
                updatePublisher.onNext(createThermostat());
            });
 
            return FlowAdapters.toFlowPublisher(updatePublisher);
        }
    }
    
```

Swipe down the system menu and locate the **Device controls** button, shown in
figure 4:
![An image showing the system ui for device controls](https://developer.android.com/static/images/ui/device_controls_ui.png) **Figure 4.** Device controls in the system menu.

Tapping **Device controls** navigates to a second screen where you can select
your app. Once you select your app, you see how the previous snippet creates a
custom system menu showing your new controls, as shown in figure 5:
![An image showing the system menu containing a light and thermostat control](https://developer.android.com/static/images/ui/device_controls_example_1.png) **Figure 5.** Light and thermostat controls to add.

Now, implement the `createPublisherFor()` method, adding the following to your
`Service`:

### Kotlin

```kotlin
    private val job = SupervisorJob()
    private val scope = CoroutineScope(Dispatchers.IO + job)
    private val controlFlows = mutableMapOf<String, MutableSharedFlow>()
 
    private var toggleState = false
    private var rangeState = 18f
 
    override fun createPublisherFor(controlIds: List): Flow.Publisher {
        val flow = MutableSharedFlow(replay = 2, extraBufferCapacity = 2)
 
        controlIds.forEach { controlFlows[it] = flow }
 
        scope.launch {
            delay(1000) // Retrieving the toggle state.
            flow.tryEmit(createLight())
 
            delay(1000) // Retrieving the range state.
            flow.tryEmit(createThermostat())
 
        }
        return flow.asPublisher()
    }
 
    private fun createLight() = createStatefulControl(
        LIGHT_ID,
        LIGHT_TITLE,
        LIGHT_TYPE,
        toggleState,
        ToggleTemplate(
            LIGHT_ID.toString(),
            ControlButton(
                toggleState,
                toggleState.toString().uppercase(Locale.getDefault())
            )
        )
    )
 
    private fun createThermostat() = createStatefulControl(
        THERMOSTAT_ID,
        THERMOSTAT_TITLE,
        THERMOSTAT_TYPE,
        rangeState,
        RangeTemplate(
            THERMOSTAT_ID.toString(),
            15f,
            25f,
            rangeState,
            0.1f,
            "%1.1f"
        )
    )
 
    private fun  createStatefulControl(id: Int, title: String, type: Int, state: T, template: ControlTemplate): Control {
        val intent = Intent(this, MainActivity::class.java)
            .putExtra(EXTRA_MESSAGE, "$title $state")
            .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        val action = PendingIntent.getActivity(
            this,
            id,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )
 
        return Control.StatefulBuilder(id.toString(), action)
            .setTitle(title)
            .setDeviceType(type)
            .setStatus(Control.STATUS_OK)
            .setControlTemplate(template)
            .build()
    }
 
    override fun onDestroy() {
        super.onDestroy()
        job.cancel()
    }
 
    
```

### Java

```java
    @NonNull
    @Override
    public Flow.Publisher createPublisherFor(@NonNull List controlIds) {
        ReplayProcessor updatePublisher = ReplayProcessor.create();
 
        controlIds.forEach(control -> {
            controlFlows.put(control, updatePublisher);
            updatePublisher.onNext(createLight());
            updatePublisher.onNext(createThermostat());
        });
 
        return FlowAdapters.toFlowPublisher(updatePublisher);
    }
 
    private Control createStatelessControl(int id, String title, int type) {
        Intent intent = new Intent(this, MainActivity.class)
                .putExtra(EXTRA_MESSAGE, title)
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        PendingIntent action = PendingIntent.getActivity(
                this,
                id,
                intent,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
        );
 
        return new Control.StatelessBuilder(id + "", action)
                .setTitle(title)
                .setDeviceType(type)
                .build();
    }
 
    private Control createLight() {
        return createStatefulControl(
                LIGHT_ID,
                LIGHT_TITLE,
                LIGHT_TYPE,
                toggleState,
                new ToggleTemplate(
                        LIGHT_ID + "",
                        new ControlButton(
                                toggleState,
                                String.valueOf(toggleState).toUpperCase(Locale.getDefault())
                        )
                )
        );
    }
 
    private Control createThermostat() {
        return createStatefulControl(
                THERMOSTAT_ID,
                THERMOSTAT_TITLE,
                THERMOSTAT_TYPE,
                rangeState,
                new RangeTemplate(
                        THERMOSTAT_ID + "",
                        15f,
                        25f,
                        rangeState,
                        0.1f,
                        "%1.1f"
                )
        );
    }
 
    private  Control createStatefulControl(int id, String title, int type, T state, ControlTemplate template) {
        Intent intent = new Intent(this, MainActivity.class)
                .putExtra(EXTRA_MESSAGE, "$title $state")
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        PendingIntent action = PendingIntent.getActivity(
                this,
                id,
                intent,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_IMMUTABLE
        );
 
        return new Control.StatefulBuilder(id + "", action)
                .setTitle(title)
                .setDeviceType(type)
                .setStatus(Control.STATUS_OK)
                .setControlTemplate(template)
                .build();
    }
    
```

In this example, the `createPublisherFor()` method contains a fake
implementation of what your app must do: communicate with your device to
retrieve its status, and emit that status to the system.

The `createPublisherFor()` method uses Kotlin coroutines and flows to satisfy
the required Reactive Streams API by doing the following:

1. Creates a `Flow`.
2. Waits for one second.
3. Creates and emits the state of the smart light.
4. Waits for another second.
5. Creates and emits the state of the thermostat.

### Handle actions

The `performControlAction()` method signals when the user interacts with a
published control. The type of `ControlAction` sent determines the action.
Perform the appropriate action for the given control and then update the state
of the device in the Android UI.

To complete the example, add the following to your `Service`:

### Kotlin

```kotlin
    override fun performControlAction(
        controlId: String,
        action: ControlAction,
        consumer: Consumer
    ) {
        controlFlows[controlId]?.let { flow ->
            when (controlId) {
                LIGHT_ID.toString() -> {
                    consumer.accept(ControlAction.RESPONSE_OK)
                    if (action is BooleanAction) toggleState = action.newState
                    flow.tryEmit(createLight())
                }
                THERMOSTAT_ID.toString() -> {
                    consumer.accept(ControlAction.RESPONSE_OK)
                    if (action is FloatAction) rangeState = action.newValue
                    flow.tryEmit(createThermostat())
                }
                else -> consumer.accept(ControlAction.RESPONSE_FAIL)
            }
        } ?: consumer.accept(ControlAction.RESPONSE_FAIL)
    }
    
```

### Java

```java
    @Override
    public void performControlAction(@NonNull String controlId, @NonNull ControlAction action, @NonNull Consumer consumer) {
        ReplayProcessor processor = controlFlows.get(controlId);
        if (processor == null) return;
 
        if (controlId.equals(LIGHT_ID + "")) {
            consumer.accept(ControlAction.RESPONSE_OK);
            if (action instanceof BooleanAction) toggleState = ((BooleanAction) action).getNewState();
            processor.onNext(createLight());
        }
        if (controlId.equals(THERMOSTAT_ID + "")) {
            consumer.accept(ControlAction.RESPONSE_OK);
            if (action instanceof FloatAction) rangeState = ((FloatAction) action).getNewValue()
            processor.onNext(createThermostat());
        }
    }
    
```

Run the app, access the **Device controls** menu, and see your light and
thermostat controls.
![An image showing a light and thermostat control](https://developer.android.com/static/images/ui/device_controls_example_2.png) **Figure 6.** Light and thermostat controls.