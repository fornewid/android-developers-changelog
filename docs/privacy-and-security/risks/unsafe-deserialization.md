---
title: https://developer.android.com/privacy-and-security/risks/unsafe-deserialization
url: https://developer.android.com/privacy-and-security/risks/unsafe-deserialization
source: md.txt
---

# Unsafe Deserialization

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

When storing or transferring large amounts of Java object data, it is often more efficient to serialize the data first. The data will then undergo a deserialization process by the receiving application, activity, or provider that ends up handling the data. Under normal circumstances, data is serialized and then deserialized without any user intervention. However, the trust relationship between the deserialization process and its intended object can be abused by a malicious actor who could, for example, intercept and alter serialized objects. This would enable the malicious actor to perform attacks such as denial of service (DoS), privilege escalation, and remote code execution (RCE).

While the[`Serializable`](https://developer.android.com/reference/java/io/Serializable)class is a common method for managing serialization, Android has its own class for handling serialization called[`Parcel`](https://developer.android.com/reference/android/os/Parcel). Using the`Parcel`class, object data can be serialized into byte stream data and packed into a`Parcel`using the[`Parcelable`](https://developer.android.com/reference/android/os/Parcelable)interface. This allows the`Parcel`to be transported or stored more efficiently.

Nevertheless, careful consideration should be given when using the`Parcel`class, as it is meant to be a high-efficiency IPC transport mechanism, but shouldn't be used to store serialized objects within the local persistent storage as this could lead to data compatibility issues or loss. When the data needs to be read, the`Parcelable`interface can be used to deserialize the`Parcel`and turn it back into object data.

There are three primary vectors for exploiting deserialization in Android:

- Taking advantage of a developer's incorrect assumption that deserializing objects proceeding from a custom class type is safe. In reality, any object sourced by any class can be potentially replaced with malicious content that, in the worst case scenario, can interfere with the same or other applications' class loaders. This interference takes the form of injecting dangerous values that, according to the class purpose, may lead, for example, to data exfiltration or account takeover.
- Exploiting deserialization methods that are considered unsafe by design (for example[CVE-2023-35669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2023-35669), a local privilege escalation flaw that allowed arbitrary JavaScript code injection through a deep-link deserialization vector)
- Exploiting flaws in the application logic (for example[CVE-2023-20963](https://nvd.nist.gov/vuln/detail/CVE-2023-20963), a local privilege escalation flaw that allowed an app to download and execute code within a privileged environment through a flaw within Android's WorkSource parcel logic).

## Impact

Any application that deserializes untrusted or malicious serialized data could be vulnerable to remote code execution or denial of service attacks.

## Risk: Deserialization of untrusted input

An attacker can exploit the lack of parcel verification within the application logic in order to inject arbitrary objects that, once deserialized, could force the application to execute malicious code that may result in denial of service (DoS), privilege escalation, and remote code execution (RCE).

These types of attacks may be subtle. For example, an application may contain an intent expecting only one parameter that, after being validated, will be deserialized. If an attacker sends a second, unexpected malicious extra parameter along with the expected one, this will cause all the data objects injected to be deserialized since the intent treats the extras as a[`Bundle`](https://developer.android.com/reference/android/os/Bundle). A malicious user may make use of this behavior to inject object data that, once deserialized, may lead to RCE, data compromise, or loss.

### Mitigations

As a best practice, assume that all serialized data is untrusted and potentially malicious. To ensure the integrity of serialized data, perform verification checks on the data to make sure it's the correct class and format expected by the application.

A feasible solution could be to implement the look-ahead pattern for the`java.io.ObjectInputStream`[library](https://developer.android.com/reference/java/io/ObjectInputStream). By modifying the code responsible for deserialization, you can make sure that[only an explicitly specified set of classes](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html#harden-your-own-javaioobjectinputstream)is deserialized within the intent.

As of Android 13 (API level 33), several methods have been updated within the`Intent`class that are considered safer alternatives to older and now-deprecated methods for handling parcels. These new type-safer methods, such as[`getParcelableExtra(java.lang.String, java.lang.Class)`](https://developer.android.com/reference/android/content/Intent#getParcelableExtra(java.lang.String,%20java.lang.Class%3CT%3E))and[`getParcelableArrayListExtra(java.lang.String, java.lang.Class)`](https://developer.android.com/reference/android/content/Intent#getParcelableArrayListExtra(java.lang.String,%20java.lang.Class%3C?%20extends%20T%3E))perform data type checks to catch mismatch weaknesses that might cause applications to crash and potentially be exploited to perform privilege escalation attacks, such as[CVE-2021-0928](https://nvd.nist.gov/vuln/detail/CVE-2021-0928).

The following example demonstrates how a safe version of the`Parcel`class could be implemented:

Suppose the class`UserParcelable`implements`Parcelable`and creates an instance of user data that's then written to a`Parcel`. The following type-safer method of[`readParcelable`](https://developer.android.com/reference/android/os/Parcel#readParcelable(java.lang.ClassLoader,%20java.lang.Class%3CT%3E))could then be used to read the serialized parcel:  

### Kotlin

    val parcel = Parcel.obtain()
    val userParcelable = parcel.readParcelable(UserParcelable::class.java.classLoader)

### Java

    Parcel parcel = Parcel.obtain();
    UserParcelable userParcelable = parcel.readParcelable(UserParcelable.class, UserParcelable.CREATOR);

Notice in the Java example above the use of`UserParcelable.CREATOR`within the method. This required parameter tells the`readParcelable`method what type to expect and is more performant than the now-deprecated version of the`readParcelable`method.

## Specific Risks

This section gathers risks that require non-standard mitigation strategies or were mitigated at certain SDK level and are here for completeness.

### Risk: Unwanted Object Deserialization

Implementing the`Serializable`interface within a class will automatically cause all subtypes of the given class to implement the interface. In this scenario, some objects may inherit the aforementioned interface, meaning specific objects that are not meant to be deserialized will still be processed. This can inadvertently increase the attack surface.

#### Mitigations

If a class inherits the`Serializable`interface, as per[OWASP guidance](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html#prevent-deserialization-of-domain-objects), the`readObject`method should be implemented as follows in order to avoid that a set of objects in the class can be deserialized:  

### Kotlin

    @Throws(IOException::class)
    private final fun readObject(in: ObjectInputStream) {
        throw IOException("Cannot be deserialized")
    }

### Java

    private final void readObject(ObjectInputStream in) throws java.io.IOException {
        throw new java.io.IOException("Cannot be deserialized");
    }

## Resources

- [Parcelables](https://developer.android.com/reference/android/os/Parcel#parcelables)
- [Parcel](https://developer.android.com/reference/android/os/Parcel)
- [Serializable](https://developer.android.com/reference/java/io/Serializable)
- [Intent](https://developer.android.com/reference/android/content/Intent)
- [Android Deserialization Vulnerabilities: A Brief history](https://securitylab.github.com/research/android-deserialization-vulnerabilities/)
- [Android Parcels: The Bad, the Good and the Better (video)](https://www.youtube.com/watch?v=qIzMKfOmIAA)
- [Android Parcels: The Bad, the Good and the Better (presentation slides)](https://i.blackhat.com/EU-22/Wednesday-Briefings/EU-22-Ke-Android-Parcels-Introducing-Android-Safer-Parcel.pdf)
- [CVE-2014-7911: Android \<5.0 Privilege Escalation using ObjectInputStream](https://seclists.org/fulldisclosure/2014/Nov/51)
- [CVE-CVE-2017-0412](https://bugs.chromium.org/p/project-zero/issues/detail?id=1002)
- [CVE-2021-0928: Parcel Serialization/Deserialization Mismatch](https://nvd.nist.gov/vuln/detail/CVE-2021-0928)
- [OWASP guidance](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html#prevent-deserialization-of-domain-objects)