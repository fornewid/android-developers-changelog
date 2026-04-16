---
title: https://developer.android.com/blog/posts/beyond-infotainment-extending-android-automotive-os-for-software-defined-vehicles
url: https://developer.android.com/blog/posts/beyond-infotainment-extending-android-automotive-os-for-software-defined-vehicles
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Beyond Infotainment: Extending Android Automotive OS for Software-defined Vehicles

###### 3-min read

![](https://developer.android.com/static/blog/assets/AAOS_SDV_Hero_dark_6dfe605408_bCiba.webp) 24 Mar 2026 [![](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z1jraMn.webp)](https://developer.android.com/blog/authors/eser-erdem) [##### Eser Erdem](https://developer.android.com/blog/authors/eser-erdem)

###### Engineering Manager

At Google we're deeply committed to the automotive industry--not just as a technology provider, but as a partner in the industry's transformation. We believe that car makers and users should have choice and flexibility, and that open platforms are the best enablers. For over a decade, we have provided Android Automotive OS (AAOS) as an open platform for infotainment, enabling rich innovation and differentiation in the in-vehicle digital experience. However, as vehicles modernize, car makers face new hurdles: fragmented software across compute components, poor portability between architectures, and a lack of granular update capabilities. To address these problems, we are expanding AAOS beyond infotainment with Android Automotive OS for Software Defined Vehicles (AAOS SDV)--an open platform featuring a modular structure, a topology-agnostic communication layer, and the support for granular updates.  

The transition toward SDVs is an incredible industry transformation, and we are eager to contribute to the broader ecosystem making it happen. Later this year, AAOS SDV will be available in the [Android Open Source Project (AOSP)](https://source.android.com/docs/automotive/start/what_automotive) for uses beyond infotainment. By bringing our SDV platform into the open-source domain, we empower the industry to develop or enhance features that lower costs, accelerate time to market, and provide significant advantages across the automotive landscape.
![automotive-os.webp](https://developer.android.com/static/blog/assets/automotive_os_28b164eff1_1dW7YL.webp)

#### A Foundation for the Software-Defined Vehicle

AAOS SDV is engineered to address the core challenges of modern vehicle development. This new AAOS expansion provides a compact, performant and scalable software foundation based on a headless Android native stack, extending much deeper into the vehicle architecture to power software components throughout the vehicle such as the seat actuator, instrument cluster, climate control, lighting, cameras, mirrors, telemetry, and more.  

AAOS SDV's core is a lightweight Android-based operating system incorporating low-level automotive specific frameworks for communications, diagnostics, software updates, and more. This enables AAOS SDV to power many different vehicle controllers, tackling Core Compute, Body Controls, and Cluster domains.  

In addition, the AAOS SDV platform includes a new framework, Display Safety, for implementing instrument cluster applications including audible chimes, regulatory camera, and sophisticated graphics that blend seamlessly with AAOS IVI content. Display Safety includes a safety design toolchain and a reference safety monitor, allowing OEMs to meet functional safety requirements leveraging the diverse platform safety mechanisms of Automotive SoCs.
![large_Google AAOS SDV Blog - Simplified Vehicle Architecture Animated (2).gif](https://developer.android.com/static/blog/assets/large_Google_AAOS_SDV_Blog_Simplified_Vehicle_Architecture_Animated_2_e9a497fff5_Zz1Uwv.webp)

**Flexible Deployment for AAOS SDV**

*Engineered for flexibility, the AAOS SDV framework can utilize hypervisor-backed virtualization with virtio support to separate software domains, or it can be deployed on bare metal for optimal low-latency performance.*

#### Transforming the Developer Experience

AAOS SDV is designed to power modern vehicles, but it was also designed to change how modern vehicle software is developed, tested and delivered with the goals to reduce development time and cost while increasing innovation and agility. With its optimized development workflows, our open-source SDV platform provides a wide range of benefits across the automotive industry:  

- **Accelerated Time-to-Market:** AAOS SDV components can accelerate development with production ready software for various components that can be further modified.
- **Standard Signal Catalog:** A new standard signal catalog to bring OEMs and automotive suppliers onto the same page eliminates redundant engineering efforts and significantly reduces platform development costs.
- **Optimized for virtual cloud development:** AAOS SDV was designed ground-up to support virtual cloud development - enabling partners to design, test and validate components in the car well ahead of hardware availability. AAOS SDV already runs on Android Virtual Device ([Cuttlefish](https://source.android.com/docs/devices/cuttlefish)), and works well with existing Google Cloud integrations such as [Google Cloud Horizon](https://cloud.google.com/blog/topics/manufacturing/slash-android-automotive-os-build-times-and-get-to-market-faster-with-horizon-on-google-cloud), enabling a digital twin solution at scale.
- **A Service-Oriented Architecture:**Vehicle functions are developed as topology-agnostic services which are reusable across different architectures. The platform treats the vehicle as a dynamic, connected system. This allows for granular, service-level updates with built-in dependency handling, enabling you to deploy new features over-the-air and create continuous improvement loops.
- **Future-Ready for new services:** The platform is designed to simplify the development of telemetry, AI training feedback loops, accelerating the deployment of advanced features for both enterprise fleets and consumer vehicles.

#### Production Ready: Partnering with Renault

We are proud to highlight our deep partnership with Renault to underscore the production readiness of the AAOS SDV platform. Renault is currently leveraging the Android Automotive OS SDV platform for its upcoming Renault Trafic e-Tech, "[\[...\] production set to begin in late 2026](https://media.renault.com/new-renault-trafic-van-e-tech-electric-a-new-efficient-agile-and-innovative-vehicle-for-business-users/?lang=eng)". The Renault Trafic e-Tech validates the platform's ability to accelerate development and enable a new generation of software-defined commercial vehicles.  

#### Scaling Ready: Partnering with Qualcomm

Qualcomm is scaling the Android Automotive OS SDV platform through our strategic partnership. At CES 2026, Qualcomm introduced [Snapdragon vSoC on Google Cloud](https://www.qualcomm.com/news/onq/2026/01/snapdragon-vsoc-aaos-sdv-google-cloud) and announced a scaling collaboration to deliver a turnkey, pre-integrated AAOS SDV stack on Snapdragon Digital Chassis platforms.  

#### Building an Open AAOS Ecosystem

The power of AAOS comes from its vibrant ecosystem. To prepare for the open source release later this year, we are proactively working with leading industry carmakers, suppliers, silicon platforms, and software vendors to ensure that the AAOS SDV platform is well supported and robustly integrated within the automotive ecosystem. We look forward to sharing more updates with our partners in the months ahead.
- [#Automotive OS](https://developer.android.com/blog/topics/automotive-os)

###### Written by:

-

  ## [Eser Erdem](https://developer.android.com/blog/authors/eser-erdem)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/eser-erdem) ![](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z1jraMn.webp) ![](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z1jraMn.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) 15 Apr 2026 15 Apr 2026 ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boosting user privacy and business protection with updated Play policies](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)

  [arrow_forward](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies) Making Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) 13 Apr 2026 13 Apr 2026 ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Test Multi-Device Interactions with the Android Emulator](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator)

  [arrow_forward](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator) Testing multi-device interactions is now easier than ever with the Android Emulator.

  ###### [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)