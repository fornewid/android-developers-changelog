---
title: https://developer.android.com/guide/playcore/in-app-review/unreal-engine
url: https://developer.android.com/guide/playcore/in-app-review/unreal-engine
source: md.txt
---

# Integrate in-app reviews (Unreal Engine)

This guide describes how to integrate in-app reviews in your app using Unreal Engine. There are separate integration guides for if you are using[Kotlin or Java](https://developer.android.com/guide/playcore/in-app-review/kotlin-java),[native code](https://developer.android.com/guide/playcore/in-app-review/native)or[Unity](https://developer.android.com/guide/playcore/in-app-review/unity).

## Unreal Engine SDK overview

The Play In-App Reviews API is part of Play Core SDK family. The API for Unreal Engine offers a`UInAppReviewsManager`class to request and launch the flow using the`RequestReviewFlow`and`LaunchReviewFlow`methods. After a request is made, your app can check the status of the request using`EInAppReviewErrorCode`.

## Supported Unreal Engine versions

The plugin supports**Unreal Engine 5.0**and all subsequent versions.

## Set up your development environment

| **Note:** If you have already used the In-app Reviews or In-app Updates plugins in Unreal Engine, you can skip to the final step.

1. Download the[Play Unreal Engine Plugin](https://github.com/google/play-unreal-engine-plugin)from the GitHub repository.

2. Copy the`GooglePlay`folder inside your`Plugins`folder in your Unreal Engine project.

3. Open your Unreal Engine project and click**Edit → Plugins**.

4. Search for**Google Play** and check the**Enabled**checkbox.

5. Restart the game project and trigger a build.

6. Open your project's`Build.cs`file and add the`PlayInAppReviews`module to`PublicDependencyModuleNames`:

       using UnrealBuildTool;

       public class MyGame : ModuleRules
       {
         public MyGame(ReadOnlyTargetRules Target) : base(Target)
         {
           // ...

           PublicDependencyModuleNames.Add("PlayInAppReviews");

           // ...
         }
       }

## Request the in-app review flow

Follow the guidance about[when to request in-app reviews](https://developer.android.com/guide/playcore/in-app-review#when-to-request)to determine good points in your app's user flow to prompt the user for a review (for example, after a user dismisses the summary screen at the end of a level in a game). When your app gets close one of these points, use the`UInAppReviewsManager`create an operation, as shown in the following example:

MyClass.h  

    void MyClass::OnReviewOperationCompleted(EInAppReviewErrorCode ErrorCode)
    {
      // ...
    }

MyClass.cpp  

    void MyClass::RequestReviewFlow()
    {
      // Create a delegate to bind the callback function.
      FReviewOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnReviewOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnReviewOperationCompleted);

      // Initiate the review flow, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppReviewsManager>()
        ->RequestReviewFlow(Delegate);
    }

1. The method creates a`FRreviewOperationCompletedDelegate`to handle the completion of the review operation.

2. The delegate is bound to the`OnReviewOperationCompleted`method, which will be called once the operation finishes.

3. The`BindDynamic`function ensures that the delegate is properly linked to the callback.

4. The`RequestReviewFlow(Delegate)`method starts the review process, passing the delegate to handle the result.

5. The review operation runs asynchronously, allowing other tasks in the app to continue while it completes.

6. Once the operation finishes, the`OnReviewOperationCompleted`callback processes the result, including success or failure.

## Launch the in-app review flow

Once the`RequestReviewFlow`operation is complete, you can launch the in-app review flow. This is done by binding a delegate to handle the completion event, ensuring the app reacts to the outcome (success or failure) of the review request.

MyClass.h  

    void MyClass::OnReviewOperationCompleted(EInAppReviewErrorCode ErrorCode)
    {
      // ...
    }

MyClass.cpp  

    void MyClass::LaunchReviewFlow()
    {
      // Create a delegate to bind the callback function.
      FReviewOperationCompletedDelegate Delegate;

      // Bind the completion handler (OnReviewOperationCompleted) to the delegate.
      Delegate.BindDynamic(this, &MyClass::OnReviewOperationCompleted);

      // Launch the review flow, passing the delegate to handle the result.
      GetGameInstance()
        ->GetSubsystem<UInAppReviewsManager>()
        ->LaunchReviewFlow(Delegate);
    }

## Next steps

[Test your app's in-app review flow](https://developer.android.com/guide/playcore/in-app-review/test)to verify that your integration is working correctly.