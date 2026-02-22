---
title: https://developer.android.com/topic/performance/power/network/action-server-traffic
url: https://developer.android.com/topic/performance/power/network/action-server-traffic
source: md.txt
---

# Optimize server-initiated network use

Network traffic sent by server programs to your app can be challenging to optimize. A solution to this problem is for your app to periodically poll the server to check for updates. This approach can waste network connection and power when your app starts up a device's radio, only to receive an answer that no new data is available. A far more efficient approach would be for the server to notify your app when it has new data, but figuring out how to send a notification from your server to potentially thousands of devices was previously no easy feat.

The Firebase Cloud Messaging (FCM) service solves this communication problem by allowing your servers to send notifications to instances of your app wherever they are installed, enabling greater network efficiency and lowering power usage.

This lesson teaches you how to apply the FCM service to reduce network use for server-initiated actions and reduce battery consumption.

## Send server updates with FCM

Firebase Cloud Messaging (FCM) is a lightweight mechanism used to transmit brief messages from an app server to your app. Using FCM, your app server uses a message-passing mechanism to notify your app that there is new data available. This approach eliminates network traffic that your app would perform, by not contacting a backend server for new data when no data is available.

An example use of FCM is an app that lists speaker sessions at a conference. When sessions are updated on your server, the server sends a brief message to your app telling it updates are available. Your app can then call the server to update the sessions on the device only when the server has new data.

FCM is more efficient than having your app poll for changes on the server. The FCM service eliminates unnecessary connections where polling would return no updates, and it avoids running periodic network requests that could cause a device's radio to power up. Since FCM can be used by many apps, using it in your app reduces the total number of network connections needed on a device and allows the device radio to sleep more often.
| **Note:** When using FCM, your app can pass messages in normal or high priority. Your server should typically use normal priority to deliver messages. Using this priority level prevents devices from being woken up if they are inactive and in a low-power Doze state. Use high priority messages only if absolutely required.