---
title: https://developer.android.com/studio/platform/projects/create-project
url: https://developer.android.com/studio/platform/projects/create-project
source: md.txt
---

Android Studio for Platform (ASfP) helps you set up your development environment
for the [Android Open Source Project (AOSP)](https://source.android.com/). Built on the IntelliJ
Workspace Model, ASfP supports both manual configuration and shareable team
templates.

## Launch the project setup wizard

You can launch the project setup wizard in two ways:

- **From the Welcome screen** : Click **New Project** or **Import ASfP
  Project**.
- **From an open project** : In the main menu, select **ASfP \> Project \>
  New Project** or **Import ASfP Project**.

## Import from a template

If your team shares a standard `.asfp-project` configuration file, you can
initialize your workspace directly from that template:

1. In the project setup wizard, select **Import from template**.
2. Browse to and select the shared `.asfp-project` or `.asfp-template` YAML file.
3. After the wizard populates the project settings from the template, verify your local **Repo checkout** path, and then click **Finish**.

## Configure manually

To create a new project configuration from scratch, do the following:

1. In the project setup wizard, choose to configure the project manually and
   fill in the project details:

   - **Repo checkout (Module paths)** : Specify the absolute path to the root of your local AOSP source checkout (for example, `/path/to/aosp`).
   - **Lunch target** : Enter the lunch target you use for building (for example, `aosp_cf_x86_64_phone-aosp_current-userdebug`).
   - **Project name**: Give your project a descriptive name.
   - **Directories and modules** : List the initial directories or Soong modules to include in your project (relative to the repository root, such as `frameworks/base` or `packages/apps/Settings`).
   - **Languages** : If your workflow includes C, C++, or Rust platform code, select **C or C++** or **Rust** . Java, Kotlin, and `Android.bp` are included by default.
   - **Environment variables and build options** : In the wizard's **Environment variables** field, add any custom environment variables like `SOONG_ALLOW_MISSING_DEPENDENCIES=true`, and optionally select the **Soong Partial Compile** (`SOONG_PARTIAL_COMPILE`) checkbox for faster incremental builds.
2. Click **Finish** . ASfP creates the project structure, generates the
   `.asfp-project` configuration file in your project root, and runs the
   initial sync.

## Share or customize your project configuration

After initial setup, you can customize your project at any time by editing the
`.asfp-project` file (**ASfP \> Project \> Open Config**):

- Add or exclude directories and Soong modules.
- Enable additional languages (`cpp`, `rust`).
- Configure custom Soong flags and environment variables.

To export your configuration for teammates, right-click the `.asfp-project` tab
and select **Export to Template**.

For more information about `.asfp-project` parameters, sync modes, and
in-editor `Android.bp` actions, see
[Projects overview and Soong workflows](https://developer.android.com/studio/platform/projects).