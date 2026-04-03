---
title: https://developer.android.com/studio/platform/projects/create-project
url: https://developer.android.com/studio/platform/projects/create-project
source: md.txt
---

Android Studio for Platform (ASfP) helps you set up your development environment
for the [Android Open Source Project (AOSP)](https://source.android.com/). This page explains how to
start a new project or import an existing one.

## Create a new project

1. If you don't have a project open, click **New Project** on the Welcome
   screen. ![ASfP Welcome Screen showing New Project
   option](https://developer.android.com/studio/platform/images/welcome_screen.png)

2. If you already have a project open, select **ASfP \> Project \> New Project**
   from the menu.

3. Fill in the project configuration details in the wizard: ![ASfP New Project
   configuration wizard screen](https://developer.android.com/studio/platform/images/finish_project_import_screen.png)

   - **Module paths:** Specify the absolute path to the root of your AOSP source code checkout (for example, `/path/to/aosp`).
   - **Lunch target:** Enter the lunch target you use for building (for example, `aosp_arm64-eng`).
   - **Project name:** Give your project a descriptive name.
   - **Directories / modules:** List the initial directories or modules you want to include in your project, separated by commas. These should be relative paths from the repository root (for example, `frameworks/base,
     packages/apps/Settings`). You can add more or refine this selection later.
4. Click **Finish** . ASfP creates the project structure and the `.asfp-project`
   configuration file.

## Configure and customize your project

After the initial project setup, you can further customize your project by
editing the `.asfp-project` file located in the project root. This file lets
you:

- Add or remove directories and modules.
- Enable support for other languages like Rust or C++.
- Configure build flags and environment variables.
- Specify test sources.

For detailed information on all configuration options, see the [Projects
overview](https://developer.android.com/studio/platform/projects). After editing `.asfp-project`, you'll need to sync the project for
the changes to take effect.

## Import an existing project

ASfP doesn't have a separate "import" action. To open an existing ASfP project
configuration:

1. Select **ASfP \> Project \> New Project**.
2. In the **Project Name** field, navigate to and select the directory containing the existing `.asfp-project` file you want to open. The fields in the wizard will populate based on the selected `.asfp-project` file.
3. Click **Finish**. ASfP opens and indexes the project.