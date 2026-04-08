---
title: https://developer.android.com/games/playgames/native-pc/publish/developer-installed
url: https://developer.android.com/games/playgames/native-pc/publish/developer-installed
source: md.txt
---

This document shows you how to publish your game on Google Play Games on PC using your game installer.

With the Developer Installed flow, the game installer you provide must manage the installation, update, and uninstallation of the game.

## Before you begin

Integrate the [Google Play Games SDK](https://developer.android.com/games/playgames/native-pc/setup) into your game.

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
     <installer requiresElevation=INSTALLER_REQUIRES_ELEVATION>
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
     - `INSTALLER_PATH`: The path to your installer file
       within the WAB. This path can be either *absolute* or *relative* to the
       parent directory of the Play publishing config. For example,
       `path\to\test\installer`.
       Remember to use [authenticode and code signing](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-and-authenticode?view=vs-2022#authenticode-and-code-signing) to sign your game's
       installer executable.

     - `UNIQUE_REGISTRY_PATH`: The Windows registry key path.
       This path must be provided relative to a registry hive such as
       [`HKEY_LOCAL_MACHINE`](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users) or `HKEY_CURRENT_USER`; don't include the
       hive name in the path string. For example, if your installer writes to
       `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`,
       specify only `Software\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`.
       Google Play Games on PC searches for this path under multiple hives to locate the values required for launch and
       uninstallation.

       The executable specified in `INSTALLER_PATH` must create these registry keys. Before installation completes, these registry-key and value-name pairs specified under `installation-path-registry-location`, `launch-path-registry-location`, and `uninstall-path-registry-location` must be created. While the example uses `InstallLocation` and `UninstallString`, you can specify any name in these `<value-name>` tags, as long as your installer creates corresponding registry entries for all three.
       Google Play Games on PC uses these values to launch and uninstall the
       game. If your game uses a launcher, then this path must point
       to the registry key containing installation information for the
       launcher, and the value in the registry entry specified by `launch-path-registry-location` must point to the launcher's
       directory.

       This path must be unique on the user's machine. For example:
       `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\YourUniqueName`.

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
     <installer requiresElevation="true">
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

## Publish the game using Play Console

After you successfully create the WAB for your game, upload it to
Play Console and manage its settings and requirements. Follow the
steps to publish your game:

> [!NOTE]
> **Note:** For all the steps, open the [Play Console](https://play.google.com/console) and select your app first. Then proceed with the mentioned steps for that particular app.

### Add the Google Play Games on PC form factor

This step is only required the first time you publish a game.

1. In the Play Console on the left menu, select **Test and
   release \> Setup \> Advanced settings** ([direct link](https://play.google.com/console/u/0/developers/app/advanced-distribution)).
2. Go to the **Form factors** tab and add `Google Play Games on PC` from the
   **+ Add form factor** drop-down.

   > [!NOTE]
   > **Note:** If you cannot access the Google Play Games on PC in the form factors tab, you can reach out to our Play partners to allowlist your account.

3. Click the **Manage** button corresponding to the **Google Play Games on PC**
   form factor on the right-hand side.

4. Select the option **Use a dedicated track for your Windows app bundle game**.

5. Click **Save** and then **Save** again on the confirmation dialog.

### Turn on Managed Publishing

To turn on Managed publishing, follow these steps.

1. On the **Publishing Overview** page, in the **Managed Publishing** section, click **Turn on Managed Publishing**.
2. A dialog will appear. Switch to **Managed publishing on** for the track.
3. Click **Save**.

### Upload the WAB file

To upload the WAB file, follow these steps:

1. In the Play Console on the left menu, select **Test and release \> Advanced settings** ([direct link](https://play.google.com/console/u/0/developers/app/advanced-distribution)).
2. In the **Advanced settings** page, click **Form factors** tab.
3. In the **Form factors** tab, click **+ Add form factor** and select **Google Play Games on PC** to add.
4. In the **Google Play Games on PC** section, click **Manage**.
5. Select **Use a dedicated track for your Windows app bundle game**.
6. Click **Save**.
7. In the Play Console on the left menu, select **Test and release \> Production** ([direct link](https://play.google.com/console/u/0/developers/app/tracks/production)).
8. In the **Production** page, select **Google Play Games on PC (Windows) only** from the form factor drop-down.
9. In the **Windows app bundle** tab, click **Edit** and upload the WAB file.

### Configure the Windows PC requirements

To configure the Windows PC requirements:

1. In the Play Console on the left menu, select **Grow users \> Store presence \> Store settings** ([direct link](https://play.google.com/console/u/0/developers/app/store-s)).
2. In the **PC requirements** section, click the **Edit** button on the right-hand side.
3. Update the fields and click **Save**.

### Configure the in-app purchase graphic

This is an optional step. To configure the in-app purchase graphic:

1. In the Play Console on the left menu, select **Grow users \> Store presence \> Store listings** ([direct link](https://play.google.com/console/u/0/developers/app/main-store-listing)).
2. In the **Default store listing** section in the **Listings** tab, click the **-\>** (arrow) button on the right-hand side. This will take you to the **Default store listing** page.
3. Navigate to the **Google Play Games on PC** section and upload the image at **Google Play Games on PC (Windows) in-app purchase graphic**.
4. Click **Save**.

### Send changes for review

> [!NOTE]
> **Note:** You can use **Managed publishing** to have more control over when your changes are published. Managed publishing is switched off by default, which means your changes will be published as soon as they are approved. To turn on Managed publishing, go to the [Publishing overview](https://play.google.com/console/u/0/developers/app/publishing) page and click the **Turn on managed publishing** button on the right-hand side.

1. In the Play Console on the left menu, select **Publishing overview**.
2. In the **Changes not yet sent for review** section, click **Send changes for review**.

When the Review team has approved your changes, your game will be discoverable on
Google Play.