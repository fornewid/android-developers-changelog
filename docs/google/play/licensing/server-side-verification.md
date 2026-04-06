---
title: https://developer.android.com/google/play/licensing/server-side-verification
url: https://developer.android.com/google/play/licensing/server-side-verification
source: md.txt
---

# Adding Server-Side License Verification to Your App

When verifying that the user has purchased or downloaded a legitimate copy of your app from the Google Play Store, it's best to perform the license verification check on a server that you control.

This guide presents a step-by-step process for completing server-side license verification and presents some best practices related to performing this check.

## Process overview

Figure 1 shows how information is transferred between your app, Google Play, and your private server:  
![Data flow diagram](https://developer.android.com/static/images/google/play/licensing/server-side-data-flow.svg)**Figure 1.**Flow of data between your app and Google Play, then between your app and your private server

1. Your app makes a request to Google Play, inquiring about whether a particular user has purchased or downloaded a legitimate copy of your app.
2. Google Play responds by sending a*response data object* , an object of type[`ResponseData`](https://developer.android.com/google/play/licensing/licensing-reference#lvl-summary), to your app. This object is a signed piece of information that states whether the user has purchased or downloaded a legitimate copy of your app.
3. Your app makes a request to a private server that you control, verifying the contents of the response data.
4. The server responds by sending a status to your app, indicating whether the user has indeed purchased or downloaded a legitimate copy of your app. If the server provides a "success" message,[verify the response](https://developer.android.com/google/play/licensing/server-side-verification#verify-app-server-response)and then grant the user access to the resources that require a license.

Because the response data is signed by Google Play, then checked on your server, there's no way to modify the object on the device running your app. If your app relies on the server and makes resources available only to legitimate users, your app is substantially more protected against unauthorized users.

The following sections provide additional considerations to keep in mind when performing server-side license verification.

## Safeguard against replay attacks

After receiving a response from Google Play regarding the user's license status, it's possible for the user to copy the response data and use it multiple times, or give it to other users who could then forge their own requests to your app's private server. This sort of action is known as a*replay attack*.

To reduce the likelihood of users performing replay attacks successfully, take the following measures before sending a request to your app's server:

- Check the timestamp that's included in the response data, making sure that Google Play generated the response recently.

  | **Note:** You can increase the allowed difference between the response data's timestamp and the current time based on how long users should be able to interact with license-bound resources after they deactivate their license.
- Perform rate-limiting on your server request, such as exponential backoff, to reduce the number of times that your app attempts to send the same response data to your app's server.

  | **Caution:** To preserve a good user experience in cases where a user interacts with your app on a variety of devices, be careful if you add rate-limiting based on number of devices.
- Before verifying the contents of Google Play's response data on your private server, make an initial, authentication-based request to your private server. In this first request, send user credentials to your server, and have your server then respond with a*nonce* , or a number that is used only once. You can then include this nonce in your next request to your private server, asking for license verification data. For details on how to choose a good value for the nonce, see the[generate a suitable nonce value](https://developer.android.com/google/play/licensing/server-side-verification#generate-nonce)section.

  | **Note:** Include a user ID field in both the nonce request and the license verification request. Your app's server can then compare the fields' values from the two requests and make sure they match.

### Generate a suitable nonce value

Use one of the following techniques to create a nonce value that's difficult to guess:

- Generate a hash value based on the user's ID.
- Generate a random value on a per-user basis. Store this random value on your app's server as part of a given user's attributes.

## Verify response data from your server

When reviewing response data that your app's server sends to your app, make sure that the License Verification Library response isn't forged. Verify the signature that's included in the app server's response data by comparing it with the key that your app received from Google Play in a previous step.

It's also worth remembering that the block specific to the License Verification Library (LVL) is the only part that's signed. Therefore, it's the only part of your app server's response data that your app should trust.