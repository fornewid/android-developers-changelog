---
title: https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app
url: https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app
source: md.txt
---

# Implement navigation app intents

Google Assistant uses three different formats of intents that your navigation app can support. You can achieve interoperability and integrate your app and Google Assistant by declaring the intent filters detailed in this page in your app's manifest. To learn more about intents, see[`Intent`](https://developer.android.com/reference/android/content/Intent).

The Assistant navigation app`Intent`class supports the following intents:

- Navigation intent
- Search intent
- Custom action intent

| **Note:** You aren't required to support all three intents for interoperability, but we recommend supporting all of them for a complete user experience.

![Intent data flow](https://developer.android.com/static/guide/app-actions/images/intent-data-flow-2.svg)

**Figure 1.**Intent data flow.

### Parameters in intent data

Intent data follows a URI format containing parameters based on the intent you're passing. Some parameters are always supplied in the data. This means you can expect them to always have an explicit value. Optional parameters, however, don't always have a value set in the data. For more information, see[Data test](https://developer.android.com/guide/components/intents-filters#DataTest).

### Offline intents

All intents listed in this page have their offline variants available. You can distinguish them by appending`.offline`to their scheme. For example, the navigation intent uses the`geo.offline`scheme. These intent filters in the manifest signify the app's ability to support these actions offline.

## Navigation intent

Use a navigation intent to fulfill a user's request to navigate to a specific destination. This destination can either be a single location (address) or multiple locations (for example, coffee shops and gas stations). Intent data follows a URI format specified for each intent.

### Intent format

The`Intent`class uses the following format for navigation app intent:

**Category:** `android.intent.category.DEFAULT`

**Action:**

- Android Auto and Android Automotive OS:`androidx.car.app.action.NAVIGATE`
- Other form factors:`android.intent.action.NAVIGATE`

**Scheme:** `geo`

**Examples:**

- `geo:0,0?q=Googleplex`
- `geo:0,0?q=1600+Amphitheatre+parkway&mode=b&intent=add_a_stop`
- `geo:0,0?q=coffee+shop&mode=w&intent=navigation`
- `geo:1.1,2.2?q=Starbucks+on+Main+Street&mode=w&intent=navigation`

**Suggested app behavior:**Navigation to the specified location starts or the user is asked to choose from multiple options.

### Manifest intent filters

Declare the following intent format in your app's manifest file so that Google Assistant knows that your navigation app can receive navigation intents.

**All form factors except Android Auto and Android Automotive OS:**  

    <intent-filter>
      <action android:name="android.intent.action.NAVIGATE" />
      <category android:name="android.intent.category.DEFAULT"/>
      <data android:scheme="geo" />
    </intent-filter>

**Android Auto and Android Automotive OS:**  

    <intent-filter>
      <action android:name="androidx.car.app.action.NAVIGATE" />
      <category android:name="android.intent.category.DEFAULT"/>
      <data android:scheme="geo" />
    </intent-filter>

### Supplied parameters

The following parameters are expected to be available in the supplied navigation app intent data.

#### Location query or geographical coordinates

Every navigation intent query contains one or both of these parameters, depending on the type of data requested:

- **Location query**

  Refers to the location the user is trying to navigate to. Use this data to resolve the user's destination.

  **Parameter key:** `q`  
  **Value:**The user's queried destination.

  **Example:** `geo:0,0?q=Golden+Gate+Bridge`  
  **Interpretation:** The user wants to navigate to the*Golden Gate Bridge*.
- **Geographical coordinates (latitude and longitude)**

  Refers to specific coordinates used by the user for navigation.

  **Parameter key:** `geo:lat,long`  
  **Value:**The user's queried coordinates.

  **Example:** `geo:1.1,2.2?mode=w&intent=navigation`  
  **Interpretation:**The user wants to navigate to coordinates (1.1, 2.2).

### Optional parameters

The optional parameters supplied in the navigation app intent data are described in this section.

#### Intent

Defines the user intent. If this parameter isn't set, then the default user intent is considered as`navigation`.
| **Note:** This is different from the[`Intent`](https://developer.android.com/reference/android/content/Intent#intent-structure)class available in Android.

**Parameter key:** `intent`  
**Possible values:**

- `navigation`\[default value\] - Replaces the destination and starts navigation. Use this for queries like*navigate to x*.
- `add_a_stop`- Adds the stop as the next destination along with previous destinations. Use this for queries like*add a stop at x*.
- `directions`- Shows route directions without starting navigation. Use this for queries like*directions to x*.

**Example:** `geo:47.61594547836694,-122.20373173098756?q=575+Bellevue+Square,+Bellevue,+WA+98004&intent=add_a_stop`**Interpretation:**The user wants to add a stop to Bellevue Square, Bellevue, with the current coordinates \[47.6, -122.2\].
| **Tip:** You can use the[Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator)to test these intents.

#### Avoid

Defines things to avoid in navigation.

**Parameter key:** `avoid`  
**Possible values:**

- `f`- ferries
- `h`- highways
- `t`- tolls

**Example:** `geo:0,0?q=googleplex&avoid=tf`  
**Interpretation:**The user wants to navigate to Googleplex avoiding tolls and ferries.

#### Travel mode

Travel mode represents the method of transportation specified in the query by the user.
| **Note:** This mode applies to all form factors except Android Automotive OS.

**Parameter key:** `mode`  
**Possible values:**

- `b`- bicycle
- `d`- drive
- `x`- taxi
- `l`- two wheeler
- `r`- transit
- `w`- walk

**Example:** `geo:0,0?q=Googleplex&mode=r`  
**Interpretation:**The user wants to navigate to Googleplex using public transit.

#### Entry

Used for logging the source of entry.

**Possible values:**assistant

**Example:** `geo:47.61594547836694,-122.20373173098756?entry=assistant`

## Search intent

Use a search intent to search for a query and display multiple results along the route while driving.

### Intent format

The`Intent`class uses the following format for search intents:

**Category:** `android.intent.category.DEFAULT`

**Action:** `android.intent.action.VIEW`

**Scheme:** `geo`

**Example:** `geo:0,0?q=restaurants+nearby`

**Suggested app behavior:**Open a list of locations that fit the user query.
| **Tip:** Navigation app intent and search intent have different action types. Navigation is[`ACTION_NAVIGATE`](https://developer.android.com/reference/androidx/car/app/CarContext#ACTION_NAVIGATE())while Search is[`ACTION_VIEW`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW)as outlined in the[Manifest intent filters](https://developer.android.com/develop/devices/assistant/intents-assistant-nav-app#search-intent-manifest).

### Manifest intent filters

Declare the following intent format in your app's manifest file so that Google Assistant knows that your navigation app can receive search intents:  

    <intent-filter>
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT"/>
      <data android:scheme="geo" />
    </intent-filter>

### Supplied parameters

The following parameters are expected to be available in the supplied search intent data.

#### Location query

A location query is the location the user is searching for while driving. This query can be imprecise or along an active navigation route.

**Parameter key:** `q`  
**Value:** The user's search term, which could be a location type such as*coffee shop* or*college* but could also have quantifiers such as*-near me* or*-with best rating*.

**Example:** `geo:0,0?q=restaurants+nearby`  
**Interpretation:**The user wants to search nearby restaurants.

## Custom action intent

Use a custom intent for custom actions like reporting accidents and ending navigation. The main action type is defined by the`act`query parameter. You can set additional parameters depending on the action type.

### Intent format

The`Intent`class uses the following format for custom action intent:

**Category:** `android.intent.category.DEFAULT`

**Action:** `android.intent.action.VIEW`

**Scheme:** `geo.action`

**Example:** `geo.action:?act=report&accident_type=major`

### Manifest intent filters

Declare the following intent format in your app's manifest file to let Google Assistant know that your navigation app can receive custom action intents.  

    <intent-filter>
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT"/>
      <data android:scheme="geo.action" />
    </intent-filter>

### Supplied parameters

The following parameters are expected to be available in the supplied Custom Action intent data:

##### Action type

It defines the type of custom action a user wants to perform.

**Parameter key:** `act`

**Examples:**

- `geo.action:?act=report_crash&accident_type=major`  
  **Interpretation:**The user wants to report a major accident.

- `geo.action:?act=mute`  
  **Interpretation:**The user wants to mute voice instructions.

- `geo.action:?act=exit_navigation`  
  **Interpretation:**The user wants to exit the current navigation.

**Suggested app behavior:**Fulfill the requested action on the navigation app or show an unsupported action message.

The following figure depicts an example of key-value pairs in the response query:

![Custom action intent data flow](https://developer.android.com/static/guide/app-actions/images/intent-data-flow-custom-action.svg)

**Figure 2.**Custom action intent data flow.

**Key-value pair:**  

    "act": "report_crash"
    "road_direction": other_side"

Every custom action always has an`act`parameter as the key. In the aforementioned example code, some actions can have additional key-value pairs. For example,`act=report_crash`supports these additional keys:`accident_type`and`road_direction`.

The key`accident_type`can support two values,`minor`and`major`.
| **Note:** Additional parameters are optional and might not be present in every intent response.

**Possible values**

The table lists possible values that Google Assistant can pass as the action the user is trying to fulfill on the navigation app.
| **Note:** If your app supports only a subset of these actions, it must inform the user whenever they request an unsupported action.

|                     Value                      |                                Description                                 | Optional parameter keys | Optional parameter values |
|------------------------------------------------|----------------------------------------------------------------------------|-------------------------|---------------------------|
| `allow_ferries`                                | Change route preference to allow ferries.                                  |                         |                           |
| `allow_highways`                               | Change route preference to allow highways.                                 |                         |                           |
| `allow_tolls`                                  | Change route preference to allow tolls.                                    |                         |                           |
| `apply_electric_vehicle_connector_filter`      | Only show EV charging locations that match the car's connector.            |                         |                           |
| `apply_electric_vehicle_fast_charging_filter`  | Only show EV charging locations that are fast chargers.                    |                         |                           |
| `apply_electric_vehicle_payment_filter`        | Only show EV charging locations that require payment.                      |                         |                           |
| `avoid_ferries`                                | Change route preference to avoid ferries.                                  |                         |                           |
| `avoid_highways`                               | Change route preference to avoid highways.                                 |                         |                           |
| `avoid_tolls`                                  | Change route preference to avoid tolls.                                    |                         |                           |
| `clear_search_results`                         | Clear search results on the map.                                           |                         |                           |
| `distance_to_destination`                      | Show distance to the destination.                                          |                         |                           |
| `distance_to_next_turn`                        | Show distance to the next turn.                                            |                         |                           |
| **eta**                                        | Show ETA to the destination.                                               |                         |                           |
| **exit_navigation**                            | Exit or cancel navigation.                                                 |                         |                           |
| `follow_mode`                                  | Change map view to follow mode.                                            |                         |                           |
| `go_back`                                      | Go back to previous map action.                                            |                         |                           |
| `hide_satellite`                               | Change map setting to hide satellite info.                                 |                         |                           |
| `hide_traffic`                                 | Change map setting to hide traffic info.                                   |                         |                           |
| **mute**                                       | Mute voice guidance.                                                       |                         |                           |
| `query_current_road`                           | Show what is the current road the user is on.                              |                         |                           |
| `query_destination`                            | Show what is the destination.                                              |                         |                           |
| `query_next_turn`                              | Show what is the next turn.                                                |                         |                           |
| `remove_electric_vehicle_connector_filter`     | Remove filtering for EV charging locations that match the car's connector. |                         |                           |
| `remove_electric_vehicle_fast_charging_filter` | Remove filtering for EV charging locations that are fast chargers.         |                         |                           |
| `remove_electric_vehicle_payment_filter`       | Remove filtering for EV charging locations that require payment.           |                         |                           |
| **report_crash**                               | Report crashes.                                                            | `accident_type`         | `minor`                   |
| **report_crash**                               | Report crashes.                                                            | `accident_type`         | `major`                   |
| **report_crash**                               | Report crashes.                                                            | `road_direction`        | `this_side`               |
| **report_crash**                               | Report crashes.                                                            | `road_direction`        | `other_side`              |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `animal`                  |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `broken_traffic_light`    |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `construction`            |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `flooding`                |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `fog`                     |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `hail`                    |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `ice`                     |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `missing_sign`            |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `object_on_road`          |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `pothole`                 |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `roadkill`                |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `snow`                    |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `vehicle`                 |
| **report_hazard**                              | Report hazards.                                                            | `hazard_type`           | `weather`                 |
| **report_hazard**                              | Report hazards.                                                            | `road_direction`        | `this_side`               |
| **report_hazard**                              | Report hazards.                                                            | `road_direction`        | `other_side`              |
| **report_hazard**                              | Report hazards.                                                            | `location_on_road`      | `on_road`                 |
| **report_hazard**                              | Report hazards.                                                            | `location_on_road`      | `on_shoulder`             |
| `report_police`                                | Report police activity.                                                    | `road_direction`        | `this_side`               |
| `report_police`                                | Report police activity.                                                    | `road_direction`        | `other_side`              |
| `report_road_closure`                          | Report road closures.                                                      | `road_closure_type`     | `partial`                 |
| `report_road_closure`                          | Report road closures.                                                      | `road_closure_type`     | `full`                    |
| **`report_traffic`**                           | Report traffic.                                                            | `traffic_type`          | `moderate`                |
| **`report_traffic`**                           | Report traffic.                                                            | `traffic_type`          | `heavy`                   |
| **`report_traffic`**                           | Report traffic.                                                            | `traffic_type`          | `standstill`              |
| **`report_traffic`**                           | Report traffic.                                                            | `road_direction`        | `this_side`               |
| **`report_traffic`**                           | Report traffic.                                                            | `road_direction`        | `other_side`              |
| `resume_navigation`                            | Resume navigation.                                                         |                         |                           |
| `route_overview`                               | Show route overview.                                                       |                         |                           |
| `show_alternates`                              | Show alternative routes.                                                   |                         |                           |
| `show_directions_list`                         | Show turn-by-turn instructions.                                            |                         |                           |
| `show_satellite`                               | Show satellite info on the map.                                            |                         |                           |
| `show_traffic`                                 | Show traffic on the map.                                                   |                         |                           |
| `time_to_destination`                          | Show ETA to destination.                                                   |                         |                           |
| `time_to_next_turn`                            | Show ETA to next turn.                                                     |                         |                           |
| **unmute**                                     | Unmute voice guidance.                                                     |                         |                           |