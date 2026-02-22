---
title: https://developer.android.com/training/testing/continuous-integration/features
url: https://developer.android.com/training/testing/continuous-integration/features
source: md.txt
---

# CI features

The following are some features that you can find in most CI systems.

## Environment

It's important to choose and understand the hardware and software environment in which the system executes the workflow. Important considerations for Android applications are:

- **Platform**: Linux, Mac, Windows, and their versions.
- **Available memory**: Building apps and running emulators can use a lot of RAM and it's often necessary to tweak parameters such as the JVM's heap size to avoid out-of-memory errors.
- **Preinstalled software**: CI systems usually provide images with a large collection of tools already available, such as the Java Development Kit (JDK), the Android Software Development Kit (SDK), build tools, platforms and emulators.
- **Runner architecture and instruction set**: ARM, x86. This is important when using emulators.
- **Environment variables** : Some are set by the CI system (for example:`ANDROID_HOME`) and you can set your own to, for example, avoid hardcoding credentials in your workflow.

There are many other aspects you should consider, such as the number of cores available, and whether virtualization is enabled to run emulators.

## Logs and reports

When a step fails, the CI system notifies you and usually doesn't let you merge the change. To find out what has gone wrong, look for errors in the logs.

Additionally, building and testing generates reports that are usually stored as artifacts of that particular build. Depending on the CI system, you can use plugins to visualize the results of those reports.

## Cache and CI run times

CI systems use a build cache to speed up the process. In its simplest form, they save all the Gradle cache files after a successful build and restore them before a new one. This relies on[Gradle's build cache](https://docs.gradle.org/current/userguide/build_cache.html)feature and should be enabled in your project.
| **Note:** take into account the time that it takes for the cache to download as, if the cache becomes too big and it contains more than is necessary, it could be detrimental to the overall build time.

Some ways to improve run times and reliability include:

- **Modules**: Detecting which modules are affected by a change and only building and testing those.
- **Skip caches**: If the build includes scripts that a developer has modified, ignore the build caches. It's safer to build from scratch.
- **Shard tests**: Especially instrumented tests, it can be helpful to shard tests across multiple devices. This is supported by the Android runner, Gradle Managed Devices and Firebase Test Lab.
- **Shard builds**: You can shard the build across multiple server instances.
- **Remote cache** : You can also use[Gradle's remote cache](https://docs.gradle.org/current/userguide/build_cache.html).

## Retry failed tests

Flakiness refers to tests or tools that fail intermittently. You should always try to find and fix the problems that generate flaky builds and tests, but some of them are difficult to reproduce, especially when running instrumented tests. A common strategy is to retry test runs whenever they fail, up to a maximum number of retries.

There is no single way to configure retries, as they can occur at multiple levels. The following table outlines the action you might take in response to a flaky test failure:

|                           Failure                            |        Action         |
|--------------------------------------------------------------|-----------------------|
| Emulator was unresponsive for a second, triggering a timeout | Rerun the failed test |
| Emulator failed to boot                                      | Rerun the whole task  |
| There was a connection error during the code checkout phase  | Restart the workflow  |

It's important to log and keep track of which parts of the system are flaky and invest in keeping CI reliable and fast, only relying on retries