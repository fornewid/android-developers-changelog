---
title: https://developer.android.com/studio/gemini/faq
url: https://developer.android.com/studio/gemini/faq
source: md.txt
---

# FAQ

This page lists some frequently asked questions about Gemini in Android Studio and how it works. For more resources, see the[troubleshooting guide](https://developer.android.com/studio/gemini/troubleshooting). If you still have questions,[send feedback](https://developer.android.com/studio/report-bugs).

## Does Gemini send my code to Google's servers?

Learn about what data is shared and how you can control your privacy settings at[Data and privacy](https://developer.android.com/studio/gemini/data-and-privacy).

## Does Gemini give accurate and safe responses?

Accelerating people's ideas with generative AI is truly exciting, but it's still early days, and Gemini is an experiment. Some of the responses might be inaccurate, so double-check information in the responses. With your feedback, Gemini is improving. While Gemini has built-in safety controls and clear mechanisms for feedback in line with our[AI Principles](https://developer.android.com/studio/gemini/data-and-privacy), be aware that it might display inaccurate information or offensive statements.

Because AI is an evolving technology, it can generate output that sounds plausible but is factually incorrect. We recommend that you validate all output from Gemini before you use it.

## Can I access Gemini without sharing context?

Yes. By default, Gemini can't see the code in the editor window and only uses the prompts and conversation history in the chatbot to respond. However, you can opt in to sharing context from your codebase to enable higher quality responses and access to experimental features such as AI code completion.

## Can Gemini help with coding?

Yes, Gemini can help with coding and topics about coding. It is experimental and you are responsible for your use of code or coding explanations. Use discretion and carefully test all code for errors, bugs, and vulnerabilities before relying on it.

## How can I reset chat history?

Gemini uses the chat history for additional context when responding to your prompts. If your chat history is no longer relevant to what you're currently trying to achieve, reset the chat history by clicking**Clear Conversation History** ![](https://developer.android.com/static/studio/images/gemini-reset-chat.png)in the Gemini pane.

## Why do I get a "code is blocked" error message?

Gemini conducts multiple layers of checks on model-generated responses. For example, there's a check to ensure that the model-generated code doesn't replicate existing content at length. It's possible that your response gets blocked due to one of these checks. In this case, try again with a different prompt.

## How and when does Gemini cite sources in its responses?

Gemini should generate original content and not replicate existing content at length. We've designed our systems to limit the chances of this occurring, and we will continue to improve how these systems function. If Gemini does directly quote at length from a code repository, it cites that source. The citation might also reference an applicable open source license. It is your responsibility to comply with any license requirements.

## What terms of service apply to my Gemini usage?

Your use of Gemini is subject to the[Google Terms of Service](https://policies.google.com/terms)and the[Generative AI Additional Terms of Service](https://policies.google.com/terms/generative-ai).

## How is Gemini different from other LLM-powered chatbots?

Gemini leverages an LLM that was designed to help with coding scenarios. Gemini is tightly integrated within Android Studio, which means it can provide more relevant responses, and lets you to take actions and apply suggestions with just a click.

## What are some tips for using Gemini?

- Be clear and concise when you ask your question.
- Use simple language that Gemini can understand.
- If Gemini does not understand your question, try rephrasing it.
- Review Gemini suggestions before using them.

For more details, see[Best practices](https://developer.android.com/studio/gemini/best-practices).

## How can I report feedback about Gemini?

We're looking for your feedback to help us improve Gemini responses across all of the domains of Android development. To help, use Gemini in your development workflow and mark its responses as helpful or not helpful using the thumbs up and thumbs down options in the Gemini UI. This input helps us identify the areas that need more training.

## How can I give feedback about a specific AI response?

To help us improve, rate the generated output with a thumbs up or thumbs down. If you get an AI response that you feel is unsafe, not helpful, inaccurate, or bad for any other reason, let us know by submitting feedback using the**Provide Feedback**option that appears when you select thumbs down.