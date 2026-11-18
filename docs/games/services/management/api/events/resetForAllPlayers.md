---
title: https://developer.android.com/games/services/management/api/events/resetForAllPlayers
url: https://developer.android.com/games/services/management/api/events/resetForAllPlayers
source: md.txt
---

> Documentation index: https://developer.android.com/games/services/management/api/events/llms.txt

**Requires [authorization](https://developer.android.com/games/services/management/api/events/resetForAllPlayers.md.txt#auth)**

Resets the event with the given ID for all players. This method is only available to user accounts for your developer console. Only draft events can be reset.

## Request

### HTTP request

```
POST https://www.googleapis.com/games/v1management/events/eventId/resetForAllPlayers
```

### Parameters

| Parameter name | Value | Description |
|---|---|---|
| **Path parameters** |||
| `eventId` | `string` | The ID of the event. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developers.google.com/identity/protocols/oauth2)).

| Scope |
|---|
| `https://www.googleapis.com/auth/games` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns an empty response body.