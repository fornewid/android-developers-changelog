---
title: https://developer.android.com/games/playgames/native-pc/reference
url: https://developer.android.com/games/playgames/native-pc/reference
source: md.txt
---

# Play Games PC SDK

# Play Games PC SDK

Play Games PC SDK API Reference

## [google::play](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play)

|                                                                         ### Classes                                                                         ||
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| [google::play::Result](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/result) | Represents the outcome of an operation. |

## [google::play::billing](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/billing)

|                                                                                           ### Classes                                                                                           ||
|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [google::play::billing::BillingClient](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/billing/billing-client) | Entrypoint for the Google Play Billing API. |

|                                                                                                                                        ### Structs                                                                                                                                         ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [google::play::billing::AcknowledgePurchaseParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/acknowledge-purchase-params)                                                 | Params for acknowledging a purchase.                         |
| [google::play::billing::AcknowledgePurchaseResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/acknowledge-purchase-result-value)                                      | Result value for acknowledging a purchase.                   |
| [google::play::billing::ConsumePurchaseParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/consume-purchase-params)                                                         | Params for consuming a purchase.                             |
| [google::play::billing::ConsumePurchaseResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/consume-purchase-result-value)                                              | Result value for consuming a purchase.                       |
| [google::play::billing::CreateBillingProgramReportingDetailsParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/create-billing-program-reporting-details-params)            | Params for creating billing program reporting details.       |
| [google::play::billing::CreateBillingProgramReportingDetailsResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/create-billing-program-reporting-details-result-value) | Result value for creating billing program reporting details. |
| [google::play::billing::IsBillingProgramAvailableParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/is-billing-program-available-params)                                   | Params for checking if a billing program is available.       |
| [google::play::billing::IsBillingProgramAvailableResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/is-billing-program-available-result-value)                        | Result value that represents a billing program is available. |
| [google::play::billing::LaunchPurchaseFlowParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/launch-purchase-flow-params)                                                  | Params for launching the purchase flow.                      |
| [google::play::billing::LaunchPurchaseFlowResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/launch-purchase-flow-result-value)                                       | Result value for launching the purchase flow.                |
| [google::play::billing::ProductDetails](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-details)                                                                        | Details for a product.                                       |
| [google::play::billing::ProductId](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-id)                                                                                  | The Google Play Store product identifier.                    |
| [google::play::billing::ProductOffer](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-offer)                                                                            | Offer details for a product.                                 |
| [google::play::billing::ProductPurchaseDetails](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/product-purchase-details)                                                       | Details for a purchased product.                             |
| [google::play::billing::QueryProductDetailsParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/query-product-details-params)                                                | Params for querying product details.                         |
| [google::play::billing::QueryProductDetailsResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/query-product-details-result-value)                                     | Result value for querying product details.                   |
| [google::play::billing::QueryPurchasesResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/billing/query-purchases-result-value)                                                | Result value for querying purchases.                         |

## [google::play::games::recall](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/games/recall)

|                                                                                                            ### Classes                                                                                                            ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [google::play::games::recall::GamesRecallClient](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/games/recall/games-recall-client) | Entrypoint for the Google Play Games Services Recall API. |

|                                                                                                             ### Structs                                                                                                             ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [google::play::games::recall::RecallAccessResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/games/recall/recall-access-result-value) | The Google Play Games Services recall access. |

## [google::play::initialization](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/initialization)

|                                                                                                     ### Structs                                                                                                      ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| [google::play::initialization::InitializeResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/initialization/initialize-result-value) | Result value for initialization. |

## [google::play::install_referrer](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/install-referrer)

|                                                                                                           ### Classes                                                                                                           ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| [google::play::install_referrer::InstallReferrerClient](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/install-referrer/install-referrer-client) | Entrypoint for the Install Referrer API. |

|                                                                                                                        ### Structs                                                                                                                         ||
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [google::play::install_referrer::GetInstallReferrerResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/install-referrer/get-install-referrer-result-value) | The result value for the GetInstallReferrer API. |

## [google::play::integrity](https://developer.android.com/games/playgames/native-pc/reference/namespace/google/play/integrity)

|                                                                                                ### Classes                                                                                                ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [google::play::integrity::IntegrityClient](https://developer.android.com/games/playgames/native-pc/reference/class/google/play/integrity/integrity-client) | Entrypoint for the Google Play Integrity API. |

|                                                                                                                   ### Structs                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| [google::play::integrity::PrepareIntegrityTokenParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/prepare-integrity-token-params)            | Params for preparing an integrity token.       |
| [google::play::integrity::PrepareIntegrityTokenResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/prepare-integrity-token-result-value) | Result value for preparing an integrity token. |
| [google::play::integrity::RequestIntegrityTokenParams](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-integrity-token-params)            | Params for requesting an integrity token.      |
| [google::play::integrity::RequestIntegrityTokenResultValue](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-integrity-token-result-value) | Result value of the integrity token request.   |
| [google::play::integrity::RequestTokenData](https://developer.android.com/games/playgames/native-pc/reference/struct/google/play/integrity/request-token-data)                                   | Data needed to request an integrity token.     |