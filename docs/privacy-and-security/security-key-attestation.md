---
title: https://developer.android.com/privacy-and-security/security-key-attestation
url: https://developer.android.com/privacy-and-security/security-key-attestation
source: md.txt
---

# Verify hardware-backed key pairs with key attestation

Key attestation gives you more confidence that the keys you use in your app are stored in a device's hardware-backed keystore. The following sections describe how to verify the properties of hardware-backed keys and how to interpret the attestation certificates' extension data.  
**Note:** Before you verify the properties of a device's hardware-backed keys in a production-level environment, make sure that the device supports hardware-level key attestation. To do so, check that the attestation certificate chain contains a root certificate that is signed with the Google attestation root key and that the`attestationSecurityLevel`element within the[key description](https://source.android.com/docs/security/features/keystore/attestation#keydescription-fields)data structure is set to the`TrustedEnvironment`security level or to the`StrongBox`security level.

In addition, it's important to verify the signatures in the certificate chain and to confirm that none of the keys in the chain have been revoked by checking the[certificate revocation status list](https://developer.android.com/privacy-and-security/security-key-attestation#certificate_status). Unless all are valid and the root is the Google root key, don't fully trust the attestation.

## Retrieve and verify a hardware-backed key pair

During key attestation, you specify the alias of a key pair and retrieve its certificate chain, which you can use to verify the properties of that key pair.

If the device supports hardware-level key attestation, the root certificate within this chain is signed using an attestation root key that is securely provisioned to the device's hardware-backed keystore.

