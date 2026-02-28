---
title: https://developer.android.com/distribute/google-play/resources/icon-design-specifications
url: https://developer.android.com/distribute/google-play/resources/icon-design-specifications
source: md.txt
---

<br />

![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/hero.png)

Apps \& Games on Google Play are adopting a new icon system to better fit diverse
developer artwork to Google Play's various UI layouts, form factors, and
devices, as well as to bring consistency and a cleaner look to Google Play.

Uniformed shapes are visually more appealing and easier to digest. They help
users focus on the artwork, as opposed to the shape. They fix alignment issues
caused by random open space to better present surrounding information, such as
the title, rating, and price.


![Freeform icon examples](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/rounded-corners-freeform.png)

Freeform -- original format
![Uniformed icon examples](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/rounded-corners-uniformed.png)

Uniformed -- new format

<br />

This page describes the guidelines you should follow when creating assets for
your app's listing on Google Play. For example, because Google Play dynamically
renders rounded corners and drop shadows for your app icons, you should omit
them from your original assets.

**Important:** If instead you're interested in learning more about creating APK
launcher icons, which are separate from the Google Play icons described on this
page, see the resources below:

- [Android Adaptive Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive)  
  Follow these APK icon guidelines to learn how to create adaptive launcher icons introduced in Android 8.0 (API level 26).
- [Product icons](https://material.io/design/iconography/product-icons.html)  
  Discover Material Design principles for product icons, including guidelines for icon design, shapes, specs, and treatment.

## Creating assets

This section describes some guidelines you should follow when creating visual
assets for your app on Google Play.

### Attributes

Icon artwork can populate the entire asset space, or you can design and position
artwork elements such as logos onto the keyline grid. When placing your artwork,
use keylines as a guideline, not a hard rule.

When creating your artwork, ensure it conforms to the following:

- Final size: 512px x 512px
- Format: 32-bit PNG
- Color space: sRGB
- Max file size: 1024KB
- Shape: Full square -- Google Play dynamically handles masking. Radius will be equivalent to 30% of icon size.
- Shadow: None -- Google Play dynamically handles shadows. See 'Shadows' section below on including shadows within your artwork.


![Total asset size](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/attributes-size.png)

Total asset size
![Product icon keylines](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/attributes-size-keylines.png)

Product icon keylines

<br />

After the asset is uploaded, Google Play dynamically applies the rounded mask
and shadow to ensure consistency across all app/game icons.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/dynamic-process.png) On the left-hand side is your new icon asset. The following three images on the right-hand side show Google Play dynamic processing of the icon.

### Sizing

Utilize the full asset space as the background when dealing with minimalistic
artwork.

Use the keylines as guides for positioning artwork elements (i.e. logos).


![Full bleed artwork (final asset) example](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/rounded-corners-asset.png)

Your full bleed artwork (final asset)
![End result with shadows and rounded corners dynamically applied by Google Play](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/rounded-corners-applied.png)

End result with shadows and rounded corners dynamically applied by Google Play

<br />

Don't force your logo or artwork to fit the full asset space. Instead, utilize
the keyline grid.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/full-space-dont.png)

### Wrong

Don't force drastic brand \& artwork transformation to full bleed ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/full-space-do.png)

### Right

Place freeform icon artwork on keylines instead

Illustrated artwork typically works well as a full bleed icon.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/illustration-full-bleed-dont.png)

### Wrong

Don't scale down illustrated artwork onto keylines ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/illustration-full-bleed-do.png)

### Right

Utilize full asset space so your artwork occupies the entire icon

These are examples of icon elements that mislead users and violate Play's
Developer policies. Avoid all of the following practices, and refer to
Google Play's [metadata policy](https://support.google.com/googleplay/android-developer/answer/9898842?ref_topic=9877064)
and [user ratings, reviews, and installs policy](https://support.google.com/googleplay/android-developer/answer/9898684?ref_topic=9877064#zippy=%2Cexamples-of-common-violations-in-app-title-icon-or-developer-name)
for further guidance.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/ranking-dont.png)

