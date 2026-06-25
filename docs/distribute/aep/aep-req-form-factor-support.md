---
title: https://developer.android.com/distribute/aep/aep-req-form-factor-support
url: https://developer.android.com/distribute/aep/aep-req-form-factor-support
source: md.txt
---

Implement high-quality experiences across multiple form factors to reduce
fragmentation and meet user expectations for a seamless multidevice ecosystem.
Expanding your app's reach across form factors like tablets, foldables,
wearables, and auto environments increases ecosystem value and provides enhanced
user experience.

## Required implementation

To qualify for AEP, apps must meet the form factor
distribution requirements^\*^ **AND** minimum quality standard
for each form factor.

**All apps** are required to meet the **Adaptive App Tier 2 guidelines** and
ensure availability on the default set of form factors:

- **At enrollment**: Phone, Tablet, Foldable, and XR
- **By March 1, 2027**: Googlebook

**Apps that support select use cases** critical to platforms like TV, Wear, and
Auto, additional requirements are defined specifically by those use cases
(for example, media streaming for TV or navigation for Auto). The following
table defines the full set of form factor requirements and minimum quality
standard per app use case.

| Form factors | Minimum quality standards to be met by the app | Required for: |
|---|---|---|
| Phone, Tablet, Foldable | [Tier 2 - Adaptive Optimized](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/tier-2) | All apps |
| XR | [Tier 2 - Adaptive Optimized](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/tier-2) or [XR differentiated](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated) | All apps |
| GoogleBook | [Tier 2 - Adaptive Optimized](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/tier-2) | All apps (Enforced by March 1, 2027) |
| Auto (Non-Driving) | [Tier 2 - Adaptive Optimized](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality/tier-2) or [Tier 2 - Car Optimized](https://developer.android.com/docs/quality-guidelines/car-app-quality#tier_2_-_car_optimized) | Apps that support: - Streaming video (TV, movies, live sports, live news, transactional video) |
| Auto (Driving) | [Tier 2 - Car Optimized](https://developer.android.com/docs/quality-guidelines/car-app-quality#tier_2_-_car_optimized) | Apps that support any of: - Streaming music, podcasts, live radio, or audiobooks - Weather forecasts and reports - Maps, driving navigation, and finding points of interest such as parking spots, charging stations, and gas stations |
| Wear | [Wear App Guidelines](https://developer.android.com/docs/quality-guidelines/wear-app-quality) | Apps that support any of: - Streaming music, podcasts, live radio, or audiobooks - Instant messaging |
| TV | [TV App Guidelines](https://developer.android.com/docs/quality-guidelines/tv-app-quality) | Apps that support any of: - Streaming video (TV, movies, live sports, live news, transactional video) - Streaming music and audio |

Form Factor quality guidelines are updated periodically, generally once or twice
per year. Apps must comply with the latest version available at the time of
enrollment. Apps are granted a 12-month grace period to comply with subsequent
quality version upgrades.

(\*) Note: This does not require distribution on Play on these Android
form factors.

## Exemptions

The following exemptions apply for this guideline:

- **Hardware constraints**: Apps can apply for exemption if a specific form factor's constraints would meaningfully degrade the core user experience or if no technical solution exists for that hardware to support the app's core use case.
- **Technical constraints**: Apps primarily intended for utilities or tools that have no logical use case on specialized form factors may be considered for exemption.
- **Form factor availability**: If a device is unavailable in a region where the app is offered, the app is exempt from distribution on that device in that region.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Form Factor Support**. These resources are for your reference only and
don't contain additional program requirements.

- [Build adaptive apps](https://developer.android.com/adaptive-apps)
- [Getting started with Wear OS](https://developer.android.com/training/wearables)
- [Adaptive App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2)
- [XR App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/android-xr)
- [Wear OS App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/wear-app-quality)
- [Car App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/car-app-quality#tier_2_-_car_optimized)
- [TV App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2)
- [Desktop App Quality Guidelines](https://developer.android.com/design/ui/desktop) (recommended for Googlebook, but not required)