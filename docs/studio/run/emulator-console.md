---
title: Send emulator console commands  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/run/emulator-console
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Send emulator console commands Stay organized with collections Save and categorize content based on your preferences.




Each running virtual device provides a console that lets you query and control the emulated
device environment. For example, you can use the console to manage port redirection, network
characteristics, and telephony events while your app is running on the emulator.

The following commands require that you already have an emulator running. For more
information about running an emulator, see
[Run apps on the Android Emulator](/studio/run/emulator) and
[Start the emulator from the command line](/studio/run/emulator-commandline).

## Start and stop a console session

To access the console and enter commands from a terminal window, use `telnet` to
connect to the console port and provide your authentication token. Each time the console displays
**OK**, it's ready to accept commands. There isn't a typical prompt.

To connect to the console of a running virtual device:

1. Open a terminal window and enter the following command:

```
telnet localhost console-port
```

The emulator window title lists the console port number when running in a separate window but
not when running in a tool window. For example, the window title for an emulator using console port 5554
could be `Pixel8_API_34:5554`. Also, the `adb devices` command prints a
list of running virtual devices and their console port numbers. For more information, see
[Query for devices](/studio/command-line/adb#devicestatus).

**Note:** The emulator listens for connections on ports 5554 to 5585
and accepts connections from `localhost` only.

2. After the console displays `OK`, enter the `auth
   auth_token` command.

Before you can enter [console commands](#querycontrol), the emulator console
requires authentication. `auth_token` must
match the contents of the `.emulator_console_auth_token` file in your home directory.

If that file doesn't exist, the `telnet localhost console-port`
command creates the file, which contains a randomly generated authentication token. To disable
authentication, delete the token from the
`.emulator_console_auth_token` file or create an empty file if it doesn't exist.

3. After you're connected to the console, enter [console commands](#querycontrol).

Enter `help`, `help command`, or `help-verbose`
to see a list of console commands and learn about specific
commands.

4. To exit the console session, enter `quit` or `exit`.

Here's an example session:

```
$ telnet localhost 5554
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Android Console: Authentication required
Android Console: type 'auth <auth_token>' to authenticate
Android Console: you can find your <auth_token> in
'/Users/me/.emulator_console_auth_token'
OK
auth 123456789ABCdefZ
Android Console: type 'help' for a list of commands
OK
help-verbose
Android console command help:
    help|h|?         Prints a list of commands
    help-verbose     Prints a list of commands with descriptions
    ping             Checks if the emulator is alive
    automation       Manages emulator automation
    event            Simulates hardware events
    geo              Geo-location commands
    gsm              GSM related commands
    cdma             CDMA related commands
    crash            Crashes the emulator instance
    crash-on-exit    Simulates crash on exit for the emulator instance
    kill             Terminates the emulator instance
    restart          Restarts the emulator instance
    network          Manages network settings  (ethernet and cellular only)
    power            Power related commands
    quit|exit        Quits control session
    redir            Manages port redirections
    sms              SMS related commands
    avd              Controls virtual device execution
    qemu             QEMU-specific commands
    sensor           Manages emulator sensors
    physics          Manages physical model
    finger           Manages emulator finger print
    debug            Controls the emulator debug output tags
    rotate           Rotates the screen clockwise by 90 degrees
    screenrecord     Records the emulator's display
    fold             Folds the device
    unfold           Unfolds the device
    multidisplay     Configures the multi-display
    nodraw           turn on/off NoDraw mode. (experimental)
    resize-display   resize the display resolution to the preset size
    virtualscene-image  customize virtualscene image for virtulscene camera
    proxy            manage network proxy server settings
    phonenumber      set phone number for the device


try 'help <command>' for command-specific help
OK
exit
Connection closed by foreign host.
```

## Emulator command reference

The following table describes the emulator console commands with their parameters and values:

**Table 1.** Emulator console commands

| General commands | Description |
| --- | --- |
| `avd {stop|start|status|name}` | Queries, controls, and manages the virtual device, as follows:  * `stop`: Stops the execution of the device. * `start`: Starts the execution of the device. * `status`: Queries the virtual device status, which can be `running`   or `stopped`. * `name`: Queries the virtual device name. |
| `avd snapshot {list|save name|load name|delete name}` | Saves and restores the device state in snapshots, as follows:  * `list`: Lists all saved snapshots. * `save name`: Saves the snapshot as name. * `load name`: Loads the named snapshot. * `delete name`: Deletes the named snapshot.   The following example saves a snapshot with the name `firstactivitysnapshot`:     ``` avd snapshot save firstactivitysnapshot ``` |
| `fold` | Folds the device to display its smaller screen configuration, if the device is foldable and currently unfolded. |
| `unfold` | Unfolds the device to display its larger screen configuration, if the device is foldable and currently folded. |
| `kill` | Terminates the virtual device. |
| `ping` | Checks whether the virtual device is running. |
| `rotate` | Rotates the AVD counterclockwise in 45 degree increments. |
| Crash the emulator | Description |
| `crash` | Crashes the emulator during app execution. |
| `crash-on-exit` | Crashes the emulator when the app exits. |
| Debug tags | Description |
| `debug tags ...` | Enables or disables debug messages from specific parts of the emulator. The tags parameter must be a value from the list of debug tags that appears when you execute `emulator -help-debug-tags`. For more information about the `-help-debug-tags` option, see the table of [commonly used options](/studio/run/emulator-commandline#common).  The following example enables the `radio` tag:     ``` debug radio ``` |
| Port redirection | Description |
| `redir list` | Lists the current port redirection. |
| `redir add protocol:host-port:guest-port` | Adds a new port redirection, as follows:  * `protocol`: Must be either `tcp`   or `udp`. * `host-port`: The port number to open on the host. * `guest-port`: The port number to route data to on the   emulator. |
| `redir del protocol:host-port` | Deletes a port redirection.  * `protocol`: Must be either `tcp`   or `udp`. * `host-port`: The port number to open on the host. |
| Geographic location | Description |
| Sets the geographic location reported to the apps running inside an emulator by sending a GPS fix to the emulator.  You can issue one of the following `geo` command as soon as a virtual device is running. The emulator sets the location you enter by creating a mock location provider. This provider responds to location listeners set by apps and supplies the location to the `LocationManager`. Any app can query the location manager to obtain the current GPS fix for the emulated device by calling `LocationManager.getLastKnownLocation("gps")`. | |
| `geo fix longitude latitude [altitude] [satellites] [velocity]` | Sends a simple GPS fix to the emulator. Specify `longitude` and `latitude` in decimal degrees. Use a number from 1 to 12 to specify the number of `satellites` to use to determine the position, and specify `altitude` in meters and `velocity` in knots. |
| `geo nmea sentence` | Sends an NMEA 0183 sentence to the emulated device as if it were sent from an emulated GPS modem. Start `sentence` with '$GP'. Only '$GPGGA' and '$GPRCM' sentences are currently supported. The following example is a GPGGA (Global Positioning System Fix Data) sentence that gets the time, position, and fix data for a GPS receiver:    ``` geo nmea $GPGGA ,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx ``` |
| Fake hardware events | Description |
| `event types` | Lists all fake event types. For events that have codes, the number of codes is listed in parentheses on the right. ``` event types event &lttype> can be an integer or one of the following aliases:     EV_SYN     EV_KEY    (405 code aliases)     EV_REL    (2 code aliases)     EV_ABS    (27 code aliases)     EV_MSC     EV_SW     (4 code aliases)     EV_LED     EV_SND     EV_REP     EV_FF     EV_PWR     EV_FF_STATUS     EV_MAX OK ``` |
| `event send types [types ...]` | Sends one or more fake event types. |
| `event codes type` | Lists the event codes for the specified fake event type. |
| `event send type[:code]:[value] [...]` | Sends one or more fake events with optional codes and code values. To discover exactly which event to send, you can use the `adb` command while manually pressing the buttons on the emulator.  These are the events generated when you press the power button:    ``` adb shell getevent -lt  /dev/input/event12: EV_KEY       KEY_POWER            DOWN /dev/input/event12: EV_SYN       SYN_REPORT           00000000 /dev/input/event12: EV_KEY       KEY_POWER            UP /dev/input/event12: EV_SYN       SYN_REPORT           00000000 ```  For example, to simulate a long press of the power button, send two `EV_KEY` events for keydown and keyup:    ``` event send EV_KEY:KEY_POWER:0 OK event send EV_KEY:KEY_POWER:1 OK ``` |
| `event text message` | Sends a string of characters that simulate keypresses. The message must be a UTF-8 string. Unicode posts are reverse-mapped according to the current device keyboard, and unsupported characters are discarded silently. |
| Power state controls | Description |
| `power display` | Displays battery and charger state. |
| `power ac {on|off}` | Sets AC charging state to `on` or `off`. |
| `power status {unknown|charging|discharging|not-charging|full}` | Changes battery status as specified. |
| `power present {true|false}` | Sets battery presence state. |
| `power health {unknown|good|overheat|dead|overvoltage|failure}` | Sets battery health state. |
| `power capacity percent` | Sets remaining battery capacity state as a percent from 0 to 100. |
| Network connection status   (Ethernet and Cellular only) | Description |
| `network status` | Checks the network status and current delay and speed characteristics. |
| `network delay latency` | Changes the emulated network latency.  The emulator lets you simulate various network latency levels so that you can test your app in an environment more typical of actual running conditions. You can set a latency level or range at emulator startup, or you can use the console to change the latency while the app is running in the emulator.  The format of network latency is one of the following (numbers are milliseconds):  **Network latency format:**   * `gprs`: GPRS, which uses a latency range of 150 minimum and 550 maximum. * `edge`: EDGE/EGPRS, which uses a latency range of 80 minimum and 400 maximum. * `umts`: UMTS/3G, which uses a latency range of 35 minimum and 200 maximum. * `none`: No latency. * `num`: Emulates the specified latency in milliseconds. * `min:max`: Emulates the specified latency range.   To set latency at emulator startup, use the `-netdelay` [emulator option](/studio/run/emulator-commandline#common) with a supported `latency` value, as listed in the preceding **Network latency format** list. Here are some examples:     ``` emulator -netdelay gprs emulator -netdelay 40,100 ```   To make changes to network delay while the emulator is running, connect to the console and use the `netdelay` command with a supported `latency` value from the preceding **Network latency format** list.     ``` network delay gprs network delay 40 100 ``` |
| `network speed speed` | The emulator lets you simulate various network transfer rates. You can set a transfer rate or range at emulator startup, or you can use the console to change the rate while the app is running in the emulator.  The format of network `speed` is one of the following (numbers are kilobits/sec):  **Network speed format:**   * `gsm`: GSM/CSD, which uses a speed of 14.4 up and 14.4 down. * `hscsd`: HSCSD, which uses a speed of 14.4 up and 43.2 down. * `gprs`: GPRS, which uses a speed of 40.0 up and 80.0 down. * `edge`: EDGE/EGPRS, which uses a speed of 118.4 up and 236.8 down. * `umts`: UMTS/3G, which uses a speed of 128.0 up and 1920 down. * `hsdpa`: HSDPA, which uses a speed of 348.0 up and 14,400.0 down. * `lte`: LTE, which uses a speed of 58,000 up and 173,000 down. * `evdo`: EVDO, which uses a speed of 75,000 up and 280,000 down. * `full`: Unlimited speed, but depends on the connection speed of your   computer. * `num`: Sets an exact rate in kilobits/sec used for both upload   and download. * `up:down`: Sets exact rates in kilobits/sec for   upload and download separately.   To set the network speed at emulator startup, use the `-netspeed` [emulator option](/studio/run/emulator-commandline#common) with a supported `speed` value, as in the preceding **Network speed format** list. Here are some examples:     ``` emulator -netspeed gsm @Pixel_API_26 emulator -netspeed 14.4,80 @Pixel_API_26 ```   To make changes to network speed while the emulator is running, connect to the console and use the `network speed` command with a supported `speed` value from the preceding **Network speed format** list.     ``` network speed 14.4 80 ``` |
| `network capture {start|stop} file` | Sends packets to a file. The following list describes the parameters and parameter values:  * `start file`: Starts sending packets to the specified file. * `stop file`: Stops sending packets to the specified file. |
| Telephony emulation | Description |
| The Android emulator includes its own GSM and CDMA emulated modems that let you simulate telephony functions in the emulator. For example, with GSM you can simulate inbound phone calls and establish and terminate data connections. With CDMA, you provide a subscription source and the preferred roaming list. The Android system handles simulated calls exactly as it would actual calls. The emulator doesn't support call audio. | |
| `gsm {call|accept|cancel|busy} phonenumber` | The `gsm` parameters are the following:  * `call`: Simulates an inbound phone call   from `phonenumber`. * `accept`: Accepts an inbound call from `phonenumber`   and changes the call state to `active`. You can   change a call state to `active` only when its   current state is `waiting` or `held`. * `cancel`: Terminates an inbound phone call from or outbound   phone call to `phonenumber`. * `busy`: Closes an outbound call to   `phonenumber` and changes the call state to `busy`.   You can change a call state to `busy` only when its current state is   `waiting`. |
| `gsm {data|voice} state` | The `data state` command changes the state of the GPRS data connection, and the `data voice state` command changes the state of the GPRS voice connection, as follows:  * `unregistered`: No network available. * `home`: On local network, non-roaming. * `roaming`: On roaming network. * `searching`: Searching networks. * `denied`: Emergency calls only. * `off`: Same as `unregistered`. * `on`: Same as `home`. |
| `gsm hold` | Changes the state of a call to `hold`. You can change a call state to `hold` only when its current state is `active` or `waiting`. |
| `gsm list` | Lists all inbound and outbound calls and their states. |
| `gsm status` | Reports the current GSM voice/data state. Values are those described for the `voice` and `data` commands. |
| `gsm signal {rssi|ber}` | Changes the reported signal strength (rssi) and bit error rate (ber) on the next 15 seconds of update. The following list describes the parameters and their values:  * `rssi` range is 0 through 31 and 99 for unknown. * `ber` range is 0 through 7 and 99 for unknown. |
| `gsm signal-profile num` | Sets the signal strength profile. `num` is a number from 0 through 4. |
| `cdma ssource source` | Sets the current CDMA subscription source, where `source` is a network-based allowlist that contains the CDMA carrier's subscribers and their values, as follows:  * nv: Reads subscription from non-volatile RAM. * ruim: Reads subscription from Removable User Identity Module (RUIM). |
| `cdma prl_version version` | Dumps the current preferred roaming list (PRL) version. The version number is for the PRL database that contains information used during the system selection and acquisition process. |
| Manage sensors on the emulator | Description |
| These commands relate to which sensors are available in the AVD. Besides using the `sensor` command, you can see and adjust the settings in the emulator in the **Virtual sensors** screen in the **Accelerometer** and **Additional sensors** tabs. | |
| `sensor status` | Lists all sensors and their status. The following is example output for the `sensor status` command: |
| `sensor get sensor-name` | Gets the settings for `sensor-name`. The following example gets the value for the acceleration sensor:    ``` sensor get acceleration acceleration = 2.23517e-07:9.77631:0.812348 ```   The `acceleration` values separated by colons(:) refer to the x, y, and z coordinates for the virtual sensors. |
| `sensor set sensor-name value-x:value-y:value-z` | Sets the values for `sensor-name`. The following example sets the acceleration sensor to the x, y, and z values separated by colons.    ``` sensor set acceleration 2.23517e-07:9.77631:0.812348 ``` |
| SMS emulation | Description |
| `sms send sender-phone-number textmessage` | Generates an emulated incoming SMS. The following list describes the parameters and their values:  * `sender-phone-number`: Contains an arbitrary numeric string. * `textmessage`: The sms message.   The following example sends the message "hi there" to the 4085555555 phone number:     ``` sms send 4085555555 hi there ```   The console forwards the SMS message to the Android framework, which passes it to an app on the emulator that handles SMS, such as the Messages app. If you pass 10 numbers, the app formats it as a phone number. Longer or shorter numeric strings display the way you sent them. |
| Fingerprint simulation | Description |
| `finger touch fingerprint-id` | Simulates a finger touching the sensor. |
| `finger remove` | Simulates finger removal. For instructions about how to use these commands, see the following section about [fingerprint simulation and validation](#finger-print). |
|

### Fingerprint simulation and validation

![](/static/studio/images/run/fingerprint_2x.png)

**Figure 1.** Fingerprint authentication screen.

Use the `finger` command to simulate and validate fingerprint authentication for your
app. You need SDK Tools 24.3 or higher and Android 6.0 (API level 23) or higher.

To simulate and validate fingerprint authentication, follow these steps:

1. If you don't yet have a fingerprint ID, enroll a new fingerprint in the emulator
   by selecting **Settings** > **Security** > **Fingerprint** and following the
   enrollment instructions.
2. Set up your app to accept
   [fingerprint
   authentication](/about/versions/marshmallow/android-6.0#fingerprint-authentication). After you perform this setup, your device displays the fingerprint
   authentication screen.
3. While your app displays the fingerprint authentication screen, go to the console and
   enter the `finger touch` command and the fingerprint ID you created. This
   simulates a finger touch.
4. Then, enter the `finger remove` command to simulate finger removal.

   Your app should respond as if a user touched and then removed their finger from the
   fingerprint sensor.