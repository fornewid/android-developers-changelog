---
title: https://developer.android.com/privacy-and-security/risks/log-info-disclosure
url: https://developer.android.com/privacy-and-security/risks/log-info-disclosure
source: md.txt
---

# Log Info Disclosure

<br />

**OWASP category:** [MASVS-STORAGE: Storage](https://mas.owasp.org/MASVS/05-MASVS-STORAGE)

## Overview

*Log Info Disclosure*is a type of vulnerability where apps print sensitive data into the device log. If exposed to malicious actors, this sensitive information may be valuable outright -- such as a user's credentials or personally identifiable information (PII) -- or it may enable further attacks.

This problem can occur in any of the following scenarios:

- App-generated logs:
  - The logs intentionally allow access to unauthorized actors, yet they accidentally contain sensitive data.
  - The logs intentionally include sensitive data, but they are accessible to unauthorized actors by accident.
  - Generic error logs that might at times print sensitive data, depending on the triggered error message.
- Externally-generated logs:
  - External components are responsible for printing logs that include sensitive data.

Android`Log.*`statements write to the common memory buffer`logcat`. Since Android 4.1 (API level 16), only privileged system apps can be granted access to read`logcat`, by declaring the`READ_LOGS`permission. However, Android supports an incredibly diverse set of devices whose pre-loaded applications sometimes declare the`READ_LOGS`privilege. As a consequence, logging directly to`logcat`is discouraged since it is more prone to data leakage.

Ensure all logging to`logcat`is sanitized in non-debug versions of your application. Remove any data that could possibly be sensitive. As an additional precaution, use tools like R8 to remove all log levels except warning and error. If you need more detailed logs, use internal storage and manage your own logs directly, instead of using the system log.

## Impact

The severity of the Log Info Disclosure vulnerability class can vary, depending on the context and the type of sensitive data.Overall, the impact of this vulnerability class is loss of confidentiality of potentially critical information such as PII and credentials

## Mitigations

### General

As a general preemptive measure during design and implementation, draw trust boundaries according to[the principle of least privilege](https://www.cisa.gov/uscert/bsi/articles/knowledge/principles/least-privilege#:%7E:text=The%20Principle%20of%20Least%20Privilege%20states%20that%20a%20subject%20should,control%20the%20assignment%20of%20rights.). Ideally, sensitive data shouldn't cross or reach outside of any of the trust areas. This reinforces the separation of privileges.

Don't log sensitive data. Only log compile-time constants whenever possible. You can use the[ErrorProne tool](https://errorprone.info/bugpattern/CompileTimeConstant)for compile-time constant annotation.

Avoid logs that print statements that might contain unanticipated information, including sensitive data, depending on the error triggered. As much as possible, the data printed in logs and error logs should only include predictable information.

Avoid logging to`logcat`. This is because logging to`logcat`might become a privacy issue due to apps with the`READ_LOGS`permission. It's also ineffective since it cannot trigger alerts or be queried. We recommend that applications configure the`logcat`backend for developer builds only.

Most log management libraries allow defining log levels, which allows for logging different amounts of information between debug and production logs. Change the log level so that it is different from "debug" as soon as product testing ends.

Remove as many log levels from production as possible. If you cannot avoid keeping logs in production, remove non-constant variables from the log statements. The following scenarios may occur:

- You're able to remove all logs from Production.
- You need to keep Warning and Error logs in Production.

For both of these cases, remove logs automatically using libraries such as R8. Any attempts to remove logs manually are prone to error. As part of the code optimization, R8 can be set to safely remove log levels that you want to keep for debugging, but strip in Production.

If you're going to log in Production, prepare flags you can use to shut down logging conditionally in case of an incident. Incident Response flags should prioritize: safety of deployment; speed and ease of deployment, thoroughness of redacting logs, memory usage, and performance costs of scanning every log message.

### Strip logs to logcat from Production builds by using R8.

In Android Studio 3.4 or Android Gradle plugin 3.4.0 and higher, R8 is the default compiler for code optimization and shrinking. However, you need to[enable R8](https://developer.android.com/studio/build/shrink-code#enable).

R8 has replaced ProGuard, but the rules file in the project's root folder is still called`proguard-rules.pro`.The following snippet shows a sample`proguard-rules.pro`file that removes all logs from production*except*warnings and errors:  

    -assumenosideeffects class android.util.Log {
        private static final String TAG = "MyTAG";
        public static boolean isLoggable(java.lang.String, int);
        public static int v(TAG, "My log as verbose");
        public static int d(TAG, "My log as debug");
        public static int i(TAG, "My log as information");
    }

The following sample`proguard-rules.pro`file removes*all*logs from production:  

    -assumenosideeffects class android.util.Log {
        private static final String TAG = "MyTAG";
        public static boolean isLoggable(java.lang.String, int);
        public static int v(TAG, "My log as verbose");
        public static int d(TAG, "My log as debug");
        public static int i(TAG, "My log as information");
        public static int w(TAG, "My log as warning");
        public static int e(TAG, "My log as error");
    }

Note that R8 provides app-shrinking capabilities and log-stripping functionality. If you would like to use R8 only for its log-stripping functionality, add the following to your`proguard-rules.pro`file:  

    -dontwarn **
    -dontusemixedcaseclassnames
    -dontskipnonpubliclibraryclasses
    -dontpreverify
    -verbose

    -optimizations !code/simplification/arithmetic,!code/allocation/variable
    -keep class **
    -keepclassmembers class *{*;}
    -keepattributes *

### Sanitize any eventual logs in Production containing sensitive data

In order to avoid leaking sensitive data, ensure all logging to`logcat`is sanitized in non-debug versions of your application. Remove any data that could possibly be sensitive.

Example:  

### Kotlin

    data class Credential<T>(val data: String) {
      /** Returns a redacted value to avoid accidental inclusion in logs. */
      override fun toString() = "Credential XX"
    }

    fun checkNoMatches(list: List<Any>) {
        if (!list.isEmpty()) {
              Log.e(TAG, "Expected empty list, but was %s", list)
        }
    }

### Java

    public class Credential<T> {
      private T t;
      /** Returns a redacted value to avoid accidental inclusion in logs. */
      public String toString(){
             return "Credential XX";
      }
    }

    private void checkNoMatches(List<E> list) {
       if (!list.isEmpty()) {
              Log.e(TAG, "Expected empty list, but was %s", list);
       }
    }

### Redact sensitive data in logs

If you must include sensitive data in your logs, then we recommend sanitizing the logs before printing them to remove or obfuscate sensitive data. To do so, use one of the following techniques:

- **Tokenization.**If sensitive data is stored in a vault, such as an encryption management system from which secrets can be referenced via tokens, log the token instead of the sensitive data.
- **Data masking.** Data masking is a one-way irreversible process. It creates a version of the sensitive data that looks structurally similar to the original, but hides the most sensitive information contained within a field. Example: Substituting the credit card number`1234-5678-9012-3456`with`XXXX-XXXX-XXXX-1313`. Before you release your app into production, we recommend that you complete a security review process to scrutinize the usage of data masking.*Warning:*Don't use data masking in cases where even releasing only a portion of the sensitive data can significantly impact security, such as when handling passwords.
- **Redaction.** Redaction is similar to masking, but hides all of the information contained within a field. Example: Substituting the credit card number`1234-5678-9012-3456`with`XXXX-XXXX-XXXX-XXXX`.
- **Filtering.**Implement format strings in your logging library of choice if they do not already exist, to facilitate the modification of non-constant values in log statements.

Log printing should only be performed through a "logs sanitizer" component that ensures all logs are sanitized before being printed, as shown in the following code snippet.  

### Kotlin

    data class ToMask<T>(private val data: T) {
      // Prevents accidental logging when an error is encountered.
      override fun toString() = "XX"

      // Makes it more difficult for developers to invoke sensitive data
      // and facilitates sensitive data usage tracking.
      fun getDataToMask(): T = data
    }

    data class Person(
      val email: ToMask<String>,
      val username: String
    )

    fun main() {
        val person = Person(
            ToMask("name@gmail.com"), 
            "myname"
        )
        println(person)
        println(person.email.getDataToMask())
    }

### Java

    public class ToMask<T> {
      // Prevents accidental logging when an error is encountered.
      public String toString(){
             return "XX";
      }

      // Makes it more difficult for developers to invoke sensitive data 
      // and facilitates sensitive data usage tracking.
      public T  getDataToMask() {
        return this;
      }
    }

    public class Person {
      private ToMask<String> email;
      private String username;

      public Person(ToMask<String> email, String username) {
        this.email = email;
        this.username = username;
      }
    }

    public static void main(String[] args) {
        Person person = new Person(
            ToMask("name@gmail.com"), 
            "myname"
        );
        System.out.println(person);
        System.out.println(person.email.getDataToMask());
    }