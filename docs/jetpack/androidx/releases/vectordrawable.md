---
title: https://developer.android.com/jetpack/androidx/releases/vectordrawable
url: https://developer.android.com/jetpack/androidx/releases/vectordrawable
source: md.txt
---

# Vectordrawable

[User Guide](https://developer.android.com/guide/topics/graphics/vector-drawable-resources)  
API Reference  
[androidx.vectordrawable.graphics.drawable](https://developer.android.com/reference/kotlin/androidx/vectordrawable/graphics/drawable/package-summary)  
Render vector graphics.  

| Latest Update |                                    Stable Release                                     | Release Candidate | Beta Release | Alpha Release |
|---------------|---------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| May 1, 2024   | [1.2.0](https://developer.android.com/jetpack/androidx/releases/vectordrawable#1.2.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on VectorDrawable, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.vectordrawable:vectordrawable:1.2.0"

    /* To be able to animate properties of a VectorDrawable, add the following.  Useful for
     * illustration purposes or state changes in response to user events
     */
    implementation "androidx.vectordrawable:vectordrawable-animated:1.2.0"

    /* To use a seekable alternative for `androidx.vectordrawable:vectordrawable-animated` add the
     * following
     */
     implementation "androidx.vectordrawable:vectordrawable-seekable:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.vectordrawable:vectordrawable:1.2.0")

    /* To be able to animate properties of a VectorDrawable, add the following.  Useful for
     * illustration purposes or state changes in response to user events
     */
    implementation("androidx.vectordrawable:vectordrawable-animated:1.2.0")

    /* To use a seekable alternative for `androidx.vectordrawable:vectordrawable-animated` add the
     * following
     */
     implementation("androidx.vectordrawable:vectordrawable-seekable:1.0.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460297+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460297&template=1422628)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Vectordrawable-Seekable 1.0.0

### Version 1.0.0

May 1, 2024

`androidx.vectordrawable:vectordrawable-seekable:1.0.0`is released. Version 1.0.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..1c8a1d98b803c68e8a606f4a69874a9e402d30cb/vectordrawable/vectordrawable-seekable).

**Major features of 1.0.0**

`androidx.vectordrawable:vectordrawable-seekable`is a seekable alternative for`androidx.vectordrawable:vectordrawable-animated`with some additional features. It supports the same XML format as`AnimatedVectorDrawable`.

- Pause and resume
- Seek (setCurrentPlayTime)
- Enhanced callbacks

See[`SeekableAnimatedVectorDrawable`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/SeekableAnimatedVectorDrawable)for the details.

### Version 1.0.0-beta01

April 20, 2022

`androidx.vectordrawable:vectordrawable-seekable:1.0.0-beta01`is released with no changes since 1.0.0-alpha02.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c0a89ec374961b3015097ab307ebb8196dbe3888/vectordrawable/vectordrawable-seekable)

### VectorDrawable-Seekable Version 1.0.0-alpha02

August 19, 2020

`androidx.vectordrawable:vectordrawable-seekable:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..96eb302ee1740ba656c90c9fb27df3723a1a89c1/vectordrawable/vectordrawable-seekable)

**Bug Fixes**

- Update dependencies. ([aosp/1380259](https://android-review.googlesource.com/c/platform/frameworks/support/+/1380259))

### Vectordrawable-Seekable Version 1.0.0-alpha01

April 15, 2020

`androidx.vectordrawable:vectordrawable-seekable:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045/vectordrawable/vectordrawable-seekable)

**New Features**

`androidx.vectordrawable:vectordrawable-seekable`is a seekable alternative for`androidx.vectordrawable:vectordrawable-animated`with some additional features. It supports the same XML format as AnimatedVectorDrawable.

- Pause and resume
- Seek (setCurrentPlayTime)
- Enhanced callbacks

See[SeekableAnimatedVectorDrawable](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/SeekableAnimatedVectorDrawable)for the details.

## Version 1.2.0

### Version 1.2.0

May 1, 2024

`androidx.vectordrawable:vectordrawable:1.2.0`and`androidx.vectordrawable:vectordrawable-animated:1.2.0`are released. Version 1.2.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7e8073001f8db1bc9e0ff39615c67f390a6a6420..1c8a1d98b803c68e8a606f4a69874a9e402d30cb/vectordrawable).

### Version 1.2.0-beta01

