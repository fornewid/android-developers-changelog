---
title: https://developer.android.com/design/ui/cars/guides/foundations/customize-app
url: https://developer.android.com/design/ui/cars/guides/foundations/customize-app
source: md.txt
---

# Customize your app

Once you've determined the sequences of templates for your app task, you can customize the content of each template and some of the styling for your app.

To learn about which aspects of the overall visual design you can customize, see[Visual design customization](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#visual-design-customization), which includes[App customization examples](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#app-customization-examples). For AAOS versions of your app, be aware that vehicle OEMs can adjust the styling to fit their vehicles, as shown in[Vehicle OEM customization examples](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#vehicle-oem-customization-examples).

To learn about customization options for specific templates, see[Templates](https://developer.android.com/design/ui/cars/guides/templates/overview).

## Visual design customization

While the app library determines the template layouts and default styling, app designers and vehicle OEMs both contribute to custom aspects of the visual design.

|          Aspect of UI          |                                                              What the library determines                                                               |                                                                                                                                                                   What apps determine or customize                                                                                                                                                                    |                                                                                   What vehicle OEMs can customize                                                                                   |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Images and iconography**     | Iconography for standard elements, such as back button and loading spinner                                                                             | Apps provide all images and iconography (see[Material icons](https://fonts.google.com/icons?selected=Material+Icons)and[Google Play icon specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications)), except as noted at left                                                                                         |                                                                                                                                                                                                     |
| **Layout, sizing and shapes**  | Default layout, plus size and shapes of all elements (defaults are standard in Android Auto version of app)                                            | - Whether images and icons are "large" or "small" - Whether[tabs](https://developer.android.com/design/ui/cars/guides/templates/tab-template)appear at the top of certain templates for switching views - Whether a second map displays in the cluster ([Navigation template](https://developer.android.com/design/ui/cars/guides/templates/navigation-template)only) | Adjustments to size, shape, button locations and proportions of template elements in AAOS versions of app (or example, the exact sizing for "large" and "small" images and icons in their vehicles) |
| **Typography and text length** | Font family and size in Android Auto version of app (see[Typography](https://developers.google.com/cars/design/android-auto/design-system/typography)) | Longer and shorter[variants of text strings](https://developer.android.com/training/cars/apps#multi-text), in some cases, to accommodate differing amounts of space on different car screens                                                                                                                                                                          | Font family and size in AAOS versions of app                                                                                                                                                        |
| **Color**                      | Default colors in Android Auto version of app (except those supplied by apps, noted at right)                                                          | Colors of place-list markers, some text elements, and some background colors (review the next section,[Color customization](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#color-customization)for more information).                                                                                                                  | Adjustments to default \& app-supplied colors to as needed to blend with vehicle UIs in AAOS versions of app                                                                                        |

## Color customization

Apps can provide colors for elements of certain templates, as noted in the following list. For AAOS versions of your app, vehicle OEMs can make some adjustments.

Apps can customize the following:

- **Text color** in secondary line of list[rows](https://developer.android.com/design/ui/cars/guides/components/row)(car maker controls color of primary line for AAOS)
- **Button text color**
- **Button background colors** (except on[action strip](https://developer.android.com/design/ui/cars/guides/components/action-strip)and[map action strip](https://developer.android.com/design/ui/cars/guides/components/map-action-strip))
- **Place-list marker colors**
- **Routing-card elements** : background color, images, and color of duration value in trip estimate (within[Navigation template requirements](https://developer.android.com/design/ui/cars/guides/templates/navigation-template#requirements))
- **Turn-by-turn notifications**(background color)

| **Note:** When customizing text color, you can choose from 4 standard colors or up to 2 custom accents. You can choose any color for the other items in the list.

Examples of customized template components are shown in[App customization examples](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#app-customization-examples)and[Vehicle OEM customization examples](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#vehicle-oem-customization-examples).

### Choose colors for your app

For most custom styling (other than the exceptions noted in the previous section), apps have the following color options:

- **Provide up to 2 custom accent colors**(with light and dark variants, to be applied as appropriate by Android Auto, or by vehicle OEMs for AAOS versions of apps)
- **Choose from 4 standard Android for Cars colors**(current versions shown at right; these may change in the future)

<br />

![Standard colors for Android for Cars apps](https://developer.android.com/static/images/design/ui/cars/foundations/colors-standard.png)**Figure 1.**Standard colors![Accent colors for Android for Cars apps](https://developer.android.com/static/images/design/ui/cars/foundations/colors-accent.png)**Figure 2.**Sample accent colors

<br />

Judicious use of color helps to focus the intent of a design. Be cautious about using colors when they don't serve a function.
| **Note:** For legibility while driving, make sure contrast between foreground and background colors meets contrast requirements of 4.5:1.

## App customization Examples

![App customization examples](https://developer.android.com/static/images/design/ui/cars/foundations/app-customization-examples.png)**Figure 3.**Examples of App customization.

## Vehicle OEM customization examples

These examples show additional style customizations a vehicle OEM might apply to the AAOS version of an app. While the color of the routing card comes from the app, vehicle OEMs customize the fonts, theming, and shapes for the routing card, buttons, and ETA card. They can also adjust button width, as shown in[Customize buttons](https://developer.android.com/design/ui/cars/guides/foundations/customize-app#customize-button).  
![Standard colors for Android for Cars apps](https://developer.android.com/static/images/design/ui/cars/foundations/oem-daytime-navigation.png)**Figure 4.**OEM daytime navigation view![Accent colors for Android for Cars apps](https://developer.android.com/static/images/design/ui/cars/foundations/oem-nighttime-navigation.png)**Figure 5.**OEM nighttime navigation view

<br />

### Customize button width, color, and shape

These examples highlight how OEMs can customize button width, color, and shape, in the AAOS version of an app.

For the button the app designated as the[primary button](https://developer.android.com/design/ui/cars/guides/components/button#primary-buttons), OEMs can decide whether to use an app accent color or their own accent color. They can also choose whether to put the primary button on the left or on the right, to accommodate situations such as vehicles with right-hand drive.  
![Standard colors for OEM buttons](https://developer.android.com/static/images/design/ui/cars/foundations/oem-button-standard-colors.png)**Figure 6.**Example of primary button on left with standard colors![Custom colors for OEM buttons](https://developer.android.com/static/images/design/ui/cars/foundations/oem-button-custom-colors.png)**Figure 7.**Example of primary button on right with custom colors

<br />