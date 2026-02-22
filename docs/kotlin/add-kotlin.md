---
title: https://developer.android.com/kotlin/add-kotlin
url: https://developer.android.com/kotlin/add-kotlin
source: md.txt
---

Android Studio provides [full support for Kotlin](https://developer.android.com/kotlin), enabling you to add
Kotlin files to your existing project and convert Java language code to Kotlin.
You can then use all of Android Studio's existing tools with your Kotlin code,
including autocomplete, lint checking, refactoring, debugging, and more.

If you're starting a new project and want to use Kotlin, see
[Create a project](https://developer.android.com/studio/projects/create-project).

For samples, check out our
[Kotlin code samples](https://developer.android.com/samples/index?language=kotlin).

## Add Kotlin to an existing project

To add Kotlin to your project, do the following:

1. Click **File \> New** , and choose one of the various Android templates, such
   as a new blank **Fragment** , as shown in figure 1. If you don't see the list
   of templates in this menu, first open the **Project** window, and select your
   app module.

   ![create a new blank fragment](https://developer.android.com/static/images/kotlin/choose-template.png) Figure 1. Choose from the available templates, such as fragment or activity.
2. In the wizard that appears, choose **Kotlin** for the **Source Language** .
   Figure 2 shows the **New Android Activity** dialog for when you want to
   create a new activity.

   ![dialog that lets you choose Kotlin for your source language](https://developer.android.com/static/images/kotlin/choose-source-language.png) Figure 2. A **New Android Activity** dialog where you can choose **Kotlin** as your **Source Language**.
3. Continue through the wizard.

Alternatively, you can click **File \> New \> Kotlin File/Class** to create a
basic Kotlin file. If you don't see this option, open the **Project** window and
select the **java** directory. The **New Kotlin File/Class** window lets you
define the file name and provides several choices for the file type: **File** ,
**Class** , **Interface** , **Enum Class** , or **Object** . The choice you make
determines the basic scaffolding created for you in the new Kotlin file. If you
choose **Class** , Android Studio creates a new Kotlin source file with the given
name and a matching class definition. If you choose **Interface**, an interface
is declared in the file, and so on.

If this is the first time you have added a new Kotlin class or file to your
project directly (not using the Android templates), Android Studio displays a
warning that Kotlin is not configured in the project, as shown in figure 3.
Configure Kotlin by clicking **Configure** either in the upper right corner of
the editor or in the **event log alert** that pops up in the lower-right corner.
![warning dialog that prompts you to configure Kotlin for your
project](https://developer.android.com/static/images/kotlin/configure-kotlin.png) Figure 3. Android Studio displays a warning dialog when Kotlin isn't configured for your project.

Choose the option to configure Kotlin for **All modules containing Kotlin
files** when prompted, as shown in figure 4:
![choose to configure Kotlin for all modules that contain Kotlin code](https://developer.android.com/static/images/kotlin/all-modules.png) Figure 4. Choose to configure Kotlin for all modules that contain Kotlin code.

Once you click **OK** , Android Studio adds Kotlin to your project classpath and
applies the Kotlin Android plugin to each module that contains Kotlin files.
Your `build.gradle` files should look similar to the examples below:  

### Groovy

```groovy
// Project build.gradle file.
buildscript {
    ext.kotlin_version = '1.4.10'
    ...
    dependencies {
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}
```

### Kotlin

```kotlin
// Project build.gradle.kts file.
buildscript {
    extra["kotlin_version"] = "1.4.10"
    ...
    dependencies {
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version")
    }
}
```  

### Groovy

```groovy
// Inside each module using kotlin
plugins {
    ...
    id 'kotlin-android'
}

...

dependencies {
    implementation 'androidx.core:core-ktx:1.3.2'
    implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
}
```

### Kotlin

```kotlin
// Inside each module using kotlin
plugins {
    ...
    kotlin("android")
}

...

val kotlin_version: String by rootProject.extra

dependencies {
    implementation("androidx.core:core-ktx:1.3.2")
    implementation("org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version")
}
```

## Source organization

By default, new Kotlin files are saved in `src/main/java/`, which makes it easy
to see both Kotlin and Java files in one location. If you'd prefer to separate
your Kotlin files from your Java files, you can put Kotlin files under
`src/main/kotlin/` instead. If you do this, then you also need to include this
directory in your [`sourceSets`](https://developer.android.com/studio/build#sourcesets)
configuration, as shown below:  

### Groovy

```groovy
android {
    sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }
}
```

### Kotlin

```kotlin
android {
    sourceSets {
        getByName("main") {
            java.srcDir("src/main/kotlin")
        }
    }
}
```

## Convert existing Java code to Kotlin code

To convert Java code to Kotlin, open the Java file in Android Studio, and select
**Code \> Convert Java File to Kotlin File** . Alternatively, create a new Kotlin
file (**File \> New \> Kotlin File/Class** ), and then paste your Java code into
that file. Android Studio then displays a prompt and offers to convert your code
to Kotlin, as shown in figure 5. Click **Yes** to convert. You can optionally
check **Don't show this dialog next time**, which makes future conversions
automatic.
![choose to configure Kotlin for all modules that contain Kotlin code](https://developer.android.com/static/images/kotlin/convert-code.png) Figure 5. Android Studio can convert Java code to Kotlin.

## Code conversion and nullability

Android Studio's conversion process produces functionally-equivalent Kotlin code
that compiles and runs. However, it's likely that you need to make additional
optimizations to the converted code. For example, you might want to refine how
the converted code handles nullable types.

In Android, it is common to delay initialization of `View` objects and other
components until the fragment or activity they are attached to reaches the
appropriate lifecycle state. For example, you may have a reference to a
button in one of your fragments, as demonstrated in the following snippet:  

    public class JavaFragment extends Fragment {

        // Null until onCreateView.
        private Button button;

        @Override
        public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                Bundle savedInstanceState) {
            View root = inflater.inflate(R.layout.fragment_content, container,false);

            // Get a reference to the button in the view, only after the root view is inflated.
            button = root.findViewById(R.id.button);

            return root;
        }

        @Override
        public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
            super.onViewCreated(view, savedInstanceState);

            // Not null at this point of time when onViewCreated runs
            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ...
                }
            });
        }
    }

Even though the button variable is nullable, for all practical purposes it
should never be null when used in this example. However, since its value is not
assigned at the point of construction, the generated Kotlin code treats `Button`
as a nullable type and uses the non-null assertion operator to unwrap the button
when adding a click listener, as shown below:  

    class JavaFragment : Fragment() {

        // Null until onCreateView.
        private var button: Button? = null

        override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                savedInstanceState: Bundle?): View? {
            ...
            // Get a reference to the button in the view, only after the root view is inflated.
            button = root.findViewById(R.id.button)
            ...
        }

        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            super.onViewCreated(view, savedInstanceState)

            // Not null at the point of time when onViewCreated fires 
            // but force unwrapped nonetheless
            button!!.setOnClickListener { }
        }
    }

This conversion is less ideal than using `lateinit` for this case, because you
are forced to unwrap the button reference with a non-null assertion or safe-call
operator in every place it is accessed.
| **Note:** This example doesn't mean that you should always avoid nullable types. Generally, this pattern of using `lateinit` applies to variables which are never expected to be `null` but cannot be initialized where they are defined, as is the case with `View` references inside of the fragment or activity in which they live.

In other cases, where `null` is a valid variable assignment based on your
application's use case, using a safe-call (?.) operator with a terminating elvis
operator (?:) operator may be a more appropriate way to safely unwrap the
nullable object or coerce to a sensible non-null default value. Android Studio
does not have enough information to make this determination during the
conversion process. While it defaults to the non-null assertion, you should
follow up and adjust the converted code as needed.

## More information

For more information about using both Kotlin and Java code in your project, see
[Calling Java code from Kotlin](https://kotlinlang.org/docs/reference/java-interop.html).

For more information about using Kotlin in enterprise scenarios, see
[Adopting Kotlin for large teams](https://developer.android.com/kotlin/adopt-for-large-teams).

For information about idiomatic Kotlin wrappers for existing Android APIs, see
[Android KTX](https://developer.android.com/kotlin/ktx).