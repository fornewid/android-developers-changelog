---
title: https://developer.android.com/training/cars/platforms/automotive-os/android-intents-automotive
url: https://developer.android.com/training/cars/platforms/automotive-os/android-intents-automotive
source: md.txt
---

# Google Maps for Android Automotive Intents

Through Android intents, you can launch navigation in Google Maps for Android Automotive.
| **Note:** Use of the third-party interoperability APIs (which interact with Google services) is subject to[Google APIs Terms of Services](https://developers.google.com/terms). Make sure your application complies with all applicable Google policies.

## Overview

This page describes the intents you can use with Google Maps for Android Automotive. For detailed Android developer documentation, see the following:

- [Intents and Intent Filters](https://developer.android.com/guide/components/intents-filters)
- [Intents common to the Android platform](https://developer.android.com/guide/components/intents-common)

## Intent requests

To launch Google Maps for Android Automotive with an intent, you must first create an[`Intent`](https://developer.android.com/reference/android/content/Intent)object, specifying its action, URI, and package.

- **Action.** All Google Maps intents are called as a View action,`ACTION_VIEW`.

- **URI.** Google Maps intents use[URI encoded strings](https://developer.android.com/training/cars/platforms/automotive-os/android-intents-automotive#urlencoding)that specify a chosen action, along with some data with which to perform the action.

- **Package.** Calling`setPackage("com.google.android.apps.maps")`ensures that the Google Maps app for Android handles the Intent. If the package isn't set, the system determines which apps can handle the Intent. If multiple apps are available, you may be asked which app you would like to use.

After creating the Intent, you can request that the system launch the related app in a number of ways. A common method is to pass the Intent to the[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))method. The system will launch the necessary app, in this case, Google Maps, and start the corresponding[`Activity`](https://developer.android.com/reference/android/app/Activity).  

    // Create a Uri from an intent string. Use the result to create an Intent.
    Uri mapIntentUri =
    Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia");
    // Create an Intent from mapIntentUri. Set the action to ACTION_VIEW
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    // Make the Intent explicit by setting the Google Maps package
    mapIntent.setPackage("com.google.android.apps.maps");
    // Attempt to start an activity that can handle the Intent
    startActivity(mapIntent);

If the system can't identify an app that can respond to the Intent, your app may crash. For this reason, first verify that a receiving application is installed before you present one of these intents to a user.

To verify that an app is available to receive the intent, call[`resolveActivity()`](https://developer.android.com/reference/android/content/Intent#resolveActivity(android.content.pm.PackageManager))on your[`Intent`](https://developer.android.com/reference/android/content/Intent)object. If the result is non-null, there is at least one app that can handle the intent and it's safe to call[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent)). If the result is null, you shouldn't use the intent and, if possible, disable the feature that invokes the intent.  

    if (mapIntent.resolveActivity(getPackageManager()) != null) {
    ...
    }

For example, to launch turn-by-turn navigation to Taronga Zoo in Sydney, you can use the following code:  

    Uri mapIntentUri = Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    if (mapIntent.resolveActivity(getPackageManager()) != null) {
    startActivity(mapIntent);
    }

## URI encoded query strings

All strings passed to the Google Maps intents must be URI encoded. For example, the string "1st \& Pike, Seattle" should become`1st%20%26%20Pike%2C%20Seattle`. Spaces in the string can be encoded with`%20`or replaced with the plus sign (+).

You can use the`android.net.Uri encode()`method to encode your strings. For example:  

    Uri mapIntentUri = Uri.parse("google.navigation:q=" + Uri.encode("1st & Pike, Seattle"));

## Display a map

Use the`geo:`intent to display a map at a specified location and zoom level. For example:

`geo:latitude,longitude?z=zoom`

### Parameters

- `latitude`and`longitude`set the center point of the map.

- `z`optionally sets the initial zoom level of the map. Accepted values range from 0 (the whole world) to 21 (individual buildings). The upper limit can vary depending on the map data available at the selected location.

### Example

    // Creates an intent that will load a map of San Francisco
    Uri gmmIntentUri = Uri.parse("geo:37.7749,-122.4194");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

## Search for a location

Use this intent to display search queries within a specified viewport:  

    geo:latitude,longitude?q=query
    geo:0,0?q=my+street+address

### Parameters

In addition to the parameters used to display a map, Search supports the this parameter:

- `q`defines the places to highlight on the map. The`q`parameter is required for all Search requests. It accepts a location as either a place name or address. The string should be URL-escaped, so an address such as "City Hall, New York, NY" should be converted to`City+Hall%2CNew+York%2CNY`.

| **Note:** If the intent URI is specified with the`q`parameter`geo:0,0?q=query`and the query returns a single value, the query result is automatically set as the destination.

### Bias search results with coordinates

When searching for a very specific location, the latitude and longitude aren't strictly required if included in the`q`parameter. However, if you don't know the exact address or the query is ambiguous, you can attempt to bias the results of the search by specifying a coordinate. For example, performing an address search for "Main Street" might return too many results:  

    // Searching for "101 Main Street" with no lat/long might return too many results
    Uri gmmIntentUri = Uri.parse("geo:0,0?q=101+main+street");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

Adding a latitude and longitude to the intent URI biases the results toward a particular area:  

    // Searches for "101 Main Street" near San Francisco
    Uri gmmIntentUri = Uri.parse("geo:37.7749,-122.4194?q=101+main+street");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

### Search along route

If a search intent`geo:latitude,longitude?q=query`is sent during navigation, it triggers a search along the route and the latitude and longitude are ignored.

### Search for predefined categories

To support integration with the vehicle, Google Maps in the car supports an intent that displays these predefined categories:

|             Category              |      Intent category encoding       |
|-----------------------------------|-------------------------------------|
| Gas station                       | `gas_station`                       |
| Restaurant                        | `restaurant`                        |
| Cafe                              | `cafe`                              |
| Parking                           | `parking`                           |
| Electric vehicle charging station | `electric_vehicle_charging_station` |

The category intent is in the form of`geo:lat,lng?c=category`.

Use`c=<pre-defined category>`regardless of the user's locale settings. Google Maps displays relevant results in the appropriate locale for this category. For example:  

    // Search for gas stations nearby
    Uri gmmIntentUri = Uri.parse("geo:0,0?c=gas_station");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

### Other categorical search

If you pass a general search term (such as "restaurants" or "coffee shops") in the user's locale, Google Maps for Android Automotive searches for business listings matching the criteria. If a specific latitude and longitude are provided in the`geo:`intent, the search is centered around that location. If no location is specified (e.g.,`geo:0,0`), Google Maps tries to find nearby business listings. For example:  

    // Search for restaurants nearby
    Uri gmmIntentUri = Uri.parse("geo:0,0?q=restaurants");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

You can further bias the search results by specifying a zoom parameter along with the query string. In the following example, adding a zoom of`10`tries to find restaurants at a city level instead of nearby:  

    Uri gmmIntentUri = Uri.parse("geo:37.7749,-122.4194?z=10&q=restaurants");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

## Launch turn-by-turn navigation

For documentation on launching turn-by-turn navigation on other Android devices, see[Launch turn-by-turn navigation in Google Maps Intents for Android](https://developer.android.com/guide/components/google-maps-intents#launch-turn-by-turn-navigation).

Use this intent to launch Google Maps navigation with turn-by-turn directions to one or several addresses or coordinates specified. Directions are always given from the user's current location.  

    google.navigation:q=a+street+address
    google.navigation:q=latitude,longitude
    google.navigation:place=placename

### Parameters

To launch navigation, use`place`or`q`with`waypoints`, which is optional. To optionally mark a waypoint as a charging station, see[Send an electric vehicle trip plan to Google Maps](https://developer.android.com/training/cars/platforms/automotive-os/android-intents-automotive#charge).

- `q`sets the endpoint for navigation searches. This can be a latitude and longitude or a query formatted address. If it is a query string that returns more than one result, the first result will be selected.

- `place`sets the endpoint to home or work. Specify home to navigate to the user's home, and work to navigate to the user's workplace.

- `avoid`sets features the route should try to avoid.`avoid`is optional and can be set to one or more of:

  - `t`for tolls
  - `h`for highways
  - `f`for ferries
- `waypoints`specifies one or more intermediary places to route directions to the final destination specified by`q`. You can specify multiple waypoints by using the pipe character (`|`) to separate places---for example,`Berlin,Germany|Paris,France`. You can use as many waypoints as needed. The waypoints will be added to the route in the same order that they are listed in the URL. Each waypoint can either be an address or comma-separated latitude and longitude coordinates; and, you can have addresses and latitude and longitude coordinates in the same intent. Strings should be[URL-escaped](https://developers.google.com/maps/url-encoding), so waypoints like "Berlin,Germany\|Paris,France" should be converted to`Berlin%2CGermany%7CParis%2CFrance`.

### Examples

This Intent will request turn-by-turn navigation to Taronga Zoo, in Sydney, Australia:  

    Uri mapIntentUri = Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

If you prefer not to pay tolls or ride a ferry, you can request routing that tries to avoid these situations:  

    Uri mapIntentUri = Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia&avoid=tf");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

Or if you'd rather navigate to your home, use:  

    Uri mapIntentUri = Uri.parse("google.navigation:place=home");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

To launch turn-by-turn navigation to the following three addresses in order, pass Taronga Zoo as the final destination`q`, and Google Sydney and Sydney Opera House as the waypoints:

1. Google Sydney

2. Sydney Opera House

3. Taronga Zoo, Sydney Australia

    Uri mapIntentUri = Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia&waypoints=Google+Sydney%7CSydney+Opera+House");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

Similar to`q`, you can represent any of the waypoints by a comma-separated latitude and longitude instead of an address. For example, to launch the same navigation while passing latitude longitude for Sydney Opera House instead of the address:  

    Uri mapIntentUri = Uri.parse("google.navigation:q=Taronga+Zoo,+Sydney+Australia&waypoints=Google+Sydney%7C-33.856159,151.215256");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

## Send an electric vehicle trip plan to Google Maps

Use this multi-destination navigation intent to specify some destinations as electric vehicle (EV) charging stops. This intent, which extends the[multi-waypoint intent](https://developer.android.com/training/cars/platforms/automotive-os/android-intents-automotive#tbt-param), helps drivers maintain sufficient electric vehicle battery charge to reach their destinations by syncing charging stop information between EV trip planning apps and Google Maps.
| **Note:** To mark any waypoints as charging stations, the route must contain at least one waypoint and the final destination.

For charging stops, trip intents:

- Must contain a name and lat-long
- May optionally contain a power output, to be used for calculating charging time

Google uses the charging station name and lat-long to find a matching charging station place to display rich data like connector types, totals, speeds and real-time availability, supported payment methods, and host points of interest (POI). For example, driving directions within outdoor parking lots for the final part of the navigation, opening hours, ratings. To ensure that charging stations match well with Google's data, use a specific`<brand name>`---for example,`ChargePoint`.

### Parameters

The following parameters allow you to specify details for the final destination and any waypoints, including those designated as EV charging stations.

#### Final destination

To set a charging station as the final destination, use:

- `q`: Must contain the lat-long value of the charging station.
- `q_type`:`1`specifies that the final destination is a charging station.
- `q_name`: The name of the final destination. Required if`q_type`is`1`.
- `q_power_output_kw`: A double number for charging station power output in kilowatts. Optional.

#### Waypoints

For waypoints, all of the parameters are parallel, pipe-separated (`|`) arrays of values in the same order as waypoints, not including final destination. A mismatch in the number of elements in parallel arrays is treated as a malformed intent.

To add one or more charging stations waypoints, use the following parameters, all of which are optional. If one of the destinations is marked as a charging station, then the waypoint name becomes mandatory for that destination.

- `waypoints`: List of waypoints as described in the turn-by-turn navigation intent. Must be a lat-long value for charging station waypoints.

- `waypoint_types`: Types per waypoint specified as a number.`0`is any stop (default value) and`1`is the charging station.

- `waypoint_names`: Waypoint names. This field is mandatory for charging stations.

- `waypoint_power_outputs_kw`: Double numbers for charging station power in kilowatts. For charging stations, you can optionally specify a waypoint power output value, which is used as a fallback if the matching station is not found. Empty slot means no value is provided.

### User experience (UX) behavior

For trip intents with multiple destinations, the route overview screen is displayed, but the navigation doesn't start automatically.

For a correctly formatted intent, Google Maps will present a route overview screen for the trip. The route overview screen will display all waypoints and the final destination from the intent, with charging recommendations where applicable.

For any waypoints or final destination marked as a charging station, Google Maps will search for a matching place in Google's database. To ensure the best possible information is displayed for charging stations:

- If a match is found, Google Maps uses Google data to display the charging station in the user interface (UI) and provide a charging recommendation for the charging station.

- If the match isn't found, data provided in the intent for a charging station (lat-long, name and power output) is used to display this charging station in the UI and provide a charging recommendation at this charging station.

### Examples

The following examples illustrate how to construct intents for various EV trip planning scenarios, including navigating by way of multiple charging stations and handling unknown power outputs.

#### Navigate to a final destination by way of multiple charging stations

The following intent navigates to the final destination, Port Macquarie NSW, by way of two charging stations, ChargePoint and Evie.

Destinations in order:

1. ChargePoint Charging Station (location: -32.9599188,151.6240806, power output: 6.6kw)

2. Evie Charging Station (location: -31.9432539,152.4699808, power output: 350kw)

3. Port Macquarie NSW

    Uri mapIntentUri =
        Uri.parse(
            "google.navigation:q=Port+Macquarie+NSW"
                + "&waypoints=-32.9599188%2C151.6240806%7C-31.9432539%2C152.4699808"
                + "&waypoint_types=1%7C1"
                + "&waypoint_names=ChargePoint+Charging+Station%7CEvie+Charging+Station"
                + "&waypoint_power_outputs_kw=6.6%7C350");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

#### Unknown power output

If the power output value is unknown, leave the relevant slot of`waypoint_power_outputs_kw`empty. Or if all slots are empty, there is no need to specify the`waypoint_power_outputs_kw`parameter.

Destinations in order:

1. ChargePoint Charging Station (location: -32.9599188,151.6240806, power output: unknown)

2. Port Macquarie NSW

    Uri mapIntentUri =
        Uri.parse(
            "google.navigation:q=Port+Macquarie+NSW"
                + "&waypoints=-32.9599188%2C151.6240806"
                + "&waypoint_types=1"
                + "&waypoint_names=ChargePoint+Charging+Station");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

#### Mark final destination as a charging station

To mark the final destination as a charging station, specify`q_type`,`q_name`and`q_power_output_kw`parameters.

Destinations in order:

1. Taronga Zoo, Sydney Australia

2. ChargePoint Charging Station (location: -32.9599188,151.6240806, power output: unknown)

3. Evie Charging Station (location: -31.9432539,152.4699808, power output: 350kw)

    Uri mapIntentUri =
        Uri.parse(
            "google.navigation:q=-31.9432539,152.4699808&q_type=1&q_name=Evie+Charging+Station&q_power_output_kw=350"
                + "&waypoints=Taronga+Zoo%2C+Sydney+Australia%7C-32.9599188%2C151.6240806"
                + "&waypoint_types=0%7C1"
                + "&waypoint_names=%7CChargePoint+Charging+Station"
                + "&waypoint_power_outputs_kw=%7C");
    Intent mapIntent = new Intent(Intent.ACTION_VIEW, mapIntentUri);
    mapIntent.setPackage("com.google.android.apps.maps");
    startActivity(mapIntent);

## Action intents

The following action intents with interfaces are available:

|                             Action                             |                                                                                                                                                                                                          Description                                                                                                                                                                                                          |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `geo.action:?act=mute`                                         | Mutes all navigation voice guidance.                                                                                                                                                                                                                                                                                                                                                                                          |
| `geo.action:?act=unmute`                                       | Unmutes navigation voice guidance.                                                                                                                                                                                                                                                                                                                                                                                            |
| `geo.action:?act=show_traffic`                                 | Shows traffic lines on the map.                                                                                                                                                                                                                                                                                                                                                                                               |
| `geo.action:?act=hide_traffic`                                 | Hides traffic lines on the map.                                                                                                                                                                                                                                                                                                                                                                                               |
| `geo.action:?act=show_satellite`                               | Shows satellite imagery on the map.                                                                                                                                                                                                                                                                                                                                                                                           |
| `geo.action:?act=hide_satellite`                               | Hides satellite imagery on the map.                                                                                                                                                                                                                                                                                                                                                                                           |
| `geo.action:?act=show_alternates`                              | Google Maps opens the alternative routes screen (only works while navigating).                                                                                                                                                                                                                                                                                                                                                |
| `geo.action:?act=query_next_turn`                              | Google Maps speaks the next turn (only works while navigating).                                                                                                                                                                                                                                                                                                                                                               |
| `geo.action:?act=distance_to_next_turn`                        | Google Maps speaks the distance to next turn (only works while navigating).                                                                                                                                                                                                                                                                                                                                                   |
| `geo.action:?act=time_to_next_turn`                            | Google Maps speaks the time to next turn (only works while navigating).                                                                                                                                                                                                                                                                                                                                                       |
| `geo.action:?act=distance_to_destination`                      | Google Maps speaks the distance to the destination (only works while navigating).                                                                                                                                                                                                                                                                                                                                             |
| `geo.action:?act=go_back`                                      | Google Maps steps back to the previous screen in the UI.                                                                                                                                                                                                                                                                                                                                                                      |
| `geo.action:?act=query_current_road`                           | Google Maps speaks the current road.                                                                                                                                                                                                                                                                                                                                                                                          |
| `geo.action:?act=query_destination`                            | Google Maps speaks the destination.                                                                                                                                                                                                                                                                                                                                                                                           |
| `geo.action:?act=traffic_report`                               | Google Maps speaks the traffic report.                                                                                                                                                                                                                                                                                                                                                                                        |
| `geo.action:?act=clear_search_results`                         | Google Maps closes the search results screen (if it's open).                                                                                                                                                                                                                                                                                                                                                                  |
| `geo.action:?act=apply_electric_vehicle_connector_filter`      | Applies connector type filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                           |
| `geo.action:?act=remove_electric_vehicle_connector_filter`     | Removes connector type filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                           |
| `geo.action:?act=apply_electric_vehicle_payment_filter`        | Applies payment filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                                  |
| `geo.action:?act=remove_electric_vehicle_payment_filter`       | Removes payment filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                                  |
| `geo.action:?act=apply_electric_vehicle_fast_charging_filter`  | Applies fast charging filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                            |
| `geo.action:?act=remove_electric_vehicle_fast_charging_filter` | Removes fast charging filter for electric vehicle charging station search results.                                                                                                                                                                                                                                                                                                                                            |
| `geo.action:?act=avoid_tolls`                                  | If the user is navigating, tells Google Maps to avoid routes with tolls. This may result in a reroute if the current route has tolls.                                                                                                                                                                                                                                                                                         |
| `geo.action:?act=allow_tolls`                                  | If the user is navigating, tells Google Maps to allow routes with tolls. This may result in a reroute if allowing tolls results in a better route being available.                                                                                                                                                                                                                                                            |
| `geo.action:?act=avoid_ferries`                                | If the user is navigating, tells Google Maps to avoid routes with ferries. This might result in a reroute if the current active route has ferries.                                                                                                                                                                                                                                                                            |
| `geo.action:?act=allow_ferries`                                | If the user is navigating, tells Google Maps to allow routes with ferries. This might result in a reroute if allowing ferries results in a better route being available.                                                                                                                                                                                                                                                      |
| `geo.action:?act=avoid_highways`                               | If the user is navigating, tells Google Maps to avoid routes with highways. This might result in a reroute if the current active route has highways.                                                                                                                                                                                                                                                                          |
| `geo.action:?act=allow_highways`                               | If the user is navigating, tells Google Maps to allow routes with highways. This might result in a reroute if allowing highways results in a better route being available.                                                                                                                                                                                                                                                    |
| `geo.action:?act=eta`                                          | If the user is navigating, Google Maps speaks the estimated time of arrival of the destination (for example, 9:15 am).                                                                                                                                                                                                                                                                                                        |
| `geo.action:?act=time_to_destination`                          | If the user is navigating, Google Maps speaks the expected time to the destination (for example, 15 minutes).                                                                                                                                                                                                                                                                                                                 |
| `geo.action:?act=exit_navigation`                              | Exits navigation.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `geo.action:?act=select_search_result&id=0`                    | If search results are shown on screen (as depicted in the accompanying image), this action starts navigation to the*n* th result based on the ID parameter provided. Note the index is 0-based (that is,`geo.action:?act=select_search_result&id=0`will select the first result in the list). ![Search results are shown on screen](https://developer.android.com/static/training/cars/images/android-automotive-intents.png) |

| **Note:** You can use the Google Automotive Emulator to test these intents.