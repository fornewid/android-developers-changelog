---
title: https://developer.android.com/jetpack/androidx/releases/hilt
url: https://developer.android.com/jetpack/androidx/releases/hilt
source: md.txt
---

# Hilt

# Hilt

[User Guide](https://developer.android.com/training/dependency-injection/hilt-android)[Code Sample](https://github.com/android/architecture-samples/tree/views-hilt)[Codelab](https://codelabs.developers.google.com/codelabs/android-hilt/#0)  
API Reference  
[androidx.hilt.lifecycle.viewmodel](https://developer.android.com/reference/kotlin/androidx/hilt/lifecycle/viewmodel/package-summary)  
[androidx.hilt.lifecycle.viewmodel.compose](https://developer.android.com/reference/kotlin/androidx/hilt/lifecycle/viewmodel/compose/package-summary)  
[androidx.hilt.navigation](https://developer.android.com/reference/kotlin/androidx/hilt/navigation/package-summary)  
[androidx.hilt.navigation.compose](https://developer.android.com/reference/kotlin/androidx/hilt/navigation/compose/package-summary)  
[androidx.hilt.navigation.fragment](https://developer.android.com/reference/kotlin/androidx/hilt/navigation/fragment/package-summary)  
[androidx.hilt.work](https://developer.android.com/reference/kotlin/androidx/hilt/work/package-summary)  
Extend the functionality of[Dagger Hilt](https://dagger.dev/hilt)to enable dependency injection of certain classes from the androidx libraries.  

|   Latest Update    |                               Stable Release                                | Release Candidate | Beta Release | Alpha Release |
|--------------------|-----------------------------------------------------------------------------|-------------------|--------------|---------------|
| September 10, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/hilt#1.3.0) | -                 | -            | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:874079+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=874079&template=1438695)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Hilt Version 1.3

### Version 1.3.0

September 10, 2025

`androidx.hilt:hilt-*:1.3.0`is released. Version 1.3.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b217c6d9af600745094beba0ccc00b35361d88b..d697e229a0933b8ef4811164e4b20f24eafafe4b/hilt).

**Important changes since 1.2.0:**

- The`hiltViewModel()`APIs for Compose have been moved to a new artifact (`androidx.hilt:hilt-lifecycle-viewmodel-compose`) and package (`androidx.hilt.lifecycle.viewmodel.compose`) such that they can be used without transitively depending on`androidx.navigation`.

### Version 1.3.0-rc01

August 27, 2025

`androidx.hilt:hilt-*:1.3.0-rc01`is released with no notable changes since 1.3.0-beta01. Version 1.3.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..1b217c6d9af600745094beba0ccc00b35361d88b/hilt).

### Version 1.3.0-beta01

August 13, 2025

`androidx.hilt:hilt-*:1.3.0-beta01`is released. Version 1.3.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..c359e97fece91f3767a7d017e9def23c7caf1f53/hilt).

### Version 1.3.0-alpha02

July 2, 2025

`androidx.hilt:hilt-*:1.3.0-alpha02`is released. Version 1.3.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..1b437892629a2cdedb46d9b7232575987b2cc6b5/hilt).

**API Changes**

- The`hiltViewModel()`APIs for Compose have been moved to a new artifact (`androidx.hilt:hilt-lifecycle-viewmodel-compose`) and package (`androidx.hilt.lifecycle.viewmodel.compose`) such that they can be used without transitively depending on`androidx.navigation`. ([Ifb222](https://android-review.googlesource.com/#/q/Ifb2226c57e78d70a282f58bafaccabe8e3b51e7f),[b/328104152](https://issuetracker.google.com/issues/328104152))

### Version 1.3.0-alpha01

May 7, 2025

`androidx.hilt:hilt-*:1.3.0-alpha01`is released. Version 1.3.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/33f909ecd90961e2478c0814f2c372c5b12e2f2f..b6c541571b9fb5471f965fc52612cb280713e5e4/hilt).

**API Changes**

- Updates the library and annotation processor to target Kotlin 2.0 to support newer Kotlin toolchain including KSP2.

## Hilt Version 1.2

### Version 1.2.0

February 21, 2024

`androidx.hilt:hilt-*:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f71c3fa96b258a9b8b03d0515fc0c1110b3a65d..33f909ecd90961e2478c0814f2c372c5b12e2f2f/hilt)

**Important changes since 1.1.0**

- Add assisted injection support to`hiltViewModel()`and`hiltNavGraphViewModels()`. Now these functions take an additional callback in which you can use the passed in assisted factory to create an assisted injected`ViewModel`.

### Version 1.2.0-rc01

February 7, 2024

`androidx.hilt:hilt-*:1.2.0-rc01`is released.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..1f71c3fa96b258a9b8b03d0515fc0c1110b3a65d/hilt)

### Version 1.2.0-beta01

January 24, 2024

`androidx.hilt:hilt-*:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/hilt)

### Version 1.2.0-alpha01

December 13, 2023

`androidx.hilt:hilt-*:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/60e349522e1cd1c1f6e4b2a79592dd8b130c36c7..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/hilt)

**API Changes**

- Add overloaded`hiltViewModel()`and`hiltNavGraphViewModels()`functions for assisted injection support. ([Ieb98d](https://android-review.googlesource.com/#/q/Ieb98de57810a71fecc58ceeb8fd674de1eba5c8f))

## Hilt Version 1.1.0

### Version 1.1.0

November 1, 2023

`androidx.hilt:hilt-*:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4367a721d36863f1754212c1c67659df43956511..60e349522e1cd1c1f6e4b2a79592dd8b130c36c7/hilt)

**Major changes since 1.0.0**

- Add KSP support to`androidx.hilt`.
- Accept`HasDefaultViewModelProviderFactory`in`hiltViewModel()`.
- The`hiltViewModel()`API now takes an optional key parameter.

### Version 1.1.0-rc01

October 18, 2023

`androidx.hilt:hilt-*:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..4367a721d36863f1754212c1c67659df43956511/hilt)

### Version 1.1.0-beta01

`androidx.hilt:hilt-common:1.1.0-beta01`,`androidx.hilt:hilt-compiler:1.1.0-beta01`,`androidx.hilt:hilt-work:1.1.0-beta01`,`androidx.hilt:hilt-navigation:1.1.0-beta01`,`androidx.hilt:hilt-navigation-compose:1.1.0-beta01`, and`androidx.hilt:hilt-navigation-fragment:1.1.0-beta01`are released.

### Version 1.1.0-alpha01

August 9, 2023

`androidx.hilt:hilt-common:1.1.0-alpha01`,`androidx.hilt:hilt-compiler:1.1.0-alpha01`, and`androidx.hilt:hilt-work:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/661b67017024a998cb20270523ec049edbc33dde..5d7dd999525725bd038a00ca4e89e0fef624a6da/hilt)

**New Features**

- Add KSP support to`androidx.hilt`. Note that this is to prepare for Hilt's KSP support. In order to use the KSP version of androidx.hilt, the main Hilt support has to be released.

## Hilt-Navigation-Fragment Version 1.1.0

### Version 1.1.0-alpha02

April 19, 2023

`androidx.hilt:hilt-navigation-fragment:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/661b67017024a998cb20270523ec049edbc33dde..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/hilt)

**API Changes**

- Accept`HasDefaultViewModelProviderFactory`in`hiltViewModel()`([I10ab6](https://android-review.googlesource.com/#/q/I10ab6e8b08e4eb2d27e0d7979e4a4f6663798245),[b/249548618](https://issuetracker.google.com/issues/249548618),[b/195190169](https://issuetracker.google.com/issues/195190169))

**Bug Fixes**

- Fixed an issue where`hiltNavGraphViewModel()`doesn't inject`SavedStateHandle`. ([3ef114](https://android-review.googlesource.com/#/q/3ef114f5b520c37096a7483b0155424234fff482),[b/272099838](https://issuetracker.google.com/issues/272099838))

## Hilt-Navigation Version 1.1.0

### Version 1.1.0-alpha02

April 19, 2023

`androidx.hilt:hilt-navigation:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/661b67017024a998cb20270523ec049edbc33dde..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/hilt)

### Version 1.1.0-alpha01

December 7, 2022

`androidx.hilt:hilt-navigation:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/60d869f2ab2e74d31f79cf029fda790cebfdb83a..4a2f5e696614339c1ac21f706c1a17c0285780e7/hilt)

## Hilt-Navigation-Compose Version 1.1.0

### Version 1.1.0-alpha01

December 7, 2022

`androidx.hilt:hilt-navigation-compose:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/60d869f2ab2e74d31f79cf029fda790cebfdb83a..4a2f5e696614339c1ac21f706c1a17c0285780e7/hilt)

