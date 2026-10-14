---
title: https://developer.android.com/blog/posts/googlebook-linux-terminal-preview-vm
url: https://developer.android.com/blog/posts/googlebook-linux-terminal-preview-vm
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Introducing the Googlebook Linux Terminal Preview: A VM-Backed Environment for AI and Development

2 min read ![](https://developer.android.com/static/blog/assets/1006_ABL_141_Strapi_1_540d64279e_Z1veewf.webp) 12 Oct 2026 [![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp)](https://developer.android.com/blog/authors/cyrus-stoller) [Cyrus Stoller](https://developer.android.com/blog/authors/cyrus-stoller) Group Product Manager, Laptops \& Tablets Today, getting the most out of AI workflows requires access to a terminal with a command line, even if someone doesn't identify as a programmer or software developer. With Googlebook, we're excited to help users express themselves and gain access to these tools. Googlebooks come with pre-installed tooling to get you going. In this post, we'll explore the capabilities of our new Linux terminal--- now available in preview--- share our future roadmap, and invite you to help us shape this ecosystem together.

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
- [#Googlebook](https://developer.android.com/blog/topics/googlebook)
Written by:

-

  ## [Cyrus Stoller](https://developer.android.com/blog/authors/cyrus-stoller)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/cyrus-stoller) ![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp) ![View Cyrus Stoller's profile](https://developer.android.com/static/blog/assets/unnamed_26_f996d1f7cf_2bofD0.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +1 ↩
- [![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)](https://developer.android.com/blog/authors/jason-buchel) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Blog_0140_strapi_8d85f71a6e_ZvGJv2.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bringing our latest frontier model to Android Developers](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli)

  [arrow_forward](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli) As agentic development accelerates, Android engineering is reaching an exciting new frontier: moving from assistive code completion to agents executing end-to-end under your direction. You have total choice and flexibility in the models and agents you use.
  [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_ZnD5Di.webp)](https://developer.android.com/blog/authors/paul-feng) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Developer_Strapi_Banner_2000x1000_c21932c96a_1wEPmN.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [New ways to drive smarter discovery, deeper engagement, and business growth on Google Play](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth) Today, we shared how we're taking our "more than a store" vision into its next chapter. From You tab, now the personal home base for over 250M monthly active users, to our unified gaming platform connecting over 700M gamer profiles, Google Play is meeting users wherever they are.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 3 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)