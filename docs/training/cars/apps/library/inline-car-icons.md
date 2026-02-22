---
title: https://developer.android.com/training/cars/apps/library/inline-car-icons
url: https://developer.android.com/training/cars/apps/library/inline-car-icons
source: md.txt
---

You can add icons inline with text to enrich your app's visual appeal using
[`CarIconSpan`](https://developer.android.com/reference/kotlin/androidx/car/app/model/CarIconSpan). See the documentation for [`CarIconSpan.create`](https://developer.android.com/reference/kotlin/androidx/car/app/model/CarIconSpan#create) for more
information on creating these spans. See [Spantastic text styling with Spans](https://medium.com/androiddevelopers/spantastic-text-styling-with-spans-17b0c16b4568)
for an overview of how text styling with spans work.
**Note:** On hosts that support a Car App API level of less than five, raw text is rendered instead of the `CarIcon`.  

### Kotlin

    val rating = SpannableString("Rating: 4.5 stars")
    rating.setSpan(
        CarIconSpan.create(
            // Create a CarIcon with an image of four and a half stars
            CarIcon.Builder(...).build(),
            // Align the CarIcon to the baseline of the text
            CarIconSpan.ALIGN_BASELINE
        ),
        // The start index of the span (index of the character '4')
        8,
        // The end index of the span (index of the last 's' in "stars")
        16,
        Spanned.SPAN_INCLUSIVE_INCLUSIVE
    )

    val row = Row.Builder()
        ...
        .addText(rating)
        .build()

### Java

    SpannableString rating = new SpannableString("Rating: 4.5 stars");
    rating.setSpan(
            CarIconSpan.create(
                    // Create a CarIcon with an image of four and a half stars
                    new CarIcon.Builder(...).build(),
                    // Align the CarIcon to the baseline of the text
                    CarIconSpan.ALIGN_BASELINE
            ),
            // The start index of the span (index of the character '4')
            8,
            // The end index of the span (index of the last 's' in "stars")
            16,
            Spanned.SPAN_INCLUSIVE_INCLUSIVE
    );
    Row row = new Row.Builder()
            ...
            .addText(rating)
            .build();