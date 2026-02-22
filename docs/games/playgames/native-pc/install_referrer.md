---
title: https://developer.android.com/games/playgames/native-pc/install_referrer
url: https://developer.android.com/games/playgames/native-pc/install_referrer
source: md.txt
---

Make informed marketing decisions by identifying your most valuable user
acquisition channels for your game. Use the Google Play Install Referrer API for
a reliable way to track your apps' referral information.

By tracking referral data, you can understand which traffic sources send the
most users to download your app from the Google Play store. These insights can
help you make the most of your advertising spend and maximize ROI.

## Prerequisites

- Complete the [SDK setup](https://developer.android.com/games/playgames/native-pc/setup).

## **Step 1**: Link to your store listing page

Start by linking your users to your application's Google Play store page. In the
URL include query params for:

- `id`: The Play package name of your game
- `referrer`: A string representing the referral source. This can be queried once your application is installed and running.

    https://play.google.com/store/apps/details?id=com.example.package&referrer=example_referrer_source

## **Step 2**: Query the referrer details on app startup

> [!NOTE]
> **Note:** The referrer will be available for 90 days after the installation of your game.

Once the user has completed the installation of game and launched it your app
can determine the traffic source that led to the installation using the Install
Referrer APIs.

Query the referrer details using
[`InstallReferrerClient::GetInstallReferrer`](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/install-referrer/install-referrer-client#getinstallreferrer). In the
response the same string passed into the `referrer` query param of your store
listing page can be retrieved. The referrer details can then be attached
analytics collected such as an app installed event.

    auto promise = std::make_shared<std::promise<GetInstallReferrerResult>>();
    install_referrer_client.GetInstallReferrer(params, [promise](GetInstallReferrerResult result) {
       promise->set_value(std::move(result));
    });

    auto get_install_referrer_result = promise->get_future().get();
    if (get_install_referrer_result.ok()) {
       auto install_referrer = get_install_referrer_result.value().install_referrer;
       // Attribute your game's installation to an acquisition channel by including
       // the install referrer. Typically this would be done by logging an app
       // install event with an analytics library of your choice that includes the
       // `install_referrer`.
    }