**Note:** On devices that ship with hardware-level key attestation, Android 7.0 (API level 24) or higher, and Google Play services, the root certificate is signed with the Google attestation root key. Verify that this root certificate is among those listed in the section on[root certificates](https://developer.android.com/privacy-and-security/security-key-attestation#root_certificate).

To implement key attestation, complete the following steps:

1. Use a[KeyStore](https://developer.android.com/reference/java/security/KeyStore)object's[getCertificateChain()](https://developer.android.com/reference/java/security/KeyStore#getCertificateChain(java.lang.String))method to get a reference to the chain of X.509 certificates associated with the hardware-backed keystore.
2. Send the certificates to a separate server that you trust for validation.

   **Caution:**Don't complete the following validation process on the same device. If the Android system on that device is compromised, that could cause the validation process to trust something that is untrustworthy.
3. Obtain a reference to the X.509 certificate chain parsing and validation library that is most appropriate for your toolset. Verify that the root public certificate is trustworthy and that each certificate signs the next certificate in the chain.

4. Check each certificate's[revocation status](https://developer.android.com/privacy-and-security/security-key-attestation#certificate_status)to ensure that none of the certificates have been revoked.

5. Optionally, inspect the provisioning information certificate extension that is only present in newer certificate chains.

   Obtain a reference to the CBOR parser library that is most appropriate for your toolset. Find the nearest certificate to the root that contains the[provisioning information certificate extension](https://source.android.com/docs/security/features/keystore/attestation#provisioninginfo_extension). Use the parser to extract the provisioning information certificate extension data from that certificate.

   See the section about the[provisioning information extension](https://source.android.com/docs/security/features/keystore/attestation#provisioninginfo_extension)for more details.
6. Obtain a reference to the ASN.1 parser library that is most appropriate for your toolset. Find the nearest certificate to the root that contains the[key attestation certificate extension](https://source.android.com/docs/security/features/keystore/attestation#attestation-extension). If the provisioning information certificate extension was present, the key attestation certificate extension must be in the immediately subsequent certificate. Use the parser to extract the key attestation certificate extension data from that certificate.

   **Caution:**Don't assume that the key attestation certificate extension is in the leaf certificate of the chain. Only the first occurrence of the extension in the chain can be trusted. Any further instances of the extension have not been issued by the secure hardware and might have been issued by an attacker extending the chain while attempting to create fake attestations for untrusted keys.

   The[Key Attestation sample](https://github.com/googlesamples/android-key-attestation)uses the ASN.1 parser from[Bouncy Castle](https://www.bouncycastle.org/)to extract an attestation certificate's extension data. You can use this sample as a reference for creating your own parser.

   See the section about the[key attestation extension data schema](https://source.android.com/docs/security/features/keystore/attestation#schema)for more details.
7. Check the extension data that you've retrieved in the previous steps for consistency and compare with the set of values that you expect the hardware-backed key to contain.

## Root certificates

The trustworthiness of the attestation depends on the root certificate of the chain. Android devices that have passed the testing required to have the Google suite of apps, including Google Play, and which launched with Android 7.0 (API level 24) or higher should use attestation keys signed by the Google Hardware Attestation Root certificate. Note that attestation was not required until Android 8.0 (API level 26). The set of valid root certificates may be downloaded as a[JSON-formatted array](https://android.googleapis.com/attestation/root).
Root Certificates

The following two root certificates should be used as trust anchors when verifying a key attestation certificate chain.  

```
-----BEGIN CERTIFICATE-----
MIIFHDCCAwSgAwIBAgIJAPHBcqaZ6vUdMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNV
BAUTEGY5MjAwOWU4NTNiNmIwNDUwHhcNMjIwMzIwMTgwNzQ4WhcNNDIwMzE1MTgw
NzQ4WjAbMRkwFwYDVQQFExBmOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0B
AQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHsK7Qui8xUFmOr75gvMsd/dTEDDJdS
Sxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfdnJLmN0pTy/4lj4/7
tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y//0rb+T+W8a9nsNL/ggj
nar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB/M0n1n/W9nGq
C4FSYa04T6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl/m00QLVWutHQ
oVJYnFPlXTcHYvASLu+RhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+O
JtvsBslHZvPBKCOdT0MS+tgSOIfga+z1Z1g7+DVagf7quvmag8jfPioyKvxnK/Eg
sTUVi2ghzq8wm27ud/mIM7AY2qEORR8Go3TVB4HzWQgpZrt3i5MIlCaY504LzSRi
igHCzAPlHws+W0rB5N+er5/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6tUXHI/+M
RPjy02i59lINMRRev56GKtcd9qO/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9E
aDK8Z4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR/bkwSWc+NpUFgNPN9PvQi8WEg5Um
AGMCAwEAAaNjMGEwHQYDVR0OBBYEFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMB8GA1Ud
IwQYMBaAFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMA8GA1UdEwEB/wQFMAMBAf8wDgYD
VR0PAQH/BAQDAgIEMA0GCSqGSIb3DQEBCwUAA4ICAQB8cMqTllHc8U+qCrOlg3H7
174lmaCsbo/bJ0C17JEgMLb4kvrqsXZs01U3mB/qABg/1t5Pd5AORHARs1hhqGIC
W/nKMav574f9rZN4PC2ZlufGXb7sIdJpGiO9ctRhiLuYuly10JccUZGEHpHSYM2G
tkgYbZba6lsCPYAAP83cyDV+1aOkTf1RCp/lM0PKvmxYN10RYsK631jrleGdcdkx
oSK//mSQbgcWnmAEZrzHoF1/0gso1HZgIn0YLzVhLSA/iXCX4QT2h3J5z3znluKG
1nv8NQdxei2DIIhASWfu804CA96cQKTTlaae2fweqXjdN1/v2nqOhngNyz1361mF
mr4XmaKH/ItTwOe72NI9ZcwS1lVaCvsIkTDCEXdm9rCNPAY10iTunIHFXRh+7KPz
lHGewCq/8TOohBRn0/NNfh7uRslOSZ/xKbN9tMBtw37Z8d2vvnXq/YWdsm1+JLVw
n6yYD/yacNJBlwpddla8eaVMjsF6nBnIgQOf9zKSe06nSTqvgwUHosgOECZJZ1Eu
zbH4yswbt02tKtKEFhx+v+OTge/06V+jGsqTWLsfrOCNLuA8H++z+pUENmpqnnHo
vaI47gC+TNpkgYGkkBT6B/m/U01BuOBBTzhIlMEZq9qkDWuM2cA5kW5V3FJUcfHn
w1IdYIg2Wxg7yHcQZemFQg==
-----END CERTIFICATE-----
```

The following root certificate will begin signing attestation certificate chains on February 1, 2026.  

```
-----BEGIN CERTIFICATE-----
MIICIjCCAaigAwIBAgIRAISp0Cl7DrWK5/8OgN52BgUwCgYIKoZIzj0EAwMwUjEc
MBoGA1UEAwwTS2V5IEF0dGVzdGF0aW9uIENBMTEQMA4GA1UECwwHQW5kcm9pZDET
MBEGA1UECgwKR29vZ2xlIExMQzELMAkGA1UEBhMCVVMwHhcNMjUwNzE3MjIzMjE4
WhcNMzUwNzE1MjIzMjE4WjBSMRwwGgYDVQQDDBNLZXkgQXR0ZXN0YXRpb24gQ0Ex
MRAwDgYDVQQLDAdBbmRyb2lkMRMwEQYDVQQKDApHb29nbGUgTExDMQswCQYDVQQG
EwJVUzB2MBAGByqGSM49AgEGBSuBBAAiA2IABCPaI3FO3z5bBQo8cuiEas4HjqCt
G/mLFfRT0MsIssPBEEU5Cfbt6sH5yOAxqEi5QagpU1yX4HwnGb7OtBYpDTB57uH5
Eczm34A5FNijV3s0/f0UPl7zbJcTx6xwqMIRq6NCMEAwDwYDVR0TAQH/BAUwAwEB
/zAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFFIyuyz7RkOb3NaBqQ5lZuA0QepA
MAoGCCqGSM49BAMDA2gAMGUCMETfjPO/HwqReR2CS7p0ZWoD/LHs6hDi422opifH
EUaYLxwGlT9SLdjkVpz0UUOR5wIxAIoGyxGKRHVTpqpGRFiJtQEOOTp/+s1GcxeY
uR2zh/80lQyu9vAFCj6E4AXc+osmRg==
-----END CERTIFICATE-----
  
```
Previously Issued Root Certificates  

```
-----BEGIN CERTIFICATE-----
MIIFYDCCA0igAwIBAgIJAOj6GWMU0voYMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNV
BAUTEGY5MjAwOWU4NTNiNmIwNDUwHhcNMTYwNTI2MTYyODUyWhcNMjYwNTI0MTYy
ODUyWjAbMRkwFwYDVQQFExBmOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0B
AQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHsK7Qui8xUFmOr75gvMsd/dTEDDJdS
Sxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfdnJLmN0pTy/4lj4/7
tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y//0rb+T+W8a9nsNL/ggj
nar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB/M0n1n/W9nGq
C4FSYa04T6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl/m00QLVWutHQ
oVJYnFPlXTcHYvASLu+RhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+O
JtvsBslHZvPBKCOdT0MS+tgSOIfga+z1Z1g7+DVagf7quvmag8jfPioyKvxnK/Eg
sTUVi2ghzq8wm27ud/mIM7AY2qEORR8Go3TVB4HzWQgpZrt3i5MIlCaY504LzSRi
igHCzAPlHws+W0rB5N+er5/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6tUXHI/+M
RPjy02i59lINMRRev56GKtcd9qO/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9E
aDK8Z4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR/bkwSWc+NpUFgNPN9PvQi8WEg5Um
AGMCAwEAAaOBpjCBozAdBgNVHQ4EFgQUNmHhAHyIBQlRi0RsR/8aTMnqTxIwHwYD
VR0jBBgwFoAUNmHhAHyIBQlRi0RsR/8aTMnqTxIwDwYDVR0TAQH/BAUwAwEB/zAO
BgNVHQ8BAf8EBAMCAYYwQAYDVR0fBDkwNzA1oDOgMYYvaHR0cHM6Ly9hbmRyb2lk
Lmdvb2dsZWFwaXMuY29tL2F0dGVzdGF0aW9uL2NybC8wDQYJKoZIhvcNAQELBQAD
ggIBACDIw41L3KlXG0aMiS//cqrG+EShHUGo8HNsw30W1kJtjn6UBwRM6jnmiwfB
Pb8VA91chb2vssAtX2zbTvqBJ9+LBPGCdw/E53Rbf86qhxKaiAHOjpvAy5Y3m00m
qC0w/Zwvju1twb4vhLaJ5NkUJYsUS7rmJKHHBnETLi8GFqiEsqTWpG/6ibYCv7rY
DBJDcR9W62BW9jfIoBQcxUCUJouMPH25lLNcDc1ssqvC2v7iUgI9LeoM1sNovqPm
QUiG9rHli1vXxzCyaMTjwftkJLkf6724DFhuKug2jITV0QkXvaJWF4nUaHOTNA4u
JU9WDvZLI1j83A+/xnAJUucIv/zGJ1AMH2boHqF8CY16LpsYgBt6tKxxWH00XcyD
CdW2KlBCeqbQPcsFmWyWugxdcekhYsAWyoSf818NUsZdBWBaR/OukXrNLfkQ79Iy
ZohZbvabO/X+MVT3rriAoKc8oE2Uws6DF+60PV7/WIPjNvXySdqspImSN78mflxD
qwLqRBYkA3I75qppLGG9rp7UCdRjxMl8ZDBld+7yvHVgt1cVzJx9xnyGCC23Uaic
MDSXYrB4I4WHXPGjxhZuCuPBLTdOLU8YRvMYdEvYebWHMpvwGCF6bAx3JBpIeOQ1
wDB5y0USicV3YgYGmi+NZfhA4URSh77Yd6uuJOJENRaNVTzk
-----END CERTIFICATE-----
  
```  

```
-----BEGIN CERTIFICATE-----
MIIFHDCCAwSgAwIBAgIJANUP8luj8tazMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNV
BAUTEGY5MjAwOWU4NTNiNmIwNDUwHhcNMTkxMTIyMjAzNzU4WhcNMzQxMTE4MjAz
NzU4WjAbMRkwFwYDVQQFExBmOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0B
AQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHsK7Qui8xUFmOr75gvMsd/dTEDDJdS
Sxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfdnJLmN0pTy/4lj4/7
tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y//0rb+T+W8a9nsNL/ggj
nar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB/M0n1n/W9nGq
C4FSYa04T6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl/m00QLVWutHQ
oVJYnFPlXTcHYvASLu+RhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+O
JtvsBslHZvPBKCOdT0MS+tgSOIfga+z1Z1g7+DVagf7quvmag8jfPioyKvxnK/Eg
sTUVi2ghzq8wm27ud/mIM7AY2qEORR8Go3TVB4HzWQgpZrt3i5MIlCaY504LzSRi
igHCzAPlHws+W0rB5N+er5/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6tUXHI/+M
RPjy02i59lINMRRev56GKtcd9qO/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9E
aDK8Z4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR/bkwSWc+NpUFgNPN9PvQi8WEg5Um
AGMCAwEAAaNjMGEwHQYDVR0OBBYEFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMB8GA1Ud
IwQYMBaAFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMA8GA1UdEwEB/wQFMAMBAf8wDgYD
VR0PAQH/BAQDAgIEMA0GCSqGSIb3DQEBCwUAA4ICAQBOMaBc8oumXb2voc7XCWnu
XKhBBK3e2KMGz39t7lA3XXRe2ZLLAkLM5y3J7tURkf5a1SutfdOyXAmeE6SRo83U
h6WszodmMkxK5GM4JGrnt4pBisu5igXEydaW7qq2CdC6DOGjG+mEkN8/TA6p3cno
L/sPyz6evdjLlSeJ8rFBH6xWyIZCbrcpYEJzXaUOEaxxXxgYz5/cTiVKN2M1G2ok
QBUIYSY6bjEL4aUN5cfo7ogP3UvliEo3Eo0YgwuzR2v0KR6C1cZqZJSTnghIC/vA
D32KdNQ+c3N+vl2OTsUVMC1GiWkngNx1OO1+kXW+YTnnTUOtOIswUP/Vqd5SYgAI
mMAfY8U9/iIgkQj6T2W6FsScy94IN9fFhE1UtzmLoBIuUFsVXJMTz+Jucth+IqoW
Fua9v1R93/k98p41pjtFX+H8DslVgfP097vju4KDlqN64xV1grw3ZLl4CiOe/A91
oeLm2UHOq6wn3esB4r2EIQKb6jTVGu5sYCcdWpXr0AUVqcABPdgL+H7qJguBw09o
jm6xNIrw2OocrDKsudk/okr/AwqEyPKw9WnMlQgLIKw1rODG2NvU9oR3GVGdMkUB
ZutL8VuFkERQGt6vQ2OCw0sV47VMkuYbacK/xyZFiRcrPJPb41zgbQj9XAEyLKCH
ex0SdDrx+tWUDqG8At2JHA==
-----END CERTIFICATE-----
  
```  

```
-----BEGIN CERTIFICATE-----
MIIFHDCCAwSgAwIBAgIJAMNrfES5rhgxMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNV
BAUTEGY5MjAwOWU4NTNiNmIwNDUwHhcNMjExMTE3MjMxMDQyWhcNMzYxMTEzMjMx
MDQyWjAbMRkwFwYDVQQFExBmOTIwMDllODUzYjZiMDQ1MIICIjANBgkqhkiG9w0B
AQEFAAOCAg8AMIICCgKCAgEAr7bHgiuxpwHsK7Qui8xUFmOr75gvMsd/dTEDDJdS
Sxtf6An7xyqpRR90PL2abxM1dEqlXnf2tqw1Ne4Xwl5jlRfdnJLmN0pTy/4lj4/7
tv0Sk3iiKkypnEUtR6WfMgH0QZfKHM1+di+y9TFRtv6y//0rb+T+W8a9nsNL/ggj
nar86461qO0rOs2cXjp3kOG1FEJ5MVmFmBGtnrKpa73XpXyTqRxB/M0n1n/W9nGq
C4FSYa04T6N5RIZGBN2z2MT5IKGbFlbC8UrW0DxW7AYImQQcHtGl/m00QLVWutHQ
oVJYnFPlXTcHYvASLu+RhhsbDmxMgJJ0mcDpvsC4PjvB+TxywElgS70vE0XmLD+O
JtvsBslHZvPBKCOdT0MS+tgSOIfga+z1Z1g7+DVagf7quvmag8jfPioyKvxnK/Eg
sTUVi2ghzq8wm27ud/mIM7AY2qEORR8Go3TVB4HzWQgpZrt3i5MIlCaY504LzSRi
igHCzAPlHws+W0rB5N+er5/2pJKnfBSDiCiFAVtCLOZ7gLiMm0jhO2B6tUXHI/+M
RPjy02i59lINMRRev56GKtcd9qO/0kUJWdZTdA2XoS82ixPvZtXQpUpuL12ab+9E
aDK8Z4RHJYYfCT3Q5vNAXaiWQ+8PTWm2QgBR/bkwSWc+NpUFgNPN9PvQi8WEg5Um
AGMCAwEAAaNjMGEwHQYDVR0OBBYEFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMB8GA1Ud
IwQYMBaAFDZh4QB8iAUJUYtEbEf/GkzJ6k8SMA8GA1UdEwEB/wQFMAMBAf8wDgYD
VR0PAQH/BAQDAgIEMA0GCSqGSIb3DQEBCwUAA4ICAQBTNNZe5cuf8oiq+jV0itTG
zWVhSTjOBEk2FQvh11J3o3lna0o7rd8RFHnN00q4hi6TapFhh4qaw/iG6Xg+xOan
63niLWIC5GOPFgPeYXM9+nBb3zZzC8ABypYuCusWCmt6Tn3+Pjbz3MTVhRGXuT/T
QH4KGFY4PhvzAyXwdjTOCXID+aHud4RLcSySr0Fq/L+R8TWalvM1wJJPhyRjqRCJ
erGtfBagiALzvhnmY7U1qFcS0NCnKjoO7oFedKdWlZz0YAfu3aGCJd4KHT0MsGiL
Zez9WP81xYSrKMNEsDK+zK5fVzw6jA7cxmpXcARTnmAuGUeI7VVDhDzKeVOctf3a
0qQLwC+d0+xrETZ4r2fRGNw2YEs2W8Qj6oDcfPvq9JySe7pJ6wcHnl5EZ0lwc4xH
7Y4Dx9RA1JlfooLMw3tOdJZH0enxPXaydfAD3YifeZpFaUzicHeLzVJLt9dvGB0b
HQLE4+EqKFgOZv2EoP686DQqbVS1u+9k0p2xbMA105TBIk7npraa8VM0fnrRKi7w
lZKwdH+aNAyhbXRW9xsnODJ+g8eF452zvbiKKngEKirK5LGieoXBX7tZ9D1GNBH2
Ob3bKOwwIWdEFle/YF/h6zWgdeoaNGDqVBrLr2+0DtWoiB1aDEjLWl9FmyIUyUm7
mD/vFDkzF+wm7cyWpQpCVQ==
-----END CERTIFICATE-----
  
```

If the root certificate in the attestation chain you receive contains this public key and none of the certificates in the chain have been[revoked](https://developer.android.com/privacy-and-security/security-key-attestation#certificate_status), you know that:

1. Your key is in hardware that Google believes to be secure; and
2. It has the properties described in the attestation certificate.

If the attestation chain has any other root public key, then Google does not make any claims about the security of the hardware. This doesn't mean that your key is compromised, only that the attestation doesn't prove that the key is in secure hardware. Adjust your security assumptions accordingly.

If the root certificate doesn't contain the public key on this page, there are two likely reasons:

- Most likely, the device launched with an Android version less than 7.0 and it doesn't support hardware attestation. In this case, Android has a software implementation of attestation that produces the same sort of attestation certificate, but signed with a key[hardcoded in Android source code](https://android.googlesource.com/platform/system/keymaster/+/android-9.0.0_r30/contexts/soft_attestation_cert.cpp#176). Because this signing key isn't a secret, the attestation might have been created by an attacker pretending to provide secure hardware.
- The other likely reason is that the device isn't a Google Play device. In that case, the device maker is free to create their own root certificate and to define the meaning of their attestation data. Refer to the device maker's documentation. Note that Google isn't aware of any device makers who have done this.

## Hardware Attestation Root Certificate Rotation

**Google is introducing a new root certificate for Android Key Attestation**. This change enhances the security and reliability of the attestation process for sensitive applications. A new root key has been generated for Android Key Attestation (KeyMint). The new root is an ECDSA P-384 key, and an ML-DSA (Post-Quantum Digital Signature Algorithm) key is planned for the future.

### Action For Developers

- If your app relies on Android Key Attestation, add the new root certificate to your trust stores by January 2026. Download both the new and old certificates from<https://android.googleapis.com/attestation/root>
- Devices that use[Remote Key Provisioning (RKP)](https://source.android.com/docs/core/ota/modular-system/remote-key-provisioning)will begin receiving certificates rooted in this new certificate in February 2026. RKP-enabled devices will exclusively use the new root by April 10, 2026.
- Update your attestation processes to trust**both**the new and existing root certificates. Older devices with factory-provisioned keys don't support key rotation and continue to use the old root.
- The certificate extension schema itself will remain unchanged; only the root is changing.
- Both human-readable and machine-readable forms of the new root will be publicly available.

### Best Practices

Don't query an endpoint for trusted roots at runtime, as this action creates security risks. Handle changes to roots of trust through a formal process.

### Phase out factory keys: Remote Key Provisioning (RKP)

For devices that launch with Android 16, the system supports only RKP. This policy phases out factory keys. It improves how you provision and manage attestation keys, expanding on the Android 15 policy where RKP support was optional. RKP prevents key leakage because the system does not program keys directly onto the device. You cannot delete these keys from the device. If you must revoke a key, you can target the revocation to a single device.

### Attestation verification libraries

Use the attestation verification[Kotlin](https://github.com/android/keyattestation)library to verify Key Attestation certificate chains. Moreover, this library already integrates the new[root certificates](https://github.com/android/keyattestation/blob/main/roots.json). If you are using a different verifier, we recommend moving to the Kotlin library instead. It is well-tested, and covers edge cases that are often missed by custom verifiers.

## Certificate revocation status list

Attestation keys can be revoked for a number of reasons, including mishandling or suspected extraction by an attacker. Therefore, it's critical that the status of each certificate in an attestation chain be checked against the official certificate revocation status list (CRL). This list is maintained by Google and published at:<https://android.googleapis.com/attestation/status>. The`Cache-Control`header in the HTTP response determines how often to check for updates so a network request is not required for every certificate being verified. This URL returns a JSON file containing the revocation status for any certificates that don't have a normal valid status. The format of the JSON file adheres to the following JSON Schema ([draft 07](https://tools.ietf.org/html/draft-handrews-json-schema-01)) definition:  

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "entries": {
      "description" : "Each entry represents the status of an attestation key. The dictionary-key is the certificate serial number in lowercase hex.",
      "type": "object",
      "propertyNames": {
        "pattern": "^[a-f1-9][a-f0-9]*$"
      },
      "additionalProperties": {
        "type": "object",
        "properties": {
          "status": {
            "description": "[REQUIRED] Current status of the key.",
            "type": "string",
            "enum": ["REVOKED", "SUSPENDED"]
          },
          "expires": {
            "description": "[OPTIONAL] UTC date when certificate expires in ISO8601 format (YYYY-MM-DD). Can be used to clear expired certificates from the status list.",
            "type": "string",
            "format": "date"
          },
          "reason": {
            "description": "[OPTIONAL] Reason for the current status.",
            "type": "string",
            "enum": ["UNSPECIFIED", "KEY_COMPROMISE", "CA_COMPROMISE", "SUPERSEDED", "SOFTWARE_FLAW"]
          },
          "comment": {
            "description": "[OPTIONAL] Free form comment about the key status.",
            "type": "string",
            "maxLength": 140
          }
        },
        "required": ["status"],
        "additionalProperties": false
      }
    }
  },
  "required": ["entries"],
  "additionalProperties": false
}
```

Example CRL:  

```
{
  "entries": {
    "2c8cdddfd5e03bfc": {
      "status": "REVOKED",
      "expires": "2020-11-13",
      "reason": "KEY_COMPROMISE",
      "comment": "Key stored on unsecure system"
    },
    "c8966fcb2fbb0d7a": {
      "status": "SUSPENDED",
      "reason": "SOFTWARE_FLAW",
      "comment": "Bug in keystore causes this key malfunction b/555555"
    }
  }
}
```

## Certificate revocation policy

Attestation forms the backbone of counterabuse and trust in the Android ecosystem. It provides a cryptographically verifiable statement to off-device parties about the booted state of the device.

The certificates for Android attestation keys will be revoked when the keys are compromised, due to the critical nature of attestation validity. This section outlines a policy for when certificates are revoked. This policy is likely to evolve and enumerate additional cases over time.

## What qualifies for revocation?

Attestation key leaks only affect the older provisioning mechanism supported in Android and don't apply to attestation keys certified by the newer Remote Key Provisioning (RKP) mechanism.

Attestation keys that have been leaked are always eligible to have their certificates revoked. Leaks are discoverable in a number of ways, including:

- Analysis of attestation data in the wild.
- Discovery of attestation keys on social media or other public sites.
- Reports directly from security researchers.

Upon discovery, attestation certificates will be revoked by having their serial numbers added to the[revocation list](https://android.googleapis.com/attestation/status). Typically this will happen within several days of discovery, but may take longer in rare cases. For example, the revocation of certificates for leaked attestation keys is usually delayed if the devices affected by the revocation can be securely re-provisioned. Scale of the impact of the revocation is also an important factor in revocation timelines.

## Key attestation extension data schema

| **Note:** Documentation about this attestation extension's data schema has been moved to<https://source.android.com/docs/security/features/keystore/attestation#schema>.

## Provisioning information extension data schema

| **Note:** Documentation about this attestation extension's data schema has been moved to<https://source.android.com/docs/security/features/keystore/attestation#provisioninginfo_extension_schema>.