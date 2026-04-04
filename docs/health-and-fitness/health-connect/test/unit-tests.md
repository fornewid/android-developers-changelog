---
title: https://developer.android.com/health-and-fitness/health-connect/test/unit-tests
url: https://developer.android.com/health-and-fitness/health-connect/test/unit-tests
source: md.txt
---

| **Note:** The Health Connect Testing library is in alpha, so future versions might include breaking changes.

The Health Connect Testing library (`androidx.health.connect:connect-testing`)
simplifies the creation of automated tests. You can use this library to verify
the behavior of your application and validate that it responds correctly to
uncommon cases, which are hard to test manually.

You can use the library to create [local unit tests](https://developer.android.com/training/testing/local-tests), which typically verify
the behavior of the classes in your app that interact with the [Health Connect
client](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient).

To start using the library, add it as a test dependency:  

     testImplementation("androidx.health.connect:connect-testing:1.0.0-alpha03")

The entry point to the library is the `FakeHealthConnectClient` class, which you
use in tests to replace the `HealthConnectClient`. The `FakeHealthConnectClient`
has the following features:

- An in-memory representation of records, so you can insert, remove, delete and read them
- Generation of change tokens and change tracking
- Pagination for records and changes
- Aggregation responses are supported with stubs
- Allows any function to throw exceptions
- A `FakePermissionController` that can be used to emulate permissions checks

To learn more about replacing dependencies in tests, read
[Dependency Injection in Android](https://developer.android.com/training/dependency-injection). To know more about fakes, read
[Using test doubles in Android](https://developer.android.com/training/testing/fundamentals/test-doubles).

For example, if the class that interacts with the client is called
`HealthConnectManager` and it takes a `HealthConnectClient` as a dependency, it
would look like:  

    class HealthConnectManager(
        private val healthConnectClient: HealthConnectClient,
        ...
    ) { }

In tests, you can pass a fake to your class under test instead:  

    import androidx.health.connect.client.testing.ExperimentalTestingApi
    import androidx.health.connect.client.testing.FakeHealthConnectClient
    import kotlinx.coroutines.test.runTest

    @OptIn(ExperimentalTestingApi::class)
    class HealthConnectManagerTest {

        @Test
        fun readRecords_filterByActivity() = runTest {
            // Create a Fake with 2 running records.
            val fake = FakeHealthConnectClient()
            fake.insertRecords(listOf(fakeRunRecord1, fakeBikeRecord1))

            // Create a manager that depends on the fake.
            val manager = HealthConnectManager(fake)

            // Read running records only.
            val runningRecords = manager.fetchReport(activity = Running)

            // Verify that the records were filtered correctly.
            assertTrue(runningRecords.size == 1)
        }
    }

This test verifies that the fictional `fetchReport` function in
`HealthConnectManager` properly filters records by activity.

## Verify exceptions

Almost every call to `HealthConnectClient` can throw exceptions. For example,
the documentation for `insertRecords` mentions these exceptions:

- `@throws android.os.RemoteException` for any IPC transportation failures.
- `@throws SecurityException` for requests with unpermitted access.
- `@throws java.io.IOException` for any disk I/O issues.

These exceptions cover cases like a bad connection or no space left on the
device. Your app must react correctly to these runtime issues, as they can
happen at any time.  

    import androidx.health.connect.client.testing.stubs.stub

    @Test
    fun addRecords_throwsRemoteException_errorIsExposed() {
        // Create Fake that throws a RemoteException
        // when insertRecords is called.
        val fake = FakeHealthConnectClient()
        fake.overrides.insertRecords = stub { throw RemoteException() }

        // Create a manager that depends on the fake.
        val manager = HealthConnectManager(fake)

        // Insert a record.
        manager.addRecords(fakeRunRecord1)

        // Verify that the manager is exposing an error.
        assertTrue(manager.errors.size == 1)
    }

## Aggregation

Aggregation calls don't have fake implementations. Instead, aggregation calls
use stubs that you can program to behave in a certain way. You can access the
stubs through the `overrides` property of the `FakeHealthConnectClient`.

For example, you can program the aggregate function to return a specific result:  

    import androidx.health.connect.client.testing.AggregationResult
    import androidx.health.connect.client.records.HeartRateRecord
    import androidx.health.connect.client.records.ExerciseSessionRecord
    import java.time.Duration

    @Test
    fun aggregate() {
        // Create a fake result.
        val result =
            AggregationResult(metrics =
                buildMap {
                    put(HeartRateRecord.BPM_AVG, 74.0)
                    put(
                        ExerciseSessionRecord.EXERCISE_DURATION_TOTAL,
                        Duration.ofMinutes(30)
                    )
                }
            )

        // Create a fake that always returns the fake
        // result when aggregate() is called.
        val fake = FakeHealthConnectClient()
        fake.overrides.aggregate = stub(result)

Then, you can verify that your class under test, `HealthConnectManager` in this
case, processed the result correctly:  

    // Create a manager that depends on the fake.
    val manager = HealthConnectManager(fake)
    // Call the function that in turn calls aggregate on the client.
    val report = manager.getHeartRateReport()

    // Verify that the manager is exposing an error.
    assertThat(report.bpmAverage).isEqualTo(74.0)

## Permissions

The testing library includes a `FakePermissionController`, which can be passed
as a dependency to `FakeHealthConnectClient`.

Your subject under test can use the `PermissionController` accessed through
the `permissionController` property of the `HealthConnectClient` interface
to check for permissions. This is typically done before every call to the
client.

To test this functionality, you can set which permissions are available using
the `FakePermissionController`:  

    import androidx.health.connect.client.testing.FakePermissionController

    @Test
    fun newRecords_noPermissions_errorIsExposed() {
        // Create a permission controller with no permissions.
        val permissionController = FakePermissionController(grantAll = false)

        // Create a fake client with the permission controller.
        val fake = FakeHealthConnectClient(permissionController = permissionController)

        // Create a manager that depends on the fake.
        val manager = HealthConnectManager(fake)

        // Call addRecords so that the permission check is made.
        manager.addRecords(fakeRunRecord1)

        // Verify that the manager is exposing an error.
        assertThat(manager.errors).hasSize(1)
    }

| **Caution:** You should also have tests to verify correct behavior when the client throws a SecurityException. Users can revoke permissions at any time.

## Pagination

Pagination is a very common source of bugs, so `FakeHealthConnectClient`
provides mechanisms to help you verify that your paging implementation for
records and changes behaves correctly.

Your subject under test, `HealthConnectManager` in our example, can specify the
page size in the `ReadRecordsRequest`:  

    fun fetchRecordsReport(pageSize: Int = 1000) }
        val pagedRequest =
            ReadRecordsRequest(
                timeRangeFilter = ...,
                recordType = ...,
                pageToken = page1.pageToken,
                pageSize = pageSize,
            )
        val page = client.readRecords(pagedRequest)
        ...

Setting the page size to a small value, such as 2, lets you test
pagination. For example, you can insert 5 records so that `readRecords` returns
3 different pages:  

    @Test
    fun readRecords_multiplePages() = runTest {

        // Create a Fake with 2 running records.
        val fake = FakeHealthConnectClient()
        fake.insertRecords(generateRunningRecords(5))

        // Create a manager that depends on the fake.
        val manager = HealthConnectManager(fake)

        // Read records with a page size of 2.
        val report = manager.generateReport(pageSize = 2)

        // Verify that all the pages were processed correctly.
        assertTrue(report.records.size == 5)
    }

## Test data

The library doesn't include APIs to generate fake data yet, but you can use the
data and generators used by the library in [Android Code Search](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:health/connect/connect-testing/src/test/java/androidx/health/connect/client/testing/testdata/TestData.kt;l=1).

For mocking metadata values in tests, you can use
[`MetadataTestHelper`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:health/connect/connect-testing/src/main/java/androidx/health/connect/client/testing/MetadataTestHelper.kt). This provides the
`populatedWithTestValues()` extension function, which simulates Health Connect
populating metadata values during record insertion.

## Stubs

The `overrides` property of `FakeHealthConnectClient` lets you program (or
*stub out* ) any of its functions so that they throw exceptions when called.
Aggregation calls can also return arbitrary data, and it supports enqueuing
multiple responses. See [`Stub`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/testing/stubs/Stub) and [`MutableStub`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/testing/stubs/MutableStub) for more information.

## Summary of edge cases

- Verify that your app behaves as expected when the client throws exceptions. Check the documentation of each function to figure out what exceptions you should check.
- Verify that every call you make to the client is preceded by the proper permissions check.
- Verify your pagination implementation.
- Verify what happens when you fetch multiple pages but one has an expired token.