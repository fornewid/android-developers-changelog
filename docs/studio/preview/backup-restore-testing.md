---
title: https://developer.android.com/studio/preview/backup-restore-testing
url: https://developer.android.com/studio/preview/backup-restore-testing
source: md.txt
---

> [!WARNING]
> **Experimental:** Automated backup and restore testing continues to evolve during the alpha phase, and its APIs and DSL syntax might change between releases. Report feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=2258505&template=2395410).

When users set up a new device or reinstall your app, Android can restore your
app's data from a cloud backup or a device-to-device transfer. If your
[backup rules](https://developer.android.com/identity/data/autobackup) leave out important data, or your app can't use
the data that it restores, users lose their settings and progress without
seeing an error.

Automated backup and restore tests help you catch these problems before you
release your app. They're JUnit 5 tests that run on your development machine
and control connected devices through Android Debug Bridge (adb). Each test
seeds app data on a device, backs up and restores the app through the Android
backup framework, and then checks that the data is intact. You configure the
tests as an Android Gradle plugin (AGP) [test suite](https://developer.android.com/reference/tools/gradle-api/9.5/com/android/build/api/dsl/AgpTestSuite) in your
module's build file.

## How it works

A backup and restore test suite has two parts that work together:

- **Host tests** are JUnit 5 tests that run on your development machine. They use a [`BackupRestoreController`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/BackupRestoreController) for each device to seed data, back up and restore your app, and check the results.
- **Device actions** are classes that implement [`BackupDeviceAction`](https://developer.android.com/reference/kotlin/androidx/test/backup/BackupDeviceAction). They run in your app's process on the device, so they can read and write data through your app's own code. Host tests call device actions by class name.

When you run the suite, AGP builds your app and a test APK that contains your
device actions. The test framework installs both APKs on each device that the
tests use and clears your app's data before each test.

### Built-in storage types

The following table lists the [`StorageDomain`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/StorageDomain) subclasses that
let you seed and verify data without writing device actions:

| Storage domain | Data |
|---|---|
| `StorageDomain.Preference` | A key in a `SharedPreferences` file. |
| `StorageDomain.Database` | A row in a SQLite database table. |
| `StorageDomain.TextFile` | A text file in your app's internal storage. |
| `StorageDomain.BinaryFile` | A binary file in your app's internal storage. |

To test other data, such as DataStore files, [write device
actions](https://developer.android.com/studio/preview/backup-restore-testing#custom-actions).

### Transport modes

Each backup uses a [`BackupTransportMode`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/BackupTransportMode) value. The following
table lists the supported transport modes:

| Mode | Scenario |
|---|---|
| `LOCAL` | A backup to the local backup transport of the device. The backup data stays on the device. |
| `CLOUD_ENCRYPTED` | A cloud backup, such as one saved to the user's Google Account from a device with client-side encryption. |
| `CLOUD_UNENCRYPTED` | A cloud backup from a device that doesn't have client-side encryption. |
| `DEVICE_TO_DEVICE` | A device-to-device transfer, for example over a cable or Wi-Fi. |

`LOCAL` works on any supported device. The cloud and device-to-device modes
create the same backups as the **Backup App Data** action in Android Studio:
the backup is saved to your development machine instead of being uploaded or
sent to another device. The cloud and device-to-device modes require Google Play
services on the device and a debuggable build of your app. If your backup rules
depend on client-side encryption, test both cloud modes.

## Requirements

To use automated backup and restore testing, make sure that your environment
meets the following requirements:

- Gradle version 9.6.0 or higher.
- JDK version 17 or higher.
- A device or emulator running Android 12 (API level 31) or higher that's connected through adb:
  - Devices or emulators on API level 36.1 or higher require Google Play services version 26.33.30 or higher.
  - To test transfers between two devices, connect two devices.

## Compatibility

The following table lists the minimum and recommended versions for automated
backup and restore testing:

| Component | Minimum version | Recommended version |
|---|---|---|
| Android Studio | Rabbit 2 Canary 1 | Rabbit 2 Canary 4 or higher |
| Android Gradle plugin (AGP) | 9.5.0-alpha06 | 9.5.0-alpha09 or higher |
| `androidx.test.backup` libraries | 1.0.0-alpha01 | 1.0.0-alpha03 or higher |

Each preview version of AGP requires the matching preview version of Android
Studio. For more information, see [AGP previews](https://developer.android.com/studio/preview/features#agp-previews).

## Set up your project

To add a backup and restore test suite to your app module, complete the
following steps:

### Enable experimental flags

In your project's `gradle.properties` file, enable test suites and backup
tests:

    android.experimental.testSuiteSupport=true
    android.experimental.enableBackupTest=true

### Declare the test suite

In your app module's `build.gradle.kts` file, declare a backup test suite in
the `testOptions` block:

    android {
        testOptions {
            backupTests {
                create("backupTest") {
                    backupTestLibraryVersion = "1.0.0-alpha03"
                }
            }
        }
    }

The suite name, `backupTest` in this example, determines the source set
directories and the Gradle task names. You can customize the suite with the
following optional properties:

- Use `backupTestLibraryVersion` to set the version of the `androidx.test.backup` libraries that AGP adds to the suite, such as `"1.0.0-alpha03"`. This property is optional. If you omit it, AGP falls back to a default library version based on the AGP version. The examples on this page require version 1.0.0-alpha03 or higher.
- Use `targetVariants` to specify the build variants that the suite tests, such as `targetVariants.add("demoDebug")`. This property is optional. If you omit it, the suite tests the variants of your module's `testBuildType`, which is `debug` by default. We recommend testing a debuggable variant because the cloud and device-to-device transport modes require a debuggable app.

AGP adds the host library, `androidx.test.backup:backup-host`, and JUnit 5 to
the host tests. It adds the device library, `androidx.test.backup:backup`, to
the test APK and sets the test APK's instrumentation runner.

To add other dependencies, use the `hostJar` and `testApk` blocks of the suite.
For example, to use [Truth](https://truth.dev/) in your host tests, add it to the `hostJar`
block:

    create("backupTest") {
        hostJar {
            dependencies {
                implementation("com.google.truth:truth:1.4.2")
            }
        }
    }

### Create the source sets

Create source set directories that match the suite name:

- Put host tests in `src/{suiteName}/test/kotlin/`.
- Put device actions in `src/{suiteName}/androidTest/kotlin/`.

For example, a suite named `backupTest` uses the following directory structure:

    app/src/backupTest/
    ├── androidTest/
    │   └── kotlin/com/example/myapp/ThemeActions.kt
    └── test/
        └── kotlin/com/example/myapp/SettingsBackupTest.kt

### Check your backup configuration

Tests back up and restore the data that your app's backup configuration
includes. Make sure that backup is enabled for your app and that your
[backup rules](https://developer.android.com/identity/data/autobackup) include the data that you test.

## Write backup and restore tests

Write host tests in the suite's `test` source set. Annotate each test class with
`@ExtendWith(BackupRestoreExtension::class)`, which provides connected devices
to the tests. The tests run against the app variant that the suite targets, so
you don't need to set its application ID.

Each test method declares a `BackupRestoreController` parameter for each device
that it uses.

> [!IMPORTANT]
> **Important:** JUnit 5 ignores test methods that return a value. They don't run, and the test report doesn't list them. A test written as `= runBlocking { ... }` returns the value of the block's last expression, so declare the `Unit` return type explicitly, as in `fun myTest(...): Unit = runBlocking { ... }`.

### Test built-in storage types

To test built-in storage types, call [`runBackupRestoreFlow`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/BackupRestoreController#runBackupRestoreFlow(kotlin.collections.List,java.nio.file.Path,androidx.test.backup.host.BackupTransportMode)) with
the data to seed, a directory for the backup file, and a transport mode. The
method runs the following steps on the device:

1. Seeds each storage domain.
2. Stops the app.
3. Backs up the app.
4. Clears the app's data.
5. Restores the backup.
6. Verifies that each storage domain has the seeded value.

If a step fails, the method throws an exception, which fails the test. The
following example tests a `SharedPreferences` key, a SQLite row, and an
internal file using the local backup transport:

    package com.example.myapp

    import androidx.test.backup.host.BackupRestoreController
    import androidx.test.backup.host.BackupRestoreExtension
    import androidx.test.backup.host.BackupTransportMode
    import androidx.test.backup.host.StorageDomain
    import java.nio.file.Path
    import kotlinx.coroutines.runBlocking
    import org.junit.jupiter.api.Test
    import org.junit.jupiter.api.extension.ExtendWith
    import org.junit.jupiter.api.io.TempDir

    @ExtendWith(BackupRestoreExtension::class)
    class SettingsBackupTest {

        @Test
        fun settingsSurviveBackupAndRestore(
            device: BackupRestoreController,
            @TempDir outputDir: Path,
        ): Unit = runBlocking {
            device.runBackupRestoreFlow(
                storages = listOf(
                    StorageDomain.Preference(
                        prefName = "settings",
                        key = "theme",
                        value = "dark",
                    ),
                    StorageDomain.Database(
                        dbName = "notes.db",
                        table = "notes",
                        primaryKeyCol = "id",
                        primaryKeyVal = 1,
                        columnValues = mapOf("title" to "Groceries"),
                    ),
                    StorageDomain.TextFile(
                        path = "drafts/note.txt",
                        content = "Buy milk",
                    ),
                ),
                outputDir = outputDir,
                mode = BackupTransportMode.LOCAL,
            )
        }
    }

Keep the following in mind when you define storage domains:

- `Preference` takes the name of the `SharedPreferences` file without the `.xml` extension.
- `TextFile` and `BinaryFile` resolve relative paths against your app's [`filesDir`](https://developer.android.com/reference/android/content/Context#getFilesDir()).
- `Database` writes the row with SQL, and creates the table with `TEXT` columns if the table doesn't exist. If your app uses Room, we recommend testing database content with [device actions](https://developer.android.com/studio/preview/backup-restore-testing#custom-actions) that use your DAOs so that the database has the schema that Room expects.

### Write device actions

To seed or verify data that the built-in storage types don't cover, write
device actions in the suite's `androidTest` source set. A device action
implements `BackupDeviceAction` and overrides two members:

- Set `phase` to `BackupDeviceAction.PHASE_POPULATE` for an action that seeds data, or `BackupDeviceAction.PHASE_VERIFY` for an action that checks data.
- Implement `execute` to run the action with your app's `Context` and the arguments from the host test. Return a result created with the `BackupDeviceActionResult.success` or `BackupDeviceActionResult.failure` factory method, and pass an error message to `failure`.

The `execute` method runs in your app's process on a background thread, so it
can block until reads and writes finish.

The following example seeds and verifies a theme setting that the app stores
with [Preferences DataStore](https://developer.android.com/topic/libraries/architecture/datastore). The app defines the DataStore in its
main source set:

    // In app/src/main/kotlin/com/example/myapp/Settings.kt
    package com.example.myapp

    import android.content.Context
    import androidx.datastore.preferences.core.stringPreferencesKey
    import androidx.datastore.preferences.preferencesDataStore

    val Context.settingsDataStore by preferencesDataStore(name = "settings")
    val THEME_KEY = stringPreferencesKey("theme")

The device actions use the same definitions:

    // In app/src/backupTest/androidTest/kotlin/com/example/myapp/ThemeActions.kt
    package com.example.myapp

    import android.content.Context
    import androidx.datastore.preferences.core.edit
    import androidx.test.backup.BackupDeviceAction
    import androidx.test.backup.BackupDeviceActionArgs
    import androidx.test.backup.BackupDeviceActionResult
    import kotlinx.coroutines.flow.first
    import kotlinx.coroutines.runBlocking

    class SeedThemeAction : BackupDeviceAction {
        override val phase = BackupDeviceAction.PHASE_POPULATE

        override fun execute(
            context: Context,
            args: BackupDeviceActionArgs,
        ): BackupDeviceActionResult {
            val theme = args["theme"]
                ?: return BackupDeviceActionResult.failure("Missing theme argument")
            runBlocking {
                context.settingsDataStore.edit { it[THEME_KEY] = theme }
            }
            return BackupDeviceActionResult.success()
        }
    }

    class VerifyThemeAction : BackupDeviceAction {
        override val phase = BackupDeviceAction.PHASE_VERIFY

        override fun execute(
            context: Context,
            args: BackupDeviceActionArgs,
        ): BackupDeviceActionResult {
            val expected = args["theme"]
            val actual = runBlocking {
                context.settingsDataStore.data.first()[THEME_KEY]
            }
            return if (actual == expected) {
                BackupDeviceActionResult.success()
            } else {
                BackupDeviceActionResult.failure("Expected $expected, found $actual")
            }
        }
    }

To return data to the host test, pass a map to the `success` method. The host
test reads the map from `BackupActionResult.Success.data`.

### Run each step of the flow

To use device actions, or to customize the flow, call each step yourself. The
following host test runs the device actions from the previous section around a
cloud backup and restore:

    package com.example.myapp

    import androidx.test.backup.host.BackupActionResult
    import androidx.test.backup.host.BackupRestoreController
    import androidx.test.backup.host.BackupRestoreExtension
    import androidx.test.backup.host.BackupTransportMode
    import java.nio.file.Path
    import kotlinx.coroutines.runBlocking
    import org.junit.jupiter.api.Test
    import org.junit.jupiter.api.extension.ExtendWith
    import org.junit.jupiter.api.fail
    import org.junit.jupiter.api.io.TempDir

    const val SEED_THEME = "com.example.myapp.SeedThemeAction"
    const val VERIFY_THEME = "com.example.myapp.VerifyThemeAction"

    @ExtendWith(BackupRestoreExtension::class)
    class ThemeBackupTest {

        @Test
        fun themeSurvivesCloudBackup(
            device: BackupRestoreController,
            @TempDir outputDir: Path,
        ): Unit = runBlocking {
            val args = mapOf("theme" to "dark")
            device.runOnDevice(SEED_THEME, args).assertSuccess()

            device.stopApp()
            val backupFile = device.performBackup(
                BackupTransportMode.CLOUD_ENCRYPTED,
                outputDir,
            )
            device.clearAppData()
            device.performRestore(backupFile)

            device.runOnDevice(VERIFY_THEME, args).assertSuccess()
        }
    }

    fun BackupActionResult.assertSuccess() {
        if (this is BackupActionResult.Failure) fail(errorMessage)
    }

When a device action fails, `runOnDevice` returns a
[`BackupActionResult.Failure`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/BackupActionResult) instead of throwing an exception,
so check the result. The other steps throw an exception if they fail.

### Test transfers between devices

To test a transfer between two devices, declare a `BackupRestoreController`
parameter for each device. Back up the app on the source device, and then
restore the backup file on the target device. The following example reuses
the constants and the `assertSuccess` helper from the previous example:

    package com.example.myapp

    import androidx.test.backup.host.BackupRestoreController
    import androidx.test.backup.host.BackupRestoreExtension
    import androidx.test.backup.host.BackupTransportMode
    import androidx.test.backup.host.Device
    import java.nio.file.Path
    import kotlinx.coroutines.runBlocking
    import org.junit.jupiter.api.Test
    import org.junit.jupiter.api.extension.ExtendWith
    import org.junit.jupiter.api.io.TempDir

    @ExtendWith(BackupRestoreExtension::class)
    class ThemeTransferTest {

        @Test
        fun themeTransfersToNewDevice(
            @Device(role = "source") source: BackupRestoreController,
            @Device(role = "target") target: BackupRestoreController,
            @TempDir outputDir: Path,
        ): Unit = runBlocking {
            val args = mapOf("theme" to "dark")
            source.runOnDevice(SEED_THEME, args).assertSuccess()
            source.stopApp()
            val backupFile = source.performBackup(
                BackupTransportMode.DEVICE_TO_DEVICE,
                outputDir,
            )

            target.clearAppData()
            target.performRestore(backupFile)
            target.runOnDevice(VERIFY_THEME, args).assertSuccess()
        }
    }

The `role` values of [`@Device`](https://developer.android.com/reference/kotlin/androidx/test/backup/host/Device) let you
[choose a device for each parameter](https://developer.android.com/studio/preview/backup-restore-testing#choose-devices) when you run the tests. If
only one device is connected, both parameters use that device, and the test
simulates the transfer on a single device. Clearing the target's data makes
sure that the restored data comes from the backup.

### Choose devices

By default, the test framework sorts the online devices by serial number and
assigns them to the `BackupRestoreController` parameters of each test in order.
If a test has more device parameters than there are devices, the extra
parameters share the first device. The `ANDROID_SERIAL` environment variable
doesn't affect device assignment.

To choose devices without putting serial numbers in your tests, give each device
parameter a role with `@Device(role = "...")`. Then, when you run the tests,
bind each role to a device with the
`androidx.test.backup.device.serial.{role}` system property. For example, the
following command runs the suite with `emulator-5554` as the source device and
`emulator-5556` as the target device:

    ./gradlew :app:testDebugBackupTestDefaultTestSuite -Dandroidx.test.backup.device.serial.source=emulator-5554 -Dandroidx.test.backup.device.serial.target=emulator-5556

A binding applies only to parameters with that role. Other parameters get the
remaining devices.

You can also choose devices with the `serial` and `api` values of `@Device`, or
with the following system properties, which take precedence over `@Device`
values:

| System property | Description |
|---|---|
| `androidx.test.backup.device.serial.{role}` | The serial number of the device for parameters annotated with `@Device(role = "{role}")`. It takes precedence over `serials` and `serial`. |
| `androidx.test.backup.device.serials` | A comma-separated list of serial numbers, assigned to device parameters in order. |
| `androidx.test.backup.device.serial` | The serial number of the device for the device parameters that `serials` doesn't cover. |
| `androidx.test.backup.device.apis` | A comma-separated list of API levels, assigned to device parameters in order. |
| `androidx.test.backup.device.api` | The API level of the device for the device parameters that `apis` doesn't cover. |

Pass these properties with `-D` in the same way. The `serial`, `serials`,
`api`, and `apis` properties apply to every test that runs, so use the
`--tests` option to run only the tests that need them.

### Test Restore Credentials

If your app uses [Restore Credentials](https://developer.android.com/identity/sign-in/restore-credentials), test that its
restore key survives a backup and restore. The cloud and device-to-device modes
back up the key with your app's data, but `LOCAL` doesn't.

Write device actions that create the key and get it with Credential Manager. The
create action returns the key's credential ID, so that the verify action can
check that the restore brings back the same key. In this example,
`createRequestJson` and `getRequestJson` are the request JSON strings that your
app passes to Credential Manager:

    // In app/src/backupTest/androidTest/kotlin/com/example/myapp/RestoreKeyActions.kt
    package com.example.myapp

    import android.content.Context
    import androidx.credentials.CreateRestoreCredentialRequest
    import androidx.credentials.CreateRestoreCredentialResponse
    import androidx.credentials.CredentialManager
    import androidx.credentials.GetCredentialRequest
    import androidx.credentials.GetRestoreCredentialOption
    import androidx.credentials.RestoreCredential
    import androidx.test.backup.BackupDeviceAction
    import androidx.test.backup.BackupDeviceActionArgs
    import androidx.test.backup.BackupDeviceActionResult
    import kotlinx.coroutines.runBlocking
    import org.json.JSONObject

    class CreateRestoreKeyAction : BackupDeviceAction {
        override val phase = BackupDeviceAction.PHASE_POPULATE

        override fun execute(
            context: Context,
            args: BackupDeviceActionArgs,
        ): BackupDeviceActionResult {
            val request = CreateRestoreCredentialRequest(createRequestJson)
            val response = runBlocking {
                CredentialManager.create(context).createCredential(context, request)
            } as CreateRestoreCredentialResponse
            val credentialId = JSONObject(response.responseJson).getString("id")
            return BackupDeviceActionResult.success(mapOf("credential_id" to credentialId))
        }
    }

    class VerifyRestoreKeyAction : BackupDeviceAction {
        override val phase = BackupDeviceAction.PHASE_VERIFY

        override fun execute(
            context: Context,
            args: BackupDeviceActionArgs,
        ): BackupDeviceActionResult {
            val option = GetRestoreCredentialOption(getRequestJson)
            val response = runBlocking {
                CredentialManager.create(context)
                    .getCredential(context, GetCredentialRequest(listOf(option)))
            }
            val credential = response.credential as RestoreCredential
            val credentialId = JSONObject(credential.authenticationResponseJson).getString("id")
            val expected = args["credential_id"]
            return if (credentialId == expected) {
                BackupDeviceActionResult.success()
            } else {
                BackupDeviceActionResult.failure("Expected key $expected, found $credentialId")
            }
        }
    }

The following host test creates the key on the source device, restores it on the
target device, and checks it there. It uses the `assertSuccess` helper from
[Run each step of the flow](https://developer.android.com/studio/preview/backup-restore-testing#step-by-step):

    package com.example.myapp

    import androidx.test.backup.host.BackupActionResult
    import androidx.test.backup.host.BackupRestoreController
    import androidx.test.backup.host.BackupRestoreExtension
    import androidx.test.backup.host.BackupTransportMode
    import androidx.test.backup.host.Device
    import java.nio.file.Path
    import kotlinx.coroutines.runBlocking
    import org.junit.jupiter.api.Test
    import org.junit.jupiter.api.extension.ExtendWith
    import org.junit.jupiter.api.io.TempDir

    const val CREATE_RESTORE_KEY = "com.example.myapp.CreateRestoreKeyAction"
    const val VERIFY_RESTORE_KEY = "com.example.myapp.VerifyRestoreKeyAction"

    @ExtendWith(BackupRestoreExtension::class)
    class RestoreKeyTest {

        @Test
        fun restoreKeyTransfersToNewDevice(
            @Device(role = "source") source: BackupRestoreController,
            @Device(role = "target") target: BackupRestoreController,
            @TempDir outputDir: Path,
        ): Unit = runBlocking {
            val created = source.runOnDevice(CREATE_RESTORE_KEY)
            created.assertSuccess()
            val credentialId =
                (created as BackupActionResult.Success).data.getValue("credential_id")
            source.stopApp()
            val backupFile = source.performBackup(
                BackupTransportMode.DEVICE_TO_DEVICE,
                outputDir,
            )

            // Also deletes any restore key on the target.
            target.clearAppData()
            target.performRestore(backupFile)
            target.runOnDevice(VERIFY_RESTORE_KEY, mapOf("credential_id" to credentialId))
                .assertSuccess()
        }
    }

To create a key with `isCloudBackupEnabled` set to `true`, the default, the
source device needs a Google Account with backup turned on and a screen lock.
Otherwise, Credential Manager throws
[`E2eeUnavailableException`](https://developer.android.com/reference/kotlin/androidx/credentials/exceptions/restorecredential/E2eeUnavailableException).

Unlike a cloud restore on a new device, the cloud modes don't require the same
Google Account or the source device's screen lock, and they restore keys created
with `isCloudBackupEnabled` set to `false`.

> [!CAUTION]
> **Caution:** Backup files from the cloud and device-to-device modes contain the restore key without encryption. Treat them as secrets.

### Keep app data between tests

Before each test, the test framework clears your app's data on each device that
the test uses. To turn this off for a test class or method, annotate it with
`@Isolation(IsolationPolicy.MANUAL)`.

### Write tests in Java

`BackupRestoreController` methods are Kotlin suspend functions. If you write
host tests in Java, use the `Async` variant of each method, such as
`runBackupRestoreFlowAsync`, which returns a `ListenableFuture`.

## Run backup and restore tests

AGP creates a Gradle task for each variant that the suite tests, named
`test{Variant}{SuiteName}DefaultTestSuite`. To run the `backupTest` suite
against the `debug` variant, connect your devices and run the task:

    ./gradlew :app:testDebugBackupTestDefaultTestSuite

The `check`, `test`, and `connectedCheck` tasks don't run backup and restore
test suites, so run the suite's task explicitly.

To run a single test class or method, use the
[`--tests` option](https://docs.gradle.org/current/userguide/java_testing.html#test_filtering):

    ./gradlew :app:testDebugBackupTestDefaultTestSuite --tests "com.example.myapp.ThemeBackupTest"

## Inspect test reports

After a test run completes, AGP generates an HTML test report at
`{module}/build/reports/tests/{taskName}/index.html`, such as
`app/build/reports/tests/testDebugBackupTestDefaultTestSuite/index.html`.

## Troubleshoot failed restores

A cloud or device-to-device restore fails with an error message in the
following cases:

- **Google Play services skips your app** , for example because its application ID starts with `com.google.` or `com.android.`, its backup is empty, or it sets `android:allowBackup="false"`. To test an app with such an application ID, use the `LOCAL` mode.
- **The Google Play services version is lower than 26.33.30** on a device or emulator that runs API level 36.1 or higher. Update Google Play services through the Play Store on the device, or use a system image that comes with version 26.33.30 or higher.

## Known issues and limitations

Automated backup and restore testing has the following known issues and
limitations:

- Android Studio support for test suites isn't available yet. The code editor might show unresolved reference errors in test suite source files even when your project is configured correctly. Build and run backup and restore tests from the command line using Gradle instead.
- Tests run only on devices and emulators that are connected to your development machine through adb. Firebase Test Lab isn't supported.
- Tests clear your app's data and change backup settings on the devices that they use. We recommend using dedicated test devices.

For changes in each release, see the
[backup and restore testing release notes](https://developer.android.com/studio/preview/backup-restore-testing-release-notes).