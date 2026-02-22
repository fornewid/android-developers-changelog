---
title: https://developer.android.com/security/fraud-prevention/authentication
url: https://developer.android.com/security/fraud-prevention/authentication
source: md.txt
---

# Secure user authentication

To protect your authentication system in Android, consider moving away from a password-based model, especially for sensitive accounts like your users' bank and email accounts. Remember that some apps your users install may not have the best intentions and may try to phish your users.

Also, don't assume that only authorized users will use the device. Phone theft is a common problem, and attackers target unlocked devices to profit directly from user data or financial apps. We suggest all sensitive apps implement a reasonable authentication timeout (15 minutes?) with biometric verification and require additional authentication before sensitive actions such as money transfers.

## Biometric authentication dialog

The Biometrics library offers a set of functions to display a prompt requesting biometric authentication such as face recognition or fingerprint recognition. However, biometric prompts can be configured to fall back to LSKF, which has[known shoulder-surfing risks](https://youtu.be/QUYODQB_2wQ). For sensitive apps, we recommend not having biometric fall back to PIN, and after exhausting biometric retries, users can wait, or re-login with password or reset accounts. Account reset should require factors that are not easily accessible on device (best practice below).

### How this helps mitigate fraud and phone theft

One particular use case that can be helpful to prevent fraud is to request biometric authentication within your app before a transaction. When your users want to make a financial transaction, the biometric dialog shows in order to verify that it is indeed the intended user who is making the transaction. This best practice would protect against an attacker stealing a device regardless of the attacker knowing or not the LSKF, as they will need to probe that they are the owner of the device.

For additional levels of security, we recommend app developers request Class 3 Biometric Authentication and utilize[`CryptoObject`](https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt.CryptoObject)for banking and financial transactions.

### Implementation

1. Make sure you include the androidx.biometric library.
2. Include the biometric login dialog in the activity or fragment which holds the logic you want the user to be authenticated.

### Kotlin

```kotlin
private var executor: Executor? = null
private var biometricPrompt: BiometricPrompt? = null
private var promptInfo: BiometricPrompt.PromptInfo? = null

fun onCreate(savedInstanceState: Bundle?) {
  super.onCreate(savedInstanceState)
  setContentView(R.layout.activity_login)
  executor = ContextCompat.getMainExecutor(this)
  biometricPrompt = BiometricPrompt(this@MainActivity,
    executor, object : AuthenticationCallback() {
      fun onAuthenticationError(
        errorCode: Int,
        @NonNull errString: CharSequence
      ) {
        super.onAuthenticationError(errorCode, errString)
        Toast.makeText(
          getApplicationContext(),
          "Authentication error: $errString", Toast.LENGTH_SHORT
        )
          .show()
      }

      fun onAuthenticationSucceeded(
        @NonNull result: BiometricPrompt.AuthenticationResult?
      ) {
        super.onAuthenticationSucceeded(result)
        Toast.makeText(
          getApplicationContext(),
          "Authentication succeeded!", Toast.LENGTH_SHORT
        ).show()
      }

      fun onAuthenticationFailed() {
        super.onAuthenticationFailed()
        Toast.makeText(
          getApplicationContext(), "Authentication failed",
          Toast.LENGTH_SHORT
        )
          .show()
      }
    })
  promptInfo = Builder()
    .setTitle("Biometric login for my app")
    .setSubtitle("Log in using your biometric credential")
    .setNegativeButtonText("Use account password")
    .build()

  // Prompt appears when user clicks "Log in".
  // Consider integrating with the keystore to unlock cryptographic operations,
  // if needed by your app.
  val biometricLoginButton: Button = findViewById(R.id.biometric_login)
  biometricLoginButton.setOnClickListener { view ->
    biometricPrompt.authenticate(
      promptInfo
    )
  }
}
```

### Java

```java
private Executor executor;
private BiometricPrompt biometricPrompt;
private BiometricPrompt.PromptInfo promptInfo;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_login);
    executor = ContextCompat.getMainExecutor(this);
    biometricPrompt = new BiometricPrompt(MainActivity.this,
            executor, new BiometricPrompt.AuthenticationCallback() {
        @Override
        public void onAuthenticationError(int errorCode,
                @NonNull CharSequence errString) {
            super.onAuthenticationError(errorCode, errString);
            Toast.makeText(getApplicationContext(),
                "Authentication error: " + errString, Toast.LENGTH_SHORT)
                .show();
        }

        @Override
        public void onAuthenticationSucceeded(
                @NonNull BiometricPrompt.AuthenticationResult result) {
            super.onAuthenticationSucceeded(result);
            Toast.makeText(getApplicationContext(),
                "Authentication succeeded!", Toast.LENGTH_SHORT).show();
        }

        @Override
        public void onAuthenticationFailed() {
            super.onAuthenticationFailed();
            Toast.makeText(getApplicationContext(), "Authentication failed",
                Toast.LENGTH_SHORT)
                .show();
        }
    });

    promptInfo = new BiometricPrompt.PromptInfo.Builder()
            .setTitle("Biometric login for my app")
            .setSubtitle("Log in using your biometric credential")
            .setNegativeButtonText("Use account password")
            .build();

    // Prompt appears when the user clicks "Log in".
    // Consider integrating with the keystore to unlock cryptographic operations,
    // if needed by your app.
    Button biometricLoginButton = findViewById(R.id.biometric_login);
    biometricLoginButton.setOnClickListener(view -> {
            biometricPrompt.authenticate(promptInfo);
    });
}
```

### Best practices

We recommend you start with the[codelab](https://developer.android.com/codelabs/biometric-login)to know more about biometrics.

Depending on your use cases you can implement the dialog with or without explicit user action. In order to avoid fraud we recommend you add the biometric dialog with explicit user action for every transaction. We understand that adding authentication can introduce friction in the UX, but due to the nature of the information being handled in a bank transaction and that biometric authentication is smoother than other authentication methods, we think it is necessary to add this level of navigation.

[Learn more about biometric authentication](https://developer.android.com/training/sign-in/biometric-auth).

## Passkeys

Passkeys are a safer and easier alternative to passwords. Passkeys use public-key cryptography to enable your users to sign into apps and websites using their device's screen lock mechanism, such as a fingerprint or face recognition. This frees the user from having to remember and manage passwords, and provides significantly improved security.

Passkeys can meet multifactor authentication requirements in a single step, replacing both a password and OTP codes to deliver robust protection against phishing attacks and avoid the user experience pain of SMS or app-based one-time passwords. Since passkeys are standardized, a single implementation enables a passwordless experience across all of the users' devices, browsers, and operating systems.

On Android, passkeys are supported using the[Credential Manager](https://developer.android.com/jetpack/androidx/releases/credentials)Jetpack library that unifies the major authentication methods, including passkeys, passwords, and federated sign in (such as Sign in with Google).

### How this helps mitigate fraud

Passkeys shield you from phishing attacks because they only function on your registered apps and websites.

A passkey's core component is a cryptographic private key. Typically, this private key resides solely on your devices, such as laptops or mobile phones, and is synchronized across them by credential providers (also known as password managers), such as Google Password Manager. Only the corresponding public key is saved by the online service when a passkey is created. During login, the service uses the private key to sign a challenge from the public key. This can only originate from one of your devices. Additionally, for this to occur, you must unlock your device or credential store, which prevents unauthorized sign-ins (for example, from a stolen phone).

To prevent unauthorized access in the event of a stolen, unlocked device, passkeys must be coupled with a sensible authentication timeout window. An attacker who steals a device shouldn't be able to use an application just because the previous user had been logged in. Instead, the credentials should expire at regular intervals (such as, every 15 minutes), and users should be required to verify their identity through screen lock reauthentication.

If your phone is stolen, passkeys protect you because thieves can't steal your passwords to use on other devices -- passkeys are device-specific. If you use Google Password Manager and your phone gets stolen, you can log into your Google Account from another device (like a computer) and remotely log out from the stolen phone. This makes the Google Password Manager on the stolen phone unusable, including any saved passkeys.

In a worst case scenario, if the stolen device is not recovered, passkeys are synced back to the new device by the credential provider that created and synced the passkey. For example, the user may have chosen Google Password Manager to create the passkey, and they can access their passkey on a new device by signing back into their Google Account and providing the screen lock from the previous device.

Learn more in the[Security of Passkeys in the Google Password Manager](https://security.googleblog.com/2022/10/SecurityofPasskeysintheGooglePasswordManager.html)article.

### Implementation

Passkeys are supported on devices that run Android 9 (API level 28) or higher. Passwords and Sign in with Google are supported starting with Android 4.4. To get started with passkeys, follow these steps:

1. Follow the[Credential Manager codelab](https://codelabs.developers.google.com/credential-manager-api-for-android#0)to get an initial understanding of how to implement passkeys.
2. Review the[passkeys user experience design guidelines](https://developer.android.com/design/ui/mobile/guides/patterns/passkeys). This document shows you what flows are recommended for your use case.
3. Study the Credential Manager by following the[guide](https://developer.android.com/training/sign-in/passkeys).
4. Plan your Credential Manager and passkeys implementation for your app. Plan adding support for[Digital Asset Links](https://developer.android.com/training/sign-in/passkeys#add-support-dal).

See our developer documentation for more details on how to create, register, and authenticate with passkeys.

## Secure account reset

An unauthorized attacker with access to an unlocked device (such as when a phone is snatched) will try to access sensitive apps, especially banking or cash apps. If the app implements biometric verification, the attacker would try to reset the account to get in. It is essential for account reset flow to not solely rely on information that is easily accessible on device, such as email or SMS OTP reset links.

Here are common best practices that you can incorporate into your app's reset flow:

- Facial recognition, in addition to OTP
- Security questions
- Knowledge factor (such as a mother's maiden name, city of birth, or favorite song)
- ID verification

## SMS Retriever API

The SMS Retriever API let's you perform SMS-based user verification in your Android app automatically. In that way the user won't need to be required to manually type verification codes. Additionally, this API doesn't ask the user for extra, potentially dangerous app permissions like`RECEIVE_SMS`or`READ_SMS`. However, SMS should not be used as the only user verification to protect against unauthorized local access to the device.

#### How this helps mitigate fraud

Some users use SMS codes as their only authentication factor which provides an easy entrypoint for fraud.

The SMS Retriever API allows the app to directly retrieve the SMS code without user interaction, and can provide a level of protection against fraud.

### Implementation

There are two parts to implementing the SMS Retriever API: Android, and Server.

**Android** : ([guide](https://developers.google.com/identity/sms-retriever/request))

1. Obtain the user's phone number.
2. Start the SMS retriever client.
3. Send the phone number to your server.
4. Receive verification messages.
5. Send the OTP to your server.

**Server** : ([guide](https://developers.google.com/identity/sms-retriever/verify))

1. Construct a verification message.
2. Send the verification message by SMS.
3. Verify the OTP when it's returned.

### Best practices

Once the app is integrated and the user's phone number is being verified with the SMS Retriever API, it tries to get the OTP. If it succeeds, that is a strong signal that the SMS was received on the device automatically. If it does not succeed and the user needs to manually type the OTP, it can be a warning sign that the user may be experiencing fraud.

SMS shouldn't be used as the only user verification mechanism as it leaves room to local attacks, such as an attacker who robs an unlocked device; or SIM cloning attacks. It is recommended using Biometrics whenever possible. On devices where Biometric sensors are not available, user authentication should rely on at least one factor that is not easily obtained from the current device.
| **Note:** This API does not protect against all threat vectors, such as SIM cloning.

## Learn more

For further reading on best practices check out the following resources:

- [Our Android documentation on Security](https://developer.android.com/security)
- [Play Integrity API documentation](http://g.co/play/integrityapi)
- [Android 15 Changes](http://goo.gle/android-15-changes)
- [Best Practices for Scam Call Prevention from Monzo Bank](https://android-developers.googleblog.com/2024/03/battling-impersonation-scams-monzo-innovative-approach.html)