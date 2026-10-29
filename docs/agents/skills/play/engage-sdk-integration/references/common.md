---
title: https://developer.android.com/agents/skills/play/engage-sdk-integration/references/common
url: https://developer.android.com/agents/skills/play/engage-sdk-integration/references/common
source: md.txt
---

This file defines common data models and entities used across the Engage SDK.

    {
      "entities": {
        "Image": {
          "package": "com.google.android.engage.common.datamodel.Image",
          "fields": {
            "imageUri": {
              "type": "Uri",
              "requirement": "Required",
              "setter": "setImageUri(Uri)",
              "getter": "getImageUri()"
            },
            "height": {
              "type": "Integer",
              "requirement": "Optional"
            },
            "width": {
              "type": "Integer",
              "requirement": "Optional"
            },
            "accessibilityText": {
              "type": "String",
              "requirement": "Required",
              "setter": "setAccessibilityText(String)",
              "getter": "getAccessibilityText()"
            },
            "theme": {
              "type": "ImageThemeEnum",
              "requirement": "Optional"
            },
            "cropType": {
              "type": "ImageCropTypeEnum",
              "requirement": "Optional"
            },
            "imageHeightInPixel": {
              "requirement": "Required",
              "setter": "setImageHeightInPixel(int)",
              "type": "Integer",
              "getter": "getImageHeightInPixel()"
            },
            "imageWidthInPixel": {
              "requirement": "Required",
              "setter": "setImageWidthInPixel(int)",
              "type": "Integer",
              "getter": "getImageWidthInPixel()"
            },
            "imageTheme": {
              "requirement": "Optional",
              "setter": "setImageTheme(@ImageTheme int)",
              "type": "@ImageTheme int",
              "getter": "getImageTheme()"
            },
            "imageCropType": {
              "requirement": "Optional",
              "setter": "setImageCropType(@ImageCropType int)",
              "type": "@ImageCropType int",
              "getter": "getImageCropType()"
            }
          }
        },
        "Price": {
          "package": "com.google.android.engage.common.datamodel.Price",
          "fields": {
            "currentPrice": {
              "type": "String",
              "requirement": "Required",
              "setter": "setCurrentPrice(String)",
              "getter": "getCurrentPrice()"
            },
            "strikethroughPrice": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setStrikethroughPrice(String)",
              "getter": "getStrikethroughPrice()"
            }
          }
        },
        "Rating": {
          "package": "com.google.android.engage.common.datamodel.Rating",
          "fields": {
            "ratingValue": {
              "type": "Float",
              "requirement": "Required"
            },
            "maxValue": {
              "type": "Double",
              "requirement": "Required",
              "setter": "setMaxValue(double)",
              "getter": "getMaxValue()"
            },
            "ratingCount": {
              "type": "Integer",
              "requirement": "Optional"
            },
            "ratingCountValue": {
              "type": "String",
              "requirement": "Optional"
            },
            "currentValue": {
              "requirement": "Required",
              "setter": "setCurrentValue(double)",
              "type": "Double",
              "getter": "getCurrentValue()"
            },
            "count": {
              "requirement": "Optional",
              "setter": "setCount(String)",
              "type": "String",
              "getter": "getCount()"
            },
            "countValue": {
              "requirement": "Optional",
              "setter": "setCountValue(long)",
              "type": "Long",
              "getter": "getCountValue()"
            }
          }
        },
        "DisplayTimeWindow": {
          "package": "com.google.android.engage.common.datamodel.DisplayTimeWindow",
          "fields": {
            "startTimeMillis": {
              "type": "Long",
              "requirement": "Required"
            },
            "endTimeMillis": {
              "type": "Long",
              "requirement": "Required"
            },
            "startTimestampMillis": {
              "requirement": "Optional",
              "setter": "setStartTimestampMillis(long)",
              "type": "Long",
              "getter": "getStartTimestampMillis()"
            },
            "endTimestampMillis": {
              "requirement": "Optional",
              "setter": "setEndTimestampMillis(long)",
              "type": "Long",
              "getter": "getEndTimestampMillis()"
            }
          }
        },
        "AccountProfile": {
          "package": "com.google.android.engage.common.datamodel.AccountProfile",
          "fields": {
            "accountId": {
              "type": "@NonNull String",
              "requirement": "Required",
              "setter": "setAccountId(@NonNull String)",
              "getter": "getAccountId()"
            },
            "profileId": {
              "type": "@NonNull String",
              "requirement": "Optional",
              "setter": "setProfileId(@NonNull String)",
              "getter": "getProfileId()"
            },
            "accountName": {
              "type": "String",
              "requirement": "Optional"
            },
            "profileImage": {
              "type": "Image",
              "requirement": "Optional"
            },
            "locale": {
              "requirement": "Optional",
              "setter": "setLocale(@NonNull String)",
              "type": "@NonNull String",
              "getter": "getLocale()"
            }
          }
        },
        "Address": {
          "package": "com.google.android.engage.common.datamodel.Address",
          "fields": {
            "city": {
              "type": "@NonNull String",
              "requirement": "Required",
              "setter": "setCity(@NonNull String)",
              "getter": "getCity()"
            },
            "country": {
              "type": "@NonNull String",
              "requirement": "Required",
              "setter": "setCountry(@NonNull String)",
              "getter": "getCountry()"
            },
            "displayAddress": {
              "type": "@NonNull String",
              "requirement": "Required",
              "setter": "setDisplayAddress(@NonNull String)",
              "getter": "getDisplayAddress()"
            },
            "streetAddress": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setStreetAddress(String)",
              "getter": "getStreetAddress()"
            },
            "state": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setState(String)",
              "getter": "getState()"
            },
            "zipCode": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setZipCode(String)",
              "getter": "getZipCode()"
            },
            "neighborhood": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setNeighborhood(String)",
              "getter": "getNeighborhood()"
            }
          }
        },
        "Badge": {
          "package": "com.google.android.engage.common.datamodel.Badge",
          "fields": {
            "text": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setText(String)",
              "getter": "getText()"
            },
            "image": {
              "type": "Image",
              "requirement": "Optional",
              "setter": "setImage(Image)",
              "getter": "getImage()"
            }
          }
        },
        "LocalizedTimestamp": {
          "package": "com.google.android.engage.common.datamodel.LocalizedTimestamp",
          "fields": {
            "timestamp": {
              "type": "Instant",
              "requirement": "Required",
              "setter": "setTimestamp(Instant)",
              "getter": "getTimestamp()"
            },
            "timezone": {
              "type": "DateTimeZone",
              "requirement": "Required",
              "setter": "setTimezone(DateTimeZone)",
              "getter": "getTimezone()"
            }
          }
        },
        "SignInCardEntity": {
          "package": "com.google.android.engage.common.datamodel.SignInCardEntity",
          "fields": {
            "actionText": {
              "type": "String",
              "requirement": "Required",
              "setter": "setActionText(String)",
              "getter": "getActionText()"
            },
            "actionUri": {
              "type": "Uri",
              "requirement": "Required",
              "setter": "setActionUri(Uri)",
              "getter": "getActionUri()"
            },
            "title": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setTitle(String)",
              "getter": "getTitle()"
            },
            "subtitle": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setSubtitle(String)",
              "getter": "getSubtitle()"
           < },
     >       "entityId": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setEntityId(String)",
              "getter":< &quo>t;getEntityId()"
            },
            "posterImages": {
              "type": "ListImage",
              "requirement": "Required",
              "adder": "addPosterImage(Image)",
              "getter": "getPosterImages()",
              "adderAll": "addPosterImages(ListImage)"
            }
          }
        },
        "GenericFeaturedEntit<y&quo>t;: {
          "package": "com.google.android.engage.common.datamodel.GenericFeaturedEntity",
          "fields": {
            "entityId": {
              "type":< "Str>ing",
              "requirement": "Optional",
              "setter": "setEntityId(String)",
              "getter": "getEntityId()"
            },
            "posterImages": {
              "type": "ListImage",
              "requirement": "Required",
              "adder": "addPosterImage(Image)",
              "getter": "getPosterImages()",
              "adderAll": "addPosterImages(ListImage)"
            },
            "actionUri": {
              "type": "Uri",
              "requirement": "Required",
              "setter":< ">;setActionUri(Uri)",
              "getter": "getActionUri()"
            },
            "title": {
             < "type>": "String",
              "requirement": "Optional",
           <   "s>etter": "setTitle(String)",
              "getter": "getTitle()"
            },
            "descripti<on&qu>ot;: {
              "type": "String",
              "requirement": "Optiona<l",
              "setter": &quo>t;setDescription(String)",
              "getter": "getDescription()"
            },
            "subtitles": {
              "type": "ListString<",>
              "requirement": "Optional",
              "adder": &q<uot;addSubtitle(S>tring)",
              "adderAll": "addSubtitles(ListString)"
            },
            "badges": {
              "type": "ListBadge",
              "requirement": "Optional",
              "<;add<er": "a>>ddBadge(Badge)",
              "adderAll": "addBadges(ListBadge)"
            },
            "contentCategories": {
              "type":< "List@Eligi>bleContentCategory int",
              "requirement": "Optional",
              "adder": "addContentCategory(@EligibleContentCategory int)",
              "adderAll": "addContentCategories(ListInteger)"
            },
            "displayTimeWindows": {
              "type": "ListDisplayTimeWindow",
              "requirement": "Optional",
              "adder": "addDisplayTimeWindow(DisplayTimeWindow)",
              "getter": "getDisplayTimeWindows()"
            },
            "allDisplayTimeWindows": {
              "type": "ListListDisplayTimeWindow",
              "requirement": "Optional",
              "adder": "addAllDisplayTimeWindow(DisplayTimeWindow)",
              "adderAll": "addAllDisplayTimeWindow(ListDisplayTimeWindow)"
            }
          }
        },
        "SubscriptionEntity": {
          "package": "com.google.android.engage.common.datamodel.SubscriptionEntity",
          "fields": {}
        },
        "UserSettingsCardEntity": {
          "package": "com.google.android.engage.common.datamodel.UserSettingsCardEntity",
          "fields": {
            "actionText": {
              "typ<e": ">String",
              "requirement": "Required",
              "setter": "setActionText(String)",
              "getter": "getActionText()"
            },
            <">;actionUri": {
              "type": "Uri",
              "requirement": "Required",
              "setter": "setActionUri(Uri)",
              "getter": "getActionUri()"
            },
            "title": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setTitle(String)",
              "getter": "g<etTit>le()"
            },
            "subtitle": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setSubtitle(String)&quo<t;,
     >         "getter": "getSubtitle()"
            },
            "entityId": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setEntityId(String)",
              "getter": "getEntityId()"
            },
            "posterImages": {
              "type": "ListImage",
              "requirement": "Required",
              "adder": "addPosterImage(Image)",
              "getter": "getPosterImages()",
              "adderAll": "addPosterImages(ListImage)"
            }
          }
        },
    <    &q>uot;ArticleEntity": {
          "package": "com.google.android.engage.common.datamodel.ArticleEntity",
          "f<ields">: {
            "entityId": {
              "type": "St<ring">,
              "requirement": "Optional",
              "setter": "setEntityId(String)",
              "getter": &qu<ot;ge>tEntityId()"
            },
            "posterImages": {
       <       "type": "ListIma>ge",
              "requirement": "Required",
              "adder": "addPosterImage(Image)",
              "getter": "getPosterImages()"<;,
        >      "adderAll": "addPosterImages(ListImage)"
            },
            "actionUri": {
              "type": "Uri",
              "requirement": "Required",
              "setter": "setActionUri(Uri)",
              "getter": "getActionUri()"
            },
            "title": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setTitle(String)",
              "getter": "getTitle()"
            },
            "description": {
              "type": "String",
              "requirement": "Optional",
              "setter": "setDescription(String)",
              "getter": "getDescription()"
            },
            "subtitles": {
              "type": "ListString",
              "requirement": "Optional",
              "adder": "addSubtitle(String)",
              "adderAll": "addSubtitles(ListString)"
            },
            "badges": {
              "type": "ListBadge",
              "requirement": "Optional",
           <   "adder&qu>ot;: "addBadge(Badge)",
              "adderAll": "addBadges(ListBadge)"
            },
            "contentCategories": {
              "type": "List@EligibleContentCategory int",
      <    <    "requirement">>: "Optional",
              "adder": "addContentCategory(@EligibleContentCategory int)",
              "adderAll": "addContentCat<egories(ListInteg>er)"
            },
            "progressPercentage": {
              "type": "Integer",
              "requirement": "Required",
              "setter": "setProgressPercentage(int)",
              "getter": "getProgressPercentage()",
              "requiredFor": [
                "ContinuationCluster"
              ]
            },
            "lastEngagementTimestampMillis": {
              "type": "Long",
              "requirement": "Required",
              "setter": "setLastEngagementTimestampMillis(long)",
              "getter": "getLastEngagementTimestampMillis()",
              "requiredFor": [
                "ContinuationCluster"
              ]
            },
            "source": {
              "type": "Badge",
              "requirement": "Optional",
              "setter": "setSource(Badge)",
              "getter": "getSource()"
            },
            "lastContentPublishTimestampMillis": {
              "type": "Long",
              "requirement": "Optional",
              "setter": "setLastContentPublishTimestampMillis(Long)",
              "getter": "getLastContentPublishTimestampMillis()"
            },
            "displayTimeWindows": {
              "type": "ListDisplayTimeWindow",
              "requirement": "Optional",
              "adder": "addDisplayTimeWindow(DisplayTimeWindow)",
              "getter": "getDisplayTimeWindows()"
            },
            "allDisplayTimeWindows": {
              "type": "ListListDisplayTimeWindow",
              "requirement": "Optional",
              "adder": "addAllDisplayTimeWindow(DisplayTimeWindow)",
              "adderAll": "addAllDisplayTimeWindow(ListDisplayTimeWindow)"
            }
          }
        }
      },
      "intents": {
        "ACTION_PUBLISH_RECOMMENDATION": "com.google.android.engage.action.PUBLISH_RECOMMENDATION",
        "ACTION_PUBLISH_FEATURED": "com.google.android.engage.action.PUBLISH_FEATURED",
        "ACTION_PUBLISH_CONTINUATION": "com.google.android.engage.action.PUBLISH_CONTINUATION"
      },
      "imports": [
        "com.google.android.engage.service.AppEngagePublishClient",
        "com.google.android.engage.service.AppEngageErrorCode",
        "com.google.android.engage.service.AppEngageException",
        "com.google.android.engage.service.AppEngagePublishStatusCode"
      ]
    }