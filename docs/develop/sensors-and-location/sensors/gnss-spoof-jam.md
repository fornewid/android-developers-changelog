---
title: https://developer.android.com/develop/sensors-and-location/sensors/gnss-spoof-jam
url: https://developer.android.com/develop/sensors-and-location/sensors/gnss-spoof-jam
source: md.txt
---

GNSS interference can be broken down into the following two categories:

- Jamming
- Spoofing

*Jamming* attacks involve broadcasting strong radio signals in the same
frequency range as GNSS, which can drown out the relatively weaker signals
broadcast from the GNSS satellites. This can prevent GNSS receivers, including
phones, from computing their location.

*Spoofing* is a more sophisticated attack during which fake signals that pretend
to be real GNSS signals are broadcast. These fake signals can fool a GNSS
receiver into computing a position or time that is very different from
reality, which is enough to confuse mapping and navigation apps into giving
users wrong information.

## About GNSS spoofing or jamming

Signal strength, or carrier-to-noise ratio (C/N0), of the signal as well as the
[automatic gain control (AGC)](https://developer.android.com/reference/android/location/GnssAutomaticGainControl) of the GNSS radio in the phone can be a good
indicator of interference.

The AGC tends to dip when spoofing or jamming is observed. When the radio
receives strong radio waves, it turns down the gain of the amplifier (AGC) to
adjust the power of the received signal.
![Comparison of signal strengths indicating interference](https://developer.android.com/static/images/sensors/gnss-spoof-scatter.png) **Figure 1.** AGC drops during interference (red area), and increases back to normal levels when interference is removed (green area). (Image source: https://doi.org/10.33012/navi.537)

However, the behavior of C/N0 changes between jamming and spoofing events. For
jamming events, the noise observed by the radio is much stronger than normal ---
therefore, the denominator of the carrier-to-noise ratio increases, and the C/N0
value drops. For spoofing, the reverse happens --- because a fake signal is being
broadcast that is loud enough to drown out the real signal from the satellite,
the overall signal strength is strong, and therefore the C/N0 increases.

## Check for GNSS spoofing or jamming

You can use the **Spoof/Jam** tab in the [GnssLogger](https://play.google.com/store/apps/details?id=com.google.android.apps.location.gps.gnsslogger) app to
explore the impact of their environment on C/N0 and AGC in real-time.

### Real-time AGC and C/N0 plot

The **Spoof/Jam** tab displays a real-time graph of AGC and C/N0 for each GNSS
constellation and band (e.g., "GPS L1" or "G:L1:", "Galileo E5a" or "E:E5A:").
![Graph of AGC and C/N0 for each GNSS constellation and band.](https://developer.android.com/static/images/sensors/gnss-spoof-all.png) **Figure 2.** AGC and C/N0 both drop when a phone is held next to a Wi-Fi router (red oval). The average top 3 signals for each constellation and band are shown as dashed lines. The AGC for each constellation and band, which is a single value, is shown as a solid line. The red circled section on the plot shows how both the AGC and C/N0 drop when the phone is held next to a Wi-Fi router, and therefore interference is observed.

### Real-time checks for spoofing and jamming

Below the real-time plot of AGC and [C/N0](http://c/N0), the app displays a
series of automated data checks that identify conditions related to GNSS
interference.
![UI displaying evidence of conditions
potentially caused by spoofing and jamming.](https://developer.android.com/static/images/sensors/gnss-spoof-spoof.png) **Figure 3.** Automated checks can identify conditions potentially caused by spoofing and jamming.

In the **Jamming checks** section, the app checks to see if the average of the
most recent 10 epochs of C/N0 and AGC have changed when compared to the previous
50 epochs. If C/N0 and AGC decrease simultaneously, this can be a symptom of
GNSS jamming. If this situation is detected, the card shows a FAIL message along
with more information:
![Conditions potentially caused by GNSS interference.](https://developer.android.com/static/images/sensors/gnss-spoof-jam.png) **Figure 4.** A failure indicating that conditions potentially caused by GNSS interference have been detected.

The first card in the **Spoofing checks** section also checks C/N0 and AGC, but
looks for a simultaneous **increase** in C/N0 and drop in AGC.

The second spoofing-related check looks for a difference over one second between
the GNSS time computed on the device and time retrieved over the Internet from a
Network Time Protocol (NTP) server (network time - GNSS time). A large
difference can indicate that the computed GNSS time is not valid.

### Tips, tricks, and caveats

Here are some things to keep in mind when using the **Spoof/Jam** feature of
GnssLogger:

- This is an experimental feature --- as we learn more about the AGC characteristics on various Android devices, the exact algorithms used for spoofing and jamming changes may be updated.
- This feature does not catch all spoofing and jamming --- The real-time graph and data checks make it easier to discover data properties in real-time, but aren't robust enough to detect every example of spoofing or jamming.
- This feature is designed to detect a change in C/N0 and AGC --- if you open the app in the presence of spoofing or jamming and C/N0 and AGC remain constant, spoofing and jamming are not detected.
- NTP servers are not necessarily secure --- Network time can be spoofed as well.

Provide feedback on the **Spoof/Jam** feature using our [public issue
tracker](https://issuetracker.google.com/issues/new?component=313183&template=0).