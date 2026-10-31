---
title: Feature flags and Canary mode  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/flags
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Feature flags and Canary mode Stay organized with collections Save and categorize content based on your preferences.





Media3 introduces new optimizations, behavioral improvements, and architectural
enhancements across its libraries. While these changes are thoroughly tested and
verified before release, Media3 includes a centralized feature flags
infrastructure (`androidx.media3.common.Flags`) centered around **Canary mode**
to give applications control over how and when new behaviors are adopted.

This page explains how Canary mode and feature flags work, and how you can use
them in your application to reduce upgrade risks across releases, run
controlled rollouts, and configure emergency rollbacks.

## Overview

Canary mode groups newly introduced, verified library improvements under a
unified, global toggle:

* **Enabled by default**: In standard Media3 releases, Canary mode is enabled
  by default (`true`). This ensures your app automatically benefits from safe
  performance enhancements, optimizations, and new capabilities.
* **Opt-out and rollback capability**: Applications can disable Canary mode
  globally or override specific feature flags individually at runtime.
* **Zero wiring complexity**: Flags are managed through the central
  [`Flags`](/reference/androidx/media3/common/Flags) class in the `common` module, eliminating the need for
  bespoke setters or configuration objects across different components.

## Why use Flags in your app?

While Canary mode is active by default, integrating [`Flags`](/reference/androidx/media3/common/Flags) with
your app's configuration or experimentation framework provides several
benefits:

### 1. Mitigating version upgrade risk

Upgrading major or minor library versions in production can introduce unexpected
interactions on specific OEM devices or custom media pipelines. When updating
Media3, you can use Canary mode and remote configuration for a safer upgrade
flow across releases:

1. **Ship the update with Canary mode disabled**: Releasing a new Media3
   version with Canary mode turned off roughly preserves the feature set of the
   previous release (with Canary enabled), letting you verify baseline library
   stability and general bug fixes in production before adopting new behaviors.
2. **Progressively enable Canary mode**: Use remote configuration to enable
   Canary mode in stages across user cohorts (for example, 5% → 25% →
   100%) or run A/B experiments to measure metric impact.
3. **Roll back if needed**: If a regression occurs on specific devices,
   remotely disable Canary mode or the specific flag ID without requiring an
   emergency app release.
4. **Adopt as default**: Once verified, leave Canary mode enabled by default
   until the next version upgrade, where previously verified Canary features
   become permanent.

### Kotlin

```
// Enable or disable Canary mode globally (defaults to true).
Flags.setCanaryModeEnabled(false)

ExperimentalFlags.kt
```

### Java

```
// Enable or disable Canary mode globally (defaults to true).
Flags.setCanaryModeEnabled(false);

ExperimentalFlags.java
```

### 2. Controlled staged releases and A/B testing

Rather than exposing 100% of your users to new library behaviors at once, you
can wire [`Flags`](/reference/androidx/media3/common/Flags) to a remote configuration or experimentation
system.

You can enable Canary mode in stages (for example, 5% of users → 25%
→ 100%) or run A/B experiments to measure the impact of new optimizations
on core playback metrics such as startup latency, rebuffer rate, and playback
failures.

### 3. Remote kill switch and rapid rollback

If a regression occurs in production on a particular device model or OS version,
you can remotely disable Canary mode (or the specific flag ID responsible) using
server-side configuration. This immediately reverts the library to its stable,
legacy fallback behavior for affected users without requiring an emergency app
hotfix or binary release.

## Configuring Canary mode and flags

The [`Flags`](/reference/androidx/media3/common/Flags) API provides methods to control global Canary mode and
individual flag overrides.

### Global Canary mode

To enable or disable all enhancements covered by Canary mode:

### Kotlin

```
// Enable or disable Canary mode globally (defaults to true).
Flags.setCanaryModeEnabled(false)

ExperimentalFlags.kt
```

### Java

```
// Enable or disable Canary mode globally (defaults to true).
Flags.setCanaryModeEnabled(false);

ExperimentalFlags.java
```

### Overriding individual flags

You can also explicitly enable or disable specific flags independently of the
global Canary mode setting:

### Kotlin