April 20, 2022

`androidx.vectordrawable:vectordrawable:1.2.0-beta01`is released with no changes since 1.2.0-alpha02.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c0a89ec374961b3015097ab307ebb8196dbe3888/vectordrawable/vectordrawable)

### VectorDrawable Version 1.2.0-alpha02

August 19, 2020

`androidx.vectordrawable:vectordrawable:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24daa503442fcd3e44ada60cf1da41df2815c045..96eb302ee1740ba656c90c9fb27df3723a1a89c1/vectordrawable/vectordrawable)

**Bug Fixes**

- Update dependencies. ([aosp/1380259](https://android-review.googlesource.com/c/platform/frameworks/support/+/1380259))

### Vectordrawable Version 1.2.0-alpha01

April 15, 2020

`androidx.vectordrawable:vectordrawable:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7e8073001f8db1bc9e0ff39615c67f390a6a6420..24daa503442fcd3e44ada60cf1da41df2815c045/vectordrawable/vectordrawable)

**New Features**

- This release does not have any new public features. It is a necessary dependency when you use`androidx.vectordrawable:vectordrawable-seekable-1.0.0-alpha01`.

## Version 1.1.0

### Version 1.1.0

September 5, 2019

`androidx.vectordrawable:vectordrawable:1.1.0`and`androidx.vectordrawable:vectordrawable-animated:1.1.0`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/f9b2f91a3f91561b19c57efc84710ec995d5fc45..7e8073001f8db1bc9e0ff39615c67f390a6a6420/graphics).

**Important changes since 1.0.0**

**New features**

- `fillType`is now supported in`ClipPath`
- Tinting is now supported using`ColorStateLists`defined with theme attrs in`VectorDrawableCompat`

**Bug fixes**

- Fixed bug in rendering`VectorDrawables`with gradients ([b/117796719](https://issuetracker.google.com/issues/117796719))
- Fixed`getColorFilter()`that returned null even when it was set ([aosp/762198](https://android-review.googlesource.com/c/platform/frameworks/support/+/762198/))

### Version 1.1.0-rc01

July 2, 2019

`androidx.vectordrawable:vectordrawable:1.1.0-rc01`and`androidx.vectordrawable:vectordrawable-animated:1.1.0-rc01`are released with no changes from`1.1.0-beta02`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/75e93a025020288fd9cd22580aabbcd7b11b4fd9..f9b2f91a3f91561b19c57efc84710ec995d5fc45/graphics/drawable).

### Version 1.1.0-beta02

June 5, 2019

`androidx.vectordrawable:vectordrawable:1.1.0-beta02`and`androidx.vectordrawable:vectordrawable-animated:1.1.0-beta02`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/2c7181c30858d401daba909d0a9400d5fc8d16d9..75e93a025020288fd9cd22580aabbcd7b11b4fd9/graphics/drawable).

**Bug fixes**

- Change vectordrawable-animated package name ([aosp/963431](https://android-review.googlesource.com/c/platform/frameworks/support/+/963431/))

### Version 1.1.0-beta01

May 7, 2019

`androidx.vectordrawable:vectordrawable:1.1.0-beta01`and`androidx.vectordrawable:vectordrawable-animated:1.1.0-beta01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/b7c49c4fbaec3ab27903b27ba7a511a370a78643..2c7181c30858d401daba909d0a9400d5fc8d16d9/graphics/drawable).

**New features**

- `fillType`is now supported in`ClipPath`

### Version 1.1.0-alpha01

December 3, 2018

**New features**

- Support tinting using`ColorStateLists`defined with theme attrs in`VectorDrawableCompat`.

**Bug fixes**

- Fixed bug in rendering`VectorDrawables`with gradients ([aosp/790377](https://android-review.googlesource.com/c/platform/frameworks/support/+/790377/))
- Fixed`getColorFilter()`that returned null even when it was set ([aosp/762198](https://android-review.googlesource.com/c/platform/frameworks/support/+/762198/))

## Version 1.0.0

### Version 1.0.0

November 7, 2018

**New features**

- [`VectorDrawableCompat`](https://developer.android.com/reference/androidx/vectordrawable/graphics/drawable/VectorDrawableCompat)gains support for gradient and[`ColorStateList`](https://developer.android.com/reference/android/content/res/ColorStateList)fills and strokes.