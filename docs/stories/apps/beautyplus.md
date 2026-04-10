---
title: https://developer.android.com/stories/apps/beautyplus
url: https://developer.android.com/stories/apps/beautyplus
source: md.txt
---

# BeautyPlus app increases readability by 15% with Android Architecture Components

![](https://developer.android.com/static/images/distribute/stories/beautyplus-logo.png)

Introduced in 2013,[BeautyPlus](https://play.google.com/store/apps/details?id=com.commsource.beautyplus)is one of the world's most popular photo-editing apps, used by makeup artists, photographers, and ordinary mobile phone snappers. About 50 million people use the app every month to edit and add filters to their selfies, pictures, and videos. Developed by China's Xiamen Meitu Technology Co., Ltd., the app (which is particularly popular with the selfie set) is used for everything from correcting skin tone and brightening smiles to slimming features and airbrushing away blemishes, all with a few simple drags and clicks.

Given the company makes frequent updates to the app, it requires a large number of developers. But, over time, the underlying architecture grew to lack uniformity and clarity. The fast-moving team needed a way to keep their collaborating developers in the loop while simplifying lifecycle management and resolving issues related to refreshing the asynchronous UI.  
![](https://developer.android.com/static/images/distribute/stories/beautyplus-screenshot.png)**Figure 1:**A sample photo-editing session in BeautyPlus

## What they did

[Android Architecture Components](https://developer.android.com/topic/libraries/architecture)provided the tools that the developers needed to make the app's code concise, stable, and easier for new engineers to read as they onboard.

Among the components the BeautyPlus developers began using is[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel), which enables easier logic processing with activity and fragment updates.`ViewModel`is designed to store and manage UI-related data in a lifecycle-conscious way that respects the lifecycle of other app components.

They also leveraged the[`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata)component, an observable data-holder class that's also lifecycle-aware to help ensure that the UI matches the data state. The team found these Android Architecture Components easy to use without encountering any problems---and the benefits were quickly noticeable.

## Results

Thanks to Android Architecture Components, the BeautyPlus app immediately had 5% leaner code and was 15% more readable. The architecture was also more unified, saving developers time and effort, and making it easier for new developers to get up to speed quickly. In addition, there were fewer memory leaks, refreshing data became easier, and developers no longer had to worry about updating the asynchronous UI.
> "When we used ViewModel and LiveData for BeautyPlus, the code became more concise and readable, and the architecture of the code was unified," says Zheng Songyin, senior development manager. "The operation of the lifecycle of the app was managed safely, and the stability improved, too."

## Get started

Android Architecture Components is open to all developers.[Get started with Android Architecture Components](https://developer.android.com/topic/libraries/architecture).