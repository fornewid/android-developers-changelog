---
title: https://developer.android.com/training/wearables/wff/time
url: https://developer.android.com/training/wearables/wff/time
source: md.txt
---

The primary job of a watch face is to show the time, and the Watch Face Format
lets you create both analog and digital clocks using the
[`AnalogClock`](https://developer.android.com/training/wearables/wff/clock/analog-clock) and [`DigitalClock`](https://developer.android.com/training/wearables/wff/clock/digital-clock) elements.

### Digital clocks

A basic digital clock can be defined using the `DigitalClock` and
[`TimeText`](https://developer.android.com/training/wearables/wff/clock/time-text) element within your watch face `Scene`:

<br />

```xml
<DigitalClock x="125" y="50" width="200" height="50">
    <TimeText x="0" y="0" width="200" height="50" format="hh:mm">
        <Font family="SYNC_TO_DEVICE" size="16" />
    </TimeText>
</DigitalClock>
```

<br />

The `format` attribute lets you control how the time is represented using
a combination of hours, minutes, and seconds. The exact options differ depending
on the version of Watch Face Format being used; version 2 expands the options
here.

In the preceding example, [Font](https://developer.android.com/training/wearables/wff/group/part/text/font) is set to use the system font.

It can also be useful to show the time for other locations in the world, for
example a *world clock* . This can be achieved through the [`Localization`](https://developer.android.com/training/wearables/wff/common/localization)
element:

<br />

```xml
<DigitalClock x="125" y="100" width="200" height="50">
    <Localization timeZone="Europe/London" />
    <!-- TimeText goes here -->
    <!-- START_EXCLUDE -->
    <TimeText x="0" y="0" width="200" height="50" format="hh:mm">
        <Font family="SYNC_TO_DEVICE" size="16" />
    </TimeText>
    <!-- END_EXCLUDE -->
</DigitalClock>
```

<br />

### Analog clocks

To create an analog clock, use the [`AnalogClock`](https://developer.android.com/training/wearables/wff/clock/analog-clock) element. Each of the
`HourHand, MinuteHand`, and `SecondHand` child elements specifies the resource
that should be used in the rendering:

<br />

```xml
<AnalogClock x="0" y="0" width="450" height="450">
    <HourHand resource="hour" x="220" y="55" width="20" height="190"
        pivotX="0.5" pivotY="0.9210" />
    <MinuteHand resource="minute" x="222" y="30" width="16" height="220"
        pivotX="0.5" pivotY="0.9" />
    <SecondHand resource="second" x="226" y="20" width="8" height="245"
        pivotX="0.5" pivotY="0.8571" />
</AnalogClock>
```

<br />

#### Specify the pivot point

Each of the hour, minute, and second resources are rotated as time advances,
but it is important to specify the correct point around which each should pivot.

In some situations, the pivot point is not quite at the bottom of the hand, and
is centered horizontally. This should be specified as `<HourHand ...
pivotY="(pivot_ratio)" />` where:
$$ pivot\\_ratio = \\frac{pivot\\_height}{full\\_height} $$

#### Color the watch hands

To allow the user to customize the appearance of the watch face, it is common to
have a configurable color for the watch hands.

A way to achieve this is through the `tintColor` on each of the hands to
separately tint each hand, or on `AnalogClock`, to tint all hands the same
color.

In addition to enabling users to tint specific colors, you can supply a
configuration option to `tintColor` to allow the user to choose, for example,
adding `tintColor="[CONFIGURATION.handColors.0]` to the `AnalogClock` element.

#### Drop shadow

For a realistic watch hand effect, using a drop shadow behind each hand can give
the appearance of depth.

To achieve this, use two of each hand type within a single `AnalogClock`,
offsetting one behind the other, and use a separate resource for the hand that
represents the shadow.

#### Face decorations

Analog watch faces often have decorations around the face showing the hours or
minutes. To achieve this, there are two approaches:

1. Include a full-screen background image, which contains your predrawn watch
   face. [See working with images](https://developer.android.com/training/wearables/wff/images).

   <br />

   ```xml
   <PartImage x="0" y="0" width="450" height="450">
       <Image resource="watch_face_dial" />
   </PartImage>
   ```

   <br />

2. Draw separate decorations and position them around the face using rotations.

   <br />

   ```xml
   <!-- Content for the "12" -->
   <Group x="200" y="0" width="50" height="450">
       <PartText x="0" y="0" width="50" height="50">
           <Text>
               <Font family="SYNC_TO_DEVICE" size="16" color="#FF00FF">
                   <![CDATA[12]]>
               </Font>
           </Text>
       </PartText>
   </Group>
   <!-- Content for the "1" -->
   <Group x="200" y="0" width="50" height="450" angle="30">
       <PartText x="0" y="0" width="50" height="50">
           <Text>
               <Font family="SYNC_TO_DEVICE" size="16" color="#FF00FF">
                   <![CDATA[1]]>
               </Font>
           </Text>
       </PartText>
   </Group>
   <!-- etc -->
   ```

   <br />