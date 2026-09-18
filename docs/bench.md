---
title: https://developer.android.com/bench
url: https://developer.android.com/bench
source: md.txt
---

![](http://developer.android.com/static/images/bench/hero.png)

### Android Bench 2.0

AI-assisted software engineering has seen the emergence of several benchmarks to measure the capabilities of LLMs. Android developers face specific challenges that aren't covered by existing benchmarks, so we created one that focuses on a north star of high quality Android development. ![](https://developer.android.com/static/images/bench/icons/lht_icon.svg) Android Bench now includes **long-horizon task** results using specialized agents. **Click a model** for detailed results, or learn more in our [blog](http://android-developers.googleblog.com/2026/09/android-bench-2-long-horizon-tasks.html) and [methodology](https://developer.android.com/bench/methodology/2).

### Long-horizon task results

All agents antigravity-sdk claude-code codex kimi-code qwen-coder All models Open weights models Closed weights models

| Model - Agent | Pass rate (%) info Average percentage of 30 tasks successfully resolved across all runs for each model | arrow_range Cl range (%) info Expected performance range, reflecting the results' statistical reliability (p-value \< 0.05) | Completion rate (%) info How close each run got to a complete solution, even when the task failed | Avg latency (h) info Average time taken to solve 30 tasks across all runs | Avg cost ($) info Average cost per full benchmark run |
|---|---|---|---|---|---|
| <button data-modal-dialog-id="android-bench-score-model-dialog-openai/gpt-6-astra"> </button> ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 6 Astra codex chevron_right | **28.0** | 13.3 --- 42.0 | **82.2** | 7.9 | $375.7 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-anthropic/claude-fable-5-1"> </button> ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Fable 5 1 claude-code chevron_right | **22.7** | 10.7 --- 36.0 | **82.4** | 22.2 | $492.6 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-openai/gpt-5.6-sol"> </button> ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Sol codex chevron_right | **19.3** | 7.3 --- 32.0 | **74.3** | 8.6 | $235.8 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-anthropic/claude-opus-5"> </button> ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 5 claude-code chevron_right | **16.7** | 5.3 --- 29.3 | **77.8** | 27.0 | $861.4 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-qwen/qwen3.8-max"> </button> ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.8 Max qwen-coder chevron_right | **14.0** | 4.7 --- 24.0 | **74.3** | 47.2 | $260.2 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-kimi-k3"> </button> ![](https://developer.android.com/static/images/bench/icons/moonshot.png) Kimi K3 kimi-code chevron_right | **12.0** | 3.3 --- 22.0 | **72.8** | 66.2 | $418.3 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-gemini/gemini-3.8-flash"> </button> :gemini: Gemini 3.8 Flash antigravity-sdk chevron_right | **8.0** | 3.3 --- 13.3 | **47.4** | 12.1 | $34.5 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-gemini/gemini-3.7-flash"> </button> :gemini: Gemini 3.7 Flash antigravity-sdk chevron_right | **7.3** | 1.3 --- 14.7 | **50.1** | 9.9 | $26.0 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-anthropic/claude-sonnet-5"> </button> ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 5 claude-code chevron_right | **6.7** | 1.3 --- 13.3 | **59.8** | 14.7 | $283.7 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-openai/gpt-5.6-terra"> </button> ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Terra codex chevron_right | **4.7** | 1.3 --- 8.7 | **53.4** | 5.1 | $53.2 |
| <button data-modal-dialog-id="android-bench-score-model-dialog-openai/gpt-5.6-luna"> </button> ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Luna codex chevron_right | **3.3** | 0.7 --- 7.3 | **55.2** | 7.6 | $13.5 |

### ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 6 Astra
•
[codex](https://chatgpt.com/codex/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 28.0% Avg completion rate 82.2% Avg latency 7.9 h Avg cost $375.7

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 99% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 83% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 98% | 3/5 | 2 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 88% | 0/5 | All runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 71% | 2/5 | 2 runs failed tests, 1 run missed required test results |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 100% | 5/5 | N/A |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 97% | 2/5 | 3 runs failed tests |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 68% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 93% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 63% | 0/5 | 4 runs failed validation, 1 run failed the build |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 99% | 4/5 | 1 run failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 47% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 92% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 100% | 5/5 | N/A |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 73% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 94% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 93% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 100% | 5/5 | N/A |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 79% | 1/5 | 4 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 74% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 47% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 80% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 100% | 5/5 | N/A |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 80% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 97% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 11% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 100% | 5/5 | N/A |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 93% | 0/5 | All runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 35% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 100% | 5/5 | N/A |

### ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Fable 5 1
•
[claude-code](https://claude.com/product/claude-code)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 22.7% Avg completion rate 82.4% Avg latency 22.2 h Avg cost $492.6

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 99% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 73% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 100% | 5/5 | N/A |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 93% | 2/5 | 3 runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 94% | 1/5 | 4 runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 80% | 4/5 | 1 run missed required test results |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 87% | 1/5 | 2 runs failed tests, 2 runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 60% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 94% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 78% | 0/5 | All runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 94% | 1/5 | 4 runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 86% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 90% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 100% | 5/5 | N/A |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 71% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 94% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 94% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 80% | 4/5 | 1 run failed the build |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 92% | 3/5 | 2 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 73% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 56% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 86% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 26% | 1/5 | 3 runs missed required test results, 1 run failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 95% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 93% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 11% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 100% | 5/5 | N/A |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 96% | 2/5 | 3 runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 71% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 93% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Sol
•
[codex](https://chatgpt.com/codex/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 19.3% Avg completion rate 74.3% Avg latency 8.6 h Avg cost $235.8

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 82% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 51% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 97% | 2/5 | 3 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 100% | 5/5 | N/A |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 73% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 100% | 5/5 | N/A |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 81% | 0/5 | All runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 58% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 90% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 71% | 0/5 | All runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 96% | 2/5 | 3 runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 58% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 80% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 95% | 3/5 | 2 runs failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 51% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 95% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 5% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 100% | 5/5 | N/A |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 83% | 2/5 | 3 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 32% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 71% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 78% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 99% | 4/5 | 1 run failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 70% | 0/5 | 4 runs failed tests, 1 run missed required test results |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 94% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 27% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 59% | 1/5 | 2 runs failed the build, 2 runs failed tests |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 94% | 0/5 | All runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 33% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 93% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 5
•
[claude-code](https://claude.com/product/claude-code)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 16.7% Avg completion rate 77.8% Avg latency 27.0 h Avg cost $861.4

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 98% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 81% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 93% | 1/5 | 4 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 99% | 4/5 | 1 run failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 80% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 100% | 5/5 | N/A |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 88% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 45% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 93% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 75% | 0/5 | All runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 92% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 58% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 97% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 100% | 5/5 | N/A |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 63% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 94% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 89% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 100% | 5/5 | N/A |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 87% | 2/5 | 3 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 66% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 47% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 84% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 43% | 1/5 | 4 runs failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 81% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 88% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 11% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 20% | 1/5 | 4 runs failed the build |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 94% | 1/5 | 4 runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 68% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 90% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.8 Max
•
[qwen-coder](https://coder.qwen.ai/)

Open weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 14.0% Avg completion rate 74.3% Avg latency 47.2 h Avg cost $260.2

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 41% | 0/5 | 4 runs failed tests, 1 run failed the build |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 47% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 95% | 1/5 | 4 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 80% | 2/5 | 3 runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 88% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 60% | 3/5 | 2 runs missed required test results |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 78% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 40% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 92% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 71% | 0/5 | All runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 91% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 65% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 91% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 91% | 3/5 | 2 runs failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 71% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 93% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 87% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 100% | 5/5 | N/A |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 61% | 3/5 | 2 runs missed required test results |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 58% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 83% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 62% | 0/5 | 4 runs failed tests, 1 run missed required test results |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 98% | 3/5 | 2 runs failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 76% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 89% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 22% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 79% | 1/5 | 3 runs failed tests, 1 run failed the build |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 94% | 0/5 | All runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 33% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 80% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/moonshot.png) Kimi K3
•
[kimi-code](https://www.kimi.com/code/en)

Open weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 12.0% Avg completion rate 72.8% Avg latency 66.2 h Avg cost $418.3

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 59% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 49% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 97% | 2/5 | 3 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 64% | 0/5 | All runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 82% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 60% | 3/5 | 2 runs missed required test results |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 78% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 48% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 91% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 56% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 89% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 63% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 94% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 82% | 0/5 | 4 runs failed tests, 1 run failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 71% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 93% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 76% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 100% | 5/5 | N/A |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 84% | 2/5 | 3 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 69% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 83% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 78% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 80% | 4/5 | 1 run failed the build |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 60% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 90% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 11% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 39% | 1/5 | 3 runs failed the build, 1 run failed tests |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 93% | 1/5 | 4 runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 44% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 87% | 0/5 | All runs failed tests |

### :gemini: Gemini 3.8 Flash
•
[antigravity-sdk](https://antigravity.google/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 8.0% Avg completion rate 47.4% Avg latency 12.1 h Avg cost $34.5

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 0% | 0/5 | 4 runs failed the build, 1 run failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 26% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 62% | 1/5 | 4 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 70% | 2/5 | 3 runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 47% | 1/5 | 3 runs failed tests, 1 run failed the build |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 53% | 2/5 | 3 runs failed tests |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 35% | 0/5 | All runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 12% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 25% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 12% | 0/5 | 4 runs failed validation, 1 run failed the build |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 89% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 42% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 48% | 0/5 | 4 runs failed validation, 1 run failed the build |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 89% | 1/5 | 3 runs failed validation, 1 run failed tests |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 66% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 76% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 5% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 40% | 2/5 | 1 run failed the build, 1 run failed tests, 1 run failed validation |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 19% | 0/5 | 3 runs failed tests, 2 runs failed validation |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 20% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 79% | 0/5 | All runs failed validation |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 63% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 62% | 2/5 | 2 runs failed tests, 1 run failed validation |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 72% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 66% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 24% | 1/5 | 4 runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 61% | 0/5 | 3 runs failed tests, 1 run failed the build, 1 run failed validation |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 51% | 0/5 | All runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 23% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 68% | 0/5 | 4 runs failed tests, 1 run failed the build |

### :gemini: Gemini 3.7 Flash
•
[antigravity-sdk](https://antigravity.google/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 7.3% Avg completion rate 50.1% Avg latency 9.9 h Avg cost $26.0

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 25% | 0/5 | 3 runs failed tests, 2 runs failed the build |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 3% | 0/5 | 4 runs failed tests, 1 run failed the build |
| New accessibility support across Droidcon (conference app) | New feature | 89% | 0/5 | All runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 97% | 4/5 | 1 run failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 66% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 48% | 2/5 | 3 runs failed tests |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 55% | 0/5 | All runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 28% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 10% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 18% | 0/5 | 3 runs failed the build, 2 runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 89% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 30% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 85% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 78% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 57% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 46% | 0/5 | 4 runs failed tests, 1 run failed the build |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 1% | 0/5 | 3 runs failed validation, 1 run failed tests, 1 run failed the build |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 60% | 3/5 | 1 run failed the build, 1 run failed tests |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 19% | 0/5 | 2 runs failed tests, 1 run failed the build, 1 run missed required test results, 1 run failed validation |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 32% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 43% | 0/5 | 2 runs failed the build, 2 runs failed validation, 1 run failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 63% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 95% | 2/5 | 3 runs failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 35% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 80% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 71% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 2% | 0/5 | 4 runs failed the build, 1 run failed validation |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 75% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in WordPress: people invite screen | Migration | 38% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 51% | 0/5 | 3 runs failed tests, 1 run failed the build, 1 run missed required test results |

### ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 5
•
[claude-code](https://claude.com/product/claude-code)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 6.7% Avg completion rate 59.8% Avg latency 14.7 h Avg cost $283.7

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 80% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 59% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 88% | 1/5 | 4 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 92% | 3/5 | 2 runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 67% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 57% | 2/5 | 2 runs failed tests, 1 run failed the build |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 72% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 50% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 69% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 66% | 0/5 | All runs failed validation |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 86% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 24% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 68% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 95% | 1/5 | 4 runs failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 50% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 49% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 16% | 0/5 | 4 runs failed validation, 1 run failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 60% | 3/5 | 1 run failed tests, 1 run failed validation |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 38% | 0/5 | 3 runs failed validation, 2 runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 11% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 63% | 0/5 | 4 runs failed tests, 1 run failed validation |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 61% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 53% | 0/5 | 3 runs failed tests, 2 runs failed validation |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 42% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 87% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 15% | 0/5 | 3 runs failed the build, 2 runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 81% | 0/5 | 4 runs failed tests, 1 run failed validation |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 75% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in WordPress: people invite screen | Migration | 18% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 88% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Terra
•
[codex](https://chatgpt.com/codex/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 4.7% Avg completion rate 53.4% Avg latency 5.1 h Avg cost $53.2

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 70% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 17% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 97% | 2/5 | 3 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 81% | 2/5 | 3 runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 61% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 33% | 1/5 | 2 runs failed the build, 2 runs failed tests |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 55% | 0/5 | All runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 21% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 48% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 24% | 0/5 | 3 runs failed validation, 2 runs failed the build |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 90% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 16% | 0/5 | 4 runs failed validation, 1 run failed tests |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 65% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 59% | 0/5 | All runs failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 55% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 59% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 24% | 0/5 | 3 runs failed validation, 2 runs failed the build |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 20% | 1/5 | 3 runs failed tests, 1 run failed the build |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 74% | 0/5 | All runs failed tests |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 21% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 65% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 48% | 0/5 | 4 runs failed tests, 1 run failed the build |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 58% | 1/5 | 2 runs failed the build, 2 runs failed tests |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 55% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 76% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 15% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 78% | 0/5 | 4 runs failed tests, 1 run failed validation |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 94% | 0/5 | All runs failed tests |
| XML views to Compose migration in WordPress: people invite screen | Migration | 32% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 79% | 0/5 | All runs failed tests |

### ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Luna
•
[codex](https://chatgpt.com/codex/)

Closed weights model <button class="devsite-dialog-close button button-white"> close </button> Pass rate 3.3% Avg completion rate 55.2% Avg latency 7.6 h Avg cost $13.5

#### Per task results

All categories App conversion App creation Migration New feature **Number of tasks:** 30 2 10 13 5 /30

| Task | Category | Avg completion rate | Runs passed | Failure reason(s) |
|---|---|---|---|---|
| Convert Flutter to Android: Habo app (habit tracker) | App conversion | 50% | 0/5 | All runs failed tests |
| Convert React Native to Android: BlueWallet app (Bitcoin wallet) | App conversion | 63% | 0/5 | All runs failed tests |
| New accessibility support across Droidcon (conference app) | New feature | 93% | 1/5 | 4 runs failed tests |
| New Media3 and ExoPlayer video playback in Now in Android (news app) | New feature | 66% | 0/5 | All runs failed tests |
| New picture-in-picture video mode in Now in Android (news app) | New feature | 70% | 0/5 | All runs failed tests |
| New CameraX profile picture capture in Now in Android (news app) | New feature | 42% | 1/5 | 3 runs failed tests, 1 run failed the build |
| New user account submodule in Food Vibes (full app creation - food delivery) | App creation | 55% | 0/5 | All runs failed validation |
| New authentication flow with SMS verification in Food Vibes (full app creation - food delivery) | App creation | 27% | 0/5 | All runs failed validation |
| New bottom navigation and Browse search screen in Food Vibes (full app creation - food delivery) | App creation | 76% | 0/5 | All runs failed validation |
| New design system and reusable UI component library in Food Vibes (full app creation - food delivery) | App creation | 12% | 0/5 | 3 runs failed validation, 2 runs failed the build |
| New All Filters screen in Food Vibes (full app creation - food delivery) | App creation | 85% | 0/5 | All runs failed validation |
| New map integration and location features in Food Vibes (full app creation - food delivery) | App creation | 14% | 0/5 | All runs failed validation |
| New real-time order tracking in Food Vibes (full app creation - food delivery) | App creation | 72% | 0/5 | All runs failed validation |
| New promotions submodule and active offers screen in Food Vibes (full app creation - food delivery) | App creation | 61% | 0/5 | All runs failed validation |
| New restaurant listing feed in Food Vibes (full app creation - food delivery) | App creation | 68% | 0/5 | All runs failed validation |
| New ViewModel layer in Fossify File Manager | New feature | 80% | 0/5 | All runs failed tests |
| Nav 2 to Nav 3 library migration in Bitwarden (password manager) | Migration | 7% | 0/5 | All runs failed tests |
| Dual-pane adaptive layout migration in Bitwarden (password manager): settings screens | Migration | 40% | 2/5 | 3 runs failed tests |
| Hilt to Koin dependency injection migration in Bitwarden (password manager) | Migration | 47% | 0/5 | 4 runs failed tests, 1 run missed required test results |
| XML views to Compose migration in Fossify File Manager: main tabs and settings | Migration | 39% | 0/5 | All runs failed tests |
| Hilt to Koin dependency injection migration in Now in Android (news app) | Migration | 62% | 0/5 | All runs failed tests |
| Kotlin Multiplatform migration in Now in Android (news app): datastore and database | Migration | 51% | 0/5 | All runs failed tests |
| Retrofit to Ktor migration in Pocket Casts (podcast player) | Migration | 78% | 1/5 | 3 runs failed tests, 1 run missed required test results |
| XML views to Compose migration in Signal (messaging app): custom chat colour creator | Migration | 79% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): profile creation | Migration | 79% | 0/5 | All runs failed tests |
| XML views to Compose migration in Signal (messaging app): phone number entry | Migration | 35% | 0/5 | All runs failed tests |
| Java to Kotlin migration in Signal (messaging app): Glide image loading module | Migration | 0% | 0/5 | All runs failed the build |
| XML views to Compose migration in Signal (messaging app): edit profile screens | Migration | 71% | 0/5 | 4 runs failed tests, 1 run failed the build |
| XML views to Compose migration in WordPress: people invite screen | Migration | 35% | 0/5 | All runs failed tests |
| New book searching app using the OpenLibrary API | App creation | 86% | 0/5 | All runs failed tests |

### 1.0 task results

All models Open weights models Closed weights models

| Model | Score (%) info Average percentage of 100 tasks successfully resolved across all runs for each model | arrow_range Cl range (%) info Expected performance range, reflecting the results' statistical reliability (p-value \< 0.05) | Avg latency (h) info Average time taken to solve 100 tasks across all runs | Avg cost ($) info Average cost per full benchmark run |
|---|---|---|---|---|
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 5 | **91.8** | 87.4 --- 95.7 | 13.2 | $175.4 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Fable 5 | **90.9** | 86.2 --- 95.4 | 8.7 | $144.3 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Sol | **90.8** | 85.6 --- 95.6 | 14.2 | $150.0 |
| ![](https://developer.android.com/static/images/bench/icons/moonshot.png) Kimi K3 | **90.2** | 85.0 --- 94.6 | 29.6 | $112.9 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Luna | **87.6** | 81.8 --- 92.3 | 10.6 | $7.2 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.8 Max | **87.0** | 82.2 --- 91.6 | 41.2 | $196.7 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Terra | **86.8** | 81.7 --- 91.2 | 7.6 | $48.0 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.5 | **80.2** | 73.0 --- 86.6 | 11.4 | $138.3 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 5 | **76.2** | 68.8 --- 82.5 | 12.3 | $99.9 |
| :gemini: Gemini 3.6 Flash | **75.6** | 67.5 --- 82.1 | 10.2 | $135.5 |
| :gemini: Gemini 3.1 Pro Preview | **74.3** | 66.8 --- 81.5 | 10.5 | $86.6 |
| ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.4 | **74.1** | 66.6 --- 81.2 | 8.4 | $83.4 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 4.8 | **72.4** | 65.1 --- 79.2 | 6.7 | $88.0 |
| ![](https://developer.android.com/static/images/bench/icons/z-ai.png) GLM 5.2 | **72.2** | 65.3 --- 79.1 | 38.9 | $117.0 |
| :gemini: Gemini 3.5 Flash | **71.1** | 63.8 --- 78.5 | 28.3 | $165.6 |
| ![](https://developer.android.com/static/images/bench/icons/moonshot.png) Kimi K2.7 Code | **70.4** | 63.4 --- 77.1 | 31.8 | $48.1 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 4.7 | **68.7** | 60.9 --- 76.4 | 7.0 | $96.5 |
| ![](https://developer.android.com/static/images/bench/icons/moonshot.png) Kimi K2.6 | **67.6** | 59.8 --- 74.8 | 57.2 | $49.4 |
| ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Sonnet 4.6 | **67.0** | 58.5 --- 75.1 | 16.9 | $127.6 |
| ![](https://developer.android.com/static/images/bench/icons/minimax.png) Minimax M3 | **63.6** | 56.1 --- 70.7 | 26.0 | $41.7 |
| ![](https://developer.android.com/static/images/bench/icons/z-ai.png) GLM 5.1 | **63.2** | 55.3 --- 70.2 | 17.6 | $53.5 |
| :gemini: Gemini 3 Flash Preview | **62.5** | 54.7 --- 69.7 | 13.1 | $30.1 |
| ![](https://developer.android.com/static/images/bench/icons/xiaomi.png) Mimo V2.5 Pro | **60.8** | 53.2 --- 68.6 | 13.6 | $9.2 |
| ![](https://developer.android.com/static/images/bench/icons/deepseek.png) Deepseek V4 Pro | **59.5** | 51.4 --- 67.9 | 9.0 | $3.7 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.7 Plus | **57.7** | 50.2 --- 65.6 | 18.5 | $18.6 |
| ![](https://developer.android.com/static/images/bench/icons/deepseek.png) Deepseek V4 Flash | **54.7** | 46.9 --- 62.8 | 8.9 | $1.5 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.7 Max | **54.2** | 46.9 --- 62.1 | 14.2 | $58.3 |
| :gemini: Gemini 3.5 Flash-Lite | **50.6** | 42.3 --- 58.4 | 5.4 | $34.1 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.6 27b | **45.1** | 37.6 --- 52.8 | 25.8 | $97.3 |
| ![](https://developer.android.com/static/images/bench/icons/minimax.png) MiniMax M2.7 | **41.6** | 34.7 --- 49.4 | 18.2 | $14.9 |
| ![](https://developer.android.com/static/images/bench/icons/google.png) Gemma 4 31b IT | **37.1** | 29.9 --- 44.5 | 36.3 | $10.4 |
| ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.6 35b A3b | **37.0** | 29.1 --- 44.3 | 16.3 | $17.8 |

**Latest results as of
September 17th.**   
View [**archived leaderboards**](https://developer.android.com/bench/archive) and check back periodically for updates.

### [Latest Updates](http://developer.android.com/bench/changelog)

Track the latest AI model benchmarks, newly introduced agent architectures, and continuous performance evaluations on the platform. Stay updated with our routine methodology updates and release logs. [View all updates](http://developer.android.com/bench/changelog)
- [New updates • Sep 17th ![](https://developer.android.com/static/images/bench/icons/news.png) Launched long-horizon tasks](https://developer.android.com/bench/methodology/2#benchmark-design)
- [New updates • Sep 17th ![](https://developer.android.com/static/images/bench/icons/robot.png) Now benchmarking models using specialized agents](https://developer.android.com/bench/methodology/2#expanding_beyond_mini-swe-agent)
- New agent results • Sep 17th   
  **antigravity-sdk results now available** :gemini: Gemini 3.6 Flash, Gemini 3.7 Flash
- New agent results • Sep 17th   
  **pi results now available** ![](https://developer.android.com/static/images/bench/icons/google.png) Gemini 3.6 Flash
- New agent results • Sep 17th   
  **codex results now available** ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Luna, GPT 5.6 Sol

<!-- -->

- New models • Aug 11th ![](https://developer.android.com/static/images/bench/icons/anthropic.png) Claude Opus 5
- New models • Aug 11th ![](https://developer.android.com/static/images/bench/icons/openai.png) GPT 5.6 Sol, GPT 5.6 Luna, GPT 5.6 Terra
- New models • Aug 11th ![](https://developer.android.com/static/images/bench/icons/kimi.png) Kimi K3
- New models • Aug 11th ![](https://developer.android.com/static/images/bench/icons/qwen.png) Qwen3.8 Max
- New models • Aug 11th :gemini: Gemini 3.6 Flash, Gemini 3.5 Flash Lite
- Archived models • Aug 11th ![](https://developer.android.com/static/images/bench/icons/google.png) Gemma 4 26B A4B IT

<!-- -->

- [New updates • Jul 13th ![](https://developer.android.com/static/images/bench/icons/github.png) Share results on the community repository](https://github.com/android-bench/community-results)
- [New updates • Jul 13th ![](https://developer.android.com/static/images/bench/icons/github.png) Contribute new tasks to our community dataset on GitHub](https://github.com/android-bench/community-dataset)
![](http://developer.android.com/static/images/picto-icons/badge.svg)

## Learn more about Android Bench

### [Our methodology](http://developer.android.com/bench/methodology)

Learn more about how we created a set of common Android developer tasks. [Read more](http://developer.android.com/bench/methodology)

### [Android best practices](http://developer.android.com/develop)

Many of the tasks are based on how we define high quality Android development, which is detailed in our developer documentation. [Read more](http://developer.android.com/develop)

### [1.0 dataset on Harbor Hub](https://hub.harborframework.com/datasets/android-bench/android-bench/latest)

See the full dataset for our 1.0 tasks on Harbor Hub. [View more](https://hub.harborframework.com/datasets/android-bench/android-bench/latest)