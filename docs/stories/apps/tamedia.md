---
title: Tamedia increased subscriber conversion with custom alerts  |  Developer stories  |  Android Developers
url: https://developer.android.com/stories/apps/tamedia
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Developer stories](https://developer.android.com/stories)

# Tamedia increased subscriber conversion with custom alerts Stay organized with collections Save and categorize content based on your preferences.



![](/static/images/distribute/stories/tamedia-icon.png)

Tamedia is a Swiss media group which publishes daily and weekly newspapers,
magazines, and digital platforms. They offer monthly and daily subscriptions to
[Berner Zeitung (BZ)](https://play.google.com/store/apps/details?id=ch.bernerzeitung.app&hl=en) -
their main daily publication in the canton of Berne, and
[24 Heures](https://play.google.com/store/apps/details?id=com.bewoopi.launcher.heures) -
their highest-circulation daily title in French, on Google Play.

Their goal with both [BZ](https://play.google.com/store/apps/details?id=ch.bernerzeitung.app&hl=en)
and [24 Heures](https://play.google.com/store/apps/details?id=com.bewoopi.launcher.heures)
apps is to increase sales of their monthly subscriptions.

The value of the monthly subscription is higher than the daily one to readers as
they get access to premium content for longer, even if the subscription price is
higher. The monthly subscription also offers Tamedia a great opportunity to
build user loyalty to their brand, as users spend more time trying and
experiencing the apps’ content.

Tamedia therefore wanted to test how they could improve awareness of their
offers and subscriptions goals performance.

![](/static/images/distribute/stories/tamedia-feature01.png)

![](/static/images/distribute/stories/tamedia-feature02.png)

## What they did

Tamedia decided to focus on frequent users who were not yet subscribed to their
apps’ premium content. In order to raise awareness of their subscription offers,
they tested two free Firebase features: **user segmentation via Firebase Analytics,
and custom messages via Firebase In-App Messaging.**

* In [BZ](https://play.google.com/store/apps/details?id=ch.bernerzeitung.app&hl=en),
  through [Firebase in-app messaging](https://firebase.google.com/products/in-app-messaging/?gclid=CNDSrZims94CFRRzGwodNYgMiA),
  non-subscribed users that opened the app more that 5 times within 7 days
  received an in-app notification advertising the subscription offer with a direct
  link to the in-app subscription screen.
* In [24 Heures](https://play.google.com/store/apps/details?id=com.bewoopi.launcher.heures),
  when non-subscribed users clicked on premium content more than 3 times without
  subscribing, they received an in-app reminder of the offer.

## Results

Their hypothesis was proven correct. Frequent readers are more willing to
subscribe when receiving a tailor made product offer according to their content
consumption through in-app notifications.

* In [BZ](https://play.google.com/store/apps/details?id=ch.bernerzeitung.app&hl=en),
  the number of in-app purchases of **subscriptions increased by 29%**, compared to
  the previous 3 month period. **82% of total purchases** were through the
  subscription notification.
* In [24 Heures](https://play.google.com/store/apps/details?id=com.bewoopi.launcher.heures),
  **in-app purchases increased by 8% after the introduction of custom alerts** to
  readers who hit the paywall twice. More than two thirds of all total subscriptions,
  resulted from implementing custom alert notifications.

## Get started

[Learn how to segment your users with Google Analytics for Firebase](/distribute/best-practices/engage/segment-google-analytics-for-firebase)
and engage your active app users with
[Firebase In-App Messaging](https://firebase.google.com/products/in-app-messaging/?gclid=CNDSrZims94CFRRzGwodNYgMiA).

You can also find out more about selling digital content from inside your
Android app or in-app with [Google Play Billing](/google/play/billing/billing_overview).