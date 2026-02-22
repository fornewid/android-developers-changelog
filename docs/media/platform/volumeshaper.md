---
title: https://developer.android.com/media/platform/volumeshaper
url: https://developer.android.com/media/platform/volumeshaper
source: md.txt
---

# Controlling amplitude with VolumeShaper

You can use a[VolumeShaper](https://developer.android.com/reference/android/media/VolumeShaper)in an audio app to perform fade-ins, fade-outs, cross fades, ducking, and other short automated volume transitions. The`VolumeShaper`class is available in Android 8.0 (API level 26) and later.

You create a`VolumeShaper`by calling`createVolumeShaper()`on an instance of[AudioTrack](https://developer.android.com/reference/android/media/AudioTrack)or[MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer). The`VolumeShaper`only acts on the audio produced by the AudioTrack or MediaPlayer that created it.
| **Note:** On this page the term "shaper" refers to an instance of a`VolumeShaper`.

## VolumeShaper.Configuration

The behavior of a`VolumeShaper`is defined by its[VolumeShaper.Configuration](https://developer.android.com/reference/android/media/VolumeShaper.Configuration). The configuration specifies a \*volume curve, interpolator type,*and*duration.\*

### Volume curve

The volume curve represents amplitude change over time. It is defined by a pair of float arrays, x\[\] and y\[\] that define a series of control points. Each (x, y) pair represents time and volume respectively. The arrays must be of equal length and contain at least 2 and no more than 16 values. (The maximum curve length is defined in[getMaximumCurvePoints()](https://developer.android.com/reference/android/media/VolumeShaper.Configuration#getMaximumCurvePoints()).)

The time coordinates are given over the interval \[0.0, 1.0\]. The first time point must be 0.0, the last must be 1.0, and the times must be monotonically increasing.

The volume coordinates are specified in linear scale over the interval \[0.0, 1.0\].

### Interpolator type

The volume curve always passes through the specified control points. Values between the control points are derived by a spline according to the configuration's interpolator type. There are four constants for the available`VolumeShaper`interpolator types:

- VolumeShaper.Configuration.INTERPOLATOR_TYPE_STEP
- VolumeShaper.Configuration.INTERPOLATOR_TYPE_LINEAR
- VolumeShaper.Configuration.INTERPOLATOR_TYPE_CUBIC
- VolumeShaper.Configuration.INTERPOLATOR_TYPE_CUBIC_MONOTONIC

### Duration

The specified time coordinates in the interval \[0.0, 1.0\] are scaled to a duration that you specify in milliseconds. This determines the actual length in time of the volume curve when the shaper is running and applying the curve to the audio output.

## Using a VolumeShaper

### Creating a configuration

Before building a`VolumeShaper`, you must create an instance of[VolumeShaper.Configuration](https://developer.android.com/reference/android/media/VolumeShaper.Configuration). Do this using a`VolumeShaper.Configuration.Builder()`:  

### Kotlin

```kotlin
val config: VolumeShaper.Configuration = VolumeShaper.Configuration.Builder()
        .setDuration(3000)
        .setCurve(floatArrayOf(0f, 1f), floatArrayOf(0f, 1f))
        .setInterpolatorType(VolumeShaper.Configuration.INTERPOLATOR_TYPE_LINEAR)
        .build()
```

### Java

```java
VolumeShaper.Configuration config =
  new VolumeShaper.Configuration.Builder()
      .setDuration(3000)
      .setCurve(new float[] {0.f, 1.f}, new float[] {0.f, 1.f})
      .setInterpolatorType(VolumeShaper.Configuration.INTERPOLATOR_TYPE_LINEAR)
      .build();
```

WithnoargumentstheVolumeShaper.Configuration.Builderconstructorreturnsabuilderthatcreatesaconfigurationwithdefaultsettings:INTERPOLATOR_TYPE_CUBIC,aonesecondduration,andnocurve.Youmustaddacurvetothebuilderbeforecallingbuild().

Theframeworkprovidesconstantsforconfigurationswithpre-builtcurves,eachwithonesecondduration:

- VolumeShaper.Configuration.LINEAR_RAMP
- VolumeShaper.Configuration.CUBIC_RAMP
- VolumeShaper.Configuration.SINE_RAMP
- VolumeShaper.Configuration.SCURVE_RAMP

### CreatingaVolumeShaper

TocreateaVolumeShaper,callcreateVolumeShaper()onaninstanceoftheappropriateclass,passinginaVolumeShaper.Configuration:  

### Kotlin

```kotlin
volumeShaper = myMediaPlayer.createVolumeShaper(config)
volumeShaper = myAudioTrack.createVolumeShaper(config)
```

### Java

```java
volumeShaper = myMediaPlayer.createVolumeShaper(config);
volumeShaper = myAudioTrack.createVolumeShaper(config);
```

Asingletrackormediaplayercanhavemanyshapersattachedtoit,andyoucancontroleachshaperseparately.Theoutputsofalltheshapersonatrackorplayeraremultipliedtogether.AVolumeShapercannotbesharedbetweenAudioTracksorMediaPlayers,butyoucanusethesameconfigurationincallstocreateVolumeShapertobuildidenticalshapersonmultipleAudioTracksorMediaPlayers.

Whenyoucreatetheshaper,itsfirstcontrolpoint(att=0)isappliedtotheaudiostream.Iftheinitialvolumeisnot1.0andyourappisplayingmaterialatcreatetime,youraudiomighthaveanabruptchangeinvolume.BestpracticeistostartplayingaudiofromsilenceanduseaVolumeShapertoimplementafade-inwhenplaybackstarts.CreateaVolumeShaperthatstartsat0volumeandfadesup.Forexample:

    setCurve(new float[] {0.f, 1.f}, new float[] {0.f, 1.f})

Start playback and the shaper at the same time. This ensures that playback begins from silence and the volume ramps up to full volume. This is explained in the next section.

### Running a VolumeShaper

Though the volume level of the first control point is applied to the audio path as soon as the shaper is created, the shaper does not progress along the curve until you call the`apply()`method with`VolumeShaper.Operation.PLAY`. After creating the shaper, the first invocation of`apply()`must specify the`PLAY`operation in order to start the shaper. This runs the curve from its first to last control points:  

### Kotlin

```kotlin
shaper.apply(VolumeShaper.Operation.PLAY)
```

### Java

```java
shaper.apply(VolumeShaper.Operation.PLAY);
```

While the shaper is running you can issue alternating`apply()`calls specifying REVERSE and PLAY operations. This changes the direction of readout of the control points each time.

The shaper continuously adjusts the volume and passes through all control points until it*expires*. This happens when the shaper reaches the last (for PLAY operation) or first (for REVERSE operation) control point in the curve.

When the shaper expires, the volume remains at the last setting, which may be the first or the last control point. You can call`VolumeShaper.getVolume()`for the current volume level at any time.

After the shaper expires, you can issue another`apply()`call to run the curve in the opposite direction. For example, if the shaper expired while running`PLAY`, the next`apply()`must be`REVERSE`. Calling`PLAY`after`PLAY`has expired, or`REVERSE`after`REVERSE`has expired has no effect.

You must alternate`PLAY`and`REVERSE`operations. There is no way to play a curve from its first to last control points and then restart it again from the first control point. You can use the`replace()`method, described in the next section, to replace the curve with a copy of itself. This resets the shaper, requiring the`PLAY`operation to start it again.

### Changing the curve

Use the`replace()`method to change a`VolumeShaper`'s curve. This method takes a configuration, an operation, and a join parameter. You can call the`replace()`method at any time, while the shaper is running or after it expires:  

### Kotlin

```kotlin
val newConfig = VolumeShaper.Configuration.Builder()
        .setDuration(1000)
        .setCurve(floatArrayOf(0f, 0.5f), floatArrayOf(0f, 1f))
        .setInterpolatorType(VolumeShaper.Configuration.INTERPOLATOR_TYPE_LINEAR)
        .build()
val join = true
shaper.replace(newConfig, VolumeShaper.Operation.PLAY, join)
```

### Java

```java
VolumeShaper.Configuration newConfig =
  new VolumeShaper.Configuration.Builder()
    .setDuration(1000)
    .setCurve(new float[] {0.f, 0.5f}, new float[] {0.f, 1.f})
    .setInterpolatorType(VolumeShaper.Configuration.INTERPOLATOR_TYPE_LINEAR)
    .build();
boolean join = true;
shaper.replace(newConfig, VolumeShaper.Operation.PLAY, join);
```

When you call`replace()`while the shaper is running, it stops changing the volume and remains at its current value. Then the shaper tries to start the new curve from the first control point. This means that the operation argument controls whether or not the shaper runs after the call. Specify`PLAY`to immediately start the new curve, specify`REVERSE`to leave the shaper paused at the volume of the first control point in the new curve. You can start the shaper later with`apply(VolumeShaper.Operation.PLAY)`.

When you call`replace()`with`join = false`, the shaper starts its curve at the level specified by its first control point. This can cause a discontinuity in the volume. You can avoid this by calling`replace()`with`join = true`. This sets the first control point of the new curve to the current level of the shaper and scales the volume of all the control points between the first and last to maintain the relative shape of the new curve (the last control point is unchanged). The scaling operation permanently changes the control points in the shaper's new curve.

### Removing a VolumeShaper

The system closes and garbage collects a`VolumeShaper`when its`AudioTrack`or`MediaPlayer`is released or no longer in use. You can call the`close()`method on a shaper to destroy it immediately. The system removes the shaper from the audio pipeline within about 20 ms. Be careful when closing a`VolumeShaper`while audio is playing. If the shaper has a volume less than 1.0 when you call`close()`, the shaper's volume scale changes to 1.0. This can cause a sudden increase in volume.