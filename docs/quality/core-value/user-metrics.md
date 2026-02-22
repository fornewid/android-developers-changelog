---
title: https://developer.android.com/quality/core-value/user-metrics
url: https://developer.android.com/quality/core-value/user-metrics
source: md.txt
---

# User metrics on Google Play

Google Play cares about app quality and uses various signals to evaluate users' experience of your app. Apps are only eligible for certain features if they meet a minimum quality bar.

Play uses a combination of user metrics and in-app evaluation to evaluate the quality of your app, including (but not limited to) uninstalls (user loss rate), daily active users (DAUs), and monthly active users (MAUs). We may also look at other app experience metrics like ad load, usability, performance, and content or feature depth compared to your peers.

## User metrics for Play details page treatments (beta)

User metrics are generally the strongest indication of a quality app. Metric thresholds are used as some of the criteria to determine eligibility for tools (such as the Inline Installs API) and quality treatments on certain surfaces of the Play Store.

The user metric quality requirements are as follows:

- User loss rate \< 5%.
- DAU divided by MAU \> 8%.
- You also need to have a sufficient number of users installing and engaging with your app to accurately assess these metrics over a minimum of 24 days in a 30 day period.

In addition, apps must continue to meet our[technical quality core vitals and bad behavior thresholds](https://developer.android.com/quality/technical#stability_and_google_play). Individual treatments and tools may also have additional requirements for eligibility.

You can use[Play Console Statistics](https://play.google.com/console/u/0/developers/app/statistics)(under the**Compare to peers**tab) to monitor your metrics.