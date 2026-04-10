---
title: https://developer.android.com/training/cars/apps/library/refresh-template
url: https://developer.android.com/training/cars/apps/library/refresh-template
source: md.txt
---

Your app can request the content of a `Screen` to be invalidated by calling the
[`Screen.invalidate`](https://developer.android.com/reference/androidx/car/app/Screen#invalidate()) method. The host subsequently calls back into your
app's [`Screen.onGetTemplate`](https://developer.android.com/reference/androidx/car/app/Screen#onGetTemplate()) method to retrieve the template with the new
contents.

When refreshing a `Screen`, it's important to understand the specific content
in the template that can be updated so the host doesn't count the new template
against the template quota. To learn more, see [Template restrictions](https://developer.android.com/training/cars/apps/library/template-restrictions).

We recommend that you structure your screens to have a one-to-one mapping
between a `Screen` and the type of template it returns through its
`onGetTemplate` implementation.