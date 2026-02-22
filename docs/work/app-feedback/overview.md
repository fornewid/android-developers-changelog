---
title: https://developer.android.com/work/app-feedback/overview
url: https://developer.android.com/work/app-feedback/overview
source: md.txt
---

# Send app feedback to EMMs

Enterprise mobility management (EMM) providers offer solutions for organizations to manage Android devices and the apps installed on them. These solutions are typically available as web consoles, called*EMM consoles*. Using an EMM console, IT admins perform device and app management tasks on behalf of their organization.

Apps targeting enterprise organizations can send feedback to EMMs in the form of keyed app states. APIs are available for EMMs to retrieve keyed app state data, which they can then display in their EMM console. This communication channel allows IT admins to receive feedback about the status of the apps installed on the devices they manage.

For example, an email client app could use keyed app states to confirm that an account was successfully configured, report when sync errors occur, or send any other status updates the app developer thinks is appropriate.

### Components of a keyed app state

A keyed app state is comprised of the following:

- **Key:**Unique identifier for the app state. Maximum 100 characters.
- **Message:**Optional message describing the app state. Maximum 1000 characters. Note: Typically messages should be significantly shorter than this.
- **Data:** Optional machine-readable value intended for EMMs to allow IT admins to set up alerts or filters based on the value. For example, an IT admin could set up an alert if the data field`battery_percentage < 10`. Maximum 1000 characters.
- **Severity:** The severity of the app state. Allowable values are[`SEVERITY_ERROR`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_ERROR)and[`SEVERITY_INFO`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_INFO)(default). Only set severity to[`SEVERITY_ERROR`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_ERROR)for genuine error conditions that an organization needs to take action to fix.
- **Timestamp:**When a keyed app state is set, it's automatically sent with a timestamp in milliseconds since epoch.

## Send managed configurations feedback

If your app supports[managed configurations](https://developer.android.com/work/managed-configurations), sending keyed app states is recommended as a way to update IT admins on the status of the configurations they set. The following example workflow describes one way to do this.
![keyed app states for managed configurations](https://developer.android.com/static/images/work/keyed-app-state.svg)

1. IT admins use their EMM console to set and send managed configurations for an app installed on a[fully managed device](https://developers.google.com/android/work/terminology#fully_managed_device)or inside a[work profile](https://developers.google.com/android/work/terminology#work_profile). For example:
   - Volume: '50%'
   - Currency: 'USDD'
2. The app attempts to apply the configurations. The volume is set successfully to 50%, but the currency code is invalid and can't be applied.
3. Based on the status of each configuration, the app sets a keyed app state. Each keyed app state contains a unique key and a message with details of the state. We recommend matching the managed configurations key where possible. For example:

   |    Key     |            Message             |                                                       Severity                                                        |  Timestamp   |
   |------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------|
   | `volume`   | Set to 50%                     | [`SEVERITY_INFO`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_INFO)   | `1554461130` |
   | `currency` | Currency 'USDD' not recognized | [`SEVERITY_ERROR`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_ERROR) | `1554461130` |

4. The EMM provider retrieves the keyed app states set by the app and displays them in its EMM console. For example:

   | Configuration |                 Status                 | Action required |            Time            |
   |---------------|----------------------------------------|-----------------|----------------------------|
   | Volume        | Set to 50%                             | No              | April 5, 2019; 10:45:30 AM |
   | Currency      | ERROR: Currency 'USDD' not recognized. | Yes             | April 5, 2019; 10:45:30 AM |

   The EMM provider should also explicitly flag any received states with[`SEVERITY_ERROR`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_ERROR)to the IT admin. IT admins can view the information in their EMM console and take action to rectify any errors in the configurations they set.

### Report resolved errors

After an error is resolved, immediately send a follow-up app state to prevent EMMs from displaying the error message indefinitely. This follow-up state should include:

- The same[key](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#getKey())as the initial error message.
- A severity of[`SEVERITY_INFO`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_INFO), which indicates that the state isn't in an error condition and doesn't require the organization to take any further action.

## Add support for keyed app states to your app

The steps below describe how to integrate keyed app states in your app.

### Step 1: Add Google's Maven repository to your`settings.gradle`file

Add Google's Maven repository as a repository location in your project's[`settings.gradle`](https://developer.android.com/studio/build#settings-file)file, as shown below:  

```
dependencyResolutionManagement {
  repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
  repositories {
       google()
  }
}
```

### Step 2: Add the enterprise feedback library to your module-level`build.gradle`file

Add the following dependency to your module-level[`build.gradle`](https://developer.android.com/studio/build#module-level)file:  

```
dependencies {
    implementation 'androidx.enterprise:enterprise-feedback:1.0.0'
}
```

### Step 3: Get an instance of`KeyedAppStatesReporter`

In your`onCreate()`method, get and store an instance of[`KeyedAppStatesReporter`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppStatesReporter). This enables a communication channel between your app and EMM providers.  

### Kotlin

```kotlin
val reporter = KeyedAppStatesReporter.create(context)
```

### Java

```java
KeyedAppStatesReporter reporter = KeyedAppStatesReporter.create(context);
```

### Step 4: Create a collection of keyed app states

Follow the best practices outlined below when creating keyed app states:

- Never include personally identifiable information (PII) in a state---keyed apps states aren't suitable for sensitive data.
- Keep keyed app states within the limits defined in[`MAX_KEY_LENGTH`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#MAX_KEY_LENGTH),[`MAX_MESSAGE_LENGTH`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#MAX_MESSAGE_LENGTH), and[`MAX_DATA_LENGTH`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#MAX_DATA_LENGTH).
- A single`setStates`or`setStatesImmediate`call is limited to 300 KB total (approximately 1/3 of the total that can be stored per day). Exceeding this will result in undefined behavior.
- Only set the severity of a state to[`SEVERITY_ERROR`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_ERROR)if a condition exists that an organization needs to take action to fix.
- When sending an app state containing errors, ensure that you also send a follow-up state when the errors are resolved so the EMM can stop flagging the errors in their console.
- For the follow-up state, use the same[key](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#getKey())as the initial state that returned the error and set severity to[`SEVERITY_INFO`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppState#SEVERITY_INFO).

The snippet below creates a collection of keyed app states:  

### Kotlin

```kotlin
    val states = hashSetOf(KeyedAppState.builder()
             .setKey("key")
             .setSeverity(KeyedAppState.SEVERITY_INFO)
             .setMessage("message")
             .setData("data")
             .build())
    
```

### Java

```java
    Collection states = new HashSet<>();
    states.add(KeyedAppState.builder()
     .setKey("key")
     .setSeverity(KeyedAppState.SEVERITY_INFO)
     .setMessage("message")
     .setData("data")
     .build());
    
```

### Step 5: Set the keyed app states

| **Note:**You can set up to 500 unique keys per day for your app. There's no limit to the number of states you can set for each unique key.

The[`setStates()`](https://developer.android.com/reference/androidx/enterprise/feedback/KeyedAppStatesReporter#setStates(java.util.Collection<androidx.enterprise.feedback.KeyedAppState>))method immediately sends keyed app states to the Play Store app (package name:`com.android.vending`) if it's installed on the device, as well as any admins of the device or work profile.  

### Kotlin

```kotlin
keyedAppStatesReporter.setStates(states)
```

### Java

```java
keyedAppStatesReporter.setStates(states);
```

## Test keyed app states

For detailed test instructions, see[Test app feedback](https://developer.android.com/work/app-feedback/testing).