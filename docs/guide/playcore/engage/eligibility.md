---
title: https://developer.android.com/guide/playcore/engage/eligibility
url: https://developer.android.com/guide/playcore/engage/eligibility
source: md.txt
---

> [!IMPORTANT]
> **Important:** Complete the [Engage SDK interest form](https://support.google.com/googleplay/contact/Engage_SDK) to get started.

## What to expect

To integrate the Engage SDK, follow these steps:

1. Review the following requirements to determine if your app meets the eligibility criteria.
2. [Submit the Engage SDK interest form](https://support.google.com/googleplay/contact/Engage_SDK). Google reviews your app's eligibility and replies within two weeks.
3. Follow the category-specific integration guide and [integration workflow](https://developer.android.com/guide/playcore/engage/workflow) after your app is approved.
4. Complete testing, verification, rollout, and monitoring during onboarding using the instructions provided by Google.

## Eligibility

To appear on Engage SDK surfaces, your app must meet the following eligibility
conditions:

- Be in good standing on Google Play and in compliance with all Play policies.
- Be downloaded or updated by the Play Store in at least one supported market (currently active in 140 countries; coverage varies by surface).
- Be in a supported app category: Media \& Entertainment, Books \& Reference, Comics \& Manga, News \& Magazines, Music \& Audio, Shopping, Food \& Drink, Social, Travel \& Local, Events, Health \& Fitness, and Education.
- Provide browseable content that can be consumed or ordered digitally.
- Not be primarily intended for an unsupported subcategory or use case, such as utilities, tools, and controls. For the full list, see the [Category and use case support](https://developer.android.com/guide/playcore/engage/eligibility#category-and-use-case-support) table.
- Meet one of the following scale criteria:
  - You are a developer in the [Media Experience Program](https://play.google.com/console/about/programs/mediaprogram/).
  - Your app has at least 100k 28-day DAU across supported markets.

Additionally:

- Pass manual verification confirming that your integration functions correctly and content meets required specifications (data quality, image specs, well-formed metadata, [Play policies](https://play.google/developer-content-policy/), refresh cadence, and valid deep links).
- After approval, your app may be re-verified at any time and must continuously meet these verification requirements.

> [!NOTE]
> **Note:** Eligibility and ongoing requirements are subject to change and may evolve based on user in-product feedback. Google reserves the right to remove any partner from Collections and other content surfaces if they don't meet these requirements.

## Personalization requirements

Engage SDK supports both personalized and non-personalized recommendations.
However, personalized content is mandatory to be shown on specific surfaces
(such as the Play Store **You** tab) and for
[Apps Experience Program (AEP) compliance](https://developer.android.com/distribute/aep/aep-req-engage-sdk), unless an
exemption applies.

### Surface-specific requirements

Select surfaces, like the **Play Store You tab** , require timely, personalized
content. To be included on these surfaces, apps must pass a stricter threshold
during verification. If your Engage SDK recommendations don't accurately reflect
user interests and actions, your app won't qualify for inclusion on the
**You tab**.

### AEP personalization requirements

To meet AEP guidelines, Engage SDK recommendations must be personalized by
developers, which typically means they reflect demonstrated user interests and
recent activity in your app in a timely manner. For more information about the
specific requirements and potential exemptions, see the
[AEP Engage SDK guideline](https://developer.android.com/distribute/aep/aep-req-engage-sdk).

While there are cases where apps may be exempt from this personalization
requirement for AEP, surfaces like the **You tab** still require timely, active
personalization.

### Evaluation

Because Engage SDK content remains on-device and isn't processed by Google,
Google doesn't inspect production user data to assess personalization quality.
Instead, a Google developer support team evaluates personalization during manual
verification using dedicated test accounts. Testers build a consistent interest
profile over several days to verify that Engage SDK recommendations accurately
reflect native app behavior.

## Apps Experience Program (AEP) requirements

Engage SDK integration is required for apps participating in Google Play's
**Apps Experience Program (AEP)** whose use cases fall within the scope of the
[AEP Engage SDK guideline](https://developer.android.com/distribute/aep/aep-req-engage-sdk), unless an exemption applies. AEP
enforces standards that go beyond basic Engage SDK eligibility
requirements---specifically, your recommendations must be personalized and update
frequently, your continuation content must reflect user activity in a timely
manner, and content must be published across all required form factors and
active regions.

You can review the specific requirements in the
[AEP Engage SDK guideline](https://developer.android.com/distribute/aep/aep-req-engage-sdk). To read more about the broader
program guidelines and the program rate card, see the
[Apps Experience Program guidelines overview](https://developer.android.com/distribute/aep/aep-guidelines-overview).

## Supported apps and surfaces

Engage SDK lets integrated app content appear across multiple Android-powered
device touchpoints and Google Play Store surfaces. The following tables outline
supported surfaces, country availability, eligible verticals, and
category-specific rules.

### Category and use case support

The following table outlines supported Engage SDK subcategories and use cases,
and highlights adjacent subcategories and use cases that aren't supported. Not
all supported subcategories are eligible to appear on every Engage SDK surface,
as each Engage SDK surface may enforce unique
[content policies](https://play.google/developer-content-policy/).

| Collections category | Supported use cases and subcategories | Unsupported use cases and subcategories *Apps won't be eligible if their primary use case falls into one of these unsupported categories* |
|---|---|---|
| **Social** | - Social networks - Image / memes - Video clips / short-form video - IRL meetups - Cloud photo storage | - Live Video Chat - Instant messaging, sharing online presence, or live real-time data (such as location or chat rooms) - File-sharing \& downloaders - Dating - Avatar generators |
| **Watch** | - Movies \& TV streaming - Live TV / Sports - On demand video clips - Sports videos - Drama Shorts | - Remote controls - Video downloaders, players, and editors - Movie \& TV reviews - Movie tickets - TV guides - Video calls \& chatrooms |
| **Read** | - eBooks - Comics - Audiobooks - UGC long-form reading content - Blogs - *News \& Magazines\* (Not eligible for Play Store)* | - eBook or PDF readers - Book reviews - Encyclopedia / Dictionary - Translator - Religious text |
| **Listen** | - Music streaming - Audiobooks - Podcast - Live radio | - MP3 player / library - Music maker - Audio recorder / converter / tool - Music recognition - Music education (supported in education) |
| **Shop** | - Clothes shopping - Online marketplace - Retailer - Food \& drink shopping / grocery - Discounts \& coupons - Pet / supplies - House \& home / Real estate | - Shopper app - B2B Shopping - Seller / merchant app - Receipts scanner rewards - Telecom service - Buy now pay later |
| **Food** | - Food / coffee / drink ordering or delivery - Restaurant / Food discovery, reviews, \& reservations - Meal subscriptions - Recipes | - Driver / deliverer app - Cooking tools / controls |
| **Travel** | - Travel \& local - Events - Pet activity, monitoring, sitting, walking | - Flight trackers |
| **Health \& Fitness** | - Fitness classes - Fitness routines - Relaxation \& meditation - Routes / trails discovery - Meal planning | - BMI calculator - Physical activity tracker / Step counter - Calorie counter - Sleep tracker - Tools / Remotes - Medical |
| **Education** | All education subcategories supported |   |

### Surface and country availability

The following table lists the supported markets, cluster types, and subcategory
exceptions for each Engage SDK surface:

| Surface | Supported markets and countries | Supported cluster types | Subcategory exceptions |
|---|---|---|---|
| Collections (Play-enabled Android phones and tablets) | **85 Countries** US, AU, BR, CA, FR, DE, IN, ID, IT, JP, MX, ES, GB, AR, AT, BH, BY, BE, BO, CL, CO, CR, CZ, DK, DO, EC, EG, SV, EE, FI, GR, GT, HN, HK, HU, IE, JO, KW, LV, LB, LT, LU, MY, NL, NZ, NI, NO, OM, PA, PY, PE, PH, PL, PT, QA, SA, SG, SK, KR, SE, CH, TH, TR, AE, BA, KH, HR, CY, IS, JM, MK, MT, MD, NP, PG, SI, LK, ZA, TW, UA, UY, VE, VN, AM, AW, HT | Continuation, Reorder, Carts, Lists, Recommendation, Featured, User Management | None (all eligible apps supported) |
| Entertainment Space (Select Android tablets) | **134 Countries** US, AU, BR, CA, FR, DE, IN, ID, IT, JP, MX, ES, GB, AR, AT, BH, BY, BE, BO, CL, CO, CR, CZ, DK, DO, EC, EG, SV, EE, FI, GR, GT, HN, HK, HU, IE, JO, KW, LV, LB, LT, LU, MY, NL, NZ, NI, NO, OM, PA, PY, PE, PH, PL, PT, QA, RU, SA, SG, SK, KR, SE, CH, TH, TR, AE, BA, KH, HR, CY, IS, JM, MK, MT, MD, NP, PG, SI, LK, KZ, RO, DZ, AZ, BD, BG, GH, IL, KE, LA, LI, NG, PK, SN, RS, ZA, TW, UA, UY, VE, VN, AM, AW, HT, KG, UZ, AL, AO, AG, BS, BZ, BJ, BW, BF, CM, CV, CI, FJ, GA, GW, MO, ML, MU, MZ, MM, NA, NE, RW, TJ, TZ, TG, TT, TM, UG, ZM, ZW | Recommendations | Only entertainment categories supported (Watch, Read, Listen) |
| **Play Store** Apps tab | **140 Countries** US, AU, BR, CA, FR, DE, IN, ID, IT, JP, MX, ES, GB, AR, AT, BH, BE, BO, CL, CO, CR, CZ, DK, DO, EC, EG, SV, EE, FI, GR, GT, HN, HK, HU, IE, JO, KW, LV, LB, LT, LU, MY, NL, NZ, NI, NO, OM, PA, PY, PE, PH, PL, PT, QA, SA, SG, SK, KR, SE, CH, TH, TR, AE, BA, KH, HR, CY, IS, JM, MK, MT, MD, NP, PG, SI, LK, KZ, RO, DZ, AZ, BD, BG, GE, GH, IQ, IL, KE, LA, LI, MA, NG, PK, SN, RS, TN, ZA, TW, UA, UY, VE, VN, AM, AW, HT, KG, UZ, AL, AO, AG, BS, BZ, BJ, BW, BF, CM, CV, CI, FJ, GA, GI, GW, MO, ML, MU, MC, MZ, MM, NA, NE, RW, SM, TJ, TZ, TG, TT, TM, UG, YE, ZM, ZW | Recommendation | News \& Magazines not supported (per [Play Premium Growth Tools](https://play.google.com/console/about/guides/premium-growth-tools/) criteria) |
| **Play Store** You tab | **140 Countries** US, AU, BR, CA, FR, DE, IN, ID, IT, JP, MX, ES, GB, AR, AT, BH, BE, BO, CL, CO, CR, CZ, DK, DO, EC, EG, SV, EE, FI, GR, GT, HN, HK, HU, IE, JO, KW, LV, LB, LT, LU, MY, NL, NZ, NI, NO, OM, PA, PY, PE, PH, PL, PT, QA, SA, SG, SK, KR, SE, CH, TH, TR, AE, BA, KH, HR, CY, IS, JM, MK, MT, MD, NP, PG, SI, LK, KZ, RO, DZ, AZ, BD, BG, GE, GH, IQ, IL, KE, LA, LI, MA, NG, PK, SN, RS, TN, ZA, TW, UA, UY, VE, VN, AM, AW, HT, KG, UZ, AL, AO, AG, BS, BZ, BJ, BW, BF, CM, CV, CI, FJ, GA, GI, GW, MO, ML, MU, MC, MZ, MM, NA, NE, RW, SM, TJ, TZ, TG, TT, TM, UG, YE, ZM, ZW | Continuation, Reorder, Carts, Lists, Recommendation | News \& Magazines not supported (per [Play Premium Growth Tools](https://play.google.com/console/about/guides/premium-growth-tools/) criteria) |
| **Play Store** store listing pages | **140 Countries** US, AU, BR, CA, FR, DE, IN, ID, IT, JP, MX, ES, GB, AR, AT, BH, BE, BO, CL, CO, CR, CZ, DK, DO, EC, EG, SV, EE, FI, GR, GT, HN, HK, HU, IE, JO, KW, LV, LB, LT, LU, MY, NL, NZ, NI, NO, OM, PA, PY, PE, PH, PL, PT, QA, SA, SG, SK, KR, SE, CH, TH, TR, AE, BA, KH, HR, CY, IS, JM, MK, MT, MD, NP, PG, SI, LK, KZ, RO, DZ, AZ, BD, BG, GE, GH, IQ, IL, KE, LA, LI, MA, NG, PK, SN, RS, TN, ZA, TW, UA, UY, VE, VN, AM, AW, HT, KG, UZ, AL, AO, AG, BS, BZ, BJ, BW, BF, CM, CV, CI, FJ, GA, GI, GW, MO, ML, MU, MC, MZ, MM, NA, NE, RW, SM, TJ, TZ, TG, TT, TM, UG, YE, ZM, ZW | Continuation, Reorder, Carts, Lists, Recommendation | News \& Magazines not supported (per [Play Premium Growth Tools](https://play.google.com/console/about/guides/premium-growth-tools/) criteria) |
| Google TV | All Google TV [markets](https://support.google.com/googletv/answer/10467234?ref_topic=10050480) | Continuation, Recommendations, Entitlements | Only apps with video content |