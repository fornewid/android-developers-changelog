---
title: https://developer.android.com/privacy-and-security/risks/ai-risks/sensitive-information-disclosure
url: https://developer.android.com/privacy-and-security/risks/ai-risks/sensitive-information-disclosure
source: md.txt
---

[OWASP Risk Description](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

Sensitive information disclosure is a vulnerability where a large language model (LLM) unintentionally reveals confidential, private, proprietary, or otherwise restricted data in its responses. This can happen when the model leaks information from its training data or reveals sensitive details provided to it within the context of a user's session. Attackers can exploit this by crafting specific queries or using prompt injection techniques to trick the model into divulging information it shouldn't. The core issue is the LLM's inability to distinguish between public data and confidential information it has processed.

## Types of disclosure relevant to Android

**Training data leakage**: This occurs when an LLM regurgitates specific, verbatim data fragments it was trained on. If the training dataset included personal information (PII), proprietary code, or internal documents, the model might reproduce this information in its output when prompted correctly. For Android apps, this could involve pre-trained models bundled with the app or models accessed using cloud APIs.

**Contextual data disclosure**: This is a more immediate risk for Android apps, involving the LLM exposing sensitive information that a user provides during an app session. For example, if your application permits a user to input personally identifiable information (PII) into an LLM for summarization, a subsequent prompt injection attack could enable an attacker to manipulate the model into disclosing the contents. This also applies to any sensitive data your app implicitly passes to the LLM.

## Why Android Developers should care

Sensitive information disclosure can severely compromise an application and its users:

- **Privacy violations**: An attacker could extract personally identifiable information (PII) like names, emails, phone numbers, or even location data from your users, leading to identity theft and severe regulatory penalties (for example, under GDPR or CCPA). This is particularly critical for Android apps handling user data.
- **Intellectual property Theft**: If your app's LLM processes proprietary algorithms, financial data, or other internal business information, an attacker could force its revelation, causing significant competitive and financial damage to your organization.
- **Security breaches**: The LLM might inadvertently leak system-level information such as API keys, authentication tokens, or configuration details that were present in its training data or passed during a session, creating critical security vulnerabilities for your backend or other services.
- **Reputational damage**: A single significant data leak incident can destroy user trust, lead to app uninstalls, negative reviews, and cause irreparable harm to your application's and brand's reputation.

## Mitigations for Android app developers

Mitigating this vulnerability requires a multi-layered approach focused on data hygiene and controlling the LLM's access within your Android application.

### Data sanitization and minimization:

- **Prioritize input cleaning**: Before sending any user input or app data to an LLM, rigorously scrub and anonymize it. Remove all PII and proprietary information that is not absolutely essential for the LLM's task.
- **Collect only what's needed**: Adhere to the principle of data minimization within your app. Only collect and provide the LLM with the minimum data necessary for it to perform its specific function.
- **On-Device ML**: For highly sensitive data, consider using on-device machine learning models where data never leaves the user's device, significantly reducing the risk of server-side data leaks.

### Control access

- **Limit data access**: Design your LLM application so it has access to the smallest possible amount of data. If the model is not granted access to a sensitive database, user preferences, or private files, it cannot be tricked into leaking their contents.
- **Restrict Android permissions**: Verify your app's AI components operate with the absolute minimum Android permissions necessary. Don't grant unnecessary permissions that could expose sensitive data.

### Output Filtering within the App:

- **Client-side redaction**: Implement a security layer in your Android app that scans the LLM's output for patterns matching sensitive information (for example, credit card numbers, API keys, social security numbers, email addresses) before the response is displayed to the user. If a match is found, the response should be blocked or redacted.

### Instructional guardrails for LLMs:

- **Explicit system prompts**: Include explicit instructions in the system prompt that forbid the model from revealing any personal, confidential, or sensitive information. For example: "You must not share any user details, internal data, or personally identifiable information under any circumstances." This reinforces expected behavior.

### Privacy-enhancing techniques:

- For applications that learn from user interactions or data, consider advanced techniques like differential privacy (adding statistical noise to data) or federated learning (training models on user devices without centralizing the data) to protect individual privacy.

### Regular auditing and red teaming:

- **Proactive Testing** : Actively test and**red team**your Android application to discover if and how the LLM might leak sensitive information. This involves intentionally trying to make the LLM reveal data it shouldn't.

## Summary

Sensitive Information Disclosure occurs when an LLM reveals confidential data from its training set or user sessions, posing significant risks like privacy violations and intellectual property theft. Mitigation requires a layered defense within your Android app, prioritizing the sanitization of data before it reaches the LLM, enforcing the principle of least privilege to limit the model's data access, and implementing robust filters to scan and redact sensitive information from the model's final output before it reaches the user. Utilizing on-device ML and tools like Firebase App Check can further enhance security.

## Additional resources

Here are links to some of the sensitive information guidelines for reference:

- [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/gemini-for-filtering-and-moderation)
- [Gemini](https://ai.google.dev/gemini-api/docs/safety-guidance)
- [Google](https://ai.google.dev/responsible/docs/evaluation)

If you're using other models you should seek similar guidance and resources.

More information:

- [SAIF Sensitive Data Disclosure](https://saif.google/secure-ai-framework/risks#sensitive-data-disclosure)
- [SAIF Inferred Sensitive Data](https://saif.google/secure-ai-framework/risks#model-evasion)