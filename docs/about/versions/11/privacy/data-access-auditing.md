---
title: https://developer.android.com/about/versions/11/privacy/data-access-auditing
url: https://developer.android.com/about/versions/11/privacy/data-access-auditing
source: md.txt
---

To provide more transparency into how your app and its dependencies access
private data from users, Android 11 introduces [data access
auditing](https://developer.android.com/guide/topics/data/audit-access). By having insights from this
process, you can better identify potentially unexpected data access.

Your app can register an instance of
[`AppOpsManager.OnOpNotedCallback`](https://developer.android.com/reference/android/app/AppOpsManager.OnOpNotedCallback), which can perform
actions each time one of the following events occurs:

- Your app's code accesses private data. To help you determine which logical part of your app invoked the event, you can audit data access by attribution tag.
- Code in a dependent library or SDK accesses private data.

## Additional resources

For more information about data access auditing, view the following materials:

### Blog posts

- [New Android 11 tools to make apps more private and
  stable](https://medium.com/androiddevelopers/new-android-11-tools-to-make-apps-more-private-and-stable-c9dcea0af415)