---
title: GooglePlayGames.BasicApi.Nearby.IDiscoveryListener Interface Reference  |  API reference  |  Android Developers
url: https://developer.android.com/games/services/unity/v2/api/interface/google-play-games/basic-api/nearby/i-discovery-listener
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [API reference](https://developer.android.com/reference)

Stay organized with collections

Save and categorize content based on your preferences.



# GooglePlayGames.BasicApi.Nearby.IDiscoveryListener

Interface for receiving notifications about discovered endpoints.

## Summary

| Public functions | |
| --- | --- |
| `OnEndpointFound(EndpointDetails discoveredEndpoint)` | `void`  Called when an endpoint is found during discovery. |
| `OnEndpointLost(string lostEndpointId)` | `void`  Called when an endpoint is lost during discovery. |

## Public functions

### OnEndpointFound

```
void OnEndpointFound(
  EndpointDetails discoveredEndpoint
)
```

Called when an endpoint is found during discovery.

Details | || Parameters | |  |  | | --- | --- | | `discoveredEndpoint` | The details of the discovered endpoint. | |

### OnEndpointLost

```
void OnEndpointLost(
  string lostEndpointId
)
```

Called when an endpoint is lost during discovery.

Details | || Parameters | |  |  | | --- | --- | | `lostEndpointId` | The ID of the lost endpoint. | |