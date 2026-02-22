---
title: https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation
url: https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation
source: md.txt
---

This document shows you how to publish your game on Google Play Games on PC using Play Managed Installation.

With Play Managed Installation, Google Play manages the installation, update, and uninstallation of the game using the game files and metadata you provide in a Windows app bundle (WAB) file.

## Before you begin

Integrate the [Google Play Games SDK](https://developer.android.com/games/playgames/native-pc/setup) into your game.

## Package your game as a WAB file

To create a Play Managed Installation WAB file, follow these steps:

1. Download the [Play publishing tool](https://developer.android.com/games/playgames/native-pc/downloads/playpublishingtool).
   You can run this tool on the Windows command line or Powershell.

2. Create the Play publishing config file, with any name. For example,
   `play_publishing_config.xml` with the following format:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <play-publishing-config version="1.0">
     <!-- Application metadata: This section contains basic information about your game. -->
     <application>
       <package-name>PACKAGE_NAME</package-name>
       <version-name>VERSION_NAME</version-name>
     </application>

     <!-- Game files: This section specifies which game files to include in the bundle and how to treat them. -->
     <game-files>
       <file-set>
         <root-folder-path>PATH_TO_ROOT_FOLDER</root-folder-path>
         <!-- absolute or relative to the parent directory of the config xml -->
         <!-- Exclusions: A list of files or folders to exclude from the bundle.
              This is useful for removing development files, temporary data, or redundant assets. -->
         <exclusions>
           <file-path>REGEX_PATTERN_OF_EXCLUDED_FILES</file-path>
           <file-path>PATH_TO_BE_EXCLUDED</file-path>
         </exclusions>

         <!-- File attributes: Define special handling for certain files during installation and updates. -->
         <file-attribute value=FILE_ATTRIBUTE_VALUE>
           <file-path>PATH_TO_FILE</file-path>
           <file-path>REGEX_PATTERN_OF_FILE_ATTRIBUTE_FILES</file-path>
         </file-attribute>
       </file-set>
     </game-files>

     <!-- This file represents the startup process for this game. Google Play Games for PC should start
         this process when user clicks on "Play" on this game. -->
     <launch-command>
       <path>PATH_TO_LAUNCH_FILE</path>
       <arguments>ARGUMENTS</arguments>
     </launch-command>

     <!-- Lifecycle operations: Custom actions to be performed during the game's installation and uninstallation. -->
     <lifecycle-operations>
       <!-- Install operations: These actions run when the game is installed. 'requiresElevation="true"'
           will trigger a UAC prompt for administrator rights. There are three types of install
           operations that can be specified. An instance of each is listed below. -->
       <install-operation requiresElevation=INSTALL_OPERATION_REQUIRES_ELEVATION>
         <operation-identifier>OPERATION_IDENTIFIER_STRING</operation-identifier>
         <execute-file>
           <path>PATH_TO_INSTALL_EXECUTE_FILE</path>
           <arguments>ARGUMENTS</arguments>
         </execute-file>
       </install-operation>

       <install-operation requiresElevation=INSTALL_OPERATION_REQUIRES_ELEVATION>
         <operation-identifier>OPERATION_IDENTIFIER_STRING</operation-identifier>
         <update-registry baseKey=BASE_KEY>
           <sub-key>SUB_KEY_PATH</sub-key>
           <value-name>VALUE_NAME</value-name>
           <value type=REGISTRY_VALUE_TYPE>VALUE_TEXT</value>
         </update-registry>
       </install-operation>

       <!-- Uninstall operations: These actions run before the game is uninstalled. -->
       <uninstall-operation requiresElevation=UNINSTALL_OPERATION_REQUIRES_ELEVATION>
         <execute-file>
           <path>PATH_TO_UNINSTALL_EXECUTE_FILE</path>
           <arguments>ARGUMENTS</arguments>
         </execute-file>
       </uninstall-operation>
     </lifecycle-operations>
   </play-publishing-config>
   ```

   Replace the following:

   - `PACKAGE_NAME`: The package name for your game. This is the unique identifier that will be associated with your game on Google Play. For example, `com.yourcompany.yourgame`. The package name must adhere to the following rules:
     - It must have at least two segments (one or more dots).
     - Each segment must start with a letter.
     - All characters must be alphanumeric or an underscore (`[a-zA-Z0-9_]`).
   - `VERSION_NAME`: The game's version string. This can be an arbitrary string, but it must be unique across all uploaded WABs for your game. For example: `1.0`, `1.0.1-beta`, `2025.11.24`, `v1.rc1`.
   - `PATH_TO_ROOT_FOLDER`: The path to the root folder
     containing your game files. All files in this folder, except those mentioned in exclusions, are added to the bundle. This path can be *absolute* or *relative* to the directory
     containing the `play_publishing_config.xml` file.

     > [!NOTE]
     > **Note:** Except for `PATH_TO_ROOT_FOLDER`, all file paths specified in this XML configuration can be relative to `PATH_TO_ROOT_FOLDER` or absolute paths.

   - `exclusions`: (Optional) Specifies file paths or patterns
     for files within `PATH_TO_ROOT_FOLDER` to exclude from
     the bundle. You can include multiple `file-path` elements within the `exclusions` element. A path can be represented in one of two ways:

     - **As a file path**: Path to the file to exclude.
     - **As a regex string** : All files that match the regular expression string are excluded from the bundle. Use [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
   - `file-attribute`: (Optional) Defines attributes for
     specific files or files matching a regular expression pattern.

     - `FILE_ATTRIBUTE_VALUE`: Can be one of the following:
       - `SKIP_UPDATE`: During an update, this attribute tells the system to copy the file only if it's not already present, preserving any changes to an existing file.
       - `MODIFIED_ON_DEVICE`: Use this for files that must be updated, but could be modified on the device after installation. The system downloads the full new file and overwrites the installed version during an update. If this file is different from the installed version during installation integrity checks, the installation is not considered corrupted.
     - `file-path`: Identifies files for this attribute. You can include multiple `file-path` elements within each `file-attribute` element. Each path can be represented in one of two ways:
       - **As a file path**: Path to the file to associate this attribute with.
       - **As a regex string** : All files that match the regular expression string are associated with the attribute value. Use [RE2 syntax](https://github.com/google/re2/wiki/Syntax).
   - `PATH_TO_LAUNCH_FILE`: Path to the executable file used to
     launch the game.

   - `ARGUMENTS`: (Optional) Command-line arguments. The `<arguments>`
     element is used to pass arguments to an executable file specified in
     `<launch-command>`, `<install-operation>`, or `<uninstall-operation>`.
     Each use of the `<arguments>` element applies only to the executable it is
     defined alongside, allowing you to specify different arguments for
     different executables.

     - If an executable has multiple arguments, separate them with a space.
     - Prepend arguments with `--` or `-` if the executable requires it. Example:

       ```xml
       <arguments>--package_name --version_name</arguments>
       ```
   - `lifecycle-operations`: (Optional) Custom actions to
     perform during game installation or uninstallation.

     - `install-operation`: An action to run when the game is installed. You can specify two types of install operations: `execute-file` and `update-registry`.
     - `uninstall-operation`: An action to run before the game is uninstalled. `update-registry` operations are automatically reverted during uninstallation.
     - `INSTALL_OPERATION_REQUIRES_ELEVATION`: Indicates whether
       the install operation needs to run with administrator privileges.

       - **"true"**: Run as Administrator.

       > [!WARNING]
       > **Warning:** Displays a [UAC prompt](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/) for the gamer.

       - **"false"**: Run as the current user. This is the default if unspecified.
     - `UNINSTALL_OPERATION_REQUIRES_ELEVATION`: Indicates whether
       the uninstall operation needs to run with administrator privileges.

       - **"true"**: Run as Administrator.

       > [!WARNING]
       > **Warning:** Displays a [UAC prompt](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/) for the gamer.

       - **"false"**: Run as the current user. This is the default if unspecified.
     - `operation-identifier`: A unique string to identify an
       `install-operation`.

     - `execute-file`: Runs an executable file.

       - `PATH_TO_INSTALL_EXECUTE_FILE`: Path to an executable to run during installation.
       - `PATH_TO_UNINSTALL_EXECUTE_FILE`: Path to an executable to run before uninstallation.
     - `update-registry`: Creates or updates a Windows registry entry.

       - `BASE_KEY`: Defines the root key to be used in the Windows registry. Accepted values: `HKEY_CLASSES_ROOT`, `HKEY_CURRENT_CONFIG`, `HKEY_CURRENT_USER`, `HKEY_LOCAL_MACHINE`, `HKEY_PERFORMANCE_DATA`, and `HKEY_USERS`. When performing an `update-registry` operation, set `requiresElevation="true"` on the parent `install-operation` based on the `baseKey` used:
         - **`HKEY_LOCAL_MACHINE` or `HKEY_CURRENT_CONFIG`** : Set `requiresElevation="true"`.
         - **`HKEY_CURRENT_USER`** : `requiresElevation="true"` is not needed.
         - **`HKEY_CLASSES_ROOT`** : Set `requiresElevation="true"` only if writing to machine-wide sections; it is not required for user-specific sections.
         - **`HKEY_USERS`** : Contains profiles for all users. Set `requiresElevation="true"` when modifying profiles other than the current user's (e.g., other users or `.DEFAULT`).
       - `SUB_KEY_PATH`: This represents the path to a specific key within the Windows Registry, nested under the main `baseKey`.
       - `VALUE_NAME`: This specifies the name of the data entry you want to modify within the designated sub-key.
       - `REGISTRY_VALUE_TYPE`: This attribute specifies the data type of the value being written to the registry. Supported values are `STRING` for a string or `DWORD` for a 32-bit number.
       - `VALUE_TEXT`: Data to be stored in the registry key.

   > [!NOTE]
   > **Note:** To include blocks of text with special characters that shouldn't be parsed as XML markup, use a CDATA section. For example:
   >
   > ```xml
   > <file-path><![CDATA[file path with special characters <>]]></file-path>
   > ```

   > [!NOTE]
   > **Note:** Verify that any game binaries you provide are targeted to run on either x86 or x64 architectures. Binaries for other architectures are not supported.

   > [!IMPORTANT]
   > **Important: Regular Expressions for File Paths:**
   >
   > When using regular expressions to specify file paths (For example, for
   > exclusions or attributes), it's crucial to use **forward slashes (/)** as
   > directory separators. This is because the tool internally normalizes all
   > file paths to use forward slashes, regardless of your operating system.
   >
   > **Backward slashes (\\\\)** should *only* be used for their standard
   > purpose in regular expressions: escaping special characters.
   >
   > Example: To exclude log files like `test_failed1.log`,
   > `test_failed2.log` within a `testing`
   > directory:
   >
   > **Correct:** `testing/test_failed\d\.log`  
   >
   > / is used for the directory.  
   >
   > \\d matches any digit.  
   >
   > \\. matches a literal dot.
   >
   > **Incorrect:** `testing\\test_failed\d\.log`  
   >
   > Using \\\\ as a path separator here will conflict with RE2's
   > interpretation of \\\\t and \\\\d as escape sequences,
   > leading to unexpected behavior.
   >
   > For more examples, see [How to use regular expressions](https://developer.android.com/games/playgames/native-pc/publish/play-managed-installation#regex-examples).

   #### How to use regular expressions

   You can use RE2 syntax regular expressions in `file-path`
   tags to apply exclusions or file attributes to a group of files. Remember to
   use forward slashes `/` for directory separators, and to escape
   special regular expression characters with a backslash `\`. For
   example, use `\.` to match a literal dot `.`, or
   `\d` to match a digit.

   Here are some common examples:
   - **Match all files with a specific extension (For example, .log) in any directory**

     Use `.*\.log` to match any path ending with
     `.log`, like `game.log` or
     `logs/errors.log`.

     ```xml
     <file-path>.*\.log</file-path>
     ```
   - **Match all files and subdirectories within a specific folder (For example, 'temp')**

     Use `temp/.*` to match all paths that start with
     `temp/`, like `temp/data.txt` or
     `temp/saves/file.sav`.

     ```xml
     <file-path>temp/.*</file-path>
     ```
   - **Match files matching a pattern in a specific folder**

     Use `assets/level\d\.dat` to match
     `assets/level1.dat`, `assets/level2.dat` but
     not `assets/other.dat`.

     ```xml
     <file-path>assets/level\d\.dat</file-path>
     ```
   - **Match a folder name when it appears anywhere in the path**

     Use `.*/cache/.*` to match files under any directory named `cache`, like `game/cache/file.txt` or `temp/cache/other.log`.

     ```xml
     <file-path>.*/cache/.*</file-path>
     ```
   - **Match files with one of several extensions (For example, .ini, .cfg, .sav)**

     Use `.*\.(ini|cfg|sav)` to match any file ending in
     `.ini`, `.cfg`, or `.sav`, like `settings.ini`,
     `config.cfg`, or `saves/slot1.sav`.

     ```xml
     <file-path>.*\.(ini|cfg|sav)</file-path>
     ```
   - **Match files with a specific extension in specific directories (For example, .ogg in music/ or sfx/)**

     Use `(music|sfx)/.*\.ogg` to match any
     `.ogg` files that are located under either the
     `music/` or `sfx/` directories, but not
     elsewhere. Matches `music/level1.ogg` or
     `sfx/explosion.ogg`, but not `voice/intro.ogg`.

     ```xml
     <file-path>(music|sfx)/.*\.ogg</file-path>
     ```

   #### Example Play publishing config file

   Here is an example `play_publishing_config.xml` for a game
   called `TestGame`:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <play-publishing-config version="1.0">
     <application>
       <package-name>com.test.package</package-name>
       <version-name>1.0</version-name>
     </application>

     <game-files>
       <file-set>
         <root-folder-path>C:\Users\Username\game-files</root-folder-path>
         <exclusions>
           <file-path>mock_game\d\.exe</file-path> <!-- exclude files using a regex -->
           <file-path>deprecated_graphics</file-path> <!-- exclude a folder -->
           <file-path>.*\.log</file-path> <!-- recursively exclude all files with .log extension -->
         </exclusions>

         <file-attribute value="SKIP_UPDATE">
           <file-path>settings.ini</file-path>
         </file-attribute>

         <file-attribute value="MODIFIED_ON_DEVICE">
           <file-path>game_assets\d\.zip</file-path> <!-- define the path using regex -->
         </file-attribute>
       </file-set>
     </game-files>

     <launch-command>
       <path>launcher_test_game.exe</path>
       <arguments>--launch-arg</arguments> <!-- optional -->
     </launch-command>

     <lifecycle-operations>
       <install-operation requiresElevation="true">
         <operation-identifier>elevated-execute-file</operation-identifier>
         <execute-file>
           <path>install_file.exe</path>
           <arguments>--arg</arguments> <!-- optional -->
         </execute-file>
       </install-operation>

       <install-operation requiresElevation="true">
         <operation-identifier>elevated-update-registry</operation-identifier>
         <update-registry baseKey="HKEY_LOCAL_MACHINE">
           <sub-key>SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\TestGame</sub-key>
           <value-name>InstallLocation</value-name>
           <value type="STRING">C:\Program Files\TestGame</value>
         </update-registry>
       </install-operation>

       <uninstall-operation requiresElevation="true">
         <execute-file>
           <path>uninstall.exe</path>
           <arguments>--test-arg</arguments> <!-- optional -->
         </execute-file>
       </uninstall-operation>
     </lifecycle-operations>
   </play-publishing-config>
   ```
3. Run the Play publishing tool on the Windows command line or Powershell,
   using the `build-bundle` command:

   ```
   playpublishingtool.exe build-bundle --input=PLAY_PUBLISHING_CONFIG_PATH --output=WAB_OUTPUT_PATH
   ```

   To overwrite an existing WAB file with the same name, use the
   `--force` argument.

   ```
   playpublishingtool.exe build-bundle --input=PLAY_PUBLISHING_CONFIG_PATH --output=WAB_OUTPUT_PATH --force
   ```

   Replace the following:
   - `PLAY_PUBLISHING_CONFIG_PATH`: The path to the Play publishing config. For example, `path\to\play_publishing_config.xml`.
   - `WAB_OUTPUT_PATH`: The path to the WAB file. For example, `path\to\output_bundle.wab`.

   > [!IMPORTANT]
   > **Important:** The WAB filename in the `--output` must have a `.wab` extension.

   > [!NOTE]
   > **Note:** The `--input` and `--output` paths can be absolute or relative with respect to the current working directory.

   #### How to use Play publishing tool

   If you have `playpublishingtool.exe`,
   `play_publishing_config.xml`, and your game files in
   `game_files/` in the current working directory:

   ```none
   .\
   ├── game_files/
   ├── play_publishing_config.xml
   ├── playpublishingtool.exe
   ```

   To create `pmi_bundle.wab` in the same directory, run:

   ```
   playpublishingtool.exe build-bundle --input=play_publishing_config.xml --output=pmi_bundle.wab
   ```

   While the tool builds the bundle, you will see a progress bar on the terminal:

   ```none
   Building bundle: [====       ] 40%
   ```

   On success, you should see output similar to the following:

   ```none
   Building bundle: [===========] 100%
   Successfully built the managed install bundle at pmi_bundle.wab
   ```

   Find the WAB file in the folder:

   ```none
     .\
     ├── game_files/
     ├── pmi_bundle.wab
     ├── play_publishing_config.xml
     ├── playpublishingtool.exe
   ```