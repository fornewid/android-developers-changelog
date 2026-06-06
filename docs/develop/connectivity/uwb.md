---
title: https://developer.android.com/develop/connectivity/uwb
url: https://developer.android.com/develop/connectivity/uwb
source: md.txt
---

> [!NOTE]
> **Note:** UWB is currently only available using [Jetpack](https://developer.android.com/jetpack/androidx/releases/core-uwb).

[Video](https://www.youtube.com/watch?v=8X_9no-9tCg)

Ultra-wideband communication is a radio technology focused on precise ranging
(measuring the location to an accuracy of 10 cm) between devices.
This radio technology can use a low-energy density for short range measurements
and perform high-bandwidth signaling over a large portion of the radio spectrum.
UWB's bandwidth is greater than 500 MHz (or exceeding 20% fractional
bandwidth).

## Controller/Initiator vs. Controlee/Responder

UWB communication occurs between two devices, where one is a Controller, and the
other is a Controlee. The Controller determines the complex channel
([`UwbComplexChannel`](https://developer.android.com/reference/androidx/core/uwb/UwbComplexChannel)) that
the two devices will share and is the initiator, while the Controlee is the
responder.

A Controller can handle multiple Controlees, but a Controlee can only subscribe
to a single Controller. Both Controller/Initiator and Controlee/Responder
configurations are supported.

## Ranging parameters

The Controller and Controlee need to identify each other and communicate
ranging parameters to begin ranging. This exchange is left to applications to
implement using a secure out-of-band (OOB) mechanism of their choice, such as
[Bluetooth Low Energy](https://developer.android.com/develop/connectivity/bluetooth/ble-overview) (BLE).

The [ranging parameters](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingParameters)
include local address, complex channel, and session key, among others. Note
that these parameters may rotate or otherwise change after the ranging session
ends and need to be recommunicated to restart ranging.

## Background ranging

An app running in background can start a UWB ranging session if the device
supports it. To check your device capabilities, see [`RangingCapabilities`](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingCapabilities).

The app doesn't receive ranging reports when running in the background; the app
receives ranging reports when it moves to the foreground.

## STS configurations

The app or service provisions a session key for each session using a Scrambled
Timestamp Sequence (STS). Provisioned STS is more secure than a static STS
configuration. Provisioned STS is supported on all UWB-enabled devices running
Android 14 or higher.

| Threat category | Static STS | Provisoned STS |
|---|---|---|
| Air: Passive observer | Mitigated | Mitigated |
| Air: Signal amplification | Mitigated | Mitigated |
| Air: Replay/relay attack | Susceptible | Mitigated |

For provisioned STS:

1. Use the `uwbConfigType` in [`RangingParameters`](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingParameters) that supports provisioned STS.

2. Provide the 16-byte key in the [`sessionKeyInfo`](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingParameters#sessionKeyInfo()) field.

For static STS:

1. Use the `uwbConfigType` in [`RangingParameters`](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingParameters) that supports static STS.

2. Provide the 8-byte key in the [`sessionKeyInfo`](https://developer.android.com/reference/kotlin/androidx/core/uwb/RangingParameters#sessionKeyInfo()) field.

## Steps

To use the UWB API, follow these steps:

1. Ensure Android devices are running on Android 12 or higher and that they support UWB using `PackageManager#hasSystemFeature("android.hardware.uwb")`.
2. If ranging against IoT devices, ensure that they are FiRa MAC 1.3 compliant.
3. Discover UWB-capable peer devices using an OOB mechanism of your choice, such as [`BluetoothLeScanner`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner).
4. Exchange ranging parameters using a secure OOB mechanism of your choice, such as [`BluetoothGatt`](https://developer.android.com/reference/android/bluetooth/BluetoothGatt).
5. If the user wants to stop the session, cancel the scope of the session.

## Usage restrictions

The following restrictions apply to usage of the UWB API:

1. The app initiating new UWB ranging sessions must be a foreground app or service unless background ranging is supported as illustrated earlier.
2. When the app moves to background (while the session is ongoing), the app may no longer receive ranging reports. The UWB session will however continue to be maintained in the lower layers. When the app moves back to the foreground, the ranging reports will resume.

## Code samples

### Sample app

For an end-to-end example on how to use the [UWB Jetpack library](https://developer.android.com/jetpack/androidx/releases/core-uwb), check our [sample application on Github](https://github.com/android/connectivity-samples/tree/main/UwbRanging). This sample app covers validating UWB compatibility on an Android device, enabling the discovery process using an OOB mechanism, and setting up UWB ranging between two UWB-capable devices. The sample also covers device control and media sharing use cases.

### UWB Ranging

This code sample initiates and terminates UWB ranging for a Controlee:

    // The coroutineScope responsible for handling uwb ranging.
    // This will be initialized when startRanging is called.
    var job: Job?

    // A code snippet that initiates uwb ranging for a Controlee.
    suspend fun startRanging() {

        // Get the ranging parameter of a partnering Controller using an OOB mechanism of choice.
        val partnerAddress : Pair<UwbAddress, UwbComplexChannel> = listenForPartnersAddress()

        // Create the ranging parameters.
        val partnerParameters = RangingParameters(
            uwbConfigType = UwbRangingParameters.UWB_CONFIG_ID_1,
            // SessionKeyInfo is used to encrypt the ranging session.
            sessionKeyInfo = null,
            complexChannel = partnerAddress.second,
            peerDevices = listOf(UwbDevice.createForAddress(partnerAddress.first)),
            updateRateType = UwbRangingParameters.RANGING_UPDATE_RATE_AUTOMATIC
        )

        // Initiate a session that will be valid for a single ranging session.
        val clientSession = uwbManager.clientSessionScope()

        // Share the localAddress of the current session to the partner device.
        broadcastMyParameters(clientSession.localAddress)

        val sessionFlow = clientSession.prepareSession(partnerParameters)

        // Start a coroutine scope that initiates ranging.
        CoroutineScope(Dispatchers.Main.immediate).launch {
            sessionFlow.collect {
                when(it) {
                    is RangingResultPosition -> doSomethingWithPosition(it.position)
                    is RangingResultPeerDisconnected -> peerDisconnected(it)
                }
            }
        }
    }

    // A code snippet that cancels uwb ranging.
    fun cancelRanging() {

        // Canceling the CoroutineScope will stop the ranging.
        job?.let {
            it.cancel()
        }
    }

### RxJava3 support

Rxjava3 support is now available to help achieve interoperability with Java
clients. This library provides a way to get ranging results as an Observable or
Flowable stream, and to retrieve the UwbClientSessionScope as a Single object.

    private final UwbManager uwbManager;

    // Retrieve uwbManager.clientSessionScope as a Single object
    Single<UwbClientSessionScope> clientSessionScopeSingle =
                    UwbManagerRx.clientSessionScopeSingle(uwbManager);
    UwbClientSessionScope uwbClientSessionScope = clientSessionScopeSingle.blockingGet();

    // Retrieve uwbClientSessionScope.prepareSession Flow as an Observable object
    Observable<RangingResult> rangingResultObservable =
                    UwbClientSessionScopeRx.rangingResultsObservable(clientSessionScope,
                            rangingParameters);

    // Consume ranging results from Observable
    rangingResultObservable.subscribe(
       rangingResult -> doSomethingWithRangingResult(result), // onNext
       (error) -> doSomethingWithError(error), // onError
       () -> doSomethingOnResultEventsCompleted(), //onCompleted
    );
    // Unsubscribe
    rangingResultObservable.unsubscribe();
       

    // Retrieve uwbClientSessionScope.prepareSession Flow as a Flowable object
    Flowable<RangingResult> rangingResultFlowable =
                    UwbClientSessionScopeRx.rangingResultsFlowable(clientSessionScope,
                            rangingParameters);

    // Consume ranging results from Flowable using Disposable
    Disposable disposable = rangingResultFlowable
       .delay(1, TimeUnit.SECONDS)
       .subscribeWith(new DisposableSubscriber<RangingResult> () {
          @Override public void onStart() {
              request(1);
          }
          
          @Override public void onNext(RangingResult rangingResult) {
                 doSomethingWithRangingResult(rangingResult);
                 request(1);
          }


          @Override public void onError(Throwable t) {
                 t.printStackTrace();
          }


             @Override public void onComplete() {
                doSomethingOnEventsCompleted();
             }
       });

    // Stop subscription
    disposable.dispose();

## Ecosystem support

Here are the supported partner devices and third party SDKs.

### UWB-enabled mobile devices

As of January 2025, these devices support the Android UWB Jetpack library:

| Vendor | Device Model |
|---|---|
| Google | Pixel Pro (6 pro and newer), Fold, Tablet |
| Motorola | Edge 50 Ultra |
| Samsung | Galaxy Note 20, Galaxy Plus and Ultra (S21 and newer), Galaxy Z Fold (Fold2 and newer) |

*Note*: Background UWB ranging is supported on all devices except for the following:

- Pixel 6 Pro, Pixel 7 Pro, and Pixel Fold.
- Samsung phones with Android 13 or lower.
- Samsung Chinese phones with Android 14 or lower.

### Third party SDKs

As of April 2023, these partner solutions are compatible with the
[current Jetpack library](https://developer.android.com/jetpack/androidx/releases/core-uwb#1.0.0-alpha04).

- Estimote [UWB Development Kit](https://estimote.com/uwb-beacons).
- Mobile Knowledge [MK UWB Kit Mobile Edition 2.0](https://www.themobileknowledge.com/product/mk-uwb-kit-mobile-edition-2-0).

#### Known issue: byte order reversed for MAC address and static STS vendor ID fields

On Android 13 and lower, the Android UWB stack incorrectly reverses the byte
order for the following fields:

- Device MAC address
- Destination MAC address
- Static STS vendor ID

The byte order reversal occurs because the Android stack treats these fields
as values, not arrays. We're working with FiRa to update the UCI specification
([CR-1112](https://groups.firaconsortium.org/wg/Technical/mail/thread/9472#15571))
to explicitly state that these fields should be treated as arrays.

This issue will be fixed through the GMS Core update in the `2320XXXX` release.
To be compliant with Android devices from that point on, IOT vendors need to modify
your implementation to avoid reversing the byte ordering of these fields.