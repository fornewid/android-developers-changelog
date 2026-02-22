---
title: https://developer.android.com/develop/connectivity/telecom/voip-app/telecom
url: https://developer.android.com/develop/connectivity/telecom/voip-app/telecom
source: md.txt
---

The `Core-Telecom` library streamlines the process of integrating your calling
application with the Android platform by providing a robust and consistent set
of APIs

If you want to explore practical implementations, you can find sample
applications on GitHub:

- [Lightweight Sample App](https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom) --- A minimal example demonstrating `Core-Telecom` API usage. Ideal for quickly understanding fundamental concepts.
- [Comprehensive Sample App (Developed by the Core-Telecom
  Team)](https://github.com/androidx/androidx/tree/androidx-main/core/core-telecom/integration-tests/referenceapp/src/main/java/androidx/core/telecom/reference) --- A more feature-rich application showcasing advanced Telecom functionalities and best practices. This is a great resource for understanding complex integration scenarios.

## Set up Core-Telecom

Add the `androidx.core:core-telecom` dependency to your app's `build.gradle`
file:  

    dependencies {
        implementation ("androidx.core:core-telecom:1.0.0")
    }

Declare the `MANAGE_OWN_CALLS` permission in your `AndroidManifest.xml`:  

    <uses-permission android:name="android.permission.MANAGE_OWN_CALLS" />

## Register your app

Register your calling app with Android using `CallsManager` to begin adding
calls to the system. When registering, specify your app's capabilities (for
example, audio, video support):  

    val callsManager = CallsManager(context)

    val capabilities: @CallsManager.Companion.Capability Int =
        (CallsManager.CAPABILITY_BASELINE or
              CallsManager.CAPABILITY_SUPPORTS_VIDEO_CALLING)

    callsManager.registerAppWithTelecom(capabilities)

## Call Management

Use Core-Telecom APIs to create and manage a call lifecycle.

### Create a call

The `CallAttributesCompat` object defines the properties of a unique call,
which can have the following characteristics:

- `displayName`: caller name.
- `address`: Call address (for example, phone number, meeting link).
- `direction`: Incoming or outgoing.
- `callType`: Audio or video.
- `callCapabilities`: Supports transfer and hold.

Here's an example of how to create an incoming call:  

    fun createIncomingCallAttributes(
        callerName: String,
        callerNumber: String,
        isVideoCall: Boolean): CallAttributesCompat {
        val addressUri = Uri.parse("YourAppScheme:$callerNumber")

        // Define capabilities supported by your call.
        val callCapabilities = CallAttributesCompat.CallCapability(
            supportsSetInactive = CallAttributesCompat.SUPPORTS_SET_INACTIVE // Call can be made inactive (implies hold)
        )

        return CallAttributesCompat(
            displayName = callerName,
            address = addressUri,
            direction = CallAttributesCompat.DIRECTION_INCOMING,
            callType = if (isVideoCall) CallAttributesCompat.CALL_TYPE_VIDEO_CALL else CallAttributesCompat.CALL_TYPE_AUDIO_CALL,
            callCapabilitiesCompat = callCapabilities
        )
    }

### Add a call

Use `callsManager.addCall` with `CallAttributesCompat` and callbacks to add a
new call to the system and manage remote surface updates. The `callControlScope`
within the `addCall` block primarily allows your app to transition the call
state and receive audio updates:  

    try {
        callsManager.addCall(
            INCOMING_CALL_ATTRIBUTES,
            onAnswerCall, // Watch needs to know if it can answer the call.
            onSetCallDisconnected,
            onSetCallActive,
            onSetCallInactive
        ) {
            // The call was successfully added once this scope runs.
            callControlScope = this
        }
    }
    catch(addCallException: Exception){
       // Handle the addCall failure.
    }

| **Note:** Once you add a call and the `CallControlScope` block is run, this does not mean your call is active, but rather that the platform is able to add a call and your call is now either `DIALING` or `RINGING`.

### Answer a call

Answer an incoming call within the `CallControlScope`:  

    when (val result = answer(CallAttributesCompat.CALL_TYPE_AUDIO_CALL)) {
        is CallControlResult.Success -> { /* Call answered */ }
        is CallControlResult.Error -> { /* Handle error */ }
    }

### Reject a call

Reject a call using `disconnect()` with `DisconnectCause.REJECTED` within the
`CallControlScope`:  

    disconnect(DisconnectCause(DisconnectCause.REJECTED))

### Make an outgoing call active

Set an outgoing call to active once the remote party answers:  

    when (val result = setActive()) {
        is CallControlResult.Success -> { /* Call active */ }
        is CallControlResult.Error -> { /* Handle error */ }
    }

