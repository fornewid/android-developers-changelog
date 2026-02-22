---
title: https://developer.android.com/build/releases/prompts/release_note_instructions
url: https://developer.android.com/build/releases/prompts/release_note_instructions
source: md.txt
---

# Android Studio Release Notes

This document contains instructions about creating the release notes for Android Studio.

## Objective

To create detailed release notes for commits from a GitHub repo.

## Instructions

Follow these instructions sequentially and completely.

## Step 1: Clone or update the repo

Check for a studio-main folder in this project. If one doesn't exist, clone the studio-main repository using the following command:

git clone -b studio-main sso://googleplex-android/platform/tools/base studio-main

If the directory already exists, refresh the directory by pulling the contents of the repo from GitHub.

Let me know the status of studio-main before proceeding.

## Step 2: Study the repo

Study the contents of the repo.

## Step 3: Get the commits

Get all commits submitted to the studio-main repository during the timeframe I provided to you. Let me know the count before proceeding. Always use wc -l for counting.

1. Identify target commits: From the git log, extract the full commit block for every commit that contains the exact string "Relnote:" whereis the product name I provided. If I don't provide a product name, just search for "Relnote".

   A "commit block" includes the commit hash, author, date, the full commit message, and the code diff.
2. Use the correct tool: To filter commits by date range and product name, use the following command:

   git log --after="" --before="" --grep="Relnote:"

   whereandare the date range I gave you, andis the product name I gave you.

   If a product name isn't provided, just use the following command:

   git log --after="" --before="" --grep="Relnote"
3. Confirm the count: Show me the total count, the hashes, and titles of all the commits you identified. I will give you a confirmation to proceed.

## Step 4: Generate detailed release notes

1. Analyze each commit: For each of the commits you identified in the previous step, perform a detailed analysis, which includes:

   - Reading the full commit message.
   - Examining the code diff (git show) to understand the change.
   - Following any linked bugs (for example, Bug: 12345678) to gather more context.

   Confirm with me before proceeding.
2. Analyze any related documents in the docs folder for information related to the commits. Use this information to create a content-rich release note.

   Let me know which commits have related information in the docs folder before proceeding.
3. Get any bugs that are referenced in the commits. Use the information in the bug to help create the release note for the commit.

4. Write the release note: For each commit, write a release note that includes:

   - Commit reference: Precede each release note with a Markdown comment containing the source commit hash, like this: .

   - A clear title: A concise, sentence-case summary of the change.

   - A detailed explanation: A paragraph explaining what the change is about.

   - Key points about the change in the following order:

     a. Why: What changed and why it changed b. Impact: The impact on app developers c. Migration: The migration path (if any)
   - "Before" and "after" code examples: If the commit involves a user-facing code change (for example, DSL changes in .gradle files or API modifications), provide clear, concise code snippets demonstrating the change.

   Follow the release note style at https://developer.android.com/studio/releases.

## Step 5: Write the release notes to a Markdown file

1. Create a Markdown file named release-notes-YYYY-MM-DDTHH:MM.md in the root of the project, where--in ISO 8601 format--YYYY-MM-DD (year-month-day) is the current date, T is a separator, and HH:MM (hours:minutes in 24-hour clock time) is the current time.
2. Write an introduction that explains the purpose of the release notes.
3. Write a summary of the release notes.
4. Write the complete, formatted release notes.

## Step 6: Create a commit

Create a Fig commit for the release notes file. Don't include a bug ID.

## Step 7: Create a changelist

Create a CL of the commit.