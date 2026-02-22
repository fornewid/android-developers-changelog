---
title: https://developer.android.com/quality/technical
url: https://developer.android.com/quality/technical
source: md.txt
---

# What great technical quality looks like

![](https://developer.android.com/static/images/quality/hero-images/technical_quality_highlighted.svg)

Technical quality includes the stability, performance, and resource utilization of your app or game. The technical quality of your app or game can affect the user experience. A high-quality experience not only minimizes technical issues, but also makes the most of capabilities of the Android OS and device hardware.

To build a high-quality app or game, follow these guidelines.

## Form factors

Your app or game should make the most of premium devices like foldables. Follow functional and technical guidelines for each form factor you support.

If it makes sense for your app or game to support multiple form factors, ensure[continuity](https://developer.android.com/develop/ui/compose/layouts/adaptive/foldables/learn-about-foldables#app_continuity)across form factors for a seamless user experience---for example, by synchronizing files and settings between devices, or saving their progress.

## Stability

Stability issues cause your app or game to crash or stop responding, which interrupts user journeys and hurts the user experience. There are different types of issues, including[crashes](https://developer.android.com/topic/performance/vitals/crash),[ANRs](https://developer.android.com/topic/performance/vitals/anr), and[LMKs](https://developer.android.com/topic/performance/memory-management#low-memory_killer), but all are equally disruptive to users.

App or game stability can vary by device. Monitor your stability metrics regularly across all devices and aim to minimize the proportion of your users and sessions that are affected by stability issues. Ensure your stability metrics are best in class compared to your peers. Monitor user feedback and engagement metrics to ensure that stability issues aren't impacting your users.

Following best practices, such as[opting into GWP-ASan](https://developer.android.com/ndk/guides/gwp-asan), programming in null-safe languages such as[Kotlin](https://developer.android.com/kotlin), and using[background work APIs](https://developer.android.com/guide/background), can reduce stability issues and also make debugging easier when they do occur.

### Stability and Google Play

If you distribute on Google Play, follow these additional stability guidelines.

**Tools to monitor and improve stability** Use Android vitals in[Play Console](https://play.google.com/console/about/vitals/)or the[reporting API](https://developers.google.com/play/developer/reporting)to monitor the stability metrics that matter most to users and Google Play. Android vitals reports user-perceived crash rate and user-perceived ANR rate daily for all apps and games, and hourly for apps and games if there's sufficient data. Android vitals also helps you compare your stability metrics to your peers, and alerts you to per-device issues.

**Discovery and featuring** The discoverability of your app or game might be limited on devices where your stability metrics exceed Google Play's bad behavior threshold, and a warning might be shown on your store listing on those devices.[Learn more](https://developer.android.com/topic/performance/vitals#core-vitals)

## Performance

Your app's or game's performance is critical to a quality experience.

### Start-up time (apps) and loading time (games)

Users want to be able to interact with your app or game as quickly as possible. The definition of a good start-up or loading time varies by category, but as a general principle you should minimize the time between launch and first interaction. This time can vary by device, and different standards could be appropriate for different device capabilities.

Ensure your metrics are best in class compared to your peers. Monitor user feedback and abandonment rates to ensure you're meeting user expectations, and check that your performance isn't degrading over time.

Leverage Android to optimize[startup time](https://developer.android.com/topic/performance/vitals/launch-time). Providing a[baseline profile](https://developer.android.com/topic/performance/baselineprofiles/overview)and declaring[reportFullyDrawn](https://developer.android.com/topic/performance/vitals/launch-time#retrieve-TTFD)will ensure the most important sections of your code load faster, and adopting the[Game State API](https://developer.android.com/reference/android/app/GameManager#setGameState(android.app.GameState))(games-only) will help the OS adjust during loading. Reducing[the size of your game or app](https://developer.android.com/quality/technical#app-size)will also improve start-up time for new installations.

### Rendering (apps)

A smooth and responsive session will make your user experience more enjoyable and keep users engaged for longer. Most apps should run at 60 fps without any dropped or delayed frames. Poor rendering performance can cause users to perceive stuttering, also known as*jank*.

Monitor your rendering metrics regularly across all devices and aim to minimize the proportion of your users and sessions that experience jank. Aim for best-in-class rendering performance compared to your peers. Monitor user feedback and engagement to ensure that you're delivering a good experience.

Providing a[baseline profile](https://developer.android.com/topic/performance/baselineprofiles/overview)can improve rendering performance and startup time. Consider using the[JankStats](https://developer.android.com/topic/performance/jankstats)library to track and analyze performance issues. Review the[best practices](https://developer.android.com/topic/performance/rendering)for rendering.

### Rendering (games)

A smooth and responsive session makes your user experience more enjoyable and helps keep users engaged longer. Most games should run their core game loop at a minimum of 30 fps to provide a reasonable experience for users. For the most rewarding user experience, consider a frame rate of 60 fps or more, particularly for games that require smooth animation or quick reaction time, and when running on higher-end devices. Keep in mind that higher frame rates come with tradeoffs in battery life, device temperature, and graphical fidelity, so increased rates may not be appropriate for all devices, games, or scenes.

Monitor your rendering metrics regularly across all devices and work to minimize the proportion of your users and sessions that experience slow rendering. Aim for best-in-class rendering performance compared to peers. Monitor user feedback and engagement to ensure that you are delivering a good experience.

Follow best practices, such as using the[Android Dynamic Performance Framework](https://developer.android.com/games/optimize/adpf),[Game Mode API](https://developer.android.com/games/gamemode/about-API-and-interventions)and[frame pacing](https://developer.android.com/games/sdk/frame-pacing), to optimize visual smoothness and stability. Use[Android Performance Tuner](https://developer.android.com/games/sdk/performance-tuner)to tune quality levels appropriately for the devices you support. Make considered choices about graphics libraries and asset formats. For example, using[Vulkan](https://developer.android.com/ndk/guides/graphics/getting-started)as a graphics API and[ASTC for assets](https://developer.android.com/guide/playcore/asset-delivery/texture-compression)can significantly improve your rendering performance.

### Google Play guidelines

If you distribute on Google Play, follow these additional performance guidelines.

**Tools to monitor and improve performance** Use Android vitals in[Play Console](https://play.google.com/console/about/vitals/)or the[reporting API](https://developers.google.com/play/developer/reporting)to monitor the performance metrics that matter most to users and Google Play. Android vitals reports startup time, loading time and rendering metrics daily for all apps and games. It also helps you compare your metrics to your peers, and alerts you if you're not meeting[Play's quality bar](https://developer.android.com/topic/performance/vitals#core-vitals).

[Play as you Download](https://developer.android.com/games/distribute/play-as-you-download)is a Google Play feature that allows users to get into your game experience while the game is still downloading, reducing the time from launch to gameplay.

**Discovery and featuring** The discoverability of your app or game might be limited on devices where your performance metrics exceed Google Play's bad behavior threshold, and a warning might be shown on your store listing on those devices.[Learn more](https://developer.android.com/topic/performance/vitals#core-vitals)

## Battery and network usage

Thoughtful and appropriate usage of limited or costly resources like battery life and network bandwidth will make your app accessible to more users, increase session length, and improve user retention. Games should reduce frame rates and display refresh rates where appropriate, for example when rendering menus and loading screens. Using the[Game Mode API](https://developer.android.com/games/gamemode/about-API-and-interventions)can help users make tradeoffs between performance and battery life, and can lead to[longer playtime](https://developer.android.com/stories/games/gameloft-gamemode).

### Google Play guidelines

If you distribute on Google Play, follow these additional battery and network usage guidelines.

**Tools to monitor and optimize battery and network usage**Use Android vitals in Play Console or the reporting API to monitor the battery and network metrics that matter most to users and Google Play.

## App size

The definition of a good app size varies widely by category, but as a general principle you should minimize the size of your app. The smaller your app, the more people who can install it, and the shorter the time between installation and first use. Users are also less likely to uninstall your app to free up device storage.

Follow recommended best practices to minimize the size of your[game](https://developer.android.com/games/optimize/game-size)or[app](https://developer.android.com/topic/performance/reduce-apk-size).

### Google Play guidelines

If you distribute on Google Play, follow these additional app size guidelines.

**Tools to monitor and optimize app size** Use Android vitals in[Play Console](https://play.google.com/console/about/vitals/)to monitor your app size. Android vitals allows you to compare your app size to your peers, and helps you understand how many devices in your user base are running low on storage. Keep in mind that Google Play proactively helps users free up device storage by suggesting apps to uninstall, and will prioritize app size when formulating these recommendations.

If you distribute on Google Play, use the[app bundle format](https://developer.android.com/guide/app-bundle)to ensure that each user downloads only the code and resources necessary to run your app or game. Larger apps and games can further benefit from[Play Feature delivery](https://developer.android.com/guide/playcore/feature-delivery)and[Play Asset delivery](https://developer.android.com/guide/playcore/asset-delivery), where specific parts of your code or assets can be downloaded conditionally or on demand.

## App freshness

Update your app regularly so that users can benefit from performance improvements, bug fixes, platform enhancements, new features, and new content. Not all users have reliable or affordable network access, or available device storage. To increase the number of active users who can update your app or game, minimize the size of your updates.

### Google Play guidelines

If you distribute on Google Play, follow these additional app freshness guidelines.

**Tools to increase app freshness** Not all users enable background updates. Adopting features like[in-app updates](https://developer.android.com/guide/playcore/in-app-updates)can increase the number of active users on the latest version of your app or game.

## Healthy releases

Changes in your codebase, whether through server-side flags or app updates, are a common cause of new technical issues. It's much better for users if you invest time in preventing issues from reaching production, rather than fixing them after they've been introduced. Users can be quick to leave feedback in the event of a poor experience, and might not update your app after first install.

To minimize the risk of introducing new issues in a release, take a phased approach to[testing](https://developer.android.com/training/testing)and rollout, and monitor your metrics frequently during any changes. You can also make it easier to mitigate emerging issues by decoupling binary releases from feature releases with remote configuration SDKs, such as[Firebase Remote Config](https://firebase.google.com/docs/remote-config).

### Google Play guidelines

If you distribute on Google Play, follow these additional guidelines for ensuring healthy releases.

**Tools to monitor and improve release quality** Play Console provides many features to help you[release with confidence](https://play.google.com/console/about/guides/releasewithconfidence/), and Android vitals reports hourly metrics for apps and games if there's sufficient data, both in[Play Console](https://play.google.com/console/about/vitals/)and the[reporting API](https://developers.google.com/play/developer/reporting).

**Discovery and featuring** Google Play evaluates technical quality across all users of your app regardless of what version they are using. Managing your release quality is therefore not only better for users, it's also better for your Google Play quality metrics.[Learn more](https://developer.android.com/topic/performance/vitals#core-vitals)