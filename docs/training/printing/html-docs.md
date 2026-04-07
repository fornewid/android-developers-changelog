---
title: Printing HTML documents  |  App data and files  |  Android Developers
url: https://developer.android.com/training/printing/html-docs
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Printing HTML documents Stay organized with collections Save and categorize content based on your preferences.



Printing out content beyond a simple photo on Android requires composing text and graphics in a
print document. The Android framework provides a way to use HTML to compose a document and
print it with a minimum of code.

In Android 4.4 (API level 19), the `WebView` class has been updated to
enable printing HTML content. The class allows you to load a local HTML resource or download
a page from the web, create a print job and hand it off to Android's print services.

This lesson shows you how to quickly build an HTML document containing text and graphics and
use `WebView` to print it.

## Load an HTML document

Printing an HTML document with `WebView` involves loading an HTML
resource or building an HTML document as a string. This section describes how to build an HTML
string and load it into a `WebView` for printing.

This view object is typically used as part of an activity layout. However, if your application
is not using a `WebView`, you can create an instance of the class
specifically for printing purposes. The main steps for creating this custom print view are:

1. Create a `WebViewClient` that starts a print job after
   the HTML resource is loaded.
2. Load the HTML resource into the `WebView` object.

The following code sample demonstrates how to create a simple `WebViewClient` and load an HTML document created on the fly:

### Kotlin

```
private var mWebView: WebView? = null

private fun doWebViewPrint() {
    // Create a WebView object specifically for printing
    val webView = WebView(activity)
    webView.webViewClient = object : WebViewClient() {

        override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest) = false

        override fun onPageFinished(view: WebView, url: String) {
            Log.i(TAG, "page finished loading $url")
            createWebPrintJob(view)
            mWebView = null
        }
    }

    // Generate an HTML document on the fly:
    val htmlDocument =
            "<html><body><h1>Test Content</h1><p>Testing, testing, testing...</p></body></html>"
    webView.loadDataWithBaseURL(null, htmlDocument, "text/HTML", "UTF-8", null)

    // Keep a reference to WebView object until you pass the PrintDocumentAdapter
    // to the PrintManager
    mWebView = webView
}
```

### Java

```
private WebView mWebView;

private void doWebViewPrint() {
    // Create a WebView object specifically for printing
    WebView webView = new WebView(getActivity());
    webView.setWebViewClient(new WebViewClient() {

            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return false;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                Log.i(TAG, "page finished loading " + url);
                createWebPrintJob(view);
                mWebView = null;
            }
    });

    // Generate an HTML document on the fly:
    String htmlDocument = "<html><body><h1>Test Content</h1><p>Testing, " +
            "testing, testing...</p></body></html>";
    webView.loadDataWithBaseURL(null, htmlDocument, "text/HTML", "UTF-8", null);

    // Keep a reference to WebView object until you pass the PrintDocumentAdapter
    // to the PrintManager
    mWebView = webView;
}
```

**Note:** Make sure your call for generating a print job happens in the `onPageFinished()` method of the `WebViewClient` you created in the previous section. If you don't wait until page
loading is finished, the print output may be incomplete or blank, or may fail completely.

**Note:** The example code above holds an instance of the
`WebView` object so that is it not garbage collected before the print job
is created. Make sure you do the same in your own implementation, otherwise the print process
may fail.

If you want to include graphics in the page, place the graphic files in the `assets/`
directory of your project and specify a base URL in the first parameter of the
`loadDataWithBaseURL()` method, as shown in the
following code example:

### Kotlin

```
webView.loadDataWithBaseURL(
        "file:///android_asset/images/",
        htmlBody,
        "text/HTML",
        "UTF-8",
        null
)
```

### Java

```
webView.loadDataWithBaseURL("file:///android_asset/images/", htmlBody,
        "text/HTML", "UTF-8", null);
```

You can also load a web page for printing by replacing the
`loadDataWithBaseURL()` method with
`loadUrl()` as shown below.

### Kotlin

```
webView.loadUrl("https://developer.android.com/about/index.html")
```

### Java

```
// Print an existing web page (remember to request INTERNET permission!):
webView.loadUrl("https://developer.android.com/about/index.html");
```

When using `WebView` for creating print documents, you should be aware of
the following limitations:

* You cannot add headers or footers, including page numbers, to the document.
* The printing options for the HTML document do not include the ability to print page
  ranges, for example: Printing page 2 to 4 of a 10 page HTML document is not supported.
* An instance of `WebView` can only process one print job at a time.
* An HTML document containing CSS print attributes, such as landscape properties, is not
  supported.
* You cannot use JavaScript in a HTML document to trigger printing.

**Note:** The content of a `WebView` object that is included in
a layout can also be printed once it has loaded a document.

If you want to create a more customized print output and have complete control of the content
draw on the printed page, jump to the next lesson:
[Printing a custom document](/training/printing/custom-docs) lesson.

## Create a print job

After creating a `WebView` and loading your HTML content, your
application is almost done with its part of the printing process. The next steps are accessing
the `PrintManager`, creating a print adapter, and finally, creating a print
job. The following example illustrates how to perform these steps:

### Kotlin

```
private fun createWebPrintJob(webView: WebView) {

    // Get a PrintManager instance
    (activity?.getSystemService(Context.PRINT_SERVICE) as? PrintManager)?.let { printManager ->

        val jobName = "${getString(R.string.app_name)} Document"

        // Get a print adapter instance
        val printAdapter = webView.createPrintDocumentAdapter(jobName)

        // Create a print job with name and adapter instance
        printManager.print(
                jobName,
                printAdapter,
                PrintAttributes.Builder().build()
        ).also { printJob ->

            // Save the job object for later status checking
            printJobs += printJob
        }
    }
}
```

### Java

```
private void createWebPrintJob(WebView webView) {

    // Get a PrintManager instance
    PrintManager printManager = (PrintManager) getActivity()
            .getSystemService(Context.PRINT_SERVICE);

    String jobName = getString(R.string.app_name) + " Document";

    // Get a print adapter instance
    PrintDocumentAdapter printAdapter = webView.createPrintDocumentAdapter(jobName);

    // Create a print job with name and adapter instance
    PrintJob printJob = printManager.print(jobName, printAdapter,
            new PrintAttributes.Builder().build());

    // Save the job object for later status checking
    printJobs.add(printJob);
}
```

This example saves an instance of the `PrintJob` object for use by the
application, which is not required. Your application may use this object to track the progress of
the print job as it's being processed. This approach is useful when you want to monitor the status
of the print job in you application for completion, failure, or user cancellation. Creating an
in-app notification is not required, because the print framework automatically creates a system
notification for the print job.

[Previous

arrow\_back

Printing photos](/training/printing/photos)

[Next

Printing custom documents

arrow\_forward](/training/printing/custom-docs)