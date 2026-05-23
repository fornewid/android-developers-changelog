---
title: https://developer.android.com/google/play/integrity/demo
url: https://developer.android.com/google/play/integrity/demo
source: md.txt
---

Play Integrity API (PIA) is an anti-abuse tool for Android developers to detect
risky devices and security threats. This demo, which uses a sample app for
testing purposes, provides a guided learning experience through
standard use cases for the Play Integrity API.

After creating the sample Android app and Node server, the initial setup
requires a single Project linking to connect the Google Cloud project to the
app in the Play Console.

The demo then guides you through the Features configuration specific to each
micro-app. For example:

- **Protecting server-side resources (e.g., Streaming micro-app):** This demonstrates how to implement tiered content delivery or responses based on the device recognition verdicts and attributes.
- **Protecting against client-side exploitation (e.g., Game micro-app):** This focuses on protecting a session environment by using PIA verdicts to detect malicious apps on the device, as well as unauthorized apps capturing the screen or controlling the device during a protected session.
- **Securing high-value actions (e.g., Bank micro-app):** This showcases how to protect critical user interactions by enforcing device integrity and content binding.

## Prerequisites

Before you begin this demo, you should do the following:

- [API overview](https://developer.android.com/google/play/integrity/overview): What the Play Integrity API is, and how it supports a secure environment for developers and their users.
- [Key terms](https://developer.android.com/google/play/integrity/terms) and data safety concepts.

## Download the sample app

We have published an open-source feature sample to the official Android GitHub
account. This sample provides a best-practice implementation of the Play
Integrity API standard request flow.

[Download the PIA sample app](https://github.com/android/security-samples/tree/main/PlayIntegrityAPI)

The sample includes:

- A canonical end-to-end reference implementation for Play Integrity API Standard requests.
- Best practices for token preparation and content binding.
- Use of optional features: Strong integrity, device attributes, and environment details (e.g. app access risk and Play Protect verdict).
- Actionable examples for handling API responses, including error codes (with retry strategies) and triggering in-app Remediation Dialogs.