### Don't

Don't use text or graphic elements to indicate ranking ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/deals-dont.png)

### Don't

Don't use text or graphic elements to promote deals or incentivize installs ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/play-program-dont.png)

### Don't

Don't use text or graphic elements to indicate participation in a Play program ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/mislead-users-dont.png)

### Don't

Don't use text or graphic elements that can mislead users

### Shadows

Google Play will dynamically add a drop shadow around the final icon once
uploaded.

When adding shadows inside your icon artwork, consider consistency with the
Android platform by following Google Material [guidelines](https://material.io/guidelines/style/icons.html#icons-product-icons).
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/shadows-dont.png)

### Wrong

Don't add drop shadows to your final asset ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/shadows-do.png)

### Right

You can create shadows and lighting within the artwork

### Corner radius

Google Play dynamically applies corner radius. This ensures consistency when the
icon is resized across different UI layouts. Radius will be equivalent to 30% of
icon size.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/corner-radius-dont.png)

### Wrong

Don't round the edges of your final asset ![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/corner-radius-do.png)

### Right

Fill your entire asset with artwork when possible

## Brand adaptation

If shapes are a critical part of a logo, do not force the artwork to full bleed.
Instead place it on the new keyline grid.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/brand-adaptation-full-bleed.png) From left to right: original icon asset, new icon asset (recommended adaptation), new icon rendered on Google Play.

If possible, pick a background color for your asset that's appropriate for your
brand and doesn't include any transparency. Transparent assets will display the
background color of Google Play UI.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/brand-adaptation-background.png) From left to right: original icon asset, new icon asset (recommended adaptation), new icon rendered on Google Play.

If there is no distinct shape around a logo defining it, place it on a full
bleed background.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/brand-adaptation-shape.png) From left to right: original icon asset, new icon asset (recommended adaptation), new icon rendered on Google Play.

If your artwork is flexible enough, consider tweaking it to fully utilize the
asset size. If that's not possible, revert to placing the logo on a keyline
grid.
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/brand-adaptation-keyline.png) From left to right: original icon asset, new icon asset (recommended adaptation), new icon rendered on Google Play.

## Legacy mode

Original icon assets that have not been updated per the new specifications will
eventually be migrated to legacy mode and scaled down 75% to the keyline grid
size (512 \* 0.75 = 384px).

Uploading an icon per the original specification will not be allowed as of May
2019. [See more details on timelines](https://android-developers.googleblog.com/2019/03/introducing-new-google-play-app-and.html).
![](https://developer.android.com/static/distribute/google-play/resources/icon-design-specifications/images/legacy-mode.png) Original icon assets will be automatically turned into legacy mode assets and be scaled down 75% to new keyline grid.

## Instructions for API users

Migration dates are slightly different for API users, but achieve the same end
result of migrating all icons to either the new specification or "legacy mode"
by June 24, 2019.

Before June 17, 2019, developers must use the Play Console to apply the new
specification to their icons. All calls to [Edits.images: upload](https://developers.google.com/android-publisher/api-ref/edits/images/upload)
will apply whichever specification is configured in the Play Console. There is
no way to apply the new specification via API. The `Edits.images: upload` call
may error if the old specification is still applied, and the error
message for that specific icon will point you to this specification. After
applying a new specification using the Play Console, you can retry the
`Edits.images: upload` call. You may need to retry the call multiple times
before it will succeed.

Beginning on June 17, 2019, all API calls to `Edits.images: upload` will
automatically apply the new specification to the icon. Following June 17, 2019,
you should only upload icons that are compatible with the new specification.

## Download design templates \& resources

To get started, download one of the provided asset templates:

- [Sketch template](https://services.google.com/fh/files/misc/playstore_icon_template.sketch.zip) (.sketch)
- [Illustrator template](https://services.google.com/fh/files/misc/playstore_icon_template.ai.zip) (.ai)
- [Photoshop template](https://services.google.com/fh/files/misc/playstore_icon_template.psd.zip) (.psd)