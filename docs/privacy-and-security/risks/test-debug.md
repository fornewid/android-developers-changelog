---
title: https://developer.android.com/privacy-and-security/risks/test-debug
url: https://developer.android.com/privacy-and-security/risks/test-debug
source: md.txt
---

# Test and debug features

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

Releasing production builds that include Testing or Debug features can negatively impact the security posture of the application. These functionalities are used to help developers discover and identify bugs within intended application use cases prior to, or after a new version release, and shouldn't be publicly accessible.

Examples of Testing/ Debug features are:

- Hidden menus
- Options to enable debug logs
- Options to alter application flow
- Options to circumvent payment or subscription processes
- Options to circumvent authentication
- Tests for application-specific activities

All the preceding can be leveraged by a malicious user in order to alter the application's intended flow or retrieve system information to tailor further attacks.

The risk introduced by leaving exposed Testing or Debug features may vary according to the action associated with the debug capabilities itself.

Another area of risk for the application is the attribute**android:debuggable** set within the AndroidManifest.xml element**`<application>`** . As reported in the[**android:debuggable**](https://developer.android.com/topic/security/risks/android-debuggable)article, deploying a production application with the aforementioned value set, allows malicious users to access administrative resources that are otherwise inaccessible.

## Impact

A malicious user interacting with a Testing or Debug feature in a production build can lead to unexpected results. The impact of any action is directly connected with the permissions assigned to the feature. The higher the permissions, the higher the impact that an active exploitation can have. Such functionalities within an application can be used to circumvent a number of protections, bypass paywalls, retrieve system or user related information, or trigger testing activities.

## Mitigations

### Avoid using debug components

Test or debug functionalities should never be implemented within production application components such as activities, broadcast receivers, services or content providers since, if exported, can be run by any other process on the device. Setting the debug component as not exported ([**android:exported="false"**](https://developer.android.com/topic/security/risks/android-exported)) does not constitute a valid protection for the capabilities since any rooted device can still execute it through the Android Debug Bridge (ADB) tool if the debug option is enabled.

### Limit debug or test features to staging builds

The execution of any test or debug function within applications should be limited only to a restricted set of Staging builds to allow only developers to debug or test application's features in a controlled environment. This can be obtained by creating a dedicated test or debug build of the application and advanced instrumented tests for it in order to ensure that any test or debug feature is run on an isolated version.

### Implement automated UI tests

When running tests on an application, opt for automated UI tests since they are repeatable, can be executed in a separated environment and are not prone to human errors.

## Resources

- [Dev guidance on advanced testing setups](https://developer.android.com/studio/test/advanced-test-setup)
- [Dev guidance on automating UI tests](https://developer.android.com/training/testing/instrumented-tests/ui-tests)
- [android:debuggable](https://developer.android.com/topic/security/risks/android-debuggable)
- [android:exported](https://developer.android.com/topic/security/risks/android-exported)
- [Debuggable Apps in Android Market](https://labs.withsecure.com/publications/debuggable-apps-in-android-market)
- [Can debug code cause security vulnerabilities?](https://www.coderskitchen.com/an-debug-code-cause-security-vulnerabilities/)