---
title: https://developer.android.com/training/sync-adapters/creating-authenticator
url: https://developer.android.com/training/sync-adapters/creating-authenticator
source: md.txt
---

The sync adapter framework assumes that your sync adapter transfers data between device storage
associated with an account and server storage that requires login access. For this reason, the
framework expects you to provide a component called an authenticator as part of your sync
adapter. This component plugs into the Android accounts and authentication framework and
provides a standard interface for handling user credentials such as login information.


Even if your app doesn't use accounts, you still need to provide an authenticator component.
If you don't use accounts or server login, the information handled by the authenticator is
ignored, so you can provide an authenticator component that contains stub method
implementations. You also need to provide a bound [Service](https://developer.android.com/reference/android/app/Service) that
allows the sync adapter framework to call the authenticator's methods.


This lesson shows you how to define all the parts of a stub authenticator that you need to
satisfy the requirements of the sync adapter framework. If you need to provide a real
authenticator that handles user accounts, read the reference documentation for
[AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator).

## Add a stub authenticator component


To add a stub authenticator component to your app, create a class that extends
[AbstractAccountAuthenticator](https://developer.android.com/reference/android/accounts/AbstractAccountAuthenticator), and then stub out the required methods,
either by returning `null` or by throwing an exception.


The following snippet shows an example of a stub authenticator class:  

### Kotlin

```kotlin
/*
 * Implement AbstractAccountAuthenticator and stub out all
 * of its methods
 */
class Authenticator(context: Context) // Simple constructor
    : AbstractAccountAuthenticator(context) {

    // Editing properties is not supported
    override fun editProperties(r: AccountAuthenticatorResponse, s: String): Bundle {
        throw UnsupportedOperationException()
    }

    // Don't add additional accounts
    @Throws(NetworkErrorException::class)
    override fun addAccount(
            r: AccountAuthenticatorResponse,
            s: String,
            s2: String,
            strings: Array<String>,
            bundle: Bundle
    ): Bundle?  = null

    // Ignore attempts to confirm credentials
    @Throws(NetworkErrorException::class)
    override fun confirmCredentials(
            r: AccountAuthenticatorResponse,
            account: Account,
            bundle: Bundle
    ): Bundle?  = null

    // Getting an authentication token is not supported
    @Throws(NetworkErrorException::class)
    override fun getAuthToken(
            r: AccountAuthenticatorResponse,
            account: Account,
            s: String,
            bundle: Bundle
    ): Bundle {
        throw UnsupportedOperationException()
    }

    // Getting a label for the auth token is not supported
    override fun getAuthTokenLabel(s: String): String {
        throw UnsupportedOperationException()
    }

    // Updating user credentials is not supported
    @Throws(NetworkErrorException::class)
    override fun updateCredentials(
            r: AccountAuthenticatorResponse,
            account: Account,
            s: String,
            bundle: Bundle
    ): Bundle {
        throw UnsupportedOperationException()
    }

    // Checking features for the account is not supported
    @Throws(NetworkErrorException::class)
    override fun hasFeatures(
            r: AccountAuthenticatorResponse,
            account: Account,
            strings: Array<String>
    ): Bundle {
        throw UnsupportedOperationException()
    }
}
```

### Java

```java
/*
 * Implement AbstractAccountAuthenticator and stub out all
 * of its methods
 */
public class Authenticator extends AbstractAccountAuthenticator {
    // Simple constructor
    public Authenticator(Context context) {
        super(context);
    }
    // Editing properties is not supported
    @Override
    public Bundle editProperties(
            AccountAuthenticatorResponse r, String s) {
        throw new UnsupportedOperationException();
    }
    // Don't add additional accounts
    @Override
    public Bundle addAccount(
            AccountAuthenticatorResponse r,
            String s,
            String s2,
            String[] strings,
            Bundle bundle) throws NetworkErrorException {
        return null;
    }
    // Ignore attempts to confirm credentials
    @Override
    public Bundle confirmCredentials(
            AccountAuthenticatorResponse r,
            Account account,
            Bundle bundle) throws NetworkErrorException {
        return null;
    }
    // Getting an authentication token is not supported
    @Override
    public Bundle getAuthToken(
            AccountAuthenticatorResponse r,
            Account account,
            String s,
            Bundle bundle) throws NetworkErrorException {
        throw new UnsupportedOperationException();
    }
    // Getting a label for the auth token is not supported
    @Override
    public String getAuthTokenLabel(String s) {
        throw new UnsupportedOperationException();
    }
    // Updating user credentials is not supported
    @Override
    public Bundle updateCredentials(
            AccountAuthenticatorResponse r,
            Account account,
            String s, Bundle bundle) throws NetworkErrorException {
        throw new UnsupportedOperationException();
    }
    // Checking features for the account is not supported
    @Override
    public Bundle hasFeatures(
        AccountAuthenticatorResponse r,
        Account account, String[] strings) throws NetworkErrorException {
        throw new UnsupportedOperationException();
    }
}
```

## Bind the authenticator to the framework


In order for the sync adapter framework to access your authenticator, you must create a bound
Service for it. This service provides an Android binder object that allows the framework
to call your authenticator and pass data between the authenticator and the framework.


The following snippet shows you how to define the bound [Service](https://developer.android.com/reference/android/app/Service):  

### Kotlin

```kotlin
/**
* A bound Service that instantiates the authenticator
* when started.
*/
class AuthenticatorService : Service() {

    // Instance field that stores the authenticator object
    private lateinit var mAuthenticator: Authenticator

    override fun onCreate() {
        // Create a new authenticator object
        mAuthenticator = Authenticator(getApplicationContext())
    }

    /*
     * When the system binds to this Service to make the RPC call
     * return the authenticator's IBinder.
     */
    override fun onBind(intent: Intent?): IBinder = mAuthenticator.iBinder
}
```

### Java

```java
/**
 * A bound Service that instantiates the authenticator
 * when started.
 */
public class AuthenticatorService extends Service {
    ...
    // Instance field that stores the authenticator object
    private Authenticator mAuthenticator;
    @Override
    public void onCreate() {
        // Create a new authenticator object
        mAuthenticator = new Authenticator(getApplicationContext());
    }
    /*
     * When the system binds to this Service to make the RPC call
     * return the authenticator's IBinder.
     */
    @Override
    public IBinder onBind(Intent intent) {
        return mAuthenticator.getIBinder();
    }
}
```

## Add the authenticator metadata file


To plug your authenticator component into the sync adapter and account frameworks, you need to
provide these framework with metadata that describes the component. This metadata declares the
account type you've created for your sync adapter and declares user interface elements
that the system displays if you want to make your account type visible to the user. Declare this
metadata in a XML file stored in the `/res/xml/` directory in your app project.
You can give any name to the file, although it's usually called `authenticator.xml`.


This XML file contains a single element `<account-authenticator>` that
has the following attributes:


`android:accountType`

:   The sync adapter framework requires each sync adapter to have an account type, in the form of a domain name. The framework uses the account type as part of the sync adapter's internal identification. For servers that require login, the account type along with a user account is sent to the server as part of the login credentials.
    If your server doesn't require login, you still have to provide an account type. For the
    value, use a domain name that you control. While the framework uses it to manage your
    sync adapter, the value is not sent to your server.


`android:icon`
:
    Pointer to a [Drawable](https://developer.android.com/guide/topics/resources/drawable-resource)
    resource containing an icon. If you make the sync adapter visible by specifying the
    attribute `android:userVisible="true"` in `res/xml/syncadapter.xml`,
    then you must provide this icon resource. It appears in the **Accounts** section of
    the system's Settings app.


`android:smallIcon`
:
    Pointer to a [Drawable](https://developer.android.com/guide/topics/resources/drawable-resource)
    resource containing a small version of the icon. This resource may be used instead of
    `android:icon` in the **Accounts** section of the system's Settings app,
    depending on the screen size.


`android:label`
:
    Localizable string that identifies the account type to users. If you make the sync adapter
    visible by specifying the attribute `android:userVisible="true"` in
    `res/xml/syncadapter.xml`, then you should provide this string. It appears in the
    **Accounts** section of the system's Settings app, next to the icon you define for the
    authenticator.


The following snippet shows the XML file for the authenticator you created previously:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<account-authenticator
        xmlns:android="http://schemas.android.com/apk/res/android"
        android:accountType="example.com"
        android:icon="@drawable/ic_launcher"
        android:smallIcon="@drawable/ic_launcher"
        android:label="@string/app_name"/>
```

## Declare the authenticator in the manifest


In a previous step, you created a bound [Service](https://developer.android.com/reference/android/app/Service) that links the authenticator
to the sync adapter framework. To identify this service to the system, declare it in your app
manifest by adding the following
[<service>](https://developer.android.com/guide/topics/manifest/service-element)
element as a child element of
[<application>](https://developer.android.com/guide/topics/manifest/application-element):  

```xml
    <service
            android:name="com.example.android.syncadapter.AuthenticatorService">
        <intent-filter>
            <action android:name="android.accounts.AccountAuthenticator"/>
        </intent-filter>
        <meta-data
            android:name="android.accounts.AccountAuthenticator"
            android:resource="@xml/authenticator" />
    </service>
```


The
[<intent-filter>](https://developer.android.com/guide/topics/manifest/intent-filter-element)
element sets up a filter that's triggered by the intent action
`android.accounts.AccountAuthenticator`, which sent by the system to run the
authenticator. When the filter is triggered, the system starts `AuthenticatorService`,
the bound [Service](https://developer.android.com/reference/android/app/Service) you have provided to wrap the authenticator.


The
[<meta-data>](https://developer.android.com/guide/topics/manifest/meta-data-element)
element declares the metadata for the authenticator. The
[android:name](https://developer.android.com/guide/topics/manifest/meta-data-element#nm)
attribute links the meta-data to the authentication framework. The
[android:resource](https://developer.android.com/guide/topics/manifest/meta-data-element#rsrc)
element specifies the name of the authenticator metadata file you created previously.


Besides an authenticator, a sync adapter also requires a content provider. If your app doesn't
use a content provider already, go to the next lesson to learn how to create a stub content
provider; otherwise, go to the lesson [Creating a Sync Adapter](https://developer.android.com/training/sync-adapters/creating-sync-adapter).