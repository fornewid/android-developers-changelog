---
title: https://developer.android.com/blog/posts/googlebook-linux-terminal-preview-vm
url: https://developer.android.com/blog/posts/googlebook-linux-terminal-preview-vm
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Introducing the Googlebook Linux Terminal Preview: A VM-Backed Environment for AI and Development

2 min read ![](https://developer.android.com/static/blog/assets/1006_ABL_141_Strapi_1_540d64279e_Z1veewf.webp) 12 Oct 2026 [![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp)](https://developer.android.com/blog/authors/cyrus-stoller.md.txt) [Cyrus Stoller](https://developer.android.com/blog/authors/cyrus-stoller.md.txt) Group Product Manager, Laptops \& Tablets Today, getting the most out of AI workflows requires access to a terminal with a command line, even if someone doesn't identify as a programmer or software developer. With Googlebook, we're excited to help users express themselves and gain access to these tools. Googlebooks come with pre-installed tooling to get you going. In this post, we'll explore the capabilities of our new Linux terminal--- now available in preview--- share our future roadmap, and invite you to help us shape this ecosystem together.

## Entry point for agentic development

AI agents use the terminal to install packages, write files, automate tasks, and create apps based on prompts written in plain language. For Googlebook to be the perfect companion for building and working at the frontier of agentic AI, the terminal needed to be easily accessible.  

We understand AI comes with risks. Googlebook OS has been architected with defense-in-depth as a core principle. All terminal commands run entirely inside the Linux VM, creating an isolated sandbox. This design allows users to grant \`sudo\` (administrator) privileges to AI tools like Antigravity and other agentic AI platforms, that make heavy use of command-line tools, while limiting opportunities for system corruption or unauthorized access to your private files. The VM boundary helps protect the host OS and unmounted files; each directory made available to the Linux VM is only mounted after the user's explicit permission. Best of all, a one-click VM reset makes experimentation stress free because users can easily retain their files on the host file system when they reset the VM. You can even see your Linux files inside the Googlebook Files app, where a user can access local folders -- including photos and files synced effortlessly from their Android phone. Using a quick Python script or AI agent, you can batch-process your files in seconds.

## Linux VM benefits

The terminal provides users with the freedom to create and use the software that they choose. We're excited to see users build tools that are hyper-specific to their needs as well as prototype apps for broader use. With a Debian Linux environment, users benefit from the mature ecosystem familiar to Linux developers. This means that they have access to the latest CLI tools and common developer workflows like \`apt\`, \`git\`, \`ssh\`, and common compilers and runtimes.  

Out of the box, our preview of the terminal on Googlebook has been optimized for rapid prototyping, web development, scripting, and agentic workflows via CLI. There is automatic localhost port forwarding to the host browser, and support for modern runtimes (e.g., Node.js, Python, Ruby, Go, Rust). Users can adjust the amount of memory made available to the VM to best suit their workloads. Our own engineers have been using Googlebooks to build a Linux kernel and use the terminal for platform engineering.

## Looking ahead

We can't wait for the terminal and Linux VM to continue getting more capable over time, including Linux GUI app support with integration directly into the app launcher. Here are some key areas on the roadmap:

- We are working hard to get you building not only on Googlebook but also for your other devices. In addition to the existing network passthrough and wireless ADB, USB passthrough and support for ADB over USB are coming, enabling local device debugging and more from our Linux VM and Antigravity. [Learn more about Antigravity on Googlebook](https://support.google.com/googlebook/answer/18668704).
- Our testers have been eager to run more complex tasks. To make this more seamless, we are adding dynamic memory and storage scaling for the VM.
- We will be adding GPU/NPU hardware acceleration for heavier local workloads, allowing users to leverage the performance and power efficiency of dedicated hardware.
- VM persistence and separation from the terminal window will better support long-running processes, when you want to take on more demanding agentic workloads.

<br />

We're looking forward to seeing your creations and will be sharing more soon. Questions? You can reach us [here for direct support](https://support.google.com/googlebook/community). We've also really enjoyed hearing your early thoughts and feedback in [r/googlebook](https://www.reddit.com/r/Googlebook/).
- [#Googlebook](https://developer.android.com/blog/topics/googlebook.md.txt)
Written by:

-

  ## [Cyrus Stoller](https://developer.android.com/blog/authors/cyrus-stoller.md.txt)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/cyrus-stoller) ![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp) ![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston.md.txt) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development.md.txt) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston.md.txt) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook.md.txt)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
  - +1 ↩
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)