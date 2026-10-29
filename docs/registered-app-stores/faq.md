---
title: https://developer.android.com/registered-app-stores/faq
url: https://developer.android.com/registered-app-stores/faq
source: md.txt
---

This page answers common questions about the Registered App Stores program,
including eligibility, geographic availability, and technical specifications.

This resource will be updated to align the evolutions of the program.

## Program requirements

The following questions address eligibility and requirements for the Registered
App Stores program.

### Are individual developer accounts eligible to register an app store?

No, individual developer accounts are not eligible, per
[program requirements](https://developer.android.com/registered-app-stores/requirements). For organizational accountability, Registered App
Store registration is strictly restricted to verified Organization (Full
Distribution) accounts in Android Developer Console.

### What if my app store package name is already registered in my Play Console account?

If your app store package name is currently managed in a Play Console account,
you will need to create an [Android Developer Console](https://developer.android.com/developer-verification/guides/android-developer-console) organization account
and transfer that package name to your Android Developer Console account before
proceeding. A package name transfer requires both the source and target accounts
to be fully verified Organization accounts in good standing. Contact
[support](https://support.google.com/android-developer-console/contact/registered_app_store_enrollment_inquiries) to request the package name transfer.

### How does the Registered App Store program differ from the Third-Party App Store on Play program?

The Registered App Stores program provides OS-level platform capabilities, such
as one-tap installs, for verified stores operating on Android devices. In
contrast, Third-Party App Store on Play is a distinct Google Play program that
governs third-party stores distributed specifically within the Play Store
ecosystem, available in the US only.

## Geographic availability

The following questions address geographic availability for the Registered App
Store program.

### In which geographic regions is Registered App Store status available?

Starting December 1, 2026, Registered App Store status is available on Android
17 QPR2 and higher devices in the following regions:

<br />

View supported regions Albania, Algeria, Angola, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, The Bahamas, Bahrain, Bangladesh, Belarus, Belgium, Belize, Benin, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Bulgaria, Burkina Faso, Cambodia, Cameroon, Canada, Cape Verde, Chile, Colombia, Costa Rica, Côte d'Ivoire, Croatia, Cuba, Cyprus, Czech Republic, Denmark, Dominican Republic, Ecuador, Egypt, El Salvador, Estonia, Fiji, Finland, France, Gabon, Germany, Ghana, Greece, Guatemala, Guinea-Bissau, Haiti, Honduras, Hong Kong, Hungary, Iceland, India, Indonesia, Iran, Republic of Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Liechtenstein, Lithuania, Luxembourg, Macau, Republic of Macedonia, Malaysia, Mali, Malta, Mauritius, Mexico, Moldova, Morocco, Mozambique, Myanmar, Namibia, Nepal, Netherland Antilles, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, Norway, Oman, Pakistan, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russia, Rwanda, Saudi Arabia, Senegal, Serbia, Singapore, Slovakia, Slovenia, South Africa, South Korea, Spain, Sri Lanka, Sweden, Switzerland, Taiwan, Tajikistan, Tanzania, Thailand, Togo, Trinidad and Tobago, Tunisia, Turkey, Turkmenistan, Uganda, Ukraine, United Arab Emirates, United Kingdom, Uruguay, Uzbekistan, Venezuela, Vietnam, Yemen, Zambia, Zimbabwe

<br />

### What happens to automatic updates when a user travels abroad?

The end-user's home account country determines feature availability. Vacations
or short-term international travel to unsupported regions won't disrupt existing
one-tap installs or automatic updates.

### What happens if a user permanently relocates?

If a user updates their official home address and account country, the device
automatically adjusts feature availability to reflect the options supported in
their new country of residence.

## Technical and policy specifications

The following questions address technical and policy specifications for the
Registered App Stores program.

### Are stores required to use foreground services for installations?

Yes. To ensure user visibility and prevent the operating system from terminating
downloads, large downloads and background installations must execute using
foreground services with visible notifications.

### How does update ownership behave if a store is uninstalled and reinstalled?

If a store is uninstalled, its installed apps remain on the device but stop
receiving automatic updates. If the same store is reinstalled later, it
automatically reclaims update ownership for its original apps without requiring
new user prompts, provided no other store updated those apps in the interim.

### Can enterprise IT administrators restrict Registered App Stores on managed devices?

Yes. IT administrators can use administrative controls to block the installation
of Registered App Stores.

### Are all third-party app stores required to enroll in the Registered App Stores program in order to offer apps on Android devices?

Participation in the program is entirely optional. Third-party app stores may
continue to operate on Android as they do today without enrolling.

If you need additional support, submit your question through the [Support
Form](https://support.google.com/android-developer-console/contact/registered_app_store_enrollment_inquiries).