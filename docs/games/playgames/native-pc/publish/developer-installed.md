---
title: https://developer.android.com/games/playgames/native-pc/publish/developer-installed
url: https://developer.android.com/games/playgames/native-pc/publish/developer-installed
source: md.txt
---

> Documentation index: https://developer.android.com/games/playgames/native-pc/llms.txt

This document shows you how to publish your game on Google Play Games on PC using your game installer.

With the Developer Installed flow, the game installer you provide must manage the installation, update, and uninstallation of the game.

## Before you begin

Integrate the [Google Play Games SDK](https://developer.android.com/games/playgames/native-pc/setup.md.txt) into your game. **Prepared to start
onboarding?** Reach out by email to
[google-play-games-pc@google.com](mailto:google-play-games-pc@google.com). The onboarding specialists
will assist you with the next steps.

> [!NOTE]
> **Note:** Most games should use [Play Managed Publishing](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation.md.txt). Installer Publishing is available by exception for games that need their own installer, and access is granted per package. Request access before your first upload by emailing [google-play-games-pc@google.com](mailto:google-play-games-pc@google.com). You can't switch between Installer Publishing and Play Managed Publishing after a Windows app bundle has been uploaded.

## Package your game as a WAB file

Google Play Games on PC requires your game's installer to be uploaded to
Google Play Console as a Windows app bundle (WAB) file. To create a WAB file,
​follow these steps:

1. Download the [Play publishing tool](https://developer.android.com/games/playgames/native-pc/downloads/playpublishingtool).
   You can run this tool on the Windows command line or PowerShell.

2. Create the Play publishing config file, with any name. For example,
   `play_publishing_config.xml` with the following format:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <play-publishing-config version="1.0">
     <application>
       <package-name>PACKAGE_NAME</package-name>
       <version-name>VERSION_NAME</version-name>
     </application>
     <installer requiresElevation=INSTALLER_REQUIRES_ELEVATION acceptsCommandLineArguments=ACCEPTS_COMMAND_LINE_ARGUMENTS>
       <path>INSTALLER_PATH</path>
       <installation-path-registry-location>
         <key-name>UNIQUE_REGISTRY_PATH</key-name>
         <value-name>InstallLocation</value-name>
       </installation-path-registry-location>
     </installer>
     <launcher requiresElevation=LAUNCHER_REQUIRES_ELEVATION>
       <launch-path-registry-location>
         <key-name>UNIQUE_REGISTRY_PATH</key-name>
         <value-name>InstallLocation</value-name>
       </launch-path-registry-location>
       <executable-invocation>
         <filename>RELATIVE_PATH_TO_LAUNCHER_EXE</filename>
         <arguments>LAUNCHER_ARGS_IF_ANY</arguments>
       </executable-invocation>
     </launcher>
     <uninstaller requiresElevation=UNINSTALLER_REQUIRES_ELEVATION>
       <uninstall-path-registry-location>
         <key-name>UNIQUE_REGISTRY_PATH</key-name>
         <value-name>UninstallString</value-name>
       </uninstall-path-registry-location>
     </uninstaller>
   </play-publishing-config>
   ```

   Replace the following:

   - `PACKAGE_NAME`: The package name for your game. This is the unique identifier that will be associated with your game on Google Play. For example, `com.yourcompany.yourgame`. The package name must adhere to the following rules:
     - It must have at least two segments (one or more dots).
     - Each segment must start with a letter.
     - All characters must be alphanumeric or an underscore (`[a-zA-Z0-9_]`).
   - `VERSION_NAME`: The game's version string. This can be an
     arbitrary string, but it must be unique across all uploaded WABs for
     your game. For example: `1.0`, `1.0.1-beta`, `2025.11.24`, `v1.rc1`.

     - `INSTALLER_REQUIRES_ELEVATION`: Indicates whether the
       installer executable needs to be run as Administrator to complete the
       installation process.

       - **"true"**: Run the executable as Administrator.

       > [!WARNING]
       > **Warning:** Displays a [UAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/) prompt for the gamer.

       - **"false"**: Run the executable as the current user.
     - `ACCEPTS_COMMAND_LINE_ARGUMENTS`: A boolean value that
       indicates whether the installer can accept command-line arguments to
       enable the auto-play feature. This is optional and the default value
       is false. For more information, see [Enabling Auto-Play](https://developer.android.com/games/playgames/native-pc/publish/developer-installed.md.txt#enable-auto-play).

     - `INSTALLER_PATH`: The path to your installer file
       within the WAB. This path can be either *absolute* or *relative* to the
       parent directory of the Play publishing config. For example,
       `path\to\test\installer`.
       Remember to use [authenticode and code signing](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022#authenticode-and-code-signing) to sign your game's
       installer executable.

     - `<installation-path-registry-location>`: The registry path that Google
       Play Games uses to detect whether the game is installed. Even if your
       game uses a custom launcher, this path must point to the game's unique
       registry key, not the launcher's registry key.

       > [!CAUTION]
       > **Important:** Don't point `<installation-path-registry-location>` to a shared launcher's registry key. If a shared launcher remains installed after the game is removed, Google Play Games will falsely detect the game as still installed. Always specify a game-specific registry key that is created upon game installation and deleted when the game client is uninstalled.

     - `UNIQUE_REGISTRY_PATH`: The Windows registry key path.
       This path must be provided relative to a registry hive such as
       [`HKEY_LOCAL_MACHINE`](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users) or `HKEY_CURRENT_USER`; don't include the
       hive name in the path string. For example, if your installer writes to
       `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`,
       specify only `Software\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`.
       Google Play Games on PC searches for this path in `HKEY_LOCAL_MACHINE`
       first and then `HKEY_CURRENT_USER`, using the first matching value it
       finds.

       > [!CAUTION]
       > **Caution:** Because Google Play Games on PC checks `HKEY_LOCAL_MACHINE` before `HKEY_CURRENT_USER` and stops at the first match, don't mix system-wide (`HKEY_LOCAL_MACHINE`) and per-user (`HKEY_CURRENT_USER`) installations across versions or across multiple titles that share a launcher registry key. If a stale path remains in `HKEY_LOCAL_MACHINE` after uninstallation or relocation to `HKEY_CURRENT_USER`, Google Play Games on PC reads the stale `HKEY_LOCAL_MACHINE` path and fails to verify or launch the game.

       The executable specified in `INSTALLER_PATH` must create these registry keys. Before installation completes, these registry-key and value-name pairs specified under `installation-path-registry-location`, `launch-path-registry-location`, and `uninstall-path-registry-location` must be created. While the example uses `InstallLocation` and `UninstallString`, you can specify any name in these `<value-name>` tags, as long as your installer creates corresponding registry entries for all three.
       Google Play Games on PC uses these values to launch and uninstall the
       game. If your game uses a launcher, the value in the registry entry
       specified by `launch-path-registry-location` must point to the launcher's
       directory (while `installation-path-registry-location` must point to the
       game's unique registry key, not the launcher's registry key).

       > [!IMPORTANT]
       > **Important:** Ensure the primary installer process remains active until all required registry keys are fully created and registered. Exiting prematurely will cause installation verification to fail.

       This path must be unique on the user's machine. For example: `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`.

       <br />

       If your game installer is a 32-bit application running on 64-bit
       Windows, Windows uses [registry redirection](https://learn.microsoft.com/en-us/windows/win32/winprog64/registry-redirector) to write registry
       entries under `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node`. For example, a
       write to
       `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`
       is redirected to
       `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`.
     - `LAUNCHER_REQUIRES_ELEVATION`: Indicates whether the
       launcher or game executable needs to be run as Administrator every time
       it is launched.

       - **"true"**: Run the executable as Administrator.

       > [!WARNING]
       > **Warning:** Displays a [UAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/) prompt for the gamer.

       - **"false"**: Run the executable as the current user.
     - `RELATIVE_PATH_TO_LAUNCHER_EXE`: The path to your
       launcher or game executable within the installation directory. This has
       to include your launcher or game executable filename. For example, if
       your launcher or game file is called mygame.exe and it is located under
       {INSTALL_DIR}\\Resources\\mygame.exe, you have to put
       Resources\\mygame.exe

     - `LAUNCHER_ARGS_IF_ANY`: Any command line arguments
       that need to be passed into your launcher or game.
       This entry is optional.

       - In case of multiple arguments associated with an executable, they need to be separated by a space.
       - The arguments need to be prepended with a '--' or '-', if that is required by the executable.
     - `UNINSTALLER_REQUIRES_ELEVATION`: Indicates whether the
       uninstaller executable needs to be run as Administrator to complete the
       uninstallation process.

       - **"true"**: Run the executable as Administrator.

       > [!WARNING]
       > **Warning:** Displays a [UAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/) prompt for the gamer.

       - **"false"**: Run the executable as the current user.

   #### Example Play publishing config file

   Consider a game called `MyGame`, with game installer
   `game_installer.exe`, game's launcher `launcher.exe`.
   The example also shows how to use CDATA.
   The following is what the `play_publishing_config.xml` will look
   like:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>

   <play-publishing-config version="1.0">
     <application>
       <!-- The package name for your game. -->
       <package-name>com.mycompany.mygame</package-name>
       <!-- The game's version string. -->
       <version-name>1.0.0</version-name>
     </application>
     <!-- If requiresElevation is "true", installer runs as Administrator
          and a UAC prompt is displayed. This is required for system-wide
          installs (e.g., to Program Files) or writing to HKLM. -->
     <!-- If acceptsCommandLineArguments is "true", the installer must
          be able to accept command-line arguments to enable the auto-play
          feature. -->
     <installer requiresElevation="true" acceptsCommandLineArguments="true">
       <!-- Path to your installer executable. -->
       <path>game_installer.exe</path>
       <!-- The registry location where the installer writes the installation path. -->
       <installation-path-registry-location>
         <!-- Registry key path (typically under HKLM or HKCU).
              game_installer.exe MUST create this key. -->
         <key-name>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MySystemWideUniqueKey</key-name>
         <!-- game_installer.exe, specified in <path>, creates the registry
              value called 'InstallLocation' within
              SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MySystemWideUniqueKey
              by the time it exits. -->
         <value-name>InstallLocation</value-name>
       </installation-path-registry-location>
     </installer>

     <!-- If requiresElevation is "true", launcher runs as Administrator
          and a UAC prompt is displayed on every game launch. -->
     <launcher requiresElevation="true">
       <!-- Specifies the registry location where Google Play Games reads the installation path
            in order to launch the game. -->
       <launch-path-registry-location >
         <!-- Registry key path (typically under HKLM or HKCU) where
              the launch path can be found. -->
         <key-name>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MySystemWideUniqueKey</key-name>
         <!-- Google Play Games reads the installation directory from this
              registry value, for example InstallLocation, to launch the game. -->
         <value-name>InstallLocation</value-name>
       </launch-path-registry-location>
       <executable-invocation>
         <!-- Game executable or launcher filename, relative to the
              directory path specified in the InstallLocation registry value. -->
         <filename>launcher.exe</filename>
         <!-- Optional arguments to pass to the executable.
              CDATA is used here to avoid issues with special characters
              like & or >. -->
         <arguments><![CDATA[arg1&arg2>arg3]]></arguments>
       </executable-invocation>
     </launcher>

     <!-- If requiresElevation is "true", uninstaller runs as
          Administrator and a UAC prompt is displayed for uninstall. -->
     <uninstaller requiresElevation="true">
       <!-- Registry key where Google Play Games finds the
            uninstallation command. -->
       <uninstall-path-registry-location>
         <!-- Registry key path (typically under HKLM or HKCU) where
              uninstall command can be found. -->
         <key-name>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MySystemWideUniqueKey</key-name>
         <!-- game_installer.exe also creates the registry value, for example, 'UninstallString'
              within SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\MySystemWideUniqueKey,
              containing the command Google Play Games executes to uninstall
              the game. -->
         <value-name>UninstallString</value-name>
       </uninstall-path-registry-location>
     </uninstaller>
   </play-publishing-config>
   ```
3. Run the Play publishing tool on the Windows command line or Powershell.

   ```
   playpublishingtool.exe build-installer-bundle --input=PLAY_PUBLISHING_CONFIG_PATH --output=WAB_OUTPUT_PATH
   ```

   To overwrite an existing WAB file with the same name, use the
   `--force` argument.

   ```
   playpublishingtool.exe build-installer-bundle --input=PLAY_PUBLISHING_CONFIG_PATH --output=WAB_OUTPUT_PATH --force
   ```

   Replace the following:
   - `PLAY_PUBLISHING_CONFIG_PATH`: The path to the Play publishing config. For example, `path\to\play_publishing_config.xml`.
   - `WAB_OUTPUT_PATH`: The path to the WAB file. For example, `path\to\output_bundle.wab`.

   > [!IMPORTANT]
   > **Important:** The WAB filename in the `--output` must have a `.wab` extension.

   > [!NOTE]
   > **Note:** The `--input` and `--output` paths can be absolute or relative with respect to the current working directory.

   #### How to use Play publishing tool

   Consider that you have the Play publishing tool binary
   `playpublishingtool.exe`, Play publishing config
   `play_publishing_config.xml` and your game installer
   `game_installer.exe` in the current working directory.

   Your current working directory should look like this:

   ```none
   .\
   ├── game_installer.exe
   ├── play_publishing_config.xml
   ├── playpublishingtool.exe
   ```

   To create a WAB with the name, say, `installer_bundle.wab` in the same
   directory, the command would look like:

   ```
   playpublishingtool.exe build-installer-bundle --input=play_publishing_config.xml --output=installer_bundle.wab
   ```

   With the `--force` argument, the command would look like:

   ```
   playpublishingtool.exe build-installer-bundle --input=play_publishing_config.xml --output=installer_bundle.wab --force
   ```

   On success, you should see output similar to the following:

   ```none
   Successfully built the installer bundle at installer_bundle.wab
   ```

   Find the WAB file in the folder:

   ```none
     .\
     ├── game_installer.exe
     ├── installer_bundle.wab
     ├── play_publishing_config.xml
     ├── playpublishingtool.exe
   ```

   #### Enabling Auto-Play upon installation of your PC Native Games (Optional)

   Google Play Games on PC lets you enable an "auto-play" feature, which automatically launches your game immediately after the installation process completes. This feature provides a seamless user experience by transitioning the player directly into the game, fully authenticated within the Google Play Games on PC ecosystem.

   **How it works**

   When you enable the **feature**, Google Play Games on PC will pass a session token to your third-party (3P) installer process using command-line arguments. Your installer is then responsible for extracting this token and using it to launch the game executable in an authenticated context.

   **Prerequisites**

   To use this feature, your 3P installer must be capable of handling command-line arguments.

   **Implementation Steps**
   1. Enable Auto-Play in Play Publishing Config

      To opt-in to this feature, add the `acceptsCommandLineArguments` attribute to the `<installer>` element in your `play_publishing_config.xml`.

      Example of excerpt from the `play_publishing_config.xml` contents:

      ```xml
           <installer requiresElevation="true" acceptsCommandLineArguments="true">
              <path>path/to/installer.exe</path>
              <installation-path-registry-location>
                <key-name>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\key</key-name>
                <value-name>InstallPath</value-name>
              </installation-path-registry-location>
           </installer>
      ```
      - Attribute: `acceptsCommandLineArguments`
      - Type: `Boolean`
      - Default: `false`
      - Behavior: When you set it to true, GPG will append the session token to the command-line arguments when executing your installer.
   2. Handle the Session Token in Your Installer

      When your installer is launched by the GPG client, it will receive the session token as a command-line argument.
      - Argument Format: `--g_session_token=<TOKEN>`

      What you must do:
      - Extraction: Your installer must parse the command-line arguments to retrieve the token string.
      - Propagation: If your installation flow involves launching a secondary launcher or game process, your installer is responsible for securely passing the session token to the final game process that uses the SDK.
      - Launch: Use the provided session token to start the game executable. This ensures the game runs within an authenticated GPG context. Otherwise, [InitializeSDK](https://developer.android.com/games/playgames/native-pc/setup.md.txt#step-4) will fail and your player will need to restart your game.
   3. Error Handling and Fallbacks

      - Token Retrieval: If, for any reason, GPG cannot generate or pass a session token (e.g., token generation failure), the installation process will still proceed. However, your installer will be launched without the `--g_session_token` argument.
      - Robustness: Your installer should be designed to handle scenarios where the session token is absent. In such cases, the installer should proceed with a standard installation; you shouldn't trigger automatic game launch as [InitializeSDK](https://developer.android.com/games/playgames/native-pc/setup.md.txt#step-4) will fail anyway.
      - Installer Errors: You are responsible for the robustness and error handling of your installer and the game launch sequence it initiates. GPG does not have control over processes that occur within the installer after it has been launched.

## Publish the game using Play Console

After you create the WAB file for your game, upload it to
Play Console and configure its settings and requirements. Open
Play Console, select your app, and follow these steps:

### Enable Windows native distribution

1. In Play Console, go to **Test and release \> Advanced settings
   \> Form factors and platforms**.
2. In the **Windows** section, click **Add Windows**.

> [!NOTE]
> **Note:** If **Add Windows** is disabled because the Android **Google Play Games on PC** form factor is opted in, select **Opt out** for **Google Play Games on PC** on Android and then select **Remove** first. If the **Windows** option isn't visible under **Form factors and platforms** , your account needs to complete onboarding first. **Prepared to start onboarding?** Reach out by email to [google-play-games-pc@google.com](mailto:google-play-games-pc@google.com). The onboarding specialists will assist you with the next steps.

### Configure PC requirements, store listing assets, and review policy

1. Set PC hardware requirements (RAM, GPU, and storage) and upload **Google Play Games on PC** store listing assets (screenshots and an optional video).
2. Return to **Test and release \> Advanced settings \> Form factors and
   platforms** and click **Agree to review policy** to confirm compliance with the [Google Play Games on PC quality guidelines](https://support.google.com/googleplay/topic/13019131).

### Test your game on the internal testing track

1. Go to **Test and release \> Testing \> Internal testing** and select the **Google Play Games on PC** track.
2. Select up to 100 testers (you can configure a separate tester list from Android), upload your Windows App Bundle (`.wab`), and click **Save and
   publish**.
3. Share both the Play Console opt-in web link (`https://play.google.com/apps/internaltest/...`) and the client deep link `googleplaygames://deeplink/details?id=PACKAGE_NAME` (replacing `PACKAGE_NAME` with your app's package name) with your testers. Testers must first open the opt-in web link and click **Accept invite** , and then paste `googleplaygames://deeplink/details?id=PACKAGE_NAME` into a Windows browser address bar or `Win+R` to open the game's details page in the Google Play Games on PC client and install the build.

> [!NOTE]
> **Note:** During internal testing, the **Install on Windows** button doesn't appear on the Google Play web store, so testers must use the `googleplaygames://deeplink/details?id=PACKAGE_NAME` deep link to install the build. Closed and open testing tracks are unavailable on Windows (only Internal testing is supported).

### Publish to production

1. Go to **Test and release \> Production** and select the **Google Play Games on PC** track.
2. Select your target countries (which must match or be a subset of your Android country targeting).
3. Create a new release or promote your internal test release, and submit your release for review. Reviews take up to 7 days.
4. Use **Managed publishing** on the **Publishing overview** page to control when your approved release goes live.

> [!NOTE]
> **Note:** A package serves either the emulated Android build or the native PC build on Windows, so publishing a native PC build replaces the emulated version for existing PC players.