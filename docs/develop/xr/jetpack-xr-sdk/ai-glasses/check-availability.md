---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-availability
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-availability
source: md.txt
---

As a user goes through their day, their AI glasses might lose their connection
to the host device (such as the user's phone) or their glasses might be
temporarily unavailable if they take their glasses off. To account for these
kinds of changes in device availability, your app can use the XR Device
Availability API, which consolidates device availability signals into the
standard Android [`Lifecycle.State`](https://developer.android.com/reference/kotlin/androidx/lifecycle/Lifecycle.State) values. Use this API to help manage
audio routing, hotword activation, and to know when to expect user input based
on when the AI glasses are available.

## Understand lifecycle states

The following table lists how device availability signals map to the
`Lifecycle.State` values.

| Lifecycle state | Device status | Description |
|---|---|---|
| `INITIALIZED` | Created | The lifecycle object is created but not yet observed. |
| `CREATED` | Inactive | The service is connected, but the user is not wearing the device. |
| `STARTED` | Active | The user is wearing the device. |
| `DESTROYED` | Disconnected | The device is disconnected or the service connection is lost. |

## Check and monitor device availability

To check and monitor a device's availability, you'll use a projected context
together with the lifecycle state to determine how your app should handle each
case:


```kotlin
    val xrDevice = XrDevice.getCurrentDevice(projectedContext)

    xrDevice.getLifecycle().currentStateFlow
        .takeWhile { it != Lifecycle.State.DESTROYED }
        .collect { state ->
            when (state) {
                Lifecycle.State.STARTED -> { /* Device is ACTIVE (worn) */ }
                Lifecycle.State.CREATED -> { /* Device is INACTIVE (not worn) */ }
                else -> { /* Handle other states */ }
            }
        }
}
```

<br />

### Key points about the code

- **Check for a connection** : Before accessing the device lifecycle, call [`ProjectedContext.isProjectedDeviceConnected`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedContext#isProjectedDeviceConnected(android.content.Context,kotlin.coroutines.CoroutineContext)) to verify that the projected device is connected to the host device.
- **Obtain a `ProjectedContext`** : Only call [`ProjectedContext.createProjectedDeviceContext`](https://developer.android.com/reference/kotlin/androidx/xr/projected/ProjectedContext#createProjectedDeviceContext(android.content.Context)) after verifying the connection, and make sure you pass this context into your [`XrDevice`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice) instance.
- **Handle context invalidation** : A new `deviceId` is generated every time a projected device connects. Once the state reaches `DESTROYED`, the current `ProjectedContext` is invalid. Stop using it immediately, and wait for a new connection.
- **Optimize battery and resources** : Gracefully handle app functionality based on the lifecycle state to preserve system resources and reduce battery consumption. For example, you should stop projecting UI content to the AI glasses when the state changes to `CREATED`.