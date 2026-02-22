---
title: https://developer.android.com/develop/devices/assistant/app-actions-test-library
url: https://developer.android.com/develop/devices/assistant/app-actions-test-library
source: md.txt
---

# App Actions Test Library

The App Actions test library (AATL) provides capabilities to enable developers to test App Action fulfillment programmatically, automating testing that would normally be done using actual voice queries or the App Actions test tool.

The library helps ensure that the`shortcut.xml`configuration is correct and the described Android intent invocation succeeds. App Actions Test Library provides a mechanism to test your app's ability to fulfill given Google Assistant intent and parameters, by converting them into an Android deep link or Android intent, that can be asserted and used to instantiate an Android activity.

Testing is performed in the form of Robolectric unit or instrumented tests in the Android environment. This allows developers to comprehensively test their application by emulating the actual app behavior. For testing BIIs, custom intents, or deep link fulfillment, any instrumented testing framework can be used (UI Automator, Espresso, JUnit4, Appium, Detox, Calabash).

If the application is multi-lingual, developers can validate that the application's functionality is behaving correctly in different locales.

## How it works

To integrate App Actions Test Library within the app's testing environment, developers should create new or update existing Robolectric or instrumented tests on the`app`module of the app.

Test code contains the following parts:

- Initialization of the library instance, in the common setup method or in individual test cases.
- Each individual test calls the`fulfill`method of the library instance to produce the intent creation result.
- The developer then asserts the deep link or triggers the App fulfillment, and runs custom validation on the app state.

## Setup requirements

In order to use the test library, there is some initial app configuration required prior to adding the tests to your application.

### Configuration

To use the App Actions Test Library, make sure your app is configured as follows:

