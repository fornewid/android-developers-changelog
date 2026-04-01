---
title: https://developer.android.com/stories/apps/microsoft
url: https://developer.android.com/stories/apps/microsoft
source: md.txt
---

# Microsoft Outlook, Teams, and Office increased active users and retention with large screens

Microsoft empowers people and organizations to work, learn, organize, connect, and create through their leading Microsoft 365 apps. To achieve that, Microsoft knows it's essential to provide an optimal productivity experience for their customers across all devices they use. With the usage of tablets and foldables exploding for productivity apps, Microsoft has been investing in improving the experiences for the Outlook, Teams, and Office apps to give their users a more desktop-like experience on the go.
> *Teams has a fair share of users on tablets and foldables, and not having optimized experiences for larger form factors was something customers complained about.*
>
> Richa Srivastava, Senior Program Manager, Microsoft

## What they did

[Multi-window mode](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode)usage has taken off on large screen devices, and companies such as Microsoft have taken advantage of the additional real estate of large screens to provide better experiences for their users. Microsoft made the Outlook, Teams, and Office apps shine on foldables and tablets by optimizing their layouts and incorporating multi-window and[multi-instance](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#multi-instance)capabilities.  

### Optimized layouts for large screens

Microsoft started by optimizing their layouts to better fit the large screen, such as using the list-detail layout for viewing a list of emails next to an expanded email in Outlook. While on a foldable or a tablet, the two views are displayed side by side, or in dual-pane mode, separated by a vertical divider. Users can now easily go through and triage their inbox and calendar without having to switch between inbox and conversation views.  
![](https://developer.android.com/static/images/distribute/stories/microsoft-before-and-after.png)

For the Teams app, they spanned the list-detail layout for when the device is in landscape orientation. This enabled their users to access their content, chats, and files faster and in a more efficient manner when on large screen devices.  
![](https://developer.android.com/static/images/distribute/stories/microsoft-teams.png)

For Office, they also created unique dual-screen experiences based on the document type to enable their users to take advantage of the real estate, such as a reading mode for Word, a list-detail layout for PowerPoint, and an extended canvas for Excel.

### Support for multitasking

While the team improved individual app experiences, they also invested in ensuring the apps work well together. Across Teams, Outlook, and Office, Microsoft implemented multitasking features. They made sure the UI was fully resizable so that the apps could seamlessly be transitioned into split-screen or multi-window mode. This helped pair productivity use cases like having a chat open while also working on a document.

Then the apps added functionality to help users be more productive in multi-window mode, like[drag and drop](https://developer.android.com/guide/topics/ui/drag-drop)---enabling drag and drop for text, files, and messages between apps, messages, and events.  

Lastly, the Office team added multi-instance support which allows users to have multiple instances of the same app side by side, which is useful when viewing two documents simultaneously. The multi-window mode helps in optimized creation with lighter edits and consumption. For Outlook, they also implemented multi-instance, enabling use cases such as composing an email while also reading another message.  
![](https://developer.android.com/static/images/distribute/stories/microsoft-multi-tasking.png)

For Teams, users can simply switch from one chat to another and have meetings that are more efficient.

Given the legacy of the Microsoft apps along with being a large company, implementing the multi-window experience was a one-month project, while implementing multi-instance took the team two months to complete. The improved experiences and the positive customer reactions were better than the teams had hoped for!

## Results

Through their efforts, Microsoft has**enabled users to be more efficient and productive** on large screen devices. These investments led to**increased active users and retention,** and**positive customer feedback.**With the success they've seen for these apps, the Microsoft team will be continuing to evolve the user experience for all screens.

## Get started

Learn more about how you can get started with optimizing your app for[large screens](http://d.android.com/large-screens), and learn more about large screen[app quality](https://developer.android.com/docs/quality-guidelines/large-screens-app-quality).