---
title: https://developer.android.com/topic/performance/app-optimization/troubleshoot-the-optimization
url: https://developer.android.com/topic/performance/app-optimization/troubleshoot-the-optimization
source: md.txt
---

Since R8's optimizations update your app's code, it's important to strongly
[test](https://developer.android.com/topic/performance/app-optimization/test-the-optimization) your app's behavior to make sure that your app is functioning as
expected. In case of unexpected behavior, use this page as a guide to
troubleshoot potential issues after optimization. For more information about
rules that you can use to troubleshoot your optimization, see
[Use rules to troubleshoot optimization](https://developer.android.com/topic/performance/app-optimization/troubleshooting-rules).

While troubleshooting, focus on the following situations:

- **Over optimization leading to app crashes**: Your app crashes because R8 optimized too much code.
- **Unclear or insufficient optimization**: R8 did not optimize your app as much as you expected or you need further explanations for the optimizations.

## App crashes

If your app crashed after optimizing it with R8, it's typically due to broken
reflection. To identify broken reflection, use the following guidelines:

- You observe an exception that means that the indicated class, method, or field is being used through reflection. These exceptions are typically one of: `ClassNotFoundException`, `NoSuchMethodException`, `NoSuchFieldException`, `NoClassDefFoundError`, `NoSuchMethodError`, `NoSuchFieldError`.
- You see code which references reflection with `import kotlin.reflect.*` or `import java.lang.reflect.*`.
- You observe a class constructor being used as follows: `Something::class.constructors`.
- You see `Class.forName(...)`.

**Solution** : Add a [keep rule](https://developer.android.com/topic/performance/app-optimization/keep-rules-overview).

## Unclear or insufficient optimization

Because rules are applied from your app as well as from included libraries, you
might need additional clarity about the rules applied, or need an explanation
for why R8 retained certain sections of code that you expected to be optimized.

- **Ambiguity about the rules applied**: Because rules from included libraries
  also apply to your app, and global options from these libraries also
  propagate to your app, you might be unsure about which rules are applied.

  **Solution** : Check which rules are applied by viewing the report of all the
  rules that R8 applies when building your project. You can find this report
  at `./app/build/outputs/mapping/configuration.txt`. This report contains all
  of the merged rules from every library and module that was used to
  configure R8, and can be used to identify inefficient rules.
- **Too much code being kept**: R8's optimization might retain code that you
  expected to be removed.

  **Solution** : Use the configuration option `-whyareyoukeeping` to help
  understand why the code was kept. The output contains a path from the kept
  code to one of your app's entry points. For more information, see
  [`-whyareyoukeeping`](https://www.guardsquare.com/manual/configuration/usage).
- **Difficulty understanding the original stack trace**: R8 changes code in
  various ways, making the stack trace no longer refer to the original code.
  For example, line numbers and the names of classes and methods can change.

  **Solution** : Starting from Android Studio Otter 3 Feature Drop and AGP 9.0,
  Logcat automatically deobfuscates stack traces. However, if you're
  using an earlier version of Android Studio, you need to manually recover the
  original stack trace. To recover the original stack trace, use the
  [`retrace`](https://developer.android.com/studio/command-line/retrace) command-line tool, which is bundled with the
  [command-line tools](https://developer.android.com/tools) package.

  To use `retrace`, provide the command with the path to a mapping file and a
  stack trace file. The mapping file, called `mapping.txt`, is automatically
  bundled with your Android App Bundle (AAB). For more details, see the
  [retrace](https://developer.android.com/studio/command-line/retrace) documentation and the Play Console Help Center article about
  how to [deobfuscate crash stack traces](https://support.google.com/googleplay/android-developer/answer/9848633). When using Play and Firebase
  Crashlytics, use the `mapping.txt` file with the crashes the service
  collects from app users. The following command shows how you can run
  `retrace` from your project's root:

      $ANDROID_HOME/cmdline-tools/latest/bin/retrace app/build/outputs/mapping/$releaseVariant/mapping.txt trace.txt

  > [!NOTE]
  > **Note:** Android Studio saves the mapping file in the `/build/outputs/mapping/` directory. The mapping file is overwritten every time you build your project, so you must save a copy each time you publish a new release.

## Report bugs

If you're unable to solve an issue with R8, [file a bug](https://b.corp.google.com/issues/new?component=326788&template=1025938&pli=1).