- Install the[Android Gradle Plugin](https://developer.android.com/reference/tools/gradle-api)(AGP)
- Include a`shortcuts.xml`file in the`res/xml`folder in the`app`module.
- Make sure`AndroidManifest.xml`includes`<meta-data
  android:name="android.app.shortcuts" android:resource="@xml/shortcuts" />`under either:
  - the`<application>`tag
  - the launcher`<activity>`tag
- Place the`<capability>`element inside the`<shortcuts>`element in`shortcuts.xml`

### Add App Actions Test Library dependencies

1. Add the Google repository to the list of project repositories in`settings.gradle`:

           allprojects {
               repositories {
                   ...
                   google()
               }
           }

2. In the app module`build.gradle`file, add the AATL dependencies:

           androidTestImplementation 'com.google.assistant.appactions:testing:1.0.0'

   Make sure to use the version number of the library you downloaded.

### Create integration tests

1. Create new tests under`app/src/androidTest`. For Robolectric tests, create them under`app/src/test`:

   ### Kotlin

   ```kotlin
     
       import android.content.Context
       import android.content.Intent
       import android.widget.TextView
       import androidx.test.core.app.ApplicationProvider
       import androidx.test.core.app.ActivityScenario
       import com.google.assistant.appactions.testing.aatl.AppActionsTestManager
       import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentIntentResult
       import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentResult
       import com.google.assistant.appactions.testing.aatl.fulfillment.FulfillmentType
       import com.google.common.collect.ImmutableMap
       import org.junit.Assert.assertEquals
       import org.junit.Before
       import org.junit.runner.RunWith
       import org.junit.Test
       import org.robolectric.RobolectricTestRunner
       ...
       @Test
       fun IntentTestExample() {
         val intentParams = mapOf("feature" to "settings")
         val intentName = "actions.intent.OPEN_APP_FEATURE"
         val result = aatl.fulfill(intentName, intentParams)

         assertEquals(FulfillmentType.INTENT, result.getFulfillmentType())

         val intentResult = result as AppActionsFulfillmentIntentResult
         val intent = intentResult.intent

         // Developer can choose to assert different relevant properties of the returned intent, such as the action, activity, package, scheme and so on
         assertEquals("youtube", intent.scheme)
         assertEquals("settings", intent.getStringExtra("featureParam"))
         assertEquals("actions.intent.OPEN_APP_FEATURE", intent.action)
         assertEquals("com.google.android.youtube/.MainActivity",
             intent.component.flattenToShortString())
         assertEquals("com.google.myapp", intent.package)

         // Developers can choose to use returned Android Intent to launch and assess the activity. Below are examples for how it will look like for Robolectric and Espresso tests.
         // Please note that the below part is just a possible example of how Android tests are validating Activity functionality correctness for given Android Intent.

         // Robolectric example:
         val activity = Robolectric.buildActivity(MainActivity::class.java,
           intentResult.intent).create().resume().get()

         val title: TextView = activity.findViewById(R.id.startActivityTitle)
         assertEquals(title?.text?.toString(), "Launching...")
       }
     
   ```

   ### Java

   ```java
     
       import android.content.Context;
       import android.content.Intent;
       import android.widget.TextView;
       import androidx.test.core.app.ApplicationProvider;
       import androidx.test.core.app.ActivityScenario;
       import com.google.assistant.appactions.testing.aatl.AppActionsTestManager;
       import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentIntentResult;
       import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentResult;
       import com.google.assistant.appactions.testing.aatl.fulfillment.FulfillmentType;
       import com.google.common.collect.ImmutableMap;
       import org.junit.Assert.assertEquals;
       import org.junit.Before;
       import org.junit.runner.RunWith;
       import org.junit.Test;
       import org.robolectric.RobolectricTestRunner;
       ...
       @Test
         public void IntentTestExample() throws Exception {
           Map<String, String> intentParams = ImmutableMap.of("feature", "settings");
           String intentName = "actions.intent.OPEN_APP_FEATURE";
           AppActionsFulfillmentResult result = aatl.fulfill(intentName, intentParams);

           assertEquals(FulfillmentType.INTENT, result.getFulfillmentType());

           AppActionsFulfillmentIntentResult intentResult = (AppActionsFulfillmentIntentResult) result;

           Intent intent = intentResult.getIntent();

           // Developer can choose to assert different relevant properties of the returned intent, such as the action, activity, package, or scheme
           assertEquals("settings", intent.getStringExtra("featureParam"));
           assertEquals("actions.intent.OPEN_APP_FEATURE", intent.getAction());
           assertEquals("com.google.android.youtube/.MainActivity", intent.getComponent().flattenToShortString());
           assertEquals("com.google.myapp", intent.getPackage());

           // Developers can choose to use returned Android Intent to launch and assess the   activity. Below are examples for how it will look like for Robolectric and  Espresso tests.
           // Please note that the below part is just a possible example of how Android tests are validating Activity functionality correctness for given Android Intent.

           // Robolectric example:
           MainActivity activity = Robolectric.buildActivity(MainActivity.class,intentResult.intent).create().resume().get();

           TextView title: TextView = activity.findViewById(R.id.startActivityTitle)
           assertEquals(title?.getText()?.toString(), "Launching...")
         }
     
   ```

   If you are using Espresso, you need to modify how you launch the Activity based on the AATL results. Here is an example for Espresso using the`ActivityScenario`method:  

   ### Kotlin

   ```kotlin
       
       ActivityScenario.launch<MainActivity>(intentResult.intent);
       Espresso.onView(ViewMatchers.withId(R.id.startActivityTitle))
         .check(ViewAssertions.matches(ViewMatchers.withText("Launching...")))
       
   ```

   ### Java

   ```java
       
         ActivityScenario.launch<MainActivity>(intentResult.intent);
         Espresso.onView(ViewMatchers.withId(R.id.startActivityTitle))
           .check(ViewAssertions.matches(ViewMatchers.withText("Launching...")))
       
   ```
2. Have the name and key properties in the parameter mappings match the parameters from the BII. For example,`exercisePlan.forExercise.name`matches the documentation for the parameter in[`GET_EXERCISE_PLAN`]().

3. Instantiate API instance with the Android Context parameter (obtained from[`ApplicationProvider`](https://developer.android.com/reference/androidx/test/core/app/ApplicationProvider)or[`InstrumentationRegistry`](https://developer.android.com/reference/androidx/test/InstrumentationRegistry)):

   - Single module app architecture:

   ### Kotlin

   ```kotlin
       
         private lateinit var aatl: AppActionsTestManager
         @Before
         fun init() {
           val appContext = ApplicationProvider.getApplicationContext()
           aatl = AppActionsTestManager(appContext)
         }
       
     
   ```

   ### Java

   ```java
       
         private AppActionsTestManager aatl;

         @Before
         public void init() {
           Context appContext = ApplicationProvider.getApplicationContext();
           aatl = new AppActionsTestManager(appContext);
         }
       
     
   ```
   - Multi-module app architecture:

   ### Kotlin

   ```kotlin
       
         private lateinit var aatl: AppActionsTestManager

         @Before
         fun init() {
           val appContext = ApplicationProvider.getApplicationContext()
           val lookupPackages = listOf("com.myapp.mainapp", "com.myapp.resources")
           aatl = AppActionsTestManager(appContext, lookupPackages)
         }
       
     
   ```

   ### Java

   ```java
       
         private AppActionsTestManager aatl;

         @Before
         public void init() throws Exception {

           Context appContext = ApplicationProvider.getApplicationContext();
           List<String> lookupPackages = Arrays.asList("com.myapp.mainapp","com.myapp.resources");
           aatl = new AppActionsTestManager(appContext, Optional.of(lookupPackages));
         }
       
     
   ```
4. Execute the`fulfill`method of the API and obtain the`AppActionsFulfillmentResult`object.

#### Perform assertions

The recommended way to assert App Actions Test Library is:

1. Assert the fulfillment type of the`AppActionsFulfillmentResult`. It has to be`FulfillmentType.INTENT`, or`FulfillmentType.UNFULFILLED`in order to test how the app behaves in case of unexpected BII requests.
2. There are 2 flavors of fulfillment:`INTENT`and`DEEPLINK`fulfillments.
   - Normally, the developer can differentiate between`INTENT`and`DEEPLINK`fulfillments by looking at the intent tag in`shortcuts.xml`that they are fulfilling by triggering the library.
   - If there is an url-template tag under the intent tag, this indicates that the`DEEPLINK`fulfills this intent.
   - If the result intent's`getData()`method returns a non-null object, this also indicates`DEEPLINK`fulfillment. Likewise, if`getData`returns`null`it means that it is an`INTENT`fulfillment.
3. For`INTENT`case, typecast`AppActionsFulfillmentResult`to`AppActionsIntentFulfillmentResult`, fetch the Android Intent by calling`getIntent`method and do one of the following:
   - Assert individual fields of Android Intent.
   - Assert the uri of an intent that is accessed through intent.getData.getHost method.
4. For`DEEPLINK`case, typecast`AppActionsFulfillmentResult`to`AppActionsIntentFulfillmentResult`(same as for the`INTENT`scenario above), fetch the Android Intent by calling`getIntent`method and assert the deeplink url (accessed through`intent.getData.getHost`).
5. For both`INTENT`and`DEEPLINK`, you can use the resulting intent to launch the activity with the chosen Android testing framework.

### Internationalization

If your App has multiple locales, you can configure tests to run a particular locale under-test. Alternatively, you can directly change the locale:  

### Kotlin

```kotlin
    
    import android.content.res.Configuration
    import java.util.Locale
    ...
    val newLocale = Locale("es")
    val conf = context.resources.configuration
    conf = Configuration(conf)
    conf.setLocale(newLocale)
    
  
```

### Java

```java
    
    Locale newLocale = new Locale("es");
    Configuration conf = context.getResources().getConfiguration();
    conf = new Configuration(conf);
    conf.setLocale(newLocale);
    
  
```

Here is an example of an AATL test configured for Spanish (ES) locale:  

### Kotlin

```kotlin
      
      import com.google.common.truth.Truth.assertThat
      import org.junit.Assert.assertEquals
      import android.content.Context
      import android.content.res.Configuration
      import androidx.test.platform.app.InstrumentationRegistry
      import com.google.assistant.appactions.testing.aatl.AppActionsTestManager
      import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentIntentResult
      import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentResult
      import com.google.assistant.appactions.testing.aatl.fulfillment.FulfillmentType
      import com.google.common.collect.ImmutableMap
      import java.util.Locale
      import org.junit.Before
      import org.junit.Test
      import org.junit.runner.RunWith
      import org.robolectric.RobolectricTestRunner

      @RunWith(RobolectricTestRunner::class)
      class ShortcutForDifferentLocaleTest {

        @Before
        fun setUp() {
          val context = InstrumentationRegistry.getInstrumentation().getContext()

          // change the device locale to 'es'
          val newLocale = Locale("es")
          val conf = context.resources.configuration
          conf = Configuration(conf)
          conf.setLocale(newLocale)

          val localizedContext = context.createConfigurationContext(conf)
        }

        @Test
        fun shortcutForDifferentLocale_succeeds() {
          val aatl = AppActionsTestManager(localizedContext)
          val intentName = "actions.intent.GET_EXERCISE_PLAN"
          val intentParams = ImmutableMap.of("exercisePlan.forExercise.name", "Running")

          val result = aatl.fulfill(intentName, intentParams)
          assertThat(result.getFulfillmentType()).isEqualTo(FulfillmentType.INTENT)

          val intentResult = result as AppActionsFulfillmentIntentResult

          assertThat(intentResult.getIntent().getData().toString())
            .isEqualTo("myexercise://browse?plan=running_weekly")
        }
      }
      
    
```

### Java

```java
      
      import static com.google.common.truth.Truth.assertThat;
      import static org.junit.Assert.assertEquals;

      import android.content.Context;
      import android.content.res.Configuration;
      import androidx.test.platform.app.InstrumentationRegistry;
      import com.google.assistant.appactions.testing.aatl.AppActionsTestManager;
      import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentIntentResult;
      import com.google.assistant.appactions.testing.aatl.fulfillment.AppActionsFulfillmentResult;
      import com.google.assistant.appactions.testing.aatl.fulfillment.FulfillmentType;
      import com.google.common.collect.ImmutableMap;
      import java.util.Locale;
      import org.junit.Before;
      import org.junit.Test;
      import org.junit.runner.RunWith;
      import org.robolectric.RobolectricTestRunner;

      @Test
      public void shortcutForDifferentLocale_succeeds() throws Exception {
        Context context = InstrumentationRegistry.getInstrumentation().getContext();

        // change the device locale to 'es'
        Locale newLocale = new Locale("es");
        Configuration conf = context.getResources().getConfiguration();
        conf = new Configuration(conf);
        conf.setLocale(newLocale);

        Context localizedContext = context.createConfigurationContext(conf);

        AppActionsTestManager aatl = new AppActionsTestManager(localizedContext);
        String intentName = "actions.intent.GET_EXERCISE_PLAN";
        ImmutableMap<String, String> intentParams = ImmutableMap.of("exercisePlan.forExercise.name", "Running");

        AppActionsFulfillmentResult result = aatl.fulfill(intentName, intentParams);
        assertThat(result.getFulfillmentType()).isEqualTo(FulfillmentType.INTENT);

        AppActionsFulfillmentIntentResult intentResult = (AppActionsFulfillmentIntentResult) result;

        assertThat(intentResult.getIntent().getData().toString())
          .isEqualTo("myexercise://browse?plan=running_weekly");
      }
      
    
```

## Troubleshoot

If your integration test fails unexpectedly, you can look for AATL log messages in the Android Studio logcat window to get the warning or error level message. You can also[increase the logging level](https://developer.android.com/studio/debug/logcat#configure-log-view)to capture more output from the library.

## Limitations

These are current limitations of the App Actions Test Library :

- AATL does not test Natural Language Understanding (NLU) or Speech-to-text (STT) features.
- AATL does not work when tests are in modules others than the default app module.
- AATL is only compatible with Android 7.0 "Nougat" (API level 24) and newer.