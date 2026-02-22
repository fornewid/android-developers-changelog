---
title: https://developer.android.com/security/fraud-prevention
url: https://developer.android.com/security/fraud-prevention
source: md.txt
---

# Fraud Prevention &nbsp;|&nbsp; Android Developers

![](http://developer.android.com/static/images/security/fraud-prevention/fraud.svg)  

### Protect users from fraud

In security, no solution or tactic can completely prevent fraud and theft. When a device is stolen, users are in a time race against attackers who will attempt to abuse their apps and extract their personal data before the device is remotely locked.

Are your users at risk for fraud? Can you mitigate phone theft abuse?

## Essential app security questions to consider

[![](http://developer.android.com/static/images/spot-icons/permissions.svg)](http://developer.android.com/security/fraud-prevention/environment)  

### [Is the app execution environment trustworthy?](http://developer.android.com/security/fraud-prevention/environment)

Ensure that the device can be cryptographically verified. Verify that your published app is authentic and has not been tampered with. Investigate if the device has settings or applications that increase risk. Examine if there is a risk of other apps on the device controlling your app? Make sure your server is able to verify the authenticity and integrity of the request it has received.  
[Learn more](http://developer.android.com/security/fraud-prevention/environment)[![](http://developer.android.com/static/images/spot-icons/handle-data.svg)](http://developer.android.com/security/fraud-prevention/activities)  

### [Is sensitive content protected?](http://developer.android.com/security/fraud-prevention/activities)

Ensure that the user's sensitive operations are not exposed or monitored by untrusted apps. Avoid including sensitive content in notifications that can be displayed over a locked screen. Design password reset mechanisms to be resilient against local attacks. Implement measures to prevent unauthorized account resets and data access by individuals with physical access to the user's device.  
[Learn more](http://developer.android.com/security/fraud-prevention/activities)[![](http://developer.android.com/static/images/spot-icons/engagement.svg)](http://developer.android.com/security/fraud-prevention/authentication)  

### [Is this the expected user, and user behavior?](http://developer.android.com/security/fraud-prevention/authentication)

Implement robust authentication mechanisms to ensure the user currently logged in is the legitimate owner of the account. Educate users about phishing attacks and how to identify and avoid them. Employ device security measures to prevent unauthorized access and usage. Require explicit user confirmation for critical actions to mitigate the risk of unauthorized operations.

Financial apps are a top target for fraud because the transactions are valuable and easy to carry out. In case of phone theft, financial apps provide a valuable target to attackers looking to monetize their theft. This document provides an overview of the tools and resources available to help you identify, address, and mitigate phone theft and fraud. It is organized around the different products, APIs, code examples, and best practices we recommend for app developers to mitigate financial fraud in their apps.  
[Learn more](http://developer.android.com/security/fraud-prevention/authentication)

## User protections

![](http://developer.android.com/static/images/security/fraud-prevention/gppShield.png)  

## Play protect

Play Protect now recommends a real-time app scan when installing apps that haven't been scanned before.  
![](http://developer.android.com/static/images/security/fraud-prevention/play-protect.png)![](http://developer.android.com/static/images/picto-icons/kotlin-friendly-sdk.svg)  

## Safe screen sharing

As of Android 15, Screen Sharing now defaults to sharing just a single app. Users can adjust this setting to share their whole screen, if needed.

During screen sharing, the developer-provided public version of the notifications will display, or a private version which has notification content removed.  
![](http://developer.android.com/static/images/security/fraud-prevention/safe-screen-sharing.png)![](http://developer.android.com/static/images/picto-icons/private-by-design.svg)  

## Smart masking of confidential data

Apps that post notifications with one-time passwords and login screens will also be hidden from remote viewers during screen share.

Starting with Android 15, most apps with the notification listener service will receive notifications with one-time password content removed.  
![](http://developer.android.com/static/images/security/fraud-prevention/smart-masking.png)![](http://developer.android.com/static/images/picto-icons/private-by-design.svg)  

## Theft protections

Finally, Android 15 offers new device theft protections including grab protection and remote quick lock.

Grab protection locks the screen when someone has grabbed or taken away a user's phone. Remote quick lock enables a user to easily lock their device remotely, even if they don't remember their Google password.  
![](http://developer.android.com/static/images/security/fraud-prevention/theft-protections.png)

## Learn more

For further reading on best practices check out the following resources.  
[![](http://developer.android.com/static/images/picto-icons/security.svg)](http://developer.android.com/privacy-and-security/security-tips)  

### [Android documentation on security](http://developer.android.com/privacy-and-security/security-tips)

Secure by default and private by design, learn Android's security best practices. Design, implement, and distribute safe, secure, and private apps.  
[Read more](http://developer.android.com/privacy-and-security/security-tips)  
[![](http://developer.android.com/static/images/logos/google-play.svg)](http://developer.android.com/google/play/integrity)  

### [Play integrity documentation](http://developer.android.com/google/play/integrity)

The Play Integrity API helps to safeguard apps against fraud and abuse. Verify that your app's interactions stem from authorized devices and apps.  
[Read more](http://developer.android.com/google/play/integrity)[![](http://developer.android.com/static/images/logos/android.svg)](http://developer.android.com/about/versions/15/behavior-changes-15)  

### [Android 15 changes](http://developer.android.com/about/versions/15/behavior-changes-15)

Changes include restricting background activity launches, making intents more secure, and protecting users from malicious apps that try to modify Do Not Disturb state.  
[Read more](http://developer.android.com/about/versions/15/behavior-changes-15)  
[![](http://developer.android.com/static/images/picto-icons/chat-bubbles.svg)](https://android-developers.googleblog.com/2024/03/battling-impersonation-scams-monzo-innovative-approach.html)  

### [Best practices for scam call prevention from Monzo](https://android-developers.googleblog.com/2024/03/battling-impersonation-scams-monzo-innovative-approach.html)

Monzo combats impersonation scams with new call status feature to verify real representatives.  
[Read more](https://android-developers.googleblog.com/2024/03/battling-impersonation-scams-monzo-innovative-approach.html)