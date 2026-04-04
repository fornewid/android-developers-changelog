---
title: https://developer.android.com/privacy-and-security/risks/insecure-library
url: https://developer.android.com/privacy-and-security/risks/insecure-library
source: md.txt
---

# Insecure API or Library

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

Using insecure APIs or libraries significantly reduces an application's security posture. A security breach in any of these dependencies would allow an attacker to leverage a number of vectors to conduct a broad set of attacks such as man- in-the-middle (MitM) and remote code execution (RCE).

The threat of implementing insecure dependencies arises when developers don't integrate security assessments and vulnerability testing into the Software Development Lifecycle (SDLC) or, in some cases, don't implement an automated update policy for application dependencies.

Dependency exploitation usually starts by analyzing application binary (.apk) to search for vulnerable libraries. At this point, Open Source Intelligence (OSINT) is performed to unearth previously discovered potentially exploitable vulnerabilities. Attackers can then leverage publicly disclosed vulnerability information such as common vulnerabilities and exposures (CVEs) to perform further attacks.

## Impact

The successful exploitation of insecure dependencies can lead to a broad set of attacks such as remote code execution (RCE), SQL injections (SQLi), or cross- site scripting (XSS). Therefore, the overall impact is directly related to the type of vulnerability that third-party software introduces and that attackers can exploit. Possible consequences of a successful exploitation of vulnerable dependencies are data breaches or service unavailability, which may lead to a significant impact on reputation and economic turnover.

## Mitigations

### Defense in depth

Note that the mitigations listed below have to be implemented in combination to ensure a stronger security posture, and reduce the application's attack surface. The exact approach should always be evaluated on a case-by-case basis.

### Dependency vulnerability assessments

Implement dependency verification at the beginning of the development lifecycle to detect vulnerabilities within third-party code. This phase tests whether the code that is not built in-house is secure before being rolled out in production environments. Verification could be complemented by implementing static application security testing (SAST) and dynamic application security testing (DAST) tools within the software development lifecycle to improve the security posture of the application.

### Continuously update dependencies

Always be careful to continuously update any dependency embedded within the code. For this purpose, it is recommended to implement automatic updates that are pushed to production whenever a third-party component releases a new security patch.

### Perform application penetration testing

Conduct regular penetration tests. These kinds of tests aim to uncover any well- known vulnerability that could affect proprietary code and, or third-party dependencies. Additionally, security assessments frequently uncover unknown vulnerabilities (0-days). Penetration tests are helpful for developers, as they provide them with a snapshot of the application's current security posture and help them prioritize exploitable security issues that have to be addressed.

## Resources

- [How to recognise and manage insecure dependencies](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)

- [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features)

- [How to secure dependencies](https://www.hacksplaining.com/prevention/toxic-dependencies)

- [CWE-1395: Dependency on Vulnerable Third-Party Component](https://cwe.mitre.org/data/definitions/1395.html)

- [SDK implementation best-practices for Android.](https://developer.android.com/guide/practices/sdk-best-practices)