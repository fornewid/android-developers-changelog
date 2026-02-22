---
title: https://developer.android.com/topic/performance/vitals/excessive-battery-usage
url: https://developer.android.com/topic/performance/vitals/excessive-battery-usage
source: md.txt
---

# Excessive battery usage

| **Note:** Excessive battery usage is only available for watch face apps with sufficient usage data.

Excessive battery usage is the percentage of watch face sessions where battery usage exceeds 4.44% per hour. Google Play collects this data when devices aren't charging and no apps are in use.

When battery usage exceeds 4.44% per hour the watch won't last a full day on a single charge. This harms users and the Wear OS ecosystem.

To maximize battery life, aim for battery usage under 3.2% per hour.

## Efficiency requirements

An efficient watch face app should have:

- \< 1% excessive battery usage
- \< 3.2% battery usage per hour for 80% of sessions

| **Warning:** If excessive battery usage exceeds 1%, Play may reduce your app's visibility. See[core vitals FAQ](https://developer.android.com/topic/performance/vitals#core-vitals-faqs)for more details.

[Vitals](https://developer.android.com/topic/performance/vitals)provides the following data:

- Excessive battery usage over time
- Battery usage per hour histogram
- Contributing factors
- Breakdowns

## Contributing factors

These are key factors affecting your app's battery usage:

- **Excessive CPU usage:**The portion of watch face sessions that use the CPU for 90 seconds or more per hour.
- **Excessive partial wakelocks:**The portion of watch face sessions use wakelocks for 18.5 seconds or more per hour.

Use[breakdowns](https://developer.android.com/topic/performance/vitals/excessive-battery-usage#breakdowns)and[Battery Historian](https://developer.android.com/topic/performance/power/battery-historian)to investigate further.

## Breakdowns

Breakdowns group affected sessions by characteristics such as OS, device, and region. Select a breakdown to see an hourly battery usage histogram for that group.

## Reduce battery usage

Use the following suggestions to reduce your app's battery usage.

### Use Watch Face Format

[Watch Face Format](https://developer.android.com/training/wearables/wff)uses declarative XML instead of executable code to simplify app creation and reduces battery usage.

### Handle Always on display (AoD) mode

When a watch isn't in use it switches to Always-on display (AoD), also called ambient mode. In AoD, your watch face should[illuminate no more than 15% of pixels](https://developer.android.com/docs/quality-guidelines/wear-app-quality#always-on-display).

### Optimize memory usage

Large images, fonts, and animations (like sweeping second hands) increase battery usage.

- Use the lowest resolution resources needed
- Crop resources to their minimum size (avoid transparent borders)
- Remove or crop anything hidden by other elements to reduce overdraw

| **Tip:** Use the[Watch Face Format Optimizer](https://github.com/google/watchface/tree/main/tools/wff-optimizer)to automatically apply some optimizations.

See[Optimize memory usage](https://developer.android.com/training/wearables/wff/memory-usage)for more suggestions.

### Limit animations

Animating elements makes watch faces visually appealing but uses more battery. To reduce their impact:

- Avoid using high fps animations
  - For most animations 15 fps is recommended
- Limit usage of dynamic elements such as[Gyro](https://developer.android.com/training/wearables/wff/common/transform/gyro)and[ArithmeticExpression](https://developer.android.com/training/wearables/wff/common/attributes/arithmetic-expression)
  - `ArithmeticExpression`updates as frequently as its source data. High frequency sources such as`MILLISECOND`and`ACCELEROMETER`use more battery.
- Avoid unnecessary animations in AoD mode

### Avoid wakelocks

Publish your app using[Watch Face Format](https://developer.android.com/training/wearables/wff)to avoid wakelocks.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Watch Face Format](https://developer.android.com/training/wearables/wff)
- [Power considerations](https://developer.android.com/design/ui/wear/guides/surfaces/watch-faces#power_considerations)
- [Battery Historian](https://developer.android.com/topic/performance/power/battery-historian)