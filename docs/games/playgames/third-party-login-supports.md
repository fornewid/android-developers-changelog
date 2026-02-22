---
title: https://developer.android.com/games/playgames/third-party-login-supports
url: https://developer.android.com/games/playgames/third-party-login-supports
source: md.txt
---

This guide describes how to use
[`CustomTabsIntent`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsIntent)
to support third-party logins.

## Web Uri intent

Google Play Games for PC redirects all regular web
[`Uri intents`](https://developer.android.com/guide/components/intents-common#Browser) to the default Windows
browser for an optimized user experience. Games don't receive any information
back from the default Windows browser, so this flow doesn't allow you to login
users via a third-party login or a social platform.

## CustomTabsIntent

However, Google Play Games for PC allows popular third-party login methods to
work using
[`CustomTabsIntent`](https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsIntent)
objects such that no changes are expected on developers' end for user login.

If you want to register a new login site, you should reach out to your Google
contact.