---
title: https://developer.android.com/games/playgames/native-pc/faq
url: https://developer.android.com/games/playgames/native-pc/faq
source: md.txt
---

This document answers common questions about SDKs and publishing for
Google Play Games on PC.

## How to add a VPN?

For developers requiring to test their game in [regions](https://support.google.com/googleplay/answer/11358071#zippy=%2Ccountryregion-availability)
where Google Play Games on PC is not supported, we recommend that you use a
VPN to acquire an IP address from a [supported region](https://support.google.com/googleplay/answer/11358071).

Ensure that you enable [TUN mode](https://proprivacy.com/guides/tun-tap) on VPN.
Guidance on enabling TUN mode and configuring the firewall can be found in
the VPN provider's operating manual.

After the TUN mode is enabled, [install](https://play.google.com/googleplaygames/?e=WebskySupportFCCInFCP::Arm_Launch) the Google Play Games on PC and
the [emulator](https://developer.android.com/games/playgames/emulator) for testing purposes.

## Can you use the purchase flow without a backend server?

From a security perspective, processing without a backend server is generally
not recommended.

For more information,
see [Process without a backend server](https://developer.android.com/games/playgames/native-pc/billing#process-no-backend).

> [!NOTE]
> **Note:** To process purchases without a backend server, you need special permissions. If your game requires these permissions, contact your Google partner.

## How to start developing for Google Play Games on PC in Unity or UE Editor?

- Enable the [developer Mode](https://developer.android.com/games/playgames/native-pc/setup/developer_mode) and proceed with testing.
- Add the `manifest.xml` and `.dll` files. For more information, see [developer document](https://developer.android.com/games/playgames/native-pc/setup#prerequisites).
- Register an [early access partner GUID](https://developer.android.com/games/playgames/native-pc/setup/developer_mode#step-2) for testing purposes.

## When you start a game using the Google Play Games app, does it sync your Google Account details

After launching the game through Google Play Games client, the account is
automatically synchronized and there's no need to login through the Google
Login process again.

## When submitting a Windows App Bundle (WAB) using a 3P launcher, is the game package required for review?

You can just submit your installer and don't need to submit your entire game
package, the reviewer will be able to download your game package using the
installer.

> [!NOTE]
> **Note:** This guidance is specifically for developers using a 3P launcher to call your game.

## If a player uses a 3P launcher instead of the Google Play Client, will their Play Games Services account sync automatically?

For the SDK functions to operate, the game must be launched directly
through the Google Play Games client. If another process, such as an
installer or launcher application, initiates the game, then that process
must itself be launched from the Google Play Games client. The game must
pass all parameters received from the client to the client process.

## How does the SDK handle Google Account sign-in for multiple instances or accounts?

Each game launch in GPG is treated as a "game session" and each "game
session" can have an account associated with it. They can be different.
So if you launch the game with account A, and then switch to account B and
relaunch both can run at the same time.

## Are there any limitations of WAB (Windows App Bundle) file size?

You can upload up to 10 GB file size for a WAB.

## Are existing API-based payment systems allowed after integrating the Google Play Games on PC SDK?

All payments must be handled by Google Play Games on PC SDK using the
Google Play Billing. You cannot use your existing API-based payment method
in the same game.

## Are there any open testing or closed testing environments similar to the mobile?

While a dedicated end-to-end sandbox isn't currently available, we
recognize the need for a production-like testing environment for developers.
A more robust solution will be offered soon.

## We cannot correctly consume purchases initiated in developer mode?

Consume purchase in the developer mode has to be done within 3 minutes, otherwise the purchase might have been refunded.

## Are there any differences between API (legacy) and Google Play Games on PC SDK?

- Legacy focused only on Billing
- The SDK will support Google Desktop Service (GDS) and full PC features
- Developer-friendly SDK interface
- No browser-based Google Sign-in needed

## Is there an alternative way to initialize the SDK by launching the game directly using the game launcher, without going through Google Play Games on PC?

Game has to be launched through the Google Play Games on PC client.
For more details, see [developer document](https://developer.android.com/games/playgames/native-pc/setup#step-4)

## Recurring payments or subscriptions are unsupported; are there any plans to implement this?

There is no plan to add those purchase options beyond the In-App Purchase, we are welcomed to get your feedback with a specific use cases.

## In the payment process, is the error code in the [billingerror](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/billing#billingerror) returned as the response of launching the purchase flow or obtaining the payment result? For purchase flow, can't we just await the SDK result instead of using a listener?

It is the response of the payment result. LaunchPurchaseFlow will return immediately without blocking but you have to listen to the callback in-order to know when it has finished and to capture the result.

## Is there any way to create a short cut to open the game directly?

You can use the following URI for opening the game directly:

`googleplaygames://launch/?pid=2&id=com.company.gamename`

The URI supports detecting whether the Google Play Games on PC client is opened. If the client is not open, the GPG client opens before the game/launcher runs. You need to manage the game/launcher to prevent multiple instances from running.

## `QueryProductDetails` API request limits

The maximum number of products that can be queried in a single call to the
[`QueryProductDetails`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client#queryproductdetails)
API is 50. If you exceed this limit, you must split the request into multiple
calls.