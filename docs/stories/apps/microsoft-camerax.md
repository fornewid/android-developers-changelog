---
title: https://developer.android.com/stories/apps/microsoft-camerax
url: https://developer.android.com/stories/apps/microsoft-camerax
source: md.txt
---

# Microsoft Lens increases developer productivity using CameraX

![](https://developer.android.com/static/images/distribute/stories/AppExcellenceCameraXCaseStudy_1024x512_Social.png)

[Microsoft Lens](https://play.google.com/store/apps/details?id=com.microsoft.office.officelens)is a product that makes images of documents and whiteboards easier to read. The Microsoft Lens team was concerned that the[Camera1](https://developer.android.com/guide/topics/media/camera)API, an Android framework API that includes support for cameras and camera features, was performing inconsistently for them on modern Android devices. They scoped out building something new and determined that the fastest development route was to use CameraX to get the modern features of a camera phone.

## What they did

Microsoft decided to use[CameraX](https://developer.android.com/training/camerax)for their suite of productivity apps that use Microsoft Lens. CameraX is an open source[Android Jetpack](https://developer.android.com/jetpack)support library that makes it simpler for developers to build camera functionality in Android apps. CameraX integrates with all of Microsoft Lens' tools to ensure use of high-quality images across select apps. CameraX also improves the developer experience by providing a simpler API and works across 94 percent of Android devices. By switching to CameraX, the Microsoft Lens team was able to solve their performance issues, increase developer productivity, and reduce the time to go to market.

## Results

![](https://developer.android.com/static/images/distribute/stories/AppExcellenceCameraXCaseStudy_1024x512_InlineGraphic_02.png)

The Microsoft Lens team found that implementing the CameraX library saved their developers a significant amount of time, as a result of fewer testing and optimization cycles. They estimate that CameraX took their engineering team about four months of effort for integration time, compared to Camera2, which would have taken about six.

"With CameraX it is easier to configure attributes like resolution, aspect ratio, image rotation, capture quality, etc., when compared to Camera1 APIs, which helped integration effort and time. CameraX internally handling the state (to open/close camera) while users switch between the applications had reduced lines of code to integrate and also helped developer productivity to focus on business logic instead of app resetting state," said Vishal Bhatnagar, Principal Software Engineer Manager at Microsoft.

![](https://developer.android.com/static/images/distribute/stories/AppExcellenceCameraXCaseStudy_1024x512_InlineGraphic_01.png)

Using CameraX led Microsoft to better launch and capture performance compared to Camera1. Their performance on modern Android devices increased by 2X in launch and capture, and some devices even saw performance gains of 3X (although this varies by device). In addition, enabling core scan functionality was easier compared to estimates for Camera2. In terms of device fragmentation, CameraX effectively hides many devices' Camera2 variations in implementation on many OEM devices.

The Microsoft team is currently integrating CameraX into some of their other Android apps, such as Office, Teams, OneDrive, Word, Excel, PowerPoint, Microsoft Lens, and My Hub. All of these apps use CameraX for image capture functionality in scenarios such as document scan and image to entity extraction (such as image to table, image to text). The Microsoft team is also planning to implement CameraX in Outlook soon and looking into its potential for other apps, such as Kaizala.

## Get started

Visit our documentation to learn more about how to implement CameraX in your app.