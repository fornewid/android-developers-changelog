---
title: https://developer.android.com/google/play/integrity/demo
url: https://developer.android.com/google/play/integrity/demo
source: md.txt
---

Play Integrity API is an anti-abuse tool for Android developers to detect risky
devices and security threats. This demo, which uses a sample app for testing
purposes, provides a guided learning experience through standard use cases for
the Play Integrity API.

After you create the sample Android app and Node server, link a Google Cloud
project to the app in the Play Console to complete the initial setup.

The demo then shows you the features configuration for each micro-app. For
example:

- **Protecting server-side resources (for example, a streaming micro-app):** This demonstrates how to implement tiered content delivery or responses based on the device recognition verdicts and attributes.
- **Protecting against client-side exploitation (for example, a game
  micro-app):** This focuses on protecting a session environment by using Play Integrity API verdicts to detect malicious apps on the device, as well as unauthorized apps capturing the screen or controlling the device during a protected session.
- **Securing high-value actions (for example, a bank micro-app):** This showcases how to protect critical user interactions by enforcing device integrity and content binding.

## Prerequisites

Before you begin, you should be familiar with the following:

- [API overview](https://developer.android.com/google/play/integrity/overview): what the Play Integrity API is, and how it supports a secure environment for developers and their users.
- [Key terms](https://developer.android.com/google/play/integrity/terms) and data safety concepts.

## Download the sample app

We have published an open-source feature sample to the official Android GitHub
account. This sample provides a best-practice implementation of the Play
Integrity API standard request flow.

[Download the sample app](https://github.com/android/security-samples/tree/main/PlayIntegrityAPI)

The sample includes:

- A canonical end-to-end reference implementation for Play Integrity API standard requests.
- Best practices for token preparation and content binding.
- Use of optional features: strong integrity, device attributes, and environment details (for example, app access risk and Play Protect verdict).
- Actionable examples for handling API responses, including error codes (with retry strategies) and triggering in-app Remediation Dialogs.