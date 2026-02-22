---
title: https://developer.android.com/jetpack/androidx/releases/tv
url: https://developer.android.com/jetpack/androidx/releases/tv
source: md.txt
---

# tv

API Reference  
[androidx.tv.foundation](https://developer.android.com/reference/kotlin/androidx/tv/foundation/package-summary)  
[androidx.tv.foundation.lazy.grid](https://developer.android.com/reference/kotlin/androidx/tv/foundation/lazy/grid/package-summary)  
[androidx.tv.foundation.lazy.list](https://developer.android.com/reference/kotlin/androidx/tv/foundation/lazy/list/package-summary)  
[androidx.tv.material3](https://developer.android.com/reference/kotlin/androidx/tv/material3/package-summary)  
Provides developers with Compose and Material design functionalities in order to write applications for TV

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| July 16, 2025 | [1.0.1](https://developer.android.com/jetpack/androidx/releases/tv#1.0.1) | - | - | [1.1.0-alpha01](https://developer.android.com/jetpack/androidx/releases/tv#1.1.0-alpha01) |

## Declaring dependencies

To add dependencies on tv-foundation and tv-material, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.tv:tv-foundation:1.0.0-alpha12"
    implementation "androidx.tv:tv-material:1.1.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.tv:tv-foundation:1.0.0-alpha12")
    implementation("androidx.tv:tv-material:1.1.0-alpha01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1254578+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1254578&template=1739419)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

There are no release notes for this artifact.

## Tv-Material Version 1.1

### Version 1.1.0-alpha01

January 15, 2025

`androidx.tv:tv-material:1.1.0-alpha01` is released. Version 1.1.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ac3ae914fa04f0399f0543d83cef4c93b2a54a8d..ad66672b42ec1e9359219e82b7f8189d03df40f5/tv/tv-material).

**API Changes**

- Change `FocusEnterExitScope.cancelFocus()` to `cancelFocusChange()`([I89959](https://android-review.googlesource.com/#/q/I89959589e5302fbda9782426938cade81a96f65e))
- `FocusProperties.enter` and `FocusProperties.exit` have been replaced with `onEnter` and `onExit`, respectively,using a receiver scope instead of `FocusDirection` parameter. ([I6e667](https://android-review.googlesource.com/#/q/I6e667ad84b51a525531f4902c1a0ac6ab8b4fba8))

**Bug Fixes**

- Moved `CompositingStrategy.OffScreen` from Surface to Text for fixing the jittery text while scaling. ([I92b15f17](https://android-review.googlesource.com/q/I92b15f174424d3009c822d14fd8d530a2cad1704))
- Fixed broken focus management in Carousel ([Ie508b721375](https://android-review.googlesource.com/q/Ie508b721375dd62b23007e9b0bbb7375bc458e51))
- Surface (non-interactive) has a simplified implementation as compared to the interactive ones. ([I7ea545150](https://android-review.googlesource.com/q/I7ea545150dfce518ba280247843140530c3d1ecd))

## Tv-Material Version 1.0

### Version 1.0.1

July 16, 2025

`androidx.tv:tv-material:1.0.1` is released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ac3ae914fa04f0399f0543d83cef4c93b2a54a8d..362dfa0918241714146398df26a837a8304472e0/tv/tv-material).

**Bug Fixes**

- Updated the `NavigationDrawerItem`'s height to match the specifications. ([cf9a3ce](https://android-review.googlesource.com/c/platform/frameworks/support/+/3442504))
- Moved compositing strategy configuration from Surface composable to the Text composable. This fixes the bug where Exoplayer wasn't rendering on the Surface composables on lower Android API versions. ([9858ffb](https://android-review.googlesource.com/c/platform/frameworks/support/+/3427222))

### Version 1.0.0

August 21, 2024

`androidx.tv:tv-material:1.0.0` is released. Version 1.0.0 is the first stable release of `androidx.tv:tv-material`.

### Version 1.0.0-rc02

August 7, 2024

`androidx.tv:tv-material:1.0.0-rc02` is released. Version 1.0.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4237f41666396b1ff39ffba3563807151fed2313..8b6a421412278b50d22e0c16099229b1f2cd7362/tv/tv-material).

**Bug Fixes**

- Fixed Jittery text animation in Surface composable. ([3163319](https://android-review.googlesource.com/c/platform/frameworks/support/+/3163319))

### Version 1.0.0-rc01

July 10, 2024

`androidx.tv:tv-material:1.0.0-rc01` is released. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fbd1ac175922f44c69a13545d194066ee428b342..4237f41666396b1ff39ffba3563807151fed2313/tv/tv-material).

### Version 1.0.0-beta01

May 1, 2024

`androidx.tv:tv-material:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..fbd1ac175922f44c69a13545d194066ee428b342/tv/tv-material).

**API Changes**

- `ColorScheme` and its utility functions are now stable. ([If34fa](https://android-review.googlesource.com/#/q/If34faf903bbaf34f9f3c597524b58f9d31bf8f38))
- `LocalContentColor` is now stable ([I60ee2](https://android-review.googlesource.com/#/q/I60ee21ae1cc6701da42cecabf5a046ae51c3af45))
- `Typography` API is now stable ([I088d6](https://android-review.googlesource.com/#/q/I088d682327725891b9625a5c6fe40f6dfb144410))
- Shapes APIs are now stable ([I0f5f4](https://android-review.googlesource.com/#/q/I0f5f47d75154bbdceb3b7fec142dceb53f27054d))
- Border API is now stable ([I69281](https://android-review.googlesource.com/#/q/I6928141d818936dcaade9c519ad616640ea15a12))
- Glow API is now stable ([Iea5f1](https://android-review.googlesource.com/#/q/Iea5f15e85f8d1d99497b8c17394b70473bb31141))
- Icon component is now stable ([I62c2d](https://android-review.googlesource.com/#/q/I62c2d2d550c3d39c1a5604192299fd723c39e013))
- `LocalTextStyles` API is now stable ([Iaded8](https://android-review.googlesource.com/#/q/Iaded884203bff5cdff16acc38079a6ec2d420f09))
- `MaterialTheme` API is now stable ([I2f541](https://android-review.googlesource.com/#/q/I2f541b5504129b6fb2c56da4667e314986505566))
- Text Component is now stable ([Ib9e31](https://android-review.googlesource.com/#/q/Ib9e3120b3c88fbada2f004ea063c8af2bb58139b))
- `RadioButton` component is now stable ([Ia03c8](https://android-review.googlesource.com/#/q/Ia03c8020701aa548cdcef8e62ad09ad74cc0b249))
- Switch component is now stable ([I6cea3](https://android-review.googlesource.com/#/q/I6cea3a169f428501b498799d2c2db0d5f7badce0))
- `Checkbox` components are now stable ([I7eafc](https://android-review.googlesource.com/#/q/I7eafcf107814c17c6c52f70915c74fc2be1c0216))
- Surface components are now stable ([I58758](https://android-review.googlesource.com/#/q/I587587d15c911cf96c343ed0b70e1fd4bd18349f), [I04aca](https://android-review.googlesource.com/#/q/I04aca8dbb52b31d807ab4b1026e60a54fd8ac901))
- Renamed `NonInteractiveSurfaceDefaults` to `SurfaceDefaults` and `NonInteractiveSurfaceColors` to `SurfaceColors` ([I0812e](https://android-review.googlesource.com/#/q/I0812e6880c45d74ba99d626cdd4f71b2475f5ccf))
- Selectable Surface now uses "select" terminology instead of "check" because they both have different semantics meaning ([I5a206](https://android-review.googlesource.com/#/q/I5a2062f4f1edf42aeb7de2def0f7a466bbc51170))
- `NavigationDrawer` and `NavigationDrawerScope` are now stable ([I249c1](https://android-review.googlesource.com/#/q/I249c1d133a6ef73740c5a8ad2a6ad7feca5c7c56))
- `NavigationDrawerItem` component is now stable ([Id6986](https://android-review.googlesource.com/#/q/Id6986ad9e01b56c558caa60e16dc9d87939b34b7))
- Tab and `TabRow` components are now stable ([I92d92](https://android-review.googlesource.com/#/q/I92d926fa7b1997051374a0dd5db7c61e4f888205))
- `Button`, `OutlinedButton`, `IconButton`, `OutlinedIconButton` and `WideButton` components are now stable ([Ib4de8](https://android-review.googlesource.com/#/q/Ib4de8ecff8e965b3418ebd6273fc29b5e4a25a43))
- `Card`, `ClassicCard`, `CompactCard`, `WideClassicCard`, `StandardCardContainer` \& `WideCardContainer` components are now stable ([I34390](https://android-review.googlesource.com/#/q/I343909f27bf4886b5bd512731291763b007e785e))
- Renamed `StandardCardLayout` to `StandardCardContainer` and `WideCardLayout` to `WideCardContainer` ([I08883](https://android-review.googlesource.com/#/q/I088834b0a80d134527c7dcd0be2474934f0b24a6))
- Removed `CardContainerDefaults.ImageCard` and renamed `CardDefaults.ContainerGradient` to `CardDefaults.ScrimBrush` ([I6adfe](https://android-review.googlesource.com/#/q/I6adfe045c24f9344ab53703f1e1d44d03dba0417)). You can make use of `Card` inplace of `CardContainerDefaults.ImageCard` in your card containers.
- `ListItem` and `DenseListItem` are now stable ([Idebd9](https://android-review.googlesource.com/#/q/Idebd9a3de84bdbb9aeaaba5c06bf52e73ff3bf37))
- `ListItemDefaults.ListItemShape`, `ListItemDefaults.FocusedDisabledBorder` \& `ListItemDefaults.SelectedContainerColorOpacity` are now private ([I5d533](https://android-review.googlesource.com/#/q/I5d53356ee38b64ba4ae0b817e07ed2d4285a1b4f))
- Rearranged the `ListItem`'s parameters \& renamed `ListItemDefaults.ListItemElevation` to `ListItemDefaults.TonalElevation` ([Id6841](https://android-review.googlesource.com/#/q/Id68410be555329772146128a3374c4b2c09bd905)). `headlineContent` parameter has been moved to the top of the composable. Earlier, you could make use of Kotlin's trailing lambda syntax to pass the `headlineContent`. Now, you will have to make use of named parameter syntax to provide the `headlineContent`.
- `LocalAbsoluteTonalElevation` is now internal ([Ibfc65](https://android-review.googlesource.com/#/q/Ibfc6544474f346b17db14f9b1f343878d089b900))
- The `ImmersiveList` component has been removed. Check out [this sample](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:tv/samples/src/main/java/androidx/tv/samples/ImmersiveListSamples.kt;drc=5920fece16ad6723107098f24a492a25937cd51a) to learn how to build it yourself. ([Id48da](https://android-review.googlesource.com/#/q/Id48da9dd9302074314a120d235b56b4561089ffa))
- tv-material components exposing a `MutableInteractionSource` in their API have been updated to now expose a nullable `MutableInteractionSource` that defaults to null. There are no semantic changes here: passing null means that you do not wish to hoist the `MutableInteractionSource`, and it will be created inside the component if needed. Changing to null allows for some components to never allocate a `MutableInteractionSource`, and allows for other components to only lazily create an instance when they need to, which improves performance across these components. If you are not using the `MutableInteractionSource` you pass to these components, it is recommended that you pass null instead. It is also recommended that you make similar changes in your own components. ([I309b4](https://android-review.googlesource.com/#/q/I309b436d212ef53897979df40da9b1768377893f), [b/298048146](https://issuetracker.google.com/issues/298048146))
- TV Text component's `TextAlign` parameter is now non-null ([Ib73b1](https://android-review.googlesource.com/#/q/Ib73b136b5d997de3869ca63e7c6dcad5e513ec1e), [b/299490814](https://issuetracker.google.com/issues/299490814))
- Introduced a special Unspecified value for `TextAlign`, `TextDirection`, `Hyphens` and `LineBreak` fields of the `ParagraphTextStyle` to replace ([I4197e](https://android-review.googlesource.com/#/q/I4197ea85db556846ecad27ca8f561955e2370951), [b/299490814](https://issuetracker.google.com/issues/299490814))

**Behaviour Changes**

- Default value of the `shape` parameter for non-interactive `Surface` has been changed to `RectangleShape` ([I1b859cb](https://android-review.googlesource.com/#/q/I1b859cb4ea1cd317bd6a536d01671d903c2bfb86))
- Some carousel features have been dropped for the beta launch due to necessary APIs being experimental ([I0e755d4](https://android-review.googlesource.com/#/q/I0e755d4d2200553e6196e74bb0a40ce7aa7d541b))
- Changing `contentColor` in `Surface` no longer animates between states ([I436e794f](https://android-review.googlesource.com/#/q/I436e794f32ef2f9dbe28c5dc854330ce34023b9d))

## Version 1.0.0

### Version 1.0.0-alpha12

January 15, 2025

`androidx.tv:tv-foundation:1.0.0-alpha12` is released. Version 1.0.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..ad66672b42ec1e9359219e82b7f8189d03df40f5/tv/tv-foundation).

**API Changes**

- Cleanup lazy layouts from tv-foundation. Refer to 1.0.0-alpha11 release notes to migrate away from tv-foundation lazy layouts. ([I2fdd3](https://android-review.googlesource.com/#/q/I2fdd36cddca3e2beeec20e48746f8980efb1c385), [b/358913893](https://issuetracker.google.com/issues/358913893))

### Version 1.0.0-alpha11

July 10, 2024

`androidx.tv:tv-foundation:1.0.0-alpha11` is released. Version 1.0.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..56579bc30499ce39f0d7a6713a065b00c6194206/tv/tv-foundation).

**API Changes**

- Tv Lazy Layouts have been deprecated from tv-foundation library. Refer to [this ticket](https://issuetracker.google.com/issues/348896032) to learn how to migrate away from the tv lazy layouts. ([I0855f](https://android-review.googlesource.com/#/q/I0855f36b41cf8bc374e8e69ac5faeabfefc97aa9), [b/332674072](https://issuetracker.google.com/issues/332674072))
- `PlatformImeOptions` is now a concrete class instead of an interface. ([If40a4](https://android-review.googlesource.com/#/q/If40a4c3e832e7852f214e18af469f5ce68e798b7))

### Version 1.0.0-alpha10

October 4, 2023

`androidx.tv:tv-foundation:1.0.0-alpha10` and `androidx.tv:tv-material:1.0.0-alpha10` are released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..1f7407d4293384a1b91bc142880e3525048b3443/tv)

**New Features**

- Introduced `NavigationDrawerItem` to be used within `NavigationDrawer` and `ModalNavigationDrawer`. ([I4b491](https://android-review.googlesource.com/#/q/I4b491cc8b9e9d4e5349e88d2d07e1766a666a207))
- Add baseline profile to tv-foundation library. ([2b57fd7](https://android-review.googlesource.com/#/q/I849e45ff4f3ff387b682c3da82b3dd815a3f8d23))
- Add baseline profile to tv-material library. ([1711ff5](https://android-review.googlesource.com/#/q/Ice9706c0a3514b5cdec8b2746e514f585530bb52))

**API Changes**

- Renamed `NavigationDrawerScope.doesTabRowHaveFocus` to `NavigationDrawerScope.hasFocus`. ([I8286b](https://android-review.googlesource.com/#/q/I8286b4833c26e250527067ba49ebb44395526cea))
- Renamed `TabRowScope.isActivated` to `TabRowScope.hasFocus`. ([Ic4273](https://android-review.googlesource.com/#/q/Ic4273b60a106128e807ac69e69b3315bb953536c))

**Bug Fixes**

- Fix compatibility of Carousel with adjacent items that use focus restorer APIs. ([7b2a7a4](https://android-review.googlesource.com/#/q/7b2a7a435fe6e724b24faa40195402a6f787433b))
- Disable glow indication for API_LEVEL below 28 as it is not supported by the OS. ([6d3616f](https://android-review.googlesource.com/#/q/I35c4633cb1a5e28867ab60d666400bd137101c37))
- Fix ANR crash caused by improper item placement in lazy containers when fast scrolling in reverse direction. ([642d65c](https://android-review.googlesource.com/#/q/I1c0bd8d5e40a839f2736b44dd6fd303ad6fa8772))
- Removed background padding in Modal Navigation Drawer. ([69965b2](https://android-review.googlesource.com/#/q/Ied625de5fca8a190835b0aa8297e6ec60cd63855))
- Fix Scrim in Navigation Drawer to be drawn above background content instead of behind it. ([d4bbefb](https://android-review.googlesource.com/#/q/I8cdd020234b214988b8f7644e7011a668131e358))

### Version 1.0.0-alpha09

September 6, 2023

`androidx.tv:tv-foundation:1.0.0-alpha09` and `androidx.tv:tv-material:1.0.0-alpha09` are released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/tv)

**API Changes**

- Add `ReusableComposition` interface for managing lifecycle and reuse of subcompositions. ([I812d1](https://android-review.googlesource.com/#/q/I812d1fa36791857a04471882d5edabea1400c15e), [b/252846775](https://issuetracker.google.com/issues/252846775))
- Sync tv-foundation fork with compose-foundation. ([I737c3](https://android-review.googlesource.com/#/q/I737c337d6ff7337d651aa0c0efa7acbee762fe7b), [b/287011882](https://issuetracker.google.com/issues/287011882))
- Overload of `LazyLayout` added, it accepts a lambda of `LazyLayoutItemProvider`, not a plain object as it was before. The previous overload is deprecated. ([I42a5a](https://android-review.googlesource.com/#/q/I42a5a3d5933deaccac5b5fc6df15c47194cf8b05))
- Add `TvKeyboardAlignment` to allow the developer to configure the on-screen keyboard position through the `AndroidImeOptions`. ([Idb772](https://android-review.googlesource.com/#/q/Idb772f8091a3a415659ccb0fb58846917c8e229c))
- Add `rememberCarouselState` to remember `CarouselState` with `Saver` to TV Compose Material. ([Id7275](https://android-review.googlesource.com/#/q/Id72754d77017118d18190d900e63ddd32e8e7d21))
- Changing the `scrimColor: Color` parameter to `scrimBrush:Brush` parameter to allow users to add gradients to the scrim. ([I254d4](https://android-review.googlesource.com/#/q/I254d4fa8c517abfbd34838d3e7c4a0bdf13346a9))

### Version 1.0.0-alpha08

July 26, 2023

`androidx.tv:tv-foundation:1.0.0-alpha08` and `androidx.tv:tv-material:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d138dfb57d0d604724f694b506cb12e8fee6ea98..4aed940027a19667e67d155563fc5fa8b7279313/tv)

**New Features**

- Introduce Chip components for Compose for TV material. ([I86da4](https://android-review.googlesource.com/#/q/I86da44e8ffbd8b123d525f8f9b7a31a71077d96c))
- Add `ListItem` component to TV Compose Material. ([I3f0b3](https://android-review.googlesource.com/#/q/I3f0b329db888f8f0515062dcb521d97079bf8ec0))
- Add `DenseListItem`component to TV Compose Material. ([I536bf](https://android-review.googlesource.com/#/q/I536bf218697af55173d4505e7e28ea5b82189559))

**API Changes**

- Marked public tv-material APIs as Experimental. ([I632e7](https://android-review.googlesource.com/#/q/I632e7c1d1aa6cb61a82d582985cb9328caa0dd2f))
- Introduced `TabRowScope` to share state from `TabRow` composable with Tab composable and renamed `TabColors` properties. ([Ief587](https://android-review.googlesource.com/#/q/Ief5874a34a8319d8a600e9a494e28c10bf4713c0))

### Version 1.0.0-alpha07

June 7, 2023

`androidx.tv:tv-foundation:1.0.0-alpha07` and `androidx.tv:tv-material:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..73f902dee011bfe400d8a0330bfd8d4bb632065f/tv)

**API Changes**

- Components' scale indications now include None to disable scaling. ([I50df5](https://android-review.googlesource.com/#/q/I50df56f8a2e1d0524ef4834120752ca896c9a963))
- Added long click support for TV Material Surface, Cards and Buttons. ([Id2b89](https://android-review.googlesource.com/#/q/Id2b89be699e7d8c7d077eec496ca8c611d099992))
- `CarouselItem` and `CarouselScope` have been removed. Foreground content animation can be achieved in the slide by using `Modifier.animateEnterExit` from `AnimatedContentScope`. ([Ic038e](https://android-review.googlesource.com/#/q/Ic038ed48502c6f01bf89d7875e8ee2b5b2d8d233))
- Merged `color` and `contentColor` params as `colors` for TV Material Surface. ([Ie69eb](https://android-review.googlesource.com/#/q/Ie69eb3cdfff2a4aa0e5a00f7564d56fea2e176d8))
- Introduced `RadioButton` composable in TV Material. ([I08690](https://android-review.googlesource.com/#/q/I086903cf19d3651f642a5abc3cc82c74f1098481))
- Introduced `Switch` composable in TV Material. ([I45e29](https://android-review.googlesource.com/#/q/I45e2908e9190dc058784056aa169b537614519bc))
- Introduced `Checkbox` composable in TV Material. ([I6a45a](https://android-review.googlesource.com/#/q/I6a45af2f388e7a185241360260f14af7ac151c2f))
- Introduced non-interactable Surface in TV Material. ([Ic5f85](https://android-review.googlesource.com/#/q/Ic5f85d30abe661505c6e02017319f3d7c589bed4))
- Make indications internal. ([Ibff82](https://android-review.googlesource.com/#/q/Ibff82ae4798c7e890d683e223271160666a37348))

### Version 1.0.0-alpha06

April 19, 2023

`androidx.tv:tv-foundation:1.0.0-alpha06` and `androidx.tv:tv-material:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/tv)

**New Features**

- Add Material 3 Card implementations optimized for TV.
  - Basic Card ([I5b701](https://android-review.googlesource.com/#/q/I5b70132ca149b6c875a2971d97ffcaf31442ac4d))
  - `ClassicCard`, `CompactCard` and `WideClassicCard` ([I70471](https://android-review.googlesource.com/#/q/I704710c40103851ee1b3bcd3d8fcb6aaf2eb8ced))
  - `StandardCardLayout` and `WideCardLayout` ([I33fae](https://android-review.googlesource.com/#/q/I33faedd7fcf0792b0378e855803e19f33788628c))
- Add Material 3 Button implementations optimized for TV.
  - Basic Button ([I69c11](https://android-review.googlesource.com/#/q/I69c114f31dd374675276629659ac40ec8c2ebbfa))
  - `IconButton` and `OutlinedIconButton` ([Ib504c](https://android-review.googlesource.com/#/q/Ib504cefcdd22dc50fd43026efcf976ab8d1d43ad))
  - `WideButton` ([I4cecf](https://android-review.googlesource.com/#/q/I4cecf3405f62f7798bcc00a48e48165c1d8a5d66))

**API Changes**

- Renamed `CarouselSlide` and `slideCount`in `Carousel` to `CarouselItem` and `itemCount`. ([Ie554c](https://android-review.googlesource.com/#/q/Ie554cbf0d7e082e6c64c0f334d47b5bd69228372))
- Renamed `forward` and `backward` `ContentTransforms` to `StartToEnd` and `EndToStart`. ([Ie554c](https://android-review.googlesource.com/#/q/Ie554cbf0d7e082e6c64c0f334d47b5bd69228372))

**Bug Fixes**

- Handle back DPAD button when focused on `NavigationDrawer`. ([d654f4](https://android.googlesource.com/platform/frameworks/support/+/d654f4d2e2b7b5af6d45d756c8faf206b844a17c))

### Version 1.0.0-alpha05

March 22, 2023

`androidx.tv:tv-foundation:1.0.0-alpha05` and `androidx.tv:tv-material:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..5e7d256f82fbafb6d059ab7b18fddd87c7531553/tv)

**API Changes**

- Introducing Side Navigation Drawer composable into `tv-material`. To learn how to use this composable, please refer to the [samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:tv/samples/src/main/java/androidx/tv/samples/NavigationDrawerSamples.kt). ([I12c08](https://android-review.googlesource.com/#/q/I12c0847b53701492f21bb064cd6ab1beb6b03a96))
- Introduce Icon composable in TV Material 3 ([I72db9](https://android-review.googlesource.com/#/q/I72db9a0631276508c90bf69a1127b5b169c92827))
- Introducing Surface composable to `tv-material` with indications such as Border, Glow and Scale, which can be used to build components that clearly highlight the focused element on the TV screen. ([I4a6d8](https://android-review.googlesource.com/#/q/I4a6d8a4ae15d9d038fa27f4c8ffbba90bb494b49)), ([Iceea1](https://android-review.googlesource.com/#/q/Iceea10dee7a9f27cff0e81c43054571f165dbcb5)), ([Iee4d4](https://android-review.googlesource.com/#/q/Iee4d4129f752bdcaff37c587868f190d2f41cdc0)), ([I79edf](https://android-review.googlesource.com/#/q/I79edfb3a936ee85ab07a87fbd4bce96d534b367a)), ([Icb376](https://android-review.googlesource.com/#/q/Icb3762b71b1338ee350176847098061b41b93606))
- Update `CarouselItem` to `CarouselSlide` to match the `slideCount` param name in 'Carousel' API ([Ic4299](https://android-review.googlesource.com/#/q/Ic42996abbc0e95c0110b0acd688c0f0118e6e2c4))

### Version 1.0.0-alpha04

February 8, 2023

`androidx.tv:tv-foundation:1.0.0-alpha04` and `androidx.tv:tv-material:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..f7337eab774a6ce3b17367d5f31708564b66e677/tv)

**New Features**

- In lazy rows, columns and grids, the pivot is overridden, if necessary, to ensure the entire item is brought into view. ([11d7e40](https://android.googlesource.com/platform/frameworks/support/+/11d7e404b79e59d4109f67eda53b073d7abe52e0))
- Add customization of tab colors in different states. ([21b2925](https://android.googlesource.com/platform/frameworks/support/+/21b2925c6ad3ac9261b0fe60ffc649b05a374034))
- Carousel now accepts custom animations for forward and backward manual scrolling. ([431494a](https://android.googlesource.com/platform/frameworks/support/+/431494a73bfe09021e5b5574504739bdf16ccead))

**API Changes**

- Renaming `androidx.tv.material` to `androidx.tv.material3` and flattening package structure under `androidx.tv.material3`. ([I6ca52](https://android-review.googlesource.com/#/q/I6ca5204047db3df141739ef3f16799277f4c05f7))
- Indicator within Carousel Indicator row is now a slot that can be customized by the developer. ([268af2a](https://android.googlesource.com/platform/frameworks/support/+/268af2a462ade6f07711bb465b6dcbffac468648))
- Renamed `focusableItem` to `immersiveListItem`. Users will have to manually add `focusable()` or `clickable()` modifier along with `immersiveListItem` ([5dd5078](https://android.googlesource.com/platform/frameworks/support/+/5dd50789a7bbcba846f41e4265bd5411fb542b02))([b/263061052](https://issuetracker.google.com/263061052))
- Renamed `timeToDisplayMillis` to `autoScrollDurationMillis` in Carousel component. ([431494a](https://android.googlesource.com/platform/frameworks/support/+/431494a73bfe09021e5b5574504739bdf16ccead))
- `CarouselItem` is now restricted to use within `Carousel`'s. ([431494a](https://android.googlesource.com/platform/frameworks/support/+/431494a73bfe09021e5b5574504739bdf16ccead))
- Carousel now accepts `ContentTransforms` as the animation definition instead of `EnterTransition` and `ExitTransitions`. ([431494a](https://android.googlesource.com/platform/frameworks/support/+/431494a73bfe09021e5b5574504739bdf16ccead))
- Introduced `PinnableContainer` api propagated by lazy lists via a composition local which allows to pin current item. ([Ib8881](https://android-review.googlesource.com/#/q/Ib8881191a529c9d9dc5e886570650b1987763207), [b/259274257](https://issuetracker.google.com/issues/259274257), [b/195049010](https://issuetracker.google.com/issues/195049010))
- Added `mainAxisItemSpacing` property to `TvLazyListLayoutInfo` and `TvLazyGridLayoutInfo` ([I37765](https://android-review.googlesource.com/#/q/I37765a04924b9e759255a48555c16ff2dc380aa4))

**Bug Fixes**

- Update tab-row to ensure it handles tab-count of 0 or 1 correctly. ([I44009](https://android-review.googlesource.com/#/q/I440099087b7a9ecca05953b55b011b56029936f4)), ([1c01525](https://android.googlesource.com/platform/frameworks/support/+/1c015259a0b6c679d0c57a7505b315f6ad473dfe)), ([b/264018028](https://issuetracker.google.com/264018028))
- Fix focus-search crash when `TvLazyColumn` contains empty `TvLazyRow`. ([e11b4fe](https://android.googlesource.com/platform/frameworks/support/+/e11b4feddd2d157c47c70c78a19a590a480bfaa3)), ([b/260299091](https://issuetracker.google.com/260299091))
- The `clickable` modifier now works with `ImmersiveList`. ([5dd5078](https://android.googlesource.com/platform/frameworks/support/+/5dd50789a7bbcba846f41e4265bd5411fb542b02)), ([b/263061052](https://issuetracker.google.com/263061052))
- Back key is now handled and used to exit Featured Carousel. ([84c138c](https://android.googlesource.com/platform/frameworks/support/+/84c138c2ddb0e893241f96b892ce5586e7c108b8))
- Carousel does not lose focus on multiple fast key-presses. ([799489f](https://android.googlesource.com/platform/frameworks/support/+/799489fbda48b1c28456669e8310220a7de29bb6))
- Carousel does not lose focus on long key-presses. ([b2cf37e](https://android.googlesource.com/platform/frameworks/support/+/b2cf37e19ad2d33fa0f9507e4985c7f8b56a1629))
- Addressed crashes when carousel slide-count changes. ([b261247](https://android.googlesource.com/platform/frameworks/support/+/b261247aa43ae317aed022705f66d614370fe311))

### Version 1.0.0-alpha03

December 7, 2022

`androidx.tv:tv-foundation:1.0.0-alpha03` and `androidx.tv:tv-material:1.0.0-alpha03` are released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..4a2f5e696614339c1ac21f706c1a17c0285780e7/tv)

**New Features**

- `TabRow` is now available as an experimental API allowing users to add top navigation bars to their apps. Generally, TV devices expect tabs to load when the tab-title is focused on in the tab-row.
- TV specific indicators like underline indicator and pill indicator are offered out of the box. Sample usages can be found in [tv-samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:tv/samples/src/main/java/androidx/tv/samples/TabRowSamples.kt)

### Version 1.0.0-alpha02

November 9, 2022

`androidx.tv:tv-foundation:1.0.0-alpha02` and `androidx.tv:tv-material:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..a1e318590b217ecfce1b2de17eed2f18b6a680bb/tv)

**Bug Fixes**

- Improved scrolling performance when scrolling through a collection of `TvLazyRows/TvLazyColumns` by reducing the focus search space.([I723a3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2255266))

### Version 1.0.0-alpha01

October 5, 2022

`androidx.tv:tv-foundation:1.0.0-alpha01` and `androidx.tv:tv-material:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/tv)

**New Features**

The first alpha contains early preview implementations of components for TV use cases, including:

- Adding modifier `scrollableWithPivot` to allow non-lazy scrolling containers such as Row, Column, Grid to have the scrolling container scroll the content so that the item-in-focus remains at the same position on the TV screen.
- Adding composables `TvLazyRow`,`TvLazyColumn`, `TvLazyHorizontalGrid`, `TvLazyVerticalGrid` to have the scrolling container scroll the content so that the item-in-focus remains at the same position on the TV screen.
- Adding Featured Carousel composable for TV that allows the user to create an auto-scrolling banner carousel.
- Adding Immersive List composable for TV that allows the user to create an Immersive Row/Column/Grid that changes the background based on the list-item in focus.

**Known issues**

- When scrolling container gains focus, the first element does not gain focus by default.
- Focusing on a `TextField` does not always open the keyboard or can inhibit focus from moving to other fields.
- Scrolling vertically in a `LazyColumn` containing `LazyRows` has poor performance.