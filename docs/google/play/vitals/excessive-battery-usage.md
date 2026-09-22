---
title: https://developer.android.com/google/play/vitals/excessive-battery-usage
url: https://developer.android.com/google/play/vitals/excessive-battery-usage
source: md.txt
---

> [!NOTE]
> **Note:** Excessive battery usage is only available for watch face apps with sufficient usage data.

Excessive battery usage is the percentage of watch face sessions where battery
usage exceeds 4.44% per hour. Google Play collects this data when devices aren't
charging and no apps are in use.

When battery usage exceeds 4.44% per hour the watch won't last a full day on a
single charge. This harms users and the Wear OS ecosystem.

To maximize battery life, aim for battery usage under 3.2% per hour.

> [!NOTE]
> **Note:** For information on how to diagnose and resolve this issue, see [Excessive battery usage](https://developer.android.com/topic/performance/issues/excessive-battery-usage).

## Efficiency requirements

An efficient watch face app should have:

- \< 1% excessive battery usage
- \< 3.2% battery usage per hour for 80% of sessions

> [!WARNING]
> **Warning:** If excessive battery usage exceeds 1%, Play may reduce your app's visibility. See [core vitals FAQ](https://developer.android.com/google/play/vitals#core-vitals-faqs) for more details.

[Vitals](https://developer.android.com/google/play/vitals) provides the following data:

- Excessive battery usage over time
- Battery usage per hour histogram
- Contributing factors
- Breakdowns

## Contributing factors

These are key factors affecting your app's battery usage:

- **Excessive CPU usage:** The portion of watch face sessions that use the CPU for 90 seconds or more per hour.
- **Excessive partial wakelocks:** The portion of watch face sessions use wakelocks for 18.5 seconds or more per hour.

Use [breakdowns](https://developer.android.com/google/play/vitals/excessive-battery-usage#breakdowns) and [Battery Historian](https://developer.android.com/topic/performance/power/battery-historian) to investigate further.

## Breakdowns

Breakdowns group affected sessions by characteristics such as OS, device, and
region. Select a breakdown to see an hourly battery usage histogram for that
group.