```
// Explicitly enable an experimental flag.
Flags.enableFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION)

// Explicitly disable a flag.
Flags.disableFlag(Flags.FLAG_DYNAMIC_SCHEDULING)

ExperimentalFlags.kt
```

### Java

```
// Explicitly enable an experimental flag.
Flags.enableFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION);

// Explicitly disable a flag.
Flags.disableFlag(Flags.FLAG_DYNAMIC_SCHEDULING);

ExperimentalFlags.java
```

Explicit overrides always take precedence over the global Canary mode default.

### Checking flag status

To check whether Canary mode or a specific flag is active in your code:

### Kotlin

```
// Query whether Canary mode is active globally.
val isCanaryActive = Flags.isCanaryModeEnabled()

// Query whether a specific flag is active.
val isFeatureActive = Flags.isEnabled(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION)

ExperimentalFlags.kt
```

### Java

```
// Query whether Canary mode is active globally.
boolean isCanaryActive = Flags.isCanaryModeEnabled();

// Query whether a specific flag is active.
boolean isFeatureActive = Flags.isEnabled(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION);

ExperimentalFlags.java
```

### Flag resolution order

When Media3 checks whether a feature is enabled at runtime, it resolves the
state in the following order:

1. **Explicit runtime override**: If [`enableFlag`](/reference/androidx/media3/common/Flags#enableFlag(int)) or
   [`disableFlag`](/reference/androidx/media3/common/Flags#disableFlag(int)) was called for the flag ID, that override
   value is returned.
2. **Static library state**: If the flag is statically disabled (for example,
   an early development feature not yet ready for Canary mode) or statically
   enabled (a feature graduated from Canary mode retaining a temporary opt-out
   fallback), that static value is returned.
3. **Canary mode state**: Otherwise, the flag follows the global Canary mode
   setting (enabled if Canary mode is `true`, disabled if `false`).

## Initialization requirements

Configure flags **before** instantiating any Media3 components (such as
`ExoPlayer`, `Transformer`, or `MediaSession`):

* **Early setup**: Configure [`Flags`](/reference/androidx/media3/common/Flags) during application startup
  (for example, inside `Application.onCreate`) or before initializing your
  app's media layer.
* **Thread safety**: Media3 components read flags during instantiation and
  propagate those values to internal playback and processing threads. Ensure
  that flag configuration happens before creating Media3 components. Modifying
  flags while players or transformers are actively running is not supported.

## Integrating with remote configuration

A recommended architecture is to expose three parameters in your remote
configuration platform:

* `media3_canary_mode_enabled` (Boolean): Global toggle for Canary mode
  (defaults to `true`).
* `media3_force_enable_flags` (List of Integers): Specific flag IDs to
  force-enable for targeted trials.
* `media3_force_disable_flags` (List of Integers): Specific flag IDs to
  force-disable if an issue is discovered.

Apply these values during startup before creating player instances:

### Kotlin

```
fun initializeMedia3Flags(
  canaryModeEnabled: Boolean,
  forceEnabledFlags: List<Int>,
  forceDisabledFlags: List<Int>,
) {
  // 1. Set global Canary mode state.
  Flags.setCanaryModeEnabled(canaryModeEnabled)

  // 2. Apply explicit force-enable overrides.
  for (flagId in forceEnabledFlags) {
    Flags.enableFlag(flagId)
  }

  // 3. Apply explicit force-disable overrides (remote kill switch).
  for (flagId in forceDisabledFlags) {
    Flags.disableFlag(flagId)
  }
}

ExperimentalFlags.kt
```

### Java

```
public static void initializeMedia3Flags(
    boolean canaryModeEnabled,
    List<Integer> forceEnabledFlags,
    List<Integer> forceDisabledFlags) {
  // 1. Set global Canary mode state.
  Flags.setCanaryModeEnabled(canaryModeEnabled);

  // 2. Apply explicit force-enable overrides.
  for (int flagId : forceEnabledFlags) {
    Flags.enableFlag(flagId);
  }

  // 3. Apply explicit force-disable overrides (remote kill switch).
  for (int flagId : forceDisabledFlags) {
    Flags.disableFlag(flagId);
  }
}

ExperimentalFlags.java
```

## Testing with flags

When writing unit tests or Robolectric tests for code paths affected by feature
flags, use `androidx.media3.test.utils.Media3FlagsRule` (available in the
`media3-test-utils` module) to ensure tests don't pollute each other's static
state.

### Automatic cleanup with Media3FlagsRule

Adding `Media3FlagsRule` ensures that all flag overrides and Canary mode
modifications are automatically reset after each test:

### Kotlin

```
class MyPlayerTest {

  @get:Rule val flagsRule = Media3FlagsRule(this)

  @Test
  fun playback_withFeatureFlagEnabled() {
    Flags.enableFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION)
    // Run test with the flag enabled...
  }
}

ExperimentalFlags.kt
```

### Java

```
public static class MyPlayerTest {

  @Rule public final Media3FlagsRule flagsRule = new Media3FlagsRule(this);

  @Test
  public void playback_withFeatureFlagEnabled() {
    Flags.enableFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION);
    // Run test with the flag enabled...
  }
}

ExperimentalFlags.java
```

### Parameterized testing

You can combine `Media3FlagsRule` with `@BindFlag` and `@BindCanaryMode`
annotations to run parameterized tests across flag states:

### Kotlin

```
class MyParameterizedPlayerTest {

  @BindCanaryMode var canaryMode: Boolean = false

  @BindFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION) var perStreamProgression: Boolean = false

  @get:Rule val flagsRule = Media3FlagsRule(this)

  @Test
  fun playback() {
    // Flags are automatically set for each test parameter combination.
  }
}

ExperimentalFlags.kt
```

### Java

```
public static class MyParameterizedPlayerTest {

  @BindCanaryMode public boolean canaryMode;

  @BindFlag(Flags.FLAG_PER_STREAM_MEDIA_PROGRESSION)
  public boolean perStreamProgression;

  @Rule public final Media3FlagsRule flagsRule = new Media3FlagsRule(this);

  @Test
  public void playback() {
    // Flags are automatically set for each test parameter combination.
  }
}

ExperimentalFlags.java
```

## Diagnostics and logging

Media3 provides diagnostic tools to verify active flags and Canary mode states
during playback initialization and at runtime.

### Initialization logs

When an `ExoPlayer` instance is initialized, it prints the active Canary state
and any explicit overrides to logcat alongside the library version:

```
ExoPlayerImpl: Init 59a18ab [AndroidXMedia3/1.10.1] [flame, Pixel 4, Google, 33] [Canary:ON]
```

If overrides are active, only the deviations from the default state are listed:

```
ExoPlayerImpl: Init 59a18ab [AndroidXMedia3/1.10.1] [flame, Pixel 4, Google, 33] [Canary:ON, Overrides: enabled=[1], disabled=[3]]
```

### Programmatic inspection

You can retrieve the formatted diagnostics string or query override lists
programmatically (for example, to include flag state in your app's crash reports
or analytics):

### Kotlin

```
// Get formatted string representing active Canary state and overrides.
val flagLogString = Flags.getLogString()

// Query explicit override IDs if needed.
val enabledFlags = Flags.getEnabledOverrides()
val disabledFlags = Flags.getDisabledOverrides()

ExperimentalFlags.kt
```

### Java

```
// Get formatted string representing active Canary state and overrides.
String flagLogString = Flags.getLogString();

// Query explicit override IDs if needed.
int[] enabledFlags = Flags.getEnabledOverrides();
int[] disabledFlags = Flags.getDisabledOverrides();

ExperimentalFlags.java
```

## Flag lifecycle

Flags in Media3 are designed to be **temporary**:

1. **Development**: A new optimization or feature is added behind a flag ID in
   `Flags.java`.
2. **Canary mode**: Once verified and ready for general use, the feature is
   active under Canary mode across releases.
3. **Promotion & Cleanup**: After a soak period proving stability in
   production, the feature is promoted to permanently enabled in the library,
   and the flag constant, fallback code paths, and conditional checks are
   removed.

If you encounter an issue with a feature flag, please file a report on the
[AndroidX Media3 GitHub issue tracker](https://github.com/androidx/media/issues) so the team can address it
before permanent promotion.