---
title: https://developer.android.com/develop/connectivity/network-ops/network-access-optimization
url: https://developer.android.com/develop/connectivity/network-ops/network-access-optimization
source: md.txt
---

Using the wireless radio to transfer data is potentially one of your app's most
significant sources of battery drain. To minimize the battery drain associated
with network activity, it's critical that you understand how your connectivity
model will affect the underlying radio hardware.

This section introduces the wireless radio state machine and explains how your
app's connectivity model interacts with it. It then offers several techniques
which, when followed, will help minimize the effect of your app's data
consumption on the battery.

## The radio state machine

The wireless radio on your user's device has built-in power-saving features that
help minimize the amount of battery power it consumes. When fully active, the
wireless radio consumes significant power, but when inactive or in standby, the
radio consumes very little power.

One important factor to remember is that the radio cannot move from standby to
fully active instantaneously. There is a latency period associated with
"powering up" the radio. So the battery transitions from higher energy states to
lower energy states slowly in order to conserve power when not in use while
attempting to minimize the latency associated with "powering up" the radio.

The state machine for a typical 3G network radio consists of three energy states:

- **Full power**: Used when a connection is active, allowing the device to transfer data at its highest possible rate.
- **Low power**: An intermediate state that cuts battery power consumption by around 50%.
- **Standby**: The minimal power-consuming state during which no network connection is active.

While the low and standby states drain significantly less battery, they also
introduce significant latency to network requests. Returning to full power from
the low state takes around 1.5 seconds, and moving from standby to full power
can take over 2 seconds.

To minimize latency, the state machine uses a delay to postpone the transition
to lower energy states. Figure 1 uses AT\&T's timings for a typical 3G radio.

