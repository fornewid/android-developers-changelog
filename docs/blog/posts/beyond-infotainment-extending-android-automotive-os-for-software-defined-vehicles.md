---
title: https://developer.android.com/blog/posts/beyond-infotainment-extending-android-automotive-os-for-software-defined-vehicles
url: https://developer.android.com/blog/posts/beyond-infotainment-extending-android-automotive-os-for-software-defined-vehicles
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Beyond Infotainment: Extending Android Automotive OS for Software-defined Vehicles

3 min read ![](https://developer.android.com/static/blog/assets/AAOS_SDV_Hero_dark_6dfe605408_iURQs.webp) 24 Mar 2026 [![View Eser Erdem's profile](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z2lhw4j.webp)](https://developer.android.com/blog/authors/eser-erdem) [Eser Erdem](https://developer.android.com/blog/authors/eser-erdem) Engineering Manager At Google we're deeply committed to the automotive industry--not just as a technology provider, but as a partner in the industry's transformation. We believe that car makers and users should have choice and flexibility, and that open platforms are the best enablers. For over a decade, we have provided Android Automotive OS (AAOS) as an open platform for infotainment, enabling rich innovation and differentiation in the in-vehicle digital experience. However, as vehicles modernize, car makers face new hurdles: fragmented software across compute components, poor portability between architectures, and a lack of granular update capabilities. To address these problems, we are expanding AAOS beyond infotainment with Android Automotive OS for Software Defined Vehicles (AAOS SDV)--an open platform featuring a modular structure, a topology-agnostic communication layer, and the support for granular updates.  

The transition toward SDVs is an incredible industry transformation, and we are eager to contribute to the broader ecosystem making it happen. Later this year, AAOS SDV will be available in the [Android Open Source Project (AOSP)](https://source.android.com/docs/automotive/start/what_automotive) for uses beyond infotainment. By bringing our SDV platform into the open-source domain, we empower the industry to develop or enhance features that lower costs, accelerate time to market, and provide significant advantages across the automotive landscape.
![automotive-os.webp](https://developer.android.com/static/blog/assets/automotive_os_28b164eff1_1qFvFP.webp)

#### A Foundation for the Software-Defined Vehicle

AAOS SDV is engineered to address the core challenges of modern vehicle development. This new AAOS expansion provides a compact, performant and scalable software foundation based on a headless Android native stack, extending much deeper into the vehicle architecture to power software components throughout the vehicle such as the seat actuator, instrument cluster, climate control, lighting, cameras, mirrors, telemetry, and more.  

AAOS SDV's core is a lightweight Android-based operating system incorporating low-level automotive specific frameworks for communications, diagnostics, software updates, and more. This enables AAOS SDV to power many different vehicle controllers, tackling Core Compute, Body Controls, and Cluster domains.  

In addition, the AAOS SDV platform includes a new framework, Display Safety, for implementing instrument cluster applications including audible chimes, regulatory camera, and sophisticated graphics that blend seamlessly with AAOS IVI content. Display Safety includes a safety design toolchain and a reference safety monitor, allowing OEMs to meet functional safety requirements leveraging the diverse platform safety mechanisms of Automotive SoCs.
![large_Google AAOS SDV Blog - Simplified Vehicle Architecture Animated (2).gif](https://developer.android.com/static/blog/assets/large_Google_AAOS_SDV_Blog_Simplified_Vehicle_Architecture_Animated_2_e9a497fff5_Z1jECiW.webp)

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
Written by:

-

  ## [Eser Erdem](https://developer.android.com/blog/authors/eser-erdem)

  ###### Engineering Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/eser-erdem) ![View Eser Erdem's profile](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z2lhw4j.webp) ![View Eser Erdem's profile](https://developer.android.com/static/blog/assets/Eser_Blue_ae0cb5cc85_Z2lhw4j.webp)
Continue reading
- [![View Ataul Munim's profile](https://developer.android.com/static/blog/assets/Ataul_Munim_cf0796f68c_ZXRdHk.webp)](https://developer.android.com/blog/authors/ataul-munim) 02 Jun 2026 02 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Differentiated_Experiences_Strapi_bbe8e7618b_Z2f8lth.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building Premium Android Experiences at Google I/O '26](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/building-premium-android-experiences-at-google-i-o-26) At Google I/O '26, we showcased how the latest advancements in the Android ecosystem can help you elevate your app's quality while maximizing development efficiency.
  [Ataul Munim](https://developer.android.com/blog/authors/ataul-munim) • 3 min read
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - [#Memory](https://developer.android.com/blog/topics/memory)
  - [#Widgets](https://developer.android.com/blog/topics/widgets)
  - [#R8](https://developer.android.com/blog/topics/r8)
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#Automotive OS](https://developer.android.com/blog/topics/automotive-os)
  - +4 ↩
- 3 Authors 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Android_X_Security_State_Library_Strapi_d3ecf61180_YYwl5.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing the AndroidX Security State Libraries: A Unified View of Device Security](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security) Today, we're thrilled to announce the stable release of the AndroidX Security State version 1.1.0 and Security State Provider version 1.0.0 libraries.
  [Maunik Shah](https://developer.android.com/blog/authors/maunik-shah), [Alec Garcia](https://developer.android.com/blog/authors/alec-garcia), [Joseph Yong](https://developer.android.com/blog/authors/joseph-yong) • 4 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Bench_2_0_Strapi_bench_8767d57564_ZmnAe.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks)

  [arrow_forward](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks) Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)