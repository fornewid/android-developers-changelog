---
title: https://developer.android.com/develop/ui/views/layout/webapps/best-practices
url: https://developer.android.com/develop/ui/views/layout/webapps/best-practices
source: md.txt
---

# Best practices for web apps

Developing web pages and applications for mobile devices presents different challenges compared to developing a web page for desktop web browsers. The following practices can help you provide the most effective web application for Android and other mobile devices.

1. **Redirect mobile devices to a dedicated mobile version of your website.**There are several ways to do this using server-side redirects. One common method is to "sniff" the User Agent string provided by the web browser. To determine whether to serve a mobile version of your site, look for the "mobile" string in the User Agent.
| **Note:**Large-screen Android-powered devices that are served full-size websites---such as tablets---don't include the "mobile" string in the User Agent, while the rest of the User Agent string is mostly the same. As such, it's important you deliver the mobile version of your website based on whether the "mobile" string exists in the User Agent.
2. **Use[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)for mobile devices.** HTML5 is the most common markup language used for mobile websites. This standard encourages mobile-first development to help ensure that websites work on a variety of devices. Unlike previous web languages, HTML5 uses simpler`<DOCTYPE>`and`charset`declarations:  

   ```xml
   <!DOCTYPE html>
   ...
   <meta charset="UTF-8">
   ```
3. **Use viewport metadata to properly resize your web page.** In your document`<head>`, provide metadata that specifies how you want the browser's viewport to render your web page. For example, your viewport metadata can specify the height and width for the browser's viewport, the initial page scale, and the target screen density.

   The following example shows how to set viewport metadata:  

   ```xml
   <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
   ```

   For more information about how to use viewport metadata for Android-powered devices, read[Support different screens in web apps](https://developer.android.com/guide/webapps/targeting).
4. **Use a vertical linear layout.**Avoid the need for the user to scroll left and right while navigating your page. Scrolling up and down is easier for the user and makes your page simpler.
5. **Set the layout height and width to`match_parent`.** Setting your[`WebView`](https://developer.android.com/reference/android/webkit/WebView)object's height and width to`match_parent`makes sure your app's views are sized correctly. We discourage setting the height to`wrap_content`because it results in incorrect sizing. Similarly, setting the layout width to`wrap_content`isn't supported and causes your`WebView`to use the width of its parent instead. Because of this behavior, it's also important to make sure none of your`WebView`object's parent layout objects have their height and width set to`wrap_content`.
6. **Avoid multiple file requests.** Because mobile devices typically have a connection speed slower than desktop computers, make your page load as fast as possible. One way to speed it up is to avoid loading extra files such as stylesheets and script files in the`<head>`. Also, consider[performing mobile analysis with Google's PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/get-started)for detailed optimization suggestions specific to your app.

## Additional resources

- [Pixel-Perfect UI in the WebView](https://developers.google.com/chrome/mobile/docs/webview/pixelperfect)
- [Learn Responsive Design](http://www.html5rocks.com/en/mobile/responsivedesign/)
- [High DPI images for variable pixel densities](http://www.html5rocks.com/en/mobile/high-dpi/)
- [Mobile Web Best Practices](http://www.w3.org/TR/mobile-bp/)
- [Make the Web Faster](https://developers.google.com/speed/overview)