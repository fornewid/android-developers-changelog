---
title: https://developer.android.com/games/pgs/publishing/publishing-start
url: https://developer.android.com/games/pgs/publishing/publishing-start
source: md.txt
---

To start making calls to the Publishing API, you must link to an API
project directly from the
[Google Play Console](https://play.google.com/apps/publish/)
and enable the Publishing API for that project. Once your API project is
set up, it can be used to manage other game projects you own.

The Publishing API can only be configured by the owner of your
[Google Play Developer account](https://developer.android.com/distribute/googleplay/developer-console#account-details).
The following instructions explain how to:

- Set up a new or existing API project
- Manage OAuth clients
- Use a service account to access the Publishing API

## Set up your API Project

Before you can access the Publishing API, you must link Google Play Console
to an API project. In most cases, you are encouraged to create a new API
project, though current
[Google Play Developer Publishing API](https://developer.android.com/distribute/googleplay/developer-console.html#account-details)
users can link to an existing API project. Keep in mind that each API project
can only be linked to a single Google Play Console account.

### Create a new API project

1. Go to the [API Access](https://play.google.com/apps/publish/#ApiAccessPlace) page on the Google Play Console.
2. Accept the Terms of Service.
3. Click **Create new project**. An API project is automatically generated and linked to your Google Play Console.
4. Turn the Game Services Publishing API option to **ON**.

Your API project is now configured to access the Publishing API.

### Use an existing API project

If you are already a user of the
[Google Play Developer API](https://developers.google.com/android-publisher),
you can set up your existing API project by following these steps. If the API
project you want to set up is not listed, verify that your Google Play Console
account is designated as an Owner, and the
[Google Play Developer API](https://developers.google.com/android-publisher/#publishing)
is enabled.

1. Go to the [API Access](https://play.google.com/apps/publish/#ApiAccessPlace) page on the Google Play Console.
2. Accept the API Terms of Service.
3. Choose the project you'd like to set up.
4. Click **Link**. Your Google Play Console is now linked to the API project.
5. Turn the Game Services Publishing API option to **ON**.

Your API project is now configured to access the Publishing API.

## Set Up API Access Clients

You access the Publishing API through an OAuth client or a service account.

### Use OAuth clients

You can allow users to perform actions via the Publishing API under their
own credentials using an
[OAuth](https://developers.google.com/accounts/docs/OAuth2) client.
| **Note:** Your Oauth client must share the same project as your [service account](https://developer.android.com/games/pgs/publishing/publishing-start#using_a_service_account).

A user's actions are limited to those permitted via the
[User Accounts \& Rights](https://play.google.com/apps/publish/#AdminPlace)
page on the Google Play Console.

1. Go to the [API Access](https://play.google.com/apps/publish/#ApiAccessPlace) page on the Google Play Console.
2. Under **OAuth Clients** , click **Create OAuth Client**.
3. Configure your product's branding information, and click **Continue**.
4. Click **Create Client ID**.

The details of your new OAuth client are displayed in a list on this page.

### Use a service account

You can also create a
[service account](https://developers.google.com/accounts/docs/OAuth2ServiceAccount)
to access the Publishing API from a build server without providing your personal
user credentials:

1. Go to the [API Access](https://play.google.com/apps/publish/#ApiAccessPlace) page on the Google Play Console.
2. Under **Service Accounts** , click **Create Service Account**.
3. Follow the instructions on the page to create your service account.
4. Once you've created the service account on the Google Developers Console, click **Done** . The [API Access](https://play.google.com/apps/publish/#ApiAccessPlace) page automatically refreshes, and your service account will be listed.
5. Click **Grant Access** to provide the service account the necessary rights to perform actions.

For more information, see
[Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/accounts/docs/OAuth2ServiceAccount).

## Accessing the Google Play Games Services Publishing API

You can access the Publishing API directly via HTTP. For more information, see
[Publishing API reference](https://developers.google.com/games/services/publishing/api)
and the
[sample app](https://github.com/playgameservices/management-tools).