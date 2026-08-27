---
title: https://developer.android.com/distribute/aep/aep-req-jetpack-compose
url: https://developer.android.com/distribute/aep/aep-req-jetpack-compose
source: md.txt
---

Use Jetpack Compose to build the UI. Jetpack Compose is the preferred UI toolkit
for Android development. It provides the most direct route to fulfill the
program criteria and create high-quality Android experiences through native
Material Design support, seamless system integration, and streamlined scaling
for various form factors.

## Required implementation

To qualify for the AEP, apps must use Jetpack Compose or an equivalent
alternative to build the user interface.

| ID | Guideline |
|---|---|
| AEP-JC-GAA | Apps must use Jetpack Compose or an equivalent alternative to build the user interface. |

While Compose is the preferred standard, you can use alternative toolkits if
they provide equivalent performance and functionality. React Native is an
approved alternative toolkit, though the list of approved toolkits may change as
the Jetpack ecosystem evolves. Toolkits may be added or removed from the list
based on their adherence to the latest standards.

This guideline permits the **supplemental use** of other toolkits such as
Flutter, Android Views, or WebView alongside Jetpack Compose or other accepted
alternatives. While current standards allow for this flexibility, future program
updates may introduce higher utilization thresholds based on the percentage of
an app's activities or UI components built with Compose. As with all program
requirement updates, sufficient notice will be given to developers before these
thresholds are updated.

## Guideline applicability

This guideline is applicable to all apps across all the form factors.

## Exemptions

You can submit alternative toolkits for evaluation if you believe they should be
considered alongside the accepted alternative toolkits. To qualify, the toolkit
must meet these benchmarks:

| ID | Category | Exemption |
|---|---|---|
| AEP-JC-EAA | Performance | Achieve [time to initial display](https://developer.android.com/topic/performance/vitals/launch-time#time-initial) under 400 ms using pre-compilation or equivalent optimizations. |
| AEP-JC-EAB | Performance | Render UI at the device's native refresh rate without frame drops. |
| AEP-JC-EAC | Standard Android UI paradigms | Provide [touch-feedback animations](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/handling-interactions) for all element interactions. |
| AEP-JC-EAD | Standard Android UI paradigms | Support edge-to-edge design by drawing behind system bars and handling window insets. |
| AEP-JC-EAE | Standard Android UI paradigms | Support [overscroll](https://developer.android.com/reference/kotlin/androidx/compose/foundation/OverscrollEffect) stretch effects at scroll boundaries. |
| AEP-JC-EAF | Standard Android UI paradigms | Respond automatically to system light and dark theme toggles without app restarts. |
| AEP-JC-EAG | Standard Android UI paradigms | Apply device-level palette APIs to adjust UI tokens dynamically using Material Design support. |
| AEP-JC-EAH | Supports assistive features | Integrate with the Android Accessibility Framework, including screen reader and TalkBack support. |
| AEP-JC-EAI | Supports assistive features | Support the Android Autofill framework for streamlined user data entry. |
| AEP-JC-EAJ | Supports assistive features | Integrate with system intelligence services for real-time app activity capture. |
| AEP-JC-EAK | Multi-Window, folding, and adaptability | Scale UI boundaries mid-session across window size classes without container restarts. |
| AEP-JC-EAL | Multi-Window, folding, and adaptability | Preserve active session states, such as video playback or form input, during mid-session folding or resizing. |

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Jetpack Compose** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Jetpack Compose for Android Developers](https://developer.android.com/courses/jetpack-compose/course)
- [Jetpack Compose Tutorial](https://developer.android.com/develop/ui/compose/tutorial)
- [Jetpack Compose documentation](https://developer.android.com/develop/ui/compose/documentation)