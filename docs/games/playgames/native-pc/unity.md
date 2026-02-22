---
title: https://developer.android.com/games/playgames/native-pc/unity
url: https://developer.android.com/games/playgames/native-pc/unity
source: md.txt
---

The Google Play Games PC SDK for Unity provides a native C# interface for
integrating Google Play Games Services on PC. This package is built specifically
for the Unity engine, wrapping the underlying C++ SDK to provide a modern,
type-safe, and asynchronous API for C# developers.

The Unity package, allow integration of core features, specifically
Billing and Integrity, without requiring custom native wrappers or manual C++
interop management.

### Key features

- **Native C# Support:** Access the full Play Games PC SDK using standard C# classes and methods. The wrapper handles all marshalling between C# and the native C++ libraries.
- **Modern Async API:** All asynchronous operations use standard C# Task and async or await patterns. This replaces legacy callback mechanisms, making your code cleaner and more readable.
- **Unified Error Handling:** API results use a standardized Result pattern. Check `Result.IsOk` to verify success or inspect `Result.Code` for specific error enums (For example, `BillingError`, `IntegrityError`).
- **x86 and x64 architecture support:** The package includes native binaries for both **x86** and **x64** architectures. This lets you to build 32-bit or 64-bit versions of your game that are fully compatible with the 64-bit Google Play Games on PC runtime environment.
- **Unity Package Manager (UPM) Format:** Distributed as a standard tar file with clean dependency management and version control integration.

### Supported features

This current release supports the following Google Play modules:

- **Initialization:** Manage the connection lifecycle between your Unity game and the Google Play Games on PC platform.
- **Google Play Billing:** Full support for In-App Purchases (IAP) and subscriptions using the modern `BillingClient`.
- **Play Integrity:** Protect your game from abuse and unauthorized modifications by requesting integrity tokens directly from Unity.

## System Requirements

Before you begin, verify your development environment meets the following
requirements:

| Component | Requirement |
|---|---|
| Unity Version | **2018.4** or higher |
| Scripting Backend | **IL2CPP** |
| API Compatibility | **.NET Standard 2.0** or **.NET Framework 4.x** |
| Target Platform | **OS:** Windows (64-bit) **Supported Game Architecture:** x86 (32-bit) or x64 (64-bit) |

## Next steps

Consider the following next steps:

- Learn how to [integrate Google Play Games PC SDK with Unity](https://developer.android.com/games/playgames/native-pc/unity/unity_start) using UPM and configure your build manifest.
- View code samples and reference documentation for [features](https://developer.android.com/games/playgames/native-pc/unity/features) such as Billing, Integrity, and Initialization.