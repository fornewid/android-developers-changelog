---
title: https://developer.android.com/tools/agents/lightbuild/publish
url: https://developer.android.com/tools/agents/lightbuild/publish
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

To publish your app on Google Play, you build a release version of the app as an
Android App Bundle, sign it with your upload key, and upload it to the Play
Console. This page shows you how to configure release signing in a Lightbuild
project and build a signed app bundle with the Lightbuild CLI.

## Create an upload key

Google Play uses [Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play) to sign the APKs that it
delivers to users, and you sign the app bundles that you upload with an upload
key. If you don't have an upload key yet, create one with `keytool`, which is
included with the JDK:

    keytool -genkey -v -keystore upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload

The command prompts you for passwords for the keystore and the key, and then
creates a keystore file named `upload-keystore.jks` in the current directory.
Store the keystore in a secure location outside your project, and don't check it
in to version control. For more information, see [Sign your app](https://developer.android.com/studio/publish/app-signing).

## Configure release signing

In your app module's `lightbuild.yaml` file, add a `signing` block to the
`release` profile in `packaging`. Instead of writing your passwords in the file,
reference environment variables with the `${NAME}` syntax:

    android:
      packaging:
        release:
          signing:
            storeFile: "${RELEASE_STORE_FILE}"
            storePassword: "${RELEASE_STORE_PASSWORD}"
            keyAlias: "${RELEASE_KEY_ALIAS}"
            keyPassword: "${RELEASE_KEY_PASSWORD}"

When you build, Lightbuild reads each value from its environment variable, so
your passwords aren't stored in your project's files. For more information about
these settings, see [Packaging](https://developer.android.com/tools/agents/lightbuild/schema#packaging) in the Lightbuild configuration
reference.

> [!IMPORTANT]
> **Important:** Don't write passwords directly in your `lightbuild.yaml` files. Anyone who can read your project's files, including its version control history, could use them to sign apps with your key.

## Set the environment variables

Before you build, set the environment variables in the terminal where you run
the Lightbuild CLI. For example, on macOS or Linux:

    export RELEASE_STORE_FILE="$HOME/keystores/upload-keystore.jks"
    export RELEASE_STORE_PASSWORD="KEYSTORE_PASSWORD"
    export RELEASE_KEY_ALIAS="upload"
    export RELEASE_KEY_PASSWORD="KEY_PASSWORD"

On Windows, in PowerShell:

    $env:RELEASE_STORE_FILE = "$HOME\keystores\upload-keystore.jks"
    $env:RELEASE_STORE_PASSWORD = "KEYSTORE_PASSWORD"
    $env:RELEASE_KEY_ALIAS = "upload"
    $env:RELEASE_KEY_PASSWORD = "KEY_PASSWORD"

Replace `KEYSTORE_PASSWORD` and `KEY_PASSWORD` with your passwords. In a CI
system, store the passwords as secrets, and expose them to your build as
environment variables.

> [!WARNING]
> **Warning:** If any of these environment variables isn't set, all builds of your app module fail, including debug builds, with an error such as `Missing required environment variable: RELEASE_STORE_FILE`. Set the variables in every environment where you build your app.

## Build a signed app bundle

Before each release, increase the `versionCode` setting in your app module's
`lightbuild.yaml` file, and update `versionName` if needed. Google Play requires
a higher version code for each upload. For more information, see
[Version your app](https://developer.android.com/studio/publish/versioning).

To build the signed release app bundle, run:

    lightbuild build app:app-release.aab

Lightbuild writes the bundle to `app/build/app-release.aab`. To see where each
of the app module's targets writes its output, run
`lightbuild query app/... --output=files`.

## Upload your app to Google Play

Upload the signed app bundle to the Play Console. To test your app before you
release it to users, upload it to an internal testing track first. For more
information, see [Upload your app to the Play Console](https://developer.android.com/studio/publish/upload-bundle).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands)
- [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema)
- [Lightbuild CLI reference](https://developer.android.com/tools/agents/lightbuild/cli-reference)