---
title: https://developer.android.com/training/cars/apps/library/constraints-api
url: https://developer.android.com/training/cars/apps/library/constraints-api
source: md.txt
---

Different cars can allow for differing numbers of
[`Item`](https://developer.android.com/reference/androidx/car/app/model/Item) instances to be displayed to the user at a time. Use the
[`ConstraintManager`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager) to check the content limit at runtime and to set the
appropriate number of items in your templates.
| **Important:** The host sets these limits, which can't be modified by client apps. To see minimum values, see the [`integers.xml`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:car/app/app/src/main/res/values/integers.xml) resource file.

Get a `ConstraintManager` from the `CarContext`:

### Kotlin

    val manager = carContext.getCarService(ConstraintManager::class.java)

### Java

    ConstraintManager manager = getCarContext().getCarService(ConstraintManager.class);

Query the retrieved `ConstraintManager` object for the relevant content limit.
For example, to get the number of items that can be displayed in a grid, call
[`getContentLimit`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager#getContentLimit(int)) with [`CONTENT_LIMIT_TYPE_GRID`](https://developer.android.com/reference/androidx/car/app/constraints/ConstraintManager#CONTENT_LIMIT_TYPE_GRID()):

### Kotlin

    val gridItemLimit = manager.getContentLimit(ConstraintManager.CONTENT_LIMIT_TYPE_GRID)

### Java

    int gridItemLimit = manager.getContentLimit(ConstraintManager.CONTENT_LIMIT_TYPE_GRID);