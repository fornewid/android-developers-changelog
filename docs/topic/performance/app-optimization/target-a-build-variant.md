---
title: Target a build variant  |  App quality  |  Android Developers
url: https://developer.android.com/topic/performance/app-optimization/target-a-build-variant
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App quality](https://developer.android.com/quality)
* [Technical quality](https://developer.android.com/quality/technical)

# Target a build variant Stay organized with collections Save and categorize content based on your preferences.




If you have different versions of your app based on different build variants,
create custom [keep rules](/topic/performance/app-optimization/add-keep-rules) for each variant. For example, if you have a free
tier and a paid tier of your app with different features and dependencies, each
tier should have its own keep rules.

## Create keep rules

To create keep rules that are specific to a build variant, add the
`proguardFiles` property in the corresponding *flavor* block under
`productFlavors`. For example, the following build script adds the rules file
`flavor2‑rules.pro` to the `flavor2` product flavor:

### Kotlin

```
android {
...
buildTypes {
    getByName("release") {
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro"
        )
    }
}
flavorDimensions.add("version")
    productFlavors {
        create("flavor1") {
            ...
        }
        create("flavor2") {
            proguardFile("flavor2-rules.pro")
        }
    }
}
```

### Groovy

```
android {
    ...
    buildTypes {
        release {
            minifyEnabled = true
            shrinkResources = true
            proguardFiles
                getDefaultProguardFile('proguard-android-optimize.txt'),
                'proguard-rules.pro'
        }
    }
    flavorDimensions "version"
    productFlavors {
        flavor1 {
            ...
        }
        flavor2 {
            proguardFile 'flavor2-rules.pro'
        }
    }
}
```

**Note:** The `flavor2` product flavor uses rules from three rules
files—`flavor2‑rules.pro`,
`proguard‑rules.pro`, and
`proguard‑android‑optimize.txt`—because the script
applies the rules from the release block.

## Additional resources

* [Customize which resources to keep](/topic/performance/app-optimization/customize-which-resources-to-keep) — Learn how to add keep rules
  for resources.