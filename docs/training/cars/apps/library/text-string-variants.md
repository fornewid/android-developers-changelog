---
title: Add text string variants  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/apps/library/text-string-variants
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Add text string variants Stay organized with collections Save and categorize content based on your preferences.



Different car screen sizes may show different amounts of text. With Car App API
level 2 and later, you can specify multiple variants of a text string to best
fit the screen. To see where text variants are accepted, look for templates and
components that take a [`CarText`](/reference/androidx/car/app/model/CarText).

You can add text string variants to a `CarText` with the
[`CarText.Builder.addVariant()`](/reference/androidx/car/app/model/CarText.Builder#addVariant(java.lang.CharSequence)) method:

### Kotlin

```
val itemTitle = CarText.Builder("This is a very long string")
    .addVariant("Shorter string")
    ...
    .build()
```

### Java

```
CarText itemTitle = new CarText.Builder("This is a very long string")
 .addVariant("Shorter string")
 ...
 .build();
```

You can then use this `CarText`—for example, as the primary text of a
[`GridItem`](/reference/androidx/car/app/model/GridItem).

### Kotlin

```
GridItem.Builder()
    .addTitle(itemTitle)
    ...
    .build()
```

### Java

```
new GridItem.Builder()
    .addTitle(itemTitle)
    ...
    build();
```

Add strings in the order of from most to least preferred. For example, from
longest to shortest. The host picks the appropriate-length string depending
on the amount of space available on the car screen.

[Next

Add inline CarIcons for rows

arrow\_forward](/training/cars/apps/library/inline-car-icons)