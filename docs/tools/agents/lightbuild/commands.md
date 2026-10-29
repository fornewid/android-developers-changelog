---
title: https://developer.android.com/tools/agents/lightbuild/commands
url: https://developer.android.com/tools/agents/lightbuild/commands
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

The Lightbuild CLI is the official command-line tool for Lightbuild. Use the
`lightbuild` command to build and test your project, find its build targets, and
resolve its dependencies. Your AI agents can run the same commands. Projects
that you create from a Lightbuild template include an `AGENTS.md` file that
tells AI agents how to work with Lightbuild and the Lightbuild CLI.

For more information about the Lightbuild CLI's commands and options, see the
[Lightbuild CLI reference](https://developer.android.com/tools/agents/lightbuild/cli-reference).

## Install the Lightbuild CLI

The Lightbuild CLI is distributed as an Android SDK package that you install
with [Android CLI](https://developer.android.com/tools/agents). You can install and set it up with a
single command, or install it manually.

### Install and set up in one step

To install the Lightbuild CLI, run the command for your operating system. The
command installs the Lightbuild CLI package in your Android SDK, and then runs
the package's setup script, which copies the Lightbuild CLI to `~/.local/bin` on
macOS and Linux, or to `$HOME\AppData\LightbuildCLI` on Windows, and makes sure
that directory is in your `PATH`:

- **macOS and Linux**:

      android sdk install build/lightbuild/0.0.30 && bash "$(android info sdk)/build/lightbuild/0.0.30/cli/install.sh"

- **Windows (PowerShell)**:

      android sdk install build/lightbuild/0.0.30; if ($LASTEXITCODE -eq 0) { & "$(android info sdk)\build\lightbuild\0.0.30\cli\install.cmd" }; if ($LASTEXITCODE -eq 0) { $env:Path += ";$HOME\AppData\LightbuildCLI"; setx LIGHTBUILD_REFRESH 1 | Out-Null; reg delete HKCU\Environment /v LIGHTBUILD_REFRESH /f | Out-Null }

- **Windows (Command Prompt)**:

      android sdk install build/lightbuild/0.0.30 && for /f "delims=" %p in ('android info sdk') do call "%p\build\lightbuild\0.0.30\cli\install.cmd" && setx LIGHTBUILD_REFRESH 1 >nul && reg delete HKCU\Environment /v LIGHTBUILD_REFRESH /f >nul

After the command finishes, [verify the installation](https://developer.android.com/tools/agents/lightbuild/commands#verify).

### Install manually

Alternatively, to install the Lightbuild CLI and add it to your `PATH` yourself,
follow these steps:

1. If you don't have Android CLI, [install it](https://developer.android.com/tools/agents).
2. Install the Lightbuild package:

       android sdk install build/lightbuild/0.0.30

3. Copy the Lightbuild CLI to a directory in your `PATH`, so that you can run
   `lightbuild` from any directory. You can copy it to any directory that's
   already in your `PATH`, or use the same directory that the setup script
   uses:

   - **macOS and Linux** : Copy the `lightbuild` file to `~/.local/bin`:

         mkdir -p ~/.local/bin
         cp "$(android info sdk)/build/lightbuild/0.0.30/cli/lightbuild" ~/.local/bin/

     If `~/.local/bin` isn't in your `PATH`, add the following line to your
     shell's startup file, such as `~/.zshrc` or `~/.bashrc`:

         export PATH="$PATH:$HOME/.local/bin"

   - **Windows** : Run the following commands in PowerShell. They copy
     `lightbuild.exe` to `$HOME\AppData\LightbuildCLI`, add that directory to
     your user `Path` if it isn't already there, and then make the change
     take effect in your current session and in terminals that you open
     later:

         $dir = "$HOME\AppData\LightbuildCLI"
         New-Item -ItemType Directory -Force $dir | Out-Null
         Copy-Item "$(android info sdk)\build\lightbuild\0.0.30\cli\lightbuild.exe" $dir
         $userPath = (Get-ItemProperty HKCU:\Environment).Path
         if (($userPath -split ";") -notcontains $dir) { Set-ItemProperty HKCU:\Environment Path "$userPath;$dir" -Type ExpandString }
         setx LIGHTBUILD_REFRESH 1 | Out-Null; reg delete HKCU\Environment /v LIGHTBUILD_REFRESH /f | Out-Null
         $env:Path += ";$dir"

4. [Verify the installation](https://developer.android.com/tools/agents/lightbuild/commands#verify)


<br />

### Verify the installation

To verify that the Lightbuild CLI is installed, check its version:

    lightbuild --version

If your terminal can't find the `lightbuild` command, open a new terminal window
so that your `PATH` changes take effect.

## Find your project's build targets

Lightbuild CLI commands take a target, which identifies the part of your project
to build, test, or inspect. A target can be a module's name, such as `app`, or
something more specific, such as `app:app-debug.apk`. To match all the targets
in a module, use the module's name followed by `/...`, such as `app/...`. To
match all the targets in your project, use `...`.

To list all the targets in your project, query them from your project's root
directory:

    lightbuild query ...

To list the files that a target produces, add `--output=files`. For example, for
the `app` target, run:

    lightbuild query app --output=files

To list the commands that are available for your project, run `lightbuild help`.

## Build your app

To build a target, run `lightbuild build` with the target. For example, to build
the `app` module, run:

    lightbuild build app

To build all the targets in your project, run:

    lightbuild build

To build a signed release app bundle that you can upload to Google Play, see
[Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish).

To remove your project's build output and caches, run:

    lightbuild clean

## Run your app

The Lightbuild CLI builds your app, but doesn't install or run it. To run your
app on a connected device or a running emulator, build the app, and then run it
with the [`android run`](https://developer.android.com/tools/agents/android-cli/commands/run) command in Android CLI:

    lightbuild build app
    android run --apks=app/build/app-debug.apk

To see where each of a module's targets writes its output, run
`lightbuild query app/... --output=files`. The locations are relative to the
module's directory.

## Run tests

To run all the tests in your project, run:

    lightbuild test

This command runs your local tests, which run on your development machine, and
your instrumented tests, which run on a connected device or a running emulator.

To run the tests in one module, add the module's target, such as `app-core`. To
run only one type of test, add `:hostTest` for local tests or `:deviceTest` for
instrumented tests to the module's target. For example:

    lightbuild test app-core:hostTest
    lightbuild test app-core:deviceTest

## Resolve dependencies

Each module records its resolved dependencies in a `resolved.deps` file. To
generate the `resolved.deps` file for a module, run `lightbuild resolve` with
the module's target. For example, for the `app` module, run:

    lightbuild resolve app

To resolve all the targets in your project, run:

    lightbuild resolve

For more information, see [Resolved dependencies](https://developer.android.com/tools/agents/lightbuild/structure#resolved-deps).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Lightbuild CLI reference](https://developer.android.com/tools/agents/lightbuild/cli-reference)
- [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup)
- [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema)
- [Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish)