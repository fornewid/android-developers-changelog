---
title: https://developer.android.com/bench
url: https://developer.android.com/bench
source: md.txt
---

![](http://developer.android.com/static/images/bench/hero.png)

### Android Bench

AI-assisted software engineering has seen the emergence of several benchmarks to measure the capabilities of LLMs. Android developers face specific challenges that aren't covered by existing benchmarks, so we created one that focuses on a north star of high quality Android development.

#### Android LLM Leaderboard

All models Open weight models Closed weight models

| Model | Score (%) info Average percentage of 100 test cases successfully resolved across 10 runs for each model | arrow_range Cl range (%) info Expected performance range, reflecting the results' statistical reliability (p-value \< 0.05) | Avg latency (h) info Average time taken to solve 100 tasks across 10 runs | Avg total tokens (M) info Average token consumption for a full benchmark run (100 tasks) across 10 runs | Avg cost ($) info Average cost per full benchmark run | Date |
|---|---|---|---|---|---|---|
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.5 | **74.0** | 66.8 --- 80.5 | 15.5 | 64.5 | $133.9 | 2026-04-27 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.4 | **72.4** | 65.4 --- 79.3 | 21.2 | 64.2 | $91.7 | 2026-03-16 |
| :gemini: Gemini 3.1 Pro Preview | **72.4** | 65.1 --- 78.8 | 11.5 | 75.4 | $49.0 | 2026-02-27 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 4 7 | **68.7** | 60.5 --- 75.9 | 11.6 | 90.0 | $124.3 | 2026-04-27 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.3 Codex | **67.7** | 59.9 --- 75.6 | 11.2 | 71.4 | $42.6 | 2026-03-18 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 4 6 | **66.6** | 59.1 --- 74.1 | 9.9 | 69.5 | $84.4 | 2026-02-26 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.2 Codex | **62.5** | 54.4 --- 70.0 | 24.3 | 124.4 | $121.9 | 2026-02-27 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 4.5 | **61.9** | 53.9 --- 70.2 | 12.5 | 79.8 | $102.5 | 2026-02-26 |
| :gemini: Gemini 3 Pro Preview | **60.4** | 52.3 --- 67.7 | 9.8 | 117.0 | $63.7 | 2026-02-27 |
| ![](https://developer.android.com/static/images/bench/icons/z-ai.png) GLM 5.1 | **59.7** | 52.4 --- 67.4 | 33.4 | 80.2 | $46.7 | 2026-05-08 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 4.6 | **58.4** | 50.3 --- 66.4 | 8.2 | 47.9 | $40.4 | 2026-03-01 |
| ![](https://developer.android.com/static/images/bench/icons/moonshotai.png) Kimi K2.6 | **58.6** | 51.3 --- 66.5 | 29.9 | 94.3 | $42.5 | 2026-05-10 |
| ![](https://developer.android.com/static/images/bench/icons/deepseek.png) DeepSeek V4 Pro | **55.4** | 47.5 --- 63.6 | 35.8 | 132.7 | $13.7 | 2026-05-08 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 4.5 | **54.2** | 45.9 --- 62.2 | 13.1 | 92.9 | $60.3 | 2026-02-26 |
| ![](https://developer.android.com/static/images/bench/icons/deepseek.png) DeepSeek V4 Flash | **52.7** | 45.3 --- 60.7 | 28.1 | 164.7 | $8.4 | 2026-05-11 |
| ![](https://developer.android.com/static/images/bench/icons/xiaomi.png) MiMo 2.5 Pro | **52.0** | 43.8 --- 60.0 | 33.1 | 97.5 | $74.5 | 2026-05-09 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen 3.6 Max Preview | **51.4** | 43.5 --- 59.3 | 20.5 | 103.0 | $222.4 | 2026-05-07 |
| :gemini: Gemini 3 Flash Preview | **42.0** | 36.6 --- 47.3 | 16.5 | 148.0 | $34.2 | 2026-02-26 |
| ![](https://developer.android.com/static/images/bench/icons/minimax.png) MiniMax M2.7 | **37.2** | 30.3 --- 44.9 | 20.3 | 128.3 | $10.1 | 2026-05-01 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen 3.6 27B | **37.4** | 30.5 --- 44.5 | 20.7 | 112.3 | $64.6 | 2026-05-05 |
| ![](https://developer.android.com/static/images/bench/icons/google.png) Gemma 4 31B IT | **33.2** | 26.2 --- 40.8 | 14.2 | 29.5 | $2.5 | 2026-05-01 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen 3.6 35B A3B | **31.7** | 24.4 --- 39.0 | 12.5 | 113.4 | $10.7 | 2026-05-05 |
| :gemini: Gemini 2.5 Pro | **29.1** | 22.3 --- 36.1 | 8.4 | 37.9 | $35.8 | 2026-03-02 |
| ![](https://developer.android.com/static/images/bench/icons/google.png) Gemma 4 26B A4B IT | **25.1** | 18.8 --- 31.8 | 21.4 | 77.2 | $3.3 | 2026-05-01 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT OSS 120B | **18.9** | 13.1 --- 25.1 | 25.9 | 122.7 | $7.6 | 2026-05-09 |
| :gemini: Gemini 2.5 Flash | **15.9** | 10.7 --- 21.1 | 4.9 | 108.8 | $11.2 | 2026-02-26 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen 3.5 9B | **15.5** | 10.1 --- 20.9 | 16.6 | 181.4 | $15.6 | 2026-05-07 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT OSS 20B | **2.4** | 1.2 --- 3.9 | 3.8 | 12.0 | $0.2 | 2026-05-11 |

**Latest results as of May 18th 2026:** This refresh includes [open-weight models](https://developer.android.com/bench/methodology#benchmarking-open-weight-models), adding new columns for [latency, tokens, and cost](https://developer.android.com/bench/methodology#new-leaderboard-dimensions).  
**Check back periodically for updates!** ![](http://developer.android.com/static/images/picto-icons/badge.svg)

## Learn more about Android Bench

### [Our methodology](http://developer.android.com/bench/methodology)

Learn more about how we created a set of common Android developer tasks. [Read more](http://developer.android.com/bench/methodology)

### [Android best practices](http://developer.android.com/develop)

Many of the tasks are based on how we define high quality Android development, which is detailed in our developer documentation. [Read more](http://developer.android.com/develop)

### [GitHub repo](https://github.com/android-bench/android-bench)

See the full repo so you can replicate the tests yourself. [View more](https://github.com/android-bench/android-bench)