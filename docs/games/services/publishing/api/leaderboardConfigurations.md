---
title: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations
url: https://developer.android.com/games/services/publishing/api/leaderboardConfigurations
source: md.txt
---

Represents the configuration of a leaderboard.

For a list of [methods](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations#methods) for this resource, see the end of this page.

## Resource representations

This is a JSON template for an leaderboard configuration resource.

```text
{
  "kind": "gamesConfiguration#leaderboardConfiguration",
  "token": string,
  "id": string,
  "scoreOrder": string,
  "scoreMin": long,
  "scoreMax": long,
  "draft": {
    "kind": "gamesConfiguration#leaderboardConfigurationDetail",
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
    "iconUrl": string,
    "sortRank": integer,
    "scoreFormat": {
      "numberFormatType": string,
      "suffix": {
        "zero": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "one": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "two": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "few": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "many": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "other": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        }
      },
      "numDecimalPlaces": integer,
      "currencyCode": string
    }
  },
  "published": {
    "kind": "gamesConfiguration#leaderboardConfigurationDetail",
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
    "iconUrl": string,
    "sortRank": integer,
    "scoreFormat": {
      "numberFormatType": string,
      "suffix": {
        "zero": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "one": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "two": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "few": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "many": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        },
        "other": {
          "kind": "gamesConfiguration#localizedStringBundle",
          "translations": [
            {
              "kind": "gamesConfiguration#localizedString",
              "locale": string,
              "value": string
            }
          ]
        }
      },
      "numDecimalPlaces": integer,
      "currencyCode": string
    }
  }
}
```

| Property name | Value | Description | Notes |
|---|---|---|---|
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#leaderboardConfiguration`. |   |
| `token` | `string` | The token for this resource. |   |
| `id` | `string` | The ID of the leaderboard. |   |
| `scoreOrder` | `string` | The type of the leaderboard. Possible values are: - "`LARGER_IS_BETTER`" - Larger scores posted are ranked higher. - "`SMALLER_IS_BETTER`" - Smaller scores posted are ranked higher. |   |
| `scoreMin` | `long` | Minimum score that can be posted to this leaderboard. |   |
| `scoreMax` | `long` | Maximum score that can be posted to this leaderboard. |   |
| `draft` | `nested object` | The draft data of the leaderboard. |   |
| `draft.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#leaderboardConfigurationDetail`. |   |
| `draft.name` | `nested object` | Localized strings for the leaderboard name. |   |
| `draft.name.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.name.translations[]` | `list` | The locale strings. |   |
| `draft.name.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.name.translations[].locale` | `string` | The locale string. |   |
| `draft.name.translations[].value` | `string` | The string value. |   |
| `draft.iconUrl` | `string` | The icon url of this leaderboard. Writes to this field are ignored. |   |
| `draft.sortRank` | `integer` | The sort rank of this leaderboard. Writes to this field are ignored. |   |
| `draft.scoreFormat` | `nested object` | The score formatting for the leaderboard. |   |
| `draft.scoreFormat.numberFormatType` | `string` | The formatting for the number. Possible values are: - "`NUMERIC`" - Numbers are formatted to have no digits or a fixed number of digits after the decimal point according to locale. An optional custom unit can be added. - "`TIME_DURATION`" - Numbers are formatted to hours, minutes and seconds. - "`CURRENCY`" - Numbers are formatted to currency according to locale. |   |
| `draft.scoreFormat.suffix` | `nested object` | An optional suffix for the NUMERIC format type. These strings follow the same [plural rules](http://developer.android.com/guide/topics/resources/string-resource.html#Plurals) as all Android string resources. |   |
| `draft.scoreFormat.suffix.zero` | `nested object` | When the language requires special treatment of the number 0 (as in Arabic). |   |
| `draft.scoreFormat.suffix.zero.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.zero.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.zero.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.zero.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.zero.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.suffix.one` | `nested object` | When the language requires special treatment of numbers like one (as with the number 1 in English and most other languages; in Russian, any number ending in 1 but not ending in 11 is in this class). |   |
| `draft.scoreFormat.suffix.one.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.one.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.one.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.one.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.one.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.suffix.two` | `nested object` | When the language requires special treatment of numbers like two (as with 2 in Welsh, or 102 in Slovenian). |   |
| `draft.scoreFormat.suffix.two.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.two.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.two.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.two.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.two.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.suffix.few` | `nested object` | When the language requires special treatment of "small" numbers (as with 2, 3, and 4 in Czech; or numbers ending 2, 3, or 4 but not 12, 13, or 14 in Polish). |   |
| `draft.scoreFormat.suffix.few.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.few.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.few.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.few.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.few.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.suffix.many` | `nested object` | When the language requires special treatment of "large" numbers (as with numbers ending 11-99 in Maltese). |   |
| `draft.scoreFormat.suffix.many.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.many.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.many.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.many.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.many.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.suffix.other` | `nested object` | When the language does not require special treatment of the given quantity (as with all numbers in Chinese, or 42 in English). |   |
| `draft.scoreFormat.suffix.other.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `draft.scoreFormat.suffix.other.translations[]` | `list` | The locale strings. |   |
| `draft.scoreFormat.suffix.other.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `draft.scoreFormat.suffix.other.translations[].locale` | `string` | The locale string. |   |
| `draft.scoreFormat.suffix.other.translations[].value` | `string` | The string value. |   |
| `draft.scoreFormat.numDecimalPlaces` | `integer` | The number of decimal places for number. Only used for NUMERIC format type. |   |
| `draft.scoreFormat.currencyCode` | `string` | The curreny code string. Only used for CURRENCY format type. |   |
| `published` | `nested object` | The published data of the leaderboard. This data is read-only. |   |
| `published.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#leaderboardConfigurationDetail`. |   |
| `published.name` | `nested object` | Localized strings for the leaderboard name. |   |
| `published.name.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.name.translations[]` | `list` | The locale strings. |   |
| `published.name.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.name.translations[].locale` | `string` | The locale string. |   |
| `published.name.translations[].value` | `string` | The string value. |   |
| `published.iconUrl` | `string` | The icon url of this leaderboard. Writes to this field are ignored. |   |
| `published.sortRank` | `integer` | The sort rank of this leaderboard. Writes to this field are ignored. |   |
| `published.scoreFormat` | `nested object` | The score formatting for the leaderboard. |   |
| `published.scoreFormat.numberFormatType` | `string` | The formatting for the number. Possible values are: - "`NUMERIC`" - Numbers are formatted to have no digits or a fixed number of digits after the decimal point according to locale. An optional custom unit can be added. - "`TIME_DURATION`" - Numbers are formatted to hours, minutes and seconds. - "`CURRENCY`" - Numbers are formatted to currency according to locale. |   |
| `published.scoreFormat.suffix` | `nested object` | An optional suffix for the NUMERIC format type. These strings follow the same [plural rules](http://developer.android.com/guide/topics/resources/string-resource.html#Plurals) as all Android string resources. |   |
| `published.scoreFormat.suffix.zero` | `nested object` | When the language requires special treatment of the number 0 (as in Arabic). |   |
| `published.scoreFormat.suffix.zero.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.zero.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.zero.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.zero.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.zero.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.suffix.one` | `nested object` | When the language requires special treatment of numbers like one (as with the number 1 in English and most other languages; in Russian, any number ending in 1 but not ending in 11 is in this class). |   |
| `published.scoreFormat.suffix.one.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.one.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.one.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.one.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.one.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.suffix.two` | `nested object` | When the language requires special treatment of numbers like two (as with 2 in Welsh, or 102 in Slovenian). |   |
| `published.scoreFormat.suffix.two.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.two.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.two.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.two.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.two.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.suffix.few` | `nested object` | When the language requires special treatment of "small" numbers (as with 2, 3, and 4 in Czech; or numbers ending 2, 3, or 4 but not 12, 13, or 14 in Polish). |   |
| `published.scoreFormat.suffix.few.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.few.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.few.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.few.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.few.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.suffix.many` | `nested object` | When the language requires special treatment of "large" numbers (as with numbers ending 11-99 in Maltese). |   |
| `published.scoreFormat.suffix.many.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.many.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.many.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.many.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.many.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.suffix.other` | `nested object` | When the language does not require special treatment of the given quantity (as with all numbers in Chinese, or 42 in English). |   |
| `published.scoreFormat.suffix.other.kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedStringBundle`. |   |
| `published.scoreFormat.suffix.other.translations[]` | `list` | The locale strings. |   |
| `published.scoreFormat.suffix.other.translations[].kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#localizedString`. |   |
| `published.scoreFormat.suffix.other.translations[].locale` | `string` | The locale string. |   |
| `published.scoreFormat.suffix.other.translations[].value` | `string` | The string value. |   |
| `published.scoreFormat.numDecimalPlaces` | `integer` | The number of decimal places for number. Only used for NUMERIC format type. |   |
| `published.scoreFormat.currencyCode` | `string` | The curreny code string. Only used for CURRENCY format type. |   |

## Methods

[delete](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/delete)
:   Delete the leaderboard configuration with the given ID.

[get](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/get)
:   Retrieves the metadata of the leaderboard configuration with the given ID.

[insert](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/insert)
:   Insert a new leaderboard configuration in this application.

[list](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/list)
:   Returns a list of the leaderboard configurations in this application.

[update](https://developer.android.com/games/services/publishing/api/leaderboardConfigurations/update)
:   Update the metadata of the leaderboard configuration with the given ID.