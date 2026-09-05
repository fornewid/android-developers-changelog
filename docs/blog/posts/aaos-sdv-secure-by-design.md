---
title: https://developer.android.com/blog/posts/aaos-sdv-secure-by-design
url: https://developer.android.com/blog/posts/aaos-sdv-secure-by-design
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# AAOS SDV - Secure by Design

5 min read ![](https://developer.android.com/static/blog/assets/Android_1_Strapi_6f49d09922_ZVXnJg.webp) 24 Aug 2026 3 Authors [Markus Vill,](https://developer.android.com/blog/authors/markus-vill) [Sean Keys,](https://developer.android.com/blog/authors/sean-keys) [István Nádor](https://developer.android.com/blog/authors/istvan-nador) At Google, we believe our products should be secure by design, which is why we built the Android Automotive Operating System for Software Defined Vehicle (AAOS SDV) on existing, [market-proven platforms](https://source.android.com/docs/automotive/sdv/workstreams/hardware/sdv-on-qnx), leveraging virtualization technologies like [Cuttlefish](https://source.android.com/docs/devices/cuttlefish). While our [release announcements](https://blog.google/products-and-platforms/platforms/android/android-automotive-os/) focused on the features, this blog post outlines some of the security concepts.

## Foundation: Domain Isolation

### Virtualization to isolate co-hosted instances

The current trend of consolidating Electronic Control Units (ECUs) into a single chip reduces isolation by running multiple domains side-by-side.

While AAOS SDV instances provide internal isolation mechanisms, it is often preferable to run logical domains independently. For instance, a cluster and an infotainment system have distinct requirements. We use virtual machines to run multiple instances in parallel, ensuring that sharing remains explicit and isolation is the default behavior.

### Inherited Android Security

AAOS SDV evolved from [Microdroid](https://source.android.com/docs/core/virtualization/microdroid), a minimalistic Android version optimized for privacy virtual machines (pVM). This lineage provides Android platform engineers with established security features they already know.

#### Process Isolation \& Deny by Default

AAOS SDV follows Android's User ID (UID)-based isolation model to set up a sandbox for each application. Each service runs in a dedicated process with a unique UID to manage access rights, data directories, and other restrictions. We employ Portable Operating System Interface (POSIX) capabilities to strictly limit operations and pair this with Security-Enhanced Linux (SELinux) to enforce a "deny-by-default" posture. This approach restricts each service to the absolute minimum required, meaning missing configurations block access rather than creating an over-permissive system. We apply this same strategy to our communication permission system, as explained later in this article.

#### Proven Vulnerability Management

AAOS SDV integrates Android's mature security response and vulnerability management infrastructure to identify, triage, remediate, and disclose security findings. This lifecycle incorporates continuous automated scanning, annual deep-dive penetration testing, and partner-driven intelligence via the [Android security vulnerability reporting process](https://source.android.com/docs/security/overview/updates-resources). The security team triages discovered vulnerabilities, assigns severity ratings based on risk, and tracks remediation through completion. We coordinate disclosure and release policies through the monthly [Android Security Bulletins](https://source.android.com/docs/security/bulletin), supplemented by rigorous periodic security audits and comprehensive architectural reviews to ensure long-term platform resilience.

## Integrity: Secure Software Delivery

Beyond guaranteeing process isolation, a secure platform must ensure code integrity before execution. We secure software delivery through the following approaches:

### Authenticated Software Delivery

AAOS SDV provides two installation methods. First, we install software directly to read-only system, product, or vendor partitions, which validate signatures on every boot. This secures basic system components.

Second, we utilize Android Pony EXpress ([APEX](https://source.android.com/docs/core/ota/apex)) packages for services. Each APEX encapsulates software and its dependencies, treating the package as a partition with mandatory signature validation. In AAOS SDV, APEX treats code signing as a continuous, hardware-enforced contract. APEX ensures malicious code execution is mitigated through four core pillars:

#### 1. Immutable Storage

- **The Mechanism:** The Android kernel loops the apex_payload.img file directly as a raw storage device using the **read-only loopback**, mounting it with the strict MS_RDONLY flag.
- **Why it's more secure:** This exposes no write path to the OS because the files are not unpacked onto the vehicle's storage. Even if an attacker gains root privileges, they cannot modify the running APEX code because the file system layer rejects all write commands.

#### 2. Cryptographic Integrity

- **The Mechanism:** The cryptographic signature validates a [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree) of the entire file system image.
- **Why it's more secure:** The kernel uses per-block dm-verity to verify the signature for every 4KB data block on-the-fly. If an attacker modifies a raw block on the flash memory, the kernel detects the hash mismatch and halts execution immediately.

#### 3. Strict Isolation

- **The Mechanism:** This applies the process isolation rules as described in the Process Isolation section to create a **sandbox**, with the APEX mounted as a dedicated partition under /apex.
- **Why it's more secure:** Each service receives its own user and data directory, restricting access unless sharing is explicit. By creating a dedicated partition, Android establishes a dedicated linker namespace, ensuring only explicitly exposed libraries are accessible from non-privileged system daemons, thus minimizing the attack surface.

#### 4. Atomic Recovery

- **The Mechanism:** APEX uses an "Active/Backup" design to enable **double-buffered rollbacks**. The factory-flashed APEX remains on the immutable /system partition, while updates reside on the mutable /data partition.
- **Why it's more secure:** If an update fails or appears malicious, the apexd daemon marks it as "failed" during early boot. The system instantly swaps symbolic links back to the /system partition. This atomic recovery helps ensure the system does not remain in a broken state.

## Resilience: Memory-Safe Development

Verified loading protects the system from external modification, but platform resilience also depends on how the underlying code is built. For new components developed for AAOS SDV, we prioritized memory safety.

### Rust as the primary language

AAOS SDV targets small systems with fast availability requirements; this prevents building on the full Android stack, so we limited our scope to the native framework. To create the required infrastructure for a distributed system, we developed multiple components in addition to existing infrastructure and adopted Rust as the primary language. We also use Rust to develop the business logic of services, helping partners write secure software. By design, [Rust leverages memory safety features to help prevent common classes of memory safety vulnerabilities, while supporting team throughput when writing native code](https://blog.google/security/rust-in-android-move-fast-fix-things/).

## Distributed Trust: Network \& Access Control

Software-defined vehicles require secure interactions between isolated domains. The AAOS SDV mesh provisioning architecture addresses this complexity by cryptographically verifying the version and author of every communication endpoint.

### Device and Mesh Provisioning

The AAOS SDV Mesh establishes authentication by [mathematically binding the network identity of every component](https://source.android.com/docs/automotive/sdv/workstreams/core/vm-attestation/dice-profile) to its **actual binary execution state**. This model replaces implicit software trust with hardware-rooted verification.

Mesh authentication is designed to be continuous and cryptographic. This prevents scenarios where, for example, a service like a vehicle gateway trusts a compromised infotainment VM just because it has the right IP address.

Hardware-enforced isolation and automated quarantine protocols secure the platform. Peer devices within the SDV mesh use DICE-based authentication and attestation, as detailed in the following section, to help identify and contain unauthorized code execution or configuration tampering.

### DICE-based TLS to secure VM-to-VM communication

Grounding the host identity in reality

**The Golden Rule of DICE (Device Identifier Composition Engine):** If a single line of code in the firmware changes (even a minor update or a malicious exploit), the derived Compound Device Identifier (CDI) changes entirely, generating a completely different Alias Key.

**DICE** and **TLS (Transport Layer Security)** integrate to solve the fundamental challenge of zero-trust architecture: authenticating a machine while simultaneously verifying its software integrity.

The combination of DICE's hardware-backed identification and TLS's encrypted handshake allows a receiving machine to verify both the caller's identity and its exact software state.

Traditional certificates only prove possession of a secret; they cannot detect firmware tampering. DICE addresses this via **measured boot layering**:

- **The Unique Device Secret (UDS):** A random cryptographic secret generated during manufacturing. Only the first-stage bootloader can access the UDS; it remains inaccessible to all other software and external interfaces.
- **Layered Measurements (The Compound Device Identifier):** The hardware ROM initiates the chain by hashing the UDS with the *exact code* and *configuration* of the next firmware layer. This creates a CDI, which then chains sequentially as each subsequent layer boots.

Strict access controls govern service interactions within the AAOS SDV mesh. Just like all AAOS SDV software, these access controls are authenticated, and their integrity is protected at the device level and across devices in the mesh through the DICE-based authentication.

### Layered Access Control

AAOS SDV employs a defense-in-depth strategy to enable dynamic vehicle updates without compromising access mechanisms. This model relies on two primary trust layers:

1. **Service-level permissions:** Define the specific resources a service on a given VM can access or expose across the mesh.
2. **VM-level permissions:** Define the cross-VM communication boundaries for all services hosted on a specific VM.

This model allows OEMs to balance security with updatability. For non-security-sensitive services, permissive VM-level policies enable installation via lightweight APEX updates rather than full VM redeployments.

Conversely, permissions for security-sensitive signals must be hard-coded into every VM. The tradeoff is that introducing a security-sensitive service to a new VM requires updating the VM-level permissions system-wide. This necessitates an update to all VMs within the mesh.

## Conclusion

![image.png](https://developer.android.com/static/blog/assets/image_8478613bb7_11crDa.webp)

AAOS SDV extends Android's security architecture to address specific automotive requirements through a secure-by-design approach. By leveraging virtualization for domain isolation and enforcing "deny-by-default" access policies, the platform establishes a resilient environment for software-defined vehicles. Cryptographic integrity is maintained via hardware-enforced, on-the-fly verification of executed code.

The platform integrates continuous security lifecycles, ranging from proactive vulnerability management to hardware-rooted identity verification via DICE. These multi-layered defenses allow OEMs to balance advanced feature updatability with the robust security necessary for modern automotive environments. Technical specifications and implementation details are available on the [AAOS SDV Overview page](https://source.android.com/docs/automotive/sdv).
- [#Android Auto](https://developer.android.com/blog/topics/android-auto)
- [#Security](https://developer.android.com/blog/topics/security)
Written by:

-

  ## [Markus Vill](https://developer.android.com/blog/authors/markus-vill)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/markus-vill) ![View Markus Vill's profile](https://developer.android.com/static/blog/assets/unnamed_19_3405162c1c_JCTR1.webp) ![View Markus Vill's profile](https://developer.android.com/static/blog/assets/unnamed_19_3405162c1c_JCTR1.webp)
-

  ## [Sean Keys](https://developer.android.com/blog/authors/sean-keys)

  ###### Security Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/sean-keys) ![View Sean Keys's profile](https://developer.android.com/static/blog/assets/unnamed_20_bdf4e82cc6_Z1w21P7.webp) ![View Sean Keys's profile](https://developer.android.com/static/blog/assets/unnamed_20_bdf4e82cc6_Z1w21P7.webp)
-

  ## [István Nádor](https://developer.android.com/blog/authors/istvan-nador)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/istvan-nador) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![View Charles Munger's profile](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)
Continue reading
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)