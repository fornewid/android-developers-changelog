---
title: https://developer.android.com/jetpack/androidx/releases/tracing
url: https://developer.android.com/jetpack/androidx/releases/tracing
source: md.txt
---

# Tracing

API Reference  
[androidx.tracing](https://developer.android.com/reference/kotlin/androidx/tracing/package-summary)  
Write trace events to the system trace buffer.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/tracing#1.3.0) | - | - | [2.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/tracing#2.0.0-alpha01) |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:898851+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=898851&template=1458540)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 2.0

### Version 2.0.0-alpha01

January 28, 2026

`androidx.tracing:tracing-*:2.0.0-alpha01` is released. Version 2.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/120ca6e0a3f4f240334c74efe9f9da0038522135..715e22619094effc2ba1fd528cd9a07b1f5d0046/tracing).

**New Features**

AndroidX Tracing 2.0 introduces a significant new API surface for low-overhead, in-process tracing, as a complement to the existing `android.os.Tracing`-based APIs in Tracing 1.0. The new APIs are available both on Android and host JVM, which enables host tools to emit low overhead traces for performance analysis, using the same standard Perfetto trace format.

Emitted traces are supported both by Android Studio and Perfetto, and can be recorded with an expanded feature set including tagging slices with metadata (such as function arguments!), and coroutine context trace propagation.

This initial alpha is only meant for in-process tracing workflows, and does not yet integrate with Android OS tracing or Studio Profiler System Tracing - these will be coming in a future alpha.

      /**
      * A [TraceSink] defines how traces are serialized.
      *
      * [androidx.tracing.wire.TraceSink] uses the `Perfetto` trace packet format.
      */
      fun createSink(): TraceSink {
          val outputDirectory = File(/* pathname = */ "/tmp/perfetto")
          // We are using the factory function defined in androidx.tracing.wire
          return TraceSink(
              sequenceId = 1,
              directory = outputDirectory
          )
      }

      /**
      * Creates a new instance of [androidx.tracing.TraceDriver].
      */
      fun createTraceDriver(): TraceDriver {
          // We are using a factory function from androidx.tracing.wire here.
          // `isEnabled` controls whether tracing is enabled for the application.
          val driver = TraceDriver(sink = createSink(), isEnabled = true)
          return driver
      }

      fun main() {
          val driver = createTraceDriver()
          driver.use {
              driver.tracer.trace(category = CATEGORY_MAIN, name = "basic") {
                  Thread.sleep(100L)
              }
          }
      }

**API Changes**

