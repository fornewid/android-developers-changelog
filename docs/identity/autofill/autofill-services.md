---
title: https://developer.android.com/identity/autofill/autofill-services
url: https://developer.android.com/identity/autofill/autofill-services
source: md.txt
---

An autofill service is an app that makes it easier for users to fill out forms
by injecting data into the views of other apps. Autofill services can also
retrieve user data from the views in an app and store it for use at a later
time. Autofill services are usually provided by apps that manage user data, such
as password managers.

Android makes filling out forms easier with the autofill framework available in
Android 8.0 (API level 26) and higher. Users can take advantage of autofill
features only if there is an app that provides autofill services on their
device.

This page shows how to implement an autofill service in your app. If you're
looking for a code sample that shows how to implement a service, see the
`AutofillFramework` sample in [Java](https://github.com/android/input-samples/tree/main/AutofillFramework) or
[Kotlin](https://github.com/android/input-samples/tree/main/AutofillFrameworkKotlin). For further details about how autofill services work,
see the reference pages for the [`AutofillService`](https://developer.android.com/reference/android/service/autofill/AutofillService) and
[`AutofillManager`](https://developer.android.com/reference/android/view/autofill/AutofillManager) classes.
| **Note:** Beginning with Android 11, the platform allows keyboards and other input-method editors (*IMEs* ) to display autofill suggestions inline, instead of using a pulldown menu. For more information on how your autofill service can support this functionality, see [Integrate autofill with
| keyboards](https://developer.android.com/guide/topics/text/ime-autofill).
| **Note:** Autofill services must not use information for purposes other than providing suggestions.

## Manifest declarations and permissions

Apps that provide autofill services must include a declaration that describes
the implementation of the service. To specify the declaration, include a
[`<service>`](https://developer.android.com/guide/topics/manifest/service-element) element in the [app manifest](https://developer.android.com/guide/topics/manifest/manifest-intro). The `<service>` element must
include the following attributes and elements:

- [`android:name`](https://developer.android.com/guide/topics/manifest/service-element#nm) attribute that points to the subclass of `AutofillService` in the app that implements the service.
- [`android:permission`](https://developer.android.com/guide/topics/manifest/service-element#prmsn) attribute that declares the [`BIND_AUTOFILL_SERVICE`](https://developer.android.com/reference/android/Manifest.permission#BIND_AUTOFILL_SERVICE) permission.
- [`<intent-filter>`](https://developer.android.com/guide/topics/manifest/intent-filter-element) element whose mandatory [`<action>`](https://developer.android.com/guide/topics/manifest/action-element) child specifies the `android.service.autofill.AutofillService` action.
- Optional [`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element) element that you can use to provide additional configuration parameters for the service.

The following example shows an autofill service declaration:  

    <service
        android:name=".MyAutofillService"
        android:label="My Autofill Service"
        android:permission="android.permission.BIND_AUTOFILL_SERVICE">
        <intent-filter>
            <action android:name="android.service.autofill.AutofillService" />
        </intent-filter>
        <meta-data
            android:name="android.autofill"
            android:resource="@xml/service_configuration" />
    </service>

The `<meta-data>` element includes an [`android:resource`](https://developer.android.com/reference/android/R.styleable#AndroidManifestMetaData_resource) attribute that
points to an XML resource with further details about the service. The
`service_configuration` resource in the previous example specifies an activity
that allows users to configure the service. The following example shows the
`service_configuration` XML resource:  

    <autofill-service
      xmlns:android="http://schemas.android.com/apk/res/android"
      android:settingsActivity="com.example.android.SettingsActivity" />

For more information about XML resources, see [App resources overview](https://developer.android.com/guide/topics/resources/providing-resources).

## Prompt to enable the service

An app is used as the autofill service after it declares the
`BIND_AUTOFILL_SERVICE` permission and the user enables it in the device
settings. An app can verify whether it's the enabled service by calling the
[`hasEnabledAutofillServices()`](https://developer.android.com/reference/android/view/autofill/AutofillManager#hasEnabledAutofillServices()) method of the `AutofillManager` class.

If the app isn't the current autofill service, then it can request the user to
change the autofill settings by using the
[`ACTION_REQUEST_SET_AUTOFILL_SERVICE`](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_SET_AUTOFILL_SERVICE) intent. The intent returns a value
of [`RESULT_OK`](https://developer.android.com/reference/android/app/Activity#RESULT_OK) if the user selects an autofill service that matches the
package of the caller.
| **Note:** Be mindful of the frequency of requests to change the autofill settings that your app makes. Analyze the interactions users have with your app and request that they change the settings only in the appropriate scenarios.

## Fill out client views

The autofill service receives requests to fill out client views when the user
interacts with other apps. If the autofill service has user data that satisfies
the request, then it sends the data in the response. The Android system shows an
autofill UI with the available data, as shown in Figure 1:
![Autofill suggestion dropdown showing an available dataset](https://developer.android.com/static/images/guide/topics/text/autofill_sample_framed.png) **Figure 1.** Autofill UI displaying a dataset.

The autofill framework defines a workflow to fill out views that is designed to
minimize the time that the Android system is bound to the autofill service. In
each request, the Android system sends an [`AssistStructure`](https://developer.android.com/reference/android/app/assist/AssistStructure) object to the
service by calling the [`onFillRequest()`](https://developer.android.com/reference/android/service/autofill/AutofillService#onFillRequest(android.service.autofill.FillRequest,%20android.os.CancellationSignal,%20android.service.autofill.FillCallback)) method.

The autofill service checks whether it can satisfy the request with user data
that it previously stored. If it can satisfy the request, then the service
packages the data in [`Dataset`](https://developer.android.com/reference/android/service/autofill/Dataset) objects. The service calls the
[`onSuccess()`](https://developer.android.com/reference/android/service/autofill/FillCallback#onSuccess(android.service.autofill.FillResponse)) method, passing a [`FillResponse`](https://developer.android.com/reference/android/service/autofill/FillResponse) object that contains
the `Dataset` objects. If the service doesn't have data to satisfy the request,
it passes `null` to the `onSuccess()` method. The service calls the
[`onFailure()`](https://developer.android.com/reference/android/service/autofill/FillCallback#onFailure(java.lang.CharSequence)) method instead if there's an error processing the request.
For a detailed explanation of the workflow, see [the description on the
`AutofillService` reference page](https://developer.android.com/reference/android/service/autofill/AutofillService#BasicUsage).
| **Note:** Starting with Android 10, you can use the [`FillRequest.FLAG_COMPATIBILITY_MODE_REQUEST`](https://developer.android.com/reference/android/service/autofill/FillRequest#FLAG_COMPATIBILITY_MODE_REQUEST) flag to determine whether an autofill request was generated using compatibility mode.

The following code shows an example of the `onFillRequest()` method:  

### Kotlin

    override fun onFillRequest(
        request: FillRequest,
        cancellationSignal: CancellationSignal,
        callback: FillCallback
    ) {
        // Get the structure from the request
        val context: List<FillContext> = request.fillContexts
        val structure: AssistStructure = context[context.size - 1].structure

        // Traverse the structure looking for nodes to fill out
        val parsedStructure: ParsedStructure = parseStructure(structure)

        // Fetch user data that matches the fields
        val (username: String, password: String) = fetchUserData(parsedStructure)

        // Build the presentation of the datasets
        val usernamePresentation = RemoteViews(packageName, android.R.layout.simple_list_item_1)
        usernamePresentation.setTextViewText(android.R.id.text1, "my_username")
        val passwordPresentation = RemoteViews(packageName, android.R.layout.simple_list_item_1)
        passwordPresentation.setTextViewText(android.R.id.text1, "Password for my_username")

        // Add a dataset to the response
        val fillResponse: FillResponse = FillResponse.Builder()
                .addDataset(Dataset.Builder()
                        .setValue(
                                parsedStructure.usernameId,
                                AutofillValue.forText(username),
                                usernamePresentation
                        )
                        .setValue(
                                parsedStructure.passwordId,
                                AutofillValue.forText(password),
                                passwordPresentation
                        )
                        .build())
                .build()

        // If there are no errors, call onSuccess() and pass the response
        callback.onSuccess(fillResponse)
    }

    data class ParsedStructure(var usernameId: AutofillId, var passwordId: AutofillId)

    data class UserData(var username: String, var password: String)

### Java

    @Override
    public void onFillRequest(FillRequest request, CancellationSignal cancellationSignal, FillCallback callback) {
        // Get the structure from the request
        List<FillContext> context = request.getFillContexts();
        AssistStructure structure = context.get(context.size() - 1).getStructure();

        // Traverse the structure looking for nodes to fill out
        ParsedStructure parsedStructure = parseStructure(structure);

        // Fetch user data that matches the fields
        UserData userData = fetchUserData(parsedStructure);

        // Build the presentation of the datasets
        RemoteViews usernamePresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
        usernamePresentation.setTextViewText(android.R.id.text1, "my_username");
        RemoteViews passwordPresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
        passwordPresentation.setTextViewText(android.R.id.text1, "Password for my_username");

        // Add a dataset to the response
        FillResponse fillResponse = new FillResponse.Builder()
                .addDataset(new Dataset.Builder()
                        .setValue(parsedStructure.usernameId,
                                AutofillValue.forText(userData.username), usernamePresentation)
                        .setValue(parsedStructure.passwordId,
                                AutofillValue.forText(userData.password), passwordPresentation)
                        .build())
                .build();

        // If there are no errors, call onSuccess() and pass the response
        callback.onSuccess(fillResponse);
    }

    class ParsedStructure {
        AutofillId usernameId;
        AutofillId passwordId;
    }

    class UserData {
        String username;
        String password;
    }

A service can have more than one dataset that satisfies the request. In this
case, the Android system shows multiple options---one for each
dataset---in the autofill UI. The following code example shows how to
provide multiple datasets in a response:  

### Kotlin

    // Add multiple datasets to the response
    val fillResponse: FillResponse = FillResponse.Builder()
            .addDataset(Dataset.Builder()
                    .setValue(parsedStructure.usernameId,
                            AutofillValue.forText(user1Data.username), username1Presentation)
                    .setValue(parsedStructure.passwordId,
                            AutofillValue.forText(user1Data.password), password1Presentation)
                    .build())
            .addDataset(Dataset.Builder()
                    .setValue(parsedStructure.usernameId,
                            AutofillValue.forText(user2Data.username), username2Presentation)
                    .setValue(parsedStructure.passwordId,
                            AutofillValue.forText(user2Data.password), password2Presentation)
                    .build())
            .build()

### Java

    // Add multiple datasets to the response
    FillResponse fillResponse = new FillResponse.Builder()
            .addDataset(new Dataset.Builder()
                    .setValue(parsedStructure.usernameId,
                            AutofillValue.forText(user1Data.username), username1Presentation)
                    .setValue(parsedStructure.passwordId,
                            AutofillValue.forText(user1Data.password), password1Presentation)
                    .build())
            .addDataset(new Dataset.Builder()
                    .setValue(parsedStructure.usernameId,
                            AutofillValue.forText(user2Data.username), username2Presentation)
                    .setValue(parsedStructure.passwordId,
                            AutofillValue.forText(user2Data.password), password2Presentation)
                    .build())
            .build();

Autofill services can navigate the [`ViewNode`](https://developer.android.com/reference/android/app/assist/AssistStructure.ViewNode) objects in the
`AssistStructure` to retrieve the autofill data required to fulfill the request.
A service can retrieve autofill data using methods of the `ViewNode` class, such
as [`getAutofillId()`](https://developer.android.com/reference/android/app/assist/AssistStructure.ViewNode#getAutofillId()).

A service must be able to describe the contents of a view to check whether it
can satisfy the request. Using the [`autofillHints`](https://developer.android.com/reference/android/R.styleable#View_autofillHints) attribute is the first
approach that a service must use to describe the contents of a view. However,
client apps must explicitly provide the attribute in their views before it is
available to the service.

If a client app doesn't provide the `autofillHints` attribute, a service must
use its own heuristics to describe the contents. The service can use methods
from other classes, such as [`getText()`](https://developer.android.com/reference/android/widget/EditText#getText()) or [`getHint()`](https://developer.android.com/reference/com/google/android/material/textfield/TextInputLayout#getHint()), to get
information about the contents of the view. For more information, see [Provide
hints for autofill](https://developer.android.com/guide/topics/text/autofill-optimize#hints).

The following example shows how to traverse the `AssistStructure` and retrieve
autofill data from a `ViewNode` object:  

### Kotlin

    fun traverseStructure(structure: AssistStructure) {
        val windowNodes: List<AssistStructure.WindowNode> =
                structure.run {
                    (0 until windowNodeCount).map { getWindowNodeAt(it) }
                }

        windowNodes.forEach { windowNode: AssistStructure.WindowNode ->
            val viewNode: ViewNode? = windowNode.rootViewNode
            traverseNode(viewNode)
        }
    }

    fun traverseNode(viewNode: ViewNode?) {
        if (viewNode?.autofillHints?.isNotEmpty() == true) {
            // If the client app provides autofill hints, you can obtain them using
            // viewNode.getAutofillHints();
        } else {
            // Or use your own heuristics to describe the contents of a view
            // using methods such as getText() or getHint()
        }

        val children: List<ViewNode>? =
                viewNode?.run {
                    (0 until childCount).map { getChildAt(it) }
                }

        children?.forEach { childNode: ViewNode ->
            traverseNode(childNode)
        }
    }

### Java

    public void traverseStructure(AssistStructure structure) {
        int nodes = structure.getWindowNodeCount();

        for (int i = 0; i < nodes; i++) {
            WindowNode windowNode = structure.getWindowNodeAt(i);
            ViewNode viewNode = windowNode.getRootViewNode();
            traverseNode(viewNode);
        }
    }

    public void traverseNode(ViewNode viewNode) {
        if(viewNode.getAutofillHints() != null && viewNode.getAutofillHints().length > 0) {
            // If the client app provides autofill hints, you can obtain them using
            // viewNode.getAutofillHints();
        } else {
            // Or use your own heuristics to describe the contents of a view
            // using methods such as getText() or getHint()
        }

        for(int i = 0; i < viewNode.getChildCount(); i++) {
            ViewNode childNode = viewNode.getChildAt(i);
            traverseNode(childNode);
        }
    }

| **Note:** Most views provide `autofillHints` attributes that comply with the list of `AUTOFILL_HINT` values included in the [`View`](https://developer.android.com/reference/android/view/View) class. However, views such as [`HtmlInfo`](https://developer.android.com/reference/android/view/ViewStructure.HtmlInfo) are more likely to be compliant with the attributes listed on the [W3C autocomplete attribute](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofilling-form-controls%3A-the-autocomplete-attribute) page.

## Save user data

An autofill service needs user data to fill out views in apps. When users
manually fill out a view, they're prompted to save the data to the current
autofill service, as shown in Figure 2.
![System dialog prompting the user to save autofill data to the service](https://developer.android.com/static/images/guide/topics/text/autofill_save.png) **Figure 2.** Autofill save UI.

To save the data, the service must indicate it is interested in storing the data
for future use. Before the Android system sends a request to save the data,
there is a fill request where the service has the opportunity to fill out the
views. To indicate that it is interested in saving the data, the service
includes a [`SaveInfo`](https://developer.android.com/reference/android/service/autofill/SaveInfo) object in the response to the fill request. The
`SaveInfo` object contains at least the following data:

- The type of user data that is saved. For a list of the available `SAVE_DATA` values, see [`SaveInfo`](https://developer.android.com/reference/android/service/autofill/SaveInfo).
- The minimum set of views that need to be changed to trigger a save request. For example, a login form typically requires the user to update the `username` and `password` views to trigger a save request.

A `SaveInfo` object is associated with a `FillResponse` object, as shown in the
following code example:  

### Kotlin

    override fun onFillRequest(
        request: FillRequest,
        cancellationSignal: CancellationSignal,
        callback: FillCallback
    ) {
        // ...
        // Builder object requires a non-null presentation
        val notUsed = RemoteViews(packageName, android.R.layout.simple_list_item_1)

        val fillResponse: FillResponse = FillResponse.Builder()
                .addDataset(
                        Dataset.Builder()
                                .setValue(parsedStructure.usernameId, null, notUsed)
                                .setValue(parsedStructure.passwordId, null, notUsed)
                                .build()
                )
                .setSaveInfo(
                        SaveInfo.Builder(
                                SaveInfo.SAVE_DATA_TYPE_USERNAME or SaveInfo.SAVE_DATA_TYPE_PASSWORD,
                                arrayOf(parsedStructure.usernameId, parsedStructure.passwordId)
                        ).build()
                )
                .build()
        // ...
    }

### Java

    @Override
    public void onFillRequest(FillRequest request, CancellationSignal cancellationSignal, FillCallback callback) {
        // ...
        // Builder object requires a non-null presentation
        RemoteViews notUsed = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);

        FillResponse fillResponse = new FillResponse.Builder()
                .addDataset(new Dataset.Builder()
                        .setValue(parsedStructure.usernameId, null, notUsed)
                        .setValue(parsedStructure.passwordId, null, notUsed)
                        .build())
                .setSaveInfo(new SaveInfo.Builder(
                        SaveInfo.SAVE_DATA_TYPE_USERNAME | SaveInfo.SAVE_DATA_TYPE_PASSWORD,
                        new AutofillId[] {parsedStructure.usernameId, parsedStructure.passwordId})
                        .build())
                .build();
        // ...
    }

The autofill service can implement logic to persist the user data in the
`onSaveRequest()` method, which is usually called after the client activity
finishes or when the client app calls [`commit()`](https://developer.android.com/reference/android/view/autofill/AutofillManager#commit()). The following code shows
an example of the `onSaveRequest()` method:  

### Kotlin

    override fun onSaveRequest(request: SaveRequest, callback: SaveCallback) {
        // Get the structure from the request
        val context: List<FillContext> = request.fillContexts
        val structure: AssistStructure = context[context.size - 1].structure

        // Traverse the structure looking for data to save
        traverseStructure(structure)

        // Persist the data - if there are no errors, call onSuccess()
        callback.onSuccess()
    }

### Java

    @Override
    public void onSaveRequest(SaveRequest request, SaveCallback callback) {
        // Get the structure from the request
        List<FillContext> context = request.getFillContexts();
        AssistStructure structure = context.get(context.size() - 1).getStructure();

        // Traverse the structure looking for data to save
        traverseStructure(structure);

        // Persist the data - if there are no errors, call onSuccess()
        callback.onSuccess();
    }

Autofill services must encrypt sensitive data before persisting it. However,
user data can include labels or data that isn't sensitive. For example, a user
account can include a label that marks the data as a *work* or a *personal*
account. Services must not encrypt labels. By not encrypting labels, services
can use the labels in presentation views if the user hasn't authenticated. Then,
services can substitute the labels with the actual data after the user
authenticates.

### Postpone the autofill save UI

Starting with Android 10, if you use multiple screens to implement an autofill
workflow---for example, one screen for the username field and another for
the password---you can postpone the autofill save UI by using the
[`SaveInfo.FLAG_DELAY_SAVE`](https://developer.android.com/reference/android/service/autofill/SaveInfo#FLAG_DELAY_SAVE) flag.

If this flag is set, the autofill save UI isn't triggered when the autofill
context associated with the `SaveInfo` response is committed. Instead, you can
use a separate activity within the same task to deliver future fill requests and
then show the UI using a save request. For more information, see
[`SaveInfo.FLAG_DELAY_SAVE`](https://developer.android.com/reference/android/service/autofill/SaveInfo#FLAG_DELAY_SAVE).

## Require user authentication

Autofill services can provide an additional level of security by requiring the
user to authenticate before it can fill out views. The following scenarios are
good candidates to implement user authentication:

- The user data in the app needs to be unlocked using a primary password or a fingerprint scan.
- A specific dataset needs to be unlocked, such as credit card details by using a card verification code (CVC).

In a scenario where the service requires user authentication before unlocking
the data, the service can present boilerplate data or a label and specify the
[`Intent`](https://developer.android.com/reference/android/content/Intent) that handles authentication. If you need additional data to
process the request after the authentication flow is done, you can add such data
to the intent. Your authentication activity can then return the data to the
`AutofillService` class in your app.

The following code example shows how to specify that the request requires
authentication:  

### Kotlin

    val authPresentation = RemoteViews(packageName, android.R.layout.simple_list_item_1).apply {
        setTextViewText(android.R.id.text1, "requires authentication")
    }
    val authIntent = Intent(this, AuthActivity::class.java).apply {
        // Send any additional data required to complete the request
        putExtra(MY_EXTRA_DATASET_NAME, "my_dataset")
    }

    val intentSender: IntentSender = PendingIntent.getActivity(
            this,
            1001,
            authIntent,
            PendingIntent.FLAG_CANCEL_CURRENT
    ).intentSender

    // Build a FillResponse object that requires authentication
    val fillResponse: FillResponse = FillResponse.Builder()
            .setAuthentication(autofillIds, intentSender, authPresentation)
            .build()

### Java

    RemoteViews authPresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
    authPresentation.setTextViewText(android.R.id.text1, "requires authentication");
    Intent authIntent = new Intent(this, AuthActivity.class);

    // Send any additional data required to complete the request
    authIntent.putExtra(MY_EXTRA_DATASET_NAME, "my_dataset");
    IntentSender intentSender = PendingIntent.getActivity(
                    this,
                    1001,
                    authIntent,
                    PendingIntent.FLAG_CANCEL_CURRENT
            ).getIntentSender();

    // Build a FillResponse object that requires authentication
    FillResponse fillResponse = new FillResponse.Builder()
            .setAuthentication(autofillIds, intentSender, authPresentation)
            .build();

Once the activity completes the authentication flow, it must call the
[`setResult()`](https://developer.android.com/reference/android/app/Activity#setResult(int)) method, passing a `RESULT_OK` value, and set the
[`EXTRA_AUTHENTICATION_RESULT`](https://developer.android.com/reference/android/view/autofill/AutofillManager#EXTRA_AUTHENTICATION_RESULT) extra to the `FillResponse` object that
includes the populated dataset. The following code shows an example of how to
return the result once the authentication flow completes:  

### Kotlin

    // The data sent by the service and the structure are included in the intent
    val datasetName: String? = intent.getStringExtra(MY_EXTRA_DATASET_NAME)
    val structure: AssistStructure = intent.getParcelableExtra(EXTRA_ASSIST_STRUCTURE)
    val parsedStructure: ParsedStructure = parseStructure(structure)
    val (username, password) = fetchUserData(parsedStructure)

    // Build the presentation of the datasets
    val usernamePresentation =
            RemoteViews(packageName, android.R.layout.simple_list_item_1).apply {
                setTextViewText(android.R.id.text1, "my_username")
            }
    val passwordPresentation =
            RemoteViews(packageName, android.R.layout.simple_list_item_1).apply {
                setTextViewText(android.R.id.text1, "Password for my_username")
            }

    // Add the dataset to the response
    val fillResponse: FillResponse = FillResponse.Builder()
            .addDataset(Dataset.Builder()
                    .setValue(
                            parsedStructure.usernameId,
                            AutofillValue.forText(username),
                            usernamePresentation
                    )
                    .setValue(
                            parsedStructure.passwordId,
                            AutofillValue.forText(password),
                            passwordPresentation
                    )
                    .build()
            ).build()

    val replyIntent = Intent().apply {
        // Send the data back to the service
        putExtra(MY_EXTRA_DATASET_NAME, datasetName)
        putExtra(EXTRA_AUTHENTICATION_RESULT, fillResponse)
    }

    setResult(Activity.RESULT_OK, replyIntent)

### Java

    Intent intent = getIntent();

    // The data sent by the service and the structure are included in the intent
    String datasetName = intent.getStringExtra(MY_EXTRA_DATASET_NAME);
    AssistStructure structure = intent.getParcelableExtra(EXTRA_ASSIST_STRUCTURE);
    ParsedStructure parsedStructure = parseStructure(structure);
    UserData userData = fetchUserData(parsedStructure);

    // Build the presentation of the datasets
    RemoteViews usernamePresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
    usernamePresentation.setTextViewText(android.R.id.text1, "my_username");
    RemoteViews passwordPresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
    passwordPresentation.setTextViewText(android.R.id.text1, "Password for my_username");

    // Add the dataset to the response
    FillResponse fillResponse = new FillResponse.Builder()
            .addDataset(new Dataset.Builder()
                    .setValue(parsedStructure.usernameId,
                            AutofillValue.forText(userData.username), usernamePresentation)
                    .setValue(parsedStructure.passwordId,
                            AutofillValue.forText(userData.password), passwordPresentation)
                    .build())
            .build();

    Intent replyIntent = new Intent();

    // Send the data back to the service
    replyIntent.putExtra(MY_EXTRA_DATASET_NAME, datasetName);
    replyIntent.putExtra(EXTRA_AUTHENTICATION_RESULT, fillResponse);

    setResult(RESULT_OK, replyIntent);

In the scenario where a credit card dataset needs to be unlocked, the service
can display a UI asking for the CVC. You can hide the data until the dataset is
unlocked by presenting boilerplate data, such as the name of the bank and the
last four digits of the credit card number. The following example shows how to
require authentication for a dataset and hide the data until the user provides
the CVC:  

### Kotlin

    // Parse the structure and fetch payment data
    val parsedStructure: ParsedStructure = parseStructure(structure)
    val paymentData: Payment = fetchPaymentData(parsedStructure)

    // Build the presentation that shows the bank and the last four digits of the
    // credit card number, such as 'Bank-1234'
    val maskedPresentation: String = "${paymentData.bank}-" +
            paymentData.creditCardNumber.substring(paymentData.creditCardNumber.length - 4)
    val authPresentation = RemoteViews(packageName, android.R.layout.simple_list_item_1).apply {
        setTextViewText(android.R.id.text1, maskedPresentation)
    }

    // Prepare an intent that displays the UI that asks for the CVC
    val cvcIntent = Intent(this, CvcActivity::class.java)
    val cvcIntentSender: IntentSender = PendingIntent.getActivity(
            this,
            1001,
            cvcIntent,
            PendingIntent.FLAG_CANCEL_CURRENT
    ).intentSender

    // Build a FillResponse object that includes a Dataset that requires authentication
    val fillResponse: FillResponse = FillResponse.Builder()
            .addDataset(
                    Dataset.Builder()
                            // The values in the dataset are replaced by the actual
                            // data once the user provides the CVC
                            .setValue(parsedStructure.creditCardId, null, authPresentation)
                            .setValue(parsedStructure.expDateId, null, authPresentation)
                            .setAuthentication(cvcIntentSender)
                            .build()
            ).build()

### Java

    // Parse the structure and fetch payment data
    ParsedStructure parsedStructure = parseStructure(structure);
    Payment paymentData = fetchPaymentData(parsedStructure);

    // Build the presentation that shows the bank and the last four digits of the
    // credit card number, such as 'Bank-1234'
    String maskedPresentation = paymentData.bank + "-" +
        paymentData.creditCardNumber.subString(paymentData.creditCardNumber.length - 4);
    RemoteViews authPresentation = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);
    authPresentation.setTextViewText(android.R.id.text1, maskedPresentation);

    // Prepare an intent that displays the UI that asks for the CVC
    Intent cvcIntent = new Intent(this, CvcActivity.class);
    IntentSender cvcIntentSender = PendingIntent.getActivity(
            this,
            1001,
            cvcIntent,
            PendingIntent.FLAG_CANCEL_CURRENT
    ).getIntentSender();

    // Build a FillResponse object that includes a Dataset that requires authentication
    FillResponse fillResponse = new FillResponse.Builder()
            .addDataset(new Dataset.Builder()
                    // The values in the dataset are replaced by the actual
                    // data once the user provides the CVC
                    .setValue(parsedStructure.creditCardId, null, authPresentation)
                    .setValue(parsedStructure.expDateId, null, authPresentation)
                    .setAuthentication(cvcIntentSender)
                    .build())
            .build();

Once the activity validates the CVC, it should call the `setResult()` method,
passing a `RESULT_OK` value, and set the `EXTRA_AUTHENTICATION_RESULT` extra to
a `Dataset` object that contains the credit card number and expiration date. The
new dataset replaces the dataset that requires authentication, and the views are
filled out immediately. The following code shows an example of how to return the
dataset once the user provides the CVC:  

### Kotlin

    // Parse the structure and fetch payment data.
    val parsedStructure: ParsedStructure = parseStructure(structure)
    val paymentData: Payment = fetchPaymentData(parsedStructure)

    // Build a non-null RemoteViews object to use as the presentation when
    // creating the Dataset object. This presentation isn't actually used, but the
    // Builder object requires a non-null presentation.
    val notUsed = RemoteViews(packageName, android.R.layout.simple_list_item_1)

    // Create a dataset with the credit card number and expiration date.
    val responseDataset: Dataset = Dataset.Builder()
            .setValue(
                    parsedStructure.creditCardId,
                    AutofillValue.forText(paymentData.creditCardNumber),
                    notUsed
            )
            .setValue(
                    parsedStructure.expDateId,
                    AutofillValue.forText(paymentData.expirationDate),
                    notUsed
            )
            .build()

    val replyIntent = Intent().apply {
        putExtra(EXTRA_AUTHENTICATION_RESULT, responseDataset)
    }

### Java

    // Parse the structure and fetch payment data.
    ParsedStructure parsedStructure = parseStructure(structure);
    Payment paymentData = fetchPaymentData(parsedStructure);

    // Build a non-null RemoteViews object to use as the presentation when
    // creating the Dataset object. This presentation isn't actually used, but the
    // Builder object requires a non-null presentation.
    RemoteViews notUsed = new RemoteViews(getPackageName(), android.R.layout.simple_list_item_1);

    // Create a dataset with the credit card number and expiration date.
    Dataset responseDataset = new Dataset.Builder()
            .setValue(parsedStructure.creditCardId,
                    AutofillValue.forText(paymentData.creditCardNumber), notUsed)
            .setValue(parsedStructure.expDateId,
                    AutofillValue.forText(paymentData.expirationDate), notUsed)
            .build();

    Intent replyIntent = new Intent();
    replyIntent.putExtra(EXTRA_AUTHENTICATION_RESULT, responseDataset);

## Organize the data in logical groups

Autofill services must organize the data in logical groups that isolate concepts
from different domains. In this page, these logical groups are referred to as
*partitions*. The following list shows typical examples of partitions and
fields:

- Credentials, which includes username and password fields.
- Address, which includes street, city, state, and ZIP code fields.
- Payment information, which includes credit card number, expiration date, and verification code fields.

An autofill service that correctly partitions data is able to better protect the
data of its users by not exposing data from more than one partition in a
dataset. For example, a dataset that includes credentials doesn't need to
include payment information. Organizing data in partitions allows your service
to expose the minimum amount of relevant information required to satisfy a
request.

Organizing data in partitions enables services to fill activities that have
views from multiple partitions while sending the minimum amount of relevant data
to the client app. For example, consider an activity that includes views for
username, password, street, and city, and an autofill service that has the
following data:

| Partition | Field 1 | Field 2 |
|---|---|---|
| Credentials | work_username | work_password |
| Credentials | personal_username | personal_password |
| Address | work_street | work_city |
| Address | personal_street | personal_city |

The service can prepare a dataset that includes the credentials partition for
both the work and personal accounts. When the user chooses a dataset, a
subsequent autofill response can provide either the work or personal address,
depending on the user's first choice.

A service can identify the field that originated the request by calling the
[`isFocused()`](https://developer.android.com/reference/android/app/assist/AssistStructure.ViewNode) method while traversing the [`AssistStructure`](https://developer.android.com/reference/android/app/assist/AssistStructure) object.
This allows the service to prepare a `FillResponse` with the appropriate
partition data.

## SMS one-time code autofill

Your autofill service can assist the user with filling one-time codes sent using
the SMS Retriever API.

To use this feature, the following requirements must be met:

- The autofill service is running on Android 9 (API level 28) or higher.
- The user grants consent for your autofill service to read one-time codes from SMS.
- The application that you are providing autofill for is not already using the SMS Retriever API to read one-time codes.

Your autofill service can use [`SmsCodeAutofillClient`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/SmsCodeAutofillClient), available by
calling `SmsCodeRetriever.getAutofillClient()` from Google Play services 19.0.56
or higher.

The primary steps for using this API in an autofill service are:

1. In the autofill service, use [`hasOngoingSmsRequest`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/SmsCodeAutofillClient.html#hasOngoingSmsRequest(java.lang.String)) from `SmsCodeAutofillClient` to determine whether there are any requests active for the package name of the application you're autofilling. Your autofill service must only display a suggestion prompt if this returns `false`.
2. In the autofill service, use [`checkPermissionState`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/SmsCodeAutofillClient.html#checkPermissionState()) from `SmsCodeAutofillClient` to check whether the autofill service has permission to autofill one-time codes. This permission state can be `NONE`, `GRANTED`, or `DENIED`. The autofill service must display a suggestion prompt for `NONE` and `GRANTED` states.
3. In the autofill authentication activity, use the `SmsRetriever.SEND_PERMISSION` permission to register a [`BroadcastReceiver`](https://developer.android.com/guide/components/broadcasts) listening for `SmsCodeRetriever.SMS_CODE_RETRIEVED_ACTION` to receive the SMS code result when it's available.
4. Call [`startSmsCodeRetriever`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/SmsCodeAutofillClient.html#startSmsCodeRetriever()) on `SmsCodeAutofillClient` to start
   listening for one-time codes sent using SMS. If the user grants permissions
   for your autofill service to retrieve one-time codes from SMS, this looks
   for SMS messages received in the last one to five minutes from now.

   If your autofill service needs to request user permission to read one-time
   codes, then the `Task` returned by `startSmsCodeRetriever` might fail with a
   [`ResolvableApiException`](https://developers.google.com/android/reference/com/google/android/gms/common/api/ResolvableApiException) returned. If this happens, you need to call
   the `ResolvableApiException.startResolutionForResult()` method to display a
   consent dialog for the permission request.
5. Receive the SMS code result from the intent and then return the SMS code as
   an autofill response.

| **Note:** You can detect that the broadcast intent is from SMS Retriever API by adding the `com.google.android.gms.auth.api.phone.permission.SEND` permission to your receiver. This permission setting is available in Google Play services version 19.8.31 or higher.

## Enable autofill on Chrome

Chrome allows third-party autofill services to natively autofill forms giving
users a smoother and simpler user experience. To use third-party autofill
services to autofill passwords, passkeys and other information like addresses
and payment data, users must select **Autofill using another service** in Chrome
settings.
![Chrome settings showing the 'Autofill using another service' toggle enabled](https://developer.android.com/static/images/guide/topics/text/autofill-chrome.jpg) **Figure 3.** Chrome settings showing the "Autofill using another service" toggle enabled.

To help users have the best autofill experience possible with your service and
Chrome on Android, autofill service providers should encourage their users to
specify their preferred service provider in Chrome settings.

To help users turn on the toggle, developers can:

- Query Chrome settings and learn whether the user wishes to use a third party autofill service.
- Deep link to the Chrome settings page where users can enable third-party autofill services.

### Specify the maximum Chrome versions for the compatibility mode

Chrome stopped supporting the compatibility mode from version 137 in favor of
Android Autofill. Keeping the compatibility mode can cause stability issues.
Specify the maximum version of Chrome packages that support the compatibility
mode for stability as follows.  

    <autofill-service>
      ...
      <compatibility-package android:name="com.android.chrome" android:maxLongVersionCode="711900039" />
      <compatibility-package android:name="com.chrome.beta" android:maxLongVersionCode="711900039" />
      <compatibility-package android:name="com.chrome.dev" android:maxLongVersionCode="711900039" />
      <compatibility-package android:name="com.chrome.canary" android:maxLongVersionCode="711900039" />
      ...
    </autofill-service>

### Read Chrome settings

Any app can read whether Chrome uses the 3P autofill mode that allows it to use
Android Autofill. Chrome uses Android's [`ContentProvider`](https://developer.android.com/reference/android/content/ContentProvider) to communicate
that information. Declare in your Android manifest which channels you want to
read settings from:  

    <uses-permission android:name="android.permission.READ_USER_DICTIONARY"/>
    <queries>
     <!-- To Query Chrome Beta: -->
     <package android:name="com.chrome.beta" />

     <!-- To Query Chrome Stable: -->
     <package android:name="com.android.chrome" />
    </queries>

Then, use Android's [`ContentResolver`](https://developer.android.com/reference/android/content/ContentResolver) to request that information by
building the content URI:  

### Kotlin

    val CHROME_CHANNEL_PACKAGE = "com.android.chrome" // Chrome Stable.
    val CONTENT_PROVIDER_NAME = ".AutofillThirdPartyModeContentProvider"
    val THIRD_PARTY_MODE_COLUMN = "autofill_third_party_state"
    val THIRD_PARTY_MODE_ACTIONS_URI_PATH = "autofill_third_party_mode"

    val uri = Uri.Builder()
        .scheme(ContentResolver.SCHEME_CONTENT)
        .authority(CHROME_CHANNEL_PACKAGE + CONTENT_PROVIDER_NAME)
        .path(THIRD_PARTY_MODE_ACTIONS_URI_PATH)
        .build()

    val cursor = contentResolver.query(
        uri,
        arrayOf(THIRD_PARTY_MODE_COLUMN), // projection
        null, // selection
        null, // selectionArgs
        null  // sortOrder
    )

    if (cursor == null) {
      // Terminate now! Chromium versions older than this don't provide this information.
    }

    cursor?.use { // Use the safe call operator and the use function for auto-closing
        if (it.moveToFirst()) { // Check if the cursor has any rows
            val index = it.getColumnIndex(THIRD_PARTY_MODE_COLUMN)
            if (index != -1) { // Check if the column exists
              val value = it.getInt(index)
              if (0 == value) {
                  // 0 means that the third party mode is turned off. Chrome uses its built-in
                  // password manager. This is the default for new users.
              } else {
                  // 1 means that the third party mode is turned on. Chrome forwards all
                  // autofill requests to Android Autofill. Users have to opt-in for this.
              }
            } else {
              // Handle the case where the column doesn't exist.  Log a warning, perhaps.
              Log.w("Autofill", "Column $THIRD_PARTY_MODE_COLUMN not found in cursor")
            }
        }
    } // The cursor is automatically closed here

### Java

    final String CHROME_CHANNEL_PACKAGE = "com.android.chrome";  // Chrome Stable.
    final String CONTENT_PROVIDER_NAME = ".AutofillThirdPartyModeContentProvider";
    final String THIRD_PARTY_MODE_COLUMN = "autofill_third_party_state";
    final String THIRD_PARTY_MODE_ACTIONS_URI_PATH = "autofill_third_party_mode";

    final Uri uri = new Uri.Builder()
                      .scheme(ContentResolver.SCHEME_CONTENT)
                      .authority(CHROME_CHANNEL_PACKAGE + CONTENT_PROVIDER_NAME)
                      .path(THIRD_PARTY_MODE_ACTIONS_URI_PATH)
                      .build();

    final Cursor cursor = getContentResolver().query(
                      uri,
                      /*projection=*/new String[] {THIRD_PARTY_MODE_COLUMN},
                      /*selection=*/ null,
                      /*selectionArgs=*/ null,
                      /*sortOrder=*/ null);

    if (cursor == null) {
      // Terminate now! Chromium versions older than this don't provide this information.
    }

    cursor.moveToFirst(); // Retrieve the result;

    int index = cursor.getColumnIndex(THIRD_PARTY_MODE_COLUMN);

    if (0 == cursor.getInt(index)) {
      // 0 means that the third party mode is turned off. Chrome uses its built-in
      // password manager. This is the default for new users.
    } else {
      // 1 means that the third party mode is turned on. Chrome forwards all
      // autofill requests to Android Autofill. Users have to opt-in for this.
    }

### Deep link to Chrome settings

To deep link to the Chrome settings page where users can enable third-party
autofill services, use an Android [`Intent`](https://developer.android.com/reference/android/content/Intent). Be sure to configure the
action and categories as shown in this example:  

### Kotlin

    val autofillSettingsIntent = Intent(Intent.ACTION_APPLICATION_PREFERENCES)
    autofillSettingsIntent.addCategory(Intent.CATEGORY_DEFAULT)
    autofillSettingsIntent.addCategory(Intent.CATEGORY_APP_BROWSER)
    autofillSettingsIntent.addCategory(Intent.CATEGORY_PREFERENCE)

    // Invoking the intent with a chooser allows users to select the channel they
    // want to configure. If only one browser reacts to the intent, the chooser is
    // skipped.
    val chooser = Intent.createChooser(autofillSettingsIntent, "Pick Chrome Channel")
    startActivity(chooser)

    // If the caller knows which Chrome channel they want to configure,
    // they can instead add a package hint to the intent, e.g.
    val specificChromeIntent = Intent(Intent.ACTION_APPLICATION_PREFERENCES) // Create a *new* intent
    specificChromeIntent.addCategory(Intent.CATEGORY_DEFAULT)
    specificChromeIntent.addCategory(Intent.CATEGORY_APP_BROWSER)
    specificChromeIntent.addCategory(Intent.CATEGORY_PREFERENCE)
    specificChromeIntent.setPackage("com.android.chrome") // Set the package on the *new* intent
    startActivity(specificChromeIntent) // Start the *new* intent

### Java

    Intent autofillSettingsIntent = new Intent(Intent.ACTION_APPLICATION_PREFERENCES);
    autofillSettingsIntent.addCategory(Intent.CATEGORY_DEFAULT);
    autofillSettingsIntent.addCategory(Intent.CATEGORY_APP_BROWSER);
    autofillSettingsIntent.addCategory(Intent.CATEGORY_PREFERENCE);

    // Invoking the intent with a chooser allows users to select the channel they
    // want to configure. If only one browser reacts to the intent, the chooser is
    // skipped.
    Intent chooser = Intent.createChooser(autofillSettingsIntent, "Pick Chrome Channel");
    startActivity(chooser);

    // If the caller knows which Chrome channel they want to configure,
    // they can instead add a package hint to the intent, e.g.
    autofillSettingsIntent.setPackage("com.android.chrome");
    startActivity(autofillSettingsIntent);

## Advanced autofill scenarios

Use autofill in the following scenarios:

### Integrate with keyboard

Beginning with Android 11, the platform allows keyboards and other
input-method editors (*IMEs* ) to display autofill suggestions inline, instead
of using a pulldown menu. For more information on how your autofill service can
support this functionality, see [Integrate autofill with keyboards](https://developer.android.com/guide/topics/text/ime-autofill).

### Paginate datasets

A large autofill response can exceed the allowed transaction size of the
[`Binder`](https://developer.android.com/reference/android/os/Binder) object that represents the remotable object required to process
the request. To prevent the Android system from throwing an exception in these
scenarios, you can keep the `FillResponse` small by adding no more than 20
`Dataset` objects at a time. If your response needs more datasets, you can add
a dataset that lets users know that there's more information and retrieves the
next group of datasets when selected. For more information, see
[`addDataset(Dataset)`](https://developer.android.com/reference/android/service/autofill/FillResponse.Builder#addDataset(android.service.autofill.Dataset)).

### Save data split in multiple screens

Apps often split user data across multiple screens within the same activity,
such as for creating new user accounts. For example, the first screen might ask
for a username, and a second screen for a password. In these situations, your
autofill service must wait until the user enters data into all relevant fields
before displaying the autofill save UI. Follow these steps to handle such
scenarios:

1. In the first fill request, add a [client state bundle](https://developer.android.com/reference/android/service/autofill/FillResponse.Builder#setClientState(android.os.Bundle)) in the response that contains the autofill IDs of the partial fields present in the screen.
2. In the second fill request, retrieve the client state bundle, get the autofill IDs set in the previous request from the client state, and add these IDs and the [`FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE`](https://developer.android.com/reference/android/service/autofill/SaveInfo#FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE) flag to the `SaveInfo` object used in the second response.
3. In the save request, use the
   proper [`FillContext`](https://developer.android.com/reference/android/service/autofill/FillContext) objects to get the value of each field. There is one
   fill context per fill request.

   For more information, see [Save when data is split in multiple screens](https://developer.android.com/reference/android/service/autofill/AutofillService#MultipleStepsSave).

### Provide initialization and teardown logic for each request

Every time there's an autofill request, the Android system binds to the service
and calls its [`onConnected()`](https://developer.android.com/reference/android/service/autofill/AutofillService#onConnected()) method. Once the service processes the
request, the Android system calls the [`onDisconnected()`](https://developer.android.com/reference/android/service/autofill/AutofillService#onDisconnected()) method and
unbinds from the service. You can implement `onConnected()` to provide code
that runs before processing a request and `onDisconnected()` to provide code
that runs after processing a request.

### Customize the autofill save UI

Autofill services can customize the autofill save UI to help users decide
whether they want to let the service save their data. Services can provide
additional information about what is saved either through text or through a
customized view. Services can also change the appearance of the button that
cancels the save request and get a notification when the user taps that button.
For more information, see the [`SaveInfo`](https://developer.android.com/reference/android/service/autofill/SaveInfo) reference page.

### Compatibility mode

The compatibility mode allows autofill services to use the [accessibility
virtual structure](https://developer.android.com/guide/topics/ui/accessibility/service#query) for autofill purposes. It's particularly useful for
providing autofill functionality in browsers that don't explicitly implement
the autofill APIs.

To test your autofill service using compatibility mode, explicitly add the
browser or app to the allowlist that requires compatibility mode. You can check
which packages are already in the allowlist by running the following command:  

    $ adb shell settings get global autofill_compat_mode_allowed_packages

If the package you're testing isn't listed, add it by running the following
command, where `pkgX` is the package of the app:  

    $ adb shell settings put global autofill_compat_mode_allowed_packages pkg1[resId1]:pkg2[resId1,resId2]

If the app is a browser, then use `resIdx` to specify the resource ID of the
input field that contains the URL of the rendered page.

Compatibility mode has the following limitations:

- A save request is triggered when the service uses the `FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE` flag or the [`setTrigger()`](https://developer.android.com/reference/android/service/autofill/SaveInfo.Builder#setTriggerId(android.view.autofill.AutofillId)) method is called. `FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE` is set by default when using compatibility mode.
- The text value of the nodes might not be available in the [`onSaveRequest(SaveRequest, SaveCallback)`](https://developer.android.com/reference/android/service/autofill/AutofillService#onSaveRequest(android.service.autofill.SaveRequest,%20android.service.autofill.SaveCallback)) method.

For more information about compatibility mode, including the limitations
associated with it, see the [`AutofillService`](https://developer.android.com/reference/android/service/autofill/AutofillService#CompatibilityMode) class reference.