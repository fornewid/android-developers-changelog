---
title: https://developer.android.com/about/versions/11/non-sdk-11
url: https://developer.android.com/about/versions/11/non-sdk-11
source: md.txt
---

Android 11 includes updated lists of restricted non-SDK
interfaces based on collaboration with Android developers and the latest
internal testing. Whenever possible, we make sure that public alternatives are
available before we restrict non-SDK interfaces.

If your app does not target Android 11, some of these changes
might not immediately affect you. However, while you can currently use some
non-SDK interfaces ([depending on your app's target API level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names)),
using any non-SDK method or field always carries a high risk of breaking your
app.

If you are unsure if your app uses non-SDK interfaces, you can [test your
app](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#test-for-non-sdk)
to find out. If your app relies on non-SDK interfaces, you should begin planning
a migration to SDK alternatives. Nevertheless, we understand that some apps have
valid use cases for using non-SDK interfaces. If you cannot find an alternative
to using a non-SDK interface for a feature in your app, you should [request a
new public API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request).

## Non-SDK test APIs now restricted

Starting in Android 11, non-SDK test APIs---those annotated with
`@TestApi` in AOSP---are now blocked by default. These non-SDK interfaces are
used to perform internal testing on the Android platform. Apps can continue to
use non-SDK test APIs that are not [restricted at their target API
level](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#list-names),
but any new test APIs will be included in the blocklist.

## List changes for Android 11

The list changes in Android 11 fall into the following categories:

- Non-SDK interfaces that were unsupported (greylisted) in Android 10 (API level 29) that are now [blocked in Android 11 (API level 30)](https://developer.android.com/about/versions/11/non-sdk-11#new-blocked).
- Non-SDK interfaces that were [added to the Android SDK in Android 11](https://developer.android.com/about/versions/11/non-sdk-11#new-sdk).

For a complete list of all non-SDK interfaces for Android 11 (API level 30),
download the following file: [`hiddenapi-flags.csv`](https://dl.google.com/developers/android/rvc/non-sdk/hiddenapi-flags.csv).

### Non-SDK interfaces that are now blocked in Android 11

### Change details

**Change Name** : `HIDE_MAXTARGETSDK_Q_HIDDEN_APIS`

**Change ID** : `149994052`

### How to toggle

As you test your app's compatibility with Android 11, you can toggle this change on or off
using the following ADB commands:

    adb shell am compat enable (149994052|HIDE_MAXTARGETSDK_Q_HIDDEN_APIS) PACKAGE_NAME
    adb shell am compat disable (149994052|HIDE_MAXTARGETSDK_Q_HIDDEN_APIS) PACKAGE_NAME

For more information about the compatibility framework and toggling changes, see
[Test and debug platform behavior changes in
your app](https://developer.android.com/guide/app-compatibility/test-debug).

The following code box lists all of the non-SDK interfaces that were unsupported
(greylisted) in Android 10 (API level 29) that are blocked in Android 11 (API
level 30). That is, these interfaces belong to the `max-target-q`
(`greylist-max-q`) list, so your app can only use these interfaces if it targets
Android 10 (API level 29) or lower.

Our goal is to make sure that public alternatives are available before we
restrict non-SDK interfaces, and we understand that your app might have a valid
use case for using these interfaces. If an interface that your app uses in a
prior version is blocked in Android 11, you should [request a new public
API](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces#feature-request)
for that interface.

```
Landroid/app/Activity;->mParent:Landroid/app/Activity;   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/AppOpsManager$OpEntry;->getOp()I   # getOpStr().
Landroid/app/AppOpsManager$OpEntry;->getRejectTime()J   # getLastRejectTime(int).
Landroid/app/AppOpsManager$OpEntry;->getTime()J   # getLastAccessTime(int).
Landroid/app/AppOpsManager;->getToken(Lcom/android/internal/app/IAppOpsService;)Landroid/os/IBinder;   # Create own local android.os.Binder.
Landroid/app/AppOpsManager;->noteOp(I)I   # Use #noteOp(java.lang.String, int, java.lang.String, java.lang.String, java.lang.String) instead.
Landroid/app/AppOpsManager;->noteOp(IILjava/lang/String;)I   # Use #noteOp(java.lang.String, int, java.lang.String, java.lang.String, java.lang.String) instead.
Landroid/app/AppOpsManager;->noteOpNoThrow(IILjava/lang/String;)I   # Use #noteOpNoThrow(java.lang.String, int, java.lang.String, java.lang.String, java.lang.String) instead.
Landroid/app/AppOpsManager;->noteProxyOp(ILjava/lang/String;)I   # Use #noteProxyOp(java.lang.String, java.lang.String, int, java.lang.String, java.lang.String) instead.
Landroid/app/IActivityManager;->broadcastIntent(Landroid/app/IApplicationThread;Landroid/content/Intent;Ljava/lang/String;Landroid/content/IIntentReceiver;ILjava/lang/String;Landroid/os/Bundle;[Ljava/lang/String;ILandroid/os/Bundle;ZZI)I   # Use android.content.Context#sendBroadcast(android.content.Intent) instead.
Landroid/app/IActivityManager;->getIntentSender(ILjava/lang/String;Landroid/os/IBinder;Ljava/lang/String;I[Landroid/content/Intent;[Ljava/lang/String;ILandroid/os/Bundle;I)Landroid/content/IIntentSender;   # Use PendingIntent#getIntentSender() instead.
Landroid/app/IActivityManager;->getProviderMimeType(Landroid/net/Uri;I)Ljava/lang/String;   # Use android.content.ContentResolver#getType public API instead.
Landroid/app/IActivityManager;->registerReceiver(Landroid/app/IApplicationThread;Ljava/lang/String;Landroid/content/IIntentReceiver;Landroid/content/IntentFilter;Ljava/lang/String;II)Landroid/content/Intent;   # Use android.content.Context#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter) instead.
Landroid/app/IActivityManager;->startActivity(Landroid/app/IApplicationThread;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;)I   # Use android.content.Context#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter) instead.
Landroid/app/IActivityManager;->startActivityAsUser(Landroid/app/IApplicationThread;Ljava/lang/String;Landroid/content/Intent;Ljava/lang/String;Landroid/os/IBinder;Ljava/lang/String;IILandroid/app/ProfilerInfo;Landroid/os/Bundle;I)I   # Use android.content.Context#createContextAsUser(android.os.UserHandle, int) and android.content.Context#startActivity(android.content.Intent) instead.
Landroid/app/LocalActivityManager;->mActivities:Ljava/util/Map;   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/LocalActivityManager;->mActivityArray:Ljava/util/ArrayList;   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/LocalActivityManager;->mParent:Landroid/app/Activity;   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/LocalActivityManager;->mResumed:Landroid/app/LocalActivityManager$LocalActivityRecord;   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/LocalActivityManager;->mSingleMode:Z   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/app/LocalActivityManager;->moveToState(Landroid/app/LocalActivityManager$LocalActivityRecord;I)V   # Use androidx.fragment.app.Fragment and androidx.fragment.app.FragmentManager instead.
Landroid/content/IContentProvider;->bulkInsert(Ljava/lang/String;Landroid/net/Uri;[Landroid/content/ContentValues;)I   # Use ContentProviderClient#bulkInsert(android.net.Uri, android.content.ContentValues[]) instead.
Landroid/content/IContentProvider;->call(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;   # Use ContentProviderClient#call(java.lang.String, java.lang.String, android.os.Bundle) instead.
Landroid/content/IContentProvider;->delete(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I   # Use ContentProviderClient#delete(android.net.Uri, java.lang.String, java.lang.String[]) instead.
Landroid/content/IContentProvider;->insert(Ljava/lang/String;Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;   # Use ContentProviderClient#insert(android.net.Uri, android.content.ContentValues) instead.
Landroid/content/IContentProvider;->update(Ljava/lang/String;Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I   # Use ContentProviderClient#update(android.net.Uri, android.content.ContentValues, java.lang.String, java.lang.String[]) instead.
Landroid/graphics/FontFamily;-><init>()V   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;-><init>([Ljava/lang/String;I)V   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->abortCreation()V   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->addFont(Ljava/lang/String;I[Landroid/graphics/fonts/FontVariationAxis;II)Z   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->addFontFromAssetManager(Landroid/content/res/AssetManager;Ljava/lang/String;IZIII[Landroid/graphics/fonts/FontVariationAxis;)Z   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->addFontFromBuffer(Ljava/nio/ByteBuffer;I[Landroid/graphics/fonts/FontVariationAxis;II)Z   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->freeze()Z   # Use android.graphics.fonts.FontFamily instead.
Landroid/graphics/FontFamily;->mNativePtr:J   # Use android.graphics.fonts.FontFamily instead.
Landroid/media/MediaScanner$FileEntry;-><init>(JLjava/lang/String;JI)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$FileEntry;->mLastModifiedChanged:Z   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$FileEntry;->mRowId:J   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->beginFile(Ljava/lang/String;Ljava/lang/String;JJZZ)Landroid/media/MediaScanner$FileEntry;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->doScanFile(Ljava/lang/String;Ljava/lang/String;JJZZZ)Landroid/net/Uri;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->endFile(Landroid/media/MediaScanner$FileEntry;ZZZZZZ)Landroid/net/Uri;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->getFileTypeFromDrm(Ljava/lang/String;)I   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->handleStringTag(Ljava/lang/String;Ljava/lang/String;)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->mFileType:I   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->mIsDrm:Z   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->mMimeType:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->mNoMedia:Z   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->mPath:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->scanFile(Ljava/lang/String;JJZZ)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->setMimeType(Ljava/lang/String;)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner$MyMediaScannerClient;->toValues()Landroid/content/ContentValues;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;-><init>(Landroid/content/Context;Ljava/lang/String;)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->FILES_PRESCAN_PROJECTION:[Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->isDrmEnabled()Z   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->isNoMediaPath(Ljava/lang/String;)Z   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mAudioUri:Landroid/net/Uri;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mClient:Landroid/media/MediaScanner$MyMediaScannerClient;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mContext:Landroid/content/Context;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mDefaultAlarmAlertFilename:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mDefaultNotificationFilename:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mDefaultRingtoneFilename:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mFilesUri:Landroid/net/Uri;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mMediaInserter:Landroid/media/MediaInserter;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->mPackageName:Ljava/lang/String;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->makeEntryFor(Ljava/lang/String;)Landroid/media/MediaScanner$FileEntry;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->postscan([Ljava/lang/String;)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->prescan(Ljava/lang/String;Z)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->scanSingleFile(Ljava/lang/String;Ljava/lang/String;)Landroid/net/Uri;   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/media/MediaScanner;->setLocale(Ljava/lang/String;)V   # All scanning requests should be performed through android.media.MediaScannerConnection.
Landroid/net/IConnectivityManager;->getLastTetherError(Ljava/lang/String;)I   # Use TetheringManager#getLastTetherError as alternative.
Landroid/net/IConnectivityManager;->getTetherableIfaces()[Ljava/lang/String;   # Use TetheringManager#getTetherableIfaces as alternative.
Landroid/net/IConnectivityManager;->getTetherableUsbRegexs()[Ljava/lang/String;   # Use TetheringManager#getTetherableUsbRegexs as alternative.
Landroid/net/IConnectivityManager;->getTetherableWifiRegexs()[Ljava/lang/String;   # Use TetheringManager#getTetherableWifiRegexs as alternative.
Landroid/net/IConnectivityManager;->getTetheredIfaces()[Ljava/lang/String;   # Use TetheringManager#getTetheredIfaces as alternative.
Landroid/net/IConnectivityManager;->getTetheringErroredIfaces()[Ljava/lang/String;   # Use TetheringManager#getTetheringErroredIfaces as Alternative.
Landroid/net/wifi/WifiManager;->enableVerboseLogging(I)V   # Use #setVerboseLoggingEnabled(boolean) instead.
Landroid/net/wifi/WifiManager;->getVerboseLoggingLevel()I   # Use #isVerboseLoggingEnabled() instead.
Landroid/os/PowerManager;->ACTION_POWER_SAVE_MODE_CHANGING:Ljava/lang/String;   # Use #ACTION_POWER_SAVE_MODE_CHANGED instead.
Landroid/os/PowerManager;->EXTRA_POWER_SAVE_MODE:Ljava/lang/String;   # Use #isPowerSaveMode() instead.
Landroid/os/storage/StorageVolume;->getPath()Ljava/lang/String;   # StorageVolume#getDirectory().
Landroid/os/storage/StorageVolume;->getPathFile()Ljava/io/File;   # StorageVolume#getDirectory().
Landroid/telephony/ServiceState;->getDataOperatorAlphaShort()Ljava/lang/String;   # Use #getOperatorAlphaShort instead.
Landroid/telephony/ServiceState;->getDataOperatorNumeric()Ljava/lang/String;   # Use #getOperatorNumeric instead.
Landroid/telephony/ServiceState;->getVoiceOperatorAlphaLong()Ljava/lang/String;   # Use #getOperatorAlphaLong instead.
Landroid/telephony/ServiceState;->getVoiceOperatorAlphaShort()Ljava/lang/String;   # Use #getOperatorAlphaShort instead.
Landroid/telephony/TelephonyManager;->getNetworkCountryIsoForPhone(I)Ljava/lang/String; # Use #getNetworkCountryIso(int) instead.
Landroid/telephony/ims/ImsReasonInfo;->mCode:I   # getCode().
Landroid/telephony/ims/ImsReasonInfo;->mExtraCode:I   # getExtraCode().
Landroid/telephony/ims/ImsReasonInfo;->mExtraMessage:Ljava/lang/String;   # getExtraMessage().
Landroid/view/inputmethod/InputMethodManager;->windowDismissed(Landroid/os/IBinder;)V   # See https://developer.android.com/reference/androidx/activity/ComponentActivity.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionAction(III)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionAction(IIILandroid/view/textclassifier/TextClassification;)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionModified(II)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionModified(IILandroid/view/textclassifier/TextClassification;)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionModified(IILandroid/view/textclassifier/TextSelection;)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;->selectionStarted(I)Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker;-><init>(Landroid/content/Context;I)V   # See android.view.textclassifier.TextClassifier.
Landroid/view/textclassifier/logging/SmartSelectionEventTracker;->logEvent(Landroid/view/textclassifier/logging/SmartSelectionEventTracker$SelectionEvent;)V   # See android.view.textclassifier.TextClassifier.
Landroid/view/View$AttachInfo;->mContentInsets:Landroid/graphics/Rect;   # Use WindowInsets#getInsets(int) instead.
Landroid/view/View$AttachInfo;->mStableInsets:Landroid/graphics/Rect;   # Use WindowInsets#getInsets(int) instead.
Landroid/view/View$AttachInfo;->mVisibleInsets:Landroid/graphics/Rect;   # Use WindowInsets#getInsets(int) instead.
Landroid/widget/TabHost$IntentContentStrategy;->getContentView()Landroid/view/View;   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost$IntentContentStrategy;->tabClosed()V   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost$TabSpec;->mContentStrategy:Landroid/widget/TabHost$ContentStrategy;   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost$TabSpec;->mIndicatorStrategy:Landroid/widget/TabHost$IndicatorStrategy;   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost;->mCurrentTab:I   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost;->mOnTabChangeListener:Landroid/widget/TabHost$OnTabChangeListener;   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabHost;->mTabSpecs:Ljava/util/List;   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabWidget;->mDrawBottomStrips:Z   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Landroid/widget/TabWidget;->mSelectedTab:I   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/about/versions/11/guide/navigation/navigation-swipe-view.
Landroid/widget/TabWidget;->setTabSelectionListener(Landroid/widget/TabWidget$OnTabSelectionChanged;)V   # Use androidx.viewpager.widget.ViewPager and com.google.android.material.tabs.TabLayout instead. See https://developer.android.com/guide/navigation/navigation-swipe-view.
Lcom/android/internal/telephony/MccTable$MccEntry;->mIso:Ljava/lang/String;   # There is no alternative for MccTable.MccEntry.mIso, but it was included in hidden APIs due to a static analysis false positive and has been added to this max-target-q (greylist-max-q) list. Please file a bug if you still require this API.
Lcom/android/internal/telephony/MccTable;->entryForMcc(I)Lcom/android/internal/telephony/MccTable$MccEntry;   # There is no alternative for MccTable.entryForMcc, but it was included in hidden APIs due to a static analysis false positive and has been added to this max-target-q (greylist-max-q) list. Please file a bug if you still require this API.
Lcom/android/internal/telephony/MccTable;->smallestDigitsMccForMnc(I)I   # There is no alternative for MccTable.smallestDigitsMccForMnc, but it was included in hidden APIs due to a static analysis false positive and has been added to this max-target-q (greylist-max-q) list. Please file a bug if you still require this API.
Lcom/android/org/conscrypt/AbstractConscryptSocket;->getAlpnSelectedProtocol()[B   # Use javax.net.ssl.SSLSocket#getApplicationProtocol().
Lcom/android/org/conscrypt/AbstractConscryptSocket;->getApplicationProtocols()[Ljava/lang/String;   # Use javax.net.ssl.SSLParameters#getApplicationProtocols().
Lcom/android/org/conscrypt/AbstractConscryptSocket;->setAlpnProtocols([B)V   # Use javax.net.ssl.SSLParameters#setApplicationProtocols(java.lang.String[]).
Lcom/android/org/conscrypt/AbstractConscryptSocket;->setAlpnProtocols([Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setApplicationProtocols(java.lang.String[]).
Lcom/android/org/conscrypt/AbstractConscryptSocket;->setApplicationProtocols([Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setApplicationProtocols(java.lang.String[]).
Lcom/android/org/conscrypt/AbstractConscryptSocket;->setHostname(Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setServerNames.
Lcom/android/org/conscrypt/AbstractConscryptSocket;->setUseSessionTickets(Z)V   # Use android.net.ssl.SSLSockets#setUseSessionTickets.
Lcom/android/org/conscrypt/ConscryptFileDescriptorSocket;->setHostname(Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setServerNames.
Lcom/android/org/conscrypt/ConscryptFileDescriptorSocket;->setUseSessionTickets(Z)V   # Use android.net.ssl.SSLSockets#setUseSessionTickets.
Lcom/android/org/conscrypt/OpenSSLSocketImpl;->getAlpnSelectedProtocol()[B   # Use javax.net.ssl.SSLSocket#getApplicationProtocol().
Lcom/android/org/conscrypt/OpenSSLSocketImpl;->setAlpnProtocols([B)V   # Use javax.net.ssl.SSLParameters#setApplicationProtocols(java.lang.String[]).
Lcom/android/org/conscrypt/OpenSSLSocketImpl;->setAlpnProtocols([Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setApplicationProtocols(java.lang.String[]).
Lcom/android/org/conscrypt/OpenSSLSocketImpl;->setHostname(Ljava/lang/String;)V   # Use javax.net.ssl.SSLParameters#setServerNames.
Lcom/android/org/conscrypt/OpenSSLSocketImpl;->setUseSessionTickets(Z)V   # Use android.net.ssl.SSLSockets#setUseSessionTickets.
Llibcore/util/EmptyArray;->BYTE:[B   # Use new byte[0] instead.
Llibcore/util/EmptyArray;->INT:[I   # Use new int[0] instead.
Llibcore/util/EmptyArray;->LONG:[J   # Use new long[0] instead.
Llibcore/util/EmptyArray;->OBJECT:[Ljava/lang/Object;   # Use new Object[0] instead.

# All of the following non-SDK interfaces are resource IDs. Apps should not directly access resource IDs.
# Instead, access resource IDs using resource.xml files or the https://developer.android.com/reference/android/content/res/Resources#getIdentifier(java.lang.String,%2520java.lang.String,%2520java.lang.String) method.

Landroid/R$styleable;->ActionBar:[I
Landroid/R$styleable;->ActionBar_background:I
Landroid/R$styleable;->ActionBar_backgroundSplit:I
Landroid/R$styleable;->ActionBar_backgroundStacked:I
Landroid/R$styleable;->ActionBar_divider:I
Landroid/R$styleable;->ActionBar_itemPadding:I
Landroid/R$styleable;->CalendarView:[I
Landroid/R$styleable;->CalendarView_dateTextAppearance:I
Landroid/R$styleable;->CalendarView_firstDayOfWeek:I
Landroid/R$styleable;->CalendarView_focusedMonthDateColor:I
Landroid/R$styleable;->CalendarView_selectedDateVerticalBar:I
Landroid/R$styleable;->CalendarView_selectedWeekBackgroundColor:I
Landroid/R$styleable;->CalendarView_showWeekNumber:I
Landroid/R$styleable;->CalendarView_shownWeekCount:I
Landroid/R$styleable;->CalendarView_unfocusedMonthDateColor:I
Landroid/R$styleable;->CalendarView_weekDayTextAppearance:I
Landroid/R$styleable;->CalendarView_weekNumberColor:I
Landroid/R$styleable;->CalendarView_weekSeparatorLineColor:I
Landroid/R$styleable;->CheckBoxPreference:[I
Landroid/R$styleable;->CheckedTextView:[I
Landroid/R$styleable;->CheckedTextView_checkMark:I
Landroid/R$styleable;->CompoundButton:[I
Landroid/R$styleable;->CompoundButton_button:I
Landroid/R$styleable;->ContactsDataKind:[I
Landroid/R$styleable;->DatePicker:[I
Landroid/R$styleable;->DialogPreference:[I
Landroid/R$styleable;->DrawableStates:[I
Landroid/R$styleable;->ExpandableListView:[I
Landroid/R$styleable;->FrameLayout_Layout:[I
Landroid/R$styleable;->HorizontalScrollView:[I
Landroid/R$styleable;->ImageView:[I
Landroid/R$styleable;->ImageView_adjustViewBounds:I
Landroid/R$styleable;->ImageView_baselineAlignBottom:I
Landroid/R$styleable;->ImageView_cropToPadding:I
Landroid/R$styleable;->ImageView_maxHeight:I
Landroid/R$styleable;->ImageView_maxWidth:I
Landroid/R$styleable;->ImageView_scaleType:I
Landroid/R$styleable;->ImageView_src:I
Landroid/R$styleable;->ImageView_tint:I
Landroid/R$styleable;->Keyboard:[I
Landroid/R$styleable;->Keyboard_Key:[I
Landroid/R$styleable;->Keyboard_Key_codes:I
Landroid/R$styleable;->Keyboard_Key_iconPreview:I
Landroid/R$styleable;->Keyboard_Key_isModifier:I
Landroid/R$styleable;->Keyboard_Key_isRepeatable:I
Landroid/R$styleable;->Keyboard_Key_isSticky:I
Landroid/R$styleable;->Keyboard_Key_keyEdgeFlags:I
Landroid/R$styleable;->Keyboard_Key_keyIcon:I
Landroid/R$styleable;->Keyboard_Key_keyLabel:I
Landroid/R$styleable;->Keyboard_Key_keyOutputText:I
Landroid/R$styleable;->Keyboard_Key_popupCharacters:I
Landroid/R$styleable;->Keyboard_Key_popupKeyboard:I
Landroid/R$styleable;->Keyboard_Row:[I
Landroid/R$styleable;->Keyboard_Row_keyboardMode:I
Landroid/R$styleable;->Keyboard_Row_rowEdgeFlags:I
Landroid/R$styleable;->Keyboard_horizontalGap:I
Landroid/R$styleable;->Keyboard_keyHeight:I
Landroid/R$styleable;->Keyboard_keyWidth:I
Landroid/R$styleable;->Keyboard_verticalGap:I
Landroid/R$styleable;->LinearLayout:[I
Landroid/R$styleable;->LinearLayout_Layout:[I
Landroid/R$styleable;->LinearLayout_Layout_layout_gravity:I
Landroid/R$styleable;->LinearLayout_Layout_layout_height:I
Landroid/R$styleable;->LinearLayout_Layout_layout_weight:I
Landroid/R$styleable;->LinearLayout_Layout_layout_width:I
Landroid/R$styleable;->LinearLayout_baselineAligned:I
Landroid/R$styleable;->LinearLayout_baselineAlignedChildIndex:I
Landroid/R$styleable;->LinearLayout_divider:I
Landroid/R$styleable;->LinearLayout_dividerPadding:I
Landroid/R$styleable;->LinearLayout_gravity:I
Landroid/R$styleable;->LinearLayout_measureWithLargestChild:I
Landroid/R$styleable;->LinearLayout_orientation:I
Landroid/R$styleable;->LinearLayout_showDividers:I
Landroid/R$styleable;->ListView:[I
Landroid/R$styleable;->ListView_divider:I
Landroid/R$styleable;->ListView_dividerHeight:I
Landroid/R$styleable;->LockPatternView:[I
Landroid/R$styleable;->NumberPicker:[I
Landroid/R$styleable;->NumberPicker_solidColor:I
Landroid/R$styleable;->PopupWindow:[I
Landroid/R$styleable;->ProgressBar:[I
Landroid/R$styleable;->ProgressBar_indeterminateDrawable:I
Landroid/R$styleable;->ProgressBar_indeterminateDuration:I
Landroid/R$styleable;->ProgressBar_maxHeight:I
Landroid/R$styleable;->ProgressBar_maxWidth:I
Landroid/R$styleable;->ProgressBar_minHeight:I
Landroid/R$styleable;->ProgressBar_minWidth:I
Landroid/R$styleable;->ProgressBar_progressDrawable:I
Landroid/R$styleable;->RingtonePreference:[I
Landroid/R$styleable;->ScrollView:[I
Landroid/R$styleable;->SearchView:[I
Landroid/R$styleable;->SeekBar:[I
Landroid/R$styleable;->SeekBar_thumb:I
Landroid/R$styleable;->SeekBar_thumbOffset:I
Landroid/R$styleable;->SlidingDrawer:[I
Landroid/R$styleable;->SlidingDrawer_allowSingleTap:I
Landroid/R$styleable;->SlidingDrawer_animateOnClick:I
Landroid/R$styleable;->SlidingDrawer_bottomOffset:I
Landroid/R$styleable;->SlidingDrawer_content:I
Landroid/R$styleable;->SlidingDrawer_handle:I
Landroid/R$styleable;->SlidingDrawer_orientation:I
Landroid/R$styleable;->SlidingDrawer_topOffset:I
Landroid/R$styleable;->Switch:[I
Landroid/R$styleable;->Switch_showText:I
Landroid/R$styleable;->Switch_splitTrack:I
Landroid/R$styleable;->Switch_switchMinWidth:I
Landroid/R$styleable;->Switch_switchPadding:I
Landroid/R$styleable;->Switch_switchTextAppearance:I
Landroid/R$styleable;->Switch_textOff:I
Landroid/R$styleable;->Switch_textOn:I
Landroid/R$styleable;->Switch_thumb:I
Landroid/R$styleable;->Switch_thumbTextPadding:I
Landroid/R$styleable;->Switch_track:I
Landroid/R$styleable;->TextAppearance:[I
Landroid/R$styleable;->TextAppearance_textAllCaps:I
Landroid/R$styleable;->TextAppearance_textColor:I
Landroid/R$styleable;->TextAppearance_textColorHighlight:I
Landroid/R$styleable;->TextAppearance_textColorHint:I
Landroid/R$styleable;->TextAppearance_textColorLink:I
Landroid/R$styleable;->TextAppearance_textSize:I
Landroid/R$styleable;->TextAppearance_textStyle:I
Landroid/R$styleable;->TextAppearance_typeface:I
Landroid/R$styleable;->TextView:[I
Landroid/R$styleable;->TextView_autoLink:I
Landroid/R$styleable;->TextView_autoText:I
Landroid/R$styleable;->TextView_bufferType:I
Landroid/R$styleable;->TextView_capitalize:I
Landroid/R$styleable;->TextView_cursorVisible:I
Landroid/R$styleable;->TextView_digits:I
Landroid/R$styleable;->TextView_drawableBottom:I
Landroid/R$styleable;->TextView_drawableEnd:I
Landroid/R$styleable;->TextView_drawableLeft:I
Landroid/R$styleable;->TextView_drawablePadding:I
Landroid/R$styleable;->TextView_drawableRight:I
Landroid/R$styleable;->TextView_drawableStart:I
Landroid/R$styleable;->TextView_drawableTop:I
Landroid/R$styleable;->TextView_editable:I
Landroid/R$styleable;->TextView_ellipsize:I
Landroid/R$styleable;->TextView_ems:I
Landroid/R$styleable;->TextView_enabled:I
Landroid/R$styleable;->TextView_freezesText:I
Landroid/R$styleable;->TextView_gravity:I
Landroid/R$styleable;->TextView_height:I
Landroid/R$styleable;->TextView_hint:I
Landroid/R$styleable;->TextView_imeActionId:I
Landroid/R$styleable;->TextView_imeActionLabel:I
Landroid/R$styleable;->TextView_imeOptions:I
Landroid/R$styleable;->TextView_includeFontPadding:I
Landroid/R$styleable;->TextView_inputMethod:I
Landroid/R$styleable;->TextView_inputType:I
Landroid/R$styleable;->TextView_lineSpacingExtra:I
Landroid/R$styleable;->TextView_lineSpacingMultiplier:I
Landroid/R$styleable;->TextView_lines:I
Landroid/R$styleable;->TextView_linksClickable:I
Landroid/R$styleable;->TextView_marqueeRepeatLimit:I
Landroid/R$styleable;->TextView_maxEms:I
Landroid/R$styleable;->TextView_maxHeight:I
Landroid/R$styleable;->TextView_maxLength:I
Landroid/R$styleable;->TextView_maxLines:I
Landroid/R$styleable;->TextView_maxWidth:I
Landroid/R$styleable;->TextView_minEms:I
Landroid/R$styleable;->TextView_minHeight:I
Landroid/R$styleable;->TextView_minLines:I
Landroid/R$styleable;->TextView_minWidth:I
Landroid/R$styleable;->TextView_numeric:I
Landroid/R$styleable;->TextView_password:I
Landroid/R$styleable;->TextView_phoneNumber:I
Landroid/R$styleable;->TextView_privateImeOptions:I
Landroid/R$styleable;->TextView_scrollHorizontally:I
Landroid/R$styleable;->TextView_selectAllOnFocus:I
Landroid/R$styleable;->TextView_shadowColor:I
Landroid/R$styleable;->TextView_shadowDx:I
Landroid/R$styleable;->TextView_shadowDy:I
Landroid/R$styleable;->TextView_shadowRadius:I
Landroid/R$styleable;->TextView_singleLine:I
Landroid/R$styleable;->TextView_text:I
Landroid/R$styleable;->TextView_textAllCaps:I
Landroid/R$styleable;->TextView_textAppearance:I
Landroid/R$styleable;->TextView_textColor:I
Landroid/R$styleable;->TextView_textColorHighlight:I
Landroid/R$styleable;->TextView_textColorHint:I
Landroid/R$styleable;->TextView_textColorLink:I
Landroid/R$styleable;->TextView_textCursorDrawable:I
Landroid/R$styleable;->TextView_textIsSelectable:I
Landroid/R$styleable;->TextView_textScaleX:I
Landroid/R$styleable;->TextView_textSelectHandle:I
Landroid/R$styleable;->TextView_textSelectHandleLeft:I
Landroid/R$styleable;->TextView_textSelectHandleRight:I
Landroid/R$styleable;->TextView_textSize:I
Landroid/R$styleable;->TextView_textStyle:I
Landroid/R$styleable;->TextView_typeface:I
Landroid/R$styleable;->TextView_width:I
Landroid/R$styleable;->Theme:[I
Landroid/R$styleable;->View:[I
Landroid/R$styleable;->ViewDrawableStates:[I
Landroid/R$styleable;->ViewGroup_Layout:[I
Landroid/R$styleable;->ViewGroup_Layout_layout_height:I
Landroid/R$styleable;->ViewGroup_Layout_layout_width:I
Landroid/R$styleable;->ViewGroup_MarginLayout:[I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_height:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_margin:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_marginBottom:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_marginLeft:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_marginRight:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_marginTop:I
Landroid/R$styleable;->ViewGroup_MarginLayout_layout_width:I
Landroid/R$styleable;->View_alpha:I
Landroid/R$styleable;->View_background:I
Landroid/R$styleable;->View_clickable:I
Landroid/R$styleable;->View_contentDescription:I
Landroid/R$styleable;->View_drawingCacheQuality:I
Landroid/R$styleable;->View_duplicateParentState:I
Landroid/R$styleable;->View_fadingEdge:I
Landroid/R$styleable;->View_filterTouchesWhenObscured:I
Landroid/R$styleable;->View_fitsSystemWindows:I
Landroid/R$styleable;->View_focusable:I
Landroid/R$styleable;->View_focusableInTouchMode:I
Landroid/R$styleable;->View_hapticFeedbackEnabled:I
Landroid/R$styleable;->View_id:I
Landroid/R$styleable;->View_isScrollContainer:I
Landroid/R$styleable;->View_keepScreenOn:I
Landroid/R$styleable;->View_longClickable:I
Landroid/R$styleable;->View_minHeight:I
Landroid/R$styleable;->View_minWidth:I
Landroid/R$styleable;->View_nextFocusDown:I
Landroid/R$styleable;->View_nextFocusLeft:I
Landroid/R$styleable;->View_nextFocusRight:I
Landroid/R$styleable;->View_nextFocusUp:I
Landroid/R$styleable;->View_onClick:I
Landroid/R$styleable;->View_overScrollMode:I
Landroid/R$styleable;->View_padding:I
Landroid/R$styleable;->View_paddingBottom:I
Landroid/R$styleable;->View_paddingEnd:I
Landroid/R$styleable;->View_paddingLeft:I
Landroid/R$styleable;->View_paddingRight:I
Landroid/R$styleable;->View_paddingStart:I
Landroid/R$styleable;->View_paddingTop:I
Landroid/R$styleable;->View_rotation:I
Landroid/R$styleable;->View_rotationX:I
Landroid/R$styleable;->View_rotationY:I
Landroid/R$styleable;->View_saveEnabled:I
Landroid/R$styleable;->View_scaleX:I
Landroid/R$styleable;->View_scaleY:I
Landroid/R$styleable;->View_scrollX:I
Landroid/R$styleable;->View_scrollY:I
Landroid/R$styleable;->View_scrollbarDefaultDelayBeforeFade:I
Landroid/R$styleable;->View_scrollbarFadeDuration:I
Landroid/R$styleable;->View_scrollbarSize:I
Landroid/R$styleable;->View_scrollbarStyle:I
Landroid/R$styleable;->View_scrollbarThumbHorizontal:I
Landroid/R$styleable;->View_scrollbarThumbVertical:I
Landroid/R$styleable;->View_scrollbarTrackHorizontal:I
Landroid/R$styleable;->View_scrollbarTrackVertical:I
Landroid/R$styleable;->View_scrollbars:I
Landroid/R$styleable;->View_soundEffectsEnabled:I
Landroid/R$styleable;->View_tag:I
Landroid/R$styleable;->View_transformPivotX:I
Landroid/R$styleable;->View_transformPivotY:I
Landroid/R$styleable;->View_translationX:I
Landroid/R$styleable;->View_translationY:I
Landroid/R$styleable;->View_visibility:I
Landroid/R$styleable;->Window:[I
Landroid/R$styleable;->Window_windowBackground:I
Landroid/R$styleable;->Window_windowFrame:I
Lcom/android/internal/R$anim;->fade_in:I
Lcom/android/internal/R$array;->config_autoBrightnessLcdBacklightValues:I
Lcom/android/internal/R$array;->config_autoBrightnessLevels:I
Lcom/android/internal/R$array;->config_mobile_hotspot_provision_app:I
Lcom/android/internal/R$array;->config_sms_enabled_locking_shift_tables:I
Lcom/android/internal/R$array;->config_sms_enabled_single_shift_tables:I
Lcom/android/internal/R$array;->config_tether_bluetooth_regexs:I
Lcom/android/internal/R$array;->config_tether_upstream_types:I
Lcom/android/internal/R$array;->config_tether_usb_regexs:I
Lcom/android/internal/R$array;->config_tether_wifi_regexs:I
Lcom/android/internal/R$array;->maps_starting_lat_lng:I
Lcom/android/internal/R$array;->maps_starting_zoom:I
Lcom/android/internal/R$attr;->actionBarStyle:I
Lcom/android/internal/R$attr;->buttonStyle:I
Lcom/android/internal/R$attr;->description:I
Lcom/android/internal/R$attr;->editTextStyle:I
Lcom/android/internal/R$attr;->mapViewStyle:I
Lcom/android/internal/R$attr;->popupWindowStyle:I
Lcom/android/internal/R$attr;->state_above_anchor:I
Lcom/android/internal/R$attr;->state_focused:I
Lcom/android/internal/R$attr;->state_pressed:I
Lcom/android/internal/R$attr;->state_selected:I
Lcom/android/internal/R$attr;->switchStyle:I
Lcom/android/internal/R$attr;->text:I
Lcom/android/internal/R$attr;->title:I
Lcom/android/internal/R$attr;->webViewStyle:I
Lcom/android/internal/R$bool;-><init>()V
Lcom/android/internal/R$bool;->config_automatic_brightness_available:I
Lcom/android/internal/R$bool;->config_intrusiveNotificationLed:I
Lcom/android/internal/R$bool;->config_mms_content_disposition_support:I
Lcom/android/internal/R$bool;->config_showNavigationBar:I
Lcom/android/internal/R$dimen;-><init>()V
Lcom/android/internal/R$dimen;->item_touch_helper_max_drag_scroll_per_frame:I
Lcom/android/internal/R$dimen;->navigation_bar_height:I
Lcom/android/internal/R$dimen;->navigation_bar_height_landscape:I
Lcom/android/internal/R$dimen;->navigation_bar_width:I
Lcom/android/internal/R$dimen;->status_bar_height:I
Lcom/android/internal/R$dimen;->toast_y_offset:I
Lcom/android/internal/R$drawable;->btn_check_off:I
Lcom/android/internal/R$drawable;->compass_arrow:I
Lcom/android/internal/R$drawable;->compass_base:I
Lcom/android/internal/R$drawable;->ic_maps_indicator_current_position_anim:I
Lcom/android/internal/R$drawable;->ic_menu_close_clear_cancel:I
Lcom/android/internal/R$drawable;->loading_tile_android:I
Lcom/android/internal/R$drawable;->maps_google_logo:I
Lcom/android/internal/R$drawable;->no_tile_256:I
Lcom/android/internal/R$drawable;->reticle:I
Lcom/android/internal/R$drawable;->stat_sys_download:I
Lcom/android/internal/R$fraction;->config_autoBrightnessAdjustmentMaxGamma:I
Lcom/android/internal/R$id;->account_name:I
Lcom/android/internal/R$id;->account_type:I
Lcom/android/internal/R$id;->alertTitle:I
Lcom/android/internal/R$id;->allow_button:I
Lcom/android/internal/R$id;->amPm:I
Lcom/android/internal/R$id;->authtoken_type:I
Lcom/android/internal/R$id;->back_button:I
Lcom/android/internal/R$id;->background:I
Lcom/android/internal/R$id;->body:I
Lcom/android/internal/R$id;->buttonPanel:I
Lcom/android/internal/R$id;->camera:I
Lcom/android/internal/R$id;->cancel:I
Lcom/android/internal/R$id;->clip_children_set_tag:I
Lcom/android/internal/R$id;->clip_children_tag:I
Lcom/android/internal/R$id;->clip_to_padding_tag:I
Lcom/android/internal/R$id;->closeButton:I
Lcom/android/internal/R$id;->content:I
Lcom/android/internal/R$id;->contentPanel:I
Lcom/android/internal/R$id;->custom:I
Lcom/android/internal/R$id;->customPanel:I
Lcom/android/internal/R$id;->datePicker:I
Lcom/android/internal/R$id;->day:I
Lcom/android/internal/R$id;->deny_button:I
Lcom/android/internal/R$id;->description:I
Lcom/android/internal/R$id;->edit:I
Lcom/android/internal/R$id;->edittext_container:I
Lcom/android/internal/R$id;->find_next:I
Lcom/android/internal/R$id;->find_prev:I
Lcom/android/internal/R$id;->icon:I
Lcom/android/internal/R$id;->keyboard:I
Lcom/android/internal/R$id;->keyboardView:I
Lcom/android/internal/R$id;->line1:I
Lcom/android/internal/R$id;->list_item:I
Lcom/android/internal/R$id;->matches:I
Lcom/android/internal/R$id;->media_actions:I
Lcom/android/internal/R$id;->mediacontroller_progress:I
Lcom/android/internal/R$id;->message:I
Lcom/android/internal/R$id;->minute:I
Lcom/android/internal/R$id;->month:I
Lcom/android/internal/R$id;->notification_header:I
Lcom/android/internal/R$id;->ok:I
Lcom/android/internal/R$id;->overlay:I
Lcom/android/internal/R$id;->package_label:I
Lcom/android/internal/R$id;->packages_list:I
Lcom/android/internal/R$id;->parentPanel:I
Lcom/android/internal/R$id;->pause:I
Lcom/android/internal/R$id;->pending_intent_tag:I
Lcom/android/internal/R$id;->progress:I
Lcom/android/internal/R$id;->redo:I
Lcom/android/internal/R$id;->remote_input_tag:I
Lcom/android/internal/R$id;->right_icon:I
Lcom/android/internal/R$id;->search_src_text:I
Lcom/android/internal/R$id;->share:I
Lcom/android/internal/R$id;->shortcut:I
Lcom/android/internal/R$id;->status_bar_latest_event_content:I
Lcom/android/internal/R$id;->tabcontent:I
Lcom/android/internal/R$id;->tabs:I
Lcom/android/internal/R$id;->text1:I
Lcom/android/internal/R$id;->text2:I
Lcom/android/internal/R$id;->text:I
Lcom/android/internal/R$id;->time:I
Lcom/android/internal/R$id;->timePicker:I
Lcom/android/internal/R$id;->time_current:I
Lcom/android/internal/R$id;->title:I
Lcom/android/internal/R$id;->titleDivider:I
Lcom/android/internal/R$id;->titleDividerTop:I
Lcom/android/internal/R$id;->title_container:I
Lcom/android/internal/R$id;->title_template:I
Lcom/android/internal/R$id;->topPanel:I
Lcom/android/internal/R$id;->up:I
Lcom/android/internal/R$id;->year:I
Lcom/android/internal/R$id;->zoomControls:I
Lcom/android/internal/R$id;->zoomMagnify:I
Lcom/android/internal/R$integer;->config_screenBrightnessDim:I
Lcom/android/internal/R$integer;->config_screenBrightnessSettingMaximum:I
Lcom/android/internal/R$integer;->config_screenBrightnessSettingMinimum:I
Lcom/android/internal/R$integer;->config_toastDefaultGravity:I
Lcom/android/internal/R$interpolator;->accelerate_cubic:I
Lcom/android/internal/R$interpolator;->decelerate_cubic:I
Lcom/android/internal/R$layout;->notification_template_material_base:I
Lcom/android/internal/R$layout;->preference_header_item:I
Lcom/android/internal/R$layout;->screen_title:I
Lcom/android/internal/R$layout;->select_dialog:I
Lcom/android/internal/R$layout;->select_dialog_multichoice:I
Lcom/android/internal/R$layout;->select_dialog_singlechoice:I
Lcom/android/internal/R$layout;->webview_find:I
Lcom/android/internal/R$layout;->zoom_magnify:I
Lcom/android/internal/R$plurals;->matches_found:I
Lcom/android/internal/R$raw;->loaderror:I
Lcom/android/internal/R$raw;->nodomain:I
Lcom/android/internal/R$string;->byteShort:I
Lcom/android/internal/R$string;->cancel:I
Lcom/android/internal/R$string;->enable_explore_by_touch_warning_title:I
Lcom/android/internal/R$string;->gigabyteShort:I
Lcom/android/internal/R$string;->kilobyteShort:I
Lcom/android/internal/R$string;->map:I
Lcom/android/internal/R$string;->megabyteShort:I
Lcom/android/internal/R$string;->no_matches:I
Lcom/android/internal/R$string;->notification_title:I
Lcom/android/internal/R$string;->ok:I
Lcom/android/internal/R$string;->petabyteShort:I
Lcom/android/internal/R$string;->redo:I
Lcom/android/internal/R$string;->share:I
Lcom/android/internal/R$string;->terabyteShort:I
Lcom/android/internal/R$string;->whichApplication:I
Lcom/android/internal/R$style;->Animation_DropDownDown:I
Lcom/android/internal/R$style;->Animation_DropDownUp:I
Lcom/android/internal/R$style;->Animation_PopupWindow:I
Lcom/android/internal/R$style;->Theme:I
Lcom/android/internal/R$style;->Theme_Dialog_Alert:I
Lcom/android/internal/R$style;->Theme_Holo_Light:I
Lcom/android/internal/R$style;->Theme_Light:I
Lcom/android/internal/R$styleable;-><init>()V
Lcom/android/internal/R$styleable;->AbsListView:[I
Lcom/android/internal/R$styleable;->AbsListView_cacheColorHint:I
Lcom/android/internal/R$styleable;->AbsListView_choiceMode:I
Lcom/android/internal/R$styleable;->AbsListView_drawSelectorOnTop:I
Lcom/android/internal/R$styleable;->AbsListView_fastScrollAlwaysVisible:I
Lcom/android/internal/R$styleable;->AbsListView_fastScrollEnabled:I
Lcom/android/internal/R$styleable;->AbsListView_listSelector:I
Lcom/android/internal/R$styleable;->AbsListView_scrollingCache:I
Lcom/android/internal/R$styleable;->AbsListView_smoothScrollbar:I
Lcom/android/internal/R$styleable;->AbsListView_stackFromBottom:I
Lcom/android/internal/R$styleable;->AbsListView_textFilterEnabled:I
Lcom/android/internal/R$styleable;->AbsListView_transcriptMode:I
Lcom/android/internal/R$styleable;->AbsSpinner:[I
Lcom/android/internal/R$styleable;->AccountAuthenticator:[I
Lcom/android/internal/R$styleable;->AccountAuthenticator_accountPreferences:I
Lcom/android/internal/R$styleable;->AccountAuthenticator_accountType:I
Lcom/android/internal/R$styleable;->AccountAuthenticator_customTokens:I
Lcom/android/internal/R$styleable;->AccountAuthenticator_icon:I
Lcom/android/internal/R$styleable;->AccountAuthenticator_label:I
Lcom/android/internal/R$styleable;->AccountAuthenticator_smallIcon:I
Lcom/android/internal/R$styleable;->ActionMode:[I
Lcom/android/internal/R$styleable;->AdapterViewAnimator:[I
Lcom/android/internal/R$styleable;->AdapterViewFlipper:[I
Lcom/android/internal/R$styleable;->AlertDialog:[I
Lcom/android/internal/R$styleable;->AnalogClock:[I
Lcom/android/internal/R$styleable;->AndroidManifest:[I
Lcom/android/internal/R$styleable;->AndroidManifestActivity:[I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_allowTaskReparenting:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_configChanges:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_description:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_enabled:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_excludeFromRecents:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_exported:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_hardwareAccelerated:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_icon:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_immersive:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_label:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_launchMode:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_logo:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_name:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_noHistory:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_permission:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_process:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_screenOrientation:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_taskAffinity:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_theme:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_uiOptions:I
Lcom/android/internal/R$styleable;->AndroidManifestActivity_windowSoftInputMode:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication:[I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_enabled:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_hardwareAccelerated:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_label:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_largeHeap:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_name:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_permission:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_process:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_supportsRtl:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_theme:I
Lcom/android/internal/R$styleable;->AndroidManifestApplication_uiOptions:I
Lcom/android/internal/R$styleable;->AndroidManifestData:[I
Lcom/android/internal/R$styleable;->AndroidManifestIntentFilter:[I
Lcom/android/internal/R$styleable;->AndroidManifestIntentFilter_priority:I
Lcom/android/internal/R$styleable;->AndroidManifestMetaData:[I
Lcom/android/internal/R$styleable;->AndroidManifestMetaData_name:I
Lcom/android/internal/R$styleable;->AndroidManifestMetaData_resource:I
Lcom/android/internal/R$styleable;->AndroidManifestMetaData_value:I
Lcom/android/internal/R$styleable;->AndroidManifestPackageVerifier:[I
Lcom/android/internal/R$styleable;->AndroidManifestProvider:[I
Lcom/android/internal/R$styleable;->AndroidManifestService:[I
Lcom/android/internal/R$styleable;->AndroidManifestService_enabled:I
Lcom/android/internal/R$styleable;->AndroidManifestService_exported:I
Lcom/android/internal/R$styleable;->AndroidManifestService_name:I
Lcom/android/internal/R$styleable;->AndroidManifestService_permission:I
Lcom/android/internal/R$styleable;->AndroidManifestService_process:I
Lcom/android/internal/R$styleable;->AndroidManifestUsesLibrary:[I
Lcom/android/internal/R$styleable;->AndroidManifestUsesPermission:[I
Lcom/android/internal/R$styleable;->AndroidManifestUsesPermission_name:I
Lcom/android/internal/R$styleable;->AndroidManifestUsesSdk:[I
Lcom/android/internal/R$styleable;->AndroidManifestUsesSdk_minSdkVersion:I
Lcom/android/internal/R$styleable;->AndroidManifestUsesSdk_targetSdkVersion:I
Lcom/android/internal/R$styleable;->AndroidManifest_installLocation:I
Lcom/android/internal/R$styleable;->AndroidManifest_sharedUserId:I
Lcom/android/internal/R$styleable;->AndroidManifest_versionCode:I
Lcom/android/internal/R$styleable;->AndroidManifest_versionName:I
Lcom/android/internal/R$styleable;->AutoCompleteTextView:[I
Lcom/android/internal/R$styleable;->CheckBoxPreference:[I
Lcom/android/internal/R$styleable;->CheckBoxPreference_disableDependentsState:I
Lcom/android/internal/R$styleable;->CheckBoxPreference_summaryOff:I
Lcom/android/internal/R$styleable;->CheckBoxPreference_summaryOn:I
Lcom/android/internal/R$styleable;->CheckedTextView:[I
Lcom/android/internal/R$styleable;->CheckedTextView_checkMark:I
Lcom/android/internal/R$styleable;->CheckedTextView_checked:I
Lcom/android/internal/R$styleable;->CompoundButton:[I
Lcom/android/internal/R$styleable;->CompoundButton_button:I
Lcom/android/internal/R$styleable;->CompoundButton_checked:I
Lcom/android/internal/R$styleable;->ContactsDataKind:[I
Lcom/android/internal/R$styleable;->DatePicker:[I
Lcom/android/internal/R$styleable;->DialogPreference:[I
Lcom/android/internal/R$styleable;->DialogPreference_dialogTitle:I
Lcom/android/internal/R$styleable;->Dream:[I
Lcom/android/internal/R$styleable;->EdgeEffect:[I
Lcom/android/internal/R$styleable;->EdgeEffect_colorEdgeEffect:I
Lcom/android/internal/R$styleable;->FastScroll:[I
Lcom/android/internal/R$styleable;->FrameLayout:[I
Lcom/android/internal/R$styleable;->FrameLayout_Layout:[I
Lcom/android/internal/R$styleable;->Gallery:[I
Lcom/android/internal/R$styleable;->GridView:[I
Lcom/android/internal/R$styleable;->IconMenuView:[I
Lcom/android/internal/R$styleable;->ImageView:[I
Lcom/android/internal/R$styleable;->ImageView_scaleType:I
Lcom/android/internal/R$styleable;->ImageView_src:I
Lcom/android/internal/R$styleable;->Keyboard:[I
Lcom/android/internal/R$styleable;->KeyboardView:[I
Lcom/android/internal/R$styleable;->Keyboard_Key:[I
Lcom/android/internal/R$styleable;->Keyboard_Row:[I
Lcom/android/internal/R$styleable;->ListPreference:[I
Lcom/android/internal/R$styleable;->ListPreference_entries:I
Lcom/android/internal/R$styleable;->ListView:[I
Lcom/android/internal/R$styleable;->ListView_divider:I
Lcom/android/internal/R$styleable;->ListView_dividerHeight:I
Lcom/android/internal/R$styleable;->ListView_entries:I
Lcom/android/internal/R$styleable;->ListView_footerDividersEnabled:I
Lcom/android/internal/R$styleable;->ListView_headerDividersEnabled:I
Lcom/android/internal/R$styleable;->ListView_overScrollFooter:I
Lcom/android/internal/R$styleable;->ListView_overScrollHeader:I
Lcom/android/internal/R$styleable;->MapView:[I
Lcom/android/internal/R$styleable;->MapView_apiKey:I
Lcom/android/internal/R$styleable;->MenuGroup:[I
Lcom/android/internal/R$styleable;->MenuItem:[I
Lcom/android/internal/R$styleable;->NumberPicker:[I
Lcom/android/internal/R$styleable;->PopupWindow:[I
Lcom/android/internal/R$styleable;->PopupWindow_popupAnimationStyle:I
Lcom/android/internal/R$styleable;->PopupWindow_popupBackground:I
Lcom/android/internal/R$styleable;->Preference:[I
Lcom/android/internal/R$styleable;->PreferenceGroup:[I
Lcom/android/internal/R$styleable;->PreferenceGroup_orderingFromXml:I
Lcom/android/internal/R$styleable;->Preference_defaultValue:I
Lcom/android/internal/R$styleable;->Preference_dependency:I
Lcom/android/internal/R$styleable;->Preference_enabled:I
Lcom/android/internal/R$styleable;->Preference_fragment:I
Lcom/android/internal/R$styleable;->Preference_icon:I
Lcom/android/internal/R$styleable;->Preference_key:I
Lcom/android/internal/R$styleable;->Preference_layout:I
Lcom/android/internal/R$styleable;->Preference_order:I
Lcom/android/internal/R$styleable;->Preference_persistent:I
Lcom/android/internal/R$styleable;->Preference_selectable:I
Lcom/android/internal/R$styleable;->Preference_shouldDisableView:I
Lcom/android/internal/R$styleable;->Preference_summary:I
Lcom/android/internal/R$styleable;->Preference_title:I
Lcom/android/internal/R$styleable;->Preference_widgetLayout:I
Lcom/android/internal/R$styleable;->ProgressBar:[I
Lcom/android/internal/R$styleable;->QuickContactBadge:[I
Lcom/android/internal/R$styleable;->RingtonePreference:[I
Lcom/android/internal/R$styleable;->ScrollView:[I
Lcom/android/internal/R$styleable;->ScrollView_fillViewport:I
Lcom/android/internal/R$styleable;->SelectionModeDrawables:[I
Lcom/android/internal/R$styleable;->Switch:[I
Lcom/android/internal/R$styleable;->SwitchPreference:[I
Lcom/android/internal/R$styleable;->SyncAdapter:[I
Lcom/android/internal/R$styleable;->SyncAdapter_accountType:I
Lcom/android/internal/R$styleable;->SyncAdapter_allowParallelSyncs:I
Lcom/android/internal/R$styleable;->SyncAdapter_contentAuthority:I
Lcom/android/internal/R$styleable;->SyncAdapter_isAlwaysSyncable:I
Lcom/android/internal/R$styleable;->SyncAdapter_settingsActivity:I
Lcom/android/internal/R$styleable;->SyncAdapter_supportsUploading:I
Lcom/android/internal/R$styleable;->SyncAdapter_userVisible:I
Lcom/android/internal/R$styleable;->TabWidget:[I
Lcom/android/internal/R$styleable;->TextAppearance:[I
Lcom/android/internal/R$styleable;->TextAppearance_fontFamily:I
Lcom/android/internal/R$styleable;->TextAppearance_textAllCaps:I
Lcom/android/internal/R$styleable;->TextAppearance_textColor:I
Lcom/android/internal/R$styleable;->TextAppearance_textColorHighlight:I
Lcom/android/internal/R$styleable;->TextAppearance_textColorHint:I
Lcom/android/internal/R$styleable;->TextAppearance_textColorLink:I
Lcom/android/internal/R$styleable;->TextAppearance_textSize:I
Lcom/android/internal/R$styleable;->TextAppearance_textStyle:I
Lcom/android/internal/R$styleable;->TextAppearance_typeface:I
Lcom/android/internal/R$styleable;->TextClock:[I
Lcom/android/internal/R$styleable;->TextView:[I
Lcom/android/internal/R$styleable;->TextViewAppearance:[I
Lcom/android/internal/R$styleable;->TextViewAppearance_textAppearance:I
Lcom/android/internal/R$styleable;->TextView_autoLink:I
Lcom/android/internal/R$styleable;->TextView_autoText:I
Lcom/android/internal/R$styleable;->TextView_bufferType:I
Lcom/android/internal/R$styleable;->TextView_capitalize:I
Lcom/android/internal/R$styleable;->TextView_cursorVisible:I
Lcom/android/internal/R$styleable;->TextView_digits:I
Lcom/android/internal/R$styleable;->TextView_drawableBottom:I
Lcom/android/internal/R$styleable;->TextView_drawableEnd:I
Lcom/android/internal/R$styleable;->TextView_drawableLeft:I
Lcom/android/internal/R$styleable;->TextView_drawablePadding:I
Lcom/android/internal/R$styleable;->TextView_drawableRight:I
Lcom/android/internal/R$styleable;->TextView_drawableStart:I
Lcom/android/internal/R$styleable;->TextView_drawableTop:I
Lcom/android/internal/R$styleable;->TextView_editable:I
Lcom/android/internal/R$styleable;->TextView_editorExtras:I
Lcom/android/internal/R$styleable;->TextView_ellipsize:I
Lcom/android/internal/R$styleable;->TextView_ems:I
Lcom/android/internal/R$styleable;->TextView_enabled:I
Lcom/android/internal/R$styleable;->TextView_freezesText:I
Lcom/android/internal/R$styleable;->TextView_gravity:I
Lcom/android/internal/R$styleable;->TextView_height:I
Lcom/android/internal/R$styleable;->TextView_hint:I
Lcom/android/internal/R$styleable;->TextView_imeActionId:I
Lcom/android/internal/R$styleable;->TextView_imeActionLabel:I
Lcom/android/internal/R$styleable;->TextView_imeOptions:I
Lcom/android/internal/R$styleable;->TextView_includeFontPadding:I
Lcom/android/internal/R$styleable;->TextView_inputMethod:I
Lcom/android/internal/R$styleable;->TextView_inputType:I
Lcom/android/internal/R$styleable;->TextView_lineSpacingExtra:I
Lcom/android/internal/R$styleable;->TextView_lineSpacingMultiplier:I
Lcom/android/internal/R$styleable;->TextView_lines:I
Lcom/android/internal/R$styleable;->TextView_linksClickable:I
Lcom/android/internal/R$styleable;->TextView_marqueeRepeatLimit:I
Lcom/android/internal/R$styleable;->TextView_maxEms:I
Lcom/android/internal/R$styleable;->TextView_maxHeight:I
Lcom/android/internal/R$styleable;->TextView_maxLength:I
Lcom/android/internal/R$styleable;->TextView_maxLines:I
Lcom/android/internal/R$styleable;->TextView_maxWidth:I
Lcom/android/internal/R$styleable;->TextView_minEms:I
Lcom/android/internal/R$styleable;->TextView_minHeight:I
Lcom/android/internal/R$styleable;->TextView_minLines:I
Lcom/android/internal/R$styleable;->TextView_minWidth:I
Lcom/android/internal/R$styleable;->TextView_numeric:I
Lcom/android/internal/R$styleable;->TextView_password:I
Lcom/android/internal/R$styleable;->TextView_phoneNumber:I
Lcom/android/internal/R$styleable;->TextView_privateImeOptions:I
Lcom/android/internal/R$styleable;->TextView_scrollHorizontally:I
Lcom/android/internal/R$styleable;->TextView_selectAllOnFocus:I
Lcom/android/internal/R$styleable;->TextView_shadowColor:I
Lcom/android/internal/R$styleable;->TextView_shadowDx:I
Lcom/android/internal/R$styleable;->TextView_shadowDy:I
Lcom/android/internal/R$styleable;->TextView_shadowRadius:I
Lcom/android/internal/R$styleable;->TextView_singleLine:I
Lcom/android/internal/R$styleable;->TextView_text:I
Lcom/android/internal/R$styleable;->TextView_textAllCaps:I
Lcom/android/internal/R$styleable;->TextView_textAppearance:I
Lcom/android/internal/R$styleable;->TextView_textColor:I
Lcom/android/internal/R$styleable;->TextView_textColorHighlight:I
Lcom/android/internal/R$styleable;->TextView_textColorHint:I
Lcom/android/internal/R$styleable;->TextView_textColorLink:I
Lcom/android/internal/R$styleable;->TextView_textCursorDrawable:I
Lcom/android/internal/R$styleable;->TextView_textEditSuggestionItemLayout:I
Lcom/android/internal/R$styleable;->TextView_textIsSelectable:I
Lcom/android/internal/R$styleable;->TextView_textScaleX:I
Lcom/android/internal/R$styleable;->TextView_textSelectHandle:I
Lcom/android/internal/R$styleable;->TextView_textSelectHandleLeft:I
Lcom/android/internal/R$styleable;->TextView_textSelectHandleRight:I
Lcom/android/internal/R$styleable;->TextView_textSize:I
Lcom/android/internal/R$styleable;->TextView_textStyle:I
Lcom/android/internal/R$styleable;->TextView_typeface:I
Lcom/android/internal/R$styleable;->TextView_width:I
Lcom/android/internal/R$styleable;->Theme:[I
Lcom/android/internal/R$styleable;->TwoLineListItem:[I
Lcom/android/internal/R$styleable;->View:[I
Lcom/android/internal/R$styleable;->ViewAnimator:[I
Lcom/android/internal/R$styleable;->ViewFlipper:[I
Lcom/android/internal/R$styleable;->ViewGroup_Layout:[I
Lcom/android/internal/R$styleable;->ViewGroup_Layout_layout_height:I
Lcom/android/internal/R$styleable;->ViewGroup_Layout_layout_width:I
Lcom/android/internal/R$styleable;->ViewStub:[I
Lcom/android/internal/R$styleable;->ViewStub_inflatedId:I
Lcom/android/internal/R$styleable;->ViewStub_layout:I
Lcom/android/internal/R$styleable;->View_background:I
Lcom/android/internal/R$styleable;->View_clickable:I
Lcom/android/internal/R$styleable;->View_focusable:I
Lcom/android/internal/R$styleable;->View_id:I
Lcom/android/internal/R$styleable;->View_longClickable:I
Lcom/android/internal/R$styleable;->WallpaperPreviewInfo:[I
Lcom/android/internal/R$styleable;->Window:[I
Lcom/android/internal/R$styleable;->Window_windowActionBarFullscreenDecorLayout:I
Lcom/android/internal/R$styleable;->Window_windowBackground:I
Lcom/android/internal/R$styleable;->Window_windowFullscreen:I
Lcom/android/internal/R$styleable;->Window_windowIsFloating:I
Lcom/android/internal/R$styleable;->Window_windowIsTranslucent:I
Lcom/android/internal/R$styleable;->Window_windowShowWallpaper:I
Lcom/android/internal/R$xml;->power_profile:I
```

### non-SDK interfaces that were added to the SDK in Android 11

The following code box lists all of the non-SDK interfaces that were unsupported
(greylisted) in Android 10 (API level 29) that were added to the Android SDK in
Android 11 (API level 30). Each interface takes up one line.

```
Landroid/provider/Settings$Global;->WIFI_P2P_PENDING_FACTORY_RESET:Ljava/lang/String;
Landroid/provider/MediaStore$Downloads;->getContentUri(Ljava/lang/String;J)Landroid/net/Uri;
Landroid/media/CamcorderProfile;->QUALITY_QHD:I
Landroid/provider/MediaStore$Audio$Media;->getContentUri(Ljava/lang/String;J)Landroid/net/Uri;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;->values()[Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/telephony/NetworkRegistrationInfo;->NR_STATE_RESTRICTED:I
Landroid/telephony/NetworkRegistrationInfo;->NR_STATE_NOT_RESTRICTED:I
Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;->EQUAL_AFTER_ROUNDING:Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/app/Notification;->getContextualActions()Ljava/util/List;
Landroid/icu/number/NumberRangeFormatterSettings;->numberFormatterBoth(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;
Landroid/app/AppOpsManager;->OPSTR_READ_MEDIA_AUDIO:Ljava/lang/String;
Landroid/net/wifi/ScanResult;->KEY_MGMT_EAP_SUITE_B_192:I
Landroid/telephony/ServiceState;->getOperatorAlphaLongRaw()Ljava/lang/String;
Landroid/Manifest$permission;->WIFI_UPDATE_USABILITY_STATS_SCORE:Ljava/lang/String;
Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;->onAbort()V
Landroid/telephony/NetworkRegistrationInfo;->NR_STATE_CONNECTED:I
Landroid/telephony/CarrierConfigManager;->KEY_SUPPORT_TDSCDMA_ROAMING_NETWORKS_STRING_ARRAY:Ljava/lang/String;
Landroid/media/CamcorderProfile;->QUALITY_4KDCI:I
Landroid/content/ContentProvider;->getCallingPackageUnchecked()Ljava/lang/String;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->APPROXIMATELY:Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Landroid/telephony/CarrierConfigManager;->KEY_CARRIER_APP_REQUIRED_DURING_SIM_SETUP_BOOL:Ljava/lang/String;
Landroid/media/audiopolicy/AudioProductStrategy;->supportsAudioAttributes(Landroid/media/AudioAttributes;)Z
Landroid/telephony/NetworkRegistrationInfo;->getNrState()I
Landroid/icu/number/NumberRangeFormatterSettings;->numberFormatterSecond(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;
Landroid/view/WindowInsetsController;->hide(I)V
Landroid/view/InsetsAnimationControlImpl;->getShownStateInsets()Landroid/graphics/Insets;
Landroid/media/CamcorderProfile;->QUALITY_TIME_LAPSE_QHD:I
Landroid/telephony/CarrierConfigManager;->KEY_USE_WFC_HOME_NETWORK_MODE_IN_ROAMING_NETWORK_BOOL:Ljava/lang/String;
Landroid/net/wifi/WifiManager;->getFactoryMacAddresses()[Ljava/lang/String;
Landroid/media/CamcorderProfile;->QUALITY_HIGH_SPEED_4KDCI:I
Landroid/telephony/TelephonyManager;->setDataAllowedDuringVoiceCall(Z)Z
Landroid/net/NetworkSpecifier;->redact()Landroid/net/NetworkSpecifier;
Landroid/icu/util/JapaneseCalendar;->REIWA:I
Landroid/provider/MediaStore$Video$VideoColumns;->COLOR_STANDARD:Ljava/lang/String;
Landroid/telephony/CarrierConfigManager;->KEY_SHOW_4G_FOR_LTE_DATA_ICON_BOOL:Ljava/lang/String;
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE_NONE:I
Landroid/icu/number/NumberRangeFormatter;->with()Landroid/icu/number/UnlocalizedNumberRangeFormatter;
Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;->onUserSelectionConnectSuccess(Landroid/net/wifi/WifiConfiguration;)V
Landroid/view/View;->getWindowInsetsController()Landroid/view/WindowInsetsController;
Landroid/net/SocketKeepalive;->SUCCESS:I
Landroid/media/ExifInterface;->TAG_OFFSET_TIME_ORIGINAL:Ljava/lang/String;
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->UNIT:Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/database/sqlite/SQLiteQueryBuilder;->insert(Landroid/database/sqlite/SQLiteDatabase;Landroid/content/ContentValues;)J
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE_VOICE:I
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->ALL:Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/view/WindowInsets$Type;->systemBars()I
Landroid/icu/number/NumberRangeFormatter;->withLocale(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;
Landroid/telephony/CarrierConfigManager;->KEY_LTE_ENABLED_BOOL:Ljava/lang/String;
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE_ALL:I
Landroid/telephony/TelephonyManager;->isDataAllowedInVoiceCall()Z
Landroid/net/NattKeepalivePacketData;-><init>(Ljava/net/InetAddress;ILjava/net/InetAddress;I[B)V
Landroid/media/CamcorderProfile;->QUALITY_TIME_LAPSE_VGA:I
Landroid/telephony/TelephonyManager;->isOpportunisticNetworkEnabled()Z
Landroid/telephony/CellSignalStrengthWcdma;->getEcNo()I
Landroid/net/MacAddress;->matches(Landroid/net/MacAddress;Landroid/net/MacAddress;)Z
Landroid/database/sqlite/SQLiteQueryBuilder;->isStrictGrammar()Z
Landroid/net/LinkProperties;->addPcscfServer(Ljava/net/InetAddress;)Z
Landroid/view/WindowInsetsAnimationController;->getCurrentInsets()Landroid/graphics/Insets;
Landroid/provider/Telephony$Carriers;->SKIP_464XLAT_DISABLE:I
Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;->valueOf(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE_SMS:I
Landroid/net/wifi/ScanResult;->KEY_MGMT_OWE:I
Landroid/net/wifi/ScanResult;->CIPHER_GCMP_256:I
Landroid/provider/MediaStore$Video$VideoColumns;->COLOR_RANGE:Ljava/lang/String;
Landroid/net/wifi/WifiManager$NetworkRequestUserSelectionCallbackProxy;->select(Landroid/net/wifi/WifiConfiguration;)V
Landroid/icu/number/NumberRangeFormatterSettings;->numberFormatterFirst(Landroid/icu/number/UnlocalizedNumberFormatter;)Landroid/icu/number/NumberRangeFormatterSettings;
Landroid/telephony/TelephonyManager;->EXTRA_SIM_COMBINATION_WARNING_TYPE_DUAL_CDMA:I
Landroid/view/WindowInsetsAnimationControlListener;->onReady(Landroid/view/WindowInsetsAnimationController;I)V
Landroid/view/WindowInsets;->isVisible(I)Z
Landroid/telephony/CarrierConfigManager;->KEY_SHOW_BLOCKING_PAY_PHONE_OPTION_BOOL:Ljava/lang/String;
Landroid/telephony/euicc/EuiccManager;->EXTRA_PHYSICAL_SLOT_ID:Ljava/lang/String;
Landroid/net/wifi/WifiConfiguration;->fromWifiNetworkSpecifier:Z
Landroid/net/wifi/ScanResult;->KEY_MGMT_SAE:I
Landroid/net/wifi/WifiManager$NetworkRequestUserSelectionCallback;->reject()V
Landroid/telephony/ims/ImsMmTelManager;->isTtyOverVolteEnabled()Z
Landroid/icu/number/UnlocalizedNumberRangeFormatter;->locale(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;
Landroid/telecom/Conference;->setConferenceState(Z)V
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_SAE:I
Landroid/view/accessibility/AccessibilityWindowInfo;-><init>(Landroid/view/accessibility/AccessibilityWindowInfo;)V
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_WEP:I
Landroid/net/wifi/WifiConfiguration;->macRandomizationSetting:I
Landroid/telephony/TelephonyManager;->setOpportunisticNetworkState(Z)Z
Landroid/icu/util/MeasureUnit;->PETABYTE:Landroid/icu/util/MeasureUnit;
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->values()[Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/view/WindowInsets$Type;->ime()I
Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;->EQUAL_BEFORE_ROUNDING:Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/telephony/TelephonyManager;->isInEmergencySmsMode()Z
Landroid/icu/number/FormattedNumberRange;->getIdentityResult()Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/media/CamcorderProfile;->QUALITY_HIGH_SPEED_CIF:I
Landroid/app/role/RoleManager;->getDefaultSmsPackage(I)Ljava/lang/String;
Landroid/telecom/PhoneAccount;->CAPABILITY_EMERGENCY_PREFERRED:I
Landroid/database/sqlite/SQLiteQueryBuilder;->isStrictColumns()Z
Landroid/telecom/Connection;->PROPERTY_REMOTELY_HOSTED:I
Landroid/net/wifi/WifiConfiguration;->setSecurityParams(I)V
Landroid/view/WindowInsetsAnimationController;->getHiddenStateInsets()Landroid/graphics/Insets;
Landroid/net/wifi/WifiNetworkSpecifier;->assertValidFromUid(I)V
Landroid/icu/number/LocalizedNumberRangeFormatter;->formatRange(II)Landroid/icu/number/FormattedNumberRange;
Landroid/media/ExifInterface;->TAG_OFFSET_TIME:Ljava/lang/String;
Landroid/media/CamcorderProfile;->QUALITY_TIME_LAPSE_2K:I
Landroid/app/AppOpsManager;->OPSTR_WRITE_MEDIA_IMAGES:Ljava/lang/String;
Landroid/view/WindowInsets$Builder;->setVisible(IZ)Landroid/view/WindowInsets$Builder;
Landroid/media/tv/TvInputManager;->VIDEO_UNAVAILABLE_REASON_NOT_CONNECTED:I
Landroid/net/wifi/WifiConfiguration$NetworkSelectionStatus;->DISABLED_AUTHENTICATION_NO_SUBSCRIPTION:I
Landroid/icu/number/LocalizedNumberRangeFormatter;->formatRange(Ljava/lang/Number;Ljava/lang/Number;)Landroid/icu/number/FormattedNumberRange;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->RANGE:Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Landroid/icu/number/UnlocalizedNumberRangeFormatter;->locale(Landroid/icu/util/ULocale;)Landroid/icu/number/LocalizedNumberRangeFormatter;
Landroid/view/WindowInsetsAnimationController;->getShownStateInsets()Landroid/graphics/Insets;
Landroid/net/NetworkCapabilities;->setTransportInfo(Landroid/net/TransportInfo;)Landroid/net/NetworkCapabilities;
Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;->onUserSelectionCallbackRegistration(Landroid/net/wifi/WifiManager$NetworkRequestUserSelectionCallback;)V
Landroid/view/WindowInsetsController;->show(I)V
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_PSK:I
Landroid/net/wifi/WifiConfiguration;->RANDOMIZATION_PERSISTENT:I
Landroid/view/WindowInsets;->getInsets(I)Landroid/graphics/Insets;
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_OPEN:I
Landroid/telephony/TelephonyManager;->EXTRA_SIM_COMBINATION_WARNING_TYPE_NONE:I
Landroid/telecom/Conference;->setCallerDisplayName(Ljava/lang/String;I)V
Landroid/telephony/CellIdentityTdscdma;->sanitizeLocationInfo()Landroid/telephony/CellIdentityTdscdma;
Landroid/net/LinkProperties;->hasIpv6DnsServer()Z
Landroid/net/wifi/WifiManager$NetworkRequestUserSelectionCallback;->select(Landroid/net/wifi/WifiConfiguration;)V
Landroid/telephony/ServiceState;->getOperatorAlphaShortRaw()Ljava/lang/String;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->SINGLE_VALUE:Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Lcom/android/internal/policy/PhoneWindow;->getInsetsController()Landroid/view/WindowInsetsController;
Landroid/telephony/CarrierConfigManager;->KEY_SUPPORT_IMS_CONFERENCE_EVENT_PACKAGE_BOOL:Ljava/lang/String;
Landroid/provider/MediaStore$Video$VideoColumns;->COLOR_TRANSFER:Ljava/lang/String;
Landroid/view/accessibility/AccessibilityNodeInfo;-><init>(Landroid/view/accessibility/AccessibilityNodeInfo;)V
Landroid/telephony/DataSpecificRegistrationInfo;->isUsingCarrierAggregation()Z
Landroid/app/AppOpsManager;->OPSTR_READ_MEDIA_IMAGES:Ljava/lang/String;
Landroid/telephony/CarrierConfigManager;->KEY_HIDE_LTE_PLUS_DATA_ICON_BOOL:Ljava/lang/String;
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_EAP_SUITE_B:I
Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;->onMatch(Ljava/util/List;)V
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->valueOf(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/telephony/CellIdentityGsm;->sanitizeLocationInfo()Landroid/telephony/CellIdentityGsm;
Landroid/telephony/TelephonyManager;->isDataEnabledForApn(I)Z
Landroid/telephony/CarrierConfigManager;->KEY_SUPPORT_TDSCDMA_BOOL:Ljava/lang/String;
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_EAP:I
Landroid/net/wifi/ScanResult;->KEY_MGMT_OWE_TRANSITION:I
Landroid/provider/MediaStore$Images$Media;->getContentUri(Ljava/lang/String;J)Landroid/net/Uri;
Landroid/telephony/TelephonyManager;->EXTRA_SIM_COMBINATION_NAMES:Ljava/lang/String;
Landroid/icu/number/FormattedNumberRange;->getSecondBigDecimal()Ljava/math/BigDecimal;
Landroid/database/sqlite/SQLiteQueryBuilder;->setStrictColumns(Z)V
Landroid/database/sqlite/SQLiteQueryBuilder;->setStrictGrammar(Z)V
Landroid/content/ContentProvider;->onCallingPackageChanged()V
Landroid/icu/util/MeasureUnit;->PERCENT:Landroid/icu/util/MeasureUnit;
Landroid/net/wifi/aware/WifiAwareAgentNetworkSpecifier;->redact()Landroid/net/NetworkSpecifier;
Landroid/telephony/CellIdentityWcdma;->sanitizeLocationInfo()Landroid/telephony/CellIdentityWcdma;
Landroid/view/InsetsController;->hide(I)V
Landroid/telephony/TelephonyManager;->isModemEnabledForSlot(I)Z
Landroid/telephony/CarrierConfigManager$Gps;->KEY_PERSIST_LPP_MODE_BOOL:Ljava/lang/String;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;->NOT_EQUAL:Landroid/icu/number/NumberRangeFormatter$RangeIdentityResult;
Landroid/view/Window;->getInsetsController()Landroid/view/WindowInsetsController;
Landroid/telecom/Conference;->setAddress(Landroid/net/Uri;I)V
Landroid/media/CamcorderProfile;->QUALITY_HIGH_SPEED_VGA:I
Landroid/net/MacAddress;->getLinkLocalIpv6FromEui48Mac()Ljava/net/Inet6Address;
Landroid/media/CamcorderProfile;->QUALITY_2K:I
Landroid/app/AppOpsManager;->OPSTR_WRITE_MEDIA_VIDEO:Ljava/lang/String;
Landroid/telephony/CarrierConfigManager;->KEY_SHOW_CARRIER_DATA_ICON_PATTERN_STRING:Ljava/lang/String;
Landroid/telephony/CarrierConfigManager;->KEY_SHOW_WFC_LOCATION_PRIVACY_POLICY_BOOL:Ljava/lang/String;
Landroid/view/InsetsController;->show(I)V
Landroid/view/InsetsAnimationControlImpl;->getTypes()I
Landroid/net/wifi/WifiNetworkAgentSpecifier;->redact()Landroid/net/NetworkSpecifier;
Landroid/telephony/SubscriptionInfo;->isGroupDisabled()Z
Landroid/provider/MediaStore$MediaColumns;->IS_TRASHED:Ljava/lang/String;
Landroid/net/wifi/p2p/WifiP2pManager;->factoryReset(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V
Landroid/provider/Telephony$Carriers;->SKIP_464XLAT:Ljava/lang/String;
Landroid/icu/number/FormattedNumberRange;->getFirstBigDecimal()Ljava/math/BigDecimal;
Landroid/content/Context;->NETWORK_STACK_SERVICE:Ljava/lang/String;
Landroid/view/WindowInsets$Type;->mandatorySystemGestures()I
Landroid/icu/number/NumberRangeFormatter;->withLocale(Ljava/util/Locale;)Landroid/icu/number/LocalizedNumberRangeFormatter;
Landroid/app/AppOpsManager;->OPSTR_READ_DEVICE_IDENTIFIERS:Ljava/lang/String;
Landroid/net/wifi/WifiConfiguration;->fromWifiNetworkSuggestion:Z
Landroid/media/MediaMetadataRetriever;->METADATA_KEY_COLOR_RANGE:I
Landroid/net/wifi/WifiConfiguration;->RANDOMIZATION_NONE:I
Landroid/telecom/Connection;->setCallDirection(I)V
Landroid/util/proto/ProtoOutputStream;->getRawSize()I
Landroid/telephony/TelephonyManager;->EXTRA_SIM_COMBINATION_WARNING_TYPE:Ljava/lang/String;
Landroid/telephony/TelephonyManager;->isApnMetered(I)Z
Landroid/media/CamcorderProfile;->QUALITY_TIME_LAPSE_4KDCI:I
Landroid/net/wifi/WifiNetworkSpecifier;->satisfiedBy(Landroid/net/NetworkSpecifier;)Z
Landroid/bluetooth/BluetoothCodecConfig;-><init>(I)V
Landroid/telephony/CellIdentityLte;->sanitizeLocationInfo()Landroid/telephony/CellIdentityLte;
Landroid/icu/number/FormattedNumberRange;->toCharacterIterator()Ljava/text/AttributedCharacterIterator;
Landroid/app/AppOpsManager;->OPSTR_READ_MEDIA_VIDEO:Ljava/lang/String;
Landroid/telephony/CarrierConfigManager$Gps;->KEY_PREFIX:Ljava/lang/String;
Landroid/view/View;->dispatchWindowInsetsAnimationProgress(Landroid/view/WindowInsets;)Landroid/view/WindowInsets;
Landroid/app/AppOpsManager;->OPSTR_WRITE_MEDIA_AUDIO:Ljava/lang/String;
Landroid/net/LinkProperties;->hasIpv4DefaultRoute()Z
Landroid/telecom/TelecomManager;->getSimCallManagerForSubscription(I)Landroid/telecom/PhoneAccountHandle;
Landroid/icu/number/NumberRangeFormatterSettings;->collapse(Landroid/icu/number/NumberRangeFormatter$RangeCollapse;)Landroid/icu/number/NumberRangeFormatterSettings;
Landroid/net/wifi/WifiConfiguration;->SECURITY_TYPE_OWE:I
Landroid/telephony/CarrierConfigManager;->KEY_WORLD_MODE_ENABLED_BOOL:Ljava/lang/String;
Landroid/media/MediaMetadataRetriever;->METADATA_KEY_COLOR_STANDARD:I
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE:Ljava/lang/String;
Landroid/media/MediaMetadataRetriever;->METADATA_KEY_COLOR_TRANSFER:I
Landroid/net/wifi/WifiNetworkAgentSpecifier;->assertValidFromUid(I)V
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->valueOf(Ljava/lang/String;)Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Landroid/icu/util/MeasureUnit;->PERMILLE:Landroid/icu/util/MeasureUnit;
Landroid/icu/number/LocalizedNumberRangeFormatter;->formatRange(DD)Landroid/icu/number/FormattedNumberRange;
Landroid/telecom/DisconnectCause;->REASON_EMULATING_SINGLE_CALL:Ljava/lang/String;
Landroid/app/NotificationManager;->getConsolidatedNotificationPolicy()Landroid/app/NotificationManager$Policy;
Landroid/telecom/Connection;->EVENT_CALL_HOLD_FAILED:Ljava/lang/String;
Landroid/net/wifi/WifiNetworkAgentSpecifier;->satisfiedBy(Landroid/net/NetworkSpecifier;)Z
Landroid/telephony/SmsMessage;->getRecipientAddress()Ljava/lang/String;
Landroid/view/WindowInsets$Type;->systemGestures()I
Landroid/telephony/DataFailCause;->UNACCEPTABLE_NETWORK_PARAMETER:I
Landroid/telephony/NetworkRegistrationInfo;->NR_STATE_NONE:I
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->AUTO:Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/telephony/CellIdentityCdma;->sanitizeLocationInfo()Landroid/telephony/CellIdentityCdma;
Landroid/icu/number/NumberRangeFormatter$RangeCollapse;->NONE:Landroid/icu/number/NumberRangeFormatter$RangeCollapse;
Landroid/telephony/TelephonyManager;->EXTRA_DEFAULT_SUBSCRIPTION_SELECT_TYPE_DATA:I
Landroid/telephony/CellSignalStrengthGsm;->getRssi()I
Landroid/view/WindowInsetsAnimationController;->getTypes()I
Landroid/Manifest$permission;->WIFI_SET_DEVICE_MOBILITY_STATE:Ljava/lang/String;
Landroid/content/res/StringBlock;->close()V
Landroid/telephony/ServiceState;->getNrFrequencyRange()I
Landroid/provider/Telephony$Carriers;->SKIP_464XLAT_DEFAULT:I
Landroid/net/wifi/ScanResult;->KEY_MGMT_FT_SAE:I
Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;->onUserSelectionConnectFailure(Landroid/net/wifi/WifiConfiguration;)V
Landroid/icu/util/MeasureUnit;->ATMOSPHERE:Landroid/icu/util/MeasureUnit;
Landroid/provider/Telephony$Carriers;->SKIP_464XLAT_ENABLE:I
Landroid/view/InsetsAnimationControlImpl;->getHiddenStateInsets()Landroid/graphics/Insets;
Landroid/media/CamcorderProfile;->QUALITY_VGA:I
Landroid/net/NattKeepalivePacketData;->CREATOR:Landroid/os/Parcelable$Creator;
Landroid/telephony/CellIdentityNr;->sanitizeLocationInfo()Landroid/telephony/CellIdentityNr;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->APPROXIMATELY_OR_SINGLE_VALUE:Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Landroid/telephony/CarrierConfigManager;->KEY_5G_ICON_CONFIGURATION_STRING:Ljava/lang/String;
Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;->values()[Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;
Landroid/net/wifi/WifiManager$NetworkRequestUserSelectionCallbackProxy;->reject()V
Landroid/telephony/SubscriptionManager;->setDisplayName(Ljava/lang/String;II)I
Landroid/view/WindowInsetsAnimationControlListener;->onCancelled()V
Landroid/telephony/CarrierConfigManager;->KEY_CARRIER_SETTINGS_ACTIVITY_COMPONENT_NAME_STRING:Ljava/lang/String;
Landroid/net/wifi/WifiManager;->unregisterNetworkRequestMatchCallback(Landroid/net/wifi/WifiManager$NetworkRequestMatchCallback;)V
Landroid/provider/MediaStore$Video$Media;->getContentUri(Ljava/lang/String;J)Landroid/net/Uri;
Landroid/telephony/CarrierConfigManager;->KEY_ALWAYS_SHOW_PRIMARY_SIGNAL_BAR_IN_OPPORTUNISTIC_NETWORK_BOOLEAN:Ljava/lang/String;
Landroid/view/ViewGroup;->dispatchWindowInsetsAnimationProgress(Landroid/view/WindowInsets;)Landroid/view/WindowInsets;
Landroid/net/LinkProperties;->hasIpv4DnsServer()Z
Landroid/media/ExifInterface;->TAG_OFFSET_TIME_DIGITIZED:Ljava/lang/String;
Landroid/telephony/CellIdentityNr;->asCellLocation()Landroid/telephony/CellLocation;
Landroid/net/wifi/ScanResult;->PROTOCOL_RSN:I
Landroid/view/WindowInsets$Builder;->setInsets(ILandroid/graphics/Insets;)Landroid/view/WindowInsets$Builder;
Landroid/telephony/CarrierConfigManager$Wifi;->KEY_PREFIX:Ljava/lang/String;
Landroid/view/InsetsAnimationControlImpl;->getCurrentInsets()Landroid/graphics/Insets;
Landroid/view/WindowInsets$Type;->tappableElement()I
Landroid/icu/number/NumberRangeFormatterSettings;->identityFallback(Landroid/icu/number/NumberRangeFormatter$RangeIdentityFallback;)Landroid/icu/number/NumberRangeFormatterSettings;
```