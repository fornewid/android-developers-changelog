---
title: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android
url: https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# A more reliable way to add and edit contacts on Android

6 min read ![](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) 21 Oct 2026 [![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)](https://developer.android.com/blog/authors/roxanna-walker) [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) Product Manager, Android

## **What's changing**

Apps that target the upcoming Android release will no longer be able to directly write to contacts with the `WRITE_CONTACTS` permission. Instead, you can use the standard contact intents ([ACTION_INSERT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT), [ACTION_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT), and [ACTION_INSERT_OR_EDIT](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT_OR_EDIT)). For a complete reference implementation, see the developer guide on how to [modify contacts using intents](https://developer.android.com/identity/providers/contacts-provider/modify-data).

On devices running the upcoming Android release, these three contact intents will behave consistently and need no permission at all. If your app targets the upcoming Android release or later and attempts to write to contacts directly, those writes will be rejected and result in a `SecurityException` or permission denial. For the small set of apps which require broad access to create and modify contacts, a new special app access permission, `MANAGE_CONTACTS`, arrives in Android 17 QPR2 (Q4 2026). Google Play is publishing updated guidelines for contact access, including `MANAGE_CONTACTS`, today.

## **Why we're doing this**

Currently, if your app needs to save even one contact, you might be requesting `WRITE_CONTACTS`. But that permission grants broad access, allowing an app to make widespread changes to contacts across the device in the background, even without user interaction. Most apps don't need such broad permission.

While alternatives exist, we've heard from you that they need to be more standardized across the ecosystem. Previously, the contact intents behaved differently from one device to the next. Some editors dropped the data you passed in, like a contact photo. On some devices, the back button saved the contact without the user meaning to or the "create new contact" option was hard to find. So asking for permission was the rational choice. We're fixing all these issues in the upcoming Android version and requiring devices running it to follow the same standards.

## **What to use instead**

#### **Add or edit a contact: use the contact intents**

When you use these intents - `ACTION_INSERT`, `ACTION_EDIT`, and `ACTION_INSERT_OR_EDIT` - the system handles the heavy lifting by presenting a clean, standardized contact editor experience. It opens a quick half-sheet form for new entries, or allows the user to easily search and add information to an existing contact. Users can seamlessly expand this into a full-page editor to fill out more details, all without your app ever needing direct write permissions. View the tentative UX mocks below:
![Figure01_01_Quick_Insert_Half_Sheet_Prefilled.png](https://developer.android.com/static/blog/assets/Figure01_01_Quick_Insert_Half_Sheet_Prefilled_47cedd26cb_Dw4kb.webp) ![Screenshot 2 - Title: Full-Sheet Mock of Create a New Contact: Screenshot of a tentative Android user interface showing a full-screen contact editor with an avatar selector, name, phone, and email fields. The design is labeled as ‘UX not Final’.](https://developer.android.com/static/blog/assets/Figure01_02_Full_Page_Editor_Default_Top_35707ebba8_4OBIj.webp)

*Figure 1: ***Create a New Contact** *\*UX not Final\**
![Figure02_01_Add_To_Existing_0_Search_State_Half_Sheet.png](https://developer.android.com/static/blog/assets/Figure02_01_Add_To_Existing_0_Search_State_Half_Sheet_7543788ec9_Z1HMcPH.webp) ![Screenshot 2 - Title: Full-Sheet Mock of “Add Info to an Existing Contact”: Screenshot of a tentative Android user interface showing a full-screen contact editor with an avatar selector, name, phone, and email fields. The full-page design features progressive disclosure chips for secondary fields. The design is labeled as 'UX not Final'.](https://developer.android.com/static/blog/assets/Figure02_02_Edit_Existing_Contact_Prefilled_Full_Page_7e796e7fb5_ZYSROB.webp)

*Figure 2: ***Add Info to an Existing Contact** *\*UX not Final\**

*** ** * ** ***

**Note:** Different device manufacturers may modify the user experience to match their OS style but the behaviour will remain consistent.

*** ** * ** ***

You can further streamline the creation process by passing optional data payloads, known as Extras, alongside your intent:

- `EXTRA_ACCOUNT` suggests which account the contact saves to, which helps if your app syncs contacts. This extra already existed, but support varied by device. Starting in the upcoming Android release, support is standardized across devices.
- `EXTRA_PHOTO_URI` passes a photo to pre-fill the contact picture. The editor handles the URI read permission for you. This is new with the upcoming Android release and will be supported across the ecosystem.

|---|---|
| **Before: writing directly with** `WRITE_CONTACTS` (*Results in a SecurityException or permission denial once your app targets the upcoming Android release.*) ```kotlin // Requires android.permission.WRITE_CONTACTS fun saveContactDirectly(context: Context, name: String, phone: String, account: Account) { val ops = arrayListOf( ContentProviderOperation.newInsert(ContactsContract.RawContacts.CONTENT_URI) .withValue(ContactsContract.RawContacts.ACCOUNT_TYPE, account.type) .withValue(ContactsContract.RawContacts.ACCOUNT_NAME, account.name) .build(), ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI) .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0) .withValue( ContactsContract.Data.MIMETYPE, ContactsContract.CommonDataKinds.StructuredName.CONTENT_ITEM_TYPE ) .withValue(ContactsContract.CommonDataKinds.StructuredName.DISPLAY_NAME, name) .build(), ContentProviderOperation.newInsert(ContactsContract.Data.CONTENT_URI) .withValueBackReference(ContactsContract.Data.RAW_CONTACT_ID, 0) .withValue( ContactsContract.Data.MIMETYPE, ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE ) .withValue(ContactsContract.CommonDataKinds.Phone.NUMBER, phone) .build() ) context.contentResolver.applyBatch(ContactsContract.AUTHORITY, ops) } ``` | **After: opening the contact editor** (*No permission needed.*) ```kotlin fun saveContactWithEditor( context: Context, name: String, phone: String, account: Account, photoUri: Uri ) { val intent = Intent(Intent.ACTION_INSERT, ContactsContract.Contacts.CONTENT_URI).apply { putExtra(ContactsContract.Intents.Insert.NAME, name) putExtra(ContactsContract.Intents.Insert.PHONE, phone) // Suggest which account the contact is saved to putExtra(ContactsContract.Intents.Insert.EXTRA_ACCOUNT, account) // New in the upcoming Android release: pre-fill the contact photo putExtra(ContactsContract.Intents.Insert.EXTRA_PHOTO_URI, photoUri) clipData = ClipData.newRawUri("", photoUri) addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION) } context.startActivity(intent) } ``` |
| **Before: updating an existing contact directly** ```kotlin // Requires android.permission.WRITE_CONTACTS fun addPhoneDirectly(context: Context, rawContactId: Long, phone: String) { val values = ContentValues().apply { put(ContactsContract.Data.RAW_CONTACT_ID, rawContactId) put(ContactsContract.Data.MIMETYPE, ContactsContract.CommonDataKinds.Phone.CONTENT_ITEM_TYPE) put(ContactsContract.CommonDataKinds.Phone.NUMBER, phone) } context.contentResolver.insert(ContactsContract.Data.CONTENT_URI, values) } ``` | **After: letting the user choose a contact to update, or create a new one** ```kotlin fun addPhoneWithEditor(context: Context, phone: String) { val intent = Intent(Intent.ACTION_INSERT_OR_EDIT).apply { type = ContactsContract.Contacts.CONTENT_ITEM_TYPE putExtra(ContactsContract.Intents.Insert.PHONE, phone) } context.startActivity(intent) } ``` If you already know which contact to update, use `ACTION_EDIT` with that contact's URI: ```kotlin fun editKnownContact(context: Context, contactUri: Uri, phone: String) { val intent = Intent(Intent.ACTION_EDIT, contactUri).apply { putExtra(ContactsContract.Intents.Insert.PHONE, phone) } context.startActivity(intent) } ``` |

#### **Pick a contact: use the Contact Picker**

If you only need to read contacts the user chooses, use the [Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker), available since Android 17. It needs no permission.

#### **Calling and messaging apps: use People Directory**

Some apps add "Call with..." or "Message with..." actions to contacts so people can start a call or chat from the Phone or Contacts app. If your app does this today by writing extra entries into the user's contacts, move to [**People Directory**](https://developer.android.com/reference/android/provider/PeopleContract#implementing-a-people-directory), arriving in Android QPR2 (Q4 2026). It's a new system directory where your app publishes how people can reach each other in your app, without editing the user's contacts.

#### **Examples of how apps can migrate**

To see how these alternatives work in practice, here are a few examples of how different types of apps can approach contact access:

|---|---|
| **Example app type (non-exclusive).** | **Recommended migration path** |
| Social, P2P Payment, \& Ride-Sharing Apps | If your app lets users find friends, split a bill, or share a trip status, you don't need contact permissions at all. Use the Contact Picker for one-time contact selection, and launch `ACTION_INSERT` with `EXTRA_PHOTO_URI` when a user taps "Save to Contacts" on a profile. |
| Business Card Scanners \& Event Networking Apps | If your app scans a badge or QR code and saves a new contact -- or adds a work phone number to an existing colleague's entry -- use `ACTION_INSERT` or `ACTION_INSERT_OR_EDIT`. The standardized half-sheet editor pre-fills the parsed fields (name, company, phone, email, and photo) so the user can verify and save in one tap without granting background permissions. |
| VoIP Calling \& Messaging Apps | Rather than requesting `WRITE_CONTACTS` to inject custom "Call with..." or "Message with..." rows into the user's address book, publish reachability metadata through People Directory and use `ACTION_INSERT` when users add a new contact from a chat thread. |
| Enterprise CRM \& Cloud Sync Apps | If your app performs continuous, two-way background contact synchronization with a cloud or enterprise account -- where prompting the user with an intent UI for every record isn't feasible -- your app qualifies to declare `MANAGE_CONTACTS ` |

#### **Changes to check for**

- **Custom data types aren't supported in the editor.** If you pass `Insert.DATA` rows with MIME types other than the standard `ContactsContract.CommonDataKinds` types, those MIME types will be silently ignored by the editor.
- `SHOW_OR_CREATE_CONTACT`**isn't handled by the system editor.** Contacts apps that come with the device can still handle it. For consistent behavior across devices, use `ACTION_INSERT_OR_EDIT`.
- **Writes fail by default.** Once you target the upcoming Android release, any direct write without `MANAGE_CONTACTS` results in a `SecurityException or permission denial`. Test for it.

#### **Do I need** `MANAGE_CONTACTS`**?**

Probably not. If your app saves or edits contacts because a user asked it to, the intents above cover you, with no permission and no Play Console declaration.

`MANAGE_CONTACTS` is for apps whose core purpose is managing contacts, where the intents aren't enough. For example:

|---|---|
| **Your app...** | **Need** `MANAGE_CONTACTS`**?** |
| Saves a contact from a chat, business card, or order. | **No,** use `ACTION_INSERT` |
| Adds a number or email to an existing contact. | **No,** use `ACTION_INSERT_OR_EDIT` or `ACTION_EDIT` |
| Lets users pick contacts to invite, share with, or pay. | **No,** use the [Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker) |
| Adds call or message actions to contacts. | **No,** use People Directory |
| Has its own branded contact editing screen. | **No,** a custom interface alone doesn't qualify |
| Is a dedicated contact manager or dialer replacement app. | **Likely yes** |
| Is a caller ID \& spam protection app that mass-updates address book entries. | **Likely yes** |
| Syncs contacts with an enterprise or cloud account in the background. | **Likely yes** |
| Performs bulk contact backup/restore or device-to-device phone transfer. | **Likely yes** |
| Sets custom ringtones for individual contacts. | **Likely yes** |

#### **How it works:**

- `MANAGE_CONTACTS` is a special app access permission. It isn't a runtime dialog. Users turn it on under **Settings \> Special app access \> Manage contacts.**

```kotlin
// Opens Settings > Apps > Special app access > Manage contacts
val intent = Intent(Settings.ACTION_MANAGE_CONTACTS, Uri.fromParts("package", packageName, null))
context.startActivity(intent)
```

- It covers reading, adding, editing, and deleting contacts, accounts and People Directory data. You don't need to request `READ_CONTACTS` as well.
- To publish on Google Play with `MANAGE_CONTACTS`, you submit a declaration in Play Console explaining why the intents aren't enough for your app's core functionality.

#### **Migration steps**

- **Find your contact writes.** Search your code for `WRITE_CONTACTS`, `ContactsContract.RawContacts.CONTENT_URI`, `ContactsContract.Data.CONTENT_URI`, and `applyBatch(ContactsContract.AUTHORITY, ...)`.
- **Replace each user-driven write with an intent:** `ACTION_INSERT` for new contacts, and `ACTION_EDIT` or `ACTION_INSERT_OR_EDIT` for updates.
- **Use only standard data types** in `Insert.DATA`. Move call or message actions to People Directory.
- **Decide whether you truly need** `MANAGE_CONTACTS` using the table above. If you do, plan your Play Console declaration.
- **Remove** `WRITE_CONTACTS` from your manifest once no code path needs it.

#### **Timeline**

|---|---|
| **When** | **What happens** |
| **October 21, 2026** | Google Play announces the `MANAGE_CONTACTS` policy |
| **2026 (Android 17 Quarterly Platform Release 2)** | `MANAGE_CONTACTS` permission becomes available |
| **2027 (Upcoming Android release)** | WRITE_CONTACTS no longer grants write access to apps targeting the upcoming Android release. Contact intents are standardized across devices |
| **2027, not earlier than the upcoming Android release** | Play Console asks apps that use `MANAGE_CONTACTS` to submit a declaration |
| **2027, not earlier than the upcoming Android release** | Play policy compliance required |

#### **FAQ**

- **Does this affect every app?**
  - The `WRITE_CONTACTS` deprecation change applies only to apps that target the upcoming Android release and after. Apps targeting older versions keep their current behavior, however, the new standardized contact editor will be available to all apps running on the new OS, regardless of their target SDK.
- **Can my app delete contacts with intent?**
  - No. There's no intent for deleting contacts. Users delete contacts in their contacts app. Apps with `MANAGE_CONTACTS` can delete contacts directly.
- **I already have my own contact editing screen. Can I keep it?**
  - Only if your app qualifies for `MANAGE_CONTACTS`. Wanting to keep a custom design isn't a qualifying reason on its own.
- **Does** `MANAGE_CONTACTS`**replace READ_CONTACTS?**
  - `MANAGE_CONTACTS` includes read access so you don't need to request both, but many apps qualify for `READ_CONTACTS` that do not need to modify contacts at all. These apps may continue to request `READ_CONTACTS`.
- **What about my users on older Android versions?**
  - The contact intents work on older versions too, handled by the device's contacts app. Most apps will work well on all devices using these intents. If your app is affected by a specific consistency issue only solved in the latest versions, you can keep the `WRITE_CONTACTS` permission in your manifest scoped with an appropriate maxSdkVersion.
- [#Android](https://developer.android.com/blog/topics/android)
Written by:

-

  ## [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/roxanna-walker) ![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp) ![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)
Continue reading
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Mesa_de_trabajo_1_copy_8_3f8cf8a935_Z1799P4.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Agentic and Flexible: A next era of Android development](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development)

  [arrow_forward](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development) Today, at the Android Dev Summit, we are announcing the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_Zj9dt4.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) • 2 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_2bzRoq.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)