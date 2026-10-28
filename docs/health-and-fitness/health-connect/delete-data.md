---
title: Delete data  |  Android health & fitness  |  Android Developers
url: https://developer.android.com/health-and-fitness/health-connect/delete-data
source: html-scrape
---

Google Fit APIs will be supported until the end of 2026. To learn about the recommended migration paths, see [Migration guide](/health-and-fitness/health-connect/migration/fit).

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Health & fitness dev center](https://developer.android.com/health-and-fitness)
* [Health Connect Guides](https://developer.android.com/health-and-fitness/health-connect)

# Delete data Stay organized with collections Save and categorize content based on your preferences.





Deleting data is a key part of the CRUD operations in Health Connect. This guide
shows you how you can delete records in two ways.

**Tip:** For further guidance on deleting data, take a look at the
[Android Developer video for reading and writing data](https://www.youtube.com/watch?v=NAx7Gv_Hk7E&t=299)
in Health Connect.

## Delete using Record IDs

You can delete records using a list of unique identifiers such as the Record ID
and your app's Client Record ID. Use [`deleteRecords`](/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,kotlin.collections.List,kotlin.collections.List)), and
supply it with two lists of `Strings`, one for the Record IDs and one for the
Client IDs. If you only have one of the IDs available, you can set `emptyList()`
on the other list.

The following code example shows how to delete Steps data using its IDs:

```
try {
    healthConnectClient.deleteRecords(
        recordType = StepsRecord::class,
        recordIdsList = idList,
        clientRecordIdsList = emptyList<String>()
    )
} catch (e: Exception) {
    // Run error handling here
}

HealthConnectManager.kt
```

## Delete using a time range

You can also delete data using a time range as your filter.
Use [`deleteRecords`](/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,androidx.health.connect.client.time.TimeRangeFilter)), and supply it with a
[`TimeRangeFilter`](/reference/kotlin/androidx/health/connect/client/time/TimeRangeFilter) object that takes
a start and end timestamp values.

The following code example shows how to delete Steps data of a specific time:

```
try {
    healthConnectClient.deleteRecords(
        StepsRecord::class,
        timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
    )
} catch (e: Exception) {
    // Run error handling here
}

HealthConnectManager.kt
```

[Previous

arrow\_back

Read aggregated data](/health-and-fitness/health-connect/aggregate-data)

[Next

Synchronize data

arrow\_forward](/health-and-fitness/health-connect/sync-data)