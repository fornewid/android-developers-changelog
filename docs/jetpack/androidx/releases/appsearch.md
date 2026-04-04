---
title: https://developer.android.com/jetpack/androidx/releases/appsearch
url: https://developer.android.com/jetpack/androidx/releases/appsearch
source: md.txt
---

# AppSearch

<br />

# AppSearch

[User Guide](https://developer.android.com/guide/topics/search/appsearch)[Code Sample](https://github.com/android/search-samples/tree/main/AppSearchSample)  
API Reference  
[androidx.appsearch.annotation](https://developer.android.com/reference/kotlin/androidx/appsearch/annotation/package-summary)  
[androidx.appsearch.app](https://developer.android.com/reference/kotlin/androidx/appsearch/app/package-summary)  
[androidx.appsearch.exceptions](https://developer.android.com/reference/kotlin/androidx/appsearch/exceptions/package-summary)  
[androidx.appsearch.localstorage](https://developer.android.com/reference/kotlin/androidx/appsearch/localstorage/package-summary)  
[androidx.appsearch.platformstorage](https://developer.android.com/reference/kotlin/androidx/appsearch/platformstorage/package-summary)  
AppSearch is an on-device search library for managing locally stored structured data, with APIs for indexing data and retrieving data using full-text search. Use it to build custom in-app search capabilities for your users.  

| Latest Update |                                  Stable Release                                  | Release Candidate | Beta Release | Alpha Release |
|---------------|----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| July 2, 2025  | [1.1.0](https://developer.android.com/jetpack/androidx/releases/appsearch#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on AppSearch, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

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

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1012737+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1012737&template=1551039)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

<br />

## Version 1.1

### Version 1.1.0

July 2, 2025

`androidx.appsearch:appsearch-*:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/bfcc16b55545366a116d37026ec4fe09c76be5dc..1ba9efeef17e71a00ddd145f3d0c5c2de2544c2c/appsearch).

### Version 1.1.0-rc01

May 20, 2025

`androidx.appsearch:appsearch-*:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/526ee99f5544977319165add70bf02aef2b565e5..bfcc16b55545366a116d37026ec4fe09c76be5dc/appsearch).

**New Features**

- `AppSearch`module enters RC.
- Adds a new experimental API to accumulate actions for the`PutDocumentsRequest#addTakenAction`method ([I7b726](https://android-review.googlesource.com/#/q/I7b726181412bd1213e46efee73a8e8e08bb61163))
- Add`SearchResult#TextMatchInfo`,`SearchResult#EmbeddingMatchInfo`; restructure`SearchResult#MatchInfo`for providing match information for embeddings matches ([I8f78d](https://android-review.googlesource.com/#/q/I8f78d8d18bcb5fcb208eba9c9e6a393ef084a183))
- Introduce ranking functions for list manipulation ([Ifa4ab](https://android-review.googlesource.com/#/q/Ifa4abb9e3443b9609f2fc7b9891dfd3e3928e936))

**API Changes**

- Support`AppSearch`annotation processor for blob handle property. ([I9520b](https://android-review.googlesource.com/#/q/I9520b94835913c640fa5e8bc6c24fc407f8e48c5))
- Update`AppSearch`annotation processor to support quantization. ([Ie0c85](https://android-review.googlesource.com/#/q/Ie0c855518e12777217ad59fd3b70b7c52d62b48d))
- Adds a static`getFeatures()`method to both`PlatformStorage`and`LocalStorage`([I5a206](https://android-review.googlesource.com/#/q/I5a20604fe044b2897e200477e09f52e1a8bc009a))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler arguments to enforce correct usage: -Xjspecify-annotations=strict, -Xtype-enhancement-improvements-strict-mode ([I91f42](https://android-review.googlesource.com/#/q/I91f42df892eec57a57a0ffdc8d42a3563fcab8c3),[b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.1.0-beta01

January 15, 2025

`androidx.appsearch:appsearch-*:1.1.0-beta01`is released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6bcf9447694395f39462f000cc77949d13e607c6..526ee99f5544977319165add70bf02aef2b565e5/appsearch).

**New Features**

- `AppSearch`module enters Beta.

**API Changes**

- Disable experimental`AppSearch`delete propagation API due to stability issues. ([Iea386](https://android-review.googlesource.com/#/q/Iea3866b5283eb65278b53f98c704cf15a74ce3e1))
- Create`GlobalSearchApplicationInfo`API, an experimental and optional way for producers and consumers to indicate interest in certain types. ([I116fd](https://android-review.googlesource.com/#/q/I116fd7c64fbffd730d9b8a9ed4e82272a24a8a02))
- Minor changes to experimental AST (query builder) APIs ([Ibd852](https://android-review.googlesource.com/#/q/Ibd852844bdb65a67feb539e3ed18e1e297b0cfa4))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ic2976](https://android-review.googlesource.com/#/q/Ic29767a1bbc463de7ce6d36001e73d1fe88f27af),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Adds required permission to`searchPersonCorpus`([I4431d](https://android-review.googlesource.com/#/q/I4431d89267bea8199c2786c4dc95bf7c7f313192))

### Version 1.1.0-alpha07

December 11, 2024

`androidx.appsearch:appsearch-*:1.1.0-alpha07`is released. Version 1.1.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..7c975fb1157a92d4285d963b9dfe96e587f3b8b8/appsearch).

**New Features**

- Add`ExperimentalAppSearchApi`annotation to new API surfaces that have not yet stabilized. ([Ib09f4](https://android-review.googlesource.com/#/q/Ib09f445fb4b85f3e6d5d19a904345d41e515cdb5))
- Support for efficiently storing and sharing binary blob data via`AppSearchSession#openBlobForWriteAsync`and related methods
- Support for filtering query results by scoring expression via the`matchScoreExpression`function ([Id525a](https://android-review.googlesource.com/#/q/Id525aa1009fd953ee47b0f4b7e585a6c0b3c3068))
- Support for propagating deletion from parent document to child documents. ([Ia032d](https://android-review.googlesource.com/#/q/Ia032df778f01bc6d57ce3820c1165334bdeab92f))
- Support for embedding quantization API to increase embedding performance with slight quality loss. ([Id8a07](https://android-review.googlesource.com/#/q/Id8a075c6450a3ef331ddbf8da546ad6db5dcd6f8))
- Support for restricting searches to certain documents using the`addFilterDocumentIds`API in`SearchSpec`. ([I7c6f1](https://android-review.googlesource.com/#/q/I7c6f1cd1574d5994695908b34d06c5dce7df7c00))

**API Changes**

- Move parent type information from`GenericDocument`to`SearchResult`. ([I34a1d](https://android-review.googlesource.com/#/q/I34a1d16719a158cdb3db5f4e2eeafbeaa1a6a339))
- Support for new action types in the`TakenAction`API, including`DismissAction`and`ImpressionAction`. ([I0c6c7](https://android-review.googlesource.com/#/q/I0c6c7f0966eceabb045b9fd08d1122b037756338))
- Added new AppSearch builtin schema`WebPage`. ([I28127](https://android-review.googlesource.com/#/q/I28127f5904084d2d5f56ce9bb7d2bad965943e84))

### Version 1.1.0-alpha06

October 16, 2024

`androidx.appsearch:appsearch-*:1.1.0-alpha06`is released. Version 1.1.0-alpha06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..b8a68b0896897fa158508d73a31998a26161d9a7/appsearch).

**API Changes**

- Added node representing the`PropertyDefined`query function. ([I1aeaf](https://android-review.googlesource.com/#/q/I1aeafb0dbb97fa06ecd90df9e60f5cdccc098789))
- Add nodes to represent numeric search and property restrict. ([I963a9](https://android-review.googlesource.com/#/q/I963a93d64dde5d39a1c2538555e01360c6522188))
- Add node representing`GetSearchStringParameter`query function. ([I4f99b](https://android-review.googlesource.com/#/q/I4f99b65bbfa33985e5b6e21018cc798d3248e1ba))
- Add node representing the`HasProperty`query function. ([I9c1c5](https://android-review.googlesource.com/#/q/I9c1c5231f19c240e8059f76028c4dd85a8b776c1))
- Added interface for implementing functions in AST. ([I9d42e](https://android-review.googlesource.com/#/q/I9d42e6ad6126e592347b17b28acad063c719d458))
- Add AND and OR operators. ([Iaa442](https://android-review.googlesource.com/#/q/Iaa44230f703098235ffe70dd25ee0f4342537d33))
- Add`NegationNode`for representing logical negation of queries in AST. ([Ia855a](https://android-review.googlesource.com/#/q/Ia855a494a5365efcc6126576f5bbfe01ad52ac28))
- Add Node interface to`AppSearch`for defining nodes. ([If42fb](https://android-review.googlesource.com/#/q/If42fba0055d383f208eaa287af3e3b77d1bb06da))
- Adds an Experimental API annotation for`AppSearch`. ([I3e57c](https://android-review.googlesource.com/#/q/I3e57c906da6a8a907a16018d775c50e0cb3e8ccc))

**Bug Fixes**

- Add`TextNodes`for holding terms. ([Iefd02](https://android-review.googlesource.com/#/q/Iefd02067696b8f9012b7cdaed29aba42de36877b))

**Security Fix**

- As of[this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address[CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on`androidx.appsearch:appsearch-external-protobuf`to the latest 1.1.0-alpha06 to address the vulnerability risk.

### Version 1.1.0-alpha05

September 4, 2024

`androidx.appsearch:appsearch-*:1.1.0-alpha05`is released. Version 1.1.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/67687dad8bd1314c67bac1e4aba4c9891177b0e1..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/appsearch).

**API Changes**

- Deprecates unnecessary`setEmbeddingSearchEnabled`and`getEmbeddingSearchEnabled`. Deletes`setListFilterTokenizeFunctionEnabled`and`getListFilterTokenizeFunctionEnabled`. Deleted the 'tokenize' query function. Replaced with`getSearchStringParameter`query function and`addSearchStringParameter`function. ([I09f5a](https://android-review.googlesource.com/#/q/I09f5af2cd71508b27b7a18c35bdd188359287a1c))
- Rename`Alarm#getComputingDevice`to`getOriginatingDevice`. ([I63121](https://android-review.googlesource.com/#/q/I631212851f54212de5d7c674715e8bca8a44f19f))

### Version 1.1.0-alpha04

August 7, 2024

`androidx.appsearch:appsearch-*:1.1.0-alpha04`is released. Version 1.1.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/67687dad8bd1314c67bac1e4aba4c9891177b0e1/appsearch).

**New Features**

- Support for new`PlayServicesStorage`implementation, which allows using`AppSearch`on older devices without incurring the significant apk size cost of`LocalStorage`. This storage implementation works by storing app data within the Play Services app.
- Support for new APIs on devices running Android 15.
- Support searching the database by embedding vectors, allowing for fuzzy matching. ([I2b41b](https://android-review.googlesource.com/#/q/I2b41b0c5b1fa7b80e9eced8a53f7f642c025cacf))
- Support parent types and polymorphism within the`AppSearch`schema model. ([I06118](https://android-review.googlesource.com/#/q/I0611822dac1c59abd2b0a1612f230483707fa7f4))
- Support the`TakenAction`API which allows apps to report when results were clicked or abandoned, for quality boosting during subsequent searches. ([I54091](https://android-review.googlesource.com/#/q/I5409187483287d0bc450c457e37e757c5f8378ba))
- Support classes with builders in the annotation processor by introducing the new`@Document.BuilderProducer`annotation. ([Iec30a](https://android-review.googlesource.com/#/q/Iec30a82e04c57f230021f0472146de026ef64ead))
- Support finer-grained control over which properties of a nested document get indexed. ([Iec30a](https://android-review.googlesource.com/#/q/Iec30a82e04c57f230021f0472146de026ef64ead))
- Support for filtering searches to certain document properties. ([Ib2659](https://android-review.googlesource.com/#/q/Ib2659afc81845eeab388ada820b7f3ea7344d363))
- Support finer-grained visibility settings by allowing OR and AND of visibility settings. ([I0274b](https://android-review.googlesource.com/#/q/I0274b77408deea1bc9fb53386518e0d37bda4f77))
- Support for granting visibility of data to all apps that can see the existence of the owning app (public visibility). ([I992e4](https://android-review.googlesource.com/#/q/I992e4a7845477e176776c4d78a2e45c0b75245dc))
- Support for retrieving only results that have data populated in a certain property. ([I7d94f](https://android-review.googlesource.com/#/q/I7d94f11a2c15d737df00c62baa6dcc000f34f508))
- Support for retrieving enterprise contacts in the personal profile. ([Idd587](https://android-review.googlesource.com/#/q/Idd5879214c6b30778802597b7281a2d27862a740))

**API Changes**

- Add`indexableNestedPropertiesList`and`inheritIndexableNestedPropertiesFromSuperclass`annotation parameters to AppSearch's`Document.DocumentProperty`annotation to allow indexing specific nested property paths. ([Iec30a](https://android-review.googlesource.com/#/q/Iec30a82e04c57f230021f0472146de026ef64ead))
- Support builder constructor to create builder instances in`AppSearch`annotation processor ([I265c9](https://android-review.googlesource.com/#/q/I265c9bbe77a4c2d9c078eb0103574b56328a0069))
- Update`AppSearch`annotation processor to support setting parent types for polymorphism ([I06118](https://android-review.googlesource.com/#/q/I0611822dac1c59abd2b0a1612f230483707fa7f4))
- Adds`GetSchemaRequest`method for clearing visibility settings ([I38379](https://android-review.googlesource.com/#/q/I383799476dc7550e54f9b569e4ff149db72b81bf))
- Support`addParentType`in AppSearch for polymorphism ([Ida14a](https://android-review.googlesource.com/#/q/Ida14a3157ceab552778b757f8ab8f9c28784ad28))
- Add APIs for additional ranking expressions ([I5d9f4](https://android-review.googlesource.com/#/q/I5d9f4eac2ba39b1a962616634cc4d7b73dda8a28))
- Add`SearchAction`API ([I54091](https://android-review.googlesource.com/#/q/I5409187483287d0bc450c457e37e757c5f8378ba))
- Adds description field for`AppSearch`types ([I84762](https://android-review.googlesource.com/#/q/I847620d214f887908e0016cc8a8580fcf4413d6c))
- Onboard embedding search query and ranking APIs to`AppSearch`([I0f6c3](https://android-review.googlesource.com/#/q/I0f6c3a8b7cf14986c58a896728c2c35401b25808))
- Removes`getDeletionPropagation`([I21192](https://android-review.googlesource.com/#/q/I21192849a6ac7e44086c0ffcaf464545c1ced8ad))

### Version 1.1.0-alpha03

May 24, 2023

`androidx.appsearch:appsearch-*:1.1.0-alpha03`is released.[Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6963514be8a8825fda0b0a34aaffd070d41a05ff..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/appsearch)

**New Features**

- Support for an advanced query API, advanced scoring API, and numeric search. ([I02d48](https://android-review.googlesource.com/#/q/I02d4800cc06f9dda0b7bb1af96d90e2abd1f17ea))
- Adds`LocalStorage.createGlobalSearchSession`API to search across all databases within the local storage of a single app. ([Id3c89](https://android-review.googlesource.com/#/q/Id3c89c5cb7a7d2da4cdfce41787977df22b143d7))
- Added an API to join documents by ID ([Iaecfa](https://android-review.googlesource.com/#/q/Iaecfac98765e5d71d586ddd28fd468f81e369ee2))
- Support property weights to mark certain properties are more important when using`RANKING_STRATEGY_RELEVANCE_SCORING`. ([I069b9](https://android-review.googlesource.com/#/q/I069b9bf88a9bd6b3b4b6fcee4e0a8ec526b71c98))
- Add Person and`ContactPoint`for querying Person corpus in`AppSearch`. ([Ia58f9](https://android-review.googlesource.com/#/q/Ia58f9eb3ee198d2052955aa78b6f069967b3f897))
- Added new Document type`ImageObject`modeled after http://schema.org/ImageObject. ([I6a0c0](https://android-review.googlesource.com/#/q/I6a0c03151a811f84f952e07d7d487a792cdeb2c2))
- Add a`VERBATIM`tokenizer which allows adding properties without interpretation by`AppSearch`. ([I47bc0](https://android-review.googlesource.com/#/q/I47bc079295517890460935b112a2601a24044df0))
- Added`RFC822_TOKENIZATION`as a tokenizer type, allowing tokenization of email addresses. ([I8a390](https://android-review.googlesource.com/#/q/I8a39074e5a493f2860a787c7393faa73e8c60ed7))
- Enable Global Search in the Debug View. ([I51fb2](https://android-review.googlesource.com/#/q/I51fb2939a4c34f7aa5ae92a3f7371ebfe1e5c11c))

**API Changes**

- Removed methods that return`ListenableFuture`and don't have Async suffix. ([I0515f](https://android-review.googlesource.com/#/q/I0515f9951bf490f1c2336ee7316df032c18a6571))
- Adds the ability to configure projections by a`Document`class. ([I94576](https://android-review.googlesource.com/#/q/I945764380bfd371433d853a15a159a2394ffab01))
- Add fields from`Thing`to`Alarm`,`AlarmInstance`,`Timer`,`Stopwatch`,`StopwatchLap`,`ContactPoint`, and`Person`([Id876c](https://android-review.googlesource.com/#/q/Id876c358ed6fe6854eead84353bcb55c20869178))

**Bug Fixes**

- Fully support Android 13 features in appsearch-platform-storage ([Ia8e61](https://android-review.googlesource.com/#/q/Ia8e617391ceb38f5cab56dcbb1adfa01a639aa79))
- Fix issues with overriding schema names and private fields when using inheritance.

### Version 1.1.0-alpha02

August 24, 2022

`androidx.appsearch:appsearch-*:1.1.0-alpha02`is released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c24e9aa02c6f6b97ada475f6d66eab39d72d29ba..dd1e45e8550560087f6447a34a9145048b5766f4/appsearch)

**New Features**

- Sped up Optimize process using index compaction rather than rebuilding index from scratch
- Changed native logging tag from "icing" to "AppSearchIcing", log INFO messages by default

**API Changes**

- Adds new`PropertyPath`object for working with paths, and new`addProjection`methods to accept`PropertyPath`. ([I45588](https://android-review.googlesource.com/#/q/I45588aad8525a9150768089d78541a0f5e4dc767))
- Added`builtin:Thing`to`AppSearch`builtin types ([I55427](https://android-review.googlesource.com/#/q/I55427fc371d3a22da578522114766bb9e529286b))
- Prevent empty property names in`GenericDocument`sooner -- previously they were prevented at indexing time, now they are prevented at`GenericDocument.Builder.build()`time ([I9e780](https://android-review.googlesource.com/#/q/I9e780218dd4fc8a65092ec76bcac8c0ba0cd4636))

**Bug Fixes**

- Removed unnecessary string formatting to improve RELEVANCE scoring performance
- More efficient pagination when encountering unreadable or deleted documents
- Implemented garbage collection for abandoned queries
- Fix nested indexing support for Documents. Previously indexNestedProperties was ignored. ([Iae9a6](https://android-review.googlesource.com/#/q/Iae9a67a03e8f2d6447578c0c26a53d03290b493f))

**External Contribution**

- Shea Smith: Fix nested indexing support for Documents. ([Iae9a6](https://android-review.googlesource.com/#/q/Iae9a67a03e8f2d6447578c0c26a53d03290b493f))

### Version 1.1.0-alpha01

June 15, 2022

`androidx.appsearch:appsearch-*:1.1.0-alpha01`is released. Version 1.1.0-alpha01 was developed in a private pre-release branch and has no public commits.

**API Changes**

- All methods returning`ListenableFuture`have been renamed to have the Async suffix. For example,`getSchema`has been renamed to`getSchemaAsync`. The previous versions have been deprecated and will be removed in a future release.

**New Features**

- First release of appsearch-builtin-types. This project contains some builtin types based on schema.org which clients may find convenient to use instead of defining their own types for common objects. More types will be added in future releases.
- Ability to use`ShortcutAdapter`to convert an`AppSearch`Document into a`ShortcutInfoCompat`. This gives clients a way to share`AppSearch`documents to Google using the core-google-shortcuts library
- Ability to use inheritance with`@Document`classes. Fields cannot be replaced or modified, but new fields can be added by extending a class annotated with`@Document`.
- New Observer API which allows clients to register for notifications when types they have access to have changed or when documents of those types are added, modified or removed. IMPORTANT: The current implementation delivers notifications only when your app is running. There is currently no way to inspect changes that have occurred while your app was stopped. Accordingly you should not rely on this API for completeness.
- Property parser API which allows you to fully handle and inspect property paths returned by`MatchInfo#getPropertyPath`.
- Global`getById`and global`getSchema`API for retrieving documents and schemas from other apps which have granted you visibility.
- Ability to retrieve visibility information in`getSchema`for data you have access to
- Ability to grant visibility to apps holding a certain Android permission (restricted to a narrow set of allowlisted permissions)
- Support`isFoo()`-style getters for boolean fields in the annotation processor, in addition to the previous supported style`hasFoo()`
- Support for new features guarded behind`@RequiresFeature`. Use`AppSearchSession#getFeatures`to determine what the current backend supports.
- Remove the \~13k token limit on individual documents
- Allow matching on non-ascii+non-alphanumeric characters, such as emojis

**Bug Fixes**

- Fix bug that would fail`SetSchema`when overriding a nested incompatible type.
- Fixes to fully support`@AutoValue`-annotated classes being used as AppSearch`@Document`classes
- Fixes for some crashes related to repeated lists of Document classes and other issues
- Fix for bug that would crash prefix search under certain circumstances
- Fix minor bug in`GetStorageInfo`that would return incorrect values when encountering IO failures
- Fix`BUSADDERR`issues when reading a document
- Fix logcat corruption caused by printing unformatted fingerprint
- Fix NPE caused by IO failures
- Fix memory leak in`GetSchemaType`,`Get`,`Delete`,`DeleteByNamespace`and`DeleteBySchemaType`

## Version 1.0.0

### Version 1.0.0-alpha04

November 3, 2021

`androidx.appsearch:appsearch-*:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85f7b1566fa43b10b48aa6c8fbb3855f6cd02adb..f07d12061370a603549747200c79b60239706330/appsearch)

**New Features**

- Guava ListenableFuture dependency automatically brought in as an API dependency

**API Changes**

- Add SearchResult#getSubmatchRange() and SearchResult#getSubmatch() to provide more information about each match. ([I2fef6](https://android-review.googlesource.com/#/q/I2fef6746cada48fc7d0e51cf55378c71a6cb3ba8))
- Clarify documentation around how to generate PackageIdentifier fingerprints for sharing data by packagename+certificate

**Bug Fixes**

- Fix crash if user tries to fetch result pages after the end of the result set
- Fix issue with all namespaces being queried if only invalid namespaces were supplied as query filters
- Fix issue with all namespaces being removed if only invalid namespaces were supplied as remove-by-query filtersLo
- Fix issue where document data stopped being indexed after a certain point for very large documents
- Fix issue where tokenization would drop segments with non-Ascii numeric characters
- Add check for consecutive failed initialization attempts to help break out of potential bad state that prevents successful initialization.

### Version 1.0.0-alpha03

July 21, 2021

`androidx.appsearch:appsearch-*:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/85f7b1566fa43b10b48aa6c8fbb3855f6cd02adb/appsearch)

**New Features**

- Release of the Platform Storage Backend to allow clients to use the AppSearch API with the new[`android.app.appsearch.AppSearchManager`](https://developer.android.com/reference/android/app/appsearch/AppSearchManager)service launching in Android S. For more details, please visit AppSearch Developer Guide.
- Annotation processor support for AutoValue
- Removal of maximum size limit of single string property
- New storage format to reduce initialization latency
- A one-time, internal data migration from old storage format to new storage format

**Bug Fixes**

- Correctly enforces maximum document limit when inserting new documents
- Fixed crash during AppSearchSession creation
- Fixed bugs in SetSchema that were not detecting some cases of backwards incompatibility and index incompatibility

### Version 1.0.0-alpha02

June 30, 2021

`androidx.appsearch:appsearch:1.0.0-alpha02`,`androidx.appsearch:appsearch-compiler:1.0.0-alpha02`, and`androidx.appsearch:appsearch-local-storage:1.0.0-alpha02`are released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/43efd2a468468f712e4555faaea12019fdfb06e9..8276b615cf32743aaecf8bca0e294eb2e8eb236b/appsearch)

**New Features**

- Full support of Chinese/Japanese/Korean/Thai languages
- Reduced size of`androidx.appsearch:appsearch-local-storage`
- Removal of maximum size limit of repeated properties
- Allow reuse of builder classes
- Improvements in`toString()`of certain objects for easier debugging
- Javadoc documentation improvements

**API Changes**

- `SearchResult#getMatches`renamed to`SearchResult#getMatchInfos`
- `@Document.Int64Property`renamed to`@Document.LongProperty`

**Bug Fixes**

- Improvements and fixes to computation of result snippets
- Fixes to bugs in AppSearchSession initialization

### Version 1.0.0-alpha01

May 5, 2021

`androidx.appsearch:appsearch:1.0.0-alpha01`,`androidx.appsearch:appsearch-compiler:1.0.0-alpha01`, and`androidx.appsearch:appsearch-local-storage:1.0.0-alpha01`are released.[Version 1.0.0-alpha01 contains these commits.](https://googleplex-android.googlesource.com/platform/frameworks/support/+log/43efd2a468468f712e4555faaea12019fdfb06e9/appsearch)

**New Features**

AppSearch is a search library for managing locally stored structured data, with APIs for indexing data and retrieving data via full-text search. Use it to build custom in-app search capabilities for your users. This initial release is`1.0.0-alpha01`.