- Make `Tracer` a property of the `TraceDriver`. ([Iabd9b](https://android-review.googlesource.com/#/q/Iabd9ba2480899caead685ac8de6eb5bda9acbcf5))
- Add support for manual context propagation. ([I899ff](https://android-review.googlesource.com/#/q/I899ff885093bc3e8f833f7bce9dad0b6fcff4f22))
- Add the ability to add call stack information in a trace section. ([If6a1b](https://android-review.googlesource.com/#/q/If6a1bb6e42067edb07407f50f3b21f76f92050d5))
- Introduce the new `androidx.tracing` APIs. ([I5102b](https://android-review.googlesource.com/#/q/I5102b729b491fc5e1504cd35e3f2ec36ae7e956c))
- Allow instant events to contain metadata, and add counters to instants \& counters. ([Ia2ed3](https://android-review.googlesource.com/#/q/Ia2ed354e4d089af676f2a1afb4bb91a0240d291c))
- Reduce the surface area of the API annotated with `@DelicateTracingApi`. Nothing in the top level API should require the use of `@DelicateTracingApi`. ([I565e0](https://android-review.googlesource.com/#/q/I565e0af46c42ce679c9bc519bb1dad9abb51aba4))
- Simplify context propagation by unifying `PropagationToken`s. ([Iab839](https://android-review.googlesource.com/#/q/Iab83943fadb3f1be4daad0ae2df73d1237bfcec0))
- Stabilize `BlackHole` APIs in `androidx.benchmark`. ([I2b67e](https://android-review.googlesource.com/#/q/I2b67e946c722511244434954a53e9b2f06b631db), [b/451749438](https://issuetracker.google.com/issues/451749438))
- Add the ability to annotate the trace section as a root span. ([Ic8365](https://android-review.googlesource.com/#/q/Ic836578e5a3804a1b1d556e2471ba20038331394))
- Allow the developer to explicit about propagation tokens. ([I06bb1](https://android-review.googlesource.com/#/q/I06bb1f7fc5325729bfb57fc64b252b0e99a35a1c))
- Renamed `MetadataHandleCloseable` to `EventMetadataCloseable`, and `MetadataHandle` to `EventMetadata`. Also added an optional `CoroutinePropagationToken` argument to `Tracer.traceCoroutine` to allow the developer to explicitly specify the propagation token to use. ([I219f7](https://android-review.googlesource.com/#/q/I219f7c761508f9684501cbfe2d647b01a771846c), [b/454147392](https://issuetracker.google.com/issues/454147392))
- Introduced a new `Tracer` entry point which gives developers a lot more control on how to trace. ([I24a7b](https://android-review.googlesource.com/#/q/I24a7beebedc49000a9692fb8f261c9bb52e6b8b6))
- Add the ability to control how context propagation happens in a `SliceTrack`. ([Ieb8fc](https://android-review.googlesource.com/#/q/Ieb8fc64f524236d7e1ae7f66e90f6943e7cd1e89))
- `fillCount` in `PooledTracePacketArray` is now correctly marked volatile. ([I75d2c](https://android-review.googlesource.com/#/q/I75d2c61941fff6b1c63aef5093052d32ce17ac74))
- Mark `MetadataEntry` `@DelicateTracingApi`. ([I8c723](https://android-review.googlesource.com/#/q/I8c723b68800f7d935d0f9f00290257be7a6e933a))
- Add the ability for a `TraceSink` to be able to handle lost trace events (when the pool is exhausted). ([I3b374](https://android-review.googlesource.com/#/q/I3b374096285623722e234ae41294f92ed98c6766))
- Add the ability to conditionally emit trace events based on a predicate. ([I621b4](https://android-review.googlesource.com/#/q/I621b4bfc7f92543860287d68f3db9d61d1e7fb1e))
- Add the ability to add categories to a trace event. ([I449c2](https://android-review.googlesource.com/#/q/I449c20d2db21cb97872542d1645f8315ba73bcf1))
- Mark `TraceEvent`, `PooledTracePacketArray` as `DelicateTracingApi`. ([Iaac6d](https://android-review.googlesource.com/#/q/Iaac6d4636f8279cc4f1fb7ad45ea5844eea6061c))
- Make `ProcessTrack.id`, `ThreadTrack.id`, `ThreadTrack.name`, `CounterTrack.name` and `CounterTrack.parent` public. ([I81210](https://android-review.googlesource.com/#/q/I8121061710c8068c60beabad6aca5302a11723e2))
- Renamed the `SliceTrack.traceFlow()` API to `traceCoroutine()`. ([I79ad0](https://android-review.googlesource.com/#/q/I79ad05e8bad90e629d9c9d6706d874ef1066e371))
- Add the ability to add contextual information to slices via debug annotations in a Perfetto trace. ([Ic2b56](https://android-review.googlesource.com/#/q/Ic2b563d405a62139cadaefcb3a20de0e26512712))
- Make it possible to construct an instance of `WireTraceSink` with a `File` / `OutputStream`. ([Iecea0](https://android-review.googlesource.com/#/q/Iecea0d0f72b8a31ca68dd1c6d046bd06249cae94))
- Removing obsolete `@RequiresApi(21)` annotations ([Ic4792](https://android-review.googlesource.com/#/q/Ic47923dcc82f4b7c4638fadb10c2c0268b414fcd))

## Version 1.3

### Version 1.3.0

April 23, 2025

`androidx.tracing:tracing:1.3.0`, `androidx.tracing:tracing-android:1.3.0`, and `androidx.tracing:tracing-ktx:1.3.0` are released. Version 1.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9eda98421361ea345fb9c84976278706ca6e84ac..120ca6e0a3f4f240334c74efe9f9da0038522135/tracing).

**Important changes since 1.2.0**

- Converted `androidx.tracing.Trace` class to Kotlin, and moved all code from the `tracing-ktx`module to `tracing`.
- Remove crossinline from trace to allow using in a `@Composable`. ([I53882](https://android-review.googlesource.com/#/q/I53882249cba8931140b96291457d8e99abe22633), [b/248344805](https://issuetracker.google.com/issues/248344805))

### Version 1.3.0-rc01

April 9, 2025

`androidx.tracing:tracing:1.3.0-rc01`, `androidx.tracing:tracing-android:1.3.0-rc01`, and `androidx.tracing:tracing-ktx:1.3.0-rc01` are released with no changes since the last beta. Version 1.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c7c2a80dc6576c43cb049b40c7c250b6cbf34f4e..9eda98421361ea345fb9c84976278706ca6e84ac/tracing).

### Version 1.3.0-beta01

February 12, 2025

`androidx.tracing:tracing:1.3.0-beta01`, `androidx.tracing:tracing-android:1.3.0-beta01`, and `androidx.tracing:tracing-ktx:1.3.0-beta01` are released. Version 1.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..c7c2a80dc6576c43cb049b40c7c250b6cbf34f4e/tracing).

**API Changes**

- Moved all the code from the `tracing-ktx` module to `tracing`. ([Iba550](https://android-review.googlesource.com/#/q/Iba5500788da397b3afd68f9e76bc3eed54317cdc))
- Converted `androidx.tracing.Trace` class to Kotlin. ([Ie4e5d](https://android-review.googlesource.com/#/q/Ie4e5d971959c6615021521c03214bc00059cb171))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.3.0-alpha02

June 21, 2023

`androidx.tracing:tracing:1.3.0-alpha02` and `androidx.tracing:tracing-ktx:1.3.0-alpha02` are released with no changes from previous alpha. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8423c3f497cfbf2bf7b87006ca05f38626060135..3b5b931546a48163444a9eddc533489fcddd7494/tracing)

### Version 1.3.0-alpha01

June 7, 2023

`androidx.tracing:tracing:1.3.0-alpha01` and `androidx.tracing:tracing-ktx:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0ad460fe9733c0fa6a69a1be92d3e8450287fa5e..8423c3f497cfbf2bf7b87006ca05f38626060135/tracing)

**API Changes**

- Remove crossinline from trace to allow using in a `@Composable`. ([I53882](https://android-review.googlesource.com/#/q/I53882249cba8931140b96291457d8e99abe22633), [b/248344805](https://issuetracker.google.com/issues/248344805))

## Version 1.2

### Version 1.2.0

November 29, 2023

`androidx.tracing:tracing:1.2.0` and `androidx.tracing:tracing-ktx:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0ad460fe9733c0fa6a69a1be92d3e8450287fa5e..538750227118fd2cca14f4de7df81bace1f50dd3/tracing)

**Important changes since 1.1.0**

- Add `trace()` and `traceAsync()` variants with lazy string and cookie computation. Also now correctly skips `Trace.end` if `Trace.begin` throws.

### Version 1.2.0-rc01

May 24, 2023

`androidx.tracing:tracing:1.2.0-rc01` and `androidx.tracing:tracing-ktx:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..0ad460fe9733c0fa6a69a1be92d3e8450287fa5e/tracing)

**Bug Fixes**

- Prevent crashes when long trace section names are passed by truncating automatically ([Iaf6e2](https://android-review.googlesource.com/#/q/Iaf6e2f42c56326ca99faff21e3efee86fc047953))

### Version 1.2.0-beta04

May 3, 2023

`androidx.tracing:tracing:1.2.0-beta04` and `androidx.tracing:tracing-ktx:1.2.0-beta04` are released with no changes. [Version 1.2.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/tracing)

### Version 1.2.0-beta03

April 5, 2023

`androidx.tracing:tracing:1.2.0-beta03` and `androidx.tracing:tracing-ktx:1.2.0-beta03` are released with no new changes. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/tracing)

### Version 1.2.0-beta02

March 22, 2023

`androidx.tracing:tracing:1.2.0-beta02` and `androidx.tracing:tracing-ktx:1.2.0-beta02` are released with no changes since the previous beta. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..5e7d256f82fbafb6d059ab7b18fddd87c7531553/tracing)

### Version 1.2.0-beta01

March 8, 2023

`androidx.tracing:tracing:1.2.0-beta01` and `androidx.tracing:tracing-ktx:1.2.0-beta01` are released with no changes since the last alpha. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/tracing)

### Version 1.2.0-alpha02

February 23, 2023

`androidx.tracing:tracing:1.2.0-alpha02` and `androidx.tracing:tracing-ktx:1.2.0-alpha02` are released with no changes from the previous alpha. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..87533b4ff06971ed59028936cd9b6da988cd4522/tracing)

**Bug Fixes**

- This release will fix a `Could not find androidx.tracing:tracing-ktx:1.2.0-alpha02` error when upgrading to `androidx.tracing: tracing-perfetto-common:1.0.0-alpha11`

### Version 1.2.0-alpha01

October 5, 2022

`androidx.tracing:tracing:1.2.0-alpha01` and `androidx.tracing:tracing-ktx:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5a2dccfbef0b52c47755962fc15ca98d378565de..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/tracing)

**New Features**

- Add `trace()` and `traceAsync()` variants with lazy string and cookie computation. Also now correctly skips `Trace.end` if `Trace.begin` throws. ([I31421](https://android-review.googlesource.com/#/q/I314210e79d91f7e71140208c61c8672591aef88b), [b/175233952](https://issuetracker.google.com/issues/175233952), [b/247066503](https://issuetracker.google.com/issues/247066503))

## Tracing Version 1.1

### Version 1.1.0

May 11, 2022

`androidx.tracing:tracing:1.1.0` and `androidx.tracing:tracing-ktx:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5954e1f49c8e5ba7511565c978c6c08df7df2cd..5a2dccfbef0b52c47755962fc15ca98d378565de/tracing)

**Important changes since 1.0.0**

- Added `Trace.forceEnableAppTracing()` an API to force-enable app trace section capture (i.e. android.os.Trace / androidx.tracing APIs) on non-debuggable builds. Call this at the beginning of startup to enable non-debuggable accurate system tracing before the introduction of the [profileable manifest tag](https://developer.android.com/guide/topics/manifest/profileable-element) in API 29. ([I3a309](https://android-review.googlesource.com/#/q/I3a30949580d8db6777302a759b041f9480e04e72))
- Avoid class verification errors when Trace.java is loaded for the first time ([05f6b4](https://android.googlesource.com/platform/frameworks/support/+/b19fac01b2a7f4d55ca777397c5719892905f6b4) and [cb101f](https://android.googlesource.com/platform/frameworks/support/+/4474e187d25886eca264463b7c834c5353cb101f))

### Version 1.1.0-rc01

April 20, 2022

`androidx.tracing:tracing:1.1.0-rc01` and `androidx.tracing:tracing-ktx:1.1.0-rc01` are released, with no changes since `beta01`. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..b5954e1f49c8e5ba7511565c978c6c08df7df2cd/tracing)

### Version 1.1.0-beta01

December 1, 2021

`androidx.tracing:tracing:1.1.0-beta01` and `androidx.tracing:tracing-ktx:1.1.0-beta01` are released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..75784ce6dbac6faa5320e5898e9472f02ab8710c/tracing)

No changes since `1.1.0-alpha02`.

### Version 1.1.0-alpha02

November 17, 2021

`androidx.tracing:tracing:1.1.0-alpha02` and `androidx.tracing:tracing-ktx:1.1.0-alpha02` are released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/tracing)

**New Features**

- Added Trace.forceEnableAppTracing() an API to force-enable app trace section capture (i.e. android.os.Trace / andoridx.tracing APIs) on non-debuggable builds. Call this at the beginning of startup to enable non-debuggable accurate system tracing before the introduction of the profileable manifest tag in API 29. ([I3a309](https://android-review.googlesource.com/#/q/I3a30949580d8db6777302a759b041f9480e04e72))

### Version 1.1.0-alpha01

November 3, 2021

`androidx.tracing:tracing:1.1.0-alpha01` and `androidx.tracing:tracing-ktx:1.1.0-alpha01` are released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2a518b53bb3172e4945cba723ae628e9c18bcd23..f07d12061370a603549747200c79b60239706330/tracing)

**Bug Fixes**

- Avoid class verification errors when Trace.java is loaded for the first time ([05f6b4](https://android.googlesource.com/platform/frameworks/support/+/b19fac01b2a7f4d55ca777397c5719892905f6b4) and [cb101f](https://android.googlesource.com/platform/frameworks/support/+/4474e187d25886eca264463b7c834c5353cb101f))

## Tracing Perfetto Version 1.0.0

### Version 1.0.1

November 19, 2025

`androidx.tracing:tracing-perfetto:1.0.1`, `androidx.tracing:tracing-perfetto-binary:1.0.1`, and `androidx.tracing:tracing-perfetto-handshake:1.0.1` are released. Version 1.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/120ca6e0a3f4f240334c74efe9f9da0038522135..262b8e77a141e4b20a5656688137c1a1a89492b0/tracing).

**Bug Fixes**

- Support for 16KB page sizes ([b7a7dd](https://android.googlesource.com/platform/frameworks/support/+/f42a711fe12a08550d75e8ca3bb6d6834db7a7dd))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))
- Avoid bundling copies of `FastNative/CriticalNative` in the library, and use the stable platform copies. ([I8238a](https://android-review.googlesource.com/#/q/I8238a3ec6e2f3563ee6262857e4978de1d176768), [b/35664282](https://issuetracker.google.com/issues/35664282), [b/280878596](https://issuetracker.google.com/issues/280878596))

### Version 1.0.0

October 4, 2023

`androidx.tracing:tracing-perfetto:1.0.0`, `androidx.tracing:tracing-perfetto-binary:1.0.0`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc9d0ceb0cf1daabde110d9965d3dd87319b575c..50f38fd7d07dfea1390b99c87a3760c8d9ef1df2/tracing)

**Major features of 1.0.0**

- This is the first stable release of the Tracing-perfetto libraries.

### Version 1.0.0-rc01

September 20, 2023

`androidx.tracing:tracing-perfetto:1.0.0-rc01`, `androidx.tracing:tracing-perfetto-binary:1.0.0-rc01`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0-rc01` are released with no changes since the last beta. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/119f68768b14c444b7ba65b4b44abd0ed7d21002..fc9d0ceb0cf1daabde110d9965d3dd87319b575c/tracing)

### Version 1.0.0-beta03

August 30, 2023

`androidx.tracing:tracing-perfetto:1.0.0-beta03`, `androidx.tracing:tracing-perfetto-binary:1.0.0-beta03`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0-beta03` are released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22eceaa7039e3fc1207b151f73e842c8021075f7..119f68768b14c444b7ba65b4b44abd0ed7d21002/)

- Version bump to match androidx.benchmark release.

### Version 1.0.0-beta02

August 23, 2023

`androidx.tracing:tracing-perfetto:1.0.0-beta02`, `androidx.tracing:tracing-perfetto-binary:1.0.0-beta02`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0-beta02` are released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c2c1745b1d05b772c7bbe82834a9197ba5b85114..22eceaa7039e3fc1207b151f73e842c8021075f7/tracing)

**New Features**

- Enabled support for tracing at app startup (cold start).

### Version 1.0.0-beta01

July 18, 2023

`androidx.tracing:tracing-perfetto:1.0.0-beta01`, `androidx.tracing:tracing-perfetto-binary:1.0.0-beta01`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0-beta01` are released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..c2c1745b1d05b772c7bbe82834a9197ba5b85114/tracing)

**API Changes**

- Renamed `androidx.tracing.perfetto.Trace` to `androidx.tracing.perfetto.PerfettoSdkTrace` ([I44af8](https://android-review.googlesource.com/#/q/I44af824893288c17c792369058132cca3ac61f1b))
- Renamed "exit code" to "result code" constants in the protocol for consistency ([Id1d1e](https://android-review.googlesource.com/#/q/Id1d1e87b1b461e0c6598a5c5425fa73054dcc3b7))
- Renamed `EnableTracingResponse` to `Response`. ([I56275](https://android-review.googlesource.com/#/q/I56275818234555399521f104067f83c6e34ac258))
- Added an option to enable cold start tracing in a persistent mode. Added a function to clear (persistent or not) cold start tracing. ([Iaa09d](https://android-review.googlesource.com/#/q/Iaa09d59477d4b8d3aa342422a8f6bcc12d866c5f))
- Made Tracing Perfetto SDK APIs consistent with `android.os.Trace`. ([I73ba0](https://android-review.googlesource.com/#/q/I73ba07ca6cc4bd2b6519553c395fe9075a49fe75), [b/282199917](https://issuetracker.google.com/issues/282199917))
- Moved to a factory pattern for `LibrarySource` allowing for future use-cases (e.g. loading the `.so` file directly) to be easily added to the API if needed. ([I128df](https://android-review.googlesource.com/#/q/I128df0728ce971ca2ed37c278b1bfe0cc2521982))
- Making `enableTracingColdStart` parameters match `enableTracingImmediate` ([I54126](https://android-review.googlesource.com/#/q/I541269228ee33cfc73fe53e64032ddd00d62997f))
- Removed `killProcess` argument in `enableTracingColdStart` ([I81c4d](https://android-review.googlesource.com/#/q/I81c4de80f211ad49bc46e6fe8255491850609252))

### Version 1.0.0-alpha17

June 21, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha17`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha17`, and `androidx.tracing:tracing-perfetto-handshake:1.0.0-alpha17` are released with no changes from previous alpha. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494/tracing)

### Version 1.0.0-alpha16

June 7, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha16`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha16`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha16` are released with no changes from previous alpha. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..8423c3f497cfbf2bf7b87006ca05f38626060135/tracing)

### Version 1.0.0-alpha15

May 3, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha15`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha15`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha15` are released with no changes. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/tracing)

### Version 1.0.0-alpha14

April 5, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha14`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha14`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha14` are released with no new changes. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/tracing)

### Version 1.0.0-alpha13

March 22, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha13`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha13`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha13` are released with no changes since the last release. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf83b7ca1e086138c9ffa3ed2a530db3b038c79a..5e7d256f82fbafb6d059ab7b18fddd87c7531553/tracing)

### Version 1.0.0-alpha12

March 8, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha12`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha12`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha12` are released with no changes since previous alpha. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..bf83b7ca1e086138c9ffa3ed2a530db3b038c79a/tracing)

### Version 1.0.0-alpha11

February 22, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha11`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha11`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha11` are released with no changes. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..87533b4ff06971ed59028936cd9b6da988cd4522/tracing)

### Version 1.0.0-alpha10

February 8, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha10`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha10` and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha10` are released with no changes. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..7d3ac1ab1206c01fae3ebb500b5b942636070155/tracing)

### Version 1.0.0-alpha09

February 10, 2023

`androidx.tracing:tracing-perfetto-binary:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..adf1c279a86ab3886e1666c08e2c3efba783367b/tracing/tracing-perfetto-binary)

**New Features**

- Version bump release to allow other `androidx.tracing:tracing-perfetto*: 1.0.0-alpha09` libraries to work together.

January 11, 2023

`androidx.tracing:tracing-perfetto:1.0.0-alpha09` and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha09` are released with no changes. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4a2f5e696614339c1ac21f706c1a17c0285780e7..adf1c279a86ab3886e1666c08e2c3efba783367b/tracing)

### Version 1.0.0-alpha08

December 7, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha08`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha08`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha08` are released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..4a2f5e696614339c1ac21f706c1a17c0285780e7/tracing)

**New Features**

- Improved performance by optimising the way strings are handled.

**Bug Fixes**

- Added a proguard rule preventing methods of `PerfettoNative` from being pruned if the class is used at all (prevents a crash in a niche case when tracing is initialised, but no tracing calls are present in the app).

### Version 1.0.0-alpha07

November 9, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha07`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha07`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha07` are released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ztac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/tracing)

- Reduced JNI overhead of `androidx.tracing:tracing-perfetto` APIs.

### Version 1.0.0-alpha06

October 24, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha06`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha06`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha06` are released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..548c8ac2570ae6cf15798fea1380491f7d93796b/tracing)

- This update includes no changes, just updating version number to sync with androidx.benchmark.

### Version 1.0.0-alpha05

October 5, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha05`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha05`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha05` are released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/tracing)

### Version 1.0.0-alpha04

September 21, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha04`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha04`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha04` are released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/tracing)

### Version 1.0.0-alpha03

September 7, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha03`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha03`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha03` are released.

**New Features**

- No new features from the 1.0.0-alpha02.

### Version 1.0.0-alpha02

August 24, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha02`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha02`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..dd1e45e8550560087f6447a34a9145048b5766f4/tracing)

**Bug Fixes**

- Several improvements to Perfetto service initialization
- Improved handling of a no-response case by introducing a dedicated exit code: RESULT_CODE_CANCELLED.
- Improved handling of parsing errors.
- Made `EnableTracingResponse.requiredVersion` nullable, as we cannot know the version if we cannot communicate with the package. ([I5ba20](https://android-review.googlesource.com/#/q/I5ba2094686f11fcd5f548b6b528e7699aafcba10))

### Version 1.0.0-alpha01

July 27, 2022

`androidx.tracing:tracing-perfetto:1.0.0-alpha01`, `androidx.tracing:tracing-perfetto-binary:1.0.0-alpha01`, and `androidx.tracing:tracing-perfetto-common:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/tracing)

- Note: All `androidx.tracing:tracing-perfetto*` libraries are **initially only intended for internal use inside AndroidX libraries.** You should have no need to depend on them directly.

**New Features**

- All `androidx.tracing:tracing-perfetto*` libraries are **initially only intended for internal use inside AndroidX libraries.** and you should have no need to depend on them directly. We are documenting these implementation details for transparency.

- `androidx.tracing:tracing-perfetto` is a library which helps write trace events using low-overhead Perfetto SDK. This can be used inside Benchmark, Android Studio or Perfetto UI.

- `androidx.tracing:tracing-perfetto-binary` is a set of binary dependencies required for androidx.tracing:tracing-perfetto.

- `androidx.tracing:tracing-perfetto-common` is an internal dependency of androidx.tracing:tracing-perfetto and can be used by tooling to integrate with androidx.tracing:tracing-perfetto.

## Tracing Version 1.0.0

### Version 1.0.0

October 28, 2020

`androidx.tracing:tracing:1.0.0` and `androidx.tracing:tracing-ktx:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b2995ba8dcdac5063b10225f6de18d766b19e609..2a518b53bb3172e4945cba723ae628e9c18bcd23/tracing)

**Major features of 1.0.0**

Helps write trace events to the system trace buffer. This can be visualized using tools like Systrace and Perfetto. This library replaces the deprecated `androidx.core.os.TraceCompat` class.

### Version 1.0.0-rc01

October 14, 2020

`androidx.tracing:tracing:1.0.0-rc01` and `androidx.tracing:tracing-ktx:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..b2995ba8dcdac5063b10225f6de18d766b19e609/tracing)

This release is identical to `1.0.0-beta01`.

### Version 1.0.0-beta01

June 24, 2020

`androidx.tracing:tracing:1.0.0-beta01` and `androidx.tracing:tracing-ktx:1.0.0-beta01` are released with no changes since `1.0.0-alpha01`. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/tracing)

### Version 1.0.0-alpha01

June 10, 2020

`androidx.tracing:tracing:1.0.0-alpha01` and `androidx.tracing:tracing-ktx:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e/tracing)

**New Features**

androidx.tracing is a library which helps write trace events to the system trace buffer. This can be visualized using tools like Systrace and Perfetto. This library replaces the deprecated [androidx.core.os.TraceCompat](https://developer.android.com/reference/kotlin/androidx/core/os/TraceCompat) class. This initial release is 1.0.0-alpha01.