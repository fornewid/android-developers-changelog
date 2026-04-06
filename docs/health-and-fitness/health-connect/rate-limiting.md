---
title: https://developer.android.com/health-and-fitness/health-connect/rate-limiting
url: https://developer.android.com/health-and-fitness/health-connect/rate-limiting
source: md.txt
---

To maintain optimal system stability and performance, Health Connect imposes
rate limits on client connections to the Health Connect API.

This guide outlines the limits imposed on read and write API operations in
Health Connect, and how to avoid rate limiting through efficient app design.

## API limits

Limits are placed on both foreground and background API operations as **fixed
request rate quotas**.

Rate and memory limits are variable based on the type of operation your app is
performing, and whether that operation occurs in the foreground or background.

### Read and changelog limits

For read and changelog limits, Health Connect imposes two limits on the number
of API calls available to your app:

- A periodic limit on the number of API calls your app can make to the API.
- A daily limit on the number of API calls your app can make.

### Insert, update and delete limits

Health Connect places four distinct limits on insertion, update and deletion
operations:

- A periodic limit on the number of calls your app can make to the API.
- A daily limit on the number of calls your app can make to the API.
- A memory limit for bulk insertions.
- A memory limit for single record insertions.

## Best practices

We recommend that apps interact with the Health Connect API in a way that
minimizes battery use, maintains optimal system health and promotes efficient
data management across all CRUD operations.

Here are some best practice guidelines to adhere to.

### Background API calls

Battery usage for background operations reduces the user experience and raises
questions regarding [data privacy](https://developer.android.com/guide/health-and-fitness/health-connect/develop/read-data#foreground-restriction).

As such, background rate limiting is stricter than foreground rate limiting.
It's therefore important to limit the amount of API calls your app carries out
in the background.

### Exception handling

If your app experiences an exception when writing data to Health Connect, we
recommend retrying from where the exception occurred.

Don't delete all the data in question and retry the entire write request.
This approach eats into your insert quota, reduces performance, and has a
negative impact on battery life.

### Changelog handling

To minimize the risk of your app being rate limited, you should utilize
[changelog handling](https://developer.android.com/guide/health-and-fitness/health-connect/develop/sync-data#pull-data) to synchronize your database with data from Health
Connect, rather than over-relying on raw read requests.