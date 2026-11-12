---
title: https://developer.android.com/games/test-rewards
url: https://developer.android.com/games/test-rewards
source: md.txt
---

Play Billing Lab is a companion app that helps you test integrations with the
Google Play billing system. You can use Play Billing Lab's out-of-app purchase
(OOAP) testing feature to validate that your app and backend are properly
configured to handle items acquired outside of your app, including
[Play Games Rewards](https://developer.android.com/games/rewards.md.txt).

With the OOAP testing feature, you can select a Play Games Reward offer,
simulate Google Play granting the reward to the user directly from Play Billing
Lab, and verify the end-to-end entitlement acquisition and fulfillment flow.

## Prerequisites

Before using Play Billing Lab to test out-of-app purchase (OOAP) flows to
validate your setup for Play Games Rewards, ensure that you meet the following
requirements:

1. **Licensed tester status:** Your test account must be registered as a
   licensed tester for the game. For details, see
   [Google Play licensed tester documentation](https://support.google.com/googleplay/android-developer/answer/6062777).

   **Note:** While any user can view the Play Billing Lab app, only licensed
   testers can configure and trigger OOAP overrides.
2. **Account consistency across surfaces:** You must sign in to Play Billing
   Lab and the Google Play Store using the same licensed tester account. If
   there is an account mismatch, the Play Store might not surface the
   overridden test product or offer, or complete the test purchase.

## Download and install

You can download and install the [Play Billing Lab app](https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion) from Google Play.

## Step-by-step integration and testing guide

The following steps detail how to integrate and test Play Games Rewards using
Play Billing Lab. For general information on testing out-of-app purchases, see
[Test out-of-app purchases](https://developer.android.com/google/play/billing/test.md.txt#out-of-app).

### Step 1: Launch Play Billing Lab and sign in

When you open Play Billing Lab for the first time after installation:

- Tap **Sign-in with Google**.
- Select the Google Account registered as the licensed tester for your app.
- After signing in, you see the main **Dashboard**.

![Play Billing Lab Dashboard](https://developer.android.com/static/images/games/rewards/rewards1.png) Play Billing Lab Dashboard.

### Step 2: Navigate to out-of-app purchases (OOAP) testing

- On the **Dashboard** , locate the **Out-of-app purchases** card.
- Tap **Test** to open the OOAP configuration setup screen.

> [!NOTE]
> **Note:** If your account is not a licensed tester for the app, this card doesn't appear, and the system prevents you from initiating an OOAP test.

### Step 3: Specify app package name and product ID

> [!NOTE]
> **Note:** [Play Games Rewards](https://developer.android.com/games/rewards.md.txt) are supported only for one-time products.

On the OOAP setup screen, enter the required app identifiers:

1. **Package name:** The exact Android package name of your app (for example, `com.example.app`).
2. **Product type:** Use the drop-down menu to select **One-time product** (in-app item).
3. **Product ID (SKU):** The product ID of the one-time product that has the Play Games Reward offer you want to test.

![Specify app package name and product ID](https://developer.android.com/static/images/games/rewards/rewards2.png) Specify app package name and product ID.

### Step 4: Select the Play Games Reward offer

After you enter the package name, product ID, and product type, Play Billing
Lab queries the backend and displays a list of available offers for that
product.

> [!CAUTION]
> **Caution:** Only offers currently eligible for your specific tester account are displayed and selectable. For non-consumable items, you must not currently own the product. For consumable items, you must consume any existing purchases before you test.

- Select the **Play Games Reward** offer that you want to test.

  ![Select an eligible offer](https://developer.android.com/static/images/games/rewards/rewards3.png) Select an eligible offer.

### Step 5: Start the OOAP test

After selecting the Play Games Reward offer, tap **Start test**. The
configuration is saved and synced with Google Play backend servers.

After activation, your **Dashboard** displays an **Active** badge on the
**Out-of-app purchases** card, showing the configured package name, product ID
(SKU), and remaining duration.

- **Testing window:** Active OOAP test configurations remain active for 2
  hours by default before expiring automatically. After this time, you must
  reconfigure the test.

  ![Start the OOAP test](https://developer.android.com/static/images/games/rewards/rewards4.png) Start the OOAP test.

### Step 6: Grant the reward and verify delivery

While the OOAP test is active for your Play Games Reward offer, you can grant
the reward directly from Play Billing Lab without purchasing it from the Google
Play Store:

1. **Grant the reward:** On the **Out of app purchase** screen in Play Billing
   Lab, click **Grant Reward** to simulate Google Play granting the reward to
   the user. Existing rewards must be [processed](https://developer.android.com/google/play/billing/integrate.md.txt#process) before additional rewards
   can be granted.

   ![Three screens showing the Play Games Rewards testing flow. On
   the first screen the user selects to grant the reward. The second
   screen shows the reward being successfully granted by Play, then the
   user clicks for the reward to be granted again. The third screen
   shows an error state because the first reward hasn't been properly
   processed.](https://developer.android.com/static/images/google/play/billing/play-billing-lab-games-rewards-testing.png) Play Games Rewards testing flow.
2. **Handle and deliver the entitlement:** Your app should detect the
   out-of-app purchase (for example, by calling `queryPurchasesAsync` when the
   game starts or is foregrounded) and then deliver the item to the respective
   user. For the full process, see [processing purchases](https://developer.android.com/google/play/billing/integrate.md.txt#process).

### Step 7: Stop and clear the OOAP test

After you finish testing:

1. Go to **Out-of-app purchases** page.
2. Tap **Clear test** to stop the OOAP test and clear the OOAP test settings.

![Stop and clear the OOAP test](https://developer.android.com/static/images/games/rewards/rewards6.png) Clear the OOAP test.

## Modifying Test Configurations

You cannot change the package name, product ID, offer selection, or change the
Play Store Country override while an OOAP test is actively running.

Doing so requires stopping and clearing the current OOAP test.

### How to edit product or offer

If you are currently running an OOAP test and want to test a different product
or offer:

1. Open Play Billing Lab and tap **View** on the active **Out-of-app
   purchases** card.
2. Tap **Edit** to modify the package name, product ID or testing offer.
3. Confirm **Stop test** when prompted. The test will be stopped and all relevant inputs will be cleared.
4. Enter your new product or select the new offer, and restart the test.

![Edit product or offer](https://developer.android.com/static/images/games/rewards/rewards7.png) Edit product or offer.

### How to test regional configurations with country overrides

Play Billing Lab lets you override your Google Play Store country to test
offer eligibility across different regions. If you don't select a country, Play
Billing Lab uses the Play Country for your licensed test account. Country
changes must be synchronized with OOAP testing:

1. **Stop Active OOAP Test:** If you attempt to edit your country override
   while an OOAP test is active, either from the Dashboard or Out of app
   purchase page, Play Billing Lab will display a warning prompting you to
   stop the test first. Confirming by tapping **Stop test**
   will stop the current OOAP test and clear the test inputs.

2. **Set Country Override:** After stopping the OOAP test, you can edit your
   country setting in the **Configuration Settings** page (or tap **Set country
   override** on the **Out of app purchase** screen). Select the target country
   (for example, Japan, United Kingdom) and tap **Apply**.

3. **Restart OOAP Test:** Once the country override is active, return to the
   **Out-of-app purchases** card, select your product and offer, and tap
   **Start test**.

   Your dashboard will now show both an active Country Override and an active
   OOAP Test.

![Test regional configurations with country overrides](https://developer.android.com/static/images/games/rewards/rewards8.png) Test regional configurations with country overrides.

## Troubleshooting and frequently asked questions

#### Why can't I select or see any offers when setting up a product in Play Billing Lab?

- **Offer eligibility:** Play Billing Lab only displays offers that your specific tester account is currently eligible to acquire. For non-consumable items, you must not currently own the product. For consumable items, you must consume any existing purchases before you test.
- **Licensed tester status:** Verify that your account is listed as an active licensed tester in Play Console.

#### Why can't I grant another reward in Play Billing Lab?

- **Unprocessed reward:** Existing rewards must be [processed](https://developer.android.com/google/play/billing/integrate.md.txt#process) (acknowledged or consumed) before additional rewards can be granted. Open your game and verify that the previous reward has been processed.
- **Expiration:** Active OOAP tests expire after 2 hours. Open Play Billing Lab to check if your test tag has changed to **Expired**. If so, start a new test.

#### Why wasn't my granted reward delivered in the game?

- **Account consistency:** Verify that the account signed in to Play Billing Lab, the Google Play Store app, and your game is the exact same licensed tester account.
- **Out-of-app purchase handling:** Check your game's `queryPurchasesAsync` implementation and purchase processing logic. Because rewards are granted outside your app's standard UI, your game or backend server must detect unacknowledged purchases and process them.

#### How do I stop or clear an active test before the 2-hour timer expires?

- Open Play Billing Lab, locate the active card (**Out-of-app purchases** or **Configuration settings** ), and tap **Stop** or **Delete** (or tap **Clear test** on the **Out of app purchase** screen). When prompted, confirm your choice. The override is immediately removed from Google Play servers.