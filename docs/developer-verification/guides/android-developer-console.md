---
title: https://developer.android.com/developer-verification/guides/android-developer-console
url: https://developer.android.com/developer-verification/guides/android-developer-console
source: md.txt
---

## For developers on the new Android Developer Console

Play developers can also manage their off-Play package names through the
Android developer console if they choose.

### Choose your account type

When you create your ADC account, you will choose a distribution type that fits
your needs. This choice affects the verification requirements and any applicable
fees.

|---|---|---|---|
| Distribution type | Best for | Cost | Key features |
| Full distribution | Organizations and professional developers with wide distribution. | $25 | Unlimited apps and installs; requires full identity verification. |
| Limited distribution | Students, hobbyists, and other personal use. | Free | Capped number of apps and installs. |

### Complete identity verification

You must provide official documentation to verify your identity. The specific
requirements depend on whether you are registering as an individual or an
organization. If you have all of the required information ready, creating your
Android Developer Console account should take you about ten minutes.

You'll need:

- Your legal name and address. These need to be verified by uploading official identity documents.
- A private email address and phone number for Google to contact you. These will need to be verified using a one-time password.
- Organizations need to provide their organization's website. This will need to be verified using Google Search Console.
- Organizations also need to provide their D-U-N-S number. This is a unique 9-digit identifier for organizations. The D-U-N-S number is associated with the organization's name and address.

> [!NOTE]
> **Note:** If you are registering as an organization, you must provide a D-U-N-S number. This is a unique nine-digit identifier for businesses provided by Dun \& Bradstreet that is used globally to establish your business's legal identity. If your organization does not have one, you can get one at no cost from the Dun \& Bradstreet website.

#### Acceptable documents

**Organizations** are required to provide official organization documents based
on the organization's location. The following is an example of what
organizations in the United States must provide. The documents required in your
location may be different.

Example of required documents:

- Any document, notice, or letter either issued by the IRS or stamped by the IRS that states your Organization name. Some examples are CP575, 147C, CP299, 988, 937, 1050, 5822 etc.
- Forms submitted to the IRS will only be accepted if a copy of the form is available on the IRS website. Some examples are Forms 8871 and 990. See here (political organizations) and here (tax exempt organizations) for ways to search for your organization on the IRS website.
- Certificate of Business Incorporation issued by the state where you conduct business activities that states your Organization name
- Your most recent SEC filing (for example, 10-K, 10-Q or 8-K forms) that state the Organization name
- Business credit reports that state your Organization name from Experian, Equifax, or TransUnion
- Only for government departments and agencies: an official letter including full name, address and date

**Individuals** must submit a government-issued photo ID and proof of address
document as part of the verification program. An example of acceptable ID
documents for individuals in the United States are:

- Passport
- State identification
- Driving license
- Permanent resident card or Green card
- Address documents must list the individual's name and address as it appears on their profile. Acceptable address documents include:
- Government issued photo ID with address listed
- Utility bill for electricity, water, gas, internet, cable TV
- Insurance statement (home insurance, health insurance, and so on)
- Credit card or bank statement

## Register your package names

If you distribute apps outside of Google Play, the registration process is
designed to verify the ownership of your app by using the app's private key.

- **For new package names**: You will be prompted to enter your package name and public SHA-256 certificate fingerprint.
- **For existing package names** : If the package name is already in use, you must prove ownership to register it. In most cases, this is a straightforward process:
  1. **Select your key**: Choose your public SHA-256 certificate fingerprint from a list of eligible keys.
  2. **Complete a cryptographic challenge**: You must sign a dummy APK with the corresponding private key and upload it to Android Developer Console. This formally verifies your ownership of the key used to sign your existing Android app.

### Handling duplicate package names

While the Android operating system mandates unique package names on individual
devices, this rule does not extend across the entire Android ecosystem. This can
lead to a scenario where two different developers use the same package name.

Since package name duplication is undesirable, we have established rules to
determine which developer can register the package name. If you and another
developer use the same name, the developer with the higher share of installs
registers it. Other developers will then need to change their package name or
apply for an exception.

**Priority for majority key holder**:

The developer whose signing key accounts for over 50% of total known installs
holds priority for registration. All other developers will be required to use a
different package name.

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| A | com.test.1 | 11 | 1000 |
| B | com.test.1 | 12 | 100 |

*In this scenario, Developer A is eligible to register the package name.
Developer B would need to use another name or apply for an exception*.

**Eligibility for keys with 50+ installs**:

If no single key has over 50% of installs, then all keys with 50 or more
installs become eligible for registration. All other developers---those with keys
with fewer than 50 installs---will be required to request permission to use the
package name.

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| C | com.test.2 | 21 | 100 |
| D | com.test.2 | 22 | 100 |
| E | com.test.2 | 23 | 10 |

*Here, no single key has a majority. Developers C and D, with 50 or more
installs, can register the package name. Developer E would need to use a
different namerequest permission*.

**First-come, first-served for keys under 50 installs**:

If no keys meet the 50-install threshold, all known keys are eligible for
registration on a first-come, first-served basis. As soon as one developer
registers the package name, the other developers would need to use a different
name for their packages (or request exceptions).

|---|---|---|---|
| **Developer** | **Package name** | **Key** | **Installs** |
| F | com.test.3 | 31 | 10 |
| G | com.test.3 | 31 | 10 |

*In this scenario, all developers with keys are eligible. Once one developer
registers the package name, the other would need to request permission*.