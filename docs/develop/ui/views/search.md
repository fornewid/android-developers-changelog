---
title: https://developer.android.com/develop/ui/views/search
url: https://developer.android.com/develop/ui/views/search
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose.  
[Search bar →](https://developer.android.com/develop/ui/compose/components/search-bar)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

Search is a core user feature on Android. Users must be able
to search any data that is available to them, whether the content is located on the device or
the internet. To help create a consistent search experience for users, Android provides a
search framework that helps you implement search for your application.  
![](https://developer.android.com/static/images/search/search-suggest-custom.png)

**Figure 1.** A search dialog with custom
search suggestions.

The search framework offers two modes of search input: a search dialog at the top of the
screen or a search widget ([SearchView](https://developer.android.com/reference/android/widget/SearchView)) that you can embed in your activity
layout. In either case, the Android system assists your search implementation by
delivering search queries to a specific activity that performs searches. You can also enable
the search dialog or widget to provide search suggestions as the user types. Figure 1 shows an
example of the search dialog with optional search suggestions.

Once you set up either the search dialog or the search widget, you can do the following:

- Enable voice search.
- Provide search suggestions based on recent user queries.
- Provide custom search suggestions that match actual results in your application data.
- Offer your application's search suggestions in the system-wide Quick Search Box.

**Note** : The search framework does *not* provide APIs to
search your data. To perform a search, you need to use APIs appropriate for your data. For example,
if your data is stored in an SQLite database, use the [android.database.sqlite](https://developer.android.com/reference/android/database/sqlite/package-summary)
APIs to perform searches.

<br />


Also, there is no guarantee that a device provides a dedicated SEARCH button that invokes the
search interface in your application. When using the search dialog or a custom interface, you
must provide a search button in your UI that activates the search interface. For more
information, see [Invoke the search
dialog](https://developer.android.com/develop/ui/views/search/search-dialog#InvokingTheSearchDialog).

The following pages show you how to use Android's framework to implement search:

**[Create a search interface](https://developer.android.com/develop/ui/views/search/search-dialog)**
:   How to set up your application to use the search dialog or search widget.

**[Add recent query
suggestions](https://developer.android.com/develop/ui/views/search/adding-recent-query-suggestions)**
:   How to provide suggestions based on queries previously used.

**[Add custom suggestions](https://developer.android.com/develop/ui/views/search/adding-custom-suggestions)**
:   How to provide suggestions based on custom data from your application and offer them
    in the system-wide Quick Search Box.

**[Searchable configuration](https://developer.android.com/develop/ui/views/search/searchable-config)**
:   A reference document for the searchable configuration file. The other
    documents also discuss the configuration file in terms of specific behaviors.

## Protect user privacy

When you implement search in your application, take steps to protect the user's
privacy. Many users consider their activities on their phone---including searches---to
be private information. To protect users' privacy, abide by the following
principles:

- **Don't send personal information to servers‐and if you must, don't log it.**

  Personal information is any information that can personally identify your users, such as their
  names, email addresses, billing information, or other data that can be reasonably linked to such
  information. If your application implements search with the assistance of a server, avoid sending
  personal information along with the search queries. For example, if you are searching for businesses
  near a ZIP code,
  you don't need to send the user ID as well; send only the ZIP code to the server. If you must
  send personal information, avoid logging it. If you must log it, protect that data
  very carefully and erase it as soon as possible.
- **Provide users with a way to clear their search history.**

  The search framework helps your application provide context-specific suggestions while the user
  types. Sometimes these
  suggestions are based on previous searches or other actions taken by the user in an earlier
  session. A user might not want previous searches to be revealed to other device users. If your
  application provides suggestions that
  can reveal previous search activities, implement a way for the user to clear their
  search history. If you are using [SearchRecentSuggestions](https://developer.android.com/reference/android/provider/SearchRecentSuggestions),
  you can call the
  [clearHistory()](https://developer.android.com/reference/android/provider/SearchRecentSuggestions#clearHistory())
  method. If you are implementing custom suggestions, you need to provide a similar "clear history"
  method in your content provider that the user can execute.