---
title: https://developer.android.com/work/dpc/rcs-messages-archival
url: https://developer.android.com/work/dpc/rcs-messages-archival
source: md.txt
---

# RCS Google Messages archival

## Background

This document outlines how to integrate with, test, and validate the RCS archival feature in Google Messages.

### Solution overview

- **Client-side archival:**Archival vendors need to develop an Android app for IT admins to deploy on their managed devices.
- **Powered by Google Messages:** This feature requires Google Messages to be the[default messaging app](https://support.google.com/messages/answer/6089066). IT admins can use Android Enterprise controls to enforce the default.
- **Requires Android Enterprise:**This feature is available only on fully managed devices.

| **Important:** Work profiles (on neither personally-owned nor company-owned devices) are not supported.

### Workflow

![Workflow for RCS messaging archival](https://developer.android.com/static/images/work/workflow-rcs-archival-1.png)**Figure 1.**RCS archival workflow.

1. IT admin deploys archival app using Android Enterprise.
2. **Optional** : IT admin programmatically configures archival app using Android Enterprise controls.
   - Required:
     - The archival app needs[`READ_SMS`](https://developer.android.com/reference/android/Manifest.permission#READ_SMS)permission
   - Recommended:
     - [Disallow user control](https://developer.android.com/reference/android/app/admin/DevicePolicyManager#setUserControlDisabledPackages(android.content.ComponentName,%20java.util.List%3Cjava.lang.String%3E))over Google Messages and archival app
     - IT admin[enforces](https://developer.android.com/reference/android/os/UserManager?_gl=1*wrcrs6*_up*MQ..*_ga*MTgxMTgzNzc3NC4xNzM4NjY5MDMy*_ga_6HH9YJMN9M*MTczODY2OTAzMS4xLjAuMTczODY2OTAzMS4wLjAuMTQ0OTczNTMyMg..#DISALLOW_CONFIG_DEFAULT_APPS)Google Messages as the default SMS/RCS client
     - Optionally, IT admin can pre-enroll archival app using MCM as well, if archival solution supports MCM
3. IT admin enables archival in Google Messages using[MCM](https://developer.android.com/work/dpc/rcs-messages-archival#google-messages-mcm-schema).
4. Google Messages writes message data to Android on message events. A message event is one of: message sent, message received, message edited, or message deleted.
5. Google Messages[notifies archival app](https://developer.android.com/work/dpc/rcs-messages-archival#notification-to-archival-app)of new message event, for both RCS and SMS/MMS messages.
6. The archival app reads the message data from the[`Telephony`](https://developer.android.com/reference/android/provider/Telephony)provider.
7. The archival app batches updates and sends them to the server.

## Implementation

### Google Messages MCM schema

Archival is configured in Google Messages using the`messages_archival`key, which accepts a string value for admins to specify their archival app by package name. If the value is empty, null, or the key is not present, archival is disabled. If the value is specified, archival is enabled, and Google Messages sends an explicit broadcast to the specified package name on a message event.

### Notification to archival app

- An explicit broadcast is sent to the specified archial app, with the action:`GOOGLE_MESSAGES_ARCHIVAL_UPDATE`
- In some cases, the message URI is included in the broadcast extras, which can be used to fetch the message that triggered the broadcast:`com.google.android.apps.messaging.EXTRA_ARCHIVAL_URI`

### Archival app requirements

**Required:**

- Claim the[FOREGROUND_SERVICE permission](https://developer.android.com/reference/android/Manifest.permission?_gl=1*ir8law*_up*MQ..*_ga*NDcyNDIyNTk3LjE3NDAzOTEzODM.*_ga_6HH9YJMN9M*MTc0MDM5MTM4My4xLjAuMTc0MDM5MTM4My4wLjAuMTM5NTk3NjU1Nw..#FOREGROUND_SERVICE).
- Declare a foreground service in your manifest, which includes the intent filter for the archival update broadcast, and is[permission-granted](https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components#permission-based-access-control-to-exported-components-mitigations)to assure only Google Messages can start the service.

    <service
            android:enabled="true"
            android:foregroundServiceType="shortService"
            android:name=".TestService"
            android:exported="true"
            android:permission="android.permission.WRITE_SMS">
          <intent-filter>
            <action android:name="GOOGLE_MESSAGES_ARCHIVAL_UPDATE" />
          </intent-filter>
    </service>

- Implement that service to handle the intent, read from telephony, and determine the type of the message event by comparing the prior state of telephony with the current state, and then cache both the message event to be uploaded to the archival service backend, and the updated state of Telephony to compare against on the next event.

**Recommended:**

- Batch updates of message events to the server with[`JobScheduler`](https://developer.android.com/reference/android/app/job/JobScheduler).

  | **Important:** Don't attempt to sync every message event with your backend in your service.
  - IT admins can guarantee your app isn't killed or your app data deleted by users, making sure your batched updates can proceed as expected.
  - Minimizing foreground service time to just the critical archival requirement minimizes UX and system health impact.
- Enable programmatic configuration of your app using MCM (as mentioned in[Messages MCM schema](https://developer.android.com/work/dpc/rcs-messages-archival#google-messages-mcm-schema)), so users don't need to sign in or specify server enrollment details manually.

## Testing

To test your implementation, use[TestDPC](https://github.com/googlesamples/android-testdpc)or your preferred EMM client.