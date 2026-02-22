---
title: https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices
url: https://developer.android.com/topic/performance/app-optimization/keep-rules-best-practices
source: md.txt
---

# Follow the best practices

While working with keep rules, it's important to reach the right amount of specificity to make sure you see benefits while maintaining your app's behaviour. See the following sections to learn about good patterns as well as things to avoid in keep rules.

## Good patterns in keep rules

Well-defined keep rules are as specific as possible and adhere to the following patterns:

- For the class specification, always specify a specific class, base class, or annotated class if possible, as shown in the following examples:

      -keepclassmembers class com.example.MyClass {
        void someSpecificMethod();
      }

      -keepclassmembers ** extends com.example.MyBaseClass {
        void someSpecificMethod();
      }

      -keepclassmembers @com.example.MyAnnotation class ** {
        void someSpecificMethod();
      }

- Whenever possible, use annotations on your source code and then target those annotations directly in your keep rules. This creates a clear, explicit link between your code and the rules that preserve it, making your configuration more robust, easier to understand, and less prone to breakage when code changes.

  For example, the following snippet demonstrates how you can keep the class MyClass, as well as other classes that are annotated with`@com.example.DisplayComponent`:  

      // In the source code
      @com.example.DisplayComponent
      class MyClass { /* ... */ }

      // In the keep rules
      -keep @com.example.DisplayComponent class * {*;}

  We recommend naming your annotations such that they provide meaningful context for why code parts are preserved. For example, use`@DisplayComponent`for an app where display components require some parts to be kept.
- Whenever possible, the member specification should be declared, and only reference the parts of the class that must be kept for the app to function. It's recommended to not apply a rule to an entire class by defining the optional member scope as`{ *; }`unless strictly needed.

      -keepclassmembers com.example.MyClass {
        void someSpecificMethod();
        void @com.example.MyAnnotation *;
      }

- If you use the[`repackageclasses`global option](https://developer.android.com/topic/performance/app-optimization/global-options#global-options), avoid specifying the optional package name. This results in smaller DEX files because the package prefix is omitted in the repackaged class names.

- Maintain keep rules for all items accessed by reflection. Even if such items are retained by R8 without explicit keep rules, maintaining the actual rules is crucial because future code changes could lead R8 to no longer retain these items.

If you can't adhere to these guidelines, you can temporarily isolate the code that needs to be kept in a dedicated package and apply your keep rule to the package. However, this isn't a solution for the long term. To learn more, see[Adopt optimizations incrementally](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally#use-package-wide). To use a keep rule for a package define a keep rule as shown in the following example:  

    -keepclassmembers class com.example.pkg.** { *; }

## Things to avoid

The keep rule syntax has many options, but for measurable sustainable performance benefits we recommend not using the following:

- Don't use package-wide keep rules such as`-keep class com.example.pkg.** {
  *; }`long-term. They can be used temporarily to work around issues when configuring R8. For more information, see[Limit the optimization scope](https://developer.android.com/topic/performance/app-optimization/adopt-optimizations-incrementally#limit-optimization). In general, be careful with wildcards--- make sure that you are keeping only the code that you need to.
- When possible, avoid libraries that suggest you copy and paste keep rules when you use them, especially package-wide keep rules. Libraries designed to perform well on Android should avoid reflection where possible and[embed consumer keep rules when necessary](https://developer.android.com/topic/performance/app-optimization/library-optimization#write-consumer-rules).
- Avoid using the inversion operator`!`in keep rules because you could unintentionally apply a rule to almost every class in your application.

If you're unable to follow these rules, you might be using a lot of open-ended reflection, and should either avoid the reflection or avoid the library using reflection (see the[Gson case study](https://developer.android.com/topic/performance/app-optimization/choose-libraries-wisely#gson-issues)).