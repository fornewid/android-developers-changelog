---
title: https://developer.android.com/develop/ui/compose/system/pip-remote-actions
url: https://developer.android.com/develop/ui/compose/system/pip-remote-actions
source: md.txt
---

If you want to add controls (play, pause, etc.) to your PiP window, create a
[`RemoteAction`](https://developer.android.com/reference/android/app/RemoteAction) for each control you want to add.

> [!NOTE]
> **Note:** If you are using a [`MediaSession`](https://developer.android.com/guide/topics/media/media3), there will be default actions added to the window that you don't need to implement yourself.

1. Add constants for your broadcast controls:

   ```kotlin
   // Constant for broadcast receiver
   const val ACTION_BROADCAST_CONTROL = "broadcast_control"

   // Intent extras for broadcast controls from Picture-in-Picture mode.
   const val EXTRA_CONTROL_TYPE = "control_type"
   const val EXTRA_CONTROL_PLAY = 1
   const val EXTRA_CONTROL_PAUSE = 2
   ```
2. Create a list of [`RemoteActions`](https://developer.android.com/reference/android/app/RemoteAction) for the controls in your PiP window.
3. Next, add a [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver) and override `onReceive()` to set the actions of each button. Use a [`DisposableEffect`](https://developer.android.com/develop/ui/compose/side-effects#disposableeffect) to register the receiver and the remote actions. When the player is disposed, unregister the receiver.

   ```kotlin
   @RequiresApi(Build.VERSION_CODES.O)
   @Composable
   fun PlayerBroadcastReceiver(player: Player?) {
       val isInPipMode = rememberIsInPipMode()
       if (!isInPipMode || player == null) {
           // Broadcast receiver is only used if app is in PiP mode and player is non null
           return
       }
       val context = LocalContext.current

       DisposableEffect(player) {
           val broadcastReceiver: BroadcastReceiver = object : BroadcastReceiver() {
               override fun onReceive(context: Context?, intent: Intent?) {
                   if ((intent == null) || (intent.action != ACTION_BROADCAST_CONTROL)) {
                       return
                   }

                   when (intent.getIntExtra(EXTRA_CONTROL_TYPE, 0)) {
                       EXTRA_CONTROL_PAUSE -> player.pause()
                       EXTRA_CONTROL_PLAY -> player.play()
                   }
               }
           }
           ContextCompat.registerReceiver(
               context,
               broadcastReceiver,
               IntentFilter(ACTION_BROADCAST_CONTROL),
               ContextCompat.RECEIVER_NOT_EXPORTED
           )
           onDispose {
               context.unregisterReceiver(broadcastReceiver)
           }
       }
   }
   ```
4. Pass in a list of your remote actions to the [`PictureInPictureParams.Builder`](https://developer.android.com/reference/android/app/PictureInPictureParams.Builder):

   ```kotlin
   val context = LocalContext.current

   val pipModifier = modifier.onGloballyPositioned { layoutCoordinates ->
       val builder = PictureInPictureParams.Builder()
       builder.setActions(
           listOfRemoteActions()
       )

       if (shouldEnterPipMode && player != null && player.videoSize != VideoSize.UNKNOWN) {
           val sourceRect = layoutCoordinates.boundsInWindow().toAndroidRectF().toRect()
           builder.setSourceRectHint(sourceRect)
           builder.setAspectRatio(
               Rational(player.videoSize.width, player.videoSize.height)
           )
       }

       if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
           builder.setAutoEnterEnabled(shouldEnterPipMode)
       }
       context.findActivity().setPictureInPictureParams(builder.build())
   }
   VideoPlayer(modifier = pipModifier)
   ```

## Next steps

- See the [Socialite](https://github.com/android/socialite) app to see the best practices of Compose PiP in action.
- See the [PiP design guidance](https://developer.android.com/design/ui/mobile/guides/home-screen/picture-in-picture) for more information.