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
> **Important:** We've refreshed our methodology to reflect how we [benchmarked
> open-weight models](https://developer.android.com/bench/methodology#benchmarking-open-weight-models), and how we calculate the [new dimensions](https://developer.android.com/bench/methodology#new-leaderboard-dimensions) you see on the leaderboard.

*** ** * ** ***

## Goal

AI-assisted software engineering has seen the emergence of several benchmarks to
measure the capabilities of LLMs. Android developers face specific challenges
that aren't covered by existing benchmarks, so we created one that focuses on
Android development. Our goals in publishing this benchmark are:

1. Encourage LLM improvements for Android development.
2. Empower Android developers to be more productive with a range of helpful models to use for AI assistance.
3. Lead to higher quality apps across the Android ecosystem.

We created a model-agnostic benchmark to accurately evaluate LLM performance on
a variety of Android development tasks.

*** ** * ** ***

## Our methodology

Android Bench evaluates the ability of LLMs to generate code that resolves the
issue by presenting them with real-world issues and pull requests from
open-source software projects. This approach aims to ensure that the tasks are
representative of the challenges developers face daily.

To establish a performance baseline and have a constant point of comparison, we
included Gemini 2.5 Flash as the base model. In doing so, we set a minimum for
all the models in the evaluation.

### Safeguards against data contamination

While sourcing real-world repositories is essential for benchmarks' usefulness,
we acknowledge that this exposure might lead to data contamination. In the
current version of the benchmark, we've implemented the following safeguards:

- **Canary strings:** We include the standard BIG-BENCH canary string to discourage the inclusion of these tasks in the future training.
- **Trajectory verification:** Our team performed a thorough review of the agent workflow to ensure that successes were not the result of reward hacking or underspecified tests.

For future versions, we're working hard to further lower this risk.

### Repository criteria

We selected the repositories and individual pull requests by applying the
following criteria:

- The repository needed to contain Android app or library code and be popular among the Android development ecosystem, having greater than or equal to 500 favorites.
- Each pull request needed to be merged, fix a reported issue, and have validation such as unit or instrumentation tests.

Some areas were underrepresented through tasks sourced on GitHub, so we took
some steps to enrich the dataset and increase coverage of these areas:

- If there was a valid pull request without matching tests, we created tests.
- If there was a valid pull request with matching tests but no associated issue, we created an issue.
- In some cases, a pull request had an issue that underspecified what was being done in the change. Because the description is sent to the LLM as a prompt, we rewrote the description of the issue to be more representative of the desired result of the change.

### Defining Android-specific challenges

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

*** ** * ** ***

## The Android Bench composition

To make sure that Android Bench is a good representation of the current Android
ecosystem, we included challenges that replicate those you'll often encounter
during development. The benchmark consists of 100 tasks selected from a pool of
38,989 pull requests.

[You can explore the full dataset on GitHub](https://github.com/android-bench/android-benchthub.com/android-bench/android-bench).

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

*** ** * ** ***

## The Android Bench test harness

To facilitate the execution of the benchmark, Android Bench uses a modified
version of the SWE Bench test harness. It runs in two parts: an Inference Agent
and a Patch Verifier.

1. The Inference Agent combines the [mini SWE agent](https://github.com/SWE-agent/mini-swe-agent) with a custom Docker
   image that can build and run Android projects and a base prompt for Android
   development. Running the agent produces patch files that are then passed to
   the Patch Verifier.

2. The Patch Verifier takes those patches, adds them to the codebase, and
   executes the test suite. It then outputs the data required to assign a score
   to the execution.

The test harness is available in [our GitHub organization](https://github.com/android-bench), allowing anyone
to independently recreate and verify the benchmark results, or to use the test
harness for executing your own tasks.

For full transparency, we've published the [experimental settings and
environment configurations](https://github.com/android-bench/android-benchthub.com/android-bench/android-bench) used to obtain the benchmark results. This allows
researchers and developers to independently recreate and verify our findings, or
to use the test harness for executing their own tasks.

*** ** * ** ***

## Task sourcing and filtering

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

## Benchmarking open-weight models

To evaluate emerging open-weight models on Android Bench, we adapted the test
harness to support diverse model configurations while preserving the benchmark's
statistical integrity.

### Models and infrastructure

This section explains how we established a reliable, standardized benchmarking
setup without managing separate infrastructure for every model.

#### Model aggregation with OpenRouter

To help ensure a reliable and standardized benchmarking environment without
managing an independent infrastructure for each model, the setup uses
[OpenRouter](https://openrouter.ai) as the canonical source for model access.

While this introduces variables typical of multi-provider ecosystems, such as
routing and load balancing, it reflects realistic deployment scenarios. Future
iterations focusing strictly on isolated infrastructure variance can use direct
provider endpoints.

#### Benchmarked models

The following table lists the 13 open-weight models we evaluated, including
their OpenRouter identifiers and the context windows utilized during the
benchmark.

| Model | OpenRouter identifier | Context window |
|---|---|---|
| Gemma 4-31B-it | `google/gemma-4-31b-it:parasail/bf16` | 262,144 |
| Gemma 4-26B-A4B-it | `google/gemma-4-26b-a4b-it:parasail/bf16` | 258,044 |
| Qwen3.6-27B | `qwen/qwen3.6-27b:alibaba` | 262,144 |
| Qwen3.6-35B-A3B | `qwen/qwen3.6-35b-a3b:parasail/fp8` | 262,144 |
| Qwen3.5 9B | `qwen/qwen3.5-9b:venice/fp8` | 262,144 |
| OpenAI GPT OSS 120B | `openai/gpt-oss-120b:deepinfra/turbo` | 131,100 |
| OpenAI GPT OSS 20B | `openai/gpt-oss-20b:deepinfra/bf16` | 131,100 |
| Deepseek 4 pro | `deepseek/deepseek-v4-pro:deepseek` | 1,048,576 |
| Deepseek 4 flash | `deepseek/deepseek-v4-flash:deepseek` | 1,048,576 |
| Xiaomi MiMo 2.5 | `xiaomi/mimo-v2.5-pro:xiaomi/fp8` | 1,050,000 |
| Minimax m2.7 | `minimax/minimax-m2.7:minimax/highspeed` | 196,608 |
| z.ai GLM 5.1 | `z-ai/glm-5.1:z-ai` | 202,800 |
| Kimi K2.6 | `moonshotai/kimi-k2.6:siliconflow/fp8` | 262,144 |
| Qwen 3.6 MAX Preview | `qwen/qwen3.6-max-preview:alibaba` | 262,144 |

> [!NOTE]
> **Note:** Qwen 3.6 MAX preview is a closed-weight model by Qwen that we also included as we were benchmarking open-weight models by the same producer.

#### Providers and deployments

OpenRouter acts as a closed system where not all model providers support each
model, and there are many third-party providers with varying server settings,
such as Parasail, SiliconFlow, DeepInfra, and Venice. The provider manages the
physical hardware and inference engine, while the deployment refers to the
specific configuration, such as the model version and quantization level.

We prioritized the highest available precision offered by the provider---for
example, `bf16` or `fp8`---to minimize performance degradation due to
quantization.

We selected providers and model deployments based on reported reliability and
maximum context window support for each model. We prioritized the highest
available precision offered by the provider---for example, `bf16` or `fp8`---to
minimize performance degradation due to quantization.

To reduce costs and latency for large context tasks, we enabled prompt caching
where supported by the provider and OpenRouter.

### API configuration and execution

To manage API calls across different models, the benchmark harness (a
[`mini-swe-agent`](https://mini-swe-agent.com/latest/) fork) relies on the [LiteLLM](https://github.com/BerriAI/litellm) library to provide an
OpenAI-compatible interface for hundreds of models. We used an interception
layer to apply specific overrides before API execution to adapt open models to
the Android Bench harness without invasive modifications to the core execution
loop.

#### Context window management

LiteLLM defaults unknown models to a conservative context window (often 2,048
tokens). To support the large contexts required for Android Bench, we
dynamically registered all target models with their correct context window
limits and cost parameters.

#### Token management and trimming

Android tasks often involve large repositories and long conversation histories.
The system calculates the maximum allowed input tokens by reserving space for
the requested output and a safety margin of 1,000 tokens. If the context exceeds
this limit, the system removes the oldest messages until it fits, preserving the
system prompt.

Accurate token counting is critical for staying within context limits. One
challenge with aggregator services is that a service's token counting may
slightly differ from local tokenizers. Where possible, we used the default
OpenRouter tokenizer and LiteLLM's default `trim_messages` function.

This relies on LiteLLM's default token counting for those models, which might
introduce variance in trimming precision compared to models with custom
tokenizers. It enables the evaluation of a wider variety of emerging models.

In some cases, such as with Gemma or Minimax, LiteLLM's default trimming
function caused the models to fail all benchmark runs due to missing token
counts. We used specific tokenizer configurations sourced from the official
Hugging Face model card for Gemma and Minimax models to ensure precise local
token counting.

#### Reasoning effort

For models that support explicit reasoning or "thinking" steps, we included the
requirement for `high` reasoning effort in the request header.

This helped us both maximize the models' full reasoning capacity during the
benchmark and avoid the penalty of default low-effort settings common in some
API configurations. As reasoning implementations are model-specific, the
respective provider determines the precise behavior, reflecting the diverse
approaches in current state-of-the-art open models.

> [!IMPORTANT]
> **Key Point:** Examples of these models are DeepSeek, Kimi, GLM, and specific Qwen variants.

#### API errors and retries

To mitigate transient API errors and rate limits from various providers, we
standardized on 10 retries per request across all open models. Adhering to this
standard helps to ensure that the benchmark measures the core capabilities and
intelligence of the models, rather than the transient availability of specific
API endpoints. This approach prioritized functional evaluation over
infrastructure reliability.

## New leaderboard dimensions

We used the following methodology to calculate the cost, token usage, and
latency dimensions on the Android Bench leaderboard. These metrics provide
insight into the resource requirements and efficiency of the evaluated models.

> [!IMPORTANT]
> **Key Point:** When you're comparing model efficiency based on these metrics, prioritize models that achieve a high pass rate while maintaining reasonable resource consumption. A model with a high failure rate may appear to have a lower average cost or latency per run.

### Metrics sourcing and calculation

We extracted execution metrics from the output files generated by the evaluation
harness to provide a comprehensive view of model efficiency beyond pure
accuracy.

Based on the open-source `mini-swe-agent` project, the harness uses `LiteLLM` to
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