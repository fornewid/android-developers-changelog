---
title: https://developer.android.com/studio/run/rundebugconfig
url: https://developer.android.com/studio/run/rundebugconfig
source: md.txt
---

When you run, debug, or test your code, Android Studio uses a run/debug
configuration to determine how to perform the operation. Typically, the
[initially-created configuration](https://developer.android.com/studio/run/rundebugconfig#initially-created-config) is sufficient to run or
debug an app. However, you can modify and create new configurations, and modify the configuration
templates to suit your development process as described on this page.

For more information, also see the following IntelliJ documentation:

- [Run/Debug Configurations](https://www.jetbrains.com/help/idea/2025.3/run-debug-configurations.html)

## About run/debug configurations

Run/debug configurations specify details such as
app installation, launch, and test options.
You can define a configuration for one-time use, or save it for future use.
After you save it, you can select the configuration from the
**Select Run/Debug Configuration** drop-down list within the [toolbar](https://developer.android.com/studio/intro#user-interface).
Android Studio saves configurations as part of the project.

### Initially-created run/debug configuration


When you first create a project, Android Studio creates a run/debug
configuration for the main activity based on the [Android App template](https://developer.android.com/studio/run/rundebugconfig#android-application). To run or debug
your project, you must always have at least one run/debug configuration defined.
For this reason, we recommend that you don't delete the initially-created configuration.

### Project scope and version control


Run/debug configurations and template changes apply to the current project only.
You can share a run/debug configuration (but not a template) through your
version control system. For more information about how to share a configuration,
see [Name and Share Configuration Options](https://developer.android.com/studio/run/rundebugconfig#nameshare).

## Open the Run/Debug Configurations dialog


To open the Run/Debug Configurations dialog,
select **Run** \> **Edit Configurations** . The
**Run/Debug Configurations** dialog appears, as shown in figure
1.


![](https://developer.android.com/static/studio/images/rdc-rundebugconfg_2-3_2x.png)

**Figure 1** . The **Run/Debug Configurations** dialog


The left panel of the dialog groups your defined configurations by template type, and
allows you to [edit configuration templates](https://developer.android.com/studio/run/rundebugconfig#editing-template) at the bottom.
You can edit the selected configuration in the right panel.
Resize the dialog to see any hidden items.


In this dialog, you can:

- [Create new run/debug configurations](https://developer.android.com/studio/run/rundebugconfig#creating).
- [Edit run/debug configurations.](https://developer.android.com/studio/run/rundebugconfig#editing)
- [Edit configuration templates.](https://developer.android.com/studio/run/rundebugconfig#editing-template)
- [Sort and group configurations.](https://developer.android.com/studio/run/rundebugconfig#sorting)

## Create a new run/debug configuration


You can define new run/debug configurations from the **Run/Debug
Configurations** dialog, the **Project** window, or the Code
Editor. The new configuration must be based on a [configuration template](https://developer.android.com/studio/run/rundebugconfig#config-templates).


The Run/Debug Configurations dialog displays your run/debug configurations and the available
configuration templates. You can start a new configuration directly from a template, or from a
copy of another configuration. You can then change the field values as needed.


Alternatively, you can right-click an item in the **Project**
window to automatically create a configuration specific to that item. For
example, if you want to run a particular activity, you can right-click the
activity Java file and select **Run** . Depending on the item,
Android Studio uses an [Android App](https://developer.android.com/studio/run/rundebugconfig#android-application),
[Android Instrumented Tests](https://developer.android.com/studio/run/rundebugconfig#android-tests), or [JUnit](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-junit.html)
configuration template to create the configuration.


In the Code Editor, you can easily create a test and run/debug configuration for
a class or method, and then execute it.


When you create a configuration outside of the **Run/Debug
Configurations** dialog, the configuration is temporary
unless you save it. By default, you can have up to five temporary configurations
in the project before Android Studio starts to remove them. To change this
default, open Android Studio settings, and change
**Advanced Settings \> Run/Debug \> Temporary configurations limit** .
For more information about temporary configurations, see
[Creating and Saving Temporary Run/Debug Configurations](https://www.jetbrains.com/help/idea/2025.3/creating-and-saving-temporary-run-debug-configurations.html).

### Start a configuration based on a template


To define a run/debug configuration based on a template, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Click **Add New Configuration** ![](https://developer.android.com/static/studio/images/rdc-iaddnewconfig_2-1.png).
3. Select a [configuration template](https://developer.android.com/studio/run/rundebugconfig#config-templates).
4. Type a name in the **Name** field.
5. Modify the configuration, as needed.
6. Be sure to correct any errors displayed at the bottom of the dialog.
7. Click **Apply** or **OK**.

### Start a configuration from a copy


To define a run/debug configuration starting from a copy of another
configuration, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Select an existing run/debug configuration in the left pane.
3. Click **Copy Configuration** ![](https://developer.android.com/static/studio/images/rdc-icopyconfig_2-1.png).
4. Type a name in the **Name** field.
5. Modify the configuration, as needed.
6. Be sure to correct any errors displayed at the bottom of the dialog.
7. Click **Apply** or **OK**.

### Define a configuration for an item in
the project


Android Studio can create a run/debug configuration for some items
displayed in the **Project** window. The configuration is based on
a configuration template, as follows:

- Activity Java file: The [Android App](https://developer.android.com/studio/run/rundebugconfig#android-application) template.
- Package: [Android Instrumented Tests](https://developer.android.com/studio/run/rundebugconfig#android-tests) or [Android JUnit](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-junit.html) template, depending on your [source set](https://developer.android.com/studio/build/build-variants#sourcesets). If you select an [instrumented test](https://developer.android.com/training/testing/unit-testing), then it uses the Android Instrumented Tests template. If you select a [local unit test](https://developer.android.com/training/testing/unit-testing), then it uses the Android JUnit template. For a local unit test, you can optionally run with code coverage. For more information, see [Code
  Coverage](https://www.jetbrains.com/help/idea/2025.3/code-coverage.html).


To create a run/debug configuration for an item in your project, follow these steps:

1. Open a project in [Android
   or Project view](https://developer.android.com/studio/projects#ProjectFiles).
2. In the **Project** window, right-click a testable item and select either **Run <var translate="no">filename</var>** or **Debug <var translate="no">filename</var>**. Android Studio creates a temporary run/debug configuration and launches your app.
3. Open the **Select Run/Debug Configuration** drop-down list in the toolbar.
4. Select **Save Configuration** from the options next to the configuration that you want to save.   
   ![](https://developer.android.com/static/studio/images/run/rundebug-saveconfiguration_2x.png)

   **Figure 2**. Save the configuration

**Note:** If you right-click and run or debug the same item (but not an
activity), Android Studio creates a new configuration.

### Define a test configuration for a class
or method


Android Studio lets you define a test run configuration for a class or method,
and then execute it. For example, if you create a new class, you can create
and run a test for it. If the test passes, you can then run the tests for the
rest of the project to make sure that your new code doesn't break anything
somewhere else.


Android Studio uses the [Android Instrumented Tests](https://developer.android.com/studio/run/rundebugconfig#android-tests) or [Android JUnit](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-junit.html)
template, depending on your [source
set](https://developer.android.com/studio/build/build-variants#sourcesets). For a local unit test, you can optionally run with [code
coverage](https://www.jetbrains.com/help/idea/2025.3/code-coverage.html).


To create a run/debug configuration for a class or method in your Java code, follow these steps:

1. Open a project in [Android
   or Project view](https://developer.android.com/studio/projects#ProjectFiles).
2. Open a Java file in the Code Editor.
3. Select a class or method in the code, and then press Control+Shift+T (Command+Shift+T).
4. Select **Create New Test** from the menu that appears.
5. In the **[Create
   Test](https://www.jetbrains.com/help/idea/2025.3/create-test.html)** dialog, optionally change or set the values and click **OK**.
6. In the **Choose Destination Directory** dialog, select where in the project you want Android Studio to place the test. You can specify the location by directory structure or by selecting a neighboring class.
7. Click **OK** .


   The new test appears in the **Project** window in the corresponding
   test source set.
8. To run the test, do one of the following:
   - In the **Project** window, right-click the test and select **Run** or **Debug**.
   - In the Code Editor, right-click a class definition or method name in the test file and select **Run** or **Debug** to test all methods in the class.
9. Open the **Select Run/Debug Configuration** drop-down list in the toolbar.
10. Select **Save Configuration** from the options next to the configuration that you want to save.   
    ![](https://developer.android.com/static/studio/images/run/rundebug-saveconfiguration_2x.png)

    **Figure 3**. Save the configuration

## Run or debug an app using a saved configuration


If you've saved a run/debug configuration, you can select it before you run or
debug your app.


To use a saved run/debug configuration, follow these steps:

1. Select the run/debug configuration from the **Select Run/Debug Configuration** drop-down list within the [toolbar](https://developer.android.com/studio/intro#user-interface).
2. The drop-down list is to the left of **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) and **Debug** ![](https://developer.android.com/static/studio/images/buttons/toolbar-debug.png) ; for example, ![](https://developer.android.com/static/studio/images/rdc-itoolbar_2-1.png).
3. Select **Run** \> **Run** or **Run** \> **Debug**.
4. Alternatively, click **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) or **Debug** ![](https://developer.android.com/static/studio/images/buttons/toolbar-debug.png).

## Edit a run/debug configuration


To edit a run/debug configuration, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Select a configuration in the left pane.
3. Modify the configuration, as needed.
4. Be sure to correct any errors displayed at the bottom of the dialog.
5. Click **Apply** or **OK**.

## Edit a run/debug configuration template


You can edit the configuration templates provided by Android Studio to suit your
development process. When you edit a template, it doesn't affect existing
configurations that use the template. So, for example, if you need to create a
number of configurations of a certain type, you can edit the template and then
change it back when you're done.


Although you can't create new templates, you can create configurations to use
similar to a template. You can [copy a configuration](https://developer.android.com/studio/run/rundebugconfig#starting-copy)
and edit the copy to create new configurations.


To edit a template, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Click **Edit configuration templates...**.
3. Select a configuration template.
4. Modify the configuration, as needed.
5. Be sure to correct any errors displayed at the bottom of the dialog.
6. Click **Apply** or **OK**.

## Sort and group
configurations


In the **Run/Debug Configurations** dialog, you can order your
configurations to find them quickly. You can sort the items in the
folder alphabetically, and create new folders to group configurations.


To sort configurations alphabetically, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Select a folder that contains configurations.
3. Click **Sort Configurations** ![](https://developer.android.com/static/studio/images/rdc-isortconfig_2-1.png).
4. Click **OK** to close the dialog.


To group configurations in folders, follow these steps:

1. [Open the Run/Debug
   Configurations dialog](https://developer.android.com/studio/run/rundebugconfig#opening).
2. Select a folder that contains configurations.
3. Click **Create New Folder** ![](https://developer.android.com/static/studio/images/rdc-icreatenewfolder_2-1.png).
4. Type a name in the **Folder Name** field.
5. Click **Apply** to save the name.

- Drag items from the same template category into the folder.
- Order the folders and configurations in the same template category by dragging them into position.
- Click **OK** to close the dialog.

## Define before-launch
operations

- You can specify tasks to execute before applying the run/debug configuration. The tasks are performed in the order they appear in the list.
- **Note:** Defining before launch tasks is an advanced feature. Instead of using this feature, we recommend that you put any preparation logic as tasks in your `build.gradle` file so they'll be executed when you build from the command line.
- To create a task list, follow these steps:
  1. At the bottom of the **Run/Debug Configurations** dialog under **Before launch** (you may need to scroll down), click **Add** ![](https://developer.android.com/static/studio/images/rdc-iaddnewconfig_2-1.png) and select a task type. If a dialog opens, fill in the fields and click **OK**.
  2. Add more tasks as needed.
  3. To order the tasks, drag them or select a task and click **Up** ![](https://developer.android.com/static/studio/images/rdc-imoveup_2-1.png) and **Down** ![](https://developer.android.com/static/studio/images/rdc-imovedown_2-1.png) to move it up or down in the list.
  4. Select **Show this page** if you want to display the run/debug configuration settings before applying them.


     This option is deselected by
     default.
  5. Select **Active tool window** if you want the [Run](https://www.jetbrains.com/help/idea/2025.3/run-tool-window.html) or [Debug](https://www.jetbrains.com/help/idea/2025.3/debug-tool-window.html) tool window to be activated when you run or debug your app.


     This option is selected by default.
- To remove a task from the list, follow these steps:
  1. Select a task.
  2. Click **Remove** ![](https://developer.android.com/static/studio/images/rdc-iremove_2-1.png).
- To edit a task, follow these steps:
  1. Select a task.
  2. Click **Edit** ![](https://developer.android.com/static/studio/images/rdc-iedit_2-1.png).
  3. Edit the task settings in the dialog that opens, and then click **OK**.
- The following table lists the available tasks you can add.

| Task | Description |
|---|---|
| Run External tool | Run an application that's external to Android Studio. In the **[External Tools](https://www.jetbrains.com/help/idea/2025.3/create-edit-copy-tool-dialog.html)** dialog, select one or more applications that you want to run and then click **OK** . If the application isn't defined in Android Studio yet, add its definition in the **[Create Tools](https://www.jetbrains.com/help/idea/2025.3/create-edit-copy-tool-dialog.html)** dialog. For more information, see [Configuring Third-Party Tools](https://www.jetbrains.com/help/idea/2025.3/configuring-third-party-tools.html) and [External Tools](https://www.jetbrains.com/help/idea/2025.3/external-tools.html). |
| Run Another Configuration | Execute one of the existing run/debug configurations. In the **Choose Configuration to Execute** dialog, select a configuration to execute and then click **OK**. |
| Make | Compile the project or the module. Android Studio executes the [Make Module command](https://www.jetbrains.com/help/idea/2025.3/compilation-types.html#make_module) if the run/debug configuration specifies a particular module, or it executes the [Make Project command](https://www.jetbrains.com/help/idea/2025.3/compilation-types.html#make_project) if no modules are specified. |
| Make Project | Compile the project. Android Studio executes the [Make Project command](https://www.jetbrains.com/help/idea/2025.3/compilation-types.html#make_project). |
| Make, no error check | This option is the same as **Make**, except that Android Studio executes the run/debug configuration irrespective of the compilation result. |
| Build Artifacts | Unsupported in Android Studio. |
| Run Gradle task | Run a Gradle task. In the [dialog](https://www.jetbrains.com/help/idea/2025.3/create-run-debug-configuration-for-gradle-tasks.html) that opens, specify the details and then click **OK** . For more information, see [Gradle](https://www.jetbrains.com/help/idea/2025.3/gradle.html). |
| Gradle-aware Make | Compile the project and run Gradle. |
| App Engine Gradle builder | The App Engine Gradle builder task syncs the project and then builds the module. |

- 

## Configuration templates

- Android Studio provides configuration templates to help you get started quickly. The following sections describe the templates that apply to Android development with Android Studio:
  - [Android App](https://developer.android.com/studio/run/rundebugconfig#android-application)
  - [Android Tests](https://developer.android.com/studio/run/rundebugconfig#android-tests)
  - [App Engine DevAppServer](https://developer.android.com/studio/run/rundebugconfig#app-engine)
  - [Wear OS Complication, Tile, and Watch Face](https://developer.android.com/studio/run/rundebugconfig#wear-os-configs)
- **Note:** Android Studio 2.1.*x* and lower had a Native Application template, which newer versions don't have. If you have a Native Application template in a project, Android Studio converts it to Android App when you load the project. A **Convert Project** dialog guides you through the process.

### Unsupported templates

- The following unsupported templates come from IntelliJ IDEA and aren't specific to Android development with Android Studio. For information about using these templates, follow the links to the IntelliJ IDEA documentation.
  - [Application](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-application.html)
  - [Compound](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-compound.html)
  - [Gradle](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-gradle.html)
  - [Groovy](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-groovy.html)
  - [JAR
    Application](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-jar-application.html)
  - [Java
    Scratch](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-java-scratch.html)
  - [JUnit](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-junit.html)
  - [Kotlin](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-kotlin.html)
  - [Kotlin Script](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-kotlin-script.html)
  - [Remote Debug](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-remote.html)
  - [Shell Script](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-shell-script.html)
  - [TestNG](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-testng.html)

### Common configuration options

- The **Name** , **Allow parallel run** , and **Store as project file** options are common to multiple configuration templates. To learn more about them, see [Common settings](https://www.jetbrains.com/help/webstorm/run-debug-configurations-dialog.html#common).
- Android Studio stores the shared run/debug configuration in individual XML files under the <var translate="no">project_directory</var>`/.idea/runConfigurations/` folder. For more information, see [Directory-based format](https://www.jetbrains.com/help/idea/2025.3/creating-and-managing-projects.html#directory-based) in the IntelliJ projects documentation.

### Android App

- You can run or debug Android apps and activities on virtual or hardware devices by using configurations based on this template.
- 

#### General tab

- In the **General** tab, you can specify installation, launch, and deployment options. The **Miscellaneous** tab also contains installation options.

| Field | Description |
|---|---|
| Module | Select a [module](https://developer.android.com/studio/projects#ApplicationModules) to apply this configuration to. |
| Installation Options: Deploy | Select an option: - **Default APK** - Build and deploy an APK for your [currently selected variant](https://developer.android.com/studio/run#changing-variant). - **APK from app bundle** - Build and deploy your app from an [Android App Bundle](https://developer.android.com/guide/app-bundle). That is, Android Studio first converts your app project into an app bundle that includes all your app's compiled code and resources. Then, from that app bundle, Android Studio generates only the APKs that are required to deploy your app to the connected device. You should typically use this option when testing the app bundle you intend to upload to Google Play because deploying from an app bundle extends the total build time. - **Custom Artifact** - Unsupported in Android Studio. - **Nothing** - Don't install an APK on a device. For example, if you prefer to manually install the APK, you don't need Android Studio to install it. |
| Installation Options: Deploy as instant app | If your app supports instant experiences---that is, you either add support for instant apps when you [create a new project](https://developer.android.com/studio/projects/create-project), or you create one or more [instant-enabled feature modules](https://developer.android.com/studio/projects/dynamic-delivery#create_instant_enabled)---you can choose to deploy those instant-enabled modules by checking the box next to **Deploy as instant app**. |
| Installation Options: Features to deploy | If your app includes [feature modules](https://developer.android.com/studio/projects/dynamic-delivery#dynamic_feature_modules), check the box next to each feature you want to include when deploying your app. You see this option only if your app includes feature modules. **Note:** If you want to test downloading and installing feature modules on demand, you must do so after you publish your app bundle and then use the Play Console internal test track. To learn more, read [Upload your app bundle to the Play Console](https://developer.android.com/studio/publish/upload-bundle). |
| Installation Options: Install Flags | Type any adb [pm install](https://developer.android.com/studio/command-line/adb#pm) options you want to use. Format the options the same way that you would on the command line, but without a path. Here are some examples: `-i foo.bar.baz -r /path/to/apk` and `-d -r` Default: no options. |
| Launch Options: Launch | Select an option: - **Nothing** - Don't launch anything when you select **Run** or **Debug** . However, if your app is already running and you select **Debug**, Android Studio attaches the debugger to your app process. - **Default Activity** - Launch the activity you've marked as startup in the manifest. For example: ```xml <intent-filter> <action android:name="android.intent.action.MAIN" /> <category android:name="android.intent.category.LAUNCHER" /> </intent-filter> ``` - **Specified Activity** - Launch a particular app activity in your module. When selected, the **Activity** field appears below, where you can type the name of the activity you want to launch, or click **More** to select an activity from a list. - **URL** - Launch a URL that matches an intent filter in your app's manifest. When selected, the **URL** field appears below, where you can enter the URL. You must fill in this field to launch an [Android Instant App](https://developer.android.com/topic/instant-apps). You may also use this to test your [Android App Links](https://developer.android.com/studio/write/app-link-indexing). |
| Launch Options: Launch Flags | Type any adb [am start](https://developer.android.com/studio/command-line/adb#am) options you want to use. Format the options the same way that you would on the command line, but without an intent. For example: ` -W` This option doesn't appear if you chose a **Launch** value of **Nothing**. Default: no options. |
| Deployment Target Options: Target | Select an option: - **Open Select Deployment Target Dialog** - Open the **Select Deployment Target** dialog to select a virtual or hardware device. - **USB Device** - Use a hardware device connected to your development computer through a USB port. If there's more than one, a dialog appears so you can select it. - **Emulator** - Use a virtual device. In a configuration, you can select an AVD; otherwise, it just uses the first AVD in the list. |
| Deployment Target Options: Use same device for future launches | By default this option is deselected so that every time you run an app, the **Select Deployment** dialog appears for you to select a device. When you select this option and then run an app, the **Select Deployment** dialog appears for you to select a device. Then, every time you run the app, it launches on the device you selected without displaying the **Select Deployment** dialog. To run the app on a different device, either deselect **Use same device for future launches** , or stop the app with **Run \> Stop <var translate="no">app</var>** or **Stop** ![](https://developer.android.com/static/studio/images/buttons/toolbar-stop.png), and then start it again. The **Select Deployment** dialog will display so you can select a device. |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

#### Miscellaneous tab

- In the **Miscellaneous** tab, you can specify logcat, installation, launch, and deployment options. The **General** tab also contains installation options.

| Field | Description |
|---|---|
| Logcat: Show logcat automatically | When this option is selected, the **Logcat** window opens every time you successfully deploy and launch an app using this configuration. Default: selected. |
| Logcat: Clear log before launch | Select this option if you want Android Studio to remove data from previous sessions from the log file before starting the app. Default: deselected. |
| Installation Options: Skip installation if APK has not changed. | When selected, Android Studio doesn't redeploy your APK if it detects that it's unchanged. If you want Android Studio to force an install of the APK, even if it hasn't changed, then deselect this option. Default: selected |
| Installation Options: Force stop running application before launching activity | If selected, when Android Studio detects that it doesn't have to reinstall an APK because it hasn't changed, it will force-stop the app so that the app starts from the default launcher activity. If this option is deselected, Android Studio doesn't force-stop the app. This option works with the previous option that controls whether an APK is installed or not. For both **Installation Options** fields, leave them at the default unless you explicitly want to force an install every time. In some cases you might want to deselect this option. For example, if you're writing an input method engine (IME), force-stopping the app deselects it as the current keyboard, which you might not want. Default: selected |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

#### Debugger tab

- Specify debug options in the **Debugger** tab.
- For C and C++ code, Android Studio uses the [LLDB](http://lldb.llvm.org/) debugger. In addition to the normal Android Studio UI, the debugger window has an **LLDB** tab that lets you enter LLDB commands during debugging. You can enter the same commands that Android Studio uses to display information in the debugger UI, and you can perform additional operations.
- For C and C++ projects, you can add symbol directories, as well as LLDB startup and post attach commands, in the **Debugger** tab. To do so, you use buttons similar to the following:
  - **Add** ![](https://developer.android.com/static/studio/images/rdc-iaddnewconfig_2-1.png) - Add a directory or command.
  - **Remove** ![](https://developer.android.com/static/studio/images/rdc-iremove_2-1.png) - Select a directory or command, and then click this button to remove the item.
  - **Up** ![](https://developer.android.com/static/studio/images/rdc-imoveup_2-1.png) - Select a directory or command, and then click this button to move the item up in the list.
  - **Down** ![](https://developer.android.com/static/studio/images/rdc-imovedown_2-1.png) - Select a directory or command, and then click this button to move the item down in the list.
- See [Debug Your
  App](https://developer.android.com/studio/debug) for more information about debugging in Android Studio.

| Field | Description |
|---|---|
| Debug type | Select one of the following options: - **Java only** - Debug Java code only. - **Detect Automatically** - Let Android Studio choose the best debug type for your project. - **Native Only** - Debug native C or C++ code. - **Dual (Java + Native)** - Debug Java and native code in two separate debug sessions. The **Detect Automatically** option is recommended because it chooses the right debug type for your project. |
| Symbol Directories | If you want to add symbol files to provide the debugger with C or C++ information generated outside of Android Studio, you can add one or more directories here. Android Studio preferentially uses any files within these directories over files generated by the [Android Plugin for Gradle](https://developer.android.com/studio/releases/gradle-plugin.html). The debugger searches the directories from top to bottom, in order, until it finds what it needs. It searches recursively through the files in the directory. To optimize the list and save time, put the directories used most often toward the top of the list. If you specify a directory high in the tree, it can take longer to search all of the subdirectories. If you add a very specific directory, it takes less time to search. You need to find the right balance between speed and finding the files you need for debugging. For example, if you have a directory that contains subdirectories for different [Android Binary Interfaces](https://developer.android.com/ndk/guides/abis.html) (ABIs), you can choose to add a directory for a specific ABI or for all ABIs. Although it can take longer to search through the upper-level directory, it's also more foolproof if you decide to debug on a different device. Note that you don't have to add directories containing Gradle symbol files because the debugger uses them automatically. |
| LLDB Startup Commands | Add LLDB commands that you want to execute before the debugger attaches to the process. For example, you can define settings for the environment, as shown in the following command: `settings set target.max-memory-read-size 2048` LLDB executes the commands in order from top to bottom. |
| LLDB Post Attach Commands | Add LLDB commands that you want to execute right after the debugger attaches to the process. For example: `process handle SIGPIPE -n true -p true -s false` LLDB executes the commands in order from top to bottom. |
| Host working directory | Specify the LLDB working directory. |
| Logging: Target channels | Specify LLDB log options. Android Studio sets the default options based on the team's experience --- so it's not too slow but contains needed information for troubleshooting issues. The log is often requested for Android Studio bug reports. This default is `lldb process:gdb-remote packets` You can change the default to gather more information. For example, the following log options gather information about a specific *platform*: `lldb process `*platform*`:gdb-remote packets` <br /> For a complete list of log commands, enter the `log list` command from an LLDB shell window in Android Studio. Android Studio places device logs in the following location, where *[ApplicationId](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:applicationId)* is the unique application ID that's used in your built APK manifest, and identifies your app on your device and in the Google Play Store: `/data/data/`*ApplicationId*`/lldb/log` Or, if multiple users access a device, it places the logs in the following location, where *[AndroidUserId](https://source.android.com/devices/tech/admin/multi-user.html)* is a unique identifier for a user on the device: `/data/user/`*AndroidUserId* `/`*ApplicationId*`/lldb/log` For information about using LLDB for remote debugging, see [Remote Debugging](http://lldb.llvm.org/remote.html). |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

#### Profiling tab

- The **Enable advanced profiling** option must be checked to enable certain features in the [Android Profiler](https://developer.android.com/studio/profile) when your device is running Android 7.1 or lower.

### Android Tests

- The test template that you should use depends on your [source set](https://developer.android.com/studio/build/build-variants#sourcesets). The Android Instrumented Tests template is for an [instrumented
  test](https://developer.android.com/training/testing/unit-testing). The Android JUnit template is for a local unit test.
- **Note:** If you're using Firebase Test Lab to test on a variety of devices, you can use the Android JUnit template to define your instrumented tests. For more information, see [Run Your Tests
  with Firebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#run-ctl).
- The following tab descriptions cover the tabs and fields for the Android Instrumented test template. For information about the tabs and fields for the Android JUnit test template, see the IntelliJ [Run/Debug
  Configuration: JUnit](https://www.jetbrains.com/help/idea/2025.3/run-debug-configuration-junit.html) page.

#### General tab

- In **General** tab, you can specify test location, instrumentation runner, adb shell, and deployment options.

| Field | Description |
|---|---|
| Module | Select a [module](https://developer.android.com/studio/projects#ApplicationModules) to apply this configuration to. |
| Test | In this area, specify the location of tests that you want to run: - **All in module** - Launch all tests from the selected module. - **All in package** - Launch all tests from the package specified in the **Package** field. Type the name, or click **More** to select the package from a dialog. - **Class** - Launch tests of the class specified in the **Class** field. Type the name, or click **More** to select the class from a dialog. - **Method** - Launch a test method. In the **Class** field, specify the class that contains the method. In the **Method** field, specify the method. Type the name, or click **More** to select the class or method from a dialog. |
| Specific instrumentation runner (optional) | Type the location of the [instrumentation runner](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:testInstrumentationRunner); click **More** to use a dialog. The `build.gradle` file specifies the location of the instrumentation runner; this value overrides it. The default is typically the [AndroidJUnitRunner](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) class from [AndroidX Test](https://developer.android.com/training/testing). |
| Extra options | Type any adb [am instrument](https://developer.android.com/studio/command-line/adb#am) options you want to use. Don't type the component. For example, if you're using ` `[AndroidJUnitRunner](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner) from [AndroidX Test](https://developer.android.com/training/testing), you can use this field to pass additional options to the runner, such as `-e size small`. **Default:** no options |
| Deployment Target Options: Target | Select an option: - **Open Select Deployment Target Dialog** - Open the **Select Deployment Target** dialog to select a virtual or hardware device. - **USB Device** - Use a hardware device connected to your development computer through a USB port. If there's more than one, a dialog appears so you can select it. - **Emulator** - Use a virtual device. In a configuration, you can select an AVD; otherwise, it just uses the first AVD in the list. - **Firebase Test Lab Device Matrix** - See [Run Your Tests with Firebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#run-ctl). |
| Deployment Target Options: Use same device for future launches | If you want to automatically use the device you chose through the **Select Deployment Target** dialog in the future, select this option. If the device isn't available, you'll receive a dialog. Default: deselected |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

#### Miscellaneous tab

- The **Miscellaneous** tab contains logcat and installation options.

| Field | Description |
|---|---|
| Logcat: Clear log before launch | Select this option if you want Android Studio to remove data from previous sessions from the log file before starting the app. Default: deselected. |
| Installation Options: Skip installation if APK has not changed | When selected, Android Studio doesn't redeploy your APK if it detects that it's unchanged. If you want Android Studio to force an install of the APK, even if it hasn't changed, then deselect this option. Default: selected |
| Installation Options: Force stop running application before launching activity | If selected, when Android Studio detects that it doesn't have to reinstall an APK because it hasn't changed, it will force-stop the app so that the app starts from the default launcher activity. If this option is deselected, Android Studio doesn't force-stop the app. This option works in conjunction with the previous option that controls whether an APK is installed or not. For both **Installation Options** fields, leave them at the default unless you explicitly want to force an install every time. In some cases you might want to deselect this option. For example, if you're writing an input method engine (IME), force-stopping the app deselects it as the current keyboard, which you might not want. Default: selected |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

#### Debugger tab

- Specify debug options in the **Debugger** tab.
- For C and C++ code, Android Studio uses the [LLDB](http://lldb.llvm.org/) debugger. In addition to the normal Android Studio UI, the debugger window has an **LLDB** tab that lets you enter LLDB commands during debugging. You can enter the same commands that Android Studio uses to display information in the debugger UI, and you can perform additional operations.
- For C and C++ projects, you can add symbol directories, as well as LLDB startup and post attach commands, in the **Debugger** tab. To do so, you use buttons similar to the following:
  - **Add** ![](https://developer.android.com/static/studio/images/rdc-iaddnewconfig_2-1.png) - Add a directory or command.
  - **Remove** ![](https://developer.android.com/static/studio/images/rdc-iremove_2-1.png) - Select a directory or command, and then click this button to remove the item.
  - **Up** ![](https://developer.android.com/static/studio/images/rdc-imoveup_2-1.png) - Select a directory or command, and then click this button to move the item up in the list.
  - **Down** ![](https://developer.android.com/static/studio/images/rdc-imovedown_2-1.png) - Select a directory or command, and then click this button to move the item down in the list.
- See [Debug Your
  App](https://developer.android.com/studio/debug) for more information about debugging in Android Studio.

| Field | Description |
|---|---|
| Debug type | Select one of the following options: - **Java only** - Debug Java code only. - **Detect Automatically** - Let Android Studio choose the best debug type for your project. - **Native Only** - Debug native C or C++ code. - **Dual (Java + Native)** - Debug Java and native code in two separate debug sessions. The **Detect Automatically** option is recommended because it chooses the right debug type for your project. |
| Symbol Directories | If you want to add symbol files to provide the debugger with C or C++ information generated outside of Android Studio, you can add one or more directories here. Android Studio preferentially uses any files within these directories over files generated by the [Android Plugin for Gradle](https://developer.android.com/studio/releases/gradle-plugin.html). The debugger searches the directories from top to bottom, in order, until it finds what it needs. It searches recursively through the files in the directory. To optimize the list and save time, put the directories used most often toward the top of the list. If you specify a directory high in the tree, it can take longer to search all of the subdirectories. If you add a very specific directory, it takes less time to search. You need to find the right balance between speed and finding the files you need for debugging. For example, if you have a directory that contains subdirectories for different [Android Binary Interfaces](https://developer.android.com/ndk/guides/abis.html) (ABIs), you can choose to add a directory for a specific ABI or for all ABIs. Although it can take longer to search through the upper-level directory, it's also more foolproof if you decide to debug on a different device. Note that you don't have to add directories containing Gradle symbol files because the debugger uses them automatically. |
| LLDB Startup Commands | Add LLDB commands that you want to execute before the debugger attaches to the process. For example, you can define settings for the environment, as shown in the following command: `settings set target.max-memory-read-size 2048` LLDB executes the commands in order from top to bottom. |
| LLDB Post Attach Commands | Add LLDB commands that you want to execute right after the debugger attaches to the process. For example: `process handle SIGPIPE -n true -p true -s false` LLDB executes the commands in order from top to bottom. |
| Host working directory | Specify the LLDB working directory. |
| Logging: Target channels | Specify LLDB log options. Android Studio sets the default options based on the team's experience --- so it's not too slow but contains needed information for troubleshooting issues. The log is often requested for Android Studio bug reports. This default is `lldb process:gdb-remote packets` You can change the default to gather more information. For example, the following log options gather information about a specific *platform*: `lldb process `*platform*`:gdb-remote packets` <br /> For a complete list of log commands, enter the `log list` command from an LLDB shell window in Android Studio. Android Studio places device logs in the following location, where *[ApplicationId](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:applicationId)* is the unique application ID that's used in your built APK manifest, and identifies your app on your device and in the Google Play Store: `/data/data/`*ApplicationId*`/lldb/log` Or, if multiple users access a device, it places the logs in the following location, where *[AndroidUserId](https://source.android.com/devices/tech/admin/multi-user.html)* is a unique identifier for a user on the device: `/data/user/`*AndroidUserId* `/`*ApplicationId*`/lldb/log` For information about using LLDB for remote debugging, see [Remote Debugging](http://lldb.llvm.org/remote.html). |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

### App Engine DevAppServer

- This run/debug configuration applies to the Google Cloud Platform. When you follow these steps and sync your project to the `build.gradle` file, Android Studio creates an App Engine DevAppServer configuration for you.
- Note that the IntellJ IDEA [App
  Engine Server](https://www.jetbrains.com/help/pycharm/2025.3/run-debug-configuration-app-engine-server.html) template is a different template that's not available in Android Studio.

| Field | Description |
|---|---|
| Single instance only | If you want to make sure that only one instance of the run/debug configuration is currently executed, select this option. It doesn't allow multiple runs of the same configuration at the same time. Default: selected |
| Module | Select a [module](https://developer.android.com/studio/projects#ApplicationModules) to apply this configuration to. |
| Synchronize with build.gradle configuration | If you add an App Engine module and sync to the `build.gradle` file, the App Engine DevAppServer configuration fields are filled in for you (recommended). Selecting **File \> Sync Project with Gradle Files** also syncs the project. Default: selected |
| App Engine SDK | Type a path to a [Google App Engine SDK](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Java) for Java on the local machine. Click **...** to select it from a dialog. |
| War Path | Type a path to the Web Application Archive (WAR) directory of the app you're deploying on the local development server. Click **...** to select it from a dialog. |
| VM Args | Specify the command-line options you want to pass to the VM for launching the DevAppServer. When specifying the options: - Use spaces to separate different options. - For options that have spaces, enclose the space in quotation marks (`"` `"`). - If an option includes quotation marks, add a backslash before the quotation mark (`\"`). For more information about VM options, see the documentation for your J2SE version, such as [`java` JDK 7](http://docs.oracle.com/javase/7/docs/technotes/tools/windows/java.html) and [`java` JDK 8](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/java.html). Default: no options |
| Server Address | Type the host [address](https://cloud.google.com/appengine/docs/java/tools/devserver#The_Development_Console) to use for the server. You might need to provide the address to be able to access the development server from another computer on your network. An address of 0.0.0.0 allows both localhost access and hostname access. Default: localhost |
| Server Port | Type the [port](https://cloud.google.com/appengine/docs/java/tools/devserver#The_Development_Console) number to use for the server. Default: 8080 |
| Disable Check for App Engine SDK Updates | If given, the development server will [not contact App Engine](https://cloud.google.com/appengine/docs/java/tools/devserver#The_Development_Console) to check for the availability of a new release of the SDK. By default, the server checks for a new version on startup, and prints a message if a new version is available. |
| Before Launch | See [Defining Before Launch Operations](https://developer.android.com/studio/run/rundebugconfig#definingbefore). |

### Wear OS run/debug configurations

- The Wear OS Complication, Tile, and Watch Face templates let you run or debug Wear OS apps on virtual or hardware devices. Most of the template configuration options are the same as the [Android App options](https://developer.android.com/studio/run/rundebugconfig#android-application). Here are the options that are more specific to the Wear OS run/debug configurations:
  - For all Wear run/debug configurations, you have to select a specific complication data source, tile, or watch face (depending on the template) to apply the configuration to. Generally each of these entities corresponds to a class in your code.
  - For the Wear OS Complication run/debug configuration, you must choose the **Slot** where you want to put the complication data provided by the complication data source. You can choose to put it at the top, right, bottom, left, or background of the watch face.
  - For the Wear OS Complication run/debug configuration, you must also select the **Type** of the complication data provided by the complication data source. The types you can choose from are limited to those that are provided by the chosen complication data source *and* supported by the chosen slot. For a list of complication data types, see [Types and fields](https://developer.android.com/training/wearables/watch-faces/adding-complications#types-fields).
- Alternatively, you can also run these surfaces from the gutter icon that is located next to the declaration of the surface, as shown in the following image. If an error occurs, such as "Error while setting the tile," check that you've correctly configured the surface, including [declaring the surface in your manifest](https://developer.android.com/training/wearables/tiles/get_started#create).
![Run button in the gutter next to a WatchFaceService class.](https://developer.android.com/static/studio/images/run/wearos_os_gutter_run.png) **Figure 1.** Run a Wear OS surface directly using the gutter icon.