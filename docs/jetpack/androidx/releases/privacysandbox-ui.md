---
title: https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui
url: https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui
source: md.txt
---

# Privacysandbox UI

# privacysandbox ui

API Reference  
[androidx.privacysandbox.ui](https://developer.android.com/reference/kotlin/androidx/privacysandbox/ui/package-summary)  
TODO  

| Latest Update | Stable Release | Release Candidate | Beta Release |                                              Alpha Release                                               |
|---------------|----------------|-------------------|--------------|----------------------------------------------------------------------------------------------------------|
| May 20, 2025  | -              | -                 | -            | [1.0.0-alpha16](https://developer.android.com/jetpack/androidx/releases/privacysandbox-ui#1.0.0-alpha16) |

## Declaring dependencies

To add a dependency on privacysandbox-ui, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    // Use to implement privacysandbox ui-client
    implementation "androidx.privacysandbox.ui:ui-client:1.0.0-alpha16"

    // Use to implement privacysandbox ui-core
    implementation "androidx.privacysandbox.ui:ui-core:1.0.0-alpha16"

    // Use to implement privacysandbox ui-core
    implementation "androidx.privacysandbox.ui:ui-provider:1.0.0-alpha16"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to implement privacysandbox ui-client
    implementation("androidx.privacysandbox.ui:ui-client:1.0.0-alpha16")

    // Use to implement privacysandbox ui-core
    implementation("androidx.privacysandbox.ui:ui-core:1.0.0-alpha16")

    // Use to implement privacysandbox ui-provider
    implementation("androidx.privacysandbox.ui:ui-provider:1.0.0-alpha16")

    
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1331007+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1331007&template=1797065)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0-alpha16

May 20, 2025

`androidx.privacysandbox.ui:ui-*:1.0.0-alpha16`is released. Version 1.0.0-alpha16 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..cd41781824511ce4d5c4a05d2df4aaaee669f0bc/privacysandbox/ui).

**New Features**

- Added logic to measure obstructions on`SandboxedSdkView`, which will be sent in`SessionObserver.onUiContainerChanged()`if`SandboxedUiAdapterSignalOptions.OBSTRUCTIONS`is included in the associated`SessionObserverFactory.signalOptions`. Obstructions are reported relative to the view itself.

**API Changes**

