---
title: https://developer.android.com/bench/methodology
url: https://developer.android.com/bench/methodology
source: md.txt
---

<br />

![](https://developer.android.com/static/images/bench/methodology/hero.png)

### Android Bench methodology

This benchmark evaluates the capabilities of a variety of commonly-used Large Language Models (LLMs) in solving real-world Android development problems. Explore our goals and methodology here.

> [!IMPORTANT]
> **Important:** We've refreshed our methodology to reflect our adoption of the [Harbor framework](https://www.harborframework.com), built-in tool calling in [mini-swe-agent v2](https://github.com/SWE-agent/mini-swe-agent), how we [benchmarked open-weight models](https://developer.android.com/bench/methodology#benchmarking-open-weight-models), and how we calculate the [new dimensions](https://developer.android.com/bench/methodology#leaderboard-dimensions) you see on the leaderboard.

*** ** * ** ***

## Goal

AI-assisted software engineering has seen the emergence of several benchmarks to
measure the capabilities of LLMs. Android developers face specific challenges
that aren't covered by existing benchmarks, so we created one that focuses on
Android development. Our goals in publishing this benchmark are:

1. Encourage LLM improvements for Android development.
2. Enable Android developers to evaluate and select helpful models for AI assistance.
3. Lead to higher quality apps across the Android ecosystem.

We created a model-agnostic benchmark to accurately evaluate LLM performance on
a variety of Android development tasks.

*** ** * ** ***

## Our methodology

Android Bench evaluates the ability of LLMs to generate code that resolves the
issue by presenting them with real-world issues and pull requests from
open-source software projects. This approach aims to ensure that the tasks are
representative of the challenges developers face daily.

To establish a performance baseline, we initially included Gemini 2.5 Flash as
the base model, with a pass rate of 16.1% in March 2026. In doing so, we had a
minimum for all the models in the evaluation.

The capabilities of current models have advanced significantly, including
built-in and parallel tool calling, streaming events, advanced multi-step
reasoning, stateful conversations, and multimodal capabilities that lets them
interpret images, audio, or video.

As LLMs improve, our evaluation standards must adapt. To continue providing you
with state-of-the-art evaluations that accurately measure the latest model
capabilities on Android development, we are standardizing our benchmark to the
[Harbor framework](https://www.harborframework.com).

*** ** * ** ***

## Defining Android-specific challenges

Because Android Bench is designed to be a measure of Android engineering
competency, we've curated tasks that are closely aligned with Android
development best practices. We categorized the tasks to ensure that we meet
those opinionated standards.

We prioritized the areas which represent our opinionated standard for building
scalable Android applications, such as:

- Jetpack Compose for UI
- Coroutines and Flows for asynchronous programming
- Room for persistence
- Hilt for dependency injection

We also looked at areas where developers frequently seek help, such as
navigation migrations, Gradle/build configurations, or the handling of breaking
changes across SDK updates.

Additional points of focus included core experiences such as system UI, camera,
or media, alongside platform-specific features such as handling configuration
changes, foldable adaptations, and granular runtime permissions.

By targeting these categories, we aim for better agentic fluency across the
whole landscape of the Android platform.

### The Android Bench composition

To make sure that Android Bench is a good representation of the current Android
ecosystem, we included challenges that replicate those you'll often encounter
during development. The benchmark consists of 100 tasks selected from a pool of
38,989 pull requests.

[You can explore the full dataset on GitHub](https://github.com/android-bench/android-bench).

We analyzed GitHub repositories and pull requests and found that 71% were
written in Kotlin and 25% in Java, confirming a shift toward the new programming
language standard. This shift was also represented in the UI area---with 41% of
Jetpack Compose representation, while maintaining 59% View-based tasks to
reflect the reality of many existing codebases.

The majority of Android repositories on GitHub are applications (63%), while
Android Bench trends toward libraries (58%). Thanks to this shift, we can test
LLMs against their ability to handle more restrictions, modularity, and
architectural patterns.

To ensure a more balanced distribution of task complexities, we also broke them
down based on changed lines of code. Nearly half the set (46%) consists of small
changes under 27 lines, followed by 33% that are between 27 and 136 lines, and
the remaining 21% that exceed 136 lines.

Across the benchmark, the median task size is 32 changed lines, with the largest
single change reaching 435 lines.

### Repository criteria

We selected the repositories and individual pull requests by applying the
following criteria:

- The repository needed to contain Android app or library code and be popular among the Android development ecosystem, having greater than or equal to 500 favorites.
- Each pull request needed to be merged, fix a reported issue, and have validation such as unit or instrumentation tests.

Some areas were underrepresented through tasks sourced on GitHub, so we took
some steps to enrich the dataset and increase coverage of these areas:

- If there was a valid pull request without matching tests, we created tests.
- If there was a valid pull request with matching tests but no associated issue, we created an issue.
- In some cases, a pull request had an issue that underspecified what was being done in the change. Because the description is sent to the LLM as a prompt, we rewrote the description of the issue to be more representative of the intended result of the change.

### Task sourcing and filtering

Tasks came from two pipelines. The first pipeline automated finding pull
requests that could become tasks. We filtered all the pull requests to ensure
they met the following criteria:

- Originated from a popular Android repository---that is, have at least 500 stars on GitHub
- Contained tests
- Were marked as fixing an issue in the repository
- Only included changes from the last 3 years

These filters reduced the set of pull requests to task candidates. Task
candidates passed through two different human reviews.

- The first review was for quality assurance. Reviewers checked pull requests to verify code compiled with and without the patch generated by the LLMs, had enough context in the description, and didn't include changes that were not mentioned in the description. They also assigned a "difficulty" rating to the task, estimating how long it would take to write the code for the task without LLM assistance.
- A subject matter expert reviewed those tasks that passed quality assurance to verify each one was sufficiently complex and related to Android development.

:chart: Figure: pull request selection funnel

Due to the filtering of pull requests, some good potential candidates were
excluded before making it to the human review. This was because they were
missing either tests or an associated issue. In such cases, we created a prompt
for the pull request or added tests where needed, allowing for additional tasks
to be included in the final evaluation. After enrichment, the tasks went through
the same subject matter expert review process.

To make sure the dataset was representative of the original collection of all
pull requests as we applied these filters, we tracked additional dimensions such
as:

- The programming language the project was written in
- The number of modules in the project
- Whether the project was an app or a library
- If the project contained UI elements, and whether it was written using Compose or Views
- The number of files and lines of code changed

Analysis of those dimensions confirmed that our dataset maintains good coverage
across the ecosystem. We tended to select more complex repositories---especially
libraries and projects using Jetpack Compose---to ensure we are testing against
up-to-date architectural standards. Conversely, the specific tasks we selected
tend to be simpler and more focused (involved fewer line changes), mirroring the
small, atomic pull requests with targeted fixes.

### Safeguards against data contamination

While sourcing real-world repositories is essential for benchmark utility, this
exposure introduces potential training contamination risks. Since the initial
release of the benchmark, we have included the standard BIG-BENCH canary string
in all task files to discourage their inclusion in training corpora.

Our team performs manual audits of agent execution trajectories to verify that
successful runs result from legitimate code fixes rather than reward hacking or
underspecified tests. We continue developing additional safeguards to further
reduce contamination risks.

*** ** * ** ***

## Benchmark execution

When we designed Android Bench, we anchored our methodology on the best-in-class
industry standards available at the time. We used mini-swe-agent, a
general-purpose benchmarking agent, and adapted it to the nuances of Android
development.

However, LLM capabilities are continuously and rapidly improving, so we need to
adapt how we benchmark them. To continue providing state-of-the-art evaluations
that accurately measure the latest model capabilities on Android development, we
are standardizing our benchmark to the [Harbor framework](https://www.harborframework.com).

Harbor defines standards and integrations that enable anyone to run the
benchmark, evaluate their preferred set-up, or share results, providing
additional transparency and visibility.

The configuration of our environment is also available in
[our GitHub organization](https://github.com/android-bench), allowing anyone to independently recreate and
verify the benchmark results, or to use the setup for executing your own tasks.

For full transparency, we've published the
[dataset on Harbor Hub](https://github.com/android-bench/android-bench). This allows researchers and developers to
independently recreate and verify our findings, evaluate their choice of models
or agents, and share results.

### Built-in tool calling and system instructions

In `mini-swe-agent` v1, models outputted shell commands as text inside Markdown
code blocks, and the system extracted them using regular expressions. In v2, the
execution interface shifted to native tool calling, requiring models to call an
explicit bash function tool through the provider API.

Models prompted with legacy instructions continued formatting commands as
Markdown code blocks. Because v2 evaluation only executes commands submitted
through the native tool API, these text blocks were not executed as commands.

To prevent unexecuted commands, we updated the system instructions and Pydantic
configuration schemas to require native tool invocation. Evaluated models
receive schema definitions for the bash tool and must invoke the tool using the
API rather than emitting Markdown text blocks.

To preserve Android engineering expertise without breaking the core tool-calling
mechanism, we explicitly changed the baseline system prompt from
`mini-swe-agent` v2 to include domain-specific Android steering. Otherwise, the
configuration directly mirrors `swe-bench.yaml`'s latest set up.

### API configuration and execution

To coordinate API calls across different models and inference endpoints (such as
OpenAI, Anthropic, Gemini, Kimi, MiniMax, DeepSeek, and [OpenRouter](https://openrouter.ai)), we use
the model interface classes from [`mini-swe-agent`](https://mini-swe-agent.com/latest/) v2.

For open-weight models accessed using OpenRouter's, we use `mini-swe-agent`'s
built-in OpenRouter's model class. For other provider endpoints, we use
`mini-swe-agent`'s built-in [LiteLLM](https://github.com/BerriAI/litellm) class to provide an OpenAI-compatible
interface.

We have prioritized accessing all models through their provider's endpoint,
using OpenRouter in cases where this wasn't accessible.

*** ** * ** ***

## Leaderboard dimensions

We used the following methodology to calculate the cost, token usage, and
latency dimensions on the Android Bench leaderboard. These metrics provide
insight into the resource requirements and efficiency of the evaluated models.

> [!IMPORTANT]
> **Key Point:** When you're comparing model efficiency based on these metrics, prioritize models that achieve a high pass rate while maintaining reasonable resource consumption. A model with a high failure rate may appear to have a lower average cost or latency per run.

### Metrics sourcing and calculation

We extracted execution metrics from the output files generated by the evaluation
system to provide a comprehensive view of model efficiency beyond pure accuracy.

Based on the open-source `mini-swe-agent` project, the system uses `LiteLLM` to
interface with various model endpoints, letting us capture standardized usage
data.

We processed each metric according to the following methodology:

| Metric | Source |
|---|---|
| Cost | We computed cost by extracting the monetary value associated with API calls to the model providers, based on standard provider pricing at the time of execution, normalizing currency representations to floating-point values in USD. |
| Token Usage | We tracked token consumption by analyzing the prompt and completion token counts reported by the inference engine for each conversational turn. |
| Latency | We measured end-to-end latency in seconds, including network transit time to the API endpoint, encompassing both prompt processing (prefill) and token generation (decoding) phases. |

### Run-level average calculation

To provide a representative cost and time estimate for a complete benchmark run
(100 tasks), we computed metrics at the run level rather than the task level:

1. We calculated the total resource consumption (cost, tokens, latency) across all tasks within a single execution of the 100-task suite.
2. We calculated the arithmetic mean of these totals across all 10 runs for a given model.

This approach accounts for variability across multiple attempts while providing
a realistic projection of the resources required for a full evaluation.

*** ** * ** ***

## Methodology limitations and caveats

Because we sum the actual recorded resources for all tasks in a run, a model
with a high failure rate may appear to have a lower average cost or latency per
run. This lower value indicates incomplete execution, not superior efficiency.

### Bias toward incomplete runs

Summing resource consumption across all tasks in a run creates a structural bias
toward models with higher failure rates. A model that fails early on multiple
tasks will incur lower total cost and latency than a model that works longer to
solve them. These metrics measure gross resource consumption per attempt, not
normalized efficiency. We strongly recommend evaluating these dimensions only
among models with comparable pass rates.

### Environmental variability in latency

Latency measurements include network transit time to the API endpoints.
Consequently, these values are subject to network conditions and the
geographical location of the client relative to the provider's servers. They
don't solely reflect the model's internal processing speed.

### Pricing fluctuations

Cost calculations rely on provider pricing active at the time of execution.
Because API pricing in the model market is highly dynamic, costs recorded at
different times may not be directly comparable.

### Token optimization variance

Token counts are listed as reported by the inference engine for each turn. This
tracking may not account for provider-specific optimizations, such as prompt
caching or shared system prompts, unless explicitly reported in the API response
usage metadata.