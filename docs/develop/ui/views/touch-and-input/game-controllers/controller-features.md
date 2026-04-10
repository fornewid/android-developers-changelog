---
title: https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-features
url: https://developer.android.com/develop/ui/views/touch-and-input/game-controllers/controller-features
source: md.txt
---

Game controllers are equipped with additional features that significantly
enhance player interaction and immersion. The haptics, motion sensors, and light
functionalities of Android game controllers are particularly instrumental in
deepening and enriching the gaming experience. Each feature uniquely stimulates
the player's senses, fostering more meaningful and intuitive interactions within
the game.

## Haptics

The haptics feature in Android game controllers is a crucial technology that
provides realistic tactile feedback during gameplay.

Haptics technology delivers physical sensations to the user through vibrations
or movements. For example, when an explosion occurs in the game, the controller
vibrates, allowing the player to feel the impact realistically. Additionally,
subtle vibrations can be synchronized with the sound of a character walking or
running, offering a more lifelike experience. This type of haptic feedback
enables players to physically feel various events happening within the game.

This technology maximizes player immersion, amplifies emotional responses, and
enriches the dynamics of the game. Haptics settings in Android game controllers
not only widen the creative possibilities for game developers but also provide
players with a gaming experience more realistic than ever before.

    fun triggerVibrationMultiChannel(
      deviceId: Int, leftIntensity: Int, leftDuration: Int,
      rightIntensity: Int, rightDuration: Int) {
      val inputDevice = InputDevice.getDevice(deviceId)
      val vibratorManager = inputDevice!!.vibratorManager
      if (vibratorManager != null) {
        val vibratorIds = vibratorManager.vibratorIds
        val vibratorCount = vibratorIds.size
        if (vibratorCount > 0) {
          // We have an assumption that game controllers have two vibrators
          // corresponding to a left motor and a right motor, and the left
          // motor will be first.
          updateVibrator(vibratorManager.getVibrator(vibratorIds[0]), leftIntensity, leftDuration)
          if (vibratorCount > 1) {
            updateVibrator(vibratorManager.getVibrator(vibratorIds[1]), rightIntensity, rightDuration)
          }
        }
      }
    }

    fun updateVibrator(vibrator: Vibrator?, intensity: Int, duration: Int) {
      if (vibrator != null) {
        if (intensity == 0) {
          vibrator.cancel()
        } else if (duration > 0) {
          vibrator.vibrate(VibrationEffect.createOneShot(duration.toLong(), intensity))
        }
      }
    }

To use vibrate, it sets a feature and permission.

    <application ...>
      ...
      <uses-feature android:name="android.hardware.gamepad" android:required="true"/>
      <uses-permission android:name="android.permission.VIBRATE"/>
      ...
    </application>

> [!NOTE]
> **Note:** When specifying `android:hardware:gamepad` support, don't set the `android:required` attribute to `true`. If you do this, users won't be able to install your app on the device.

