---
title: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/sign-in
url: https://developer.android.com/design/ui/wear/guides/m2-5/behaviors-and-patterns/sign-in
source: md.txt
---

# Sign-in

Keep in mind the following best practices when designing sign-in experiences.

## Use Credential Manager

Each of[Credential Manager's](https://developer.android.com/identity/sign-in/credential-manager)built-in authentication methods are fully standalone, requiring only the users watch and a data connection for authentication. No other authentication method can offer this benefit.

Use Credential Manager as the base of your authentication solution.

### Primary options: Credential Manager built-ins

Implement passkeys as the foremost option in Credential Manager to provide state-of-the-art security and simplicity to your users.

Implement the complete experience by adding passwords and Sign in With Google as well.  
![A users passkey as the preferred authentication solution on Wear OS](https://developer.android.com/static/wear/images/design/passkeys-sign-in.png)**Fig. 1a:**Passkeys![Passkeys, passwords, and Sign in With Google are all available for a user to authenticate with](https://developer.android.com/static/wear/images/design/passkey-password-gsi-options.png)**Fig. 1b:**Passkeys, passwords, \& Sign in with Google

### Secondary options

Offer at least one secondary option to handle users dismissing Credential Manager. Provide at least two distinct sign-in options in total.

Apps without multiple sign-in methods create a difficult user experience. For example, an app that offers only a "Sign in on phone" option fails if the user's phone is not nearby.  
![A user taps dismiss to navigate to backup authentication methods](https://developer.android.com/static/wear/images/design/dismiss-passkeys.png)**Fig. 2a:**Tap 'Dismiss' for backups![Backup authentication options for Credential Manager](https://developer.android.com/static/wear/images/design/secondary-sign-in-screen.png)**Fig. 2b:**Backup authentication

**Special Case:** [Automatic data layer authentication](https://developer.android.com/training/wearables/apps/auth-wear#tokens)is the only secondary option which is acceptable to precede Credential Manager in your UX. This comes with several important caveats:

1. You must offer at least one other authentication method beyond this because it works only on paired watches with a corresponding mobile app installed.
2. You must fully automate the token exchange for the user, and you must not present any UI to the user beforehand. In other words, you should make the authentication process fully automatic from the user's perspective.
3. If this method fails, either the user is not logged in on a paired phone, or there is no paired phone to begin with. Don't alert the user there was a failed attempt, instead navigate directly to Credential Manager.

### Prompt users correctly

**For apps requiring sign-in for all functionality:**Immediately present Credential Manager as the first screen to a signed-out user, without any preceding UI.

**For apps offering functionality without sign-in:**Delay presenting Credential Manager until necessary. Provide as many features as possible without requiring sign-in. When authentication becomes essential, display a 'sign in' button to launch Credential Manager. If sign-in fails, offer the option to skip authentication.
![Sign in immediately if needed for full functionality](https://developer.android.com/static/wear/images/design/sign-in-flow-chart.png)

## Authentication best practices

### Explain sign-in benefits

For apps that delay user sign-in until it becomes essential, clearly explain the benefits of signing in. Use the surrounding UI context to articulate the value to the user; don't assume they understand why signing in is beneficial.

Never refer to Credential Manager by name in your UI.  
![](https://developer.android.com/static/wear/images/design/deferred-sign-in-bezel.png)  
check_circle

### Do

Provide context by asking for sign-in after the user initiates an action.  
![](https://developer.android.com/static/wear/images/design/sign-in-no-explanation.png)  
cancel

### Don't

Display sign-in without explaining why sign-in is beneficial.

### Streamline

Streamline the authentication process by:

1. Using Credential Manager
2. Reducing the number of steps needed in secondary sign in options
3. Keeping users signed in for as long as possible (within your privacy and security requirements)

![](https://developer.android.com/static/wear/images/design/passkeys-sign-in.png)  
check_circle

### Do

Use Credential manager  
![](https://developer.android.com/static/wear/images/design/secondary-sign-in-screen.png)  
check_circle

### Do

Display all secondary options together.  
![](https://developer.android.com/static/wear/images/design/running-app-homescreen.png)  
check_circle

### Do

Stay signed in

### Sign-in status and confirmations

When using secondary, non-Credential Manager options, display a message that alerts the user that they are being signed in the first time the app is opened, then display a confirmation message upon successful sign-in.  
![](https://developer.android.com/static/wear/images/design/signing-in-state.png)  
check_circle

### Do

Tell user they're being signed in.  
![](https://developer.android.com/static/wear/images/design/signed-in-confirmation.png)  
check_circle

### Do

Show a confirmation.

## Other Resources

To learn how to implement Credential Manager on Wear, see our[developer guide](https://developer.android.com/training/wearables/apps/auth-wear)and our[public sample](https://github.com/android/identity-samples/tree/credman-compose/Shrine).