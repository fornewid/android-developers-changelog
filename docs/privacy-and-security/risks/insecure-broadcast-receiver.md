---
title: https://developer.android.com/privacy-and-security/risks/insecure-broadcast-receiver
url: https://developer.android.com/privacy-and-security/risks/insecure-broadcast-receiver
source: md.txt
---

# Insecure broadcast receivers

<br />

**OWASP category:** [MASVS-PLATFORM: Platform Interaction](https://mas.owasp.org/MASVS/09-MASVS-PLATFORM)

## Overview

Improperly implemented broadcast receivers can allow an attacker to send a malicious intent to make the vulnerable application perform actions which are not intended for external callers.

The vulnerability generally refers to instances where the broadcast receiver is unintentionally exported, either by setting[`android:exported="true"`](https://developer.android.com/guide/topics/manifest/receiver-element#exported)in the AndroidManifest or by creating a broadcast receiver programmatically which makes the receiver public by default. If the receiver doesn't contain any intent filters the default value is`"false"`but if the receiver contains at least one intent filter the default value of android:exported is`"true"`.

Intentionally exported broadcast receivers without proper access control can be abused if the developer did not intend for it to be called by all applications.

## Impact

Insecurely implemented broadcast receivers can be abused by an attacker to gain unauthorized access to execute behavior in the application that the developer did not mean to expose to third parties.

## Mitigations

### Avoid the problem entirely

To resolve the dilemma entirely, set`exported`to`false`:  

    <receiver android:name=".MyReceiver" android:exported="false">
        <intent-filter>
            <action android:name="com.example.myapp.MY_ACTION" />
        </intent-filter>
    </receiver>

### Use calls and callbacks

In the case you used broadcast receivers for internal app purposes (ie. event completion notification), you can restructure your code to pass a callback that would fire after event completion instead.

###### Event completion listener

### Kotlin

    interface EventCompletionListener {
        fun onEventComplete(data: String)
    }

### Java

    public interface EventCompletionListener {
        public void onEventComplete(String data);
    }

###### Secure task

### Kotlin

    class SecureTask(private val listener: EventCompletionListener?) {
        fun executeTask() {
            // Do some work...

            // Notify that the event is complete
            listener?.onEventComplete("Some secure data")
        }
    }

### Java

    public class SecureTask {

        final private EventCompletionListener listener;

        public SecureTask(EventCompletionListener listener) {
            this.listener = listener;
        }

        public void executeTask() {
            // Do some work...

            // Notify that the event is complete
            if (listener != null) {
                listener.onEventComplete("Some secure data");
            }
        }
    }

###### Main activity

### Kotlin

    class MainActivity : AppCompatActivity(), EventCompletionListener {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)

            val secureTask = SecureTask(this)
            secureTask.executeTask()
        }

        override fun onEventComplete(data: String) {
            // Handle event completion securely
            // ...
        }
    }

### Java

    public class MainActivity extends AppCompatActivity implements EventCompletionListener {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            SecureTask secureTask = new SecureTask(this);
            secureTask.executeTask();
        }

        @Override
        public void onEventComplete(String data) {
            // Handle event completion securely
            // ...
        }
    }

### Secure broadcast receivers with permissions

Only register dynamic receivers for[protected broadcasts](https://developer.android.com/about/versions/12/reference/broadcast-intents-31)(broadcasts that only system level applications can send) or with[self-declared signature level permissions](https://developer.android.com/guide/topics/manifest/permission-element#plevel).

## Resources

- [Exported Receiver Elements](https://developer.android.com/guide/topics/manifest/receiver-element#exported)
- [Broadcast Receiver Permissions documentation](https://developer.android.com/guide/components/broadcasts#receiving-broadcasts-permissions)
- [Protected Broadcast Intents](https://developer.android.com/about/versions/12/reference/broadcast-intents-31)