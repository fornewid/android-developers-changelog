---
title: https://developer.android.com/studio/run/emulator-networking-voice
url: https://developer.android.com/studio/run/emulator-networking-voice
source: md.txt
---

The emulator automatically forwards simulated voice calls and SMS messages
from one instance to another. To send a voice call or SMS, use the dialer app
or SMS app, respectively, from one of the emulators.

To initiate a simulated voice call to another emulator instance:

1. Launch the dialer app on the originating emulator instance.
2. As the number to dial, enter the console port number of the target instance.

You can determine the console port number of the target instance by checking
its window title, if it is running in a separate window, but not if it is
running in a tool window. The console port number is reported as "Android
Emulator (\<port\>)".

Alternatively, the `adb devices` command prints a list of running virtual
devices and their console port numbers. For more information, see [Query for
devices](https://developer.android.com/studio/command-line/adb#devicestatus).

1. Click the dial button. A new inbound call appears in the target emulator instance.

To send an SMS message to another emulator instance:

1. If an SMS app is available, launch it.
2. Specify the console port number of the target emulator instance as the SMS address.
3. Enter the message text.
4. Send the message. The message is delivered to the target emulator instance.

You can also connect to an emulator console to simulate an incoming voice call
or SMS. For more information, see [Telephony emulation](https://developer.android.com/studio/run/emulator-console#telephony)
and [SMS emulation](https://developer.android.com/studio/run/emulator-console#sms).