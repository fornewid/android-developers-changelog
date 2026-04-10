---
title: https://developer.android.com/privacy-and-security/risks/xml-external-entities-injection
url: https://developer.android.com/privacy-and-security/risks/xml-external-entities-injection
source: md.txt
---

# XML External Entities Injections (XXE)

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

An XML eXternal Entity injection (XXE) is an attack against applications that parse XML input. An XXE attack occurs when untrusted XML input with a reference to an external entity is processed by a weakly configured XML parser. This attack can be used to stage multiple incidents, including denial of service, file system access, or data exfiltration.

## Impact

When an application parses an XML document, it can process any DTDs (Document Type Definitions, also known as external entities) contained within the document. An attacker can exploit this behavior by injecting malicious code as DTDs. This code can then access parts of the file system of the device, only accessible to the application and potentially containing sensitive data. Furthermore, this malicious code can make requests from the device, potentially bypassing perimeter security measures.

Lastly, if the application expands DTDs, this can create a situation with multiple iterations of referenced entities, exhausting the resources of the device and leading to a denial of service.

## Mitigations

### Disable DTDs

The safest way to prevent XXE is to always disable DTDs (external entities) completely. Depending on the parser in use, the method could be similar to the following example for the XML Pull Parser library:  

### Java

    XmlPullParserFactory factory = XmlPullParserFactory.newInstance();
    factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);

### Kotlin

    val factory = XmlPullParserFactory.newInstance()
    factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)

Disabling DTDs also makes the parser secure against denial of service attacks. If it is not possible to disable DTDs completely, then external entities and external document type declarations must be disabled in a way that's specific to each parser.

Because of the large number of XML parsing engines in the market, the ways to prevent XXE attacks differ from engine to engine. You may need to refer to your engine documentation for more information.

### Perform input sanitisation

The application should be reconfigured so that it does not allow users to inject arbitrary code in the XML document's preamble. This has to be verified server-side, as client-side controls can be bypassed.

### Use a different library

If the library or method used cannot be configured in a secure manner, a different one should be considered.[XML Pull Parser](https://developer.android.com/reference/org/xmlpull/v1/XmlPullParser)and[SAX Parser](https://developer.android.com/reference/javax/xml/parsers/SAXParser)can both be configured in a secure manner, disallowing DTDs and entities.

## Resources

- [OWASP XXE](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing)
- [OWASP XXE Prevention Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- [XML Constants: FEATURE_SECURE_PROCESSING](https://developer.android.com/reference/javax/xml/XMLConstants#FEATURE_SECURE_PROCESSING)
- [XML Pull Parser](https://developer.android.com/reference/org/xmlpull/v1/XmlPullParser)
- [SAX Parser](https://developer.android.com/reference/javax/xml/parsers/SAXParser)