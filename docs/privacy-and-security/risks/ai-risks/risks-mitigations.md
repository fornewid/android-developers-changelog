---
title: https://developer.android.com/privacy-and-security/risks/ai-risks/risks-mitigations
url: https://developer.android.com/privacy-and-security/risks/ai-risks/risks-mitigations
source: md.txt
---

This guide provides crucial information for developers building Android applications using generative AI (GenAI). GenAI integration presents unique challenges that extend beyond standard software development.

This guide is continuously updated to reflect new and evolving AI risks. Use this content to understand the significant risks associated with integrating GenAI capabilities into your apps and discover effective mitigation strategies.

## Prompt injection

[OWASP Risk Description](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

An attacker crafts malicious inputs (prompts) to trick the model into bypassing its security and safety policies or performing unintended actions. A successful attack could cause the model to reveal sensitive data, generate harmful content, or execute unintended actions, damaging user trust. Learn how to mitigate[prompt injection attacks](https://developer.android.com/privacy-and-security/risks/ai-risks/prompt-injection).

## Sensitive information disclosure

[OWASP Risk Description](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

Generative AI models pose a significant risk of sensitive information disclosure, potentially leaking a wide range of data affecting both the LLM and its application context. Leaks can occur when the model outputs this confidential data to other users, when machine learning as a service (MLaaS) providers insecurely store prompts, or when malicious actors exploit the system to reveal internal logic. The consequences are severe, ranging from intellectual property breaches and regulatory penalties (for example,[GDPR](https://gdpr-info.eu/),[CCPA](https://oag.ca.gov/privacy/ccpa))) to a complete loss of user trust and system compromise. Learn how to[mitigate sensitive information disclosure](https://developer.android.com/privacy-and-security/risks/ai-risks/sensitive-data-disclosure)risk.

## Excessive agency

[OWASP Risk Description](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

Integrating LLM agents with functions or tools to undertake actions can introduce security risks. Malicious prompts exploiting function calling could lead to unintended data loss. Developers are responsible for implementing safeguards (e.g., user consent, validation, access controls) to prevent harmful AI actions. Learn how to[mitigate excessive agency risk](https://developer.android.com/privacy-and-security/risks/ai-risks/excessive-agency).

## Summary

Securing GenAI systems requires a multi-faceted approach that extends traditional cybersecurity practices to address the unique challenges posed by AI models, like development lifecycle, and interactions with users and systems. This comprehensive effort involves proactive testing, continuous monitoring, robust governance, and adherence to evolving regulatory frameworks. A great way to put these principles into practice is by using industry tools like the[SAIF Risk Self-Assessment](https://saif.google/risk-self-assessment)to better understand and mitigate risks.