---
title: https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security
url: https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Introducing the AndroidX Security State Libraries: A Unified View of Device Security

4 min read ![](https://developer.android.com/static/blog/assets/Android_X_Security_State_Library_Strapi_d3ecf61180_YYwl5.webp) 17 Sep 2026 3 Authors [Maunik Shah,](https://developer.android.com/blog/authors/maunik-shah) [Alec Garcia,](https://developer.android.com/blog/authors/alec-garcia) [Joseph Yong](https://developer.android.com/blog/authors/joseph-yong) At Android, we are constantly working to provide developers and enterprise partners with the data they need to keep devices protected. Today, we're thrilled to announce the stable release of the [**AndroidX Security State**](https://developer.android.com/jetpack/androidx/releases/security#security-state_2) **version 1.1.0** and [**Security State Provider**](https://developer.android.com/jetpack/androidx/releases/security#security-state-provider_2)**version 1.0.0** libraries which provides a centralized mechanism designed to bring further transparency to the comprehensive security posture and pending updates across the Android ecosystem.

Whether you develop security-critical, consumer-facing apps (such as banking, fintech, or healthcare) or Mobile Device Management (MDM) solutions, these libraries enable you to programmatically verify the security state of the device per component. Rather than relying on a coarse, monolithic Security Patch Level (SPL), you can evaluate true component-level protection and whether remediations are actively pending via the [androidx.security.state](https://developer.android.com/reference/kotlin/androidx/security/state/package-summary) library. For OEMs and Over-The-Air (OTA) client developers, the companion [androidx.security.state.provider](https://developer.android.com/reference/kotlin/androidx/security/state/provider/package-summary) library allows you to expose update availability via standardized mechanisms.

## **Understanding Security Patch Levels (SPL)**

As Android has evolved to deliver rapid, independent component updates through modular systems like Google Play system updates, relying on a single SPL build property is no longer the best way to determine a device's true security posture. To provide component level visibility, the Security State libraries provide APIs for three distinct patch levels:

- **Device SPL (DSPL):** The security patch level currently installed and running on the device for specific system components, queried from device properties and configs without network calls.
- **Published SPL (PSPL):** The latest patch level officially published in the [Android Security Bulletin](https://source.android.com/docs/security/bulletin) for those components.
- **Available SPL (ASPL):** The patch level ready to be downloaded and installed on the specific device, queried asynchronously via inter-process communication (IPC) with on-device update clients.

The Security State libraries track these patch levels across the following components:

- **System:**The core Android operating system, updated via standard/OEM system OTA updates.
- **System modules:**Modular OS subsystems updated seamlessly in the background via Google Play system updates (Project Mainline).
- **Kernel:**The foundational layer connecting the device's hardware and software, evaluated via Long-Term Support (LTS) release versions (such as 5.15.159 or 6.1.91) rather than monthly calendar dates.

By surfacing these three distinct patch levels at the component level, developers and enterprises can now understand exactly how secure a device is, identify missing patches, and take proactive remediation steps. One way of doing so can be seen in the example below.

Rather than taking an all-or-nothing approach to device access, developers and enterprises can combine DSPL, PSPL, and ASPL to make smart, contextual security decisions. For example, a banking or enterprise app can compare a device's current security patch (DSPL) against pending updates (ASPL) before initiating sensitive workflows like high-value payments or credential enrollment. If an update is waiting to be installed, developers and enterprises can require the user to update their device first. For even finer control, developers and enterprises can query whether specific high-risk vulnerabilities (CVEs) have been patched on the device, such as verifying that critical NFC or Bluetooth fixes are in place before authorizing tap-to-pay or proximity data sharing.

## **High-level flow**

![blog_effective_security_state.png](https://developer.android.com/static/blog/assets/blog_effective_security_state_cf811d99ca_Z1F4RwT.webp)

## For app developers and enterprise management

Client applications can use the [androidx.security.state](https://developer.android.com/reference/kotlin/androidx/security/state/package-summary) library to make informed, context-aware decisions:

- **Synchronous Posture Checks (DSPL)**: Apps can immediately inspect the installed patch levels of the system, system modules, and kernel on app launch and compare with PSPL to verify whether the device meets an organization's required security baseline before unlocking sensitive corporate resources or biometric access.
- **Pending Update Prompting (ASPL)**: Instead of immediately blocking an employee whose device is slightly behind on patches, enterprise apps can query ASPL to check if a pending system update or Google Play system update is staged and ready to install. If so, apps can display tailored in-app guidance directing the user to System Settings to complete the installation.
- **Vulnerability-Level Auditing (CVEs)**: For high-assurance use cases, the library provides ability to download device-specific vulnerability reports from Open Source Vulnerabilities (OSV) to programmatically audit whether specific, critical CVEs have been resolved on the device.

## For OEMs \& update clients: Standardizing update availability

The companion [androidx.security.state.provider](https://developer.android.com/reference/kotlin/androidx/security/state/provider/package-summary) library establishes a standardized, Android IPC mechanism for update clients to report update availability directly on the device. Historically, even if proprietary OTA clients surfaced update availability, this information was siloed and not queryable by third-party applications. Going forward, apps can access ASPL details through a single, unified API, regardless of whether the update is delivered via an OEM's dedicated OTA client or Google Play, as long as it is provided by the update client.

- Google Play system updates already expose ASPL across GMS Android devices.
- Google Over-The-Air (GOTA) has also been onboarded and we are working with OEMs worldwide to onboard their OTA clients to this standardized framework.

## Incorporating bulletin-level data

Beyond a single SPL string, the Security State libraries provide clarity on what that patch level actually means for the device. By integrating with the Open Source Vulnerabilities ([OSV](https://opensource.googleblog.com/2024/04/osv-and-helping-developers-fix-known-vulnerabilities.html)) database to obtain [Android Security Bulletin](https://source.android.com/docs/security/bulletin) data, the libraries can look deeper than ever before. Instead of just asking if a specific threat, such as a CVE entry, is blocked, this data also allows the libraries to provide the "effective" and granular security state of the device.

Here are two ways this approach benefits enterprises and Android OEMs:

- Sometimes, a monthly security update does not contain any new threats for a specific component. In this case, the libraries automatically increments the security level for that component to reflect its "effective" security state. This ensures that a device is accurately credited for being fully protected against all known security threats.
- A new feature introduced in Android 17 allows OEMs to declare specific security fixes that have been applied above the SPL via a [Supplemental Patches XML file](https://source.android.com/docs/security/overview/supplemental-security-patches). This feature allows OEMs who backport specific security fixes to immediately prove device compliance without having to wait for a full monolithic SPL bump, ensuring continuous patching efforts are properly credited. The Security State libraries surface this granular information to apps and services, ensuring that continuous patching efforts are recognized the moment they are implemented.

## **Get started**

The Security State Libraries are built to empower the entire Android ecosystem.

- **App Developers \& MDMs:** To start protecting your users and evaluating real-time patch posture, explore the official [Understand device security state guide](https://developer.android.com/privacy-and-security/understand-device-security-state).
- **OEMs and Update Clients:** Onboard your update clients to expose ASPL using the [AndroidX Security State Provider](https://developer.android.com/reference/kotlin/androidx/security/state/provider/package-summary) library. Claim immediate credit for backported patches by publishing [Supplemental Patches XMLs](https://source.android.com/docs/security/overview/supplemental-security-patches).
- **Release Notes:** Check out the official AndroidX Release Notes for [Security-State](https://developer.android.com/jetpack/androidx/releases/security#security-state_2) and [Security-State-Provider](https://developer.android.com/jetpack/androidx/releases/security#security-state-provider_2) libraries for complete changelogs and API signatures.

We value your feedback! Please try out the libraries and let us know your thoughts or report any issues on the public [Android Issue Tracker](https://issuetracker.google.com/issues?q=componentid:618647).
Written by:

-

  ## [Maunik Shah](https://developer.android.com/blog/authors/maunik-shah)

  ###### Staff Software Engineer,

  [read_more
  View profile](https://developer.android.com/blog/authors/maunik-shah) ![View Maunik Shah's profile](https://developer.android.com/static/blog/assets/secimage_fb4aa8502b_1n3cYA.webp) ![View Maunik Shah's profile](https://developer.android.com/static/blog/assets/secimage_fb4aa8502b_1n3cYA.webp)
-

  ## [Alec Garcia](https://developer.android.com/blog/authors/alec-garcia)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/alec-garcia) ![View Alec Garcia's profile](https://developer.android.com/static/blog/assets/unnamed_23_8ee579621d_Xq76V.webp) ![View Alec Garcia's profile](https://developer.android.com/static/blog/assets/unnamed_23_8ee579621d_Xq76V.webp)
-

  ## [Joseph Yong](https://developer.android.com/blog/authors/joseph-yong)

  ###### Technical Program Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/joseph-yong) ![View Joseph Yong's profile](https://developer.android.com/static/blog/assets/11299_bfb35d6c9d_Z1WIWC8.webp) ![View Joseph Yong's profile](https://developer.android.com/static/blog/assets/11299_bfb35d6c9d_Z1WIWC8.webp)
Continue reading
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Bench_2_0_Strapi_bench_8767d57564_ZmnAe.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks)

  [arrow_forward](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks) Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- 3 Authors 09 Sep 2026 09 Sep 2026 ![](https://developer.android.com/static/blog/assets/Introducing_Fast_and_Reliable_Wireless_Debugging_Strapi_cf55ad145b_2vFLdh.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing Fast and Reliable Wireless Debugging with Android Debug Bridge (ADB) Wi-Fi 2.0](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0) Wireless debugging on Android is now faster, more reliable, and easier to set up than ever. With ADB Wi-Fi 2.0, we've introduced a new server stack and smarter network handling to directly address developer feedback around usability gaps.
  [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins), [Sherif Eid](https://developer.android.com/blog/authors/sherif-eid), [Fabien Sanglard](https://developer.android.com/blog/authors/fabien-sanglard) • 1 min read
  - [#Wireless Debugging](https://developer.android.com/blog/topics/wireless-debugging)
  - [#ADB Wi-Fi 2.0](https://developer.android.com/blog/topics/adb-wi-fi-2-0)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_Z1CHwnO.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_ZqnmK9.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)