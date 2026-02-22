---
title: https://developer.android.com/health-and-fitness/health-connect/data-format
url: https://developer.android.com/health-and-fitness/health-connect/data-format
source: md.txt
---

Data types in Health Connect are stored in objects that are subclasses of
[`Record`](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/Record).

For each data type, there are associated fields that are either generic such as
`time` and `zoneOffset`, or specific such as `title`, `count`, and `percentage`.
Some fields use basic types---such as long, double, or string---while others use
complex types like enumerations and classes like [`Instant`](https://developer.android.com/reference/java/time/Instant) and
[`ZoneOffset`](https://developer.android.com/reference/java/time/ZoneOffset). The attributes of these fields can be required or
optional. Some attributes are read-only, and some attributes are clamped to a
specific range of values.

For the full list of available data types and their fields, refer to the classes
in [Jetpack](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/package-summary#classes).

## Metadata attributes

Data in the Health Connect API also includes [metadata](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/Metadata) attributes
described in the following list:

- **Health Connect ID:** Each point of data is assigned with a unique identifier (UID) upon creation. This is useful for standard read and write operations. See [Health Connect ID](https://developer.android.com/health-and-fitness/health-connect/data-format#health-connect-id) for more details.
- **Last modified time:** This marks the timestamp the last instance a record has an update. It's automatically generated on the first creation of the record or on every update.
- **Data origin:** Health Connect stores information about the app where the data came from. It contains the package name of that origin, which is automatically added upon creation.
- **Device:** Health Connect stores information about the device where the data came from. It contains the manufacturer and model of that device, which you manually supply the value.
- **Client ID:** Health Connect provides Client IDs so that client apps can refer to data using their own IDs, which helps with conflict resolution and makes syncing easier. This is supplied to the record manually.
- **Client record version:** Along with the Client ID, Health Connect provides versioning to help tracking changes during data syncing. This is supplied to the record manually.
- **Recording method:** Health Connect lets you understand how data is recorded. These methods include apps recording data passively (automatically), and users recording data actively or manually.

## Health Connect ID

Health Connect assigns unique identifiers (UIDs) to newly inserted data objects,
which identify data objects and distinguish them from others. Health Connect IDs
are useful in read or write requests. Health Connect IDs aren't identical to
Client IDs. A client app assigns Client IDs, while Health Connect exclusively
assigns Health Connect IDs.

**Keep in mind** of the following notes when working with Health Connect IDs:

- Sessions have a single Health Connect ID, but data within sessions have their own Health Connect IDs.
- Health Connect IDs aren't tied or related to timestamps.
- Some use cases might require storing a specific Health Connect ID during a workflow. For example, a specific ID is required to retrieve and show to a user the data entry that they just logged.

## Time in Health Connect

All data written to Health Connect must specify the zone offset information.
Specifying the zone offset enables apps to read the data to represent it in
civil time. Civil time is the time that is local and relevant to the user,
but not necessarily in Coordinated Universal Time (UTC).

In rare circumstances, the zone offset might not be available. When this occurs
in Android 14 (API Level 34), Health Connect sets the zone offset based on the
system default time zone of the device. In Android 13 and lower versions
(API Level 33 and lower), it's possible to write to Health Connect without
specifying any zone offset information, which must be avoided whenever possible.

### Time and zone setting

Specifying zone offset information while writing data provides time zone
information when reading data in Health Connect. However, it may fail to do so
in certain situations, such as when the zone offset isn't provided. Your app
needs to be prepared to deal with both kinds of data, in a way that makes sense
for your specific circumstances.