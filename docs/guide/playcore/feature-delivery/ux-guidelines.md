---
title: https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines
url: https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines
source: md.txt
---

# UX best practices for on demand delivery

The functionality that works well as an on demand module are those that aren't needed by the majority of your users at install time. The following are a few examples for app features that would appropriate on demand modules:

- Editing and uploading a video in an app where the majority of users only watch videos
- Adding a recipe in an app, where most users only browse and follow others' recipes
- Help and support functionality when most users don't seek help, or don't seek it within the app
- Large libraries for less used functionality such as providing detailed bug capture and reporting
- Specific payment or checkout capabilities
- Very high-resolution media experiences or VR/AR features

In the typical case where these modules are relatively small (less than 10MB), and there aren't any network or other failures, users can download and use an on demand module very quickly. That is, the experience is typically no different than if the module had been present at app install.

This page describes best practices that help you do the following:

- Ensure your users are aware and feel in control of relatively larger module downloads which don't load instantly, or module install errors.
- Further optimize the module delivery experience, especially in situations where you can anticipate that a user will need a particular module.

After you've read through this guide, see these best practices in action by trying the[Play Core API sample app](https://github.com/android/app-bundle-samples/tree/main/DynamicFeatures).

## Keep the user informed

You should inform the user when a feature is not immediately available. If a user decides to download the feature from Google Play, display the progress of the download.

You can[monitor the request state](https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests)to display the download progress and install state. However, the type of UI you want to display might depend on the size of the download:

- For smaller modules (\~10 MB or less) that can be installed very quickly, consider indicators such as spinners or a brief "downloading content" message.
- For larger modules that can take a few seconds or longer to download and install, consider showing a download and install progress bar, such as the one shown in figure 1.

![](https://developer.android.com/static/studio/images/projects/dynamic-delivery/progress_bar.png)

**Figure 1.**Displaying a message and progress bar when downloading and installing an on demand feature

<br />

## Communicate installation delays and failures gracefully

If a download fails or progresses slower than expected, clearly and transparently communicate to the user what's going on and what, if anything, they can do, as shown in figures 2 and 3. For example, if you[monitor the state of the download request](https://developer.android.com/guide/playcore/feature-delivery/on-demand#monitor_requests), and your app receives a`API_NOT_AVAILABLE`error, notify the user that their device doesn't support on demand downloads.  
![](https://developer.android.com/static/studio/images/projects/dynamic-delivery/failed_download.png)

**Figure 2.**Let the user know why a feature cannot be installed at this time  
![](https://developer.android.com/static/studio/images/projects/dynamic-delivery/large_download.png)

**Figure 3.**Explain to the user why a feature might be taking longer than expected to download

## Show value before permission is requested for large downloads

If an on demand module is large (\> 150MB), Google Play requires that the user first consent before downloading it.

Before you request the module, explain the value of the module to your users. Help them understand why you're making this request of them, as you would when requesting app permissions. Communicating openly with users increases the likelihood that they will accept the download.

For example, imagine you're building an e-commerce app and one of the features allows users to place furniture directly within their apartment using Augmented Reality (AR). You might include a message such as, "Would you like to see your new sofa in your living room? Install the augmented reality viewer now."

## Perform download and install in the background

Module download and installation should always occur in the background. That is, while a user is waiting for a feature to become available, you should allow them to continue using other parts of your app. And, when the feature is available, you should provide a notification that allows the user to switch to using that feature at their discretion.

As shown in figure 5, the user continues to use the app and receives a notification when the installation of an on demand feature is complete.

![](https://developer.android.com/static/studio/images/projects/dynamic-delivery/success_notification.png)

**Figure 5.**Rather than changing the user's context suddenly when a module installation is complete, notify the user that the requested feature is ready for them.

<br />

When the module is ready to use, notify the user and give them the choice whether to launch the feature. This pattern provides the user with context and control over their experience.

In some cases, you*could*launch the feature as soon as it's ready. However, because it might interrupt the user's experience, carefully consider whether this behavior is expected and appropriate.

## Free up device storage when a module is no longer needed

A useful capability of all feature modules is the ability to uninstall them, individually. If a feature module is no longer being used, you can reduce the size of your app on a user's device by requesting Google Play to[uninstall that module](https://developer.android.com/guide/playcore/dynamic-delivery#uninstall_modules).

For example, your app may have a robust onboarding flow, perhaps containing rich media. After a user has completed the onboarding flow, or after they've been active users for a certain amount of time, you can use the Play Feature Delivery API to request Google Play uninstall only that component of your app.

Keep in mind, you can also later uninstall modules that you include at initial app install. For example, a module that trains new users on how to use your app is valuable when users first use your app. However, to reduce app size, you can then uninstall it after they've completed the training.

## Advanced tips

Typically, you need to handle situations where the user explicitly signals intent to use the functionality of your on demand feature modules.

However, you might want to predict when a user is likely to engage with a feature*before*they signal to you that they want to use it. Using an app that allows you to download and create cooking recipes as an example, the following guidelines describe how to optimize the module delivery experience by anticipating user needs.

**Anticipate a user's need for a feature in the current session**. Consider if users only need to create an account for the recipe app when they want to create and share their own recipes with the community. You can use the account creation as a signal that the user is likely to want to add their own recipe start downloading the feature module before the user even taps on 'add recipe'. You can apply this approach to other user journeys in the app to make the feature download process more seamless.

**Anticipate a user's need for the feature in an upcoming session**. If you do not need your app to immediately download and install an on demand module, you can defer installation for when the app is in the background, and Google Play will handle the download and install for you. For example, imagine that you want to release new seasonal recipes for the cooking app, which aren't a high priority for the user's current session. You can request for Play to download and install these recipes when the app is in the background. This is especially useful for larger features (\>10MB) which aren't needed right away but will likely be needed in the future.
| **Note:** Requests for deferred installs are best-effort and you cannot track their progress. Before trying to access a module you had marked for deferred installation,[check that the module has been installed](https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage_installed_modules). If it hasn't, you can always install it on-demand at that time.

**Anticipate a user's need for a feature ahead of app installation** . You might want to[add support for conditional delivery](https://developer.android.com/studio/projects/dynamic-delivery/conditional-delivery)to include your feature at install time based on user country, device hardware capability, and API level. For example, you might want to include recipes that use pork in conditional modules and omit that module from app install in regions that predominantly avoid pork dishes.