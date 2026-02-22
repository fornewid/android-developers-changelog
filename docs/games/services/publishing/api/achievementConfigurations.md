---
title: https://developer.android.com/games/services/publishing/api/achievementConfigurations
url: https://developer.android.com/games/services/publishing/api/achievementConfigurations
source: md.txt
---

Represents the configuration of an accomplishment.

For a list of [methods](https://developer.android.com/games/services/publishing/api/achievementConfigurations#methods) for this resource, see the end of this page.

## Resource representations

This is a JSON template for an achievement configuration resource.

```text
{
  "kind": "gamesConfiguration#achievementConfiguration",
  "token": string,
  "id": string,
  "achievementType": string,
  "initialState": string,
  "stepsToUnlock": integer,
  "draft": {
    "kind": "gamesConfiguration#achievementConfigurationDetail",
    "name": {
      "kind": "gamesConfiguration#localizedStringBundle",
      "translations": [
        {
          "kind": "gamesConfiguration#localizedString",
          "locale": string,
          "value": string
        }
      ]
    },
    "description": {
      "kind": "gamesConfiguration#localizedStringBundle",
      "translations": [
        {
          "kind": "gamesConfiguration#localizedString",
          "locale": string,
          "value": string
        }
      ]
    },
    "pointValue": integer,
    "iconUrl": string,
    "sortRank": integer
  },
  "published": {
    "kind": "gamesConfiguration#achievementConfigurationDetail",
    "name": {
      "kind": "gamesConfiguration#localizedStringBundle",
      "translations": [
        {
          "kind": "gamesConfiguration#localizedString",
          "locale": string,
          "value": string
        }
      ]
    },
    "description": {
      "kind": "gamesConfiguration#localizedStringBundle",
      "translations": [
        {
          "kind": "gamesConfiguration#localizedString",
          "locale": string,
          "value": string
        }
      ]
    },
    "pointValue": integer,
    "iconUrl": string,
    "sortRank": integer
  }
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#achievementConfiguration`. |   |
| `token` | `string` | The token for this resource. |   |
| `id` | `string` | The ID of the achievement. |   |
| `achievementType` | `string` | The type of the achievement. Possible values are: - "`STANDARD`" - Achievement is either locked or unlocked. - "`INCREMENTAL`" - Achievement is incremental. |   |
| `initialState` | `string` | The initial state of the achievement. Possible values are: - "`HIDDEN`" - Achievement is hidden. - "`REVEALED`" - Achievement is revealed. - "`UNLOCKED`" - Achievement is unlocked. |   |
| `stepsToUnlock` | `integer` | Steps to unlock. Only applicable to incremental achievements. |   |
| `draft` | `nested object` | The draft data of the achievement. |   |
| `draft.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#achievementConfigurationDetail`. |   |
| `draft.name` | `nested object` | Localized strings for the achievement name. |   |
| `draft.name.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.name.translations[]` | `list` | The locale strings. |   |
| `draft.name.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.name.translations[].locale` | `string` | The locale string. |   |
| `draft.name.translations[].value` | `string` | The string value. |   |
| `draft.description` | `nested object` | Localized strings for the achievement description. |   |
| `draft.description.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.description.translations[]` | `list` | The locale strings. |   |
| `draft.description.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.description.translations[].locale` | `string` | The locale string. |   |
| `draft.description.translations[].value` | `string` | The string value. |   |
| `draft.pointValue` | `integer` | Point value for the achievement. |   |
| `draft.iconUrl` | `string` | The icon url of this achievement. Writes to this field are ignored. |   |
| `draft.sortRank` | `integer` | The sort rank of this achievement. Writes to this field are ignored. |   |
| `published` | `nested object` | The published data of the achievement. This data is read-only. |   |
| `published.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#achievementConfigurationDetail`. |   |
| `published.name` | `nested object` | Localized strings for the achievement name. |   |
| `published.name.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.name.translations[]` | `list` | The locale strings. |   |
| `published.name.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.name.translations[].locale` | `string` | The locale string. |   |
| `published.name.translations[].value` | `string` | The string value. |   |
| `published.description` | `nested object` | Localized strings for the achievement description. |   |
| `published.description.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.description.translations[]` | `list` | The locale strings. |   |
| `published.description.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.description.translations[].locale` | `string` | The locale string. |   |
| `published.description.translations[].value` | `string` | The string value. |   |
| `published.pointValue` | `integer` | Point value for the achievement. |   |
| `published.iconUrl` | `string` | The icon url of this achievement. Writes to this field are ignored. |   |
| `published.sortRank` | `integer` | The sort rank of this achievement. Writes to this field are ignored. |   |

## Methods

[delete](https://developer.android.com/games/services/publishing/api/achievementConfigurations/delete)
:   Delete the achievement configuration with the given ID.

[get](https://developer.android.com/games/services/publishing/api/achievementConfigurations/get)
:   Retrieves the metadata of the achievement configuration with the given ID.

[insert](https://developer.android.com/games/services/publishing/api/achievementConfigurations/insert)
:   Insert a new achievement configuration in this application.

[list](https://developer.android.com/games/services/publishing/api/achievementConfigurations/list)
:   Returns a list of the achievement configurations in this application.

[update](https://developer.android.com/games/services/publishing/api/achievementConfigurations/update)
:   Update the metadata of the achievement configuration with the given ID.