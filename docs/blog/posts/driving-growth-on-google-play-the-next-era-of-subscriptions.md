---
title: https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions
url: https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Driving growth on Google Play: The next era of subscriptions

4 min read ![](https://developer.android.com/static/blog/assets/ABL_0137_Strapi_1331188d3a_Z17ea85.webp) 29 Sep 2026 [![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp)](https://developer.android.com/blog/authors/sheenam-mittal) [Sheenam Mittal](https://developer.android.com/blog/authors/sheenam-mittal) Senior Product Manager, Google Play The subscription landscape is evolving rapidly, especially with the surge of generative AI and increasingly sophisticated app experiences. As the ecosystem shifts, we recognize that developers need more flexible and robust tools to monetize effectively while improving the LTV of recurring purchases. On Google Play, we are continuously expanding our subscription platform to help you drive growth, adapt to new business models, and meet your users exactly where they are.

Here is a look at the capabilities we are testing and rolling out to support the next generation of subscriptions, along with powerful existing features designed to maximize your conversion and retention.

## Unlock new ways to sell and grow with flexible monetization models

As we look at the next few years of the subscription business, flexibility is paramount. Developers building GenAI tools, entertainment, educational platforms, and business solutions need adaptable pricing and packaging models to scale access beyond the individual user and capture higher cart value at checkout.

### Multi-Quantity Subscriptions: Scale subscriptions to teams

To support collaborative and team-wide or group usage, Play is introducing **Multi-Quantity Subscription Purchase**. This allows users to make multiple subscription purchases in a single transaction and easily assign those as seats or subscriptions to team members or students. This is a game-changer for productivity, EdTech, and GenAI developers looking to sell team-wide subscription access seamlessly.

### Usage-Based Billing: Support AI and variable-cost features

For apps with variable computing costs---like AI generation tools or other usage-based services---rigid recurring subscriptions do not always fit. **Usage-Based Billing** enables you to set up prepaid metered billing where users can automatically top up their balance whenever it falls below a set threshold. This ensures uninterrupted service for your users while protecting your margins.

**Beyond these flexible models, we are also making it easier to package your products and upsell creatively at checkout:**

### Mixed Carts: Sell subscriptions and one-time products in a single checkout

Historically, subscriptions and one-time products were purchased in separate transactions. If a user wanted to buy a monthly membership alongside a starter pack of in-app currency or bonus credits, they had to complete two separate checkout flows.

**Mixed Carts** bridges this gap for developers who want to sell both auto-renewing subscriptions and one-time products (OTPs). By enabling you to process an auto-renewing base subscription alongside OTPs in a single API call and unified checkout sheet, Mixed Carts streamlines the transaction process.

This unified experience also opens up powerful upsell opportunities for your business---such as offering targeted discounts if an end user purchases a complete bundle of a subscription and complementary in-app items together.

### Cross-Developer Bundling: Partner across apps to unlock shared growth

Partnerships are a proven strategy for acquiring new users and driving growth. With **Cross-Developer Bundling**, you can create and sell a hard bundle of two or more complementary subscriptions in your own catalog.

This capability allows you to team up with other developers---or combine offerings across your own portfolio of apps---to deliver massive value through a single purchase. For example, if you manage a language learning app, you can now create a single SKU that bundles your monthly membership with a partner's premium travel guide subscription, offering users a combined subscription at a discounted rate.

By sharing the acquisition benefits, you can seamlessly reach new audiences and secure more recurring revenue for your business.

## Maximize subscription performance: Keep and win back the users you've earned

Acquiring a subscriber is only the first step---long-term growth depends on minimizing friction across the billing lifecycle. We are heavily invested in improving subscription performance to help you prevent involuntary payment declines and retain your subscribers.
![Placeholder2.png](https://developer.android.com/static/blog/assets/Placeholder2_5693af8378_15pjSC.webp)

### The In-App Messaging API: Resolve payment declines and price change updates in-context

Available now to all developers, we highly encourage adopting the **In-App Messaging API**. This tool allows you to meet end users exactly where they are---inside your app---with critical transactional messages. You can use this API to:

- Prompt users to fix a payment decline immediately.
- Notify users of upcoming price changes transparently.

By handling these critical account states gracefully within the app experience, you can continue running your business without disrupting the user journey. [Learn more](https://developer.android.com/google/play/billing/subscriptions#in-app-messaging).

### Dynamic Grace Period: Tailor payment recovery windows with predictive models

![Placeholder3.png](https://developer.android.com/static/blog/assets/Placeholder3_0f64e7eb42_Z22xTLi.webp)

Involuntary churn from payment declines is often addressed with a static, one-size-fits-all grace period. However, fixed durations force a difficult trade-off between giving users enough time to resolve payment issues and managing developer service costs during unpaid periods. With **Dynamic Grace Period**, Google Play utilizes machine learning and heuristic models to tailor the grace period duration for individual subscribers following a payment decline. By intelligently matching the recovery window to the user's recovery likelihood, this capability is designed to help developers better balance renewal recovery against unpaid service access. To ensure consistency with your business rules, Google Play automatically adjusts the subsequent account hold duration, preserving your total configured recovery window without requiring client-side code changes.

### Retention Offers and Plan Change: Prevent voluntary churn in the cancellation flow

Acquiring new subscribers is expensive, making it critical to engage and retain your existing user base. When users consider canceling, capturing their attention before they leave is essential for protecting your customer lifetime value. With **Retention Offers**, you can present developer-funded incentives---like a discount---directly within the Play Store cancellation flow.

For users who may not be eligible for a discount or promotional offer, you can suggest a **Plan Change** to a lower-priced tier, ensuring you offer a flexible path to keep them engaged in your app rather than losing them entirely.

### Native Winback Offers: Re-engage lapsed subscribers directly on the Play Store

A canceled subscription doesn't have to be the end of the user lifecycle. Former subscribers already understand the value of your app---they often just need the right incentive at the perfect moment to return. Traditional winback campaigns rely on email or push notifications, which fall flat if a user has uninstalled your app. Google Play's **Subscription Winback Offers** close this gap in your re-acquisition strategy by reaching users directly on the Google Play Store, helping you present lapsed users with personalized offers that make coming back easier than ever.

## Behind the scenes: The revenue shield you don't have to build

Alongside the tools you configure in Play Console, Google Play runs a continuous engine of zero-lift optimizations behind the scenes to grow your subscriber base and reduce involuntary churn---without requiring a single line of developer code. From smart payment retries and automatically cycling through backup payment methods for opted-in users, to sending intelligent, context-aware reminders during grace periods and account hold, Play works continuously to recover failed transactions seamlessly.

We also protect your revenue with built-in fraud and abuse prevention systems that block bad actors from exploiting promotional offers or manipulating billing cycles. This ensures your promotional budgets reward legitimate, high-value subscribers---securing your business while naturally lifting overall retention.

Many of these features are currently available or rolling out through our Early Access Program, meaning capabilities are in active testing with select partners to gather feedback before rolling out more broadly in Play Console. If you work with a Google Play partner manager, you can reach out to express interest as programs open. To learn more about our current subscription capabilities and get your app ready for what's next, [explore our Google Play Billing subscriptions documentation](https://developer.android.com/google/play/billing/subscriptions).
- [#Google Play subscriptions](https://developer.android.com/blog/topics/google-play-subscriptions)
Written by:

-

  ## [Sheenam Mittal](https://developer.android.com/blog/authors/sheenam-mittal)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/sheenam-mittal) ![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp) ![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp)
Continue reading
- [![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)](https://developer.android.com/blog/authors/simona-milanovic) 02 Oct 2026 02 Oct 2026 ![](https://developer.android.com/static/blog/assets/ABL_135_Android_CLI_and_Android_skills_Strapi_d22702426a_ZIUXgH.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Device Streaming and Android skills - available in Android CLI](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills) As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build.
  [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) • 4 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 24 Sep 2026 24 Sep 2026 ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build your way: Use any AI agent of your choice in Android Studio](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio) Last year, Android Studio opened up to any AI model. Today, we're taking the next step by introducing support for your choice of coding agents.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)