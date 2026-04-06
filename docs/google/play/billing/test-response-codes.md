---
title: https://developer.android.com/google/play/billing/test-response-codes
url: https://developer.android.com/google/play/billing/test-response-codes
source: md.txt
---

The Play Billing Library returns a [`BillingResult`](https://developer.android.com/reference/com/android/billingclient/api/BillingResult) response to let you
know the outcome of an action that was triggered. For more
information, see [handling `BillingResult` response codes](https://developer.android.com/google/play/billing/errors). Before you
deploy your app to the production environment, you can test your app's various
response flows by using the Response Simulator.

## Response Simulator

When you integrate your app with the Play Billing Library, it can be difficult
to test all of the [`BillingResponseCode`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode) flows, because you don't have much
control over the communication between the Play Store and Play's backend.
The Response Simulator feature in the [Play Billing Lab](https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion) app lets you
configure error code responses for the Play Billing Library to test various complex
error scenarios.

### Enable billing overrides testing for the Play Billing Library

| **Note:** Before testing, ensure that your app is using [Play Billing Library](https://developer.android.com/google/play/billing/integrate#dependency) version 7.1.1 or later.

To enable communication between the Response Simulator and your app,
you must enable billing overrides testing for the Play Billing Library
from within your app. To do this, add the following metadata tags to your app's
`AndroidManifest.xml` file.

```scdoc
<manifest ... >
  <application ... >
    ...
     <meta-data
      android:name="com.google.android.play.largest_release_audience.NONPRODUCTION"
      android:value="" />
    <meta-data
      android:name="com.google.android.play.billingclient.enableBillingOverridesTesting"
      android:value="true" />
  </application>
</manifest>
```
| **Note:** Even though adding only the `enableBillingOverridesTesting` tag and setting it to `true` is sufficient to enable billing overrides testing for your app, it's recommended that you also add the `NONPRODUCTION` tag. The `NONPRODUCTION` tag prevents accidental deployment of your app to the production environment with billing overrides testing enabled.

When you deploy your app to the production environment, you should either
use a separate `AndroidManifest.xml` file that doesn't include these
metadata tags or ensure that you've removed these tags from the
`AndroidManifest.xml` file.

### Simulate Play Billing Library errors

To simulate Play Billing Library errors, first, configure the response codes
in the [Play Billing Lab](https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion) app, and then test your app.

#### Configure a response code

1. In the Play Billing Lab app, sign in with a [license tester](https://developer.android.com/google/play/billing/test#license-testers) account for your app.
   This displays the Play Billing Lab **Dashboard** including
   the **Response Simulator** card.

   ![Dashboard with Response Simulator card](https://developer.android.com/static/images/google/play/billing/play-billing-lab-dashboard-response-simulator.png) **Figure 1.** Response Simulator card.
2. Click **Manage** on the Response Simulator card.
   This shows the **Response Simulator** screen.

3. When prompted, allow notifications from Play Billing Lab to see the connection status of your app.

4. Enable the **Simulate Play Billing Library responses** switch, if it isn't
   already enabled.

   ![Simulate Play Billing Library responses switch](https://developer.android.com/static/images/google/play/billing/play-billing-lab-response-simulator.png) **Figure 2.** Simulate Play Billing Library responses switch.
5. Select a response code for the Play Billing Library APIs that you want
   to test.
   Your selections are automatically saved, and the Response Simulator
   is ready to send the selected response codes to your app.

#### Test your app's error handling

| **Note:** When testing using the Response Simulator, ensure that you first open Play Billing Lab, and then open your app. Opening your app before opening Play Billing Lab may result in issues connecting to the Response Simulator.

1. Open your app.

   - If you have allowed notifications from Play Billing Lab, you will see the Play Billing Lab notification icon in your device's status bar which indicates a successful connection to the Response Simulator.

   ![Play Billing Lab notification icon in status bar](https://developer.android.com/static/images/google/play/billing/play-billing-lab-response-simulator-notification.png) **Figure 3.** Play Billing Lab icon indicating successful connection.
2. Trigger the Play Billing Library API method you want to test. For example,
   if you want to test the `launchBillingFlow`, initiate an in-app purchase
   flow.