For more information about
[`VibratorManager`](https://developer.android.com/reference/android/os/VibratorManager) and
[App manifest](https://developer.android.com/guide/topics/manifest/manifest-intro).

## Motion sensors

One of the most innovative technologies enhancing gameplay experiences is the
motion sensor-equipped Android game controller. This technology precisely
detects the physical movements of users and translates that data into actions
within the game, providing a more intuitive and immersive gaming experience.
In this introduction, we will explore how the motion sensor features in
Android game controllers works.

Motion sensors typically incorporate gyroscopes and accelerometers to detect the
movements and orientations of users.

It needs to implement acceleration and gyroscope listener classes and register
these listeners with the controller's sensor manager.

    fun setIntegratedAccelerometerActive(deviceId: Int) {
      val device = InputDevice.getDevice(deviceId)
      val sensorManager = device?.sensorManager
      val accelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
      if (accelerometer != null) {
        val accelerometerListener =
          GameControllerAccelerometerListener(accelerometer)
        sensorManager.registerListener(
          accelerometerListener, accelerometer,
          SensorManager.SENSOR_DELAY_GAME
        )
      }
    }

    fun setIntegratedGyroscopeActive(deviceId: Int) {
      val device = InputDevice.getDevice(deviceId)
      val sensorManager = device?.sensorManager
      val gyroscope = sensorManager?.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
      if (gyroscope != null) {
        val gyroscopeListener = GameControllerGyroscopeListener(gyroscope)
        sensorManager.registerListener(
          gyroscopeListener, gyroscope,
          SensorManager.SENSOR_DELAY_GAME
        )
      }
    }

    class GameControllerAccelerometerListener(private val listenerAccelerometer: Sensor?) :
      SensorEventListener {
      override fun onSensorChanged(event: SensorEvent) {
        if (listenerAccelerometer != null) {
          synchronized(listenerAccelerometer) {
            if (event.sensor == listenerAccelerometer) {
              Log.d("Accelerometer",
                "onSensorChanged " + event.values[0] + ", "
                + event.values[1] + ", " + event.values[2])
            }
          }
        }
      }

      override fun onAccuracyChanged(sensor: Sensor, accuracy: Int) {
      }
    }

    class GameControllerGyroscopeListener(private val listenerGyroscope: Sensor?) :
      SensorEventListener {
      override fun onSensorChanged(event: SensorEvent) {
        if (listenerGyroscope != null) {
          synchronized(listenerGyroscope) {
            if (event.sensor == listenerGyroscope) {
              Log.d("Gyroscope",
                "onSensorChanged " + event.values[0] + ", " +
                event.values[1] + ", " + event.values[2])
            }
          }
        }
      }

      override fun onAccuracyChanged(sensor: Sensor, accuracy: Int) {
      }
    }

For more information about
[Motion sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion) and
[`SensorEventListener`](https://developer.android.com/reference/android/hardware/SensorEventListener).

## Lights

The light color settings on Android game controllers add a new dimension of
immersion to gameplay through visual elements.

The light color feature utilizes built-in LED lights in the controller to
display various colors, which respond dynamically to different gaming scenarios.
For example, the lights might flash red when the player's health is critical or
glow green upon the completion of a specific mission, providing visual feedback
based on in-game events. These light color settings deepen user engagement,
heighten the suspense and enjoyment of the game, and help players immerse more
fully into the game world.

The light color features in Android game controllers serves more than a
mere decorative purpose---it plays a significant role in setting the mood of the
game and improving the user experience.

    fun changeControllerLightColor(deviceId: Int, color: Int) {
      val device = InputDevice.getDevice(deviceId)
      device?.let {
        if (it.sources and InputDevice.SOURCE_JOYSTICK == InputDevice.SOURCE_JOYSTICK) {
          val lightsManager = device.lightsManager
          lightsManager?.let { manager ->
            manager.lights.forEach { light ->
              val stateBuilder = LightState.Builder()
              stateBuilder.setColor(color)
              val requestBuilder = LightsRequest.Builder()
              requestBuilder.addLight(light, stateBuilder.build())
              val lightsSession = lightsManager.openSession()
              lightsSession.requestLights(requestBuilder.build())
            }
          }
        }
      }
    }

To use vibrate, it sets a feature and permission.

    <application ...>
      ...
      <uses-feature android:name="android.hardware.gamepad" android:required="true"/>
      <uses-permission android:name="android.permission.LIGHTS" />
      ...
    </application>

> [!NOTE]
> **Note:** When specifying `android:hardware:gamepad` support, don't set the `android:required` attribute to `"true"`. If you do this, users won't be able to install your app on the device.

For more information about
[`LightsManager`](https://developer.android.com/reference/android/hardware/lights/LightsManager) and
[App manifest](https://developer.android.com/guide/topics/manifest/manifest-intro).

## Controller touchpad

Some game controllers include a touchpad which can be used for a variety of
in-game actions, such as navigating menus or controlling game characters in a
more intuitive way.
![Touchpad on the game controller.](https://developer.android.com/static/images/training/game-controller-touchpad.png) **Figure 1.** Touchpad on the game controller.

Game controllers with integrated touchpads offer direct device control on
Android. Touching the touchpad generates an on-screen mouse pointer, allowing
for intuitive mouse-like navigation.