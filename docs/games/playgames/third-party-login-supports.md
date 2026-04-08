---
title: Third-party login support  |  Android game development  |  Android Developers
url: https://developer.android.com/games/playgames/third-party-login-supports
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Google Play](https://developer.android.com/distribute)
* [Games dev center](https://developer.android.com/games)
* [Guides](https://developer.android.com/games/guides)

Send feedback

# Third-party login support Stay organized with collections Save and categorize content based on your preferences.




This guide describes how to use
[`CustomTabsIntent`](/reference/androidx/browser/customtabs/CustomTabsIntent)
to support third-party logins.

## Web Uri intent

Google Play Games for PC redirects all regular web
[`Uri intents`](/guide/components/intents-common#Browser) to the default Windows
browser for an optimized user experience. Games don't receive any information
back from the default Windows browser, so this flow doesn't allow you to login
users via a third-party login or a social platform.

## CustomTabsIntent

However, Google Play Games for PC allows popular third-party login methods to
work using
[`CustomTabsIntent`](/reference/androidx/browser/customtabs/CustomTabsIntent)
objects such that no changes are expected on developers' end for user login.

If you want to register a new login site, you should reach out to your Google
contact.






Send feedback