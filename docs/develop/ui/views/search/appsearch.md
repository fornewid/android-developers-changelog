---
title: https://developer.android.com/develop/ui/views/search/appsearch
url: https://developer.android.com/develop/ui/views/search/appsearch
source: md.txt
---

AppSearch is a high-performance on-device search solution for managing locally
stored, structured data. It contains APIs for indexing data and retrieving data
using full-text search. Applications can use AppSearch to offer custom in-app
search capabilities, allowing users to search for content even while offline.
![Diagram illustrating indexing and searching within AppSearch](https://developer.android.com/static/images/guide/topics/search/appsearch.png)

AppSearch provides the following features:

- A fast, mobile-first storage implementation with low I/O use
- Highly efficient indexing and querying over large data sets
- Multi-language support, such as English and Spanish
- Relevance ranking and usage scoring

Due to lower I/O use, AppSearch offers lower latency for indexing and searching
over large datasets compared to SQLite. AppSearch simplifies cross-type queries
by supporting single queries whereas SQLite merges results from multiple tables.

To illustrate AppSearch's features, let's take the example of a music
application that manages users' favorite songs and allows users to easily search
for them. Users enjoy music from around the world with song titles in different
languages, which AppSearch natively supports indexing and querying for. When the
user searches for a song by title or artist name, the application simply passes
the request to AppSearch to quickly and efficiently retrieve matching songs. The
application surfaces the results, allowing its users to quickly start playing
their favorite songs.

## Setup

To use AppSearch in your application, add the following dependencies to your
application's `build.gradle` file:

### Groovy

```groovy
dependencies {
    def appsearch_version = "1.1.0"

    implementation "androidx.appsearch:appsearch:$appsearch_version"
    // Use kapt instead of annotationProcessor if writing Kotlin classes
    annotationProcessor "androidx.appsearch:appsearch-compiler:$appsearch_version"

    implementation "androidx.appsearch:appsearch-local-storage:$appsearch_version"
    // PlatformStorage is compatible with Android 12+ devices, and offers additional features
    // to LocalStorage.
    implementation "androidx.appsearch:appsearch-platform-storage:$appsearch_version"

    // PlayServicesStorage is compatible with all devices that support Google Play Services on
    // all API levels. It offers the same features as PlatformStorage and is the recommended
    // solution for lower API levels on which PlatformStorage is not supported.
    implementation "androidx.appsearch:appsearch-play-services-storage:$appsearch_version"
}
```

### Kotlin

```kotlin
dependencies {
    val appsearch_version = "1.1.0"

    implementation("androidx.appsearch:appsearch:$appsearch_version")
    // Use annotationProcessor instead of kapt if writing Java classes
    kapt("androidx.appsearch:appsearch-compiler:$appsearch_version")

    implementation("androidx.appsearch:appsearch-local-storage:$appsearch_version")
    // PlatformStorage is compatible with Android 12+ devices, and offers additional features
    // to LocalStorage.
    implementation("androidx.appsearch:appsearch-platform-storage:$appsearch_version")

    // PlayServicesStorage is compatible with all devices that support Google Play Services on
    // all API levels. It offers the same features as PlatformStorage and is the recommended
    // solution for lower API levels on which PlatformStorage is not supported.
    implementation("androidx.appsearch:appsearch-play-services-storage:$appsearch_version")

}
```

## AppSearch concepts

The following diagram illustrates AppSearch concepts and their interactions.

![Diagram
outline of a client application and its interactions with the following
AppSearch concepts: AppSearch database, schema, schema types, documents,
session, and search.](https://developer.android.com/static/images/search/appsearch_overview_diagram.png)
**Figure 1.** Diagram of AppSearch concepts: AppSearch database, schema,
schema types, documents, session, and search.

### Database and session

An AppSearch database is a collection of documents that conforms to the database
schema. Client applications create a database by providing their application
context and a database name. Databases can be opened only by the application
that created them. When a database is opened, a session is returned to interact
with the database. The session is the entry point for calling the AppSearch APIs
and remains open until it's closed by the client application.

### Schema and schema types

A schema represents the organizational structure of data within an AppSearch
database.

The schema is composed of schema types that represent unique types of data.
Schema types consist of properties that contain a name, data type, and
cardinality. Once a schema type is added to the database schema, documents of
that schema type can be created and added to the database.

### Documents

In AppSearch, a unit of data is represented as a document. Each document in an
AppSearch database is uniquely identified by its namespace and ID. Namespaces
are used to separate data from different sources when only one source needs
to be queried, such as user accounts.

Documents contain a creation timestamp, a time-to-live (TTL), and a score that
can be used for ranking during retrieval. A document is also assigned a schema
type that describes additional data properties the document must have.

A document class is an abstraction of a document. It contains annotated fields
that represent the contents of a document. By default, the name of the document
class sets the name of the schema type.

### Search

Documents are indexed and can be searched by providing a query. A document is
matched and included in the search results if it contains the terms in the query
or matches another search specification. Results are ordered based on their
score and ranking strategy. Search results are represented by pages that you can
retrieve sequentially.

AppSearch offers [customizations](https://developer.android.com/reference/androidx/appsearch/app/SearchSpec)
for search, such as filters, page size configuration, and snippeting.

## Platform Storage, Local Storage or Play Services Storage

AppSearch offers three storage solutions: `LocalStorage`, `PlatformStorage` and
`PlayServicesStorage`. With `LocalStorage`, your application manages an
app-specific index that lives in your application data directory. With both
`PlatformStorage` and `PlayServicesStorage`, your application contributes to a
system-wide central index. `PlatformStorage`'s index is hosted in the system
server and `PlayServicesStorage`'s index is hosted in Google Play Service's
storage. Data access within these central indexes is restricted to data your
application has contributed and data that has been explicitly shared with you
by another application. All these storage options share the same API and can be
interchanged based on a device's version:

### Kotlin

```kotlin
if (BuildCompat.isAtLeastS()) {
    appSearchSessionFuture.setFuture(
        PlatformStorage.createSearchSession(
            PlatformStorage.SearchContext.Builder(mContext, DATABASE_NAME)
               .build()
        )
    )
} else {
    if (usePlayServicesStorageBelowS) {
        appSearchSessionFuture.setFuture(
            PlayServicesStorage.createSearchSession(
                PlayServicesStorage.SearchContext.Builder(mContext, DATABASE_NAME)
                    .build()
            )
        )
    } else {
        appSearchSessionFuture.setFuture(
            LocalStorage.createSearchSession(
                LocalStorage.SearchContext.Builder(mContext, DATABASE_NAME)
                    .build()
            )
        )
    }
}
```

### Java

```java
if (BuildCompat.isAtLeastS()) {
    mAppSearchSessionFuture.setFuture(PlatformStorage.createSearchSession(
            new PlatformStorage.SearchContext.Builder(mContext, DATABASE_NAME)
                    .build()));
} else {
    if (usePlayServicesStorageBelowS) {
        mAppSearchSessionFuture.setFuture(PlayServicesStorage.createSearchSession(
                new PlayServicesStorage.SearchContext.Builder(mContext, DATABASE_NAME)
                        .build()));
    } else {
        mAppSearchSessionFuture.setFuture(LocalStorage.createSearchSession(
                new LocalStorage.SearchContext.Builder(mContext, DATABASE_NAME)
                        .build()));
    }
}
```

Using `PlatformStorage` and `PlayServicesStorage`, your application can
securely share data with other applications to allow them to search over
your app's data as well. Read-only application data sharing is granted
using a certificate handshake to ensure that the other application has
permission to read the data. Read more about this API in the documentation
for [`setSchemaTypeVisibilityForPackage()`](https://developer.android.com/reference/androidx/appsearch/app/SetSchemaRequest.Builder#setSchemaTypeVisibilityForPackage(java.lang.String,%20boolean,%20androidx.appsearch.app.PackageIdentifier)).

Additionally with `PlatformStorage`, data that is indexed can be displayed
on System UI surfaces. Applications can opt out of some or all of their data
being displayed on System UI surfaces. Read more about this API in the
documentation for [`setSchemaTypeDisplayedBySystem()`](https://developer.android.com/reference/androidx/appsearch/app/SetSchemaRequest.Builder#setSchemaTypeDisplayedBySystem(java.lang.String,%20boolean)).

| Features | `LocalStorage` (compatible with Android 5.0+) | `PlatformStorage` (compatible with Android 12+) | `PlayServicesStorage` (compatible with Android 5.0+) |
|---|---|---|---|
| Efficient full-text search | Yes | Yes | Yes |
| Multi-language support | Yes | Yes | Yes |
| Reduced binary size | No | Yes | Yes |
| Application-to-application data sharing | No | Yes | Yes |
| Capability to display data on System UI surfaces | No | Yes | No |
| Unlimited document size and count can be indexed | Yes | No | No |
| Faster operations without additional binder latency | Yes | No | No |

There are additional trade-offs to consider when choosing between `LocalStorage`
and `PlatformStorage`. Because `PlatformStorage` wraps Jetpack APIs over the
AppSearch system service, the APK size impact is minimal compared to using
LocalStorage. However, this also means AppSearch operations incur additional
binder latency when calling the AppSearch system service. With `PlatformStorage`
, AppSearch limits the number of documents and size of documents an application
can index to ensure an efficient central index. `PlayServicesStorage` also has
the same limitations as `PlatformStorage` and is only supported on devices with
Google Play services.

## Get started with AppSearch

The example in this section showcases how to use AppSearch APIs to integrate
with a hypothetical note-keeping application.

### Write a document class

The first step to integrate with AppSearch is to write a document class to
describe the data to insert into the database. Mark a class as a document class
by using the [`@Document`](https://developer.android.com/reference/androidx/appsearch/annotation/Document)
annotation.You can use instances of the document class to put documents in and
retrieve documents from the database.

The following code defines a Note document class with a
[`@Document.StringProperty`](https://developer.android.com/reference/androidx/appsearch/annotation/Document.StringProperty) annotated
field for indexing a Note object's text.

### Kotlin

```kotlin
@Document
public data class Note(

    // Required field for a document class. All documents MUST have a namespace.
    @Document.Namespace
    val namespace: String,

    // Required field for a document class. All documents MUST have an Id.
    @Document.Id
    val id: String,

    // Optional field for a document class, used to set the score of the
    // document. If this is not included in a document class, the score is set
    // to a default of 0.
    @Document.Score
    val score: Int,

    // Optional field for a document class, used to index a note's text for this
    // document class.
    @Document.StringProperty(indexingType = AppSearchSchema.StringPropertyConfig.INDEXING_TYPE_PREFIXES)
    val text: String
)
```

### Java

```java
@Document
public class Note {

  // Required field for a document class. All documents MUST have a namespace.
  @Document.Namespace
  private final String namespace;

  // Required field for a document class. All documents MUST have an Id.
  @Document.Id
  private final String id;

  // Optional field for a document class, used to set the score of the
  // document. If this is not included in a document class, the score is set
  // to a default of 0.
  @Document.Score
  private final int score;

  // Optional field for a document class, used to index a note's text for this
  // document class.
  @Document.StringProperty(indexingType = StringPropertyConfig.INDEXING_TYPE_PREFIXES)
  private final String text;

  Note(@NonNull String id, @NonNull String namespace, int score, @NonNull String text) {
    this.id = Objects.requireNonNull(id);
    this.namespace = Objects.requireNonNull(namespace);
    this.score = score;
    this.text = Objects.requireNonNull(text);
  }

  @NonNull
  public String getNamespace() {
    return namespace;
  }

  @NonNull
  public String getId() {
    return id;
  }

  public int getScore() {
    return score;
  }

  @NonNull
  public String getText() {
     return text;
  }
}
```

### Open a database

You must create a database before working with documents. The following code
creates a new database with the name `notes_app` and gets a `ListenableFuture`
for an [`AppSearchSession`](https://developer.android.com/reference/androidx/appsearch/app/AppSearchSession),
which represents the connection to the database and provides the APIs for
database operations.

### Kotlin

```kotlin
val context: Context = getApplicationContext()
val sessionFuture = LocalStorage.createSearchSession(
    LocalStorage.SearchContext.Builder(context, /*databaseName=*/"notes_app")
    .build()
)
```

### Java

```java
Context context = getApplicationContext();
ListenableFuture<AppSearchSession> sessionFuture = LocalStorage.createSearchSession(
       new LocalStorage.SearchContext.Builder(context, /*databaseName=*/ "notes_app")
               .build()
);
```

### Set a schema

You must set a schema before you can put documents in and retrieve
documents from the database. The database schema consists of different types
of structured data, referred to as "schema types." The following code sets the
schema by providing the document class as a schema type.

### Kotlin

```kotlin
val setSchemaRequest = SetSchemaRequest.Builder().addDocumentClasses(Note::class.java)
    .build()
val setSchemaFuture = Futures.transformAsync(
    sessionFuture,
    { session ->
        session?.setSchema(setSchemaRequest)
    }, mExecutor
)
```

### Java

```java
SetSchemaRequest setSchemaRequest = new SetSchemaRequest.Builder().addDocumentClasses(Note.class)
       .build();
ListenableFuture<SetSchemaResponse> setSchemaFuture =
       Futures.transformAsync(sessionFuture, session -> session.setSchema(setSchemaRequest), mExecutor);
```

### Put a document in the database

Once a schema type is added, you can add documents of that type to the database.
The following code builds a document of schema type `Note` using the `Note`
document class builder. It sets the document namespace `user1` to represent an
arbitrary user of this sample. The document is then inserted into the database
and a listener is attached to process the result of the put operation.

### Kotlin

```kotlin
val note = Note(
    namespace="user1",
    id="noteId",
    score=10,
    text="Buy fresh fruit"
)

val putRequest = PutDocumentsRequest.Builder().addDocuments(note).build()
val putFuture = Futures.transformAsync(
    sessionFuture,
    { session ->
        session?.put(putRequest)
    }, mExecutor
)

Futures.addCallback(
    putFuture,
    object : FutureCallback<AppSearchBatchResult<String, Void>?> {
        override fun onSuccess(result: AppSearchBatchResult<String, Void>?) {

            // Gets map of successful results from Id to Void
            val successfulResults = result?.successes

            // Gets map of failed results from Id to AppSearchResult
            val failedResults = result?.failures
        }

        override fun onFailure(t: Throwable) {
            Log.e(TAG, "Failed to put documents.", t)
        }
    },
    mExecutor
)
```

### Java

```java
Note note = new Note(/*namespace=*/"user1", /*id=*/
                "noteId", /*score=*/ 10, /*text=*/ "Buy fresh fruit!");

PutDocumentsRequest putRequest = new PutDocumentsRequest.Builder().addDocuments(note)
       .build();
ListenableFuture<AppSearchBatchResult<String, Void>> putFuture =
       Futures.transformAsync(sessionFuture, session -> session.put(putRequest), mExecutor);

Futures.addCallback(putFuture, new FutureCallback<AppSearchBatchResult<String, Void>>() {
   @Override
   public void onSuccess(@Nullable AppSearchBatchResult<String, Void> result) {

     // Gets map of successful results from Id to Void
     Map<String, Void> successfulResults = result.getSuccesses();

     // Gets map of failed results from Id to AppSearchResult
     Map<String, AppSearchResult<Void>> failedResults = result.getFailures();
   }

   @Override
   public void onFailure(@NonNull Throwable t) {
      Log.e(TAG, "Failed to put documents.", t);
   }
}, mExecutor);
```

### Search

You can search documents that are indexed using the search operations covered in
this section. The following code performs queries for the term "fruit" over the
database for documents that belong to the `user1` namespace.

### Kotlin

```kotlin
val searchSpec = SearchSpec.Builder()
    .addFilterNamespaces("user1")
    .build();

val searchFuture = Futures.transform(
    sessionFuture,
    { session ->
        session?.search("fruit", searchSpec)
    },
    mExecutor
)
Futures.addCallback(
    searchFuture,
    object : FutureCallback<SearchResults> {
        override fun onSuccess(searchResults: SearchResults?) {
            iterateSearchResults(searchResults)
        }

        override fun onFailure(t: Throwable?) {
            Log.e("TAG", "Failed to search notes in AppSearch.", t)
        }
    },
    mExecutor
)
```

### Java

```java
SearchSpec searchSpec = new SearchSpec.Builder()
       .addFilterNamespaces("user1")
       .build();

ListenableFuture<SearchResults> searchFuture =
       Futures.transform(sessionFuture, session -> session.search("fruit", searchSpec),
       mExecutor);

Futures.addCallback(searchFuture,
       new FutureCallback<SearchResults>() {
           @Override
           public void onSuccess(@Nullable SearchResults searchResults) {
               iterateSearchResults(searchResults);
           }

           @Override
           public void onFailure(@NonNull Throwable t) {
               Log.e(TAG, "Failed to search notes in AppSearch.", t);
           }
       }, mExecutor);
```

### Iterate through SearchResults

Searches return a [`SearchResults`](https://developer.android.com/reference/androidx/appsearch/app/SearchResults)
instance, which gives access to the pages of [`SearchResult`](https://developer.android.com/reference/androidx/appsearch/app/SearchResult) objects. Each `SearchResult`
holds its matched [`GenericDocument`](https://developer.android.com/reference/androidx/appsearch/app/GenericDocument), the general form of a
document that all documents are converted to. The following code gets the first
page of search results and converts the result back into a `Note` document.

### Kotlin

```kotlin
Futures.transform(
    searchResults?.nextPage,
    { page: List<SearchResult>? ->
        // Gets GenericDocument from SearchResult.
        val genericDocument: GenericDocument = page!![0].genericDocument
        val schemaType = genericDocument.schemaType
        val note: Note? = try {
            if (schemaType == "Note") {
                // Converts GenericDocument object to Note object.
                genericDocument.toDocumentClass(Note::class.java)
            } else null
        } catch (e: AppSearchException) {
            Log.e(
                TAG,
                "Failed to convert GenericDocument to Note",
                e
            )
            null
        }
        note
    },
    mExecutor
)
```

### Java

```java
Futures.transform(searchResults.getNextPage(), page -> {
  // Gets GenericDocument from SearchResult.
  GenericDocument genericDocument = page.get(0).getGenericDocument();
  String schemaType = genericDocument.getSchemaType();

  Note note = null;

  if (schemaType.equals("Note")) {
    try {
      // Converts GenericDocument object to Note object.
      note = genericDocument.toDocumentClass(Note.class);
    } catch (AppSearchException e) {
      Log.e(TAG, "Failed to convert GenericDocument to Note", e);
    }
  }

  return note;
}, mExecutor);
```

### Remove a document

When the user deletes a note, the application deletes the corresponding `Note`
document from the database. This ensures the note will no longer be surfaced in
queries. The following code makes an explicit request to remove the `Note`
document from the database by Id.

### Kotlin

```kotlin
val removeRequest = RemoveByDocumentIdRequest.Builder("user1")
    .addIds("noteId")
    .build()

val removeFuture = Futures.transformAsync(
    sessionFuture, { session ->
        session?.remove(removeRequest)
    },
    mExecutor
)
```

### Java

```java
RemoveByDocumentIdRequest removeRequest = new RemoveByDocumentIdRequest.Builder("user1")
       .addIds("noteId")
       .build();

ListenableFuture<AppSearchBatchResult<String, Void>> removeFuture =
       Futures.transformAsync(sessionFuture, session -> session.remove(removeRequest), mExecutor);
```

### Persist to disk

Updates to a database should be periodically persisted to disk by calling
[`requestFlush()`](https://developer.android.com/reference/androidx/appsearch/app/AppSearchSession#requestFlush()). The
following code calls `requestFlush()` with a listener to determine if the call
was successful.

### Kotlin

```kotlin
val requestFlushFuture = Futures.transformAsync(
    sessionFuture,
    { session -> session?.requestFlush() }, mExecutor
)

Futures.addCallback(requestFlushFuture, object : FutureCallback<Void?> {
    override fun onSuccess(result: Void?) {
        // Success! Database updates have been persisted to disk.
    }

    override fun onFailure(t: Throwable) {
        Log.e(TAG, "Failed to flush database updates.", t)
    }
}, mExecutor)
```

### Java

```java
ListenableFuture<Void> requestFlushFuture = Futures.transformAsync(sessionFuture,
        session -> session.requestFlush(), mExecutor);

Futures.addCallback(requestFlushFuture, new FutureCallback<Void>() {
    @Override
    public void onSuccess(@Nullable Void result) {
        // Success! Database updates have been persisted to disk.
    }

    @Override
    public void onFailure(@NonNull Throwable t) {
        Log.e(TAG, "Failed to flush database updates.", t);
    }
}, mExecutor);
```

### Close a session

An [`AppSearchSession`](https://developer.android.com/reference/androidx/appsearch/app/AppSearchSession)
should be closed when an application will no longer be calling any database
operations. The following code closes the AppSearch session that was opened
previously and persists all updates to disk.

### Kotlin

```kotlin
val closeFuture = Futures.transform<AppSearchSession, Unit>(sessionFuture,
    { session ->
        session?.close()
        Unit
    }, mExecutor
)
```

### Java

```java
ListenableFuture<Void> closeFuture = Futures.transform(sessionFuture, session -> {
   session.close();
   return null;
}, mExecutor);
```

## Additional resources

To learn more about AppSearch, see the following additional resources:

### Samples

- [Android AppSearch Sample (Kotlin)](https://github.com/android/search-samples/tree/main/AppSearchSample), a note taking app that uses AppSearch to index a user's notes and allows users to search over their notes.

## Provide feedback

Share your feedback and ideas with us through these resources:

[Issue tracker](https://issuetracker.google.com/issues/new?component=1012737&template=1551039)

Report bugs so we can fix them.