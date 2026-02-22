---
title: https://developer.android.com/privacy-and-security/security-gms-provider
url: https://developer.android.com/privacy-and-security/security-gms-provider
source: md.txt
---

# Update your security provider to protect against SSL exploits

Android relies on a security[Provider](https://developer.android.com/reference/java/security/Provider)to provide secure network communications. However, from time to time, vulnerabilities are found in the default security provider. To protect against these vulnerabilities,[Google Play services](https://developer.android.com/google/play-services)provides a way to automatically update a device's security provider to protect against known exploits. By calling Google Play services methods, you can help ensure that your app is running on a device that has the latest updates to protect against known exploits.

For example, a vulnerability was discovered in OpenSSL ([CVE-2014-0224](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)) that can leave apps open to an on-path attack that decrypts secure traffic without either side knowing. Google Play services version 5.0 offers a fix, but apps must check that this fix is installed. By using the Google Play services methods, you can help ensure that your app is running on a device that's secured against that attack.

**Caution:** Updating a device's security`Provider`does*not* update[android.net.SSLCertificateSocketFactory](https://developer.android.com/reference/android/net/SSLCertificateSocketFactory), which remains vulnerable. Rather than using this deprecated class, we encourage app developers to use high-level methods for interacting with cryptography, such as[HttpsURLConnection](https://developer.android.com/reference/javax/net/ssl/HttpsURLConnection).

## Patch the security provider using ProviderInstaller

To update a device's security provider, use the[`ProviderInstaller`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller)class. You can verify that the security provider is up to date (and update it, if necessary) by calling that class's[`installIfNeeded()`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller#installIfNeeded(android.content.Context))(or[`installIfNeededAsync()`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller#installIfNeededAsync(android.content.Context, com.google.android.gms.security.ProviderInstaller.ProviderInstallListener))) method. This section describes these options at a high level. The sections that follow provide more detailed steps and examples.

When you call`installIfNeeded()`, the`ProviderInstaller`does the following:

- If the device's`Provider`is successfully updated (or is already up to date), the method returns without throwing an exception.
- If the device's Google Play services library is out of date, the method throws[`GooglePlayServicesRepairableException`](https://developers.google.com/android/reference/com/google/android/gms/common/GooglePlayServicesRepairableException). The app can then catch this exception and show the user an appropriate dialog box to update Google Play services.
- If a non-recoverable error occurs, the method throws[`GooglePlayServicesNotAvailableException`](https://developers.google.com/android/reference/com/google/android/gms/common/GooglePlayServicesNotAvailableException.html)to indicate that it is unable to update the`Provider`. The app can then catch the exception and choose an appropriate course of action, such as displaying the standard[fix-it flow diagram](https://developers.google.com/android/reference/com/google/android/gms/common/SupportErrorDialogFragment.html).

The`installIfNeededAsync()`method behaves similarly, except that instead of throwing exceptions, it calls the appropriate callback method to indicate success or failure.

If the security provider is already up to date,`installIfNeeded()`takes a negligible amount of time. If the method needs to install a new`Provider`, this can take anywhere from 30-50 ms (on more recent devices) to 350 ms (on older devices). To avoid affecting user experience:

- Call`installIfNeeded()`from background networking threads immediately when the threads are loaded, instead of waiting for the thread to try to use the network. (There's no harm in calling the method multiple times, since it returns immediately if the security provider doesn't need updating.)
- Call the asynchronous version of the method,`installIfNeededAsync()`, if user experience can be affected by the thread blocking---for example, if the call is from an activity in the UI thread. (If you do this, you need to wait for the operation to finish before you attempt any secure communications. The`ProviderInstaller`calls your listener's[`onProviderInstalled()`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller.ProviderInstallListener.html#onProviderInstalled())method to signal success.)

**Warning:** If the`ProviderInstaller`is unable to install an updated`Provider`, your device's security provider might be vulnerable to known exploits. Your app should behave as if all HTTP communication is unencrypted.

Once the`Provider`is updated, all calls to security APIs (including SSL APIs) are routed through it. (However, this doesn't apply to`android.net.SSLCertificateSocketFactory`, which remains vulnerable to exploits like[CVE-2014-0224](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224).)

### Patch synchronously

The simplest way to patch the security provider is to call the synchronous method`installIfNeeded()`. This is appropriate if user experience won't be affected by the thread blocking while it waits for the operation to finish.

For example, here's an implementation of a[worker](https://developer.android.com/topic/libraries/architecture/workmanager/basics)that updates the security provider. Since a worker runs in the background, it's okay if the thread blocks while waiting for the security provider to be updated. The worker calls`installIfNeeded()`to update the security provider. If the method returns normally, the worker knows the security provider is up to date. If the method throws an exception, the worker can take appropriate action (such as prompting the user to update Google Play services).  

### Kotlin

```kotlin
/**
 * Sample patch Worker using {@link ProviderInstaller}.
 */
class PatchWorker(appContext: Context, workerParams: WorkerParameters): Worker(appContext, workerParams) {

  override fun doWork(): Result {
        try {
            ProviderInstaller.installIfNeeded(context)
        } catch (e: GooglePlayServicesRepairableException) {

            // Indicates that Google Play services is out of date, disabled, etc.

            // Prompt the user to install/update/enable Google Play services.
            GoogleApiAvailability.getInstance()
                    .showErrorNotification(context, e.connectionStatusCode)

            // Notify the WorkManager that a soft error occurred.
            return Result.failure()

        } catch (e: GooglePlayServicesNotAvailableException) {
            // Indicates a non-recoverable error; the ProviderInstaller can't
            // install an up-to-date Provider.

            // Notify the WorkManager that a hard error occurred.
            return Result.failure()
        }


        // If this is reached, you know that the provider was already up to date
        // or was successfully updated.
        return Result.success()
    }
}
```

### Java

```java
/**
 * Sample patch Worker using {@link ProviderInstaller}.
 */
public class PatchWorker extends Worker {

  ...

  @Override
  public Result doWork() {
    try {
      ProviderInstaller.installIfNeeded(getContext());
    } catch (GooglePlayServicesRepairableException e) {

      // Indicates that Google Play services is out of date, disabled, etc.

      // Prompt the user to install/update/enable Google Play services.
      GoogleApiAvailability.getInstance()
              .showErrorNotification(context, e.connectionStatusCode)

      // Notify the WorkManager that a soft error occurred.
      return Result.failure();

    } catch (GooglePlayServicesNotAvailableException e) {
      // Indicates a non-recoverable error; the ProviderInstaller can't
      // install an up-to-date Provider.

      // Notify the WorkManager that a hard error occurred.
      return Result.failure();
    }

    // If this is reached, you know that the provider was already up to date
    // or was successfully updated.
    return Result.success();
  }
}
```

### Patch asynchronously

Updating the security provider can take as much as 350 ms (on older devices). If you're doing the update on a thread that directly affects user experience, such as the UI thread, you don't want to make a synchronous call to update the provider, since that can result in the app or device freezing until the operation finishes. Instead, use the asynchronous method`installIfNeededAsync()`. That method indicates its success or failure by calling callbacks.

For example, here's some code that updates the security provider in an activity in the UI thread. The activity calls`installIfNeededAsync()`to update the provider, and designates itself as the listener to receive success or failure notifications. If the security provider is up to date or is successfully updated, the activity's[`onProviderInstalled()`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller.ProviderInstallListener.html#onProviderInstalled())method is called, and the activity knows communication is secure. If the provider can't be updated, the activity's[`onProviderInstallFailed()`](https://developers.google.com/android/reference/com/google/android/gms/security/ProviderInstaller.ProviderInstallListener.html#onProviderInstallFailed(int, android.content.Intent))method is called, and the activity can take appropriate action (such as prompting the user to update Google Play services).  

### Kotlin

```kotlin
private const val ERROR_DIALOG_REQUEST_CODE = 1

/**
 * Sample activity using {@link ProviderInstaller}.
 */
class MainActivity : Activity(), ProviderInstaller.ProviderInstallListener {

    private var retryProviderInstall: Boolean = false

    // Update the security provider when the activity is created.
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ProviderInstaller.installIfNeededAsync(this, this)
    }

    /**
     * This method is only called if the provider is successfully updated
     * (or is already up to date).
     */
    override fun onProviderInstalled() {
        // Provider is up to date; app can make secure network calls.
    }

    /**
     * This method is called if updating fails. The error code indicates
     * whether the error is recoverable.
     */
    override fun onProviderInstallFailed(errorCode: Int, recoveryIntent: Intent) {
        GoogleApiAvailability.getInstance().apply {
            if (isUserResolvableError(errorCode)) {
                // Recoverable error. Show a dialog prompting the user to
                // install/update/enable Google Play services.
                showErrorDialogFragment(this@MainActivity, errorCode, ERROR_DIALOG_REQUEST_CODE) {
                    // The user chose not to take the recovery action.
                    onProviderInstallerNotAvailable()
                }
            } else {
                onProviderInstallerNotAvailable()
            }
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int,
                                  data: Intent) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == ERROR_DIALOG_REQUEST_CODE) {
            // Adding a fragment via GoogleApiAvailability.showErrorDialogFragment
            // before the instance state is restored throws an error. So instead,
            // set a flag here, which causes the fragment to delay until
            // onPostResume.
            retryProviderInstall = true
        }
    }

    /**
     * On resume, check whether a flag indicates that the provider needs to be
     * reinstalled.
     */
    override fun onPostResume() {
        super.onPostResume()
        if (retryProviderInstall) {
            // It's safe to retry installation.
            ProviderInstaller.installIfNeededAsync(this, this)
        }
        retryProviderInstall = false
    }

    private fun onProviderInstallerNotAvailable() {
        // This is reached if the provider can't be updated for some reason.
        // App should consider all HTTP communication to be vulnerable and take
        // appropriate action.
    }
}
```

### Java

```java
/**
 * Sample activity using {@link ProviderInstaller}.
 */
public class MainActivity extends Activity
    implements ProviderInstaller.ProviderInstallListener {

  private static final int ERROR_DIALOG_REQUEST_CODE = 1;

  private boolean retryProviderInstall;

  // Update the security provider when the activity is created.
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    ProviderInstaller.installIfNeededAsync(this, this);
  }

  /**
   * This method is only called if the provider is successfully updated
   * (or is already up to date).
   */
  @Override
  protected void onProviderInstalled() {
    // Provider is up to date; app can make secure network calls.
  }

  /**
   * This method is called if updating fails. The error code indicates
   * whether the error is recoverable.
   */
  @Override
  protected void onProviderInstallFailed(int errorCode, Intent recoveryIntent) {
    GoogleApiAvailability availability = GoogleApiAvailability.getInstance();
    if (availability.isUserRecoverableError(errorCode)) {
      // Recoverable error. Show a dialog prompting the user to
      // install/update/enable Google Play services.
      availability.showErrorDialogFragment(
          this,
          errorCode,
          ERROR_DIALOG_REQUEST_CODE,
          new DialogInterface.OnCancelListener() {
            @Override
            public void onCancel(DialogInterface dialog) {
              // The user chose not to take the recovery action.
              onProviderInstallerNotAvailable();
            }
          });
    } else {
      // Google Play services isn't available.
      onProviderInstallerNotAvailable();
    }
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode,
      Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == ERROR_DIALOG_REQUEST_CODE) {
      // Adding a fragment via GoogleApiAvailability.showErrorDialogFragment
      // before the instance state is restored throws an error. So instead,
      // set a flag here, which causes the fragment to delay until
      // onPostResume.
      retryProviderInstall = true;
    }
  }

  /**
  * On resume, check whether a flag indicates that the provider needs to be
  * reinstalled.
  */
  @Override
  protected void onPostResume() {
    super.onPostResume();
    if (retryProviderInstall) {
      // It's safe to retry installation.
      ProviderInstaller.installIfNeededAsync(this, this);
    }
    retryProviderInstall = false;
  }

  private void onProviderInstallerNotAvailable() {
    // This is reached if the provider can't be updated for some reason.
    // App should consider all HTTP communication to be vulnerable and take
    // appropriate action.
  }
}
```