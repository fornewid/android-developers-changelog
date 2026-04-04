---
title: Redirect a call  |  Connectivity  |  Android Developers
url: https://developer.android.com/develop/connectivity/telecom/dialer-app/redirect-a-call
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [Connectivity](https://developer.android.com/develop/connectivity)
* [Guides](https://developer.android.com/develop/connectivity/overview)

# Redirect a call Stay organized with collections Save and categorize content based on your preferences.



Devices that run Android 10 or higher manage call intents differently than
devices that run Android 9 or lower. On Android 10 and higher, the
[`ACTION_NEW_OUTGOING_CALL`](/reference/android/content/Intent#ACTION_NEW_OUTGOING_CALL)
broadcast is deprecated and replaced with the
[`CallRedirectionService`](/reference/android/telecom/CallRedirectionService)
API. The `CallRedirectionService` provides interfaces for you to use to
modify outgoing calls made by the Android platform. For example, third-party
apps might cancel calls and reroute them over VoIP.

### Kotlin

```
class RedirectionService : CallRedirectionService() {
    override fun onPlaceCall(
        handle: Uri,
        initialPhoneAccount: PhoneAccountHandle,
        allowInteractiveResponse: Boolean
    ) {
        // Determine if the call should proceed, be redirected, or cancelled.
        val callShouldProceed = true
        val callShouldRedirect = false
        when {
            callShouldProceed -> {
                placeCallUnmodified()
            }
            callShouldRedirect -> {
                // Update the URI to point to a different phone number or modify the
                // PhoneAccountHandle and redirect.
                redirectCall(handle, initialPhoneAccount, true)
            }
            else -> {
                cancelCall()
            }
        }
    }
}
```

### Java

```
class RedirectionService extends CallRedirectionService {
    @Override
    public void onPlaceCall(
            @NonNull Uri handle,
            @NonNull PhoneAccountHandle initialPhoneAccount,
            boolean allowInteractiveResponse
    ) {
        // Determine if the call should proceed, be redirected, or cancelled.
        // Your app should implement this logic to determine the redirection.
        boolean callShouldProceed = true;
        boolean callShouldRedirect = false;
        if (callShouldProceed) {
            placeCallUnmodified();
        } else if (callShouldRedirect) {
            // Update the URI to point to a different phone number or modify the
            // PhoneAccountHandle and redirect.
            redirectCall(handle, initialPhoneAccount, true);
        } else {
            cancelCall();
        }
    }
}
```

You must register this service in the manifest so the system can start it
correctly.

```
<service
    android:name=".RedirectionService"
    android:permission="android.permission.BIND_CALL_REDIRECTION_SERVICE">
    <intent-filter>
        <action android:name="android.telecom.CallRedirectionService"/>
    </intent-filter>
</service>
```

To use a redirection service, your app must request the call redirection role
from the [`RoleManager`](/reference/android/app/role/RoleManager). This will ask
the user if they want to allow your app to handle call redirects. If your app
isn't granted this role, your redirection service isn't used.

You should check if your app has this role when the user launches your app so
you can request it as needed. You launch an intent created by the `RoleManager`,
so ensure you override the
[`onActivityResult()`](/reference/android/app/Activity#onActivityResult(int,%20int,%20android.content.Intent))
function to handle the user’s selection.

### Kotlin

```
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Tell the system that you want your app to handle call redirects. This
        // is done by using the RoleManager to register your app to handle redirects.
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.Q) {
            val roleManager = getSystemService(Context.ROLE_SERVICE) as RoleManager
            // Check if the app needs to register call redirection role.
            val shouldRequestRole = roleManager.isRoleAvailable(RoleManager.ROLE_CALL_REDIRECTION) &&
                    !roleManager.isRoleHeld(RoleManager.ROLE_CALL_REDIRECTION)
            if (shouldRequestRole) {
                val intent = roleManager.createRequestRoleIntent(RoleManager.ROLE_CALL_REDIRECTION)
                startActivityForResult(intent, REDIRECT_ROLE_REQUEST_CODE)
            }
        }
    }

    companion object {
        private const val REDIRECT_ROLE_REQUEST_CODE = 1
    }
}
```

### Java

```
class MainActivity extends AppCompatActivity {
    private static final int REDIRECT_ROLE_REQUEST_CODE = 0;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Tell the system that you want your app to handle call redirects. This
        // is done by using the RoleManager to register your app to handle redirects.
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.Q) {
            RoleManager roleManager = (RoleManager) getSystemService(Context.ROLE_SERVICE);
            // Check if the app needs to register call redirection role.
            boolean shouldRequestRole = roleManager.isRoleAvailable(RoleManager.ROLE_CALL_REDIRECTION) &&
                    !roleManager.isRoleHeld(RoleManager.ROLE_CALL_REDIRECTION);
            if (shouldRequestRole) {
                Intent intent = roleManager.createRequestRoleIntent(RoleManager.ROLE_CALL_REDIRECTION);
                startActivityForResult(intent, REDIRECT_ROLE_REQUEST_CODE);
            }
        }
    }
}
```