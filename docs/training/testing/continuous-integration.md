---
title: https://developer.android.com/training/testing/continuous-integration
url: https://developer.android.com/training/testing/continuous-integration
source: md.txt
---

# Continuous Integration basics

Continuous Integration (CI) is a software development practice where developers frequently merge their code changes into a central repository, after which automated builds and tests run.

You can set up a basic CI system to prevent new changes that would break the build after merging in. You can program a more advanced CI system to automatically test the app and make sure it behaves as expected in different environments, such as API levels, screen sizes, and platforms.
![A diagram showing how multiple developers request code changes and how they are checked by the CI system before getting merged into the main code repository.](https://developer.android.com/static/training/testing/continuous-integration/ci1.svg)**Figure 1.**A CI system keeps a code repository healthy by running checks before merging.

This document demonstrates common strategies developers use to set up effective CI systems for Android projects. These guidelines are generic and apply to the majority of solutions.

## Typical example

A typical CI system follows a*workflow* or*pipeline*, which might look as follows:

1. The CI system detects a change in the code, usually when a developer creates a pull request, also called "change list" or "merge request".
2. It provisions and initializes a server to run the workflow.
3. It fetches the code as well as tools such as the Android SDK or emulator images if needed.
4. It builds the project by running a given command, for example .`/gradlew
   build`.
5. It runs the[local tests](https://developer.android.com/training/testing/local-tests)by running a given command, for example running .`/gradlew test`.
6. It starts emulators and runs the[instrumented tests](https://developer.android.com/training/testing/instrumented-tests).
7. It uploads artifacts such as test results and APKs.

![A diagram showing a basic CI workflow](https://developer.android.com/static/training/testing/continuous-integration/ci2.svg)**Figure 2.**A basic CI workflow

## Benefits of CI

The advantages of CI include:

- **Improved quality of software**: CI can help to improve the quality of software by identifying and fixing problems early on. This can help to reduce the number of bugs in software releases and improve the overall user experience.
- **Reduced risk of broken builds**: When you automate your build process with CI you can better avoid broken builds by resolving issues earlier in the process.
- **Increased confidence in releases**: CI can help to ensure that each release is stable and ready for production. By running automated tests, CI can identify any potential problems before you release them to the public.
- **Improved communication and collaboration**: By providing a central place for developers to share code and test results, CI can help to make it easier for developers and other team members to work together and track progress.
- **Increased productivity**: CI can help to increase developer productivity by automating tasks that would otherwise be time-consuming and error-prone.

## Further reading

More more information on how you can use constant integration to improve development for your app, read the following pages:

- **[CI Automation](https://developer.android.com/training/testing/continuous-integration/automation)**

- **[CI Features](https://developer.android.com/training/testing/continuous-integration/features)**