**API Changes**

- The`hiltViewModel()`API now takes an optional key parameter. This allows you to get multiple instances of the same`ViewModel`type using different keys. ([I6ee47](https://android-review.googlesource.com/#/q/I6ee4727a4b690bc35af4280b61ba2986d9eebb9b),[b/245139957](https://issuetracker.google.com/issues/245139957))

## Hilt-Navigation-Compose Version 1.0.0

### Version 1.0.0

January 26, 2022

`androidx.hilt:hilt-navigation-compose:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7e2685eebba0fdb40c93e3e06609bb01398a71a3..60d869f2ab2e74d31f79cf029fda790cebfdb83a/hilt/hilt-navigation-compose)

**Major features of 1.0.0**

The`androidx.hilt:hilt-navigation-compose`artifact provides APIs that allow users to get a`@HiltViewModel`annotated ViewModel from a Navigation back stack entry within a Compose application using`:navigation-compose`.

The function`hiltViewModel()`returns an existing`ViewModel`or creates a new one scoped to the current navigation graph present on the`NavController`back stack. The function can optionally take a`NavBackStackEntry`to scope the`ViewModel`to a parent back stack entry.

### Version 1.0.0-rc01

December 15, 2021

`androidx.hilt:hilt-navigation-compose:1.0.0-rc01`is released with no changes since`1.0.0-beta01`.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..7e2685eebba0fdb40c93e3e06609bb01398a71a3/hilt/hilt-navigation-compose)

### Version 1.0.0-beta01

November 17, 2021

`androidx.hilt:hilt-navigation-compose:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..cc1240d00b28657ee0c1a937f60430eaf1b03b09/hilt/hilt-navigation-compose)

**API Changes**

- Remove deprecated`hiltNavGraphViewModel()`function and its overloads. These were all replaced by`hiltViewModel()`. ([Iaf7d7](https://android-review.googlesource.com/#/q/Iaf7d7994d709047fac03b6fd8bf20eff94ab2fa3))

### Version 1.0.0-alpha03

June 16, 2021

`androidx.hilt:hilt-navigation-compose:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..f434dccf3dc4d4e82d8d965da3746615870537b4/hilt/hilt-navigation-compose)

**API Changes**

- The`hiltViewModel()`method now aligns with the`viewModel()`API changes in[Lifecycle-ViewModel-Compose`1.0.0-alpha07`](https://developer.android.com/jetpack/androidx/releases/lifecycle#lifecycle-viewmodel-compose-1.0.0-alpha07)and now takes an optional`ViewModelStoreOwner`parameter, rather than having a no argument version and one that takes only a`NavBackStackEntry`. This allows you to continue to use`hiltViewModel()`to access the default owner provided by`LocalViewModelStoreOwner`or use`hiltViewModel(navBackStackEntry)`or another`ViewModelStoreOwner`to specify any specific owner. ([I2628d](https://android-review.googlesource.com/#/q/I2628d27791bfeb8a0d2f45b0fa8e9e72cb00c34b))

### Version 1.0.0-alpha02

May 18, 2021

`androidx.hilt:hilt-navigation-compose:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..66681ad83c328d0dd821b943bb3d375f02c1db61/hilt/hilt-navigation-compose)

**API Changes**

- Renamed`hiltNavGraphViewModel()`to`hiltViewModel()`and removed the extension on`NavController`since a user can directly use the`navigation-compose`API for getting a`NavBackStackEntry`from a route. ([I6ef57](https://android-review.googlesource.com/#/q/I6ef57a195f43a7cc7d9d7d56837778534b02121a))

**Compose Compatibility**

- `androidx.hilt:hilt-navigation-compose:1.0.0-alpha02`is only compatible with Compose version`1.0.0-beta07`and above.

**Dependency updates**

- `hilt-navigation-compose`now depends on[Navigation`2.4.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.4.0-alpha01).

### Version 1.0.0-alpha01

March 10, 2021

`androidx.hilt:hilt-navigation-compose:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51/hilt/hilt-navigation-compose)

**New Features**

- The`:hilt-navigation-compose`artifact provides APIs that allow users to get a`@HiltViewModel`annotated`ViewModel`from a Navigation back stack entry within a Compose application using`:navigation-compose`. The function`hiltNavGraphViewModel()`can either take a`NavBackStackEntry`or a 'route' string that can be used to scope the`ViewModel`to either the current back stack entry or to a parent entry in the stack. ([Ia9234](https://android-review.googlesource.com/#/q/Ia92343c281823099390b2e1795b89cdb1abfc440))

## Hilt Version 1.1

### Version 1.1.0-beta01

October 4, 2023

`androidx.hilt:hilt-*:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..1f7407d4293384a1b91bc142880e3525048b3443/hilt)

`androidx.hilt:hilt-*:1.1.0-beta01`is released with no changes since`1.1.0-alpha*`.

## Hilt Version 1.0.0

### Version 1.0.0

May 5, 2021

`androidx.hilt:hilt-*:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..661b67017024a998cb20270523ec049edbc33dde/hilt)

**Major features of 1.0.0**

The`androidx.hilt`artifacts offers extensions for integrating[Hilt](https://dagger.dev/hilt/)with various other AndroidX libraries, such as WorkManager and Navigation. To see a list of features and examples check out[the integration documentation](https://developer.android.com/training/dependency-injection/hilt-jetpack).

### Version 1.0.0-beta01

March 10, 2021

`androidx.hilt:hilt-*:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/hilt)

**API Changes**

- Remove`@Deprecated`types from the AndroidX Hilt artifacts, specifically`@androidx.hilt.ViewModelInject`and`@androidx.hilt.Assisted`. Note that`@ViewModelInject`was replaced by[@HiltViewModel](https://dagger.dev/hilt/view-model). ([I626fe](https://android-review.googlesource.com/#/q/I626fede2d170649f874fc0e6ac110ca0abc1aa16))

### Version 1.0.0-alpha03

January 27, 2021

`androidx.hilt:hilt-*:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..aee18b103203a91ee89df91f0af5df2ecff356d6/hilt)

**New Features**

- Provide APIs for retrieving`@HiltViewModel`annotated ViewModel from a Navigation`NavBackStackEntry`. The artifact`hilt-navigation-fragment`offers a`hiltNavGraphViewModels`Kotlin extension while`hilt-navigation`exposes a`HiltViewModelFactory`factory method that takes in a`NavBackStackEntry`as argument and returns a`ViewModelProvider.Facctory`that can be used with`ViewModelProvider`or other View Model retrieving APIs, such as Compose's`viewModel()`function:`viewModel(HiltViewModelFactory(AmbientContext.current, backStackEntry))`. ([I00e67](https://android-review.googlesource.com/#/q/I00e675363f5af3922205a30f4670a4c33877a7b3))

**API Changes**

- Replace`@WorkerInject`with`@HiltWorker`.`@HiltWorker`is now a type annotation and requires the usage of @AssistedInject in the constructor. ([Ic2f15](https://android-review.googlesource.com/#/q/Ic2f15c63880a02ed082e9205fcad7acdb2b38751))
- Deprecate`@ViewModelInject`. Equivalent functionality is now offered by`@HiltViewModel`, which is now part of the core Hilt Android APIs. ([I36a41](https://android-review.googlesource.com/#/q/I36a41e8fccf38c6e98fff4c00e7bb55cae824fd9))

**Bug Fixes**

- Fix an issue where AndroidX Hilt extension Modules would not get correctly picked up by Hilt causing Workers to not be available for creation. ([I3181c](https://android-review.googlesource.com/#/q/I3181c8aad0973d15d82661b48404f2eeeb7ef954),[b/159540434](https://issuetracker.google.com/issues/159540434))
- Migrate AndroidX Hilt extensions to the`SingletonComponent`, removing the deprecated warning of using`ApplicationCompoonent`. ([I9c916](https://android-review.googlesource.com/#/q/I9c9162e175bad46c56a48c9889ace813550e4f8a),[b/175849092](https://issuetracker.google.com/issues/175849092))

### Version 1.0.0-alpha02

July 22, 2020

`androidx.hilt:hilt-*:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..9f60cc700129e30cee9df020005c317fb39d32ec/hilt)

**Bug Fixes**

- Fixed an issue of duplicate saved state keys when a non-Hilt injected ViewModel was requested from an`@AndroidEntryPoint`-annotated class. ([b/158737069](https://issuetracker.google.com/158737069))
- Fixed an issue in`HiltWorkerFactory`where it wouldn't correctly initialize nested Worker classes annotated with`@WorkerInject`. ([b/160524718](https://issuetracker.google.com/160524718))

### Version 1.0.0-alpha01

June 10, 2020

`androidx.hilt:hilt-*:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e/hilt)

The`androidx.hilt`package and libraries extend the functionality of[Dagger Hilt](https://dagger.dev/hilt)to enable dependency injection of certain classes from the androidx libraries.