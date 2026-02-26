---
title: https://developer.android.com/build/publish-library
url: https://developer.android.com/build/publish-library
source: md.txt
---

In addition to publishing Android apps for users, you can publish
libraries that developers can incorporate in their apps. There are four main
tasks when publishing an Android library:

- [Prepare the library for release](https://developer.android.com/studio/publish-library/prep-lib-release). During the preparation step, you configure settings such as the library name, the technical requirements to run or embed the library, and the metadata that helps the Android Gradle plugin (AGP) consume libraries.
- [Configure publication
  variants](https://developer.android.com/studio/publish-library/configure-pub-variants). Publication variants let you publish different versions of your library, such as for debug versus release.
- [Configure test fixtures for publication](https://developer.android.com/studio/publish-library/configure-test-fixtures). This helps ensure that your tests are robust and repeatable.
- [Publish multiple libraries as one](https://developer.android.com/studio/publish-library/fused-library). Use the Fused Library to publish multiple libraries in a single library.
- [Upload your library](https://developer.android.com/studio/publish-library/upload-library). This involves choosing a distribution mechanism and creating the actual publication.

If you're a library author, read through each page in this
document for a detailed explanation of the considerations and steps involved in
publishing your library.