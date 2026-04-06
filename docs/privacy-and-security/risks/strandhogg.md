---
title: https://developer.android.com/privacy-and-security/risks/strandhogg
url: https://developer.android.com/privacy-and-security/risks/strandhogg
source: md.txt
---

# StrandHogg Attack / Task Affinity Vulnerability

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

The StrandHogg attack / Task Affinity vulnerability was enabled / caused by a design bug in the way Android handled multiple tasks, specifically the feature called task reparenting. Application task reparenting is a feature that allows an application to move an activity from one task to another.

The StrandHogg attack exploits a lack of clarity on how to vet incoming application task stack activities and allows a malicious application to either:

- move a malicious activity to or from a victim stack
- set the malicious activity as the return stack upon completion of a victim activity

This vulnerability is exploited by manipulating the`allowTaskReparenting`and`taskAffinity`settings.

## Impact

A malicious application can set the taskAffinity of one of its activities to match the packageName of a target application. This can then be coupled with intent hijacking so that the next time the target application is launched by the user, the malicious application is also launched and displayed on top of the target application.

The Task Affinity vulnerability can then be used to hijack legitimate user actions.

The user could be tricked into providing credentials to a malicious application. By default, once an activity starts and is associated with a task, that association persists for the activity's entire lifecycle. However, setting allowTaskReparenting to true breaks this restriction, allowing an existing activity to be re-parented to a newly created "native" task.

For example, App A can be targeted by App B, redirecting App A activities to an App B activity stack upon return from App A's completed activity. This transition from one app to another is hidden from the user and creates a significant phishing threat.

## Mitigations

Update to`android:minSdkVersion="30"`.

The StrandHogg attack / Task affinity vulnerability was originally patched in March 2019 with a newer and more comprehensive variant patched in September 2020. Android SDK versions 30 and newer (Android 11) contain the appropriate OS patches to avoid this vulnerability. While it is possible to partially mitigate version 1 of the StrandHogg attack through individual application configuration, version 2 of the attack can only be prevented by this SDK version patch.

## Resources

- [Original academic paper describing the vulnerability at Usenix 15](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-ren-chuangang.pdf){.external}
- [Promon Security group's expansion of the original vulnerability](https://promon.co/security-news/the-strandhogg-vulnerability/){.external}
- [Android developer documentation for android:allowTaskReparenting](https://developer.android.com/guide/topics/manifest/activity-element#reparent)
- [Android developer documentation for android:taskAffinity](https://developer.android.com/guide/topics/manifest/activity-element#aff)
- [Android developer documentation for the application element of android:allowTaskReparenting](https://developer.android.com/guide/topics/manifest/application-element#reparent)