- Moved`SandboxedSdkUi`from ui-client into a new ui-client-compose library.
- Added logic to measure obstructions on UI containers. ([I34bea](https://android-review.googlesource.com/#/q/I34bea6c7c016b1a7a03056ce7e8256e644235b74))

**Bug Fixes**

- Fixed`SandboxedSdkView.setAlpha()`, which now updates the alpha of its content view.

### Version 1.0.0-alpha15

March 26, 2025

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha15`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha15`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha15`are released. Version 1.0.0-alpha15 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..78132378b67c86698d1ade3dc368c9f15d738a71/privacysandbox/ui).

**New Features**

- Set the default Z-ordering of`SandboxedSdkView`and`SandboxedSdkUi`to "below", indicating that the provider's surface is now placed below the client's window. Added support for the UI provider to receive`MotionEvents`in this mode after being received by the client window.
- Added a`signalOptions`field to the`SessionObserverFactory`interface. This can be used to define a set of String options which will be used to determine which signals are collected for the associated`SessionObserver`. The initial set of signals is defined in`SandboxedUiAdapterSignalOptions`. If no signal options are set, only`SessionObserver.onSessionOpened()`and`SessionObserver.onSessionClosed()`will be called.

**API Changes**

- Renamed`SessionConstants`to`SessionData`in`SandboxedUiAdapter.openSession()`.

**Known Issues**

- When the SDK is loaded in the SDK Runtime and the Z-order of`SandboxedSdkView`or`SandboxedSdkUi`is "above", the gesture is exclusively received by the provider window and not transferred to the client window anymore.

### Version 1.0.0-alpha14

February 26, 2025

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha14`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha14`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha14`are released. Version 1.0.0-alpha14 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/4c47131cd5b50c3091fc0874eb606aaac5b168fa..fd7408b73d9aac0f18431c22580d9ab612278b1e/privacysandbox/ui).

**New Features**

- You can now create 'shared UI', i.e. UI that can have elements that are client-owned and provider-owned. Shared UI can be hosted using`SharedUiContainer`, which extends`ViewGroup`. New APIs utilize the concept of session management similar to that of`SandboxedSdkView`and`SandboxedUiAdapter`.
- All APIs added in this release are behind the`SharedUiPresentationApi``@RequiresOptIn`flag.

**API Changes**

- Added session management and asset registration APIs to`SharedUiContainer`. Session management is implemented using`SharedUiAdapter`introduced in the same release. ([Ic60b0](https://android-review.googlesource.com/#/q/Ic60b02e354b9b561732e914599269e06050405e5))
- Added`SharedUiContainer`that can host client-owned and provider-owned UI. It places all of its child views in the top left corner. ([Ia7310](https://android-review.googlesource.com/#/q/Ia7310cc5be45e54912aebee0669aab6152de59bd))
- Added backwards compatibility support for`SharedUiAdapter`. ([I56d7a](https://android-review.googlesource.com/#/q/I56d7ab5ef8c1630d339b6f1f2375a8b780dc3f33))
- Added`SharedUiAdapter`for session management of View containers that can host client-owned and provider-owned UI. Session management logic is similar to that of`SandboxedUiAdapter`. ([I501f6](https://android-review.googlesource.com/#/q/I501f67b9a1562649e73c1295526c85a81e44580e))

**Bug Fixes**

- Compute viewability when`onVisibilityAggregated`is called. ([I91c69](https://android-review.googlesource.com/#/q/I91c69f41bbb779cfe4e72d7c3091b52cc627c40b))

**Known Issues**

- When placed inside a`PoolingContainer`,`SharedUiContainer`closes the session on window detachment.

### Version 1.0.0-alpha13

January 29, 2025

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha13`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha13`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha13`are released. Version 1.0.0-alpha13 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..4c47131cd5b50c3091fc0874eb606aaac5b168fa/privacysandbox/ui).

**New Features**

- Added a Composable object called`SandboxedSdkUi`which can be used to display remote content within a Compose UI. This object utilizes existing`SandboxedSdkView`concepts for session management and event listeners. ([I009cf](https://android-review.googlesource.com/#/q/I009cfe94ac9e612dcbdfd95b05e5b703549ece1b))
- Changed the`SandboxedUiAdapter.openSession`signature to include a new`SessionConstants`parameter which replaces the previous`windowInputToken`. This parameter is to be used to pass values which will be constant for the lifetime of the`SandboxedUiAdapter.Session`. ([Ibc0df](https://android-review.googlesource.com/#/q/Ibc0df73a948497e97133a108dd1383d681e2b4d0),[I28435](https://android-review.googlesource.com/#/q/I2843561492332167c544cdbaa25748fb1cfb0233))

**Known Issues**

- `SessionObserver`events are not sent for`SandboxedSdkUi`when it is scrolled.
- `SandboxedSdkUi`is not clipped by parent views when it is in Z-above mode.

**API Changes**

- Remove deprecated`SDKActivityLauncher`code ([I49a4f](https://android-review.googlesource.com/#/q/I49a4f10521bbbb602f04a6e2a1511eb73651c564))
- Separated observer factory registration logic from`SandboxedUiAdapter`by adding a new`SessionObserverFactoryRegistry`interface. ([I245cc](https://android-review.googlesource.com/#/q/I245ccecf4ca306dd070b63005ac58e5feaf3bd67))

### Version 1.0.0-alpha12

December 11, 2024

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha12`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha12`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha12`are released. Version 1.0.0-alpha12 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/privacysandbox/ui).

**New Features**

- Replaced`StateChangedListener`with`SandboxedSdkViewEventListener`. This event listener can be used to listen to UI displayed, session closed and session error events.

**API Changes**

- Adds`SandboxedSdkViewEventListener`for listening to UI events inside`SandboxedSdkView`. This version also removes`StateChangedListener`. ([Id71ea](https://android-review.googlesource.com/#/q/Id71ea0a13bf1813547fa58197173dba40ca9c7d1))

**Bug Fixes**

- Removed clipping bounds logic from`SandboxedSdkView`. This will cause UX issues if`SandboxedSdkView`is placed in a scrollable container and`orderProviderUiAboveClientUi(false)`has not been called (until the underlying framework bug is fixed). ([Id420d](https://android-review.googlesource.com/#/q/Id420d880865a6debe6d595dfc2e6e9cd3316b236))
- Fixed`RemoteException`that could occur if the remote process dies while using`DelegatingSandboxedUiAdapter`.

### Version 1.0.0-alpha11

November 13, 2024

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha11`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha11`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha11`are released. Version 1.0.0-alpha11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..6f09cf2ae979e48fdb19485f757a033e4a34bb82/privacysandbox/ui).

**New Features**

- Introduced an experimental API,`DelegatingSandboxedUiAdapter`, which extends`SandboxedUiAdapter`and can be used to delegate between different`SandboxedUiAdapters`. When this adapter is set on a client container such as`SandboxedSdkView`, the delegating adapter can change the delegate adapter using`updateDelegate`. This will close the existing session and create a new`SandboxedUiAdapter.Session`for the new delegate. This allows for seamless transitions between delegates. ([I5f1c5](https://android-review.googlesource.com/#/q/I5f1c501d1f4018d0f5eba2bd569eafe065e824aa),[I9e3e7](https://android-review.googlesource.com/#/q/I9e3e70ad9118fae9da424749f54043de672ae72f))
- Added better`SandboxedSdkView`support for padding. ([Ic414f](https://android-review.googlesource.com/#/q/Ic414fb34bce985fc31423cc8161fc970f7360233))

**Bug Fixes**

- Fixed`NullPointerException`that could occur on a global layout event.

### Version 1.0.0-alpha10

September 18, 2024

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha10`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha10`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha10`are released. Version 1.0.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/948119be341fa4affc055418e695d8c4c7e5e2e4..0431b84980e97d6bafdfda7c9038bc4d9529564f/privacysandbox/ui).

**New Features**

- Updated session opening logic to only open a session inside a`SandboxedSdkView`if the window containing the`SandboxedSdkView`is visible.
- Updated`SessionObserver`logic to send`onUiContainerChanged`when the visibility of the window containing the`SandboxedSdkView`changes.

**Bug Fixes**

- Invoke`onUiContainerChanged`when the window visibility changes ([I541cf](https://android-review.googlesource.com/#/q/I541cfd2fc205a4874f7f9387dd0a85b360b46b78))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.0.0-alpha09

June 26, 2024

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha09`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha09`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha09`are released. Version 1.0.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..948119be341fa4affc055418e695d8c4c7e5e2e4/privacysandbox/ui).

**New Features**

- Introduced`AbstractSandboxedUiAdapter`and`AbstractSandboxedUiAdapter.AbstractSession`abstract classes that can be used by UI providers to avoid implementing the entire`SandboxedUiAdapter`or`Session`interfaces. It is recommended for UI providers to use these abstract classes.
- Added`registerObserverFactory`logic that allows a`SessionObserverFactory`to be attached to a`SandboxedUiAdapter`. When a`SessionObserverFactory`is attached to an adapter, a`SessionObserver`will be created for each new UI session created for that adapter. The created`SessionObserver`will receive an`onSessionOpened`callback when the UI session is opened. When the UI presentation of the`Session`'s view changes,`SessionObserver.onUiContainerChanged`will be called.`onUiContainerChanged`is throttled and will be called at most every 200ms.
- Added`SandboxedSdkViewUiInfo`which can be created from the`Bundle`sent in`SessionObserver.onUiContainerChanged`. This object represents the UI state of the`SandboxedSdkView`that is hosting the UI session. It contains height and width information, a`Rect`representing the geometry of the view that is visible on screen, and an opacity hint that represents the opacity of the view.

**API Changes**

- Add opacity hint to`SandboxedSdkViewUiInfo`. ([I093ac](https://android-review.googlesource.com/#/q/I093acd0cfe7506466497257f2732257274d1e15f))
- Add`SessionObserver.onUiContainerChanged`and`SandboxedSdkViewUiInfo`. ([Ie98bc](https://android-review.googlesource.com/#/q/Ie98bcf74e46b6b9cb4f3668f664935dd25620e11))
- Add`SessionObserver`interface and registration logic. ([I047dc](https://android-review.googlesource.com/#/q/I047dc591b385780fb8c8b914832165b48ca8727d))
- Add`AbstractSandboxedUiAdapter`and`AbstractSession`. ([I3617a](https://android-review.googlesource.com/#/q/I3617af7cec1902062750eaa6d6e3c9cad57ff87d))

**Known Issues**

- When the UI provider is in the same process as the client application,`SessionObserver.onUiContainerChanged`is not sent when the container scrolls.

### Version 1.0.0-alpha08

May 14, 2024

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha08`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha08`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha08`are released. Version 1.0.0-alpha08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/privacysandbox/ui).

**New Features**

- Added support for using`SandboxedSdkView`inside a`PoolingContainer`such as a`RecyclerView`. When a`SandboxedSdkView`has a parent that is a`PoolingContainer`, the lifecycle of its UI sessions will be aligned with that of the`PoolingContainer`to ensure that the session can persist through window detachment.

**API Changes**

- Deprecated Privacy Sandbox Activity APIs. These APIs can now be found in the dedicated Activity library`androidx.privacysandbox.activity`instead. ([I68beb](https://android-review.googlesource.com/#/q/I68beb04e2ec882bbf13b87d5b29e5885bc74ddce))

**Bug Fixes**

- Fixed rendering bug when displaying remote content inside pooling containers. ([I804df](https://android-review.googlesource.com/#/q/I804dfd4ab8736593ed310df2f72e5ae37b73b381))
- Fixed a bug that caused rendering issues for`ViewGroups`in backwards compatibility mode. ([I8de92](https://android-review.googlesource.com/#/q/I8de92044eee18d7aee96cb04e62e7d1ca89b2a12))
- When one of`SandboxedSdkView`'s parents is a`PoolingContainer`, close the UI Session when the`PoolingContainer`indicates resources can be released, instead of on window detachment. ([I2046b](https://android-review.googlesource.com/#/q/I2046b6630cb57fd6ffd47fb0e5a75301ced0a260))

**External Contribution**

- `GestureDetectorCompat`is now deprecated as`GestureDetector`is available from the`minSdk`. ([Icc4cd](https://android-review.googlesource.com/#/q/Icc4cd9df0b358863ac36d059dc6b997775321be6))

### Version 1.0.0-alpha07

October 18, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha07`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha07`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha07`are released.[Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91bb8c1f81dcb031bda00fcd8e55f1e890b56f06..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/privacysandbox/ui)

**New Features**

- Added backwards compatibility support for the library. On API 33 and below, the provider's view will be rendered inside the app process, in a different classloader. ([If0b7a](https://android-review.googlesource.com/#/q/If0b7adce29b55c8058a3d0789b46600815b3e1e3))
- Added logic that allows the resizing of host and provider containers to be committed in the same frame to avoid visible UI jank. ([Ic2cd9](https://android-review.googlesource.com/#/q/Ic2cd94d14cc2cc34abd3effcfa750cfccc05977e))

**API Changes**

- MinSdk for the library bumped to API 21. ([I474b8](https://android-review.googlesource.com/#/q/I474b853da5fdd363934f43a40b256c9c4f5345c3))

### Version 1.0.0-alpha06

September 20, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha06`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha06`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha06`are released.[Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/privacysandbox/ui)

**New Features**

- Added logic to clip`SandboxedSdkView`to the "bounding parent" View that it may scroll within. This ensures that the contents of the`SandboxedSdkView`do not occlude other views or any UI components outside of the root content view. ([I9ea94](https://android-review.googlesource.com/#/q/I9ea945b86383a9eb663dfc0922c66c620e60a2e5))

**API Changes**

- Rename`SandboxedSdkView.setZOrderOnTopAndEnableUserInteraction`to`orderProviderUiAboveClientUi`([Iecb7e](https://android-review.googlesource.com/#/q/Iecb7e9ca8d7120713689806e5a78692e386c7fd7))

**Bug Fixes**

- Send the correct Z-order value to the host. ([Ib0ddf](https://android-review.googlesource.com/#/q/Ib0ddf82ffe6942b200891e0695dcc1d961c68a2f))
- Only transfer touch focus for vertical scrolls/flings. ([I0528c](https://android-review.googlesource.com/#/q/I0528caf3a662ab647a893b18f6d6fb5d6b19c2d4))

### Version 1.0.0-alpha05

August 9, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha05`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha05`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha05`are released.[Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..5d7dd999525725bd038a00ca4e89e0fef624a6da/privacysandbox/ui)

**New Features**

- Added logic to transfer touch focus to host on scroll and fling gestures originating from`SandboxedSdkView`. This allows the client's scrollable container hosting provider UI to respond correctly to scrolls and flings.

**API Changes**

- Added`windowInputToken`parameter to`SandboxedUiAdapter`([Ief578](https://android-review.googlesource.com/#/q/Ief578bfa0202f8577e6a426c5b049f763c0b4846))

**Bug Fixes**

- Set session state to Active after the first draw ([I36f3f](https://android-review.googlesource.com/#/q/I36f3f32628c10ddb6fdd61cd4d63565138042794))
- Fix layout issue with`SandboxedSdkView`. ([I09cb8](https://android-review.googlesource.com/#/q/I09cb8ca91bc59523d4d970eaf3831eb33f99bf8e))
- Added logic to transfer touch focus to host. ([I33b54](https://android-review.googlesource.com/#/q/I33b54b772e2802e2f987aa2414e06f83bafd9e7f))
- Add`windowInputToken`parameter to`SandboxedUiAdapter`. This is necessary to ensure that the`SurfaceControlViewHost`'s token is correctly associated with the host of the embedded hierarchy. ([Ief578](https://android-review.googlesource.com/q/Ief578bfa0202f8577e6a426c5b049f763c0b4846))
- Run`notifyResized`inside the main thread. ([I62440](https://android-review.googlesource.com/#/q/I6244052f1a76345026664a2956064755d48d603b))
- Fix crash in the`Session.close()`flow. ([I5392e](https://android-review.googlesource.com/#/q/I5392e8af71f2c47511d668100544bd4939375546))

### Version 1.0.0-alpha04

June 21, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha04`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha04`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha04`are released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..3b5b931546a48163444a9eddc533489fcddd7494/privacysandbox/ui)

**New Features**

- Introduce the`SdkActivityLauncher`. An interface for allowing runtime enabled SDKs to launch activities. ([I5b3dc](https://android-review.googlesource.com/#/q/I5b3dc443f76c5c43e88a43ba272869d9b15668b0))

**Bug Fixes**

- Fix`notifyZOrderChanged`race condition. Ensures that the UI provider is notified for all Z-order changes. The UI provider will not be explicitly notified if the Z-order of the`SandboxedSdkView`is changed before openSession is invoked.

### Version 1.0.0-alpha03

May 24, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha03`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha03`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha03`are released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/privacysandbox/ui)

**New Features**

- `StateChangedListener`informs the application of changes in the UI session

**API Changes**

- Added`StateChangedListener`to replace the`ErrorConsumer`([Icd5d3](https://android-review.googlesource.com/#/q/Icd5d31a2f6a095683eaec51688ae395f0e279987))

**Bug Fixes**

- Fixed`notifyZOrderChanged`race condition so the UI provider is notified for all Z-order changes

### Version 1.0.0-alpha02

April 19, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha02`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha02`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha02`are released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/privacysandbox/ui)

**Bug Fixes**

- Disabled flaking testChangingSandboxedSdkViewLayoutChangesChildLayout test

### Version 1.0.0-alpha01

March 8, 2023

`androidx.privacysandbox.ui:ui-client:1.0.0-alpha01`,`androidx.privacysandbox.ui:ui-core:1.0.0-alpha01`, and`androidx.privacysandbox.ui:ui-provider:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/privacysandbox/ui)

**New Features**

- These are new jetpack libraries that applications and Runtime Enabled SDKs (Privacy Sandbox) can use to let the application (client) host any UI provided by the SDK (provider).