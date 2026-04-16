---
title: https://developer.android.com/blog/posts/the-embedded-photo-picker
url: https://developer.android.com/blog/posts/the-embedded-photo-picker
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# The Embedded Photo Picker

###### 8-min read

![](https://developer.android.com/static/blog/assets/Android_Photo_Picker_Blogger_60fa0ede59_YTu6Y.webp) 27 Jan 2026 [![](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_GLFQH.webp)](https://developer.android.com/blog/authors/roxanna-walker)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/yacine-rezgui)

##### [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker)
\&
[Yacine Rezgui](https://developer.android.com/blog/authors/yacine-rezgui)

## **The Embedded Photo Picker: A more seamless way to privately request photos and videos in your app**

![photopicker.png](https://developer.android.com/static/blog/assets/photopicker_ce2c4832e2_Z1LaAYt.webp)

Get ready to enhance your app's user experience with an exciting new way to use the Android photo picker! The new embedded photo picker offers a seamless and privacy-focused way for users to select photos and videos, right within your app's interface. Now your app can get all the same benefits available with the photo picker, including access to cloud content, integrated directly into your app's experience.

### **Why embedded?**

We understand that many apps want to provide a highly integrated and seamless experience for users when selecting photos or videos. The embedded photo picker is designed to do just that, allowing users to quickly access their recent photos without ever leaving your app. They can also explore their full library in their preferred cloud media provider (e.g., Google Photos), including favorites, albums and search functionality. This eliminates the need for users to switch between apps or worry about whether the photo they want is stored locally or in the cloud.

### **Seamless integration, enhanced privacy**

With the embedded photo picker, your app doesn't need access to the user's photos or videos until they actually select something. This means greater privacy for your users and a more streamlined experience. Plus, the embedded photo picker provides users with access to their entire cloud-based media library, whereas the standard photo permission is restricted to local files only.

### **The embedded photo picker in Google Messages**

Google Messages showcases the power of the embedded photo picker. Here's how they've integrated it:

- **Intuitive placement:**The photo picker sits right below the camera button, giving users a clear choice between capturing a new photo or selecting an existing one.
- **Dynamic preview:** Immediately after a user taps a photo, they see a large preview, making it easy to confirm their selection. If they deselect the photo, the preview disappears, keeping the experience clean and uncluttered.
- **Expand for more content:**The initial view is simplified, offering easy access to recent photos. However, users can easily expand the photo picker to browse and choose from all photos and videos in their library, including cloud content from Google Photos.
- **Respecting user choices:** The embedded photo picker only grants access to the specific photos or videos the user selects, meaning they can stop requesting the photo and video permissions altogether. This also saves the Messages from needing to handle situations where users only grant limited access to photos and videos.

![gif1.gif](https://developer.android.com/static/blog/assets/gif1_6da309a505_1HrfcC.webp) ![gif2.gif](https://developer.android.com/static/blog/assets/gif2_ea91aa5328_bL0it.webp)

### **Implementation**

Integrating the embedded photo picker is made easy with the [Photo Picker Jetpack library](https://developer.android.com/jetpack/androidx/releases/photopicker).

### **Jetpack Compose**

First, include the Jetpack Photo Picker library as a dependency.

`implementation("androidx.photopicker:photopicker-compose:1.0.0-alpha01")`

The EmbeddedPhotoPicker composable function provides a mechanism to include the embedded photo picker UI directly within your Compose screen. This composable creates a SurfaceView which hosts the embedded photo picker UI. It manages the connection to the EmbeddedPhotoPicker service, handles user interactions, and communicates selected media URIs to the calling application.

```
@Composable
fun EmbeddedPhotoPickerDemo() {
    // We keep track of the list of selected attachments
    var attachments by remember { mutableStateOf(emptyList<Uri>()) }

    val coroutineScope = rememberCoroutineScope()
    // We hide the bottom sheet by default but we show it when the user clicks on the button
    val scaffoldState = rememberBottomSheetScaffoldState(
        bottomSheetState = rememberStandardBottomSheetState(
            initialValue = SheetValue.Hidden,
            skipHiddenState = false
        )
    )

    // Customize the embedded photo picker
    val photoPickerInfo = EmbeddedPhotoPickerFeatureInfo
        .Builder()
        // Set limit the selection to 5 items
        .setMaxSelectionLimit(5)
        // Order the items selection (each item will have an index visible in the photo picker)
        .setOrderedSelection(true)
        // Set the accent color (red in this case, otherwise it follows the device's accent color)
        .setAccentColor(0xFF0000)
        .build()

    // The embedded photo picker state will be stored in this variable
    val photoPickerState = rememberEmbeddedPhotoPickerState(
        onSelectionComplete = {
            coroutineScope.launch {
                // Hide the bottom sheet once the user has clicked on the done button inside the picker
                scaffoldState.bottomSheetState.hide()
            }
        },
        onUriPermissionGranted = {
            // We update our list of attachments with the new Uris granted
            attachments += it
        },
        onUriPermissionRevoked = {
            // We update our list of attachments with the Uris revoked
            attachments -= it
        }
    )

       SideEffect {
        val isExpanded = scaffoldState.bottomSheetState.targetValue == SheetValue.Expanded

        // We show/hide the embedded photo picker to match the bottom sheet state
        photoPickerState.setCurrentExpanded(isExpanded)
    }

    BottomSheetScaffold(
        topBar = {
            TopAppBar(title = { Text("Embedded Photo Picker demo") })
        },
        scaffoldState = scaffoldState,
        sheetPeekHeight = if (scaffoldState.bottomSheetState.isVisible) 400.dp else 0.dp,
        sheetContent = {
            Column(Modifier.fillMaxWidth()) {
                // We render the embedded photo picker inside the bottom sheet
                EmbeddedPhotoPicker(
                    state = photoPickerState,
                    embeddedPhotoPickerFeatureInfo = photoPickerInfo
                )
            }
        }
    ) { innerPadding ->
        Column(Modifier.padding(innerPadding).fillMaxSize().padding(horizontal = 16.dp)) {
            Button(onClick = {
                coroutineScope.launch {
                    // We expand the bottom sheet, which will trigger the embedded picker to be shown
                    scaffoldState.bottomSheetState.partialExpand()
                }
            }) {
                Text("Open photo picker")
            }
            LazyVerticalGrid(columns = GridCells.Adaptive(minSize = 64.dp)) {
                // We render the image using the Coil library
                itemsIndexed(attachments) { index, uri ->
                    AsyncImage(
                        model = uri,
                        contentDescription = "Image ${index + 1}",
                        contentScale = ContentScale.Crop,
                        modifier = Modifier.clickable {
                            coroutineScope.launch {
                                // When the user clicks on the media from the app's UI, we deselect it
                                // from the embedded photo picker by calling the method deselectUri
                                photoPickerState.deselectUri(uri)
                            }
                        }
                    )
                }
            }
        }
    }
}
```

### **Views**

First, include the Jetpack Photo Picker library as a dependency.

`implementation("androidx.photopicker:photopicker:1.0.0-alpha01")`

To add the embedded photo picker, you need to add an entry to your layout file.

```
<view class="androidx.photopicker.EmbeddedPhotoPickerView"
    android:id="@+id/photopicker"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

And initialize it in your activity/fragment.

```
// We keep track of the list of selected attachments
private val _attachments = MutableStateFlow(emptyList<Uri>())
val attachments = _attachments.asStateFlow()

private lateinit var picker: EmbeddedPhotoPickerView
private var openSession: EmbeddedPhotoPickerSession? = null

val pickerListener = object EmbeddedPhotoPickerStateChangeListener {
    override fun onSessionOpened (newSession: EmbeddedPhotoPickerSession) {
        openSession = newSession
    }

    override fun onSessionError (throwable: Throwable) {}

    override fun onUriPermissionGranted(uris: List<Uri>) {
        _attachments += uris
    }

    override fun onUriPermissionRevoked (uris: List<Uri>) {
        _attachments -= uris
    }

    override fun onSelectionComplete() {
        // Hide the embedded photo picker as the user is done with the photo/video selection
    }
}

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.main_view)
    
    //
    // Add the embedded photo picker to a bottom sheet to allow the dragging to display the full photo library
    //

    picker = findViewById(R.id.photopicker)
    picker.addEmbeddedPhotoPickerStateChangeListener(pickerListener)
    picker.setEmbeddedPhotoPickerFeatureInfo(
        // Set a custom accent color
        EmbeddedPhotoPickerFeatureInfo.Builder().setAccentColor(0xFF0000).build()
    )
}
```

You can call different methods of `EmbeddedPhotoPickerSession` to interact with the embedded picker.

```
// Notify the embedded picker of a configuration change
openSession.notifyConfigurationChanged(newConfig)

// Update the embedded picker to expand following a user interaction
openSession.notifyPhotoPickerExpanded(/* expanded: */ true)

// Resize the embedded picker
openSession.notifyResized(/* width: */ 512, /* height: */ 256)

// Show/hide the embedded picker (after a form has been submitted)
openSession.notifyVisibilityChanged(/* visible: */ false)

// Remove unselected media from the embedded picker after they have been
// unselected from the host app's UI
openSession.requestRevokeUriPermission(removedUris)
```

It's important to note that the embedded photo picker experience is available for users running Android 14 (API level 34) or higher with SDK Extensions 15+. [Read more about photo picker device availability](https://developer.android.com/training/data-storage/shared/photo-picker/embedded#device-availability).

For enhanced user privacy and security, the system renders the embedded photo picker in a way that prevents any drawing or overlaying. This intentional design choice means that your UX should consider the photo picker's display area as a distinct and dedicated element, much like you would plan for an advertising banner.  

If you have any feedback or suggestions, submit tickets to our [issue tracker](https://developer.android.com/about/versions/14/feedback#create_vote).

###### Written by:

-

  ## [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/roxanna-walker) ![](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_GLFQH.webp) ![](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_GLFQH.webp)
-

  ## [Yacine Rezgui](https://developer.android.com/blog/authors/yacine-rezgui)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/yacine-rezgui) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_GLFQH.webp)](https://developer.android.com/blog/authors/roxanna-walker) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/contact_Picker_4392c5da87_ZQDO82.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Contact Picker: Privacy-First Contact Sharing](https://developer.android.com/blog/posts/contact-picker-privacy-first-contact-sharing)

  [arrow_forward](https://developer.android.com/blog/posts/contact-picker-privacy-first-contact-sharing) Privacy and user control remain at the heart of the Android experience. Just as the photo picker made media sharing secure and easy to implement, we are now bringing that same level of privacy, simplicity, and great user experience to contact selection.

  ###### [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) 15 Apr 2026 15 Apr 2026 ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boosting user privacy and business protection with updated Play policies](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)

  [arrow_forward](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies) Making Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) 13 Apr 2026 13 Apr 2026 ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Test Multi-Device Interactions with the Android Emulator](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator)

  [arrow_forward](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator) Testing multi-device interactions is now easier than ever with the Android Emulator.

  ###### [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)