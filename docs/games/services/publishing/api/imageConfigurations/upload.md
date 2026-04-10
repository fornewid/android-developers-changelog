---
title: https://developer.android.com/games/services/publishing/api/imageConfigurations/upload
url: https://developer.android.com/games/services/publishing/api/imageConfigurations/upload
source: md.txt
---

| **Deprecated:** This API is deprecated and is being removed, so you shouldn't use it. Attempting to use this API causes errors.


**Requires [authorization](https://developer.android.com/games/services/publishing/api/imageConfigurations/upload#auth)**

Uploads an image for a resource with the given ID and image type.

This method supports an **/upload** URI and accepts uploaded media with the following characteristics:

- **Maximum file size:** 15MB
- **Accepted Media MIME types:** `image/*`

## Request

### HTTP request

```
POST https://www.googleapis.com/upload/games/v1configuration/images/resourceId/imageType/imageType
```

### Parameters

| Parameter name | Value | Description |
|---|---|---|
| **Path parameters** |||
| `imageType` | `string` | Selects which image in a resource for this method. <br /> <br /> Acceptable values are: - "`ACHIEVEMENT_ICON`": The icon image for an achievement resource. - "`LEADERBOARD_ICON`": The icon image for a leaderboard resource. |
| `resourceId` | `string` | The ID of the resource used by this method. |
| **Required query parameters** |||
| `uploadType` | `string` | The type of upload request to the **/upload** URI. Acceptable values are: - `media` - [Simple upload](https://developer.android.com/games/services/publishing/upload#simple). Upload the media data. - `resumable` - [Resumable upload](https://developer.android.com/games/services/publishing/upload#resumable). Upload the file in a resumable fashion, using a series of at least two requests. |

### Authorization

This request requires authorization with the following scope ([read more about authentication and authorization](https://developer.android.com/accounts/docs/OAuth2)).

| Scope |
|---|
| `https://www.googleapis.com/auth/androidpublisher` |

### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "kind": "gamesConfiguration#imageConfiguration",
  "url": string,
  "resourceId": string,
  "imageType": string
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#imageConfiguration`. |   |
| `url` | `string` | The url for this image. |   |
| `resourceId` | `string` | The resource ID of resource which the image belongs to. |   |
| `imageType` | `string` | The image type for the image. <br /> Acceptable values are: - "`ACHIEVEMENT_ICON`" - "`LEADERBOARD_ICON`" |   |