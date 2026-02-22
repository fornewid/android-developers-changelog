---
title: https://developer.android.com/tools/apksigner
url: https://developer.android.com/tools/apksigner
source: md.txt
---

The `apksigner` tool, available in revision 24.0.3 and higher of
the Android SDK Build Tools, lets you sign APKs and confirm that an
APK's signature will be verified successfully on all versions of the Android
platform supported by that APK.

This page presents a short guide for using
the tool and serves as a reference for the different command-line options that
the tool supports. For a more complete description of how the
`apksigner` tool is used for signing your APKs, see [Sign your app](https://developer.android.com/studio/publish/app-signing).


**Caution:** If you sign your APK using `apksigner`
and make further changes to the APK, the APK's signature is invalidated.
If you use
[`zipalign`](https://developer.android.com/studio/command-line/zipalign) to align
your APK, use it before signing the APK.

## Usage

### Sign an APK


The syntax for signing an APK using the `apksigner` tool is as
follows:  

```
apksigner sign --ks keystore.jks |
  --key key.pk8 --cert cert.x509.pem
  [signer_options] app-name.apk
```


When you sign an APK using the `apksigner` tool, you must provide
the signer's private key and certificate. You can include this information in
two ways:

- Specify a KeyStore file using the `--ks` option.
- Specify the private key file and certificate file separately using the `--key` and `--cert` options, respectively. The private key file must use the PKCS #8 format, and the certificate file must use the X.509 format.


Usually, you sign an APK using only one signer. If you need to
sign an APK using multiple signers, use the `--next-signer` option
to separate the set of [general options](https://developer.android.com/tools/apksigner#options-sign-general) to
apply to each signer:  

```
apksigner sign [signer_1_options] --next-signer [signer_2_options] app-name.apk
```

### Verify the signature of an APK


The syntax for confirming the successful verification of an APK's signature
on supported platforms is as follows:  

```
apksigner verify [options] app-name.apk
```

### Rotate signing keys

The syntax for rotating a *signing certificate lineage*, or a new sequence of
signatures, is as follows:  

```
$ apksigner rotate --in /path/to/existing/lineage \
  --out /path/to/new/file \
  --old-signer --ks old-signer-jks \
  --new-signer --ks new-signer-jks
```

## Options


The following lists include the set of options for each command that the
`apksigner` tool supports.

### Sign command

The `apksigner` sign command has the following options.

#### General options


The following options specify basic settings to apply to a signer:

`--out <apk-filename>`
:
    The location where you'd like to save the signed APK. If this option isn't
    provided explicitly, the APK package is signed in place, which overwrites
    the input APK file.

`--min-sdk-version <integer>`
:
    The lowest Android framework API level that `apksigner` uses to
    confirm that the APK's signature will be verified. Higher values allow the
    tool to use stronger security parameters when signing the app but limit
    the APK's availability to devices running more recent versions of Android.
    By default, `apksigner` uses the value of the
    `minSdkVersion` attribute from the app's manifest file.

`--max-sdk-version <integer>`
:
    The highest Android framework API level that `apksigner` uses
    to confirm that the APK's signature will be verified. By default, the tool
    uses the highest possible API level.

`--rotation-min-sdk-version <integer>`
:
    The lowest API level the APK's rotated signing
    key should use to produce the APK's signature. The
    original (unrotated) signing key for the APK will be used for all
    previous platform versions. By default,
    rotated signing keys, which are supported on devices that run Android 13
    (API level 33) or higher, are used with the v3.1 signing block.

`--v1-signing-enabled <true | false>`
:
    Determines whether `apksigner` signs the given APK package
    using the traditional, JAR-based signing scheme. By default, the tool uses
    the values of `--min-sdk-version` and
    `--max-sdk-version` to decide when to apply this signature
    scheme.

`--v2-signing-enabled <true | false>`
:
    Determines whether `apksigner` signs the given APK package
    using the [APK
    Signature Scheme v2](https://developer.android.com/about/versions/nougat/android-7.0#apk_signature_v2). By default, the tool uses the values of
    `--min-sdk-version` and `--max-sdk-version` to decide
    when to apply this signature scheme.

`--v3-signing-enabled <true | false>`
:
    Determines whether `apksigner` signs the given APK package
    using the [APK
    Signature Scheme v3](https://source.android.com/security/apksigning/v3). By default, the tool uses the values of
    `--min-sdk-version` and `--max-sdk-version` to decide
    when to apply this signature scheme.

`--v4-signing-enabled <true | false | only>`

:   Determines whether `apksigner` signs the given APK package
    using the [APK
    Signature Scheme v4](https://developer.android.com/about/versions/11/features#signature-scheme-v4). This scheme
    produces a signature in a separate file (<var translate="no">apk-name</var>`.apk.idsig`).
    If `true` and the APK is not signed, then a v2 or v3 signature
    is generated based on the values of `--min-sdk-version` and
    `--max-sdk-version`. The command then produces the
    `.idsig` file based on the content of the signed APK.

    Use `only` to generate only the v4
    signature without modifying the APK and any signatures
    it had before the invocation. `only` fails if the APK doesn't
    have a v2 or v3 signature already or if the signature used a different key
    than the one provided for the current invocation.

    By default, the tool uses the values of
    `--min-sdk-version` and `--max-sdk-version` to decide
    when to apply this signature scheme.

`-v`, `--verbose`
:
    Use the verbose output mode.

#### Per-signer options


The following options specify the configuration of a particular signer. These
options aren't necessary if you sign your app using only one signer.

`--next-signer <signer-options>`
:
    Used for specifying different general options for each signer.

`--v1-signer-name <basename>`
:
    The base name for the files that comprise the JAR-based signature for the
    current signer. By default, `apksigner` uses the key alias of
    the KeyStore or the basename of the key file for this signer.

#### Key and certificate options


The following options specify the signer's private key and certificate:

`--ks <filename>`
:
    The signer's private key and certificate chain reside in the given
    Java-based KeyStore file. If the filename is set to `"NONE"`,
    the KeyStore containing the key and certificate doesn't need a file
    specified, which is the case for some PKCS #11 KeyStores.

`--ks-key-alias <alias>`
:
    The name of the alias that represents the signer's private key and
    certificate data within the KeyStore. If the KeyStore associated with the
    signer contains multiple keys, you must specify this option.

`--ks-pass <input-format>`

:
    The password for the KeyStore that contains the signer's private key and
    certificate. You must provide a password to open a KeyStore. The
    `apksigner` tool supports the following formats:

    - `pass:<password>` -- Password provided inline with the rest of the `apksigner sign` command.
    - `env:<name>` -- Password is stored in the given environment variable.
    - `file:<filename>` -- Password is stored as a single line in the given file.
    - `stdin` -- Password is provided as a single line in the standard input stream. This is the default behavior for `--ks-pass`.


    **Note:** If you include multiple passwords in the same
    file, specify them on separate lines. The `apksigner` tool
    associates passwords with an APK's signers based on the order in which
    you specify the signers. If you've provided two passwords for a signer,
    `apksigner` interprets the first password as the KeyStore
    password and the second one as the key password.

`--pass-encoding <charset>`
:
    Includes the specified character encodings, such as
    `ibm437` or `utf-8`, when trying to
    handle passwords containing non-ASCII characters.


    Keytool often encrypts keystores by converting the password using the console's default
    charset. By default, `apksigner` tries to decrypt using several forms of the
    password:
    - The Unicode form
    - The form encoded using the JVM default charset
    - On Java 8 and older, the form encoded using the console's default charset
    - On Java 9, `apksigner` cannot detect the console's charset. You may need to specify `--pass-encoding` when a non-ASCII password is used. You may also need to specify this option with KeyStores that keytool created on a different OS or in a different locale.

`--key-pass <input-format>`

:
    The password for the signer's private key, which is needed if the
    private key is password protected. The `apksigner` tool
    supports the following formats:

    - `pass:<password>` -- Password is provided inline with the rest of the `apksigner sign` command.
    - `env:<name>` -- Password is stored in the given environment variable.
    - `file:<filename>` -- Password is stored as a single line in the given file.
    - `stdin` -- Password is provided as a single line in the standard input stream. This is the default behavior for `--key-pass`.

`--ks-type <algorithm>`
:
    The type or algorithm associated with the KeyStore that contains the
    signer's private key and certificate. By default, `apksigner`
    uses the type defined as the `keystore.type` constant in the
    Security properties file.

`--ks-provider-name <name>`
:
    The name of the JCA Provider to use when requesting the signer's KeyStore
    implementation. By default, `apksigner` uses the
    highest-priority provider.

`--ks-provider-class <class-name>`
:
    The fully qualified class name of the JCA Provider to use when requesting
    the signer's KeyStore implementation. This option serves as an alternative
    for `--ks-provider-name`. By default, `apksigner`
    uses the provider specified with the `--ks-provider-name`
    option.

`--ks-provider-arg <value>`
:
    A string value to pass in as the argument for the constructor of the JCA
    Provider class; the class itself is defined with the
    `--ks-provider-class` option. By default, `apksigner`
    uses the class's zero-argument constructor.

`--key <filename>`
:
    The name of the file that contains the signer's private key. This file
    must use the PKCS #8 DER format. If the key is password protected,
    `apksigner` prompts for the password using standard input
    unless you specify a different kind of input format using the
    `--key-pass` option.

`--cert <filename>`
:
    The name of the file that contains the signer's certificate chain. This
    file must use the X.509 PEM or DER format.

### Verify command

The `apksigner` verify command has the following options.

`--print-certs`
:
    Show information about the APK's signing certificates.

`--print-certs-pem`
:
    Show information about the APK's signing certificates and print the PEM
    encoding of each signing certificate to stdout.

`--min-sdk-version <integer>`
:
    The lowest Android framework API level that `apksigner` uses to
    confirm that the APK's signature will be verified. Higher values allow the
    tool to use stronger security parameters when signing the app but limit
    the APK's availability to devices running more recent versions of Android.
    By default, `apksigner` uses the value of the
    `minSdkVersion` attribute from the app's manifest file.

`--max-sdk-version <integer>`
:
    The highest Android framework API level that `apksigner` uses
    to confirm that the APK's signature will be verified. By default, the tool
    uses the highest possible API level.

`-v`, `--verbose`
:
    Use the verbose output mode.

`-Werr`
:
    Treat warnings as errors.

## Examples

The following are examples using `apksigner`.

### Sign an APK


Sign an APK using `release.jks`, which is the only key in the
KeyStore:  

```
$ apksigner sign --ks release.jks app.apk
```


Sign an APK using a private key and certificate stored as separate files:  

```
$ apksigner sign --key release.pk8 --cert release.x509.pem app.apk
```


Sign an APK using two keys:  

```
$ apksigner sign --ks first-release-key.jks --next-signer --ks second-release-key.jks app.apk
```


Sign an APK with a rotated signing key and the rotation targeting SDK version 28+:  

```
$ apksigner sign --ks release.jks --next-signer --ks release2.jks \
  --lineage /path/to/signing/history/lineage app.apk \
  --rotation-min-sdk-version 28
```


Sign an APK with a rotated signing key and the rotation targeting SDK version 33+:  

```
$ apksigner sign --ks release.jks --next-signer --ks release2.jks \
  --lineage /path/to/signing/history/lineage app.apk
```

### Verify the signature of an APK


Check whether the APK's signatures are expected to be confirmed as valid on
all Android platforms that the APK supports:  

```
$ apksigner verify app.apk
```


Check whether the APK's signatures are expected to be confirmed as valid on
Android 4.0.3 (API level 15) and higher:  

```
$ apksigner verify --min-sdk-version 15 app.apk
```

### Rotate signing keys

Enable a signing certificate lineage that supports key rotation:  

```
$ apksigner rotate --out /path/to/new/file --old-signer \
    --ks release.jks --new-signer --ks release2.jks
```

Rotate your signing keys again:  

```
$ apksigner rotate --in /path/to/existing/lineage \
  --out /path/to/new/file --old-signer --ks release2.jks \
  --new-signer --ks release3.jks
```