### Place a call on hold

Use `setInactive()` to put a call on hold:  

    when (val result = setInactive()) {
        is CallControlResult.Success -> { /* Call on hold */ }
        is CallControlResult.Error -> { /* Handle error */ }
    }

### Disconnect a call

Disconnect a call using `disconnect()` with a `DisconnectCause`:  

    disconnect(DisconnectCause(DisconnectCause.LOCAL))

## Manage call audio endpoints

Observe and manage audio endpoints using `currentCallEndpoint`,
`availableEndpoints`, and `isMuted` `Flow`s within the `CallControlScope`  

    fun observeAudioStateChanges(callControlScope: CallControlScope) {
        with(callControlScope) {
            launch { currentCallEndpoint.collect { /* Update UI */ } }
            launch { availableEndpoints.collect { /* Update UI */ } }
            launch { isMuted.collect { /* Handle mute state */ } }
        }
    }

Change the active audio device using `requestEndpointChange()`:  

    coroutineScope.launch {
         callControlScope.requestEndpointChange(callEndpoint)
    }

| **Note:** Ensure media stream uses [AudioManager.STREAM_VOICE_CALL](https://developer.android.com/reference/android/media/AudioManager#STREAM_VOICE_CALL).

## Foreground support

The library uses `ConnectionService` (Android 13 API level 33 and lower) or
[foregroundtypes](https://developer.android.com/about/versions/14/changes/fgs-types-required) (Android 14 API level 34 and higher) for foreground
support.

As part of the foreground requirements, the application must post a notification
for users to know that the application is running in the foreground.

To ensure that your app gets foreground execution priority, create a
notification once you add the call with the platform. Foreground priority is
removed when your app terminates the call or your notification is no longer
valid.
| **Note:** You are required to post a notification within 5 seconds of adding the call to the platform.

[Learn more about foreground services](https://developer.android.com/guide/components/foreground-services).

## Remote Surface support

Remote devices (smartwatches, Bluetooth headsets, Android Auto) are capable of
call management without direct phone interaction. Your app must implement
callback lambdas (`onAnswerCall`, `onSetCallDisconnected`, `onSetCallActive`,
`onSetCallInactive`) provided to `CallsManager.addCall` to handle actions
initiated by these devices.

When a remote action occurs, the corresponding lambda is invoked.
| **Warning:** Your app must execute the requested action within a 5-second timeout. Failure to do so (either by not returning or by throwing an exception) is considered a transaction failure and may tear down the call session.

Successful completion of the lambda signals that the command was processed. If
the command cannot be obeyed, the lambda should throw an exception.

Proper implementation ensures seamless call control across different devices.
Test thoroughly with various remote surfaces.

### Call Extensions

| **Note:** This feature is still experimental while we work on supporting new extensions. Use `@OptIn(ExperimentalAppActions::class)` to opt-in to supporting call extensions and use the [issue tracker](https://issuetracker.google.com/issues/new?component=1356313&template=1817517) to file bugs or request support for new call extensions.

In addition to managing the call state and audio route of your calls, the
library also supports call extensions, which are optional features that your app
can implement for a richer calling experience on remote surfaces, such as
Android Auto. These features include meeting rooms, call silence, and additional
call icons. When your app implements an extension, information that the app
provides will be synchronized with all of the connected devices that also
support displaying these extensions in their UI. This means that these features
will be also be available on remote devices for users to interact with.

#### Create a Call with Extensions

When creating a call, instead of using `CallManager#addCall` to create the call,
you can instead use [CallManager#addCallWithExtensions](https://developer.android.com/reference/kotlin/androidx/core/telecom/extensions/CallsManagerExtensions#addCallWithExtensions(androidx.core.telecom.CallAttributesCompat,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction1,kotlin.coroutines.SuspendFunction0,kotlin.coroutines.SuspendFunction0,kotlin.coroutines.SuspendFunction1)), which gives the
app access to a different scope called `ExtensionInitializationScope`. This
scope allows the application to initialize the set of optional extensions that
it supports. Additionally, this scope provides an extra method, `onCall`,
which provides a `CallControlScope` back to the app after extension capability
exchange and initialization completes.  

    scope.launch {
        mCallsManager.addCallWithExtensions(
            attributes,
            onAnswer,
            onDisconnect,
            onSetActive,
            onSetInactive
        ) {
            // Initialize extension-specific code...

            // After the call has been initialized, perform in-call actions
            onCall {
                // Example: process call state updates
                callStateFlow.onEach { newState ->
                    // handle call state updates and notify telecom
                }.launchIn(this)

                // Use initialized extensions...
            }
        }
    }

#### Support Call Participants

If your app supports call participants for meetings or group calls, use
`addParticipantExtension` to declare support for this extension and
use the related APIs to update remote surfaces when the participants change.  

    mCallsManager.addCallWithExtensions(...) {
            // Initialize extensions...

            // Notifies Jetpack that this app supports the participant
            // extension and provides the initial participants state in the call.
            val participantExtension = addParticipantExtension(
                initialParticipants,
                initialActiveParticipant
            )

            // After the call has been initialized, perform in-call control actions
            onCall {
                // other in-call control and extension actions...

                // Example: update remote surfaces when the call participants change
                participantsFlow.onEach { newParticipants ->
                    participantExtension.updateParticipants(newParticipants)
                }.launchIn(this)
            }
        }

Along with notifying remote surfaces of what participants are in the call,
the active participant can also be updated using
`ParticipantExtension#updateActiveParticipant`.

There's also support for optional actions related to the call participants.
The app can use `ParticipantExtension#addRaiseHandSupport` to support the
notion of participants raising their hand in the call and see which other
participants also have their hands raised.  

    mCallsManager.addCallWithExtensions(...) {
            // Initialize extensions...

            // Notifies Jetpack that this app supports the participant
            // extension and provides the initial list of participants in the call.
            val participantExtension = addParticipantExtension(initialParticipants)
            // Notifies Jetpack that this app supports the notion of participants
            // being able to raise and lower their hands.
            val raiseHandState = participantExtension.addRaiseHandSupport(
                    initialRaisedHands
                ) { onHandRaisedStateChanged ->
                    // handle this user's raised hand state changed updates from
                    // remote surfaces.
                }

            // After the call has been initialized, perform in-call control actions
            onCall {
                // other in-call control and extension actions...

                // Example: update remote surfaces when the call participants change
                participantsFlow.onEach { newParticipants ->
                    participantExtension.updateParticipants(newParticipants)
                }.launchIn(this)
                // notify remote surfaces of which of the participants have their
                // hands raised
                raisedHandsFlow.onEach { newRaisedHands ->
                    raiseHandState.updateRaisedHands(newRaisedHands)
                }.launchIn(this)
            }
        }

#### Support Call Silence

Call silence allows a user to request that the app silence a call's outgoing
audio without physically muting the device's microphone. This feature is
managed per call, so Jetpack handles the complexity of managing the global mute
state of ongoing cellular calls while a VOIP call is active. This makes
silencing outgoing audio less error prone in multi-call scenarios while also
allowing for helpful features such as "are you speaking" indications when the
user is speaking while not realizing that call silence is enabled.  

    mCallsManager.addCallWithExtensions(...) {
            // Initialize extensions...

            // Add support for locally silencing the call's outgoing audio and
            // register a handler for when the user changes the call silence state
            // from a remote surface.
            val callSilenceExtension = addLocalCallSilenceExtension(
                initialCallSilenceState = false
            ) { newCallSilenceStateRequest ->
                // handle the user's request to enable/disable call silence from
                // a remote surface
            }

            // After the call has been initialized, perform in-call control actions
            onCall {
                // other in-call control and extension actions...

                // When the call's call silence state changes, update remote
                // surfaces of the new state.
                callSilenceState.onEach { isSilenced ->
                    callSilenceExtension.updateIsLocallySilenced(isSilenced)
                }.launchIn(this)
            }
        }

#### Support Call Icons

A call icon allows the app to specify a custom icon representing the call to be
displayed on remote surfaces during the call. This icon can also be updated over
the lifetime of the call.
**Note:** Content URIs are not accessible to other apps unless an app explicitly grants another app permission to use that URI. Use a `FileProvider` to generate the `content://` URIs that are shared with remote surfaces. See the [`CallIconExtension`](https://developer.android.com/reference/kotlin/androidx/core/telecom/extensions/CallIconExtension) docs for more details on how to set up call icon support for remote surfaces in your app.  

    mCallsManager.addCallWithExtensions(...) {
            // Initialize extensions...

            // Add support for a custom call icon to be displayed during the
            // lifetime of the call.
            val callIconExtension = addCallIconExtension(
                initialCallIconUri = initialUri
            )

            // After the call has been initialized, perform in-call control actions
            onCall {
                // other in-call control and extension actions...

                // When the call's icon changes, update remote surfaces by providing
                // the new URI.
                callIconUri.onEach { newIconUri ->
                    callIconExtension.updateCallIconUri(newIconUri)
                }.launchIn(this)
            }
        }