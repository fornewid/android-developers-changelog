---
title: https://developer.android.com/build/jcenter-migration
url: https://developer.android.com/build/jcenter-migration
source: md.txt
---

JFrog, the company that maintains the JCenter artifact repository used by
many Android projects, made JCenter a read-only repository on March 31, 2021.
According to [the announcement](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/),
JCenter will allow downloads of existing artifacts indefinitely.

Developers who publish artifacts on JCenter should migrate their
packages to a new host, such as
[Maven Central](https://maven.apache.org/repository/index.html).

Developers who use dependencies from JCenter must find the new location of
updated versions of those dependencies.

> [!WARNING]
> **Warning:** Don't include the `jcenter()` repository in your build config to avoid getting outdated dependencies.