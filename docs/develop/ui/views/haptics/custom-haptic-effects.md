---
title: https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects
url: https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects
source: md.txt
---

This page covers the examples of how to use different [haptics APIs](https://developer.android.com/develop/ui/views/haptics/haptics-apis) to
create custom effects beyond the standard [vibration waveforms](https://developer.android.com/develop/ui/views/haptics/actuators) in an Android
app.

This page includes the following examples:

- [Custom vibration patterns](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#custom_vibration_patterns)
  - [Ramp up pattern](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#ramp_up_pattern): A pattern that begins smoothly.
  - [Repeating pattern](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#repeating_pattern): A pattern with no end.
  - [Pattern with fallback](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#pattern_with_fallback): A fallback demonstration.
- [Vibration compositions](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#vibration_compositions)
  - [Resist](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#resist): A drag effect with dynamic intensity.
  - [Expand](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#expand): A rise then fall effect.
  - [Wobble](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#wobble): A wobbly effect using the `SPIN` primitive.
  - [Bounce](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#bounce): A bouncing effect using the `THUD` primitive.
- [Vibration waveform with envelopes](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#vibration-waveform-with-envelopes)
  - [Bouncing spring](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#bouncing-spring): A springy bouncing effect using basic envelope effects.
  - [Rocket launch](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#rocket-launch): A rocket launch effect using waveform envelope effects.

For additional examples, see [Add haptic feedback to events](https://developer.android.com/develop/ui/views/haptics/haptic-feedback), and always
follow [haptics design principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles).

## Use fallbacks to handle device compatibility

When implementing any custom effect, consider the following:

- Which device capabilities are required for the effect
- What to do when the device is not capable of playing the effect

The [Android haptics API reference](https://developer.android.com/develop/ui/views/haptics/haptics-apis) provides details on how to check for
support for components involved in your haptics, so that your app can provide a
consistent overall experience.

Depending on your use case, you might want to disable custom effects or to
provide alternative custom effects based on different potential capabilities.

Plan for the following high-level classes of device capability:

- If you're using haptic *primitives*: devices supporting those primitives
  needed by the custom effects. (See the next section for details on
  primitives.)

- Devices with *amplitude control*.

- Devices with *basic* vibration support (on/off)---in other words, those
  lacking amplitude control.

If your app's haptic effect choice accounts for these categories, then its
haptic user experience should remain predictable for any individual device.

## Usage of haptic primitives

Android includes several haptics *primitives* that vary in both amplitude and
frequency. You may use one primitive alone or multiple primitives in combination
to achieve rich haptic effects.

- Use delays of 50 ms or longer for discernible gaps between two primitives, also taking into account the [primitive duration](https://developer.android.com/reference/android/os/Vibrator#getPrimitiveDurations(int...)) if possible.
- Use scales that differ by a ratio of 1.4 or more so the difference in intensity is better perceived.
- Use scales of 0.5, 0.7, and 1.0 to create a low, medium, and high intensity
  version of a primitive.

  | **Note:** A 0.0 `scale` parameter indicates minimum perceivable vibration, not off.

## Create custom vibration patterns

Vibration patterns are often used in attentional haptics, such as notifications
and ringtones. The [`Vibrator`](https://developer.android.com/reference/android/os/Vibrator) service can play long vibration patterns
that change the vibration amplitude over time. Such effects are called
waveforms.

Waveform effects are usually perceivable, but sudden long vibrations can startle
the user if played in a quiet environment. Ramping to a target amplitude too
fast might also produce audible buzzing noises. Design waveform patterns to
smooth the amplitude transitions to create ramp up and down effects.
| **Important:** Start and end a waveform at zero amplitude whenever possible. This avoids any sudden changes in the input voltage amplitude to the actuator which may cause the actuator to resonate; in other words, vibrate at its resonance frequency. Also, some drivers apply *active braking* if the waveform ends at 0, so the vibration stops more quickly. See [Vibration actuators primer](https://developer.android.com/develop/ui/views/haptics/actuators) for details.

## Examples of vibration patterns

The following sections provide several examples of vibration patterns:

### Ramp-up pattern

Waveforms are represented as [`VibrationEffect`](https://developer.android.com/reference/android/os/VibrationEffect) with three parameters:

1. **Timings:** an array of durations, in milliseconds, for each waveform segment.
2. **Amplitudes:** the wanted vibration amplitude for each duration specified in the first argument, represented by an integer value from 0 to 255, with 0 representing the vibrator "off state" and 255 being the device's maximum amplitude.
3. **Repeat index:** the index in the array specified in the first argument to start repeating the waveform, or -1 if it should play the pattern only once.

Here is an example waveform that pulses twice with a pause of 350 ms in between
pulses. The first pulse is a smooth ramp up to the maximum amplitude, and the
second is a quick ramp to hold maximum amplitude. Stopping at the end is defined
by the negative repeat index value.  

### Kotlin

    val timings: LongArray = longArrayOf(
        50, 50, 50, 50, 50, 100, 350, 25, 25, 25, 25, 200)
    val amplitudes: IntArray = intArrayOf(
        33, 51, 75, 113, 170, 255, 0, 38, 62, 100, 160, 255)
    val repeatIndex = -1 // Don't repeat.

    vibrator.vibrate(VibrationEffect.createWaveform(
        timings, amplitudes, repeatIndex))

### Java

    long[] timings = new long[] {
        50, 50, 50, 50, 50, 100, 350, 25, 25, 25, 25, 200 };
    int[] amplitudes = new int[] {
        33, 51, 75, 113, 170, 255, 0, 38, 62, 100, 160, 255 };
    int repeatIndex = -1; // Don't repeat.

    vibrator.vibrate(VibrationEffect.createWaveform(
        timings, amplitudes, repeatIndex));

### Repeating pattern

Waveforms can also be played repeatedly until cancelled. The way to create a
repeating waveform is to set a non-negative `repeat` parameter. When you play a
repeating waveform, the vibration continues until it's explicitly cancelled in
the service:  

### Kotlin

    void startVibrating() {
    val timings: LongArray = longArrayOf(50, 50, 100, 50, 50)
    val amplitudes: IntArray = intArrayOf(64, 128, 255, 128, 64)
    val repeat = 1 // Repeat from the second entry, index = 1.
    VibrationEffect repeatingEffect = VibrationEffect.createWaveform(
        timings, amplitudes, repeat)
    // repeatingEffect can be used in multiple places.

    vibrator.vibrate(repeatingEffect)
    }

    void stopVibrating() {
    vibrator.cancel()
    }

### Java

    void startVibrating() {
    long[] timings = new long[] { 50, 50, 100, 50, 50 };
    int[] amplitudes = new int[] { 64, 128, 255, 128, 64 };
    int repeat = 1; // Repeat from the second entry, index = 1.
    VibrationEffect repeatingEffect = VibrationEffect.createWaveform(
        timings, amplitudes, repeat);
    // repeatingEffect can be used in multiple places.

    vibrator.vibrate(repeatingEffect);
    }

    void stopVibrating() {
    vibrator.cancel();
    }

This is very useful for intermittent events that require user action to
acknowledge it. Examples of such events include incoming phone calls and
triggered alarms.

### Pattern with fallback

Controlling the amplitude of a vibration is a
[hardware-dependent capability](https://developer.android.com/develop/ui/views/haptics/haptics-apis#amplitude_control). Playing a waveform on a low-end device
without this capability causes the device to vibrate at the maximum amplitude
for each positive entry in the amplitude array. If your app needs to accommodate
such devices, either use a pattern that doesn't generate a buzzing effect when
played in that condition, or design a simpler ON/OFF pattern that can be played
as a fallback instead.  

### Kotlin

    if (vibrator.hasAmplitudeControl()) {
      vibrator.vibrate(VibrationEffect.createWaveform(
        smoothTimings, amplitudes, smoothRepeatIdx))
    } else {
      vibrator.vibrate(VibrationEffect.createWaveform(
        onOffTimings, onOffRepeatIdx))
    }

### Java

    if (vibrator.hasAmplitudeControl()) {
      vibrator.vibrate(VibrationEffect.createWaveform(
        smoothTimings, amplitudes, smoothRepeatIdx));
    } else {
      vibrator.vibrate(VibrationEffect.createWaveform(
        onOffTimings, onOffRepeatIdx));
    }

| **Note:** The ON/OFF pattern is actually specified in the API as a OFF/ON sequence of durations. See more details in the [API reference documentation](https://developer.android.com/reference/android/os/VibrationEffect#createWaveform(long%5B%5D,%20int)).

## Create vibration compositions

This section presents ways to compose vibrations into longer and more complex
custom effects, and goes beyond that to explore rich haptics using more advanced
hardware capabilities. You can use combinations of effects that vary amplitude
and frequency to create more complex haptic effects on devices with haptic
actuators that have a wider frequency bandwidth.
| **Note:** See [Add haptics feedback to events](https://developer.android.com/develop/ui/views/haptics/haptic-feedback) for predefined haptic effects and how to use them.

The process for [creating custom vibration patterns](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#custom_vibration_patterns), described previously on
this page, explains how to control the vibration amplitude to create smooth
effects of ramping up and down. Rich haptics improves on this concept by
exploring the wider frequency range of the device vibrator to make the effect
even smoother. These waveforms are especially effective at creating a crescendo
or diminuendo effect.

The composition [primitives](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#primitives), described earlier on this page, are
implemented by the device manufacturer. They provide a crisp, short, and
pleasant vibration that aligns with [haptics principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles) for clear haptics.
For more details about these capabilities and how they work, see [Vibration
actuators primer](https://developer.android.com/develop/ui/views/haptics/actuators).

Android doesn't provide fallbacks for compositions with unsupported primitives.
Therefore, perform the following steps:

1. Before activating your advanced haptics, check that a given device supports
   all the primitives you're using.

2. Disable the consistent set of experiences that are unsupported, not just the
   effects that are missing a primitive.

More information on how to check the device's support is shown in the following
sections.

### Create composed vibration effects

You can create composed vibration effects with
[`VibrationEffect.Composition`](https://developer.android.com/reference/android/os/VibrationEffect.Composition). Here is an example of a slowly rising
effect followed by a sharp click effect:  

### Kotlin

    vibrator.vibrate(
        VibrationEffect.startComposition().addPrimitive(
        VibrationEffect.Composition.PRIMITIVE_SLOW_RISE
        ).addPrimitive(
        VibrationEffect.Composition.PRIMITIVE_CLICK
        ).compose()
    )

### Java

    vibrator.vibrate(
        VibrationEffect.startComposition()
            .addPrimitive(VibrationEffect.Composition.PRIMITIVE_SLOW_RISE)
            .addPrimitive(VibrationEffect.Composition.PRIMITIVE_CLICK)
            .compose());

A composition is created by adding primitives to be played in sequence. Each
primitive is also scalable, so you can control the amplitude of the vibration
generated by each of them. The scale is defined as a value between 0 and 1,
where 0 actually maps to a minimum amplitude at which this primitive can be
(barely) felt by the user.

### Create variants in vibration primitives

If you'd like to create a weak and strong version of the same primitive, create
strength ratios of 1.4 or more, so the difference in intensity can be readily
perceived. Don't try to create more than three intensity levels of the same
primitive, because they aren't perceptually distinct. For example, use scales of
0.5, 0.7, and 1.0 to create low, medium, and high intensity versions of a
primitive.

### Add gaps between vibration primitives

The composition can also specify delays to be added in between consecutive
primitives. This delay is expressed in milliseconds since the end of the
previous primitive. In general, a 5 to 10 ms gap between two primitives is too
short to be detectable. Use a gap on the order of 50 ms or longer if you want to
create a discernible gap between two primitives. Here is an example of a
composition with delays:  

### Kotlin

    val delayMs = 100
    vibrator.vibrate(
        VibrationEffect.startComposition().addPrimitive(
        VibrationEffect.Composition.PRIMITIVE_SPIN, 0.8f
        ).addPrimitive(
        VibrationEffect.Composition.PRIMITIVE_SPIN, 0.6f
        ).addPrimitive(
        VibrationEffect.Composition.PRIMITIVE_THUD, 1.0f, delayMs
        ).compose()
    )

### Java

    int delayMs = 100;
    vibrator.vibrate(
        VibrationEffect.startComposition()
            .addPrimitive(VibrationEffect.Composition.PRIMITIVE_SPIN, 0.8f)
            .addPrimitive(VibrationEffect.Composition.PRIMITIVE_SPIN, 0.6f)
            .addPrimitive(
                VibrationEffect.Composition.PRIMITIVE_THUD, 1.0f, delayMs)
            .compose());

### Check which primitives are supported

The following APIs can be used to verify the device support for specific
primitives:  

### Kotlin

    val primitive = VibrationEffect.Composition.PRIMITIVE_LOW_TICK

    if (vibrator.areAllPrimitivesSupported(primitive)) {
      vibrator.vibrate(VibrationEffect.startComposition()
            .addPrimitive(primitive).compose())
    } else {
      // Play a predefined effect or custom pattern as a fallback.
    }

### Java

    int primitive = VibrationEffect.Composition.PRIMITIVE_LOW_TICK;

    if (vibrator.areAllPrimitivesSupported(primitive)) {
      vibrator.vibrate(VibrationEffect.startComposition()
            .addPrimitive(primitive).compose());
    } else {
      // Play a predefined effect or custom pattern as a fallback.
    }

It's also possible to check multiple primitives and then decide which ones to
compose based on the device support level:  

### Kotlin

    val effects: IntArray = intArrayOf(
    VibrationEffect.Composition.PRIMITIVE_LOW_TICK,
    VibrationEffect.Composition.PRIMITIVE_TICK,
    VibrationEffect.Composition.PRIMITIVE_CLICK
    )
    val supported: BooleanArray = vibrator.arePrimitivesSupported(primitives)

### Java

    int[] primitives = new int[] {
    VibrationEffect.Composition.PRIMITIVE_LOW_TICK,
    VibrationEffect.Composition.PRIMITIVE_TICK,
    VibrationEffect.Composition.PRIMITIVE_CLICK
    };
    boolean[] supported = vibrator.arePrimitivesSupported(effects);

## Examples of vibration compositions

The following sections provide several examples of vibration compositions, taken
from the [haptics sample app](https://github.com/android/platform-samples/tree/main/samples/user-interface/haptics) on GitHub.

### Resist (with low ticks)

You can control the amplitude of the primitive vibration to convey useful
feedback to an action in progress. Closely-spaced scale values can be used to
create a smooth crescendo effect of a primitive. The delay between consecutive
[primitives](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#primitives) can also be dynamically set based on the user interaction. This
is illustrated in the following example of a view animation controlled by a drag
gesture and augmented with haptics.  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of a circle being dragged down.](https://developer.android.com/static/develop/ui/views/haptics/images/resist-demo.gif)  
![Plot of input vibration waveform.](https://developer.android.com/static/develop/ui/views/haptics/images/resist-waveform.svg)

**Figure 1.** This waveform represents the
output acceleration of the vibration on a device.  

### Kotlin

    @Composable
    fun ResistScreen() {
        // Control variables for the dragging of the indicator.
        var isDragging by remember { mutableStateOf(false) }
        var dragOffset by remember { mutableStateOf(0f) }

        // Only vibrates while the user is dragging
        if (isDragging) {
            LaunchedEffect(Unit) {
            // Continuously run the effect for vibration to occur even when the view
            // is not being drawn, when user stops dragging midway through gesture.
            while (true) {
                // Calculate the interval inversely proportional to the drag offset.
                val vibrationInterval = calculateVibrationInterval(dragOffset)
                // Calculate the scale directly proportional to the drag offset.
                val vibrationScale = calculateVibrationScale(dragOffset)

                delay(vibrationInterval)
                vibrator.vibrate(
                VibrationEffect.startComposition().addPrimitive(
                    VibrationEffect.Composition.PRIMITIVE_LOW_TICK,
                    vibrationScale
                ).compose()
                )
            }
            }
        }

        Screen() {
            Column(
            Modifier
                .draggable(
                orientation = Orientation.Vertical,
                onDragStarted = {
                    isDragging = true
                },
                onDragStopped = {
                    isDragging = false
                },
                state = rememberDraggableState { delta ->
                    dragOffset += delta
                }
                )
            ) {
            // Build the indicator UI based on how much the user has dragged it.
            ResistIndicator(dragOffset)
            }
        }
    }

### Java

    class DragListener implements View.OnTouchListener {
        // Control variables for the dragging of the indicator.
        private int startY;
        private int vibrationInterval;
        private float vibrationScale;

        @Override
        public boolean onTouch(View view, MotionEvent event) {
            switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                startY = event.getRawY();
                vibrationInterval = calculateVibrationInterval(0);
                vibrationScale = calculateVibrationScale(0);
                startVibration();
                break;
            case MotionEvent.ACTION_MOVE:
                float dragOffset = event.getRawY() - startY;
                // Calculate the interval inversely proportional to the drag offset.
                vibrationInterval = calculateVibrationInterval(dragOffset);
                // Calculate the scale directly proportional to the drag offset.
                vibrationScale = calculateVibrationScale(dragOffset);
                // Build the indicator UI based on how much the user has dragged it.
                updateIndicator(dragOffset);
                break;
            case MotionEvent.ACTION_CANCEL:
            case MotionEvent.ACTION_UP:
                // Only vibrates while the user is dragging
                cancelVibration();
                break;
            }
            return true;
        }

        private void startVibration() {
            vibrator.vibrate(
                VibrationEffect.startComposition()
                    .addPrimitive(VibrationEffect.Composition.PRIMITIVE_LOW_TICK,
                            vibrationScale)
                    .compose());

            // Continuously run the effect for vibration to occur even when the view
            // is not being drawn, when user stops dragging midway through gesture.
            handler.postDelayed(this::startVibration, vibrationInterval);
        }

        private void cancelVibration() {
            handler.removeCallbacksAndMessages(null);
        }
    }

### Expand (with rise and fall)

There are two [primitives](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#primitives) for ramping up the perceived vibration intensity:
[`PRIMITIVE_QUICK_RISE`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_QUICK_RISE) and [`PRIMITIVE_SLOW_RISE`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_SLOW_RISE). They both reach
the same target, but with different durations. There is only one primitive for
ramping down, [`PRIMITIVE_QUICK_FALL`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_QUICK_FALL). These primitives work better
together to create a waveform segment that grows in intensity and then dies off.
You can align scaled primitives to prevent sudden jumps in amplitude between
them, which also works well for extending the overall effect duration.
Perceptually, people always notice the rising portion more than the falling
portion, so making the rising portion shorter than the falling can be used to
shift the emphasis towards the falling portion.

Here is an example of an application of this composition for expanding and
collapsing a circle. The rise effect can enhance the feeling of expansion during
the animation. The combination of rise and fall effects helps emphasize the
collapsing at the end of the animation.  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of an expanding circle.](https://developer.android.com/static/develop/ui/views/haptics/images/expand-demo.gif)  
![Plot of input vibration waveform.](https://developer.android.com/static/develop/ui/views/haptics/images/expand-waveform.svg)

**Figure 2.**This waveform represents the
output acceleration of the vibration on a device.  

### Kotlin

    enum class ExpandShapeState {
        Collapsed,
        Expanded
    }

    @Composable
    fun ExpandScreen() {
        // Control variable for the state of the indicator.
        var currentState by remember { mutableStateOf(ExpandShapeState.Collapsed) }

        // Animation between expanded and collapsed states.
        val transitionData = updateTransitionData(currentState)

        Screen() {
            Column(
            Modifier
                .clickable(
                {
                    if (currentState == ExpandShapeState.Collapsed) {
                    currentState = ExpandShapeState.Expanded
                    vibrator.vibrate(
                        VibrationEffect.startComposition().addPrimitive(
                        VibrationEffect.Composition.PRIMITIVE_SLOW_RISE,
                        0.3f
                        ).addPrimitive(
                        VibrationEffect.Composition.PRIMITIVE_QUICK_FALL,
                        0.3f
                        ).compose()
                    )
                    } else {
                    currentState = ExpandShapeState.Collapsed
                    vibrator.vibrate(
                        VibrationEffect.startComposition().addPrimitive(
                        VibrationEffect.Composition.PRIMITIVE_SLOW_RISE
                        ).compose()
                    )
                }
                )
            ) {
            // Build the indicator UI based on the current state.
            ExpandIndicator(transitionData)
            }
        }
    }

### Java

    class ClickListener implements View.OnClickListener {
        private final Animation expandAnimation;
        private final Animation collapseAnimation;
        private boolean isExpanded;

        ClickListener(Context context) {
            expandAnimation = AnimationUtils.loadAnimation(context, R.anim.expand);
            expandAnimation.setAnimationListener(new Animation.AnimationListener() {

            @Override
            public void onAnimationStart(Animation animation) {
                vibrator.vibrate(
                VibrationEffect.startComposition()
                    .addPrimitive(
                        VibrationEffect.Composition.PRIMITIVE_SLOW_RISE, 0.3f)
                    .addPrimitive(
                        VibrationEffect.Composition.PRIMITIVE_QUICK_FALL, 0.3f)
                    .compose());
            }
            });

            collapseAnimation = AnimationUtils
                    .loadAnimation(context, R.anim.collapse);
            collapseAnimation.setAnimationListener(new Animation.AnimationListener() {

                @Override
                public void onAnimationStart(Animation animation) {
                    vibrator.vibrate(
                    VibrationEffect.startComposition()
                        .addPrimitive(
                            VibrationEffect.Composition.PRIMITIVE_SLOW_RISE)
                        .compose());
                }
            });
        }

        @Override
        public void onClick(View view) {
            view.startAnimation(isExpanded ? collapseAnimation : expandAnimation);
            isExpanded = !isExpanded;
        }
    }

### Wobble (with spins)

One of the key [haptics principles](https://developer.android.com/develop/ui/views/haptics/haptics-principles) is to delight users. A fun way to
introduce a pleasant unexpected vibration effect is to use
[`PRIMITIVE_SPIN`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_SPIN). This primitive is most effective when it is called more
than once. Multiple spins concatenated can create a wobbling and unstable
effect, which can be further enhanced by applying a somewhat random scaling on
each primitive. You can also experiment with the gap between successive spin
[primitives](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#primitives). Two spins without any gap (0 ms in between) creates a tight
spinning sensation. Increasing the inter-spin gap from 10 to 50 ms leads to a
looser spinning sensation, and can be used to match the duration of a video or
animation.

Don't use a gap that is longer than 100 ms, as the successive spins no longer
integrate well and begin to feel like individual effects.

Here is an example of a elastic shape that bounces back after being dragged down
and then released. The animation is enhanced with a pair of spin effects, played
with varying intensities that are proportional to the bounce displacement.  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of an elastic shape bouncing](https://developer.android.com/static/develop/ui/views/haptics/images/wobble-demo.gif)  
![Plot of input vibration waveform](https://developer.android.com/static/develop/ui/views/haptics/images/wobble-waveform.svg)

**Figure 3.** This waveform represents the
output acceleration of the vibration on a device.  

### Kotlin

    @Composable
    fun WobbleScreen() {
        // Control variables for the dragging and animating state of the elastic.
        var dragDistance by remember { mutableStateOf(0f) }
        var isWobbling by remember { mutableStateOf(false) }

        // Use drag distance to create an animated float value behaving like a spring.
        val dragDistanceAnimated by animateFloatAsState(
            targetValue = if (dragDistance > 0f) dragDistance else 0f,
            animationSpec = spring(
                dampingRatio = Spring.DampingRatioHighBouncy,
                stiffness = Spring.StiffnessMedium
            ),
        )

        if (isWobbling) {
            LaunchedEffect(Unit) {
                while (true) {
                    val displacement = dragDistanceAnimated / MAX_DRAG_DISTANCE
                    // Use some sort of minimum displacement so the final few frames
                    // of animation don't generate a vibration.
                    if (displacement > SPIN_MIN_DISPLACEMENT) {
                        vibrator.vibrate(
                            VibrationEffect.startComposition().addPrimitive(
                                VibrationEffect.Composition.PRIMITIVE_SPIN,
                                nextSpinScale(displacement)
                            ).addPrimitive(
                            VibrationEffect.Composition.PRIMITIVE_SPIN,
                            nextSpinScale(displacement)
                            ).compose()
                        )
                    }
                    // Delay the next check for a sufficient duration until the
                    // current composition finishes. Note that you can use
                    // Vibrator.getPrimitiveDurations API to calculcate the delay.
                    delay(VIBRATION_DURATION)
                }
            }
        }

        Box(
            Modifier
                .fillMaxSize()
                .draggable(
                    onDragStopped = {
                        isWobbling = true
                        dragDistance = 0f
                    },
                    orientation = Orientation.Vertical,
                    state = rememberDraggableState { delta ->
                        isWobbling = false
                        dragDistance += delta
                    }
                )
        ) {
            // Draw the wobbling shape using the animated spring-like value.
            WobbleShape(dragDistanceAnimated)
        }
    }

    // Calculate a random scale for each spin to vary the full effect.
    fun nextSpinScale(displacement: Float): Float {
        // Generate a random offset in the range [-0.1, +0.1] to be added to the
        // vibration scale so the spin effects have slightly different values.
        val randomOffset: Float = Random.Default.nextFloat() * 0.2f - 0.1f
        return (displacement + randomOffset).absoluteValue.coerceIn(0f, 1f)
    }

### Java

    class AnimationListener implements DynamicAnimation.OnAnimationUpdateListener {
        private final Random vibrationRandom = new Random(seed);
        private final long lastVibrationUptime;

        @Override
        public void onAnimationUpdate(
            DynamicAnimation animation, float value, float velocity) {
            // Delay the next check for a sufficient duration until the current
            // composition finishes. Note that you can use
            // Vibrator.getPrimitiveDurations API to calculcate the delay.
            if (SystemClock.uptimeMillis() - lastVibrationUptime < VIBRATION_DURATION) {
                return;
            }

            float displacement = calculateRelativeDisplacement(value);

            // Use some sort of minimum displacement so the final few frames
            // of animation don't generate a vibration.
            if (displacement < SPIN_MIN_DISPLACEMENT) {
                return;
            }

            lastVibrationUptime = SystemClock.uptimeMillis();
            vibrator.vibrate(
            VibrationEffect.startComposition()
                .addPrimitive(VibrationEffect.Composition.PRIMITIVE_SPIN,
                nextSpinScale(displacement))
                .addPrimitive(VibrationEffect.Composition.PRIMITIVE_SPIN,
                nextSpinScale(displacement))
                .compose());
        }

        // Calculate a random scale for each spin to vary the full effect.
        float nextSpinScale(float displacement) {
            // Generate a random offset in the range [-0.1,+0.1] to be added to
            // the vibration scale so the spin effects have slightly different
            // values.
            float randomOffset = vibrationRandom.nextFloat() * 0.2f - 0.1f
            return MathUtils.clamp(displacement + randomOffset, 0f, 1f)
        }
    }

### Bounce (with thuds)

Another advanced application of vibration effects is to simulate physical
interactions. [`PRIMITIVE_THUD`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_THUD) can create a strong and reverberating
effect, which can be paired with the visualization of an impact, in a video or
animation for example, to augment the overall experience.

Here is an example of a ball drop animation enhanced with a thud effect played
each time the ball bounces off the bottom of the screen:  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of a dropped ball bouncing off the bottom of the screen.](https://developer.android.com/static/develop/ui/views/haptics/images/bounce-demo.gif)  
![Plot of input vibration waveform.](https://developer.android.com/static/develop/ui/views/haptics/images/bounce-waveform.svg)

**Figure 4.** This waveform represents the
output acceleration of the vibration on a device.  

### Kotlin

    enum class BallPosition {
        Start,
        End
    }

    @Composable
    fun BounceScreen() {
        // Control variable for the state of the ball.
        var ballPosition by remember { mutableStateOf(BallPosition.Start) }
        var bounceCount by remember { mutableStateOf(0) }

        // Animation for the bouncing ball.
        var transitionData = updateTransitionData(ballPosition)
        val collisionData = updateCollisionData(transitionData)

        // Ball is about to contact floor, only vibrating once per collision.
        var hasVibratedForBallContact by remember { mutableStateOf(false) }
        if (collisionData.collisionWithFloor) {
            if (!hasVibratedForBallContact) {
            val vibrationScale = 0.7.pow(bounceCount++).toFloat()
            vibrator.vibrate(
                VibrationEffect.startComposition().addPrimitive(
                VibrationEffect.Composition.PRIMITIVE_THUD,
                vibrationScale
                ).compose()
            )
            hasVibratedForBallContact = true
            }
        } else {
            // Reset for next contact with floor.
            hasVibratedForBallContact = false
        }

        Screen() {
            Box(
            Modifier
                .fillMaxSize()
                .clickable {
                if (transitionData.isAtStart) {
                    ballPosition = BallPosition.End
                } else {
                    ballPosition = BallPosition.Start
                    bounceCount = 0
                }
                },
            ) {
            // Build the ball UI based on the current state.
            BouncingBall(transitionData)
            }
        }
    }

### Java

    class ClickListener implements View.OnClickListener {
        @Override
        public void onClick(View view) {
            view.animate()
            .translationY(targetY)
            .setDuration(3000)
            .setInterpolator(new BounceInterpolator())
            .setUpdateListener(new AnimatorUpdateListener() {

                boolean hasVibratedForBallContact = false;
                int bounceCount = 0;

                @Override
                public void onAnimationUpdate(ValueAnimator animator) {
                boolean valueBeyondThreshold = (float) animator.getAnimatedValue() > 0.98;
                if (valueBeyondThreshold) {
                    if (!hasVibratedForBallContact) {
                    float vibrationScale = (float) Math.pow(0.7, bounceCount++);
                    vibrator.vibrate(
                        VibrationEffect.startComposition()
                        .addPrimitive(
                            VibrationEffect.Composition.PRIMITIVE_THUD,
                            vibrationScale)
                        .compose());
                    hasVibratedForBallContact = true;
                    }
                } else {
                    // Reset for next contact with floor.
                    hasVibratedForBallContact = false;
                }
                }
            });
        }
    }

## Vibration waveform with envelopes

The process for [creating custom vibration patterns](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#custom_vibration_patterns) lets you control the
vibration amplitude to create smooth effects of ramping up and down. This
section explains how to create dynamic haptic effects using waveform envelopes
that allow for precise control of the vibration amplitude and frequency over
time. This lets you craft richer and more nuanced haptic experiences.

Starting in Android 16 (API level 36), the system provides the following APIs to
create a vibration waveform envelope by defining a sequence of control points:

- **[`BasicEnvelopeBuilder`](https://developer.android.com/reference/android/os/VibrationEffect.BasicEnvelopeBuilder):** An accessible approach to creating hardware-agnostic haptic effects.
- **[`WaveformEnvelopeBuilder`](https://developer.android.com/reference/android/os/VibrationEffect.WaveformEnvelopeBuilder):** A more advanced approach to creating haptic effects; requires familiarity with haptics hardware.

Android doesn't provide fallbacks for envelope effects. If you require this
support, complete the following steps:

1. Check a given device supports envelope effects using [`Vibrator.areEnvelopeEffectsSupported()`](https://developer.android.com/reference/android/os/Vibrator#areEnvelopeEffectsSupported()).
2. Disable the consistent set of experiences that are unsupported, or use [custom vibration patterns](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#custom_vibration_patterns) or [compositions](https://developer.android.com/develop/ui/views/haptics/actuators#vibrator-output-acceleratio) as fallback alternatives.

To create more basic envelope effects, use the `BasicEnvelopeBuilder` with these
parameters:

- An **[intensity](https://developer.android.com/develop/ui/views/haptics/actuators#vibration-acceleration-levels)** value in the range \\( \[0, 1\] \\), which represents the perceived strength of the vibration. For example, a value of \\( 0.5 \\) is perceived as half the global maximum intensity that can be achieved by the device.
- A **sharpness** value in the range \\( \[0, 1\] \\), which represents the
  crispness of the vibration. Lower values translate to smoother vibrations,
  while higher values create a more sharp sensation.

  | **Note:** Setting an initial sharpness is optional. If omitted, the framework defaults the initial sharpness to the value of the first control point.
- A **duration** value, which represents the time, in milliseconds, taken to
  transition from the last control point---that is, an intensity and sharpness
  pair---to the new one.

| **Caution:** When using the basic envelope API for envelope based vibrations, check that your effect concludes with a control point of zero intensity. Otherwise, an [`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException) occurs.

Here is an example waveform that ramps up the intensity from a low-pitch to a
high-pitch, maximum-strength vibration over 500 ms and then ramps back down to
\\( 0 \\) (off) over 100 ms.  

    vibrator.vibrate(VibrationEffect.BasicEnvelopeBuilder()
        .setInitialSharpness(0.0f)
        .addControlPoint(1.0f, 1.0f, 500)
        .addControlPoint(0.0f, 1.0f, 100)
        .build()
    )

If you have more advanced knowledge of haptics, you can define envelope effects
using `WaveformEnvelopeBuilder`. When using this object, you can access the
[frequency-to-output-acceleration mapping (FOAM)](https://developer.android.com/develop/ui/views/haptics/actuators#vibrator-output-acceleratio) through the
[`VibratorFrequencyProfile`](https://developer.android.com/reference/android/os/vibrator/VibratorFrequencyProfile).

- An amplitude value in the range \\( \[0, 1\] \\), which represents the achievable vibration strength at given frequency, as determined by the device FOAM. For example, a value of \\( 0.5 \\) generates half the maximum output acceleration that can be achieved at the given frequency.
- A **frequency** value, specified in Hertz.

  | **Note:** Setting an initial frequency for `WaveformEnvelopeBuilder` is optional. If omitted, the framework defaults the initial frequency to the value of the first control point.
- A **duration** value, which represents the time, in milliseconds, taken to
  transition from the last control point to the new one.

| **Note:** To help your vibration patterns play correctly, use frequencies within the device's capabilities. The system completely ignores vibration effects that contain unsupported frequencies. Refer to the [`VibratorFrequencyProfile` API
| reference](https://developer.android.com/reference/android/os/vibrator/VibratorFrequencyProfile) to determine the supported frequency range. In addition, check device support for envelope effects using [`VibratorEnvelopeEffectInfo`](https://developer.android.com/reference/android/os/vibrator/VibratorEnvelopeEffectInfo).

The following code shows an example waveform that defines a 400 ms vibration
effect. It begins with a 50 ms amplitude ramp, from off to full, at a constant
60 Hz. Then, the frequency ramps up to 120 Hz over the next 100 ms and remains
at that level for 200 ms. Finally, the amplitude ramps down to \\( 0 \\), and
the frequency returns to 60 Hz over the last 50 ms:  

    vibrator.vibrate(VibrationEffect.WaveformEnvelopeBuilder()
        .addControlPoint(1.0f, 60f, 50)
        .addControlPoint(1.0f, 120f, 100)
        .addControlPoint(1.0f, 120f, 200)
        .addControlPoint(0.0f, 60f, 50)
        .build()
    )

The following sections provide several examples of vibration waveforms with
envelopes.

### Bouncing spring

A previous sample uses [`PRIMITIVE_THUD`](https://developer.android.com/reference/android/os/VibrationEffect.Composition#PRIMITIVE_THUD) to simulate [physical bounce
interactions](https://developer.android.com/develop/ui/views/haptics/custom-haptic-effects#bounce). The [basic envelope API](https://developer.android.com/reference/android/os/VibrationEffect.BasicEnvelopeBuilder) offers significantly finer
control, allowing you to precisely tailor vibration intensity and sharpness.
This results in haptic feedback that more accurately follows animated events.

Here's an example of a free-falling spring with the animation enhanced with a
basic envelope effect played each time the spring bounces off the bottom of the
screen:  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of a dropped spring bouncing off the bottom of the screen.](https://developer.android.com/static/develop/ui/views/haptics/images/bouncing-spring.gif)  
![Plot of input vibration waveform.](https://developer.android.com/static/develop/ui/views/haptics/images/spring-waveform-graph.svg)

**Figure 5.** An output acceleration waveform graph for a vibration that
simulates a bouncing spring.  

    @Composable
    fun BouncingSpringAnimation() {
      var springX by remember { mutableStateOf(SPRING_WIDTH) }
      var springY by remember { mutableStateOf(SPRING_HEIGHT) }
      var velocityX by remember { mutableFloatStateOf(INITIAL_VELOCITY) }
      var velocityY by remember { mutableFloatStateOf(INITIAL_VELOCITY) }
      var sharpness by remember { mutableFloatStateOf(INITIAL_SHARPNESS) }
      var intensity by remember { mutableFloatStateOf(INITIAL_INTENSITY) }
      var multiplier by remember { mutableFloatStateOf(INITIAL_MULTIPLIER) }
      var bottomBounceCount by remember { mutableIntStateOf(0) }
      var animationStartTime by remember { mutableLongStateOf(0L) }
      var isAnimating by remember { mutableStateOf(false) }

      val (screenHeight, screenWidth) = getScreenDimensions(context)

      LaunchedEffect(isAnimating) {
        animationStartTime = System.currentTimeMillis()
        isAnimating = true

        while (isAnimating) {
          velocityY += GRAVITY
          springX += velocityX.dp
          springY += velocityY.dp

          // Handle bottom collision
          if (springY > screenHeight - FLOOR_HEIGHT - SPRING_HEIGHT / 2) {
            // Set the spring's y-position to the bottom bounce point, to keep it
            // above the floor.
            springY = screenHeight - FLOOR_HEIGHT - SPRING_HEIGHT / 2

            // Reverse the vertical velocity and apply damping to simulate a bounce.
            velocityY *= -BOUNCE_DAMPING
            bottomBounceCount++

            // Calculate the fade-out duration of the vibration based on the
            // vertical velocity.
            val fadeOutDuration =
                ((abs(velocityY) / GRAVITY) * FRAME_DELAY_MS).toLong()

            // Create a "boing" envelope vibration effect that fades out.
            vibrator.vibrate(
                VibrationEffect.BasicEnvelopeBuilder()
                    // Starting from zero sharpness here, will simulate a smoother
                    // "boing" effect.
                    .setInitialSharpness(0f)

                    // Add a control point to reach the desired intensity and
                    // sharpness very quickly.
                    .addControlPoint(intensity, sharpness, 20L)

                    // Add a control point to fade out the vibration intensity while
                    // maintaining sharpness.
                    .addControlPoint(0f, sharpness, fadeOutDuration)
                    .build()
            )

            // Decrease the intensity and sharpness of the vibration for subsequent
            // bounces, and reduce the multiplier to create a fading effect.
            intensity *= multiplier
            sharpness *= multiplier
            multiplier -= 0.1f
          }

          if (springX > screenWidth - SPRING_WIDTH / 2) {
            // Prevent the spring from moving beyond the right edge of the screen.
            springX = screenWidth - SPRING_WIDTH / 2
          }

          // Check for 3 bottom bounces and then slow down.
          if (bottomBounceCount >= MAX_BOTTOM_BOUNCE &&
                System.currentTimeMillis() - animationStartTime > 1000) {
            velocityX *= 0.9f
            velocityY *= 0.9f
          }

          delay(FRAME_DELAY_MS) // Control animation speed.

          // Determine if the animation should continue based on the spring's
          // position and velocity.
          isAnimating = (springY < screenHeight + SPRING_HEIGHT ||
                springX < screenWidth + SPRING_WIDTH)
            && (velocityX >= 0.1f || velocityY >= 0.1f)
        }
      }

      Box(
        modifier = Modifier
          .fillMaxSize()
          .noRippleClickable {
            if (!isAnimating) {
              resetAnimation()
            }
          }
          .width(screenWidth)
          .height(screenHeight)
      ) {
        DrawSpring(mutableStateOf(springX), mutableStateOf(springY))
        DrawFloor()
        if (!isAnimating) {
          DrawText("Tap to restart")
        }
      }
    }

### Rocket launch

A previous sample shows how to use the basic envelope API to
simulate a bouncy spring reaction. The [`WaveformEnvelopeBuilder`](https://developer.android.com/reference/android/os/VibrationEffect.WaveformEnvelopeBuilder) unlocks
precise control over the device's full frequency range, enabling highly
customized haptic effects. By combining this with FOAM data, you can tailor
vibrations to specific frequency capabilities.

Here's an example which demonstrates a rocket launch simulation using a dynamic
vibration pattern. The effect goes from the minimum supported frequency
acceleration output, 0.1 G, to the resonant frequency, always maintaining a 10%
amplitude input. This lets the effect start with a reasonably strong output and
increase the perceived intensity and sharpness, even though the driving
amplitude is the same. Upon reaching resonance, the effect frequency descends
back to the minimum, which is perceived as descending intensity and sharpness.
This creates a sensation of initial resistance followed by a release, mimicking
a launch into space.

This effect isn't possible with the basic envelope API, as it abstracts away the
device-specific information about its resonant frequency and output acceleration
curve. Increasing sharpness can push the equivalent frequency beyond resonance,
potentially causing an unintended acceleration dip.  
![](https://developer.android.com/static/develop/ui/views/haptics/images/demo-portrait.svg) ![Animation of a rocket ship taking off from the bottom of the screen.](https://developer.android.com/static/develop/ui/views/haptics/images/rocket-launch.gif)  
![Plot of input vibration waveform.](https://developer.android.com/static/develop/ui/views/haptics/images/rocket-waveform-graph.svg)

**Figure 6.** An output acceleration waveform graph for a vibration that
simulates a rocket launch.  

    @Composable
    fun RocketLaunchAnimation() {
      val context = LocalContext.current
      val screenHeight = remember { mutableFloatStateOf(0f) }
      var rocketPositionY by remember { mutableFloatStateOf(0f) }
      var isLaunched by remember { mutableStateOf(false) }
      val animation = remember { Animatable(0f) }

      val animationDuration = 3000
      LaunchedEffect(isLaunched) {
        if (isLaunched) {
          animation.animateTo(
            1.2f, // Overshoot so that the rocket goes off the screen.
            animationSpec = tween(
              durationMillis = animationDuration,
              // Applies an easing curve with a slow start and rapid acceleration
              // towards the end.
              easing = CubicBezierEasing(1f, 0f, 0.75f, 1f)
            )
          ) {
            rocketPositionY = screenHeight.floatValue * value
          }
          animation.snapTo(0f)
          rocketPositionY = 0f;
          isLaunched = false;
        }
      }

      Box(
        modifier = Modifier
          .fillMaxSize()
          .noRippleClickable {
            if (!isLaunched) {
              // Play vibration with same duration as the animation, using 70% of
              // the time for the rise of the vibration, to match the easing curve
              // defined previously.
              playVibration(vibrator, animationDuration, 0.7f)
              isLaunched = true
            }
          }
          .background(Color(context.getColor(R.color.background)))
          .onSizeChanged { screenHeight.floatValue = it.height.toFloat() }
      ) {
        drawRocket(rocketPositionY)
      }
    }

    private fun playVibration(
      vibrator: Vibrator,
      totalDurationMs: Long,
      riseBias: Float,
      minOutputAccelerationGs: Float = 0.1f,
    ) {
      require(riseBias in 0f..1f) { "Rise bias must be between 0 and 1." }

      if (!vibrator.areEnvelopeEffectsSupported()) {
        return
      }

      val resonantFrequency = vibrator.resonantFrequency
      if (resonantFrequency.isNaN()) {
        // Device doesn't have or expose a resonant frequency.
        return
      }

      val startFrequency = vibrator.frequencyProfile?.getFrequencyRange(minOutputAccelerationGs)?.lower ?: return

      if (startFrequency >= resonantFrequency) {
        // Vibrator can't generate the minimum required output at lower frequencies.
        return
      }

      val minDurationMs = vibrator.envelopeEffectInfo.minControlPointDurationMillis
      val rampUpDurationMs = (riseBias * totalDurationMs).toLong() - minDurationMs
      val rampDownDurationMs = totalDurationMs - rampUpDuration - minDurationMs

      vibrator.vibrate(
        VibrationEffect.WaveformEnvelopeBuilder()
          // Quickly reach the desired output at the start frequency
          .addControlPoint(0.1f, startFrequency, minDurationMs)
          .addControlPoint(0.1f, resonantFrequency, rampUpDurationMs)
          .addControlPoint(0.1f, startFrequency, rampDownDurationMs)

          // Controlled ramp down to zero to avoid ringing after the vibration.
          .addControlPoint(0.0f, startFrequency, minDurationMs)
          .build()
      )
    }