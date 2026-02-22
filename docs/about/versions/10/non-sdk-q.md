---
title: https://developer.android.com/about/versions/10/non-sdk-q
url: https://developer.android.com/about/versions/10/non-sdk-q
source: md.txt
---

# Updates to non-SDK interface restrictions in Android 10

To help ensure app stability and compatibility, the platform started restricting which[non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)your app can use in Android 9 (API level 28). Android 10 includes updated lists of restricted non-SDK interfaces based on collaboration with Android developers and the latest internal testing. Our goal is to make sure that public alternatives are available before we restrict non-SDK interfaces.

If you will not be targeting Android 10 (API level 29), some of these changes might not immediately affect you. However, while you can currently use some non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)), using any non-SDK method or field always carries a high risk of breaking your app.

If you are unsure if your app uses non-SDK interfaces, you can[test your app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)to find out. If your app relies on non-SDK interfaces, you should begin planning a migration to SDK alternatives. Nevertheless, we understand that some apps have valid use cases for using non-SDK interfaces. If you cannot find an alternative to using a non-SDK interface for a feature in your app, you should[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

## Naming changes for non-SDK interface lists

In Android 9 (API level 28), the non-SDK interface lists (greylists) were split between the following two lists:

- A list of unsupported non-SDK interfaces (light greylist) that could be used regardless of target API level.
- A list of blocked non-SDK interfaces (dark greylist) that could not be used if your app targeted API level 28 or higher.

Starting in Android 10, non-SDK interfaces that are restricted by target API level (previously the darkgrey list) are now referred to by the maximum target SDK version that the interface can be used in.

**Example**

If a non-SDK interface was blocked when an app targeted Android 9 (API level 28), that interface is now part of the`max-target-o`(`greylist-max-o`) list, where "o" stands for Oreo or Android 8.1 (API level 27). In this case, you would only be able to use an interface that belongs to the`max-target-o`(`greylist-max-o`) list if your app targets Android 8.1 (API level 27) or lower.

Similarly, if a non-SDK interface was not blocked in Android Pie but is now blocked in Android 10, that interface is part of the`max-target-p`(`greylist-max-p`) list, where "p" stands for Pie or Android 9 (API level 28).

These names should provide more insight about the maximum target SDK level a non-SDK API can be used in before it is blocked by the platform.

### Code annotations for non-SDK interfaces

In addition to the list name changes, many non-SDK interfaces are now annotated in the code using the following annotations.

|                          Annotation                          |                                              Meaning                                               |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `@UnsupportedAppUsage`                                       | Unsupported non-SDK interfaces                                                                     |
| `@UnsupportedAppUsage(maxTargetSdk = 0)`                     | Blocklist                                                                                          |
| `@UnsupportedAppUsage(maxTargetSdk = Build.VERSION_CODES.O)` | Conditionally blocked. Only accessible by apps targeting Android 8.1 Oreo (API level 27) or lower. |
| `@UnsupportedAppUsage(maxTargetSdk = Build.VERSION_CODES.P)` | Conditionally blocked. Only accessible by apps targeting Android 9 Pie (API level 28) or lower.    |

Due to the large number of non-SDK interfaces that are conditionally blocked in Android 8.1 Oreo (API level 27), many of the interfaces in that list were not annotated. While these new annotations can provide a quick reference point, you should[test your app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)if you are unsure whether your app uses non-SDK interfaces.

## Enabling access to non-SDK interfaces in Android 10

In Android 10, the commands that you can use to enable access to non-SDK interfaces have changed. You can enable access to non-SDK interfaces on development devices by changing the API enforcement policy. To do so, use the following ADB command:  

```
adb shell settings put global hidden_api_policy  1
```

To reset the API enforcement policy to the default settings, use the following command:  

```
adb shell settings delete global hidden_api_policy
```

These commands do not require a rooted device.

You can set the integer in the API enforcement policy to one of the following values:

- 0: Disable all detection of non-SDK interfaces. Using this setting disables all log messages for non-SDK interface usage and prevents you from testing your app[using the`StrictMode`API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-strictmode-api). This setting is not recommended.
- 1: Enable access to all non-SDK interfaces, but print log messages with warnings for any non-SDK interface usage. Using this setting also allows you to test your app[using the`StrictMode`API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-strictmode-api).
- 2: Disallow usage of non-SDK interfaces that belong to either the blocklist or are conditionally blocked for your[target API level](https://developer.android.com/distribute/best-practices/develop/target-sdk).

## List changes for Android 10

The list changes in Android 10 fall into the following categories:

- Non-SDK interfaces that were unsupported (greylisted) in Android 9 (API level 28) that are now[blocked in Android 10 (API level 29)](https://developer.android.com/about/versions/10/non-sdk-q#new-blocked).
- Non-SDK interfaces that were[added to the Android SDK in Android 10](https://developer.android.com/about/versions/10/non-sdk-q#new-sdk).

For a complete list of all non-SDK interfaces for Android 10, download the following file:[`hiddenapi-flags.csv`](https://dl.google.com/developers/android/qt/non-sdk/hiddenapi-flags.csv).

### Non-SDK interfaces that are now blocked in Android 10

The following code box lists all of the non-SDK interfaces that were unsupported (greylisted) in Android 9 (API level 28) that are blocked in Android 10 (API level 29). That is, these interfaces belong to the`max-target-p`(`greylist-max-p`) list, so your app can only use these interfaces if it targets Android 9 (API level 28) or lower.

Wherever possible, alternative APIs are suggested in a comment following the name of the interface. False positives are noted for interfaces that we thought might be in use but turned out not to be. Each interface takes up one line.

Our goal is to make sure that public alternatives are available before we restrict non-SDK interfaces, and we understand that your app might have a valid use case for using these interfaces. If an interface that you currently use in Android 9 is now blocked, you should[request a new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request)for that interface.  

```
Landroid/accessibilityservice/AccessibilityService;->mWindowToken:Landroid/os/IBinder;   # False Positive
Landroid/accounts/AccountManager$AmsTask;->mActivity:Landroid/app/Activity;   # False Positive
Landroid/accounts/AccountManager$AmsTask;->mHandler:Landroid/os/Handler;   # False Positive
Landroid/accounts/AccountManager$AmsTask;->mResponse:Landroid/accounts/IAccountManagerResponse;   # False Positive
Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;->mAuthTokenType:Ljava/lang/String;   # False Positive
Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;->mLoginOptions:Landroid/os/Bundle;   # False Positive
Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;->mMyCallback:Landroid/accounts/AccountManagerCallback;   # False Positive
Landroid/accounts/AuthenticatorDescription;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/accounts/AuthenticatorDescription;-><init>(Ljava/lang/String;)V   # False Positive
Landroid/animation/LayoutTransition;->cancel()V   # This is used by androidx.transitions only for the API levels less than 18, so it is safe to restrict it after P. If developers are using it directly we encourage them to migrate to AndroidX Transition library instead
Landroid/animation/LayoutTransition;->cancel(I)V   # This is used by androidx.transitions only for the API levels less than 18, so it is safe to restrict it after P. If developers are using it directly we encourage them to migrate to AndroidX Transition library instead
Landroid/animation/ValueAnimator;->sDurationScale:F   # Use ValueAnimator.areAnimatorsEnabled() (introduced in API 26) to query whether duration scale = 0. Otherwise, it is intended not to expose impl details such as the actual duration scales to devs.
Landroid/app/Activity;->mVisibleFromClient:Z   # False Positive
Landroid/app/Activity;->mVoiceInteractor:Landroid/app/VoiceInteractor;   # False Positive
Landroid/app/Activity;->setParent(Landroid/app/Activity;)V   # False Positive
Landroid/app/ActivityManager$TaskDescription;->getBackgroundColor()I   # False Positive
Landroid/app/ActivityThread$ActivityClientRecord;-><init>()V   # False Positive
Landroid/app/ActivityThread$AppBindData;->compatInfo:Landroid/content/res/CompatibilityInfo;   # False Positive
Landroid/app/ActivityThread;->getPackageInfo(Ljava/lang/String;Landroid/content/res/CompatibilityInfo;I)Landroid/app/LoadedApk;   # False Positive
Landroid/app/ActivityThread;->handleReceiver(Landroid/app/ActivityThread$ReceiverData;)V   # False Positive
Landroid/app/ActivityThread;->mLocalProviders:Landroid/util/ArrayMap;   # False Positive
Landroid/app/ActivityThread;->mResourcesManager:Landroid/app/ResourcesManager;   # False Positive
Landroid/app/ActivityThread;->peekPackageInfo(Ljava/lang/String;Z)Landroid/app/LoadedApk;   # False Positive
Landroid/app/ActivityThread;->sMainThreadHandler:Landroid/os/Handler;   # False Positive
Landroid/app/admin/DeviceAdminInfo$PolicyInfo;->tag:Ljava/lang/String;   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordHistoryLength(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumLength(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumLetters(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumLowerCase(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumNonLetter(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumNumeric(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumSymbols(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordMinimumUpperCase(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/admin/DevicePolicyManager;->getPasswordQuality(Landroid/content/ComponentName;I)I   # False Positive
Landroid/app/assist/AssistContent;->mClipData:Landroid/content/ClipData;   # False Positive
Landroid/app/assist/AssistContent;->mExtras:Landroid/os/Bundle;   # False Positive
Landroid/app/assist/AssistContent;->mIntent:Landroid/content/Intent;   # False Positive
Landroid/app/assist/AssistContent;->mIsAppProvidedIntent:Z   # False Positive
Landroid/app/assist/AssistContent;->mStructuredData:Ljava/lang/String;   # False Positive
Landroid/app/assist/AssistContent;->mUri:Landroid/net/Uri;   # False Positive
Landroid/app/assist/AssistContent;->writeToParcelInternal(Landroid/os/Parcel;I)V   # False Positive
Landroid/app/ContentProviderHolder;->noReleaseNeeded:Z   # False Positive
Landroid/app/ContextImpl;->mFlags:I   # False Positive
Landroid/app/ContextImpl;->mOpPackageName:Ljava/lang/String;   # False Positive
Landroid/app/ContextImpl;->mSharedPrefsPaths:Landroid/util/ArrayMap;   # False Positive
Landroid/app/Dialog;->CANCEL:I   # False Positive
Landroid/app/Dialog;->mHandler:Landroid/os/Handler;   # False Positive
Landroid/app/DownloadManager$Query;->orderBy(Ljava/lang/String;I)Landroid/app/DownloadManager$Query;   # False Positive
Landroid/app/DownloadManager;->setAccessFilename(Z)V   # False Positive
Landroid/app/Fragment;->mView:Landroid/view/View;   # False Positive
Landroid/app/Fragment;->sClassMap:Landroid/util/ArrayMap;   # False Positive
Landroid/app/IInstrumentationWatcher$Stub;->asInterface(Landroid/os/IBinder;)Landroid/app/IInstrumentationWatcher;   # False Positive
Landroid/app/Instrumentation;->checkStartActivityResult(ILjava/lang/Object;)V   # False Positive
Landroid/app/ISearchManager$Stub;-><init>()V   # False Positive
Landroid/app/IUiModeManager$Stub;->asInterface(Landroid/os/IBinder;)Landroid/app/IUiModeManager;   # False Positive
Landroid/app/IUiModeManager;->disableCarMode(I)V   # False Positive
Landroid/app/job/JobInfo;->flags:I   # False Positive
Landroid/app/job/JobWorkItem;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/app/job/JobWorkItem;->mDeliveryCount:I   # False Positive
Landroid/app/job/JobWorkItem;->mGrants:Ljava/lang/Object;   # False Positive
Landroid/app/job/JobWorkItem;->mIntent:Landroid/content/Intent;   # False Positive
Landroid/app/job/JobWorkItem;->mWorkId:I   # False Positive
Landroid/app/KeyguardManager;->isDeviceLocked(I)Z   # False Positive
Landroid/app/LoadedApk$ReceiverDispatcher;->mContext:Landroid/content/Context;   # False Positive
Landroid/app/LoadedApk$ServiceDispatcher;->mContext:Landroid/content/Context;   # False Positive
Landroid/app/LoadedApk;->mDataDirFile:Ljava/io/File;   # False Positive
Landroid/app/LoadedApk;->mServices:Landroid/util/ArrayMap;   # False Positive
Landroid/app/Notification$Action;->mIcon:Landroid/graphics/drawable/Icon;   # False Positive
Landroid/app/ProgressDialog;->mProgress:Landroid/widget/ProgressBar;   # False Positive
Landroid/app/ResultInfo;->CREATOR:Landroid/os/Parcelable$Creator;   # False Positive
Landroid/app/UiAutomation;-><init>(Landroid/os/Looper;Landroid/app/IUiAutomationConnection;)V   # False Positive
Landroid/app/UiAutomation;->connect()V   # False Positive
Landroid/app/UiAutomation;->disconnect()V   # False Positive
Landroid/app/usage/ConfigurationStats;->mActivationCount:I   # False Positive
Landroid/app/usage/ConfigurationStats;->mBeginTimeStamp:J   # False Positive
Landroid/app/usage/ConfigurationStats;->mConfiguration:Landroid/content/res/Configuration;   # False Positive
Landroid/app/usage/ConfigurationStats;->mEndTimeStamp:J   # False Positive
Landroid/app/usage/ConfigurationStats;->mLastTimeActive:J   # False Positive
Landroid/app/usage/ConfigurationStats;->mTotalTimeActive:J   # False Positive
Landroid/app/usage/UsageEvents$Event;->mClass:Ljava/lang/String;   # False Positive
Landroid/app/usage/UsageEvents$Event;->mConfiguration:Landroid/content/res/Configuration;   # False Positive
Landroid/app/usage/UsageEvents$Event;->mEventType:I   # False Positive
Landroid/app/usage/UsageEvents$Event;->mPackage:Ljava/lang/String;   # False Positive
Landroid/app/usage/UsageEvents$Event;->mTimeStamp:J   # False Positive
Landroid/app/usage/UsageEvents;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/app/usage/UsageEvents;->findStringIndex(Ljava/lang/String;)I   # False Positive
Landroid/app/usage/UsageEvents;->mEventCount:I   # False Positive
Landroid/app/usage/UsageEvents;->mEventsToWrite:Ljava/util/List;   # False Positive
Landroid/app/usage/UsageEvents;->mIndex:I   # False Positive
Landroid/app/usage/UsageEvents;->mStringPool:[Ljava/lang/String;   # False Positive
Landroid/app/usage/UsageEvents;->readEventFromParcel(Landroid/os/Parcel;Landroid/app/usage/UsageEvents$Event;)V   # False Positive
Landroid/app/usage/UsageEvents;->writeEventToParcel(Landroid/app/usage/UsageEvents$Event;Landroid/os/Parcel;I)V   # False Positive
Landroid/app/usage/UsageStats;->mBeginTimeStamp:J   # False Positive
Landroid/app/usage/UsageStats;->mEndTimeStamp:J   # False Positive
Landroid/app/usage/UsageStats;->mLastTimeUsed:J   # False Positive
Landroid/app/usage/UsageStats;->mPackageName:Ljava/lang/String;   # False Positive
Landroid/app/usage/UsageStatsManager;->mContext:Landroid/content/Context;   # False Positive
Landroid/app/usage/UsageStatsManager;->sEmptyResults:Landroid/app/usage/UsageEvents;   # False Positive
Landroid/app/WallpaperManager;->setBitmap(Landroid/graphics/Bitmap;Landroid/graphics/Rect;ZII)I   # False Positive
Landroid/bluetooth/BluetoothA2dp;->getPriority(Landroid/bluetooth/BluetoothDevice;)I   # False Positive
Landroid/bluetooth/BluetoothA2dp;->stateToString(I)Ljava/lang/String;   # False Positive
Landroid/bluetooth/BluetoothClass;-><init>(I)V   # False Positive
Landroid/bluetooth/BluetoothGatt;->mAuthRetryState:I   # False Positive
Landroid/bluetooth/BluetoothProfile;->PAN:I   # False Positive
Landroid/bluetooth/BluetoothUuid;->AdvAudioDist:Landroid/os/ParcelUuid;   # False Positive
Landroid/bluetooth/BluetoothUuid;->AudioSink:Landroid/os/ParcelUuid;   # False Positive
Landroid/bluetooth/BluetoothUuid;->Handsfree:Landroid/os/ParcelUuid;   # False Positive
Landroid/bluetooth/BluetoothUuid;->HSP:Landroid/os/ParcelUuid;   # False Positive
Landroid/bluetooth/IBluetooth$Stub;-><init>()V   # False Positive
Landroid/bluetooth/IBluetoothA2dp$Stub;-><init>()V   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;-><init>(ILjava/lang/String;Landroid/os/Bundle;IZZLandroid/os/IBinder;II)V   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;->mFlags:I   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;->mResultCode:I   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;->mResultData:Ljava/lang/String;   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;->mToken:Landroid/os/IBinder;   # False Positive
Landroid/content/BroadcastReceiver$PendingResult;->mType:I   # False Positive
Landroid/content/ClipData$Item;->mUri:Landroid/net/Uri;   # False Positive
Landroid/content/ContentProvider;-><init>(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;[Landroid/content/pm/PathPermission;)V   # False Positive
Landroid/content/ContentProviderClient;->mPackageName:Ljava/lang/String;   # False Positive
Landroid/content/Context;->COUNTRY_DETECTOR:Ljava/lang/String;   # False Positive
Landroid/content/Entity;->mSubValues:Ljava/util/ArrayList;   # False Positive
Landroid/content/Entity;->mValues:Landroid/content/ContentValues;   # False Positive
Landroid/content/IContentProvider;->descriptor:Ljava/lang/String;   # False Positive
Landroid/content/IIntentReceiver$Stub;->asInterface(Landroid/os/IBinder;)Landroid/content/IIntentReceiver;   # False Positive
Landroid/content/IIntentSender$Stub;->asInterface(Landroid/os/IBinder;)Landroid/content/IIntentSender;   # False Positive
Landroid/content/IntentFilter;->isVerified()Z   # False Positive
Landroid/content/pm/ApplicationInfo$DisplayNameComparator;->mPM:Landroid/content/pm/PackageManager;   # False Positive
Landroid/content/pm/ApplicationInfo$DisplayNameComparator;->sCollator:Ljava/text/Collator;   # False Positive
Landroid/content/pm/ApplicationInfo;->disableCompatibilityMode()V   # False Positive
Landroid/content/pm/ApplicationInfo;->isPackageUnavailable(Landroid/content/pm/PackageManager;)Z   # False Positive
Landroid/content/pm/LauncherApps;->mService:Landroid/content/pm/ILauncherApps;   # False Positive
Landroid/content/pm/PackageInfo;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/content/pm/PackageInfoLite;->CREATOR:Landroid/os/Parcelable$Creator;   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->active:Z   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->appIcon:Landroid/graphics/Bitmap;   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->appLabel:Ljava/lang/CharSequence;   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->appPackageName:Ljava/lang/String;   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->installerPackageName:Ljava/lang/String;   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->mode:I   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->progress:F   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->sessionId:I   # False Positive
Landroid/content/pm/PackageInstaller$SessionInfo;->sizeBytes:J   # False Positive
Landroid/content/pm/PackageInstaller$SessionParams;->appLabel:Ljava/lang/String;   # False Positive
Landroid/content/pm/PackageInstaller$SessionParams;->appPackageName:Ljava/lang/String;   # False Positive
Landroid/content/pm/PackageInstaller$SessionParams;->mode:I   # False Positive
Landroid/content/pm/PackageParser;->parseBaseApk(Ljava/lang/String;Landroid/content/res/Resources;Landroid/content/res/XmlResourceParser;I[Ljava/lang/String;)Landroid/content/pm/PackageParser$Package;   # False Positive
Landroid/content/pm/PackageStats;->userHandle:I   # False Positive
Landroid/content/pm/ParceledListSlice;->CREATOR:Landroid/os/Parcelable$ClassLoaderCreator;   # False Positive
Landroid/content/pm/ShortcutInfo;->getIcon()Landroid/graphics/drawable/Icon;   # False Positive
Landroid/content/pm/ShortcutManager;->mService:Landroid/content/pm/IShortcutService;   # False Positive
Landroid/content/res/CompatibilityInfo;->CREATOR:Landroid/os/Parcelable$Creator;   # False Positive
Landroid/content/RestrictionsManager;->mService:Landroid/content/IRestrictionsManager;   # False Positive
Landroid/content/SyncAdapterType;-><init>(Ljava/lang/String;Ljava/lang/String;)V   # False Positive
Landroid/content/SyncAdapterType;->supportsUploading:Z   # False Positive
Landroid/content/SyncAdapterType;->userVisible:Z   # False Positive
Landroid/content/SyncInfo;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/content/SyncRequest;->mAuthority:Ljava/lang/String;   # False Positive
Landroid/content/SyncRequest;->mExtras:Landroid/os/Bundle;   # False Positive
Landroid/database/AbstractCursor;->mExtras:Landroid/os/Bundle;   # False Positive
Landroid/database/DatabaseUtils;->getTypeOfObject(Ljava/lang/Object;)I   # False Positive
Landroid/database/MatrixCursor;->data:[Ljava/lang/Object;   # False Positive
Landroid/database/MatrixCursor;->rowCount:I   # False Positive
Landroid/database/sqlite/SQLiteCustomFunction;->name:Ljava/lang/String;   # False Positive
Landroid/database/sqlite/SQLiteQueryBuilder;->computeProjection([Ljava/lang/String;)[Ljava/lang/String;   # False Positive
Landroid/database/sqlite/SQLiteQueryBuilder;->mDistinct:Z   # False Positive
Landroid/database/sqlite/SQLiteQueryBuilder;->mTables:Ljava/lang/String;   # False Positive
Landroid/database/sqlite/SQLiteQueryBuilder;->mWhereClause:Ljava/lang/StringBuilder;   # False Positive
Landroid/graphics/Bitmap;->mNinePatchChunk:[B   # Bitmap#getNinePatchChunk already exists since API level 1
Landroid/graphics/BitmapRegionDecoder;-><init>(J)V   # False Positive
Landroid/graphics/Canvas;-><init>(J)V   # False Positive
Landroid/graphics/Canvas;->mBitmap:Landroid/graphics/Bitmap;   # Canvas#setBitmap(Bitmap) to set, and for getters we consider it an anti-pattern on Canvas and recommend instead explicit side channel for that information if the app needs it.
Landroid/graphics/drawable/AnimatedStateListDrawable;->mState:Landroid/graphics/drawable/AnimatedStateListDrawable$AnimatedStateListState;   # False Positive
Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;-><init>(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;Landroid/graphics/drawable/DrawableContainer;Landroid/content/res/Resources;)V   # False Positive
Landroid/graphics/drawable/GradientDrawable$GradientState;->mAngle:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getOrientation() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mGradient:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getGradientType() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mGradientColors:[I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getColors() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mHeight:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getIntrinsicHeight() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mInnerRadius:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getInnerRadius() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mInnerRadiusRatio:F   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getInnerRadiusRatio() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mOrientation:Landroid/graphics/drawable/GradientDrawable$Orientation;   # Use GradientDrawable#getOrientation which is public and added in API level 16
Landroid/graphics/drawable/GradientDrawable$GradientState;->mPadding:Landroid/graphics/Rect;   # Use https://developer.android.com/reference/android/graphics/drawable/Drawable#getPadding(android.graphics.Rect) instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mRadius:F   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getGradientRadius() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mRadiusArray:[F   # GradientDrawable#getCornerRadii added in API level 24
Landroid/graphics/drawable/GradientDrawable$GradientState;->mShape:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getShape() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mSolidColors:Landroid/content/res/ColorStateList;   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getColor() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mThickness:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getThickness() instead.
Landroid/graphics/drawable/GradientDrawable$GradientState;->mThicknessRatio:F   # GradientDrawable#getThicknessRatio is public in Android 10
Landroid/graphics/drawable/GradientDrawable$GradientState;->mWidth:I   # Use https://developer.android.com/reference/android/graphics/drawable/GradientDrawable.html#getIntrinsicWidth() instead.
Landroid/graphics/drawable/GradientDrawable;->mGradientState:Landroid/graphics/drawable/GradientDrawable$GradientState;   # Use https://developer.android.com/reference/android/graphics/drawable/Drawable#getConstantState() instead.
Landroid/graphics/drawable/GradientDrawable;->mPadding:Landroid/graphics/Rect;   # Use https://developer.android.com/reference/android/graphics/drawable/Drawable#getPadding(android.graphics.Rect) instead.
Landroid/graphics/drawable/Icon;->getDataBytes()[B   # False Positive
Landroid/graphics/drawable/Icon;->getDataOffset()I   # False Positive
Landroid/graphics/drawable/Icon;->getResources()Landroid/content/res/Resources;   # False Positive
Landroid/graphics/drawable/Icon;->mString1:Ljava/lang/String;   # False Positive
Landroid/graphics/drawable/Icon;->mType:I   # False Positive
Landroid/graphics/fonts/FontVariationAxis;->mTag:I   # False Positive
Landroid/graphics/Movie;-><init>(J)V   # False Positive
Landroid/graphics/Paint;->mTypeface:Landroid/graphics/Typeface;   # False Positive
Landroid/graphics/Picture;->mNativePicture:J   # No public alternative as it's a pointer to a private native object. We suspect this was a false-positive.
Landroid/graphics/Typeface;-><init>(J)V   # False Positive
Landroid/graphics/Typeface;->setDefault(Landroid/graphics/Typeface;)V   # Please use font in xml and also your application global theme to change the default Typeface. android:textViewStyle and its attribute android:textAppearance can be used in order to change typeface and other text related properties.
Landroid/hardware/Camera;->mNativeContext:J   # False Positive
Landroid/hardware/Camera;->setPreviewSurface(Landroid/view/Surface;)V   # False Positive
Landroid/hardware/HardwareBuffer;-><init>(J)V   # False Positive
Landroid/hardware/input/InputManager;->mIm:Landroid/hardware/input/IInputManager;   # False Positive
Landroid/hardware/usb/UsbManager;-><init>(Landroid/content/Context;Landroid/hardware/usb/IUsbManager;)V   # False Positive
Landroid/inputmethodservice/InputMethodService;->mTheme:I   # False Positive
Landroid/inputmethodservice/InputMethodService;->mTmpInsets:Landroid/inputmethodservice/InputMethodService$Insets;   # False Positive
Landroid/inputmethodservice/Keyboard;->resize(II)V   # False Positive
Landroid/location/CountryDetector;-><init>(Landroid/location/ICountryDetector;)V   # False Positive
Landroid/location/GpsStatus;->setTimeToFirstFix(I)V   # False Positive
Landroid/location/Location;->mProvider:Ljava/lang/String;   # False Positive
Landroid/location/LocationManager;->sendNiResponse(II)Z   # False Positive
Landroid/location/LocationRequest;->checkDisplacement(F)V   # False Positive
Landroid/location/LocationRequest;->checkInterval(J)V   # False Positive
Landroid/location/LocationRequest;->checkProvider(Ljava/lang/String;)V   # False Positive
Landroid/location/LocationRequest;->checkQuality(I)V   # False Positive
Landroid/location/LocationRequest;->mExpireAt:J   # False Positive
Landroid/location/LocationRequest;->mExplicitFastestInterval:Z   # False Positive
Landroid/location/LocationRequest;->mFastestInterval:J   # False Positive
Landroid/location/LocationRequest;->mNumUpdates:I   # False Positive
Landroid/location/LocationRequest;->mQuality:I   # False Positive
Landroid/location/LocationRequest;->mSmallestDisplacement:F   # False Positive
Landroid/media/AudioAttributes;->mContentType:I   # False Positive
Landroid/media/AudioAttributes;->mFlags:I   # False Positive
Landroid/media/AudioAttributes;->mSource:I   # False Positive
Landroid/media/audiofx/AudioEffect;->command(I[B[B)I   # False Positive
Landroid/media/CamcorderProfile;->native_init()V   # False Positive
Landroid/media/ExifInterface;->convertRationalLatLonToFloat(Ljava/lang/String;Ljava/lang/String;)F   # False Positive
Landroid/media/ExifInterface;->mFilename:Ljava/lang/String;   # False Positive
Landroid/media/ExifInterface;->mHasThumbnail:Z   # False Positive
Landroid/media/ExifInterface;->sFormatter:Ljava/text/SimpleDateFormat;   # False Positive
Landroid/media/MediaCodec;->mNativeContext:J   # False Positive
Landroid/media/MediaCodecInfo$VideoCapabilities;->create(Landroid/media/MediaFormat;Landroid/media/MediaCodecInfo$CodecCapabilities;)Landroid/media/MediaCodecInfo$VideoCapabilities;   # False Positive
Landroid/media/MediaMetadataRetriever;->native_finalize()V   # False Positive
Landroid/media/MediaMetadataRetriever;->native_init()V   # False Positive
Landroid/media/MediaMetadataRetriever;->native_setup()V   # False Positive
Landroid/media/MediaRecorder;->_prepare()V   # False Positive
Landroid/media/MediaRecorder;->mEventHandler:Landroid/media/MediaRecorder$EventHandler;   # False Positive
Landroid/media/MediaRecorder;->mFd:Ljava/io/FileDescriptor;   # False Positive
Landroid/media/MediaRecorder;->mPath:Ljava/lang/String;   # False Positive
Landroid/media/MediaRecorder;->native_finalize()V   # False Positive
Landroid/media/MediaRecorder;->native_init()V   # False Positive
Landroid/media/MediaRecorder;->native_reset()V   # False Positive
Landroid/media/MediaRouter$RouteInfo;->isDefault()Z   # False Positive
Landroid/media/PlaybackParams;->mSet:I   # False Positive
Landroid/media/PlaybackParams;->mSpeed:F   # False Positive
Landroid/media/ThumbnailUtils;->closeSilently(Landroid/os/ParcelFileDescriptor;)V   # False Positive
Landroid/media/ThumbnailUtils;->computeInitialSampleSize(Landroid/graphics/BitmapFactory$Options;II)I   # False Positive
Landroid/media/ThumbnailUtils;->computeSampleSize(Landroid/graphics/BitmapFactory$Options;II)I   # False Positive
Landroid/media/ThumbnailUtils;->createThumbnailFromEXIF(Ljava/lang/String;IILandroid/media/ThumbnailUtils$SizedThumbnailBitmap;)V   # False Positive
Landroid/media/ThumbnailUtils;->makeInputStream(Landroid/net/Uri;Landroid/content/ContentResolver;)Landroid/os/ParcelFileDescriptor;   # False Positive
Landroid/media/ThumbnailUtils;->transform(Landroid/graphics/Matrix;Landroid/graphics/Bitmap;III)Landroid/graphics/Bitmap;   # False Positive
Landroid/net/ConnectivityManager;->getActiveLinkProperties()Landroid/net/LinkProperties;   # Use  getLinkProperties(getActiveNetwork())
Landroid/net/ConnectivityManager;->getLinkProperties(I)Landroid/net/LinkProperties;   # Use getLinkProperties(Network) instead
Landroid/net/ConnectivityManager;->isNetworkSupported(I)Z   # This legacy method returns results that don't make sense in modern Android. To find out about available networks, please use ConnectivityManager#registerNetworkCallback.
Landroid/net/ConnectivityManager;->isNetworkTypeMobile(I)Z   # Please use NetworkCapabilities with TRANSPORT_CELLULAR instead. If you want to know if a network is metered, use NET_CAPABILITY_NOT_METERED.
Landroid/net/ConnectivityManager;->mService:Landroid/net/IConnectivityManager;   # This is an internal interface with methods that can change at any time. Please use the public methods in ConnectivityManager instead.
Landroid/net/ConnectivityManager;->TYPE_MOBILE_CBS:I   # Use NetworkCapabilities#NET_CAPABILITY_CBS instead.
Landroid/net/ConnectivityManager;->TYPE_MOBILE_EMERGENCY:I   # Use NetworkCapabilities#NET_CAPABILITY_EIMS instead.
Landroid/net/ConnectivityManager;->TYPE_MOBILE_FOTA:I   # Use NetworkCapabilities#NET_CAPABILITY_FOTA instead.
Landroid/net/ConnectivityManager;->TYPE_NONE:I   # Use the NetworkCapabilities API instead -- this is not needed any more.
Landroid/net/ConnectivityManager;->unregisterNetworkFactory(Landroid/os/Messenger;)V   # False Positive
Landroid/net/http/SslError;->mErrors:I   # False Positive
Landroid/net/http/SslError;->mUrl:Ljava/lang/String;   # False Positive
Landroid/net/IConnectivityManager;->getNetworkInfo(I)Landroid/net/NetworkInfo;   # False Positive
Landroid/net/IConnectivityManager;->reportInetCondition(II)V   # False Positive
Landroid/net/LinkAddress;->address:Ljava/net/InetAddress;   # False Positive
Landroid/net/LinkAddress;->isIPv6()Z   # Implementation detail, do not use. Use getAddress() to find about the address.
Landroid/net/LinkAddress;->prefixLength:I   # False Positive
Landroid/net/LinkProperties;->hasGlobalIPv6Address()Z   # Implementation detail, do not use. Use getLinkAddresses() to find out about addresses.
Landroid/net/LinkProperties;->hasIPv4Address()Z   # Implementation detail, do not use. Use getLinkAddresses() to find out about addresses.
Landroid/net/LinkProperties;->hasIPv4DefaultRoute()Z   # Implementation detail, do not use. Use getRoutes() to find out about routes.
Landroid/net/LinkProperties;->hasIPv4DnsServer()Z   # Implementation detail, do not use. Use getDnsServers to find out about DNS servers.
Landroid/net/LinkProperties;->hasIPv6DefaultRoute()Z   # Implementation detail, do not use. Use getRoutes() to find out about routes.
Landroid/net/LinkProperties;->hasIPv6DnsServer()Z   # Implementation detail, do not use. Use getDnsServers to find out about DNS servers.
Landroid/net/LinkProperties;->isIdenticalHttpProxy(Landroid/net/LinkProperties;)Z   # False Positive
Landroid/net/LinkProperties;->isIPv6Provisioned()Z   # Implementation detail, do not use. Use getRoutes(), getLinkAddresses() and getDnsServers() instead.
Landroid/net/LinkProperties;->mIfaceName:Ljava/lang/String;   # False Positive
Landroid/net/NetworkAgent;->sendNetworkInfo(Landroid/net/NetworkInfo;)V   # False Positive
Landroid/net/NetworkCapabilities;->getNetworkSpecifier()Landroid/net/NetworkSpecifier;   # False Positive
Landroid/net/NetworkCapabilities;->mSignalStrength:I   # Use NetworkCapabilities#getSignalStrength() instead.
Landroid/net/NetworkFactory;->dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V   # False Positive
Landroid/net/NetworkFactory;->setScoreFilter(I)V   # False Positive
Landroid/net/NetworkPolicyManager;->registerListener(Landroid/net/INetworkPolicyListener;)V   # False Positive
Landroid/net/NetworkPolicyManager;->unregisterListener(Landroid/net/INetworkPolicyListener;)V   # False Positive
Landroid/net/NetworkRequest;->legacyType:I   # False Positive
Landroid/net/NetworkState;->network:Landroid/net/Network;   # False Positive
Landroid/net/NetworkUtils;->numericToInetAddress(Ljava/lang/String;)Ljava/net/InetAddress;   # Use InetAddresses#parseNumericAddress() instead
Landroid/net/RouteInfo;->isHost()Z   # False Positive
Landroid/net/RouteInfo;->mIsHost:Z   # False Positive
Landroid/net/SSLCertificateSocketFactory;->getAlpnSelectedProtocol(Ljava/net/Socket;)[B   # False Positive
Landroid/net/SSLCertificateSocketFactory;->setChannelIdPrivateKey(Ljava/security/PrivateKey;)V   # False Positive
Landroid/net/SSLCertificateSocketFactory;->TAG:Ljava/lang/String;   # False Positive
Landroid/net/TrafficStats;->getMobileIfaces()[Ljava/lang/String;   # Please use public methods like ConnectivityManager#registerNetworkCallback or ConnectivityManager#getAllNetworks. You can learn about the interfaces with the LinkProperties associated object (NetworkCallback#onLinkPropertiesChanged, ConnectivityManager#getLinkProperties(Network))
Landroid/net/TrafficStats;->getStatsService()Landroid/net/INetworkStatsService;   # This is an internal interface that has methods that can change at any time. Please use NetworkStatsManager instead.
Landroid/net/WebAddress;->mPort:I   # False Positive
Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo;->createRequest(Ljava/lang/String;II)Ljava/lang/String;   # False Positive
Landroid/net/wifi/p2p/nsd/WifiP2pServiceInfo;-><init>(Ljava/util/List;)V   # False Positive
Landroid/net/wifi/p2p/nsd/WifiP2pServiceInfo;->mQueryList:Ljava/util/List;   # False Positive
Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;-><init>(ILjava/lang/String;)V   # False Positive
Landroid/net/wifi/p2p/WifiP2pManager;-><init>(Landroid/net/wifi/p2p/IWifiP2pManager;)V   # False Positive
Landroid/net/wifi/p2p/WifiP2pWfdInfo;-><init>()V   # False Positive
Landroid/net/wifi/WifiConfiguration;->INVALID_RSSI:I   # False Positive
Landroid/net/wifi/WifiInfo;->mBSSID:Ljava/lang/String;   # False Positive
Landroid/nfc/NfcManager;-><init>(Landroid/content/Context;)V   # False Positive
Landroid/os/BatteryStats$Counter;-><init>()V   # False Positive
Landroid/os/BatteryStats$HistoryItem;->clear()V   # False Positive
Landroid/os/BatteryStats$HistoryItem;->next:Landroid/os/BatteryStats$HistoryItem;   # False Positive
Landroid/os/BatteryStats$HistoryItem;->same(Landroid/os/BatteryStats$HistoryItem;)Z   # False Positive
Landroid/os/BatteryStats$HistoryItem;->setTo(JBLandroid/os/BatteryStats$HistoryItem;)V   # False Positive
Landroid/os/BatteryStats$HistoryItem;->setTo(Landroid/os/BatteryStats$HistoryItem;)V   # False Positive
Landroid/os/BatteryStats$Timer;-><init>()V   # False Positive
Landroid/os/BatteryStats$Uid$Pkg;-><init>()V   # False Positive
Landroid/os/BatteryStats$Uid$Proc;-><init>()V   # False Positive
Landroid/os/BatteryStats$Uid$Sensor;-><init>()V   # False Positive
Landroid/os/BatteryStats$Uid$Wakelock;-><init>()V   # False Positive
Landroid/os/BatteryStats;-><init>()V   # False Positive
Landroid/os/BatteryStats;->getMobileRadioActiveTime(JI)J   # False Positive
Landroid/os/BatteryStats;->getNetworkActivityBytes(II)J   # False Positive
Landroid/os/CancellationSignal;->mCancelInProgress:Z   # False Positive
Landroid/os/CancellationSignal;->mIsCanceled:Z   # False Positive
Landroid/os/CancellationSignal;->mOnCancelListener:Landroid/os/CancellationSignal$OnCancelListener;   # False Positive
Landroid/os/CancellationSignal;->mRemote:Landroid/os/ICancellationSignal;   # False Positive
Landroid/os/CancellationSignal;->waitForCancelFinishedLocked()V   # False Positive
Landroid/os/health/SystemHealthManager;->from(Landroid/content/Context;)Landroid/os/health/SystemHealthManager;   # False Positive
Landroid/os/IPowerManager;->nap(J)V   # False Positive
Landroid/os/Parcel;->mCreators:Ljava/util/HashMap;   # False Positive
Landroid/os/PowerManager;->mHandler:Landroid/os/Handler;   # False Positive
Landroid/os/Process;->sendSignalQuiet(II)V   # False Positive
Landroid/os/Registrant;->getHandler()Landroid/os/Handler;   # False Positive
Landroid/os/RegistrantList;->get(I)Ljava/lang/Object;   # False Positive
Landroid/os/RemoteCallback;->mHandler:Landroid/os/Handler;   # False Positive
Landroid/os/storage/DiskInfo;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/os/storage/DiskInfo;->CREATOR:Landroid/os/Parcelable$Creator;   # False Positive
Landroid/os/storage/IObbActionListener$Stub;->asInterface(Landroid/os/IBinder;)Landroid/os/storage/IObbActionListener;   # False Positive
Landroid/os/storage/StorageVolume;->getOwner()Landroid/os/UserHandle;   # False Positive
Landroid/os/SystemProperties;->native_add_change_callback()V   # False Positive
Landroid/os/SystemProperties;->native_get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;   # False Positive
Landroid/os/SystemProperties;->native_get_boolean(Ljava/lang/String;Z)Z   # False Positive
Landroid/os/SystemProperties;->native_get_int(Ljava/lang/String;I)I   # False Positive
Landroid/os/SystemProperties;->native_set(Ljava/lang/String;Ljava/lang/String;)V   # False Positive
Landroid/os/UserHandle;->formatUid(Ljava/io/PrintWriter;I)V   # False Positive
Landroid/os/WorkSource;->sGoneWork:Landroid/os/WorkSource;   # False Positive
Landroid/os/WorkSource;->sNewbWork:Landroid/os/WorkSource;   # False Positive
Landroid/os/WorkSource;->sTmpWorkSource:Landroid/os/WorkSource;   # False Positive
Landroid/os/WorkSource;->updateLocked(Landroid/os/WorkSource;ZZ)Z   # False Positive
Landroid/preference/Preference;->onKey(Landroid/view/View;ILandroid/view/KeyEvent;)Z   # False Positive
Landroid/preference/PreferenceManager;->mFragment:Landroid/preference/PreferenceFragment;   # False Positive
Landroid/preference/PreferenceManager;->setFragment(Landroid/preference/PreferenceFragment;)V   # False Positive
Landroid/provider/Telephony$Sms;->query(Landroid/content/ContentResolver;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;   # False Positive
Landroid/security/KeyStore;->isEmpty()Z   # False Positive
Landroid/security/KeyStore;->reset()Z   # False Positive
Landroid/service/carrier/ICarrierMessagingCallback$Stub;-><init>()V   # False Positive
Landroid/service/carrier/ICarrierMessagingService;->filterSms(Landroid/service/carrier/MessagePdu;Ljava/lang/String;IILandroid/service/carrier/ICarrierMessagingCallback;)V   # False Positive
Landroid/service/dreams/DreamService;->canDoze()Z   # False Positive
Landroid/service/dreams/DreamService;->isDozing()Z   # False Positive
Landroid/service/dreams/DreamService;->stopDozing()V   # False Positive
Landroid/service/notification/NotificationListenerService;->getNotificationInterface()Landroid/app/INotificationManager;   # False Positive
Landroid/service/notification/NotificationListenerService;->mHandler:Landroid/os/Handler;   # False Positive
Landroid/service/notification/NotificationListenerService;->mNoMan:Landroid/app/INotificationManager;   # False Positive
Landroid/service/notification/NotificationListenerService;->TAG:Ljava/lang/String;   # False Positive
Landroid/service/notification/StatusBarNotification;->initialPid:I   # False Positive
Landroid/service/notification/StatusBarNotification;->notification:Landroid/app/Notification;   # False Positive
Landroid/service/notification/StatusBarNotification;->postTime:J   # False Positive
Landroid/service/notification/StatusBarNotification;->tag:Ljava/lang/String;   # False Positive
Landroid/service/notification/StatusBarNotification;->user:Landroid/os/UserHandle;   # False Positive
Landroid/service/wallpaper/WallpaperService$Engine;->mPendingXOffset:F   # False Positive
Landroid/telecom/AudioState;->isMuted:Z   # Deprecated class; use https://developer.android.com/reference/android/telecom/CallAudioState.html#isMuted()
Landroid/telecom/AudioState;->route:I   # Deprecated class; use https://developer.android.com/reference/android/telecom/CallAudioState.html#getRoute()
Landroid/telecom/AudioState;->supportedRouteMask:I   # Deprecated class; use https://developer.android.com/reference/android/telecom/CallAudioState.html#getSupportedRouteMask()
Landroid/telecom/Call$Details;->CAPABILITY_CAN_UPGRADE_TO_VIDEO:I   # This extra is not used in the framework at all; apps needing to know whether a call supports video should use CAPABILITY_SUPPORTS_VT_LOCAL_BIDIRECTIONAL and CAPABILITY_SUPPORTS_VT_REMOTE_BIDIRECTIONAL instead.
Landroid/telecom/ParcelableCall;->CREATOR:Landroid/os/Parcelable$Creator;   # False Positive
Landroid/telecom/ParcelableCall;->getConnectTimeMillis()J   # False Positive
Landroid/telecom/ParcelableCall;->getDisconnectCause()Landroid/telecom/DisconnectCause;   # False Positive
Landroid/telecom/ParcelableCall;->getHandle()Landroid/net/Uri;   # False Positive
Landroid/telecom/ParcelableCall;->getId()Ljava/lang/String;   # False Positive
Landroid/telecom/Phone;->setProximitySensorOff(Z)V   # No public alternative; this method does not do anything and is part of a deprecated class.
Landroid/telecom/Phone;->setProximitySensorOn()V   # No public alternative; this method does not do anything and is part of a deprecated class.
Landroid/telecom/PhoneAccountHandle;-><init>(Landroid/os/Parcel;)V   # False Positive
Landroid/telecom/PhoneAccountHandle;->mComponentName:Landroid/content/ComponentName;   # Use https://developer.android.com/reference/android/telecom/PhoneAccountHandle.html#getComponentName()
Landroid/telecom/PhoneAccountHandle;->mId:Ljava/lang/String;   # False Positive
Landroid/telecom/TelecomManager;->EXTRA_IS_HANDOVER:Ljava/lang/String;   # EXTRA_IS_HANDOVER is no longer used in the framework; it was part of non-supported experimental functionality.  Apps performing handovers should use android.telecom.Call#handoverTo() and the APIs linked from its documentation -- these APIs are fully supported and tested through CTS tests.
Landroid/telecom/TelecomManager;->from(Landroid/content/Context;)Landroid/telecom/TelecomManager;   # Apps should use TelecomManager telecomManager = (TelecomManager) context.getSystemService(Context.TELECOM_SERVICE) instead.
Landroid/telecom/TelecomManager;->getCallCapablePhoneAccounts(Z)Ljava/util/List;   # No public alternative as disabled PhoneAccounts are not intended to be exposed to any external application; this method shoudl never be used.  Apps should use TelecomManager#getCallCapablePhoneAccounts() instead to get a list of the phone accounts which are enabled.  Disabled phone accounts are not available to place calls; no public API consumers should be able to see disabled phone accounts as they cannot possibly be enabled by a consumer of the public API, nor could they be used to place calls.
Landroid/telecom/TelecomManager;->getSimCallManager(I)Landroid/telecom/PhoneAccountHandle;   # No public alternative as there is no valid use-case for querying the SimCallManager across users; apps should use TelecomManager#getSimCallManager() instead.  OEMs modifying AOSP are free to add private APIs to meet their needs, however apps targeting public APIS should NEVER interact across users.
Landroid/telecom/VideoCallImpl;->destroy()V   # No public alternative; no need to call this directly.
Landroid/telephony/CarrierMessagingServiceManager;-><init>()V   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->equalsHandlesNulls(Ljava/lang/Object;Ljava/lang/Object;)Z   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->mBaseStationId:I   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->mBaseStationLatitude:I   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->mBaseStationLongitude:I   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->mNetworkId:I   # False Positive
Landroid/telephony/cdma/CdmaCellLocation;->mSystemId:I   # False Positive
Landroid/telephony/CellIdentityLte;-><init>(IIIII)V   # False Positive
Landroid/telephony/CellInfoCdma;-><init>(Landroid/telephony/CellInfoCdma;)V   # False Positive
Landroid/telephony/CellInfoLte;->setCellIdentity(Landroid/telephony/CellIdentityLte;)V   # False Positive
Landroid/telephony/CellInfoLte;->setCellSignalStrength(Landroid/telephony/CellSignalStrengthLte;)V   # False Positive
Landroid/telephony/CellSignalStrengthGsm;->mTimingAdvance:I   # public alternative: CellSignalStrengthGsm#getTimingAdvance
Landroid/telephony/CellSignalStrengthLte;->mCqi:I   # public alternative: CellSignalStrengthLte#getCqi
Landroid/telephony/CellSignalStrengthLte;->mRsrp:I   # public alternative: CellSignalStrengthLte#getRsrp()
Landroid/telephony/CellSignalStrengthLte;->mRsrq:I   # public alternative: CellSignalStrengthLte#getRsrq
Landroid/telephony/CellSignalStrengthLte;->mRssnr:I   # public alternative: CellSignalStrengthLte#getRssi
Landroid/telephony/CellSignalStrengthLte;->mSignalStrength:I   # alternative: {@link CellSignalStengthLte#getRssi()}
Landroid/telephony/CellSignalStrengthLte;->mTimingAdvance:I   # public alternative: CellSignalStrengthLte#getTimingAdvance
Landroid/telephony/gsm/GsmCellLocation;->setPsc(I)V   # False Positive
Landroid/telephony/NeighboringCellInfo;->mCid:I   # False Positive
Landroid/telephony/NeighboringCellInfo;->mLac:I   # False Positive
Landroid/telephony/NeighboringCellInfo;->mNetworkType:I   # False Positive
Landroid/telephony/NeighboringCellInfo;->mPsc:I   # False Positive
Landroid/telephony/NeighboringCellInfo;->mRssi:I   # False Positive
Landroid/telephony/PhoneStateListener;-><init>(Landroid/os/Looper;)V   # Apps should use the PhoneStateListener constructor which uses an Executor.
Landroid/telephony/PhoneStateListener;-><init>(Ljava/lang/Integer;)V   # alternative: {@link PhoneStateListener()} use default constructor without passing subId. To listen for specific subscription, use {@TelephonyManager#createForSubscriptionId(int subId)} and {@link TelephonyManager#listen(PhoneStateListener psl)};
Landroid/telephony/PhoneStateListener;-><init>(Ljava/lang/Integer;Landroid/os/Looper;)V   # TelephonyManager.createForSubscriptionId(int subId).listen(PhoneStateListener(@NonNull Executor executor))
Landroid/telephony/RadioAccessFamily;->getNetworkTypeFromRaf(I)I   # False Positive
Landroid/telephony/Rlog;->i(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I   # False Positive
Landroid/telephony/ServiceState;->bearerBitmapHasCdma(I)Z   # False Positive
Landroid/telephony/ServiceState;->equalsHandlesNulls(Ljava/lang/Object;Ljava/lang/Object;)Z   # False Positive
Landroid/telephony/ServiceState;->getCssIndicator()I   # False Positive
Landroid/telephony/ServiceState;->getDataNetworkType()I   # TelephonyManager.getServiceState().getNetworkRegistrationState(NetworkRegistrationState.DOMAIN_PS, AccessNetworkConstants.TransportType.WWAN).getAccessNetworkTechnology()
Landroid/telephony/ServiceState;->getDataRoaming()Z   # TelephonyManager.getServiceState().getNetworkRegistrationState(NetworkRegistrationState.DOMAIN_PS, AccessNetworkConstants.TransportType.WWAN).isRomaing()
Landroid/telephony/ServiceState;->getDataRoamingType()I   # SystemAPI ServiceState.getNetworkRegistrationState(NetworkRegistrationState.DOMAIN_PS, AccessNetworkConstants.TransportType.WWAN).getRoamingType()
Landroid/telephony/ServiceState;->getVoiceNetworkType()I   # alternative: {@link NetworkRegistrationInfo#getAccessNetworkTechnology()}
Landroid/telephony/ServiceState;->getVoiceOperatorNumeric()Ljava/lang/String;   # System API ServiceState.getOperatorNumeric()
Landroid/telephony/ServiceState;->getVoiceRegState()I   # Public: ServiceState.getState() or SystemAPI NetworkRegistrationState.getRegState()
Landroid/telephony/ServiceState;->getVoiceRoaming()Z   # SystemAPI ServiceState.getNetworkRegistrationState(NetworkRegistrationState.DOMAIN_CS, AccessNetworkConstants.TransportType.WWAN).getRoamingType()
Landroid/telephony/ServiceState;->getVoiceRoamingType()I   # alternative: {@link NetworkRegistrationInfo#getRoamingType()} use ServiceState.getNetworkRegistrationInfo(NetworkRegistrationInfo.DOMAIN_CS, AccessNetworkConstants.TRANSPORT_TYPE_WWAN) to get NetworkRegistration instance for roaming type.
Landroid/telephony/ServiceState;->mCdmaDefaultRoamingIndicator:I   # False Positive
Landroid/telephony/ServiceState;->mCdmaEriIconIndex:I   # False Positive
Landroid/telephony/ServiceState;->mCdmaEriIconMode:I   # False Positive
Landroid/telephony/ServiceState;->mCdmaRoamingIndicator:I   # False Positive
Landroid/telephony/ServiceState;->mCssIndicator:Z   # False Positive
Landroid/telephony/ServiceState;->mIsManualNetworkSelection:Z   # TelephonyManager.getServiceState().isManualNetworkSelection()
Landroid/telephony/ServiceState;->mNetworkId:I   # TelephonyManager.getServiceState().getCdmaNetworkId()
Landroid/telephony/ServiceState;->mSystemId:I   # TelephonyManager.getServiceState().getCdmaSystemId()
Landroid/telephony/ServiceState;->RIL_RADIO_TECHNOLOGY_IWLAN:I   # don't use the internal RIL version, move to SystemAPI TelephonyManager.NETWORK_TYPE_IWLAN
Landroid/telephony/ServiceState;->setCdmaDefaultRoamingIndicator(I)V   # False Positive
Landroid/telephony/ServiceState;->setCdmaEriIconIndex(I)V   # False Positive
Landroid/telephony/ServiceState;->setCdmaEriIconMode(I)V   # False Positive
Landroid/telephony/ServiceState;->setCdmaRoamingIndicator(I)V   # False Positive
Landroid/telephony/ServiceState;->setCssIndicator(I)V   # False Positive
Landroid/telephony/ServiceState;->setDataRegState(I)V   # False Positive
Landroid/telephony/ServiceState;->setEmergencyOnly(Z)V   # False Positive
Landroid/telephony/SignalStrength;->fillInNotifierBundle(Landroid/os/Bundle;)V   # This is a helper API to set Intent Bundle from SignalStrength. Use {@link Bundle#putParcelable()} instead and full access to internal storage is available via {@link getCellSignalStrengths()}
Landroid/telephony/SignalStrength;->getAsuLevel()I   # @link CellSignalStrengthLte#getAsuLevel
Landroid/telephony/SignalStrength;->getCdmaAsuLevel()I   # @link CellSignalStrengthCdma#getAsuLevel
Landroid/telephony/SignalStrength;->getCdmaLevel()I   # alternative: {@link CellSignalStrengthCdma#getLevel}
Landroid/telephony/SignalStrength;->getDbm()I   # alternative: {@link CellSignalStrength#getDbm()}
Landroid/telephony/SignalStrength;->getEvdoAsuLevel()I   # alternative: {@link CellSignalStrengthCdma#getEvdoAsuLevel}
Landroid/telephony/SignalStrength;->getEvdoLevel()I   # alternative: {@link CellSignalStrengthCdma#getEvdoLevel}
Landroid/telephony/SignalStrength;->getGsmAsuLevel()I   # alternative: {@link CellSignalStrengthGsm#getAsuLevel}
Landroid/telephony/SignalStrength;->getGsmDbm()I   # alternative: {@link CellSignalStrengthGsm#getDbm}
Landroid/telephony/SignalStrength;->getGsmLevel()I   # alternative: {@link CellSignalStrengthGsm#getLevel}
Landroid/telephony/SignalStrength;->getLteAsuLevel()I   # public alternative: CellSignalStrengthLte#getAsuLevel
Landroid/telephony/SignalStrength;->getLteCqi()I   # alternative: {@link CellSignalStrengthLte#getCqi}
Landroid/telephony/SignalStrength;->getLteDbm()I   # alternative: {@link CellSignalStrengthLte#getDbm}
Landroid/telephony/SignalStrength;->getLteLevel()I   # alternative: {@link CellSignalStrengthLte#getLevel}
Landroid/telephony/SignalStrength;->getLteRsrp()I   # public alternative: CellSignalStrengthLte#getRsrp
Landroid/telephony/SignalStrength;->getLteRsrq()I   # alternative: {@link CellSignalStrengthLte#getRsrq}
Landroid/telephony/SignalStrength;->getLteRssnr()I   # CellSignalStrengthLte.getRssi()
Landroid/telephony/SignalStrength;->getLteSignalStrength()I   # alternative: CellSignalStrengthLte#getRssi
Landroid/telephony/SignalStrength;->getTdScdmaAsuLevel()I   # alternative: {@link CellSignalStrengthTdscdma#getAsuLevel}
Landroid/telephony/SignalStrength;->getTdScdmaDbm()I   # alternative: {@link CellSignalStrengthTdscdma#getDbm}
Landroid/telephony/SignalStrength;->getTdScdmaLevel()I   # alternative: {@link CellSignalStrengthTdscdma#getLevel}
Landroid/telephony/SignalStrength;->setFromNotifierBundle(Landroid/os/Bundle;)V   # This method relies on non-stable implementation details, and full access to internal storage is available via {@link getCellSignalStrengths()}
Landroid/telephony/SignalStrength;->SIGNAL_STRENGTH_GOOD:I   # CellSignalStrength.SIGNAL_STRENGTH_GOOD
Landroid/telephony/SignalStrength;->SIGNAL_STRENGTH_GREAT:I   # CellSignalStrength.SIGNAL_STRENGTH_GREAT
Landroid/telephony/SignalStrength;->SIGNAL_STRENGTH_MODERATE:I   # CellSignalStrength.SIGNAL_STRENGTH_MODERATE
Landroid/telephony/SignalStrength;->SIGNAL_STRENGTH_NONE_OR_UNKNOWN:I   # CellSignalStrength.SIGNAL_STRENGTH_NONE_OR_UNKNOWN
Landroid/telephony/SignalStrength;->SIGNAL_STRENGTH_POOR:I   # CellSignalStrength.SIGNAL_STRENGTH_POOR
Landroid/telephony/SmsManager;->mSubId:I   # False Positive
Landroid/telephony/SubscriptionManager;->getPhoneId(I)I   # No public alternative.  The phone id is an internal implementation detail of the telephony stack.  Apps should use subcription ID or slot index based APIs instead.
Landroid/telephony/SubscriptionManager;->isUsableSubIdValue(I)Z   # SubscriptionManager.isUsableSubscriptionId(int subscriptionId)
Landroid/telephony/SubscriptionManager;->isValidSlotIndex(I)Z   # False Positive
Landroid/telephony/SubscriptionManager;->NAME_SOURCE_USER_INPUT:I   # False Positive
Landroid/telephony/SubscriptionManager;->putPhoneIdAndSubIdExtra(Landroid/content/Intent;I)V   # No public alternative; this method simply adds values to an intent.  An app is free to add the sub ID extra itself.  Apps should never rely upon the phone ID for any operations as this is an internal implementation detail of Telephony
Landroid/telephony/TelephonyManager;->from(Landroid/content/Context;)Landroid/telephony/TelephonyManager;   # context.getSystemService(Context.TELEPHONY_SERVICE)
Landroid/telephony/TelephonyManager;->getDataNetworkType(I)I   # TelephonyManager.createForSubscriptionId(int subId).getServiceState().getNetworkRegistrationState(NetworkRegistrationState.DOMAIN_PS, AccessNetworkConstants.TransportType.WWAN).getAccessNetworkTechnology()
Landroid/telephony/TelephonyManager;->getDefault()Landroid/telephony/TelephonyManager;   # context.getSystemService(Context.TELEPHONY_SERVICE)
Landroid/telephony/TelephonyManager;->getITelephony()Lcom/android/internal/telephony/ITelephony;   # No public alternative as apps can access all TelephonyManager APIs directly through TelephonyManager itself; there is no valid use-case where accessing the internal binder is necessary.
Landroid/telephony/TelephonyManager;->getMsisdn(I)Ljava/lang/String;   # Alternative: {@link TelephonyManager#getMsisdn()} To call an API for a specific subscription, use {@link #createForSubscriptionId(int)}
Landroid/telephony/TelephonyManager;->getNetworkOperator(I)Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getNetworkOperator()
Landroid/telephony/TelephonyManager;->getNetworkOperatorName(I)Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getNetworkOperatorName()
Landroid/telephony/TelephonyManager;->getNetworkType(I)I
Landroid/telephony/TelephonyManager;->getOtaSpNumberSchemaForPhone(ILjava/lang/String;)Ljava/lang/String;   # False Positive
Landroid/telephony/TelephonyManager;->getServiceStateForSubscriber(I)Landroid/telephony/ServiceState;   # TelephonyManager.createForSubscriptionId(int subId).getServiceState()
Landroid/telephony/TelephonyManager;->getSimCountryIso(I)Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getSimCountryIso()
Landroid/telephony/TelephonyManager;->getSimOperator(I)Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getSimOperator()
Landroid/telephony/TelephonyManager;->getSimOperatorName(I)Ljava/lang/String;   # {@link TelephonyManager#getSimOperatorName()} To call an API for a specific subscription, use {@link #createForSubscriptionId(int)}.
Landroid/telephony/TelephonyManager;->getSimOperatorNumeric()Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getSimOperator()
Landroid/telephony/TelephonyManager;->getSimOperatorNumeric(I)Ljava/lang/String;   # TelephonyManager.createForSubscriptionId(int subId).getSimOperator()
Landroid/telephony/TelephonyManager;->getSimOperatorNumericForPhone(I)Ljava/lang/String;   # recomment to use subId to query instead of phoneId. see TelephonyManager.createForSubscriptionId(int subId).getSimOperator()
Landroid/telephony/TelephonyManager;->getSubscriberId(I)Ljava/lang/String;   # TelephonyManager createForSubscriptionId(int subId).getSubscriberId()
Landroid/telephony/TelephonyManager;->getVoiceNetworkType(I)I   # TelephonyManage.createForSubscriptionId(int subId).getVoiceNetworkType()
Landroid/telephony/TelephonyManager;->isImsRegistered()Z   # SystemAPI ImsMmTelManager#registerImsRegistrationCallback to listen IMS registration state change
Landroid/telephony/TelephonyManager;->setBasebandVersionForPhone(ILjava/lang/String;)V   # False Positive
Landroid/telephony/TelephonyManager;->setPhoneType(II)V   # False Positive
Landroid/telephony/TelephonyManager;->setSimCountryIsoForPhone(ILjava/lang/String;)V   # False Positive
Landroid/telephony/TelephonyManager;->setSimOperatorNameForPhone(ILjava/lang/String;)V   # False Positive
Landroid/telephony/TelephonyManager;->setSimStateForPhone(ILjava/lang/String;)V   # False Positive
Landroid/telephony/VoLteServiceState;-><init>(I)V   # False Positive
Landroid/text/DynamicLayout;-><init>(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/text/TextPaint;ILandroid/text/Layout$Alignment;Landroid/text/TextDirectionHeuristic;FFZIIILandroid/text/TextUtils$TruncateAt;I)V   # False Positive
Landroid/text/method/HideReturnsTransformationMethod;->sInstance:Landroid/text/method/HideReturnsTransformationMethod;   # False Positive
Landroid/text/method/PasswordTransformationMethod;->DOT:C   # False Positive
Landroid/text/StaticLayout;-><init>(Ljava/lang/CharSequence;IILandroid/text/TextPaint;ILandroid/text/Layout$Alignment;Landroid/text/TextDirectionHeuristic;FFZLandroid/text/TextUtils$TruncateAt;II)V   # Please use StaticLayout.Builder instead
Landroid/text/StaticLayout;->getHeight(Z)I   # False Positive
Landroid/text/style/BulletSpan;->mColor:I   # False Positive
Landroid/text/style/BulletSpan;->mGapWidth:I   # False Positive
Landroid/text/style/BulletSpan;->mWantColor:Z   # False Positive
Landroid/text/TextLine;->mSpanned:Landroid/text/Spanned;   # False Positive
Landroid/text/TextLine;->sCached:[Landroid/text/TextLine;   # No public alternative: There is no direct public alternative. The class is hidden, and the field is hidden. This is a utility class used by StaticLayout. On Q we provided a very low level text layout API. Suggestion to developers: For custom text layout please use lower level APIs such as android.graphics.text.LineBreaker or android.graphics.Paint. For higher level use cases please use android.text.StaticLayout.
Landroid/transition/ChangeBounds;->BOTTOM_RIGHT_ONLY_PROPERTY:Landroid/util/Property;   # Developers should use View.setLeftTopRightBottom() instead.
Landroid/transition/ChangeBounds;->POSITION_PROPERTY:Landroid/util/Property;   # Developers should use View.setLeftTopRightBottom() instead.
Landroid/transition/Scene;->mEnterAction:Ljava/lang/Runnable;   # This was used by old versions of androidx.transitions library. Developers should migrate to newer versions of AndroidX Transition library
Landroid/transition/Scene;->mExitAction:Ljava/lang/Runnable;   # This was used by old versions of androidx.transitions library. Developers should migrate to newer versions of AndroidX Transition library
Landroid/util/ArrayMap;->allocArrays(I)V   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->append(Ljava/lang/Object;Ljava/lang/Object;)V   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->CACHE_SIZE:I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->EMPTY:Landroid/util/ArrayMap;   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->EMPTY_IMMUTABLE_INTS:[I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->freeArrays([I[Ljava/lang/Object;I)V   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->indexOf(Ljava/lang/Object;I)I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->indexOfNull()I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mArray:[Ljava/lang/Object;   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mBaseCache:[Ljava/lang/Object;   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mBaseCacheSize:I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mHashes:[I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mSize:I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mTwiceBaseCache:[Ljava/lang/Object;   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArrayMap;->mTwiceBaseCacheSize:I   # Not needed, nobody should be touching this.  If you want some kind of custom ArrayMap, there is a full source ArrayMap in the support library that can be copied.
Landroid/util/ArraySet;->allocArrays(I)V   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->freeArrays([I[Ljava/lang/Object;I)V   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->indexOf(Ljava/lang/Object;I)I   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->indexOfNull()I   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->mArray:[Ljava/lang/Object;   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->mHashes:[I   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/ArraySet;->mSize:I   # Not needed, nobody should be touching this.  If you want a special ArraySet behavior, you can copy the code out of the platform and make your own class.
Landroid/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V   # False Positive
Landroid/util/LongSparseLongArray;->mKeys:[J   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/LongSparseLongArray;->mSize:I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/LongSparseLongArray;->mValues:[J   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/Slog;->wtfStack(Ljava/lang/String;Ljava/lang/String;)I   # False Positive
Landroid/util/SparseArray;->mKeys:[I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseArray;->mSize:I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseArray;->mValues:[Ljava/lang/Object;   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseBooleanArray;->mKeys:[I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseBooleanArray;->mSize:I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseBooleanArray;->mValues:[Z   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseIntArray;->mKeys:[I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseIntArray;->mSize:I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/SparseIntArray;->mValues:[I   # Not needed, nobody should be touching this.  If you want special behavior, you can copy the code out of the platform and make your own class.
Landroid/util/TimeUtils;->formatDuration(JLjava/io/PrintWriter;)V   # False Positive
Landroid/util/TimeUtils;->formatDuration(JLjava/io/PrintWriter;I)V   # False Positive
Landroid/view/accessibility/AccessibilityEvent;->mAction:I   # False Positive
Landroid/view/accessibility/AccessibilityManager;->mIsEnabled:Z   # No public alternative for setting this field. Developers should use AccessibilityManager.isEnabled() to read this field.
Landroid/view/animation/Animation;->mListener:Landroid/view/animation/Animation$AnimationListener;   # Use setAnimationListener()
Landroid/view/Choreographer;->mLock:Ljava/lang/Object;   # False Positive
Landroid/view/Choreographer;->USE_VSYNC:Z   # No public alternative for accessing this flag. VSYNC is enabled by default.
Landroid/view/ContextThemeWrapper;->mTheme:Landroid/content/res/Resources$Theme;   # Use https://developer.android.com/reference/android/view/ContextThemeWrapper.html#setTheme(android.content.res.Resources.Theme) instead.
Landroid/view/Display;->getDisplayInfo(Landroid/view/DisplayInfo;)Z   # No public alternative. Developers should never access this class directly.
Landroid/view/DisplayInfo;-><init>()V   # No public alternative. Developers should never access this class directly.
Landroid/view/DisplayInfo;->displayCutout:Landroid/view/DisplayCutout;   # Use https://developer.android.com/reference/android/view/Display.html#getCutout() instead.
Landroid/view/GestureDetector;->LONGPRESS_TIMEOUT:I   # Use ViewConfiguration#getLongPressTimeout(). This value is not editable.
Landroid/view/GhostView;->addGhost(Landroid/view/View;Landroid/view/ViewGroup;)Landroid/view/GhostView;   # No public alternative. Developers should never access this class directly.
Landroid/view/GhostView;->removeGhost(Landroid/view/View;)V   # No public alternative. Developers should never access this class directly.
Landroid/view/IGraphicsStats$Stub$Proxy;-><init>(Landroid/os/IBinder;)V   # Unclear what developer use case is enabled by reflecting on this API
Landroid/view/IGraphicsStats$Stub;->asInterface(Landroid/os/IBinder;)Landroid/view/IGraphicsStats;   # Unclear as to why this is being access via reflection, can we reach out to app developers to find out why?
Landroid/view/InputDevice;->mIsExternal:Z   # Use public isExternal method; do not edit
Landroid/view/inputmethod/InputMethodManager;->mH:Landroid/view/inputmethod/InputMethodManager$H;   # This field was useful to developers working around context leak bugs that have now been fixed and backported via AppCompatActivity
Landroid/view/inputmethod/InputMethodManager;->mNextServedView:Landroid/view/View;   # Hacks to  fix context leaks are backported to androidx.activity.ComponentActivity
Landroid/view/inputmethod/InputMethodManager;->mServedInputConnectionWrapper:Landroid/view/inputmethod/InputMethodManager$ControlledInputConnectionWrapper;   # False Positive
Landroid/view/inputmethod/InputMethodManager;->mServedView:Landroid/view/View;   # Hacks to  fix context leaks are backported to androidx.activity.ComponentActivity
Landroid/view/inputmethod/InputMethodManager;->notifyUserAction()V   # Developers can directly implement InputConnection without extending BaseInputConnection (more context crbug.com/551193)
Landroid/view/inputmethod/InputMethodManager;->showSoftInputUnchecked(ILandroid/os/ResultReceiver;)V   # No public alternative. Developers should never access this method directly.
Landroid/view/IWindowManager;->setInTouchMode(Z)V   # False Positive
Landroid/view/IWindowManager;->showStrictModeViolation(Z)V   # False Positive
Landroid/view/KeyEvent;->mSource:I   # False Positive
Landroid/view/KeyEvent;->recycle()V   # False Positive
Landroid/view/LayoutInflater;->mConstructorArgs:[Ljava/lang/Object;   # No public alternative. Developers should never access this field directly.
Landroid/view/LayoutInflater;->mContext:Landroid/content/Context;   # Use getContext() to read, cloneInContext to produce a new inflater with a different context
Landroid/view/LayoutInflater;->mFactorySet:Z   # No public alternative. Developers should never access this field directly.
Landroid/view/LayoutInflater;->sConstructorMap:Ljava/util/HashMap;   # No public alternative. Developers should never access this field directly.
Landroid/view/MotionEvent;->mNativePtr:J   # No public alternative
Landroid/view/PointerIcon;->load(Landroid/content/Context;)Landroid/view/PointerIcon;   # False Positive
Landroid/view/PointerIcon;->mType:I   # False Positive
Landroid/view/ScaleGestureDetector;->mMinSpan:I   # Use https://developer.android.com/reference/android/view/ViewConfiguration#getScaledMinimumScalingSpan() instead.
Landroid/view/ScaleGestureDetector;->mSpanSlop:I   # Value tuned by OEM configuration; should not be edited
Landroid/view/SurfaceView;->mDrawingStopped:Z   # False Positive
Landroid/view/SurfaceView;->mIsCreating:Z   # False Positive
Landroid/view/SurfaceView;->mLastLockTime:J   # False Positive
Landroid/view/SurfaceView;->mRequestedHeight:I   # False Positive
Landroid/view/SurfaceView;->mRequestedWidth:I   # False Positive
Landroid/view/SurfaceView;->mSurfaceFrame:Landroid/graphics/Rect;   # False Positive
Landroid/view/View;->dispatchAttachedToWindow(Landroid/view/View$AttachInfo;I)V   # Should not be used directly as it violates internal code guarantees. Instead Views need to be actually attached to the window.
Landroid/view/View;->dispatchDetachedFromWindow()V   # Should not be used directly as it violates internal code guarantees. Instead Views need to be actually attached to the window.
Landroid/view/View;->getWindowSession()Landroid/view/IWindowSession;   # False Positive
Landroid/view/View;->internalSetPadding(IIII)V   # Use get/setPadding public APIs
Landroid/view/View;->mAnimator:Landroid/view/ViewPropertyAnimator;   # False Positive
Landroid/view/View;->mAttachInfo:Landroid/view/View$AttachInfo;   # No public alternative
Landroid/view/View;->mBottom:I   # Getter and setter exist since API 11
Landroid/view/View;->mHasPerformedLongPress:Z   # False Positive
Landroid/view/View;->mLayoutParams:Landroid/view/ViewGroup$LayoutParams;   # Users should rely on the getter / setter. The setter additionally guarantees internal state correctness.
Landroid/view/View;->mLeft:I   # Getter and setter exist since API 11
Landroid/view/View;->mMinHeight:I   # Getter and setter exist since API 16
Landroid/view/View;->mMinWidth:I   # Getter and setter exist since API 16
Landroid/view/View;->mParent:Landroid/view/ViewParent;   # Getter and setter exist since API 11
Landroid/view/View;->mPrivateFlags2:I   # Use various setters/getters, should not be exposed directly
Landroid/view/View;->mPrivateFlags3:I   # Use various setters/getters, should not be exposed
Landroid/view/View;->mPrivateFlags:I   # Various setters, should not be exposed directly
Landroid/view/View;->mRight:I   # Getter and setter exist since API 11
Landroid/view/View;->mScrollX:I   # Please use getScrollX(), getScrollY(), setScrollX(int), setScrollY(int) instead
Landroid/view/View;->mScrollY:I   # Please use getScrollX(), getScrollY(), setScrollX(int), setScrollY(int) instead
Landroid/view/View;->mTop:I   # Getter and setter exist since API 11
Landroid/view/View;->mViewFlags:I   # Directly use the now public View.setTransitionVisibility() instead of reflecting on the field
Landroid/view/View;->setAlphaNoInvalidation(F)Z   # N/A
Landroid/view/View;->setFlags(II)V   # False Positive
Landroid/view/View;->setFrame(IIII)Z   # Use setLeftTopRightBottom() instead. Overriding of setFrame is not a recommended approach for custom ViewGroups. Developers can always add their logic into onSizeChanged() callback.
Landroid/view/View;->startActivityForResult(Landroid/content/Intent;I)V   # False Positive
Landroid/view/ViewConfiguration;->sHasPermanentMenuKey:Z   # Use hasPermanentMenuKey()
Landroid/view/ViewGroup;->FLAG_DISALLOW_INTERCEPT:I   # Use requestDisallowInterceptTouchEvent()
Landroid/view/ViewGroup;->FLAG_SUPPORT_STATIC_TRANSFORMATIONS:I   # No public alternative for getting this flag. Developers should use ViewGroup.setStaticTransformationsEnabled(...) to set this flag.
Landroid/view/ViewGroup;->FLAG_USE_CHILD_DRAWING_ORDER:I   # Use is/setChildrenDrawingOrderEnabled()
Landroid/view/ViewGroup;->mChildren:[Landroid/view/View;   # getChildAt() exists since API 1, addView/removeView and detach/attachView can be used to change the order of the children
Landroid/view/ViewGroup;->mChildrenCount:I   # getChildCount() exists since API 1, there should be no setter, use the addView*() methods instead
Landroid/view/ViewGroup;->mFocused:Landroid/view/View;   # False Positive
Landroid/view/ViewGroup;->mGroupFlags:I   # Use various setters, should not be exposed directly
Landroid/view/ViewGroup;->mOnHierarchyChangeListener:Landroid/view/ViewGroup$OnHierarchyChangeListener;   # No public alternative for getting this field. Developers should use ViewGroup.setOnHierarchyChangeListener(...) to set this field.
Landroid/view/Window;->mWindowManager:Landroid/view/WindowManager;   # False Positive
Landroid/view/Window;->shouldCloseOnTouch(Landroid/content/Context;Landroid/view/MotionEvent;)Z   # False Positive
Landroid/view/WindowManagerGlobal;->peekWindowSession()Landroid/view/IWindowSession;   # False Positive
Landroid/view/WindowManagerGlobal;->trimMemory(I)V   # No public alternative. Developers should never access this method directly.
Landroid/webkit/ConsoleMessage;->mLevel:Landroid/webkit/ConsoleMessage$MessageLevel;   # False Positive
Landroid/webkit/ConsoleMessage;->mLineNumber:I   # False Positive
Landroid/webkit/ConsoleMessage;->mMessage:Ljava/lang/String;   # False Positive
Landroid/webkit/ConsoleMessage;->mSourceId:Ljava/lang/String;   # False Positive
Landroid/widget/AbsListView$FlingRunnable;->endFling()V   # AbsListView#smoothScrollBy(0,0) can be used instead to stop a fling/scroll early
Landroid/widget/AbsListView$FlingRunnable;->start(I)V   # Developers can use AbsListView#fling(int) instead
Landroid/widget/AbsListView$LayoutParams;->viewType:I   # False Positive
Landroid/widget/AbsListView;->mActivePointerId:I   # False Positive
Landroid/widget/AbsListView;->mEdgeGlowBottom:Landroid/widget/EdgeEffect;   # Use https://developer.android.com/reference/android/widget/AbsListView.html#setBottomEdgeEffectColor(int) instead.
Landroid/widget/AbsListView;->mEdgeGlowTop:Landroid/widget/EdgeEffect;   # Implementation detail. Use RecyclerView with the setEdgeEffectFactory method to modify this functionality.
Landroid/widget/AbsListView;->mFastScroll:Landroid/widget/FastScroller;   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AbsListView;->mFlingRunnable:Landroid/widget/AbsListView$FlingRunnable;   # AbsListView#smoothScrollBy(0,0) can be used instead to stop a fling/scroll early
Landroid/widget/AbsListView;->mMaximumVelocity:I   # Implementation detail tuned by devices. Do not modify. Use ViewConfiguration#getScaledMaximumFlingVelocity to read.
Landroid/widget/AbsListView;->mOnScrollListener:Landroid/widget/AbsListView$OnScrollListener;   # Use public accessors
Landroid/widget/AbsListView;->mOverflingDistance:I   # Implementation detail. Use RecyclerView instead which does not have this behavior.
Landroid/widget/AbsListView;->mRecycler:Landroid/widget/AbsListView$RecycleBin;   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AbsListView;->mSelector:Landroid/graphics/drawable/Drawable;   # False Positive
Landroid/widget/AbsListView;->mSelectorPosition:I   # Implementation detail. Use RecyclerView for additional features.
Landroid/widget/AbsListView;->mSelectorRect:Landroid/graphics/Rect;   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AbsListView;->mTouchMode:I   # Use View.isInTouchMode()
Landroid/widget/AbsListView;->reportScrollStateChange(I)V   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AbsListView;->trackMotionScroll(II)Z   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AdapterView;->mDataChanged:Z   # Developers should use RecyclerView for displaying lists.
Landroid/widget/AutoCompleteTextView;->doAfterTextChanged()V   # Use https://developer.android.com/reference/android/widget/AutoCompleteTextView.html#refreshAutoCompleteResults() instead.
Landroid/widget/AutoCompleteTextView;->doBeforeTextChanged()V   # Use https://developer.android.com/reference/android/widget/AutoCompleteTextView.html#refreshAutoCompleteResults() instead.
Landroid/widget/AutoCompleteTextView;->ensureImeVisible(Z)V   # Use https://developer.android.com/reference/android/widget/AutoCompleteTextView.html#setInputMethodMode(int) instead.
Landroid/widget/AutoCompleteTextView;->isInputMethodNotNeeded()Z   # Use https://developer.android.com/reference/android/widget/AutoCompleteTextView.html#getInputMethodMode() instead.
Landroid/widget/AutoCompleteTextView;->setDropDownAnimationStyle(I)V   # False Positive
Landroid/widget/EdgeEffect;->mPaint:Landroid/graphics/Paint;   # No public alternative. Developers should never access this field directly.
Landroid/widget/Editor;->mSelectHandleCenter:Landroid/graphics/drawable/Drawable;   # Use the new TextView#get/setTextSelectHandleLeft()
Landroid/widget/Editor;->mSelectHandleLeft:Landroid/graphics/drawable/Drawable;   # Use the new TextView#get/setTextSelectHandle()
Landroid/widget/Editor;->mSelectHandleRight:Landroid/graphics/drawable/Drawable;   # Use the new TextView#get/setTextSelectHandleRight()
Landroid/widget/Editor;->mShowCursor:J   # This seems to be used in combination with mCursorDrawableRes to set a custom cursor and 'blink' it - developers should now use TextView#setTextCursorDrawable to set a custom cursor - not sure why they would need to handle the blinking themselves anymore.
Landroid/widget/Gallery;->getCenterOfGallery()I   # False Positive
Landroid/widget/Gallery;->getCenterOfView(Landroid/view/View;)I   # False Positive
Landroid/widget/Gallery;->mGestureDetector:Landroid/view/GestureDetector;   # False Positive
Landroid/widget/Gallery;->mSelectedChild:Landroid/view/View;   # False Positive
Landroid/widget/GridView;->fillDown(II)Landroid/view/View;   # No public alternative
Landroid/widget/GridView;->fillUp(II)Landroid/view/View;   # No public alternative
Landroid/widget/GridView;->mColumnWidth:I   # Use get/setColumnWidth()
Landroid/widget/GridView;->mNumColumns:I   # Use get/setNumColumns()
Landroid/widget/GridView;->mRequestedNumColumns:I   # Use public accessors
Landroid/widget/HorizontalScrollView;->mEdgeGlowLeft:Landroid/widget/EdgeEffect;   # Implementation detail, do not modify. Copy class using public API if further changes are desired. See NestedScrollView in Jetpack
Landroid/widget/HorizontalScrollView;->mEdgeGlowRight:Landroid/widget/EdgeEffect;   # Use https://developer.android.com/reference/android/widget/HorizontalScrollView.html#setRightEdgeEffectColor(int) instead.
Landroid/widget/ImageView;->mDrawMatrix:Landroid/graphics/Matrix;   # Use https://developer.android.com/reference/android/widget/ImageView.html#setImageMatrix(android.graphics.Matrix) instead.
Landroid/widget/ImageView;->mMaxHeight:I   # These two have getters (since api 16) and setters (since api 1), so no reason to be reflecting anymore
Landroid/widget/ImageView;->mMaxWidth:I   # These two have getters (since api 16) and setters (since api 1), so no reason to be reflecting anymore
Landroid/widget/LinearLayout;->mGravity:I   # Getter and setter exist since API 1
Landroid/widget/ListView;->correctTooHigh(I)V   # False Positive
Landroid/widget/ListView;->correctTooLow(I)V   # False Positive
Landroid/widget/ListView;->fillDown(II)Landroid/view/View;   # No public alternative
Landroid/widget/ListView;->fillSpecific(II)Landroid/view/View;   # No public alternative
Landroid/widget/ListView;->fillUp(II)Landroid/view/View;   # No public alternative
Landroid/widget/ListView;->mDividerHeight:I   # False Positive
Landroid/widget/ListView;->measureHeightOfChildren(IIIII)I   # False Positive
Landroid/widget/MediaController;->mCurrentTime:Landroid/widget/TextView;   # False Positive
Landroid/widget/MediaController;->mEndTime:Landroid/widget/TextView;   # False Positive
Landroid/widget/MediaController;->mNextButton:Landroid/widget/ImageButton;   # False Positive
Landroid/widget/MediaController;->mPrevButton:Landroid/widget/ImageButton;   # False Positive
Landroid/widget/NumberPicker;->mSelectionDivider:Landroid/graphics/drawable/Drawable;   # Use the new get/setSelectionDividerHeight
Landroid/widget/NumberPicker;->mSelectionDividerHeight:I   # Use the new get/setSelectionDividerHeight
Landroid/widget/NumberPicker;->mSelectorWheelPaint:Landroid/graphics/Paint;   # No public alternative. Developers should never access this field directly.
Landroid/widget/PopupWindow;->invokePopup(Landroid/view/WindowManager$LayoutParams;)V   # No public alternative. Developers should never access this method directly.
Landroid/widget/PopupWindow;->mAboveAnchorBackgroundDrawable:Landroid/graphics/drawable/Drawable;   # False Positive
Landroid/widget/PopupWindow;->mBelowAnchorBackgroundDrawable:Landroid/graphics/drawable/Drawable;   # False Positive
Landroid/widget/PopupWindow;->mOnScrollChangedListener:Landroid/view/ViewTreeObserver$OnScrollChangedListener;   # No public alternative. Developers should never access this field directly.
Landroid/widget/PopupWindow;->mOverlapAnchor:Z   # Use the getter and setter available since API 23
Landroid/widget/ProgressBar;->mCurrentDrawable:Landroid/graphics/drawable/Drawable;   # ProgressBar#getCurrentDrawable made public in Android 10
Landroid/widget/ProgressBar;->mDuration:I   # Developers should use an indeterminate drawable that implements Animatable.
Landroid/widget/ProgressBar;->mIndeterminate:Z   # Use isIndeterminate()
Landroid/widget/ProgressBar;->mMaxHeight:I   # Use the new get/setMaxHeight
Landroid/widget/ProgressBar;->mMinHeight:I   # Use the new get/setMinHeight
Landroid/widget/ProgressBar;->mMinWidth:I   # Use the new get/setMinWidth
Landroid/widget/RelativeLayout;->mGravity:I   # Use get/setGravity()
Landroid/widget/ScrollBarDrawable;->mVerticalThumb:Landroid/graphics/drawable/Drawable;   # Exposed View#setHorizontalThumbDrawable/View#setVerticalThumbDrawable in Q
Landroid/widget/ScrollBarDrawable;->setHorizontalThumbDrawable(Landroid/graphics/drawable/Drawable;)V   # Exposed View#setHorizontalThumbDrawable/View#setVerticalThumbDrawable in Q
Landroid/widget/ScrollBarDrawable;->setVerticalThumbDrawable(Landroid/graphics/drawable/Drawable;)V   # Use https://developer.android.com/reference/android/view/View#setVerticalScrollbarThumbDrawable(android.graphics.drawable.Drawable) instead.
Landroid/widget/ScrollView;->mChildToScrollTo:Landroid/view/View;   # Use the new scrollToDescendant(android.view.View)
Landroid/widget/ScrollView;->mEdgeGlowBottom:Landroid/widget/EdgeEffect;   # Use https://developer.android.com/reference/android/widget/AbsListView.html#setBottomEdgeEffectColor(int) instead.
Landroid/widget/ScrollView;->mEdgeGlowTop:Landroid/widget/EdgeEffect;   # Use https://developer.android.com/reference/android/widget/AbsListView.html#setTopEdgeEffectColor(int) instead.
Landroid/widget/ScrollView;->mMinimumVelocity:I   # Implementation detail. Fork ScrollView using public API if additional changes such as this are desired.
Landroid/widget/ScrollView;->mOverflingDistance:I   # Use https://developer.android.com/reference/android/view/ViewConfiguration.html#getScaledOverflingDistance() instead.
Landroid/widget/ScrollView;->mOverscrollDistance:I   # Implementation detail, do not modify. Copy class using public API if further changes are desired. See NestedScrollView in Jetpack
Landroid/widget/SearchView;->onCloseClicked()V   # False Positive
Landroid/widget/SearchView;->setQuery(Ljava/lang/CharSequence;)V   # False Positive
Landroid/widget/SimpleAdapter;->mData:Ljava/util/List;   # False Positive
Landroid/widget/SimpleCursorAdapter;->mFrom:[I   # False Positive
Landroid/widget/TextView;->getHorizontallyScrolling()Z   # Use the new isHorizontallyScrolling()
Landroid/widget/TextView;->mCurHintTextColor:I   # False Positive
Landroid/widget/TextView;->mCursorDrawableRes:I   # Use the new get/setTextCursorDrawable
Landroid/widget/TextView;->mCurTextColor:I   # setTextColor/getCurrentTextColor should be used instead
Landroid/widget/TextView;->mHorizontallyScrolling:Z   # Use the new isHorizontallyScrolling()
Landroid/widget/TextView;->mTextSelectHandleLeftRes:I   # Use the new get/setTextSelectHandleLeft()
Landroid/widget/TextView;->mTextSelectHandleRes:I   # Use the new get/setTextSelectHandle()
Landroid/widget/TextView;->mTextSelectHandleRightRes:I   # Use the new get/setTextSelectHandleRight()
Landroid/widget/TextView;->startMarquee()V   # False Positive
Landroid/widget/TextView;->startStopMarquee(Z)V   # False Positive
Landroid/widget/Toast$TN;->mGravity:I   # Use Toast.set/getGravity()
Landroid/widget/Toast$TN;->mNextView:Landroid/view/View;   # No public alternative. Developers should never access this field directly.
Landroid/widget/Toast$TN;->mParams:Landroid/view/WindowManager$LayoutParams;   # No public alternative. Developers should never access this field directly.
Landroid/widget/Toast$TN;->mView:Landroid/view/View;   # Use Toast.getView()
Landroid/widget/Toast$TN;->mY:I   # Use Toast.getYOffset()
Landroid/widget/Toast$TN;->show(Landroid/os/IBinder;)V   # False Positive
Landroid/widget/Toast;->getService()Landroid/app/INotificationManager;   # Use public NotificationManager
Landroid/widget/Toast;->mTN:Landroid/widget/Toast$TN;   # Internal structure used to communicate with the WindowManager, apps shouldn't need to access this
Landroid/widget/Toast;->sService:Landroid/app/INotificationManager;   # Use public NotificationManager
Landroid/widget/Toolbar;->mNavButtonView:Landroid/widget/ImageButton;   # False Positive
Landroid/widget/VideoView;->mErrorListener:Landroid/media/MediaPlayer$OnErrorListener;   # False Positive
Landroid/widget/VideoView;->mSurfaceHolder:Landroid/view/SurfaceHolder;   # False Positive
Landroid/widget/VideoView;->STATE_IDLE:I   # False Positive
Lcom/android/internal/net/VpnProfile;->server:Ljava/lang/String;   # False Positive
Lcom/android/internal/os/AtomicFile;->getBaseFile()Ljava/io/File;   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestActivityAlias:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestGrantUriPermission:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestInstrumentation:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestOriginalPackage:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestPathPermission:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestPermission:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestPermissionGroup:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestPermissionTree:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestProtectedBroadcast:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestSupportsScreens:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestUsesConfiguration:[I   # False Positive
Lcom/android/internal/R$styleable;->AndroidManifestUsesFeature:[I   # False Positive
Lcom/android/internal/R$styleable;->CycleInterpolator:[I   # False Positive
Lcom/android/internal/R$styleable;->LinearLayout:[I   # False Positive
Lcom/android/internal/R$styleable;->MenuView:[I   # False Positive
Lcom/android/internal/R$styleable;->Searchable:[I   # False Positive
Lcom/android/internal/R$styleable;->SearchableActionKey:[I   # False Positive
Lcom/android/internal/telephony/GsmAlphabet;->gsm8BitUnpackedToString([BIILjava/lang/String;)Ljava/lang/String;   # False Positive
Lcom/android/internal/telephony/IPhoneSubInfo$Stub;-><init>()V   # False Positive
Lcom/android/internal/telephony/ITelephonyRegistry;->notifyCallForwardingChanged(Z)V   # False Positive
Lcom/android/internal/telephony/ITelephonyRegistry;->notifyCellLocation(Landroid/os/Bundle;)V   # False Positive
Lcom/android/internal/telephony/ITelephonyRegistry;->notifyDataActivity(I)V   # False Positive
Lcom/android/internal/telephony/OperatorInfo;-><init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V   # False Positive
Lcom/android/internal/telephony/SmsMessageBase;->getProtocolIdentifier()I   # False Positive
Lcom/android/internal/telephony/SmsMessageBase;->getServiceCenterAddress()Ljava/lang/String;   # False Positive
Lcom/android/internal/telephony/SmsMessageBase;->getStatus()I   # False Positive
Lcom/android/internal/telephony/SmsMessageBase;->isReplace()Z   # False Positive
Lcom/android/internal/telephony/SmsMessageBase;->isReplyPathPresent()Z   # False Positive
Lcom/android/internal/util/AsyncChannel;->cmdToString(I)Ljava/lang/String;   # False Positive
Lcom/android/internal/util/AsyncChannel;->replyToMessage(Landroid/os/Message;I)V   # False Positive
Lcom/android/internal/util/JournaledFile;->chooseForRead()Ljava/io/File;   # False Positive
Lcom/android/internal/util/JournaledFile;->chooseForWrite()Ljava/io/File;   # False Positive
Lcom/android/internal/util/JournaledFile;->commit()V   # False Positive
Lcom/android/internal/util/JournaledFile;->rollback()V   # False Positive
Lcom/android/internal/view/BaseIWindow;-><init>()V   # False Positive
Lcom/android/internal/view/IInputConnectionWrapper;->mInputConnection:Landroid/view/inputmethod/InputConnection;   # False Positive
Ljava/lang/Boolean;->value:Z   # java.lang.Boolean.booleanValue()
Ljava/lang/Byte;->value:B   # java.lang.Byte.byteValue()
Ljava/lang/Character;->value:C   # java.lang.Character.charValue()
Ljava/lang/Double;->value:D   # java.lang.Double.doubleValue()
Ljava/lang/Float;->value:F   # java.lang.Float.floatValue()
Ljava/lang/Integer;->value:I   # java.lang.Integer.intValue()
Ljava/lang/Long;->value:J   # java.lang.Long.longValue()
Ljava/lang/Short;->value:S   # java.lang.Short.shortValue()
Ljava/net/InetAddress;->isNumeric(Ljava/lang/String;)Z   # android.net.InetAddresses.isNumericAddress(String) - there is a behavioural difference between the original method and its replacement.
Ljava/net/InetAddress;->parseNumericAddress(Ljava/lang/String;)Ljava/net/InetAddress;   # android.net.InetAddresses.parseNumericAddress(String) - there is a behavioural difference between the original method and its replacement.
Ljavax/net/ssl/SSLServerSocketFactory;->defaultServerSocketFactory:Ljavax/net/ssl/SSLServerSocketFactory;   # Use getDefault() method instead
Ljavax/net/ssl/SSLSocketFactory;->defaultSocketFactory:Ljavax/net/ssl/SSLSocketFactory;   # Use getDefault() method instead
Lorg/apache/http/conn/ssl/SSLSocketFactory;-><init>()V   # False Positive
Lorg/apache/http/conn/ssl/SSLSocketFactory;->hostnameVerifier:Lorg/apache/http/conn/ssl/X509HostnameVerifier;   # False Positive
```

### non-SDK interfaces that were added to the SDK in Android 10

The following code box lists all of the non-SDK interfaces that were unsupported (greylisted) in Android 9 (API level 28) that were added to the Android SDK in Android 10 (API level 29). Each interface takes up one line.  

```
Landroid/app/admin/DevicePolicyManager;->setDefaultSmsApplication(Landroid/content/ComponentName;Ljava/lang/String;)V
Landroid/app/AppOpsManager;->MODE_FOREGROUND:I
Landroid/app/AppOpsManager;->startWatchingMode(Ljava/lang/String;Ljava/lang/String;ILandroid/app/AppOpsManager$OnOpChangedListener;)V
Landroid/app/AppOpsManager;->unsafeCheckOpRaw(Ljava/lang/String;ILjava/lang/String;)I
Landroid/app/AppOpsManager;->WATCH_FOREGROUND_CHANGES:I
Landroid/content/Context;->getOpPackageName()Ljava/lang/String;
Landroid/content/ContextWrapper;->getOpPackageName()Ljava/lang/String;
Landroid/content/res/Resources;->getFloat(I)F
Landroid/graphics/drawable/AnimatedVectorDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/BitmapDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/DrawableContainer;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/Drawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/Drawable;->isProjected()Z
Landroid/graphics/drawable/DrawableWrapper;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/GradientDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/InsetDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/NinePatchDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/drawable/StateListDrawable;->getStateCount()I
Landroid/graphics/drawable/StateListDrawable;->getStateDrawable(I)Landroid/graphics/drawable/Drawable;
Landroid/graphics/drawable/StateListDrawable;->getStateSet(I)[I
Landroid/graphics/drawable/VectorDrawable;->getOpticalInsets()Landroid/graphics/Insets;
Landroid/graphics/ImageFormat;->Y8:I
Landroid/graphics/Insets;->bottom:I
Landroid/graphics/Insets;->left:I
Landroid/graphics/Insets;->NONE:Landroid/graphics/Insets;
Landroid/graphics/Insets;->of(IIII)Landroid/graphics/Insets;
Landroid/graphics/Insets;->of(Landroid/graphics/Rect;)Landroid/graphics/Insets;
Landroid/graphics/Insets;->right:I
Landroid/graphics/Insets;->top:I
Landroid/graphics/Paint;->getTextRunAdvances([CIIIIZ[FI)F
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_GOOD:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_IMAGER_DIRTY:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_INSUFFICIENT:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_PARTIAL:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_TOO_FAST:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ACQUIRED_TOO_SLOW:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_CANCELED:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_HW_NOT_PRESENT:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_HW_UNAVAILABLE:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_LOCKOUT:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_LOCKOUT_PERMANENT:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_NO_BIOMETRICS:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_NO_SPACE:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_TIMEOUT:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_UNABLE_TO_PROCESS:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_USER_CANCELED:I
Landroid/hardware/biometrics/BiometricConstants;->BIOMETRIC_ERROR_VENDOR:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_GOOD:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_IMAGER_DIRTY:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_INSUFFICIENT:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_PARTIAL:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_TOO_FAST:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ACQUIRED_TOO_SLOW:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_CANCELED:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_HW_NOT_PRESENT:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_HW_UNAVAILABLE:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_LOCKOUT:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_LOCKOUT_PERMANENT:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_NO_FINGERPRINTS:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_NO_SPACE:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_TIMEOUT:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_UNABLE_TO_PROCESS:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_USER_CANCELED:I
Landroid/hardware/biometrics/BiometricFingerprintConstants;->FINGERPRINT_ERROR_VENDOR:I
Landroid/hardware/camera2/CameraCharacteristics$Key;-><init>(Ljava/lang/String;Ljava/lang/Class;)V
Landroid/hardware/camera2/CaptureRequest$Key;-><init>(Ljava/lang/String;Ljava/lang/Class;)V
Landroid/hardware/camera2/CaptureResult$Key;-><init>(Ljava/lang/String;Ljava/lang/Class;)V
Landroid/icu/text/Transliterator;->createFromRules(Ljava/lang/String;Ljava/lang/String;I)Landroid/icu/text/Transliterator;
Landroid/icu/text/Transliterator;->getInstance(Ljava/lang/String;I)Landroid/icu/text/Transliterator;
Landroid/icu/text/Transliterator;->getInstance(Ljava/lang/String;)Landroid/icu/text/Transliterator;
Landroid/icu/text/Transliterator;->transliterate(Landroid/icu/text/Replaceable;Landroid/icu/text/Transliterator$Position;Ljava/lang/String;)V
Landroid/icu/text/Transliterator;->transliterate(Ljava/lang/String;)Ljava/lang/String;
Landroid/icu/text/UForwardCharacterIterator;->DONE:I
Landroid/media/ThumbnailUtils;->createImageThumbnail(Ljava/lang/String;I)Landroid/graphics/Bitmap;
Landroid/media/tv/TvContract$PreviewProgramColumns;->ASPECT_RATIO_1_1:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->ASPECT_RATIO_16_9:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->ASPECT_RATIO_2_3:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->ASPECT_RATIO_3_2:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->ASPECT_RATIO_4_3:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->AVAILABILITY_AVAILABLE:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->AVAILABILITY_FREE_WITH_SUBSCRIPTION:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->AVAILABILITY_PAID_CONTENT:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_AUTHOR:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_AVAILABILITY:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_BROWSABLE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_CONTENT_ID:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_DURATION_MILLIS:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_INTENT_URI:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_INTERACTION_COUNT:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_INTERACTION_TYPE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_INTERNAL_PROVIDER_ID:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_ITEM_COUNT:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_LAST_PLAYBACK_POSITION_MILLIS:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_LIVE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_LOGO_URI:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_OFFER_PRICE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_POSTER_ART_ASPECT_RATIO:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_PREVIEW_VIDEO_URI:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_RELEASE_DATE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_STARTING_PRICE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_THUMBNAIL_ASPECT_RATIO:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_TRANSIENT:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->COLUMN_TYPE:Ljava/lang/String;
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_FANS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_FOLLOWERS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_LIKES:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_LISTENS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_THUMBS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_VIEWERS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->INTERACTION_TYPE_VIEWS:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_ALBUM:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_ARTIST:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_CHANNEL:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_CLIP:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_EVENT:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_MOVIE:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_PLAYLIST:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_STATION:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_TRACK:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_TV_EPISODE:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_TV_SEASON:I
Landroid/media/tv/TvContract$PreviewProgramColumns;->TYPE_TV_SERIES:I
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_AUDIO_LANGUAGE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_CANONICAL_GENRE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_CONTENT_RATING:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_EPISODE_DISPLAY_NUMBER:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_EPISODE_TITLE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_INTERNAL_PROVIDER_DATA:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_INTERNAL_PROVIDER_FLAG1:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_INTERNAL_PROVIDER_FLAG2:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_INTERNAL_PROVIDER_FLAG3:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_INTERNAL_PROVIDER_FLAG4:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_LONG_DESCRIPTION:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_POSTER_ART_URI:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_REVIEW_RATING:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_REVIEW_RATING_STYLE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_SEARCHABLE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_SEASON_DISPLAY_NUMBER:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_SEASON_TITLE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_SHORT_DESCRIPTION:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_THUMBNAIL_URI:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_TITLE:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_VERSION_NUMBER:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_VIDEO_HEIGHT:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->COLUMN_VIDEO_WIDTH:Ljava/lang/String;
Landroid/media/tv/TvContract$ProgramColumns;->REVIEW_RATING_STYLE_PERCENTAGE:I
Landroid/media/tv/TvContract$ProgramColumns;->REVIEW_RATING_STYLE_STARS:I
Landroid/media/tv/TvContract$ProgramColumns;->REVIEW_RATING_STYLE_THUMBS_UP_DOWN:I
Landroid/net/LinkProperties;->addRoute(Landroid/net/RouteInfo;)Z
Landroid/net/LinkProperties;->clear()V
Landroid/net/LinkProperties;->getMtu()I
Landroid/net/LinkProperties;->setDnsServers(Ljava/util/Collection;)V
Landroid/net/LinkProperties;->setDomains(Ljava/lang/String;)V
Landroid/net/LinkProperties;->setHttpProxy(Landroid/net/ProxyInfo;)V
Landroid/net/LinkProperties;->setInterfaceName(Ljava/lang/String;)V
Landroid/net/LinkProperties;->setLinkAddresses(Ljava/util/Collection;)V
Landroid/net/LinkProperties;->setMtu(I)V
Landroid/net/NetworkCapabilities;->getSignalStrength()I
Landroid/net/RouteInfo;->hasGateway()Z
Landroid/os/Handler;->hasCallbacks(Ljava/lang/Runnable;)Z
Landroid/os/Parcel;->readParcelableList(Ljava/util/List;Ljava/lang/ClassLoader;)Ljava/util/List;
Landroid/os/Parcel;->writeParcelableList(Ljava/util/List;I)V
Landroid/os/Process;->BLUETOOTH_UID:I
Landroid/os/Process;->ROOT_UID:I
Landroid/os/Process;->SHELL_UID:I
Landroid/provider/ContactsContract$ContactCounts;->EXTRA_ADDRESS_BOOK_INDEX_COUNTS:Ljava/lang/String;
Landroid/provider/ContactsContract$ContactCounts;->EXTRA_ADDRESS_BOOK_INDEX:Ljava/lang/String;
Landroid/provider/ContactsContract$ContactCounts;->EXTRA_ADDRESS_BOOK_INDEX_TITLES:Ljava/lang/String;
Landroid/service/notification/StatusBarNotification;->getOpPkg()Ljava/lang/String;
Landroid/service/notification/StatusBarNotification;->getUid()I
Landroid/system/Os;->bind(Ljava/io/FileDescriptor;Ljava/net/SocketAddress;)V
Landroid/system/Os;->connect(Ljava/io/FileDescriptor;Ljava/net/SocketAddress;)V
Landroid/system/OsConstants;->AF_NETLINK:I
Landroid/system/OsConstants;->AF_PACKET:I
Landroid/system/OsConstants;->ARPHRD_ETHER:I
Landroid/system/OsConstants;->ETH_P_ALL:I
Landroid/system/OsConstants;->ETH_P_ARP:I
Landroid/system/OsConstants;->ETH_P_IP:I
Landroid/system/OsConstants;->ETH_P_IPV6:I
Landroid/system/OsConstants;->ICMP6_ECHO_REPLY:I
Landroid/system/OsConstants;->ICMP6_ECHO_REQUEST:I
Landroid/system/OsConstants;->ICMP_ECHO:I
Landroid/system/OsConstants;->ICMP_ECHOREPLY:I
Landroid/system/OsConstants;->NETLINK_ROUTE:I
Landroid/system/OsConstants;->RTMGRP_NEIGH:I
Landroid/system/Os;->sendto(Ljava/io/FileDescriptor;[BIIILjava/net/SocketAddress;)I
Landroid/system/Os;->setsockoptTimeval(Ljava/io/FileDescriptor;IILandroid/system/StructTimeval;)V
Landroid/system/StructTimeval;->fromMillis(J)Landroid/system/StructTimeval;
Landroid/telecom/TelecomManager;->getSystemDialerPackage()Ljava/lang/String;
Landroid/telecom/TelecomManager;->getUserSelectedOutgoingPhoneAccount()Landroid/telecom/PhoneAccountHandle;
Landroid/telecom/VideoProfile$CameraCapabilities;-><init>(IIZF)V
Landroid/telephony/SubscriptionManager;->DEFAULT_SUBSCRIPTION_ID:I
Landroid/telephony/SubscriptionManager;->getSlotIndex(I)I
Landroid/telephony/SubscriptionManager;->isValidSubscriptionId(I)Z
Landroid/text/style/SuggestionSpan;->getUnderlineColor()I
Landroid/text/TextPaint;->underlineColor:I
Landroid/text/TextPaint;->underlineThickness:F
Landroid/util/ArrayMap;->indexOfValue(Ljava/lang/Object;)I
Landroid/util/ArraySet;-><init>(Ljava/util/Collection;)V
Landroid/view/InputDevice;->isExternal()Z
Landroid/view/SurfaceControl$Transaction;->apply()V
Landroid/view/SurfaceControl$Transaction;-><init>()V
Landroid/view/SurfaceControl$Transaction;->setAlpha(Landroid/view/SurfaceControl;F)Landroid/view/SurfaceControl$Transaction;
Landroid/view/SurfaceControl$Transaction;->setLayer(Landroid/view/SurfaceControl;I)Landroid/view/SurfaceControl$Transaction;
Landroid/view/View;->getAccessibilityDelegate()Landroid/view/View$AccessibilityDelegate;
Landroid/view/View;->getLocationInSurface([I)V
Landroid/view/View;->getTransitionAlpha()F
Landroid/view/ViewGroup;->suppressLayout(Z)V
Landroid/view/View;->setAnimationMatrix(Landroid/graphics/Matrix;)V
Landroid/view/View;->setLeftTopRightBottom(IIII)V
Landroid/view/View;->setTransitionAlpha(F)V
Landroid/view/View;->transformMatrixToGlobal(Landroid/graphics/Matrix;)V
Landroid/view/View;->transformMatrixToLocal(Landroid/graphics/Matrix;)V
Landroid/view/WindowInsets;->inset(IIII)Landroid/view/WindowInsets;
Landroid/widget/ImageView;->animateTransform(Landroid/graphics/Matrix;)V
Landroid/widget/PopupWindow;->setEpicenterBounds(Landroid/graphics/Rect;)V
Landroid/widget/PopupWindow;->setTouchModal(Z)V
Landroid/widget/TextView;->getTextDirectionHeuristic()Landroid/text/TextDirectionHeuristic;
Landroid/widget/TextView;->isSingleLine()Z
Lcom/android/org/conscrypt/AbstractConscryptSocket;->getApplicationProtocol()Ljava/lang/String;
Lcom/android/org/conscrypt/AbstractConscryptSocket;->getHandshakeApplicationProtocol()Ljava/lang/String;
Ljava/util/concurrent/ConcurrentHashMap$BaseIterator;->hasMoreElements()Z
Ljava/util/HashMap$HashIterator;->hasNext()Z
Ljava/util/HashMap$HashIterator;->remove()V
Ljava/util/LinkedHashMap$LinkedHashIterator;->hasNext()Z
Ljava/util/zip/ZipConstants;->CENATT:I
Ljava/util/zip/ZipConstants;->CENATX:I
Ljava/util/zip/ZipConstants;->CENCOM:I
Ljava/util/zip/ZipConstants;->CENCRC:I
Ljava/util/zip/ZipConstants;->CENDSK:I
Ljava/util/zip/ZipConstants;->CENEXT:I
Ljava/util/zip/ZipConstants;->CENFLG:I
Ljava/util/zip/ZipConstants;->CENHDR:I
Ljava/util/zip/ZipConstants;->CENHOW:I
Ljava/util/zip/ZipConstants;->CENLEN:I
Ljava/util/zip/ZipConstants;->CENNAM:I
Ljava/util/zip/ZipConstants;->CENOFF:I
Ljava/util/zip/ZipConstants;->CENSIG:J
Ljava/util/zip/ZipConstants;->CENSIZ:I
Ljava/util/zip/ZipConstants;->CENTIM:I
Ljava/util/zip/ZipConstants;->CENVEM:I
Ljava/util/zip/ZipConstants;->CENVER:I
Ljava/util/zip/ZipConstants;->ENDCOM:I
Ljava/util/zip/ZipConstants;->ENDHDR:I
Ljava/util/zip/ZipConstants;->ENDOFF:I
Ljava/util/zip/ZipConstants;->ENDSIG:J
Ljava/util/zip/ZipConstants;->ENDSIZ:I
Ljava/util/zip/ZipConstants;->ENDSUB:I
Ljava/util/zip/ZipConstants;->ENDTOT:I
Ljava/util/zip/ZipConstants;->EXTCRC:I
Ljava/util/zip/ZipConstants;->EXTHDR:I
Ljava/util/zip/ZipConstants;->EXTLEN:I
Ljava/util/zip/ZipConstants;->EXTSIG:J
Ljava/util/zip/ZipConstants;->EXTSIZ:I
Ljava/util/zip/ZipConstants;->LOCCRC:I
Ljava/util/zip/ZipConstants;->LOCEXT:I
Ljava/util/zip/ZipConstants;->LOCFLG:I
Ljava/util/zip/ZipConstants;->LOCHDR:I
Ljava/util/zip/ZipConstants;->LOCHOW:I
Ljava/util/zip/ZipConstants;->LOCLEN:I
Ljava/util/zip/ZipConstants;->LOCNAM:I
Ljava/util/zip/ZipConstants;->LOCSIG:J
Ljava/util/zip/ZipConstants;->LOCSIZ:I
Ljava/util/zip/ZipConstants;->LOCTIM:I
Ljava/util/zip/ZipConstants;->LOCVER:I
```