---
title: https://developer.android.com/stories/games/netmarble-got-adpf
url: https://developer.android.com/stories/games/netmarble-got-adpf
source: md.txt
---

# Netmarble Games: Optimizing Performance with ADPF

![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_got_logo.jpg)Netmarble: Game of Thrones series logo![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_got_battle.jpg)Netmarble: battle scene![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_got_dragon.jpg)Netmarble: battle scene with field boss Drogon

Netmarble, a leading mobile game developer, developed[Game of Thrones: Kingsroad](https://gameofthrones.netmarble.com/en/)(coming soon to Android), an action-adventure RPG based on the Emmy® Award-winning and Golden Globe® winning Game of Thrones series. They encountered performance challenges, specifically thermal throttling, while running the game on Android devices, impacting sustained performance and user experience. To address this, they strategically leveraged the[Android Adaptive Performance Framework (ADPF)](https://developer.android.com/games/optimize/adpf)and implemented optimizations focused on resolution scaling and dynamic frame rate adjustment.

## Challenge

High-fidelity mobile games demand significant GPU and CPU resources, often leading to excessive heat generation and thermal throttling on Android devices. Netmarble observed that prolonged gameplay sessions resulted in increased device temperature, causing performance degradation, including frame rate drops and inconsistent performance. The core challenge was maintaining a visually engaging experience while effectively managing device temperatures to avoid throttling and ensure sustained performance.

## Solution

Netmarble adopted a data-driven approach to use ADPF, focusing on dynamic adjustments based on real-time thermal status.

### Identify Performance Bottlenecks

Netmarble conducted a meticulous performance analysis, measuring the impact of various graphics quality settings on both frame rates and thermal load. This analysis revealed that resolution scaling had the most significant impact on GPU load and thermal output, without severely impacting frame rates. Importantly, they found that other graphics options (shadows, textures, etc.) had a comparatively minimal impact on overall thermal performance.

### Dynamic Resolution Scaling

Netmarble added a dynamic resolution system. It changes the game's image quality based on the device's temperature, using the ADPF Thermal API. This lets the game adapt to different conditions. When the device is cool, the game uses a high resolution. If the device gets too hot, the game lowers the resolution to reduce heat.

### Adaptive Frame Rate Adjustment

In conjunction with resolution scaling, Netmarble implemented dynamic frame rate adjustments. If the game's target FPS is set to 60, the system can gradually reduce the target FPS when excessive heat is detected. While avoiding the thermal issues, Netmarble set the minimum scalable FPS to 30. This ensured a consistent gaming experience. Additionally, the system is designed to gradually increase the FPS back to the target when heat decreases, maintaining optimal performance.

## Results

The implementation of dynamic resolution scaling and adaptive FPS adjustments, driven by ADPF, resulted in significant improvements in thermal management and sustained performance.
![](https://developer.android.com/static/images/cards/distribute/stories/netmarble_got.png)Netmarble: performance comparison

- **Improved Thermal Headroom:**ADPF reduced average thermal headroom from 1.04 to 0.92 (11% reduction), preventing performance degradation and enhancing device longevity. The thermal headroom value never exceeded 1.0, hence preventing device overheating.
- **More Consistent Frame Rates:**ADPF delivers a smoother gaming experience by intelligently adjusting the game's target FPS based on the device's thermal state. Without ADPF, the game's FPS could fluctuate significantly (e.g. from 40 to 56) due to thermal throttling. This inconsistent frame rate, caused by the device struggling to manage heat, can lead to a jarring and unpleasant gameplay experience. With ADPF, the game proactively reduces the target FPS as needed to prevent excessive heat buildup, ensuring a more stable and consistent frame rate, typically within the 50-60 FPS range. This prevents the abrupt frame drops associated with thermal throttling, resulting in a significantly improved and more enjoyable player experience.
- **Preserved High-Quality Graphics:**By prioritizing resolution scaling as the primary adjustment mechanism, Netmarble minimized the visual impact of thermal management, keeping other settings (textures, effects, etc.) at higher levels.

## Conclusion

By focusing on resolution scaling and dynamic FPS adjustments guided by ADPF, Netmarble successfully mitigated overheating issues in Game of Thrones: Kingsroad while preserving an optimal balance between performance, visual quality, and user experience. Their strategic use of ADPF highlights an effective approach for mobile game developers facing similar challenges. ADPF enabled a more reliable, enjoyable, and consistent experience, allowing players to play longer with fewer frame drops and reduced concerns about device overheating. With this solution in place, Netmarble continues to deliver high-quality gaming experiences while ensuring optimal device performance and longevity.

## Get started with ADPF today in Unity, Unreal and C++

Developers who are interested in using Android Adaptability should do the following:

- Learn more about[ADPF](https://developer.android.com/games/optimize/adpf), the[Unreal Engine ADPF plugin](https://github.com/android/adpf-unreal-plugin), and the[Unity Adaptive Performance Android provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@5.1/manual/index.html).
- Utilize ADPF with the default[Unity quality levels](https://docs.unity3d.com/Manual/class-QualitySettings.html)and[Unreal Engine scalability](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine).
- Monitor the performance of the game to ensure that it is meeting expectations. Experiment with different settings - resolution, frame rates, shadows, textures, etc - to find the best performance and minimal thermal increase.
- Change graphic quality settings separately to reduce sudden performance decreases.

Regardless of which engine you use, you can always choose to use the APIs directly. Learn more at[Android Adaptability](https://developer.android.com/games/optimize/adpf)and[Unreal Engine ADPF plugin](https://github.com/android/adpf-unreal-plugin).