---
title: https://developer.android.com/tools/agents/android-cli/release-notes
url: https://developer.android.com/tools/agents/android-cli/release-notes
source: md.txt
---

Android CLI is the primary interface for Android development from the terminal,
built to empower your development workflows using the agent and tools of your
choice.

This page lists the new features in every Android CLI release. To download
Android CLI, go to the [download page](https://developer.android.com/tools/agents). To learn more,
see the [Android CLI overview](https://developer.android.com/tools/agents/android-cli).

## Version 1.0.15985488 (July 2026)

- **Dedicated install command** : Install APKs using the standalone `android install` command that features incremental APK push making incremental installations orders of magnitude faster than `adb`.
- **Run incremental installs** : Similarly, use the new `--use-delta-install` flag in `android run` for faster incremental APK deployments to devices.
- **Cross-platform SDK management** : Target non-host platforms with the new `--platform <os_arch>` flag in `android sdk` commands (`install`, `update`, `materialize`) to inspect, resolve, and install components across OS and CPU architectures.
- **Skills CLI enhancements** : Expanded `android skills` subcommands (`add`, `remove`, `list`, `find`) with `--help` documentation, clear feedback when skills are missing, and safer atomic download staging with automatic rollback.

## Version 1.0.15857036 (July 2026)

- **Broader agent skills support** : Install skills across dozens of agent environments (including Claude Code, Cursor, Cline, OpenHands, Windsurf, Zed, and Devin) using `android skills install`.
- **Native downloader with proxy support**: Download network resources reliably using a native HTTP downloader with out-of-the-box support for corporate proxies.
- **SDK package management** : Manage SDK packages with multi-package removal in `android sdk remove` and SHA-based resolution in `android sdk resolve`.
- **Describe and screen improvements** : View Gradle build errors directly on standard output in `android describe`, and target specific devices using the `--device` flag in `android screen`.
- **CLI usability and error reporting** : Clearer error messages when entering unknown commands or invalid project creation targets, case-insensitive `android emulator` commands.

## Version 1.0.15498356 (May 2026)

- **Dynamic SDK template loading** : Project templates for `android create` are now downloaded dynamically from the Android SDK package rather than bundled in the CLI binary, ensuring new projects always use the latest templates.
- **SDK license compatibility** : Accepted SDK licenses saved by `android sdk` now match the file format expected by older Android SDK tools and Gradle plugins.
- **Symlink support**: Added support for symbolic links across CLI commands and file operations.
- **Atomic binary extraction**: Prevent extraction race conditions during concurrent multi-process CLI invocations by unpacking binaries to a temporary directory before atomically moving them into place.
- **Windows stability**: Improved Windows compatibility and performance on Windows 11, alongside fixes for home directory path resolution.

## Version 1.0.15433482 (May 2026)

- **Antigravity integration** : Android CLI and skills are now officially integrated into [Google Antigravity 2.0](https://antigravity.google/docs/build-with-google) as an optional bundle of resources to streamline your agentic development.
- **Android Studio commands** : Use the new [`android studio`](https://developer.android.com/tools/agents/android-cli#studio-check) command to enable your agents to leverage the deep, contextual capabilities of Android Studio, including code analysis, semantic lookups, and Compose rendering.
- **Support for Journeys** : Validate critical user experiences using [Journeys](https://developer.android.com/tools/agents/android-cli/journeys), which are natural language descriptions of user flows that your agents can run from the terminal or in CI/CD.
- **New Android skills** : Access new [Android skills
  library](https://developer.android.com/tools/agents/android-skills/browse), including skills for CameraX migration, adaptive UI, AppFunctions, and Compose Styles.
- **More installation options** : Install and update Android CLI using popular package managers, including `apt-get`, `winget`, and `homebrew`. For details, see the [download options](https://developer.android.com/tools/agents/android-cli/download).

## Version 0.7 (April 2026)

First release!