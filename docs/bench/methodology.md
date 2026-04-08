---
title: Android Bench  |  Android Developers
url: https://developer.android.com/bench/methodology
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Bench](https://developer.android.com/bench)
* [Our methodology](https://developer.android.com/bench/methodology)

Stay organized with collections

Save and categorize content based on your preferences.




![](/static/images/bench/methodology/hero.png)

### Android Bench methodology

This benchmark evaluates the capabilities of a variety of commonly-used Large Language Models (LLMs) in solving real-world Android development problems. Explore our goals and methodology here.

---

## Goal

AI-assisted software engineering has seen the emergence of several benchmarks to
measure the capabilities of LLMs. Android developers face specific challenges
that aren't covered by existing benchmarks, so we created one that focuses on
Android development. Our goals in publishing this benchmark are:

1. Encourage LLM improvements for Android development.
2. Empower Android developers to be more productive with a range of helpful
   models to use for AI assistance.
3. Lead to higher quality apps across the Android ecosystem.

We created a model-agnostic benchmark to accurately evaluate LLM performance on
a variety of Android development tasks.

---

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
current version of the benchmark, we have implemented the following safeguards:

* **Canary strings:** We include the standard BIG-BENCH canary string to
  discourage the inclusion of these tasks in the future training.
* **Trajectory verification:** Our team performed a thorough review of the
  agent workflow to ensure that successes were not the result of reward
  hacking or underspecified tests.

For future versions, we're working hard to further lower this risk.

### Repository criteria

We selected the repositories and individual pull requests by applying the
following criteria:

* The repository needed to contain Android app or library code and be popular
  among the Android development ecosystem, having greater than or equal to 500
  favorites.
* Each pull request needed to be merged, fix a reported issue, and have
  validation such as unit or instrumentation tests.

Some areas were underrepresented through tasks sourced on GitHub, so we took
some steps to enrich the dataset and increase coverage of these areas:

* If there was a valid pull request without matching tests, we created tests.
* If there was a valid pull request with matching tests but no associated
  issue, we created an issue.
* In some cases, a pull request had an issue that underspecified what was
  being done in the change. Because the description is sent to the LLM as a
  prompt, we rewrote the description of the issue to be more representative of
  the desired result of the change.

### Defining Android-specific challenges

To guarantee Android Bench is a measure of Android engineering competency, we
have curated tasks that are closely aligned with Android development best
practices. We categorized the tasks to ensure that we meet those opinionated
standards.

We prioritized the areas which represent our opinionated standard for building
scalable Android applications, such as:

* Jetpack Compose for UI
* Coroutines and Flows for asynchronous programming
* Room for persistence
* Hilt for dependency injection

We also looked at areas where developers frequently seek help, such as
navigation migrations, Gradle/build configurations, or the handling of breaking
changes across SDK updates.

Additional points of focus included core experiences such as system UI, camera,
or media, alongside platform-specific features such as handling configuration
changes, foldable adaptations, and granular runtime permissions.

By targeting these categories, we aim for better agentic fluency across the
whole landscape of the Android platform.

---

## The Android Bench composition

To make sure that Android Bench is a good representation of the current Android
ecosystem, we included challenges that replicate those you'll often encounter
during development. The benchmark consists of 100 tasks selected from a pool of
38,989 pull requests.

[You can explore the full dataset on GitHub](https://github.com/android-bench/android-bench).

We analyzed GitHub repositories and pull requests and found that 71% were
written in Kotlin and 25% in Java, confirming a shift toward the new programming
language standard. This shift was also represented in the UI area—with 41% of
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

---

## The Android Bench test harness

To facilitate the execution of the benchmark, Android Bench uses a modified
version of the SWE Bench test harness. It runs in two parts: an Inference Agent
and a Patch Verifier.

1. The Inference Agent combines the [mini SWE agent](https://github.com/SWE-agent/mini-swe-agent) with a custom Docker
   image that can build and run Android projects and a base prompt for Android
   development. Running the agent produces patch files that are then passed to the
   Patch Verifier.
2. The Patch Verifier takes those patches, adds them to the codebase, and
   executes the test suite. It then outputs the data required to assign a score
   to the execution.

The test harness is available in [our GitHub organization](https://github.com/android-bench), allowing anyone
to independently recreate and verify the benchmark results, or to use the test
harness for executing your own tasks.

For full transparency, we have published the [experimental settings and
environment configurations](https://github.com/android-bench/android-bench) used to obtain the benchmark results. This allows
researchers and developers to independently recreate and verify our findings, or
to use the test harness for executing their own tasks.

---

## Task sourcing and filtering

Tasks came from two pipelines. The first pipeline automated finding pull
requests that could become tasks. We filtered all the pull requests to ensure
they met the following criteria:

* Originated from a popular Android repository—that is, have at least 500
  stars on GitHub
* Contained tests
* Were marked as fixing an issue in the repository
* Only included changes from the last 3 years

These filters reduced the set of pull requests to task candidates. Task
candidates passed through two different human reviews.

* The first review was for quality assurance. Reviewers checked pull requests
  to ensure code compiled with and without the patch generated by the LLMs, had
  enough context in the description, and didn't include changes that were not
  mentioned in the description. They also assigned a "difficulty" rating to the
  task, estimating how long it would take to write the code for the task
  without LLM assistance.
* A subject matter expert reviewed those tasks that passed quality assurance
  to ensure each one was sufficiently complex and related to Android
  development.

![](/static/images/bench/methodology/chart.png)

Figure: pull request selection funnel

Due to the filtering of pull requests, some good potential candidates were
excluded before making it to the human review. This was because they were
missing either tests or an associated issue. In such cases, we created a prompt
for the pull request or added tests where needed, allowing for additional tasks
to be included in the final evaluation. After enrichment, the tasks went through
the same subject matter expert review process.

To make sure the dataset was representative of the original collection of all
pull requests as we applied these filters, we tracked additional dimensions such
as:

* The programming language the project was written in
* The number of modules in the project
* Whether the project was an app or a library
* If the project contained UI elements, and whether it was written using
  Compose or Views
* The number of files and lines of code changed

Analysis of those dimensions confirmed that our dataset maintains good coverage
across the ecosystem. We tended to select more complex repositories—especially
libraries and projects using Jetpack Compose—to ensure we are testing against
up-to-date architectural standards. Conversely, the specific tasks we selected
tend to be simpler and more focused (involved fewer line changes), mirroring the
small, atomic pull requests with targeted fixes.