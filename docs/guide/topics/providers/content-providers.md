---
title: Content providers  |  App data and files  |  Android Developers
url: https://developer.android.com/guide/topics/providers/content-providers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Content providers Stay organized with collections Save and categorize content based on your preferences.




Content providers can help an application manage access to data stored by itself or
stored by other apps and provide a way to share data with other apps. They encapsulate the
data and provide mechanisms for defining data security. Content providers are the standard
interface that connects data in one process with code running in another process.

Implementing a content provider has many advantages. Most importantly, you can configure a
content provider to let other applications securely access and modify your app data,
as illustrated in figure 1.

![Overview diagram of how content providers manage access to storage.](/static/guide/topics/providers/images/content-provider-overview.png)

**Figure 1.** Overview diagram of how content providers
manage access to storage.

Use content providers if you plan to share data. If you don’t plan to share data,
you don't have to use them, but you might choose to because they provide an abstraction
that lets you make modifications to your application data storage
implementation without affecting other applications that rely on access to your data.

In this scenario, only your content provider is affected and not the applications that
access it. For example, you might swap out a SQLite database for alternative storage, as
illustrated in figure 2.

![Illustration of migrating content provider storage.](/static/guide/topics/providers/images/content-provider-migration.png)

**Figure 2.** Illustration of migrating content provider storage.

A number of other classes rely on the `ContentProvider` class:

* `AbstractThreadedSyncAdapter`
* `CursorAdapter`
* `CursorLoader`

If you use any of these classes, you need to implement a content provider
in your application. When working with the sync adapter framework you can also create
a stub content provider as an alternative. For more information, see
[Create a stub content
provider](/training/sync-adapters/creating-stub-provider). In addition, you need your own content provider in the following cases:

* To implement custom search suggestions in your application.
* To expose your application data to widgets.
* To copy and paste complex data or files from your application to other
  applications.

The Android framework includes content providers that manage data such as audio, video, images,
and personal contact information. You can see some of them listed in the reference
documentation for the
`android.provider` package. With some restrictions, these providers are accessible to any Android
application.

A content provider can be used to manage access to a variety of data storage sources, including
both structured data, such as a SQLite relational database, or unstructured data such as image
files. For more information about the types of storage available on Android, see the
[Data and file storage overview](/guide/topics/data/data-storage) and
[Design data storage](/guide/topics/providers/content-provider-creating#DataStorage).

## Advantages of content providers

Content providers offer granular control over the permissions for accessing data. You can
choose to restrict access to only a content provider that is within your application, grant
blanket permission to access data from other applications, or configure different permissions
for reading and writing data. For more information about using content providers securely, see the
[security tips for data storage](/privacy-and-security/security-tips#StoringData) and
[Content provider permissions](/guide/topics/providers/content-provider-basics#Permissions).

You can use a content provider to abstract away the details for accessing different data
sources in your application. For example, your application might store structured records in a
SQLite database, as well as video and audio files. You can use a content provider to access all
of this data.

Also, `CursorLoader` objects rely on content providers to run
asynchronous queries and then return the results to the UI layer in your application. For more
information about using a `CursorLoader` to load data in the background, see
[Loaders](/training/load-data-background/setup-loader).

The following topics describe content providers in more detail:

**[Content provider basics](/guide/topics/providers/content-provider-basics)**
:   How to access and update data using an existing content provider.

**[Create a content provider](/guide/topics/providers/content-provider-creating)**
:   How to design and implement your own content provider.

**[Calendar provider overview](/guide/topics/providers/calendar-provider)**
:   How to access the Calendar Provider that is part of the Android platform.

**[Contacts Provider](/guide/topics/providers/contacts-provider)**
:   How to access the Contacts Provider that is part of the Android platform.