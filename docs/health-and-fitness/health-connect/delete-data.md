---
title: https://developer.android.com/health-and-fitness/health-connect/delete-data
url: https://developer.android.com/health-and-fitness/health-connect/delete-data
source: md.txt
---

Deleting data is a key part of the CRUD operations in Health Connect. This guide
shows you how you can delete records in two ways.
| **Tip:** For further guidance on deleting data, take a look at the [Android Developer video for reading and writing data](https://www.youtube.com/watch?v=NAx7Gv_Hk7E&t=299) in Health Connect.

## Delete using Record IDs

You can delete records using a list of unique identifiers such as the Record ID
and your app's Client Record ID. Use [`deleteRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,kotlin.collections.List,kotlin.collections.List)), and
supply it with two lists of `Strings`, one for the Record IDs and one for the
Client IDs. If you only have one of the IDs available, you can set `emptyList()`
on the other list.

The following code example shows how to delete Steps data using its IDs:  

    suspend fun deleteStepsByUniqueIdentifier(
        healthConnectClient: HealthConnectClient,
        idList: List<String>
    ) {
        try {
            healthConnectClient.deleteRecords(
                StepsRecord::class,
                idList = idList,
                clientRecordIdsList = emptyList()
            )
        } catch (e: Exception) {
            // Run error handling here
        }
    }

## Delete using a time range

You can also delete data using a time range as your filter.
Use [`deleteRecords`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient#deleteRecords(kotlin.reflect.KClass,androidx.health.connect.client.time.TimeRangeFilter)), and supply it with a
[`TimeRangeFilter`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/time/TimeRangeFilter) object that takes
a start and end timestamp values.

The following code example shows how to delete Steps data of a specific time:  

    suspend fun deleteStepsByTimeRange(
        healthConnectClient: HealthConnectClient,
        startTime: Instant,
        endTime: Instant
    ) {
        try {
            healthConnectClient.deleteRecords(
                StepsRecord::class,
                timeRangeFilter = TimeRangeFilter.between(startTime, endTime)
            )
        } catch (e: Exception) {
            // Run error handling here
        }
    }