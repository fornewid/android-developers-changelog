---
title: https://developer.android.com/games/playgames/native-pc/setup/developer_mode
url: https://developer.android.com/games/playgames/native-pc/setup/developer_mode
source: md.txt
---

In order to successfully initialize the SDK inside of a game several
requirements must be satisfied. These include:

- Running from a digitally signed game executable

- Launching the game executable from Google Play Games

These can be burdensome for developers that are actively building their game
inside of a game editor or code IDE as they require packaging \& publishing the
game for release.

To provide a better development workflow the SDK offers a developer
mode. When enabled, the developer mode allows the SDK to function inside
of a game editor or code IDE. The SDK can be initialized without
requiring the executable to be digitally signed or launched from Google Play
Games.

## Prerequisites

- Obtain an early-access partner (EAP) GUID. This a secret key that allows your development team to use the SDK from within your game engine editor without needing to package or digitally sign your game executable or launch it from Google Play Games.

> [!NOTE]
> **Note:** Work with your Google Partner to get an early-access partner GUID for your development team. If you don't have an early-access partner, complete the [express interest form](https://docs.google.com/forms/d/e/1FAIpQLScn35BX-X63ggG84S76okR37nwq6qRA1PNPk4fsBpDbD7J21Q/viewform?_ga=2.233777694.1640262997.1747860154-345235146.1745606832).

## **Step 1**: Enable developer mode in the manifest

> [!WARNING]
> **Warning:** Make sure to remove the `<IsDeveloperMode>` tag before publishing your game.

Enable developer mode for your application by setting `IsDeveloperMode` to
`true` inside of the your application's `manifest.xml`.

    <?xml version="1.0" encoding="utf-8"?>
    <Manifest version="1">
        <Application>
            <PackageName>com.example.package</PackageName>
            \<IsDeveloperMode\>true\</IsDeveloperMode\>
        </Application>
    </Manifest>

## **Step 2**: Enable early access

> [!WARNING]
> **Warning:** The early access partner GUID is a secret. Don't share this value.

Enable early access on the device where your are testing by setting the
`EarlyAccessPartnerGuid` string value under the
`HKLM\Software\Google\Play Games Services\EarlyAccessPartnerGuid` registry key.

This can be done either using the Windows Registry Editor, or from an admin cmd
terminal with the command:

    C:\> reg add "HKLM\Software\Google\Play Games Services" /v EarlyAccessPartnerGuid /t REG_SZ /d EAP GUID

## **Step 3**: Sign into Google Play Games for PC

When developer mode is enabled, the SDK uses the account signed into
[Google Play Games for PC](https://play.google.com/googleplaygames) when making API
calls. If multiple accounts are signed in, the active account will be used.

If your game not been publicly released (has never published to the production
release track inside of the Play Console), we recommend using a Google Account
that has joined your game's internal testing group. Internal testers will have
access to your game before release which is required for some SDK APIs to
function. For example, completing a purchase with Play Billing. You may manage
your app's internal testers inside of the
[Play Console](https://play.google.com/console/about/internal-testing/).

## Next steps

Add Google Play PC features to your app:

- Sell digital goods with [Play Billing](https://developer.android.com/games/playgames/native-pc/billing)
- Measure your marketing with [Play Install Referrer](https://developer.android.com/games/playgames/native-pc/install_referrer)
- Protect your game with [Play Integrity for PC](https://developer.android.com/games/playgames/native-pc/trust)