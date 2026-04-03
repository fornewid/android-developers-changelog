---
title: Inline complex XML resources  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/topics/resources/complex-xml-resources
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Inline complex XML resources Stay organized with collections Save and categorize content based on your preferences.




Certain resource types are a composition of multiple complex resources represented by XML files.
One example is an animated vector drawable, which is a drawable resource encapsulating a vector
drawable and an animation. This requires the use of at least three XML files, as shown in the
following
examples.

`res/drawable/avd.xml`
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:drawable="@drawable/vectordrawable" >
        <target
            android:name="rotationGroup"
            android:animation="@anim/rotation" />
    </animated-vector>
    ```

`res/drawable/vectordrawable.xml`
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <vector xmlns:android="http://schemas.android.com/apk/res/android"
        android:height="64dp"
        android:width="64dp"
        android:viewportHeight="600"
        android:viewportWidth="600" >
        <group
            android:name="rotationGroup"
            android:pivotX="300.0"
            android:pivotY="300.0"
            android:rotation="45.0" >
            <path
                android:fillColor="#000000"
                android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z" />
        </group>
    </vector>
    ```

`res/anim/rotation.xml`
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <objectAnimator xmlns:android="http://schemas.android.com/apk/android"
        android:duration="6000"
        android:propertyName="rotation"
        android:valueFrom="0"
        android:valueTo="360" />
    ```

If the vector drawable and animations are re-used elsewhere, this is the best way to implement an
animated vector drawable. But if these files are only used for this animated vector drawable,
then there is a more compact way to implement them.

Using AAPT’s inline resource format, you can define all three resources in the same XML file, as
shown in the following example.
For an animated vector drawable, put the file under `res/drawable/`.

`res/drawable/avd.xml`
:   ```
    <?xml version="1.0" encoding="utf-8"?>
    <animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:aapt="http://schemas.android.com/aapt" >

        <aapt:attr name="android:drawable" >
            <vector
                android:height="64dp"
                android:width="64dp"
                android:viewportHeight="600"
                android:viewportWidth="600" >
                <group
                    android:name="rotationGroup"
                    android:pivotX="300.0"
                    android:pivotY="300.0"
                    android:rotation="45.0" >
                    <path
                        android:fillColor="#000000"
                        android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z" />
                </group>
            </vector>
        </aapt:attr>

        <target android:name="rotationGroup">
            <aapt:attr name="android:animation" >
                <objectAnimator
                    android:duration="6000"
                    android:propertyName="rotation"
                    android:valueFrom="0"
                    android:valueTo="360" />
            </aapt:attr>
        </target>
    </animated-vector>
    ```

The XML tag `<aapt:attr >` tells AAPT to treat the tag’s child as a
resource and extract it into its own resource file. The value in the attribute name specifies where
to use the inline resource within the parent tag.

AAPT generates resource files and names for all the inline resources.
Applications built using this inline format are compatible with all versions of Android.