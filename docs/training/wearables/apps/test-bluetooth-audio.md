---
title: https://developer.android.com/training/wearables/apps/test-bluetooth-audio
url: https://developer.android.com/training/wearables/apps/test-bluetooth-audio
source: md.txt
---

# Test Bluetooth audio on emulators

On the Wear OS emulator, system images that run Wear OS 4 or higher include support for emulated Bluetooth. This support lets you test several use cases related to Bluetooth audio.

## Pair with an emulated phone

Using the emulator's Bluetooth support, you can pair with an emulated phone. To do so, enable the setup wizard from the command line:  

    -append-userspace-opt androidboot.setupwizard_mode=REQUIRED

## Play audio through an emulated output device

Using the emulator's Bluetooth support, you can also play audio through an emulated Bluetooth output device. To test audio output switching in the emulator, connect to an emulated Bluetooth output device using the open source[Bumble project](https://www.github.com/google/bumble).

### Prepare your environment

To prepare your development machine for using Bumble, complete the following steps:

1. Fetch the Bumble source code:

   ```
   git clone https://github.com/google/bumble
   ```
2. Navigate to the`bumble`directory, then build and install Bumble modules:

   ```
   cd bumble && python3 -m pip install "."
   ```

### Launch emulated Bluetooth speaker

To launch the emulated speaker, complete the following steps:

1. Launch a version of the emulator that supports Wear OS 4 or higher.

   **Note:** If you're using an emulator version lower than 33.1.10, launch the emulator from the command line using the`-packet-streamer-endpoint default`parameter.
2. To discover and connect to the emulated speaker, run the following command in the`bumble`directory:

   ```
   python3 examples/run_a2dp_sink.py examples/a2dp_sink1.json \
     android-netsim stdout | ffplay -i
   ```

   The audio output is played through your computer's speakers.

   You can also redirect output to a file:  

   ```
   python3 examples/run_a2dp_sink.py examples/a2dp_sink1.json \
     android-netsim output.sbc
   ```