![](https://developer.android.com/static/images/develop/connectivity/mobile_radio_state_machine.png)   

**Figure 1.** Typical 3G wireless radio state machine.

The radio state machine on each device, particularly the associated transition
delay ("tail time") and startup latency, will vary based on the wireless radio
technology employed (3G, LTE, 5G, and so on) and is defined and configured by
the carrier network over which the device is operating.

This page describes a representative state machine for a typical 3G wireless
radio, based on data provided by AT\&T. However, the general principles and
resulting best practices are applicable for all wireless radio implementations.

This approach is particularly effective for typical mobile web browsing as it
prevents unwelcome latency while users browse the web. The relatively low
tail-time also ensures that once a browsing session has finished, the radio can
move to a lower energy state.

Unfortunately, this approach can lead to inefficient apps on modern smartphone
operating systems like Android, where apps run both in the foreground (where
latency is important) and in the background (where battery life should be
prioritized).

## How apps impact the radio state machine

Every time you create a new network connection, the radio transitions to the
full power state. In the case of the typical 3G radio state machine described
earlier, it will remain at full power for the duration of your transfer---plus
an additional 5 seconds of tail time---followed by 12 seconds at the low energy
state. So for a typical 3G device, every data transfer session will cause the
radio to draw energy for at least 18 seconds.

In practice, this means that an app which makes a one second data transfer,
three times a minute, will keep the wireless radio perpetually active, moving it
back to high power just as it is entering standby mode.

![](https://developer.android.com/static/images/develop/connectivity/unbundled.png)   

**Figure 2.** Relative wireless radio power use for one-second transfer running
three times every minute. Figure excludes "power up" latency between runs.

By comparison, if the same app bundled its data transfers, running a single
three-second transfer every minute, this would keep the radio in the high-power
state for a total of only 20 seconds each minute. This would allow the radio to
be on standby for 40 seconds of every minute, resulting in a significant
reduction in battery consumption.

![](https://developer.android.com/static/images/develop/connectivity/bundled.png)   

**Figure 3.** Relative wireless radio power use for three second transfers
running once every minute.

## Optimization techniques

Now that you understand how network access affects battery life, let's talk
about a few things that you can do to help reduce battery drain, while also
providing a fast and fluid user experience.

### Bundle data transfers

As stated in the previous section, bundling your data transfers so that you're
transferring more data less often is one of the best ways to improve battery
efficiency.

Of course, this is not always possible to do if your app needs to receive or
send data immediately in response to a user action. You can mitigate this by
anticipating and [prefetching data](https://developer.android.com/develop/connectivity/network-ops/network-access-optimization#prefetch-data). Other scenarios, such as
sending logs or analytics to a server and other, non-urgent, app-initiated data
transfers, lend themselves very well to batching and bundling. See [Optimizing
app-initiated
tasks](https://developer.android.com/develop/connectivity/minimize-effect-regular-updates#app-initiated) for
tips on scheduling background network transfers.

### Prefetch data

Prefetching data is another effective way to reduce the number of independent
data transfer sessions that your app runs. With prefetching, when the user
performs an action in your app, the app anticipates which data will most likely
be needed for the next series of user actions and fetches that data in a single
burst, over a single connection, at full capacity.

By front-loading your transfers, you reduce the number of radio activations
required to download the data. As a result, you not only conserve battery life,
but also improve the latency, lower the required bandwidth, and reduce download
times.

Prefetching also provides an improved user experience by minimizing in-app
latency caused by waiting for downloads to complete before performing an action
or viewing data.

Here's a practical example.

#### A news reader

Many news apps attempt to reduce bandwidth by downloading headlines only after a
category has been selected, full articles only when the user wants to read them,
and thumbnails just as they scroll into view.

Using this approach, the radio is forced to remain active for the majority
of users' news-reading session as they scroll headlines, change categories, and
read articles. Not only that, the constant switching between energy states
results in significant latency when switching categories or reading
articles.

A better approach is to prefetch a reasonable amount of data at startup,
beginning with the first set of news headlines and thumbnails---ensuring a
low-latency startup time---and continuing with the remaining headlines and
thumbnails, as well as the article text for each article available from at least
the primary headline list.

Another alternative is to prefetch every headline, thumbnail, article text, and
possibly even full article pictures---typically in the background on a
predetermined schedule. This approach risks spending significant bandwidth and
battery life downloading content that's never used, so it should be implemented
with caution.

#### Additional considerations

While prefetching data carries a lot of benefits, used too aggressively
prefetching also introduces the risk of increasing battery drain and bandwidth
use---as well as download quota---by downloading data that isn't used. It's also
important to ensure that prefetching doesn't delay application startup while the
app waits for the prefetch to complete. In practical terms that might mean
processing data progressively, or initiating consecutive transfers prioritized
such that the data required for application startup is downloaded and processed
first.

How aggressively you prefetch data depends on the size of the data being
downloaded and the likelihood of it being used. As a rough guide, based on the
state machine described earlier, for data that has a 50% chance of being used
within the current user session, you can typically prefetch for around 6 seconds
(approximately 1-2 megabytes) before the potential cost of downloading unused
data matches the potential savings of not downloading that data, to begin with.

Generally speaking, it's good practice to prefetch data such that you will only
need to initiate another download every 2 to 5 minutes, and in the order of 1 to
5 megabytes.

Following this principle, large downloads---such as video files---should be
downloaded in chunks at regular intervals (every 2 to 5 minutes), effectively
prefetching only the video data likely to be viewed in the next few minutes.

One solution is to schedule the full download to occur only when connected to
Wi-Fi, and possibly only when the device is charging. The
[WorkManager API](https://developer.android.com/topic/libraries/architecture/workmanager/how-to/define-work#constraints)
supports exactly this use case, allowing you to restrict the background work
until the device meets the developer-specified criteria, such as charging and
being connected to Wi-Fi.

### Check for connectivity before making requests

Searching for a cell signal is one of the most power-draining operations on a
mobile device. A best practice for user-initiated requests is to first check for
a connection using
[`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager), as shown in
[Monitor connectivity status and connection
metering](https://developer.android.com/training/monitoring-device-state/connectivity-status-type#DetermineConnection).
If there's no network, the app can save battery by not forcing the mobile radio
to search. The request can then be scheduled and performed in a batch with other
requests when a connection is made.

### Pool connections

An additional strategy that can help in addition to batching and prefetching, is
to pool your app's network connections.

It's generally more efficient to reuse existing network connections than it is
to initiate new ones. Reusing connections also allows the network to
more-intelligently react to congestion and related network data issues.

[`HttpURLConnection`](https://developer.android.com/reference/java/net/HttpURLConnection) and most HTTP
clients, such as [OkHttp](https://square.github.io/okhttp/), enable
connection-pooling by default, and reusing the same connection for multiple
requests.

## Recap and looking ahead

In this section, you learned a lot about the wireless radio and some strategies
that you can apply broadly to provide a fast, responsive user experience while
reducing battery drain.

In the next section, we'll take a detailed look at three distinct types of
network interactions common to most apps. You'll learn the drivers for each of
these types as well as modern techniques and APIs for managing these
interactions efficiently.