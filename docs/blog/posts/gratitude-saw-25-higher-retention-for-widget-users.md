---
title: https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users
url: https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users
source: md.txt
---

[Case Studies](https://developer.android.com/blog/categories/case-studies)

# Gratitude saw 25% higher retention for widget users

3-min read ![](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_2000x1000_7d5a00e6c2_Z2vwfIA.webp) 08 May 2026 [![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp)](https://developer.android.com/blog/authors/ash-nohe) [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev) \& [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe) Practicing gratitude may decrease symptoms of depression and anxiety, and improve mental health and life satisfaction¹. Consistent gratitude practice may lead to sustained improvements that last months². The mindfulness app [Gratitude](https://play.google.com/store/apps/details?id=com.northstar.gratitude) encourages consistency through micro daily journaling, affirmations, and vision boards. The app has over 6 million downloads, 150 thousand 5 star ratings, and 100 million journal entries logged.

Developers Divij Gupta and Narendra Aanjna developed widgets for each of their app's core user journeys. Their goal was to meet users in their everyday moments without requiring the overhead of a full app session.

By surfacing interactive journaling prompts, affirmations, vision board images and metrics directly on the user's home screen, the team lowered the barrier to entry for daily reflection and reported **a 25% increase in retention** for widget users and **\~1K weekly journal entries from widgets**. This increase in user loyalty translates to tangible health outcomes for the users: consistent habit formations that support long-term mental well-being.

*"Widgets helped us make the app more present in users' daily routines by providing quick inspiration, reminders, and reflections directly on the home screen. This increased engagement and made it easier for users to stay consistent with their mindfulness practices." -- Divij Gupta*
![AANDDM_Gratitude_01.png](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_01_5480b69b77_Z24hDBG.webp)

### The Challenge: modernize without decreasing retention

While the impact of widgets was clear, Gratitude's original XML-based RemoteViews implementation created technical debt. As the app's design system evolved toward Material 3, the legacy widgets became increasingly difficult to align with the modern UI. Every visual update required manual XML overhead and brittle workarounds, slowing developer velocity.
![AANDDM_Gratitude_02.png](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_02_bf11ffc3b7_EmHcu.webp)

### The Solution Part 1: migrating from XML to Jetpack Glance

To modernize their widgets, the team turned to [Jetpack Glance](https://developer.android.com/develop/ui/compose/glance).

They first consulted the [Widgets on Android](https://developer.android.com/design/ui/widget) design page and [canonical widget layouts](https://developer.android.com/design/ui/mobile/guides/widgets/layouts) to understand best practices for displaying information within a limited amount of space.

Then, they migrated their widget suite to Jetpack Glance. This declarative framework enabled the developers to move from planning to shipping in **less than a month** , **saving about 50% development time**, and saw two additional advantages:

- Replacing restrictive XML layouts with declarative code made the codebase easier to read, maintain, and reduced developer effort.
- Jetpack Glance allowed the team to more easily implement [dynamic colors](https://developer.android.com/develop/ui/compose/glance/theme), flexible [resizing](https://developer.android.com/develop/ui/compose/glance/build-ui#sizemode.exact), and expanded configuration options. These features ensure the widgets harmonize with a user's unique home screen layout.

![AANDDM_Gratitude_03.png](https://developer.android.com/static/blog/assets/AANDDM_Gratitude_03_f177cefe5d_GJLdE.webp)

The following GIF shows two Gratitude widgets and adaptive resizing:
![GratitudeAdaptiveWidgets.gif](https://developer.android.com/static/blog/assets/Gratitude_Adaptive_Widgets_fb927de278_ZJOx6n.webp)

While Glance simplified the UI, the team noted that testing across various OEM launchers was also essential to ensure layout consistency across devices.

The team also implemented [Generated Widget Previews](https://developer.android.com/develop/ui/compose/glance/generated-previews) so users can see personalized previews. They noted that testing Generated Previews could be slow, as the previews are rate limited to preserve battery. To bypass the rate limiting for testing, use the adb command:

`adb shell device_config put systemui generated_preview_api_reset_interval_ms 0`

All of their efforts have made the Gratitude widget [high quality and differentiated](https://developer.android.com/docs/quality-guidelines/widget-quality).

### The Solution Part 2: promote new widgets in-app

The developers then used [in-app widget pinning](https://developer.android.com/develop/ui/compose/glance/pin-in-app) to increase widget discoverability and widget installs. Asking users to install widgets at a contextually relevant moment within the app helps users find their widgets without needing to go through the system widget picker. The following GIF shows Gratitude's bottom sheet to add widgets from within the app:

The team also refactored widget packages, which changed widget receiver paths and caused widgets to be deleted from users' home screens. Using previously stored user flags to identify widget users, they triggered another `requestPinGlanceAppWidget` prompt inviting widget users to use the new modernized widgets.

**Developer Tip:** To maintain widget installs while migrating from RemoteViews to Jetpack Glance, ensure your `GlanceAppWidgetReceiver` uses the same class name and package as your previous `AppWidgetProvider` in the Android Manifest. If a new class name or package location is required, follow the Gratitude's lead by using in-app pinning to help users restore their widgets.

The strategy is working, as **10% of total DAU** have adopted widgets.

### Conclusion

This Gratitude story shows that widgets can be tools for habit formation. By implementing quick actions to self-reflect right from the home screen, the team improved user loyalty. Gratitude reduced technical debt and modernized their widgets by adopting Jetpack Glance, and prompted users to add widgets within their app.

*"Our experience with Jetpack Glance has been excellent. The Compose-based approach feels much more modern, flexible, and aligned with the way we build the rest of our UI today. It allows us to express widget layouts more naturally, reuse familiar Compose components, and iterate on UI changes much faster. Many of the UI constraints we previously faced with RemoteViews are no longer an issue, which made it easier to build widgets that better match our app's design and experience."* -- Divij Gupta

### Getting Started

To get started with Jetpack Glance and learn about the technologies mentioned in this post, see these guides:

- [Jetpack Glance Overview](https://developer.android.com/develop/ui/compose/glance)
- [Widgets on Android](https://developer.android.com/design/ui/widget) design page
- [Canonical widget layouts](https://developer.android.com/design/ui/mobile/guides/widgets/layouts)
- [Generated Widget Previews](https://developer.android.com/develop/ui/compose/glance/generated-previews)
- [Widget Quality Tiers](https://developer.android.com/docs/quality-guidelines/widget-quality)
- [In-app widget pinning](https://developer.android.com/develop/ui/compose/glance/pin-in-app)
- [Dynamic colors](https://developer.android.com/develop/ui/compose/glance/theme)
- [Resizing](https://developer.android.com/develop/ui/compose/glance/build-ui#sizemode.exact)
- [Configuration activities](https://developer.android.com/codelabs/glance#3)

See other widget case studies:

- [Google's Contacts app created a new widget 25% faster using Jetpack Glance](https://android-developers.googleblog.com/2023/10/googles-contacts-app-created-new-widget-faster-using-jetpack-glance.html)
- [SoundCloud uses Jetpack Glance to build Liked Tracks widget in just 2 weeks](https://android-developers.googleblog.com/2025/02/soundcloud-uses-jetpack-glance-to-build-liked-tracks-widget-in-just-2-weeks.html)

1: Diniz, G., Korkes, L., Tristão, L. S., Pelegrini, R., Bellodi, P. L., \& Bernardo, W. M. (2023). The effects of gratitude interventions: a systematic review and meta-analysis. einstein (Sao Paulo)., 21, eRW0371. <https://doi.org/10.31744/einstein_journal/2023RW0371>

2: Bohlmeijer, E., Kraiss, J., Schotanus-Dijkstra, M., \& ten Klooster, P. (2022). Gratitude as mood mediates the effects of a 6-weeks gratitude intervention on mental well-being: post hoc analysis of a randomized controlled trial. Front. Psychol., 12, 799447. <https://doi.org/10.3389/fpsyg.2021.799447>
Written by:

-

  ## [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev)

  ###### Staff Developer Advocate

  [read_more
  View profile](https://developer.android.com/blog/authors/amrit-sanjeev) ![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp) ![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)
-

  ## [Ash Nohe](https://developer.android.com/blog/authors/ash-nohe)

  ###### Sr. Android Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ash-nohe) ![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp) ![View Ash Nohe's profile](https://developer.android.com/static/blog/assets/ash_32bd9f9ed7_Zhh9o0.webp)
Continue reading
- [![View Amrit Sanjeev's profile](https://developer.android.com/static/blog/assets/Amrit_Sanjeev_5215e0d7cc_CrDLy.webp)](https://developer.android.com/blog/authors/amrit-sanjeev)[![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/trevor-johns) 08 Jan 2026 08 Jan 2026 ![](https://developer.android.com/static/blog/assets/Ultrahumanx_Gi_AS_Banner_1612731319_Z23acG3.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Ultrahuman launches features 15% faster with Gemini in Android Studio](https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/ultrahuman-launches-features-faster-with-gemini-in-android-studio) Ultrahuman is a consumer health-tech startup that provides daily well-being insights to users based on biometric data from the company's wearables, like the RING Air and the M1 Live Continuous Glucose Monitor (CGM).
  [Amrit Sanjeev](https://developer.android.com/blog/authors/amrit-sanjeev), [Trevor Johns](https://developer.android.com/blog/authors/trevor-johns) • 2 min read
- 3 Authors 08 Jun 2026 08 Jun 2026 ![](https://developer.android.com/static/blog/assets/ANDDM_TITLE_Strapi_b83ae0beee_i9nEs.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [Datadog delivers millions of in-depth performance insights with ProfilingManager](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager)

  [arrow_forward](https://developer.android.com/blog/posts/datadog-delivers-millions-of-in-depth-performance-insights-with-profiling-manager) Performance regressions are notoriously hard to reproduce, making regressions a massive bottleneck for mobile developers.
  [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan), [Arti Arutiunov](https://developer.android.com/blog/authors/arti-arutiunov), [Nikita Ogorodnikov](https://developer.android.com/blog/authors/nikita-ogorodnikov) • 4 min read
  - [#Profiling Manager](https://developer.android.com/blog/topics/profiling-manager)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +1 ↩
- [![View Garan Jenkin's profile](https://developer.android.com/static/blog/assets/Garan_Jenkin_0529dbfef9_Z2crRat.webp)](https://developer.android.com/blog/authors/garan-jenkin) 15 May 2026 15 May 2026 ![](https://developer.android.com/static/blog/assets/cross_device_discovery_to_score_record_Wear_OS_adoption_Strapi_2f9244f1db_Z23QTbE.webp) [Case Studies](https://developer.android.com/blog/categories/case-studies)

  ## [How FotMob leveraged cross-device discovery to score record Wear OS adoption](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption)

  [arrow_forward](https://developer.android.com/blog/posts/how-fot-mob-leveraged-cross-device-discovery-to-score-record-wear-os-adoption) FotMob recently experienced its largest single-day increase on Wear OS among its installed audience in 5 years, at 2-3x the daily average. The secret? A simple cross-device installation flow that helps users discover their Wear OS app directly from their phone.
  [Garan Jenkin](https://developer.android.com/blog/authors/garan-jenkin) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)