---
title: https://developer.android.com/privacy-and-security/risks/insecure-machine-to-machine
url: https://developer.android.com/privacy-and-security/risks/insecure-machine-to-machine
source: md.txt
---

# Insecure machine-to-machine communication setup

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

It's not rare to see applications that implement functionality allowing users to transfer data, or interact with other devices, using radio frequency (RF) communications or cabled connections. The most common technologies used in Android for this purpose are classic Bluetooth (Bluetooth BR/EDR), Bluetooth Low Energy (BLE), Wifi P2P, NFC, and USB.

These technologies are usually implemented in applications that are expected to communicate with smart home accessories, health monitoring devices, public transportation kiosks, payment terminals, and other Android-powered devices.

As with any other channel, machine-to-machine communications are susceptible to attacks that aim to compromise the trust boundary established between two or more devices. Techniques such as device impersonation can be leveraged by malicious users to achieve a broad number of attacks against the communication channel.

Android makes specific[APIs](https://developer.android.com/develop/connectivity/overview)for configuring machine-to-machine communications available to developers.

These APIs should be used carefully as errors while implementing communication protocols may lead to user or device data being exposed to unauthorized third-parties. In the worst case scenario, attackers may be able to remotely take over one or more devices, consequently gaining full access to the content on the device.

## Impact

The impact may vary according to the device-to-device technology implemented in the application.

The wrong usage or configuration of machine-to-machine communication channels may leave the user device exposed to untrusted communication attempts. This can lead to the device being vulnerable to additional attacks such as man-in-the-middle (MiTM), command injection, DoS, or impersonation attacks.

## Risk: Eavesdropping of sensitive data over wireless channels

When implementing machine-to-machine communication mechanisms, careful consideration should be given to both the used technology and the type of data that should be transmitted. While cabled connections are in practice more secure for such tasks, as they require a physical link between the involved devices, communications protocols using radio frequencies such as classic Bluetooth, BLE, NFC, and Wifi P2P can be intercepted. An attacker may be able to impersonate one of the terminals or access points involved in the data exchange, intercepting the communication over the air, consequently gaining access to sensitive user data. Additionally, malicious applications installed on the device, if granted the communication-specific[runtime permissions](https://developer.android.com/guide/topics/permissions/overview#runtime), may be able to retrieve data exchanged between the devices by reading system message buffers.

### Mitigations

If the application does require machine-to-machine exchange of sensitive data over wireless channels, then application-layer security solutions, such as encryption, should be implemented in the application's code. This will prevent attackers from sniffing on the communication channel and retrieving the exchanged data in clear-text. For additional resources, refer to the[Cryptography](https://developer.android.com/privacy-and-security/cryptography)documentation.

*** ** * ** ***

## Risk: Wireless malicious data injection

Wireless machine-to-machine communication channels (classic Bluetooth, BLE, NFC, Wifi P2P) can be tampered with using malicious data. Sufficiently skilled attackers can identify the communication protocol in use and tamper with the data exchange flow, for example by impersonating one of the endpoints, sending specifically crafted payloads. This kind of malicious traffic may degrade the application's functionality and, in the worst case scenario, cause unexpected application and device behavior, or result in attacks such as DoS, command injection, or device takeover.

### Mitigations

Android provides developers with[powerful APIs](https://developer.android.com/develop/connectivity/overview)to manage machine-to-machine communications such as classic Bluetooth, BLE, NFC, and Wifi P2P. These should be combined with a carefully implemented data validation logic to sanitize any data exchanged between two devices.

This solution should be implemented at the application level and should include checks that verify if the data has the expected length, format, and contains a valid payload that can be interpreted by the application.

The following snippet shows example data validation logic. This was implemented over the Android developers[example](https://developer.android.com/develop/connectivity/bluetooth/transfer-data#example)for implementing Bluetooth data transfer:  

### Kotlin

    class MyThread(private val mmInStream: InputStream, private val handler: Handler) : Thread() {

        private val mmBuffer = ByteArray(1024)
          override fun run() {
            while (true) {
                try {
                    val numBytes = mmInStream.read(mmBuffer)
                    if (numBytes > 0) {
                        val data = mmBuffer.copyOf(numBytes)
                        if (isValidBinaryData(data)) {
                            val readMsg = handler.obtainMessage(
                                MessageConstants.MESSAGE_READ, numBytes, -1, data
                            )
                            readMsg.sendToTarget()
                        } else {
                            Log.w(TAG, "Invalid data received: $data")
                        }
                    }
                } catch (e: IOException) {
                    Log.d(TAG, "Input stream was disconnected", e)
                    break
                }
            }
        }

        private fun isValidBinaryData(data: ByteArray): Boolean {
            if (// Implement data validation rules here) {
                return false
            } else {
                // Data is in the expected format
                return true
            }
        }
    }

### Java

    public void run() {
                mmBuffer = new byte[1024];
                int numBytes; // bytes returned from read()
                // Keep listening to the InputStream until an exception occurs.
                while (true) {
                    try {
                        // Read from the InputStream.
                        numBytes = mmInStream.read(mmBuffer);
                        if (numBytes > 0) {
                            // Handle raw data directly
                            byte[] data = Arrays.copyOf(mmBuffer, numBytes);
                            // Validate the data before sending it to the UI activity
                            if (isValidBinaryData(data)) {
                                // Data is valid, send it to the UI activity
                                Message readMsg = handler.obtainMessage(
                                        MessageConstants.MESSAGE_READ, numBytes, -1,
                                        data);
                                readMsg.sendToTarget();
                            } else {
                                // Data is invalid
                                Log.w(TAG, "Invalid data received: " + data);
                            }
                        }
                    } catch (IOException e) {
                        Log.d(TAG, "Input stream was disconnected", e);
                        break;
                    }
                }
            }

            private boolean isValidBinaryData(byte[] data) {
                if (// Implement data validation rules here) {
                    return false;
                } else {
                    // Data is in the expected format
                    return true;
               }
        }

*** ** * ** ***

## Risk: USB malicious data injection

USB connections between two devices can be targeted by a malicious user interested in intercepting communications. In this case, the physical link required constitutes an additional security layer as the attacker needs to gain access to the cable that connects the terminals to be able to eavesdrop on any message. Another attack vector is represented by untrusted USB devices that, either intentionally or unintentionally, are plugged into the device.

If the application filters USB devices using PID/VID for triggering specific in-app functionality, attackers may be able to tamper with the data sent over the USB channel by impersonating the legitimate device. Attacks of this kind can allow malicious users to send keystrokes to the device or execute application activities that, in the worst case, may lead to remote code execution or unwanted software download.

### Mitigations

An application-level validation logic should be implemented. This logic should filter the data sent over USB checking that the length, format, and content match the application use case. For example, a heartbeat monitor shouldn't be able to send keystroke commands.

Additionally, when possible, consideration should be given to restricting the number of USB packets that the application can receive from the USB device. This prevents malicious devices from performing attacks such as the rubber ducky.

This validation can be accomplished by creating a new thread for checking the buffer content, for example, upon a[`bulkTransfer`](https://developer.android.com/reference/android/hardware/usb/UsbDeviceConnection#bulkTransfer(android.hardware.usb.UsbEndpoint,%20byte%5B%5D,%20int,%20int)):  

### Kotlin

    fun performBulkTransfer() {
        // Stores data received from a device to the host in a buffer
        val bytesTransferred = connection.bulkTransfer(endpointIn, buffer, buffer.size, 5000)

        if (bytesTransferred > 0) {
            if (//Checks against buffer content) {
                processValidData(buffer)
            } else {
                handleInvalidData()
            }
        } else {
            handleTransferError()
        }
    }

### Java

    public void performBulkTransfer() {
            //Stores data received from a device to the host in a buffer
            int bytesTransferred = connection.bulkTransfer(endpointIn, buffer, buffer.length, 5000);
            if (bytesTransferred > 0) {
                if (//Checks against buffer content) {
                    processValidData(buffer);
                } else {
                    handleInvalidData();
                }
            } else {
                handleTransferError();
            }
        }

*** ** * ** ***

## Specific Risks

This section gathers risks that require non-standard mitigation strategies or were mitigated at certain SDK level and are here for completeness.

### Risk: Bluetooth -- incorrect discoverability time

As highlighted in the[Android developers Bluetooth documentation](https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices#enable-discoverability), while configuring the Bluetooth interface within the application, using the[`startActivityForResult(Intent, int)`](https://developer.android.com/reference/android/app/Activity#startActivityForResult(android.content.Intent,%20int))method to enable device discoverability and setting the[`EXTRA_DISCOVERABLE_DURATION`](https://developer.android.com/reference/android/bluetooth/BluetoothAdapter#EXTRA_DISCOVERABLE_DURATION)to zero will cause the device to be discoverable as long as the application is running either in background or foreground. As for[classic Bluetooth specification](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/), discoverable devices are constantly broadcasting specific discovery messages that allow other devices to retrieve device data or connect to it. In such a scenario, a malicious third-party can intercept such messages and connect to the Android-powered device. Once connected, an attacker can perform further attacks such as data theft, DoS, or command injection.

#### Mitigations

The`EXTRA_DISCOVERABLE_DURATION`should never be set to zero. If the`EXTRA_DISCOVERABLE_DURATION`parameter is not set, by default, Android makes the devices discoverable for 2 minutes. The max value that can be set for the`EXTRA_DISCOVERABLE_DURATION`parameter is 2 hours (7200 seconds). It is recommended to keep the discoverable duration time to the shortest time possible, according to the application use case.

*** ** * ** ***

### Risk: NFC -- cloned intent-filters

A malicious application can register intent-filters to read specific NFC tags or NFC-enabled devices. These filters can replicate the ones defined by a legitimate application, making it possible for an attacker to read the content of the exchanged NFC data. It should be noted that, when two activities specify the same intent-filters for a specific NFC tag, the[Activity Chooser](https://developer.android.com/develop/connectivity/nfc/nfc#dispatching)is presented, therefore the user will still need to choose the malicious application for the attack to be successful. Nevertheless, combining intent-filters with cloaking, this scenario is still possible. This attack is significant only for cases where the data exchanged over NFC can be considered highly sensitive.

#### Mitigations

When implementing NFC reading capabilities within an application, intent-filters can be used together with[Android application records](https://developer.android.com/develop/connectivity/nfc/nfc#aar)(AARs). Embedding the AAR record inside an NDEF message will give strong assurance that only the legitimate application, and its associated NDEF handling activity, is started. This will prevent unwanted applications or activities from reading highly sensitive tag or device data exchanged through NFC.

*** ** * ** ***

### Risk: NFC -- lack of NDEF message validation

When an Android-powered device receives data from an[NFC tag](https://developer.android.com/develop/connectivity/nfc/nfc#tag-dispatch)or NFC-enabled device, the system automatically triggers the application or the specific activity that is configured to handle the NDEF message contained within. According to the logic implemented in the application, the data contained in the tag, or received from the device, can be served to other activities to trigger further actions, such as opening web pages.

An application lacking NDEF message content validation may allow attackers to use NFC-enabled devices or NFC tags to inject malicious payloads within the application, causing unexpected behavior that may result in malicious file download, command injection, or DoS.

#### Mitigations

Before dispatching the received NDEF message to any other application component, data within should be validated to be in the expected format and to contain the expected information. This avoids malicious data being passed to other applications' components unfiltered, reducing the risk of unexpected behavior or attacks using tampered NFC data.

The following snippet shows example data validation logic implemented as a method with an NDEF message as an argument and its index in the messages array. This was implemented over the Android developers[example](https://developer.android.com/develop/connectivity/nfc/nfc#obtain-info)to get data from a scanned NFC NDEF tag:  

### Kotlin

    //The method takes as input an element from the received NDEF messages array
    fun isValidNDEFMessage(messages: Array<NdefMessage>, index: Int): Boolean {
        // Checks if the index is out of bounds
        if (index < 0 || index >= messages.size) {
            return false
        }
        val ndefMessage = messages[index]
        // Retrieves the record from the NDEF message
        for (record in ndefMessage.records) {
            // Checks if the TNF is TNF_ABSOLUTE_URI (0x03), if the Length Type is 1
            if (record.tnf == NdefRecord.TNF_ABSOLUTE_URI && record.type.size == 1) {
                // Loads payload in a byte array
                val payload = record.payload

                // Declares the Magic Number that should be matched inside the payload
                val gifMagicNumber = byteArrayOf(0x47, 0x49, 0x46, 0x38, 0x39, 0x61) // GIF89a

                // Checks the Payload for the Magic Number
                for (i in gifMagicNumber.indices) {
                    if (payload[i] != gifMagicNumber[i]) {
                        return false
                    }
                }
                // Checks that the Payload length is, at least, the length of the Magic Number + The Descriptor
                if (payload.size == 13) {
                    return true
                }
            }
        }
        return false
    }

### Java

    //The method takes as input an element from the received NDEF messages array
        public boolean isValidNDEFMessage(NdefMessage[] messages, int index) {
            //Checks if the index is out of bounds
            if (index < 0 || index >= messages.length) {
                return false;
            }
            NdefMessage ndefMessage = messages[index];
            //Retrieve the record from the NDEF message
            for (NdefRecord record : ndefMessage.getRecords()) {
                //Check if the TNF is TNF_ABSOLUTE_URI (0x03), if the Length Type is 1
                if ((record.getTnf() == NdefRecord.TNF_ABSOLUTE_URI) && (record.getType().length == 1)) {
                    //Loads payload in a byte array
                    byte[] payload = record.getPayload();
                    //Declares the Magic Number that should be matched inside the payload
                    byte[] gifMagicNumber = {0x47, 0x49, 0x46, 0x38, 0x39, 0x61}; // GIF89a
                    //Checks the Payload for the Magic Number
                    for (int i = 0; i < gifMagicNumber.length; i++) {
                        if (payload[i] != gifMagicNumber[i]) {
                            return false;
                        }
                    }
                    //Checks that the Payload length is, at least, the length of the Magic Number + The Descriptor
                    if (payload.length == 13) {
                        return true;
                    }
                }
            }
            return false;
        }

*** ** * ** ***

## Resources

- [Runtime Permissions](https://developer.android.com/guide/topics/permissions/overview#runtime)
- [Connectivity guides](https://developer.android.com/develop/connectivity/overview)
- [Example](https://developer.android.com/develop/connectivity/bluetooth/transfer-data#example)
- [bulkTransfer](https://developer.android.com/reference/android/hardware/usb/UsbDeviceConnection#bulkTransfer(android.hardware.usb.UsbEndpoint,%20byte%5B%5D,%20int,%20int))
- [Cryptography](https://developer.android.com/privacy-and-security/cryptography)
- [Set up Bluetooth](https://developer.android.com/develop/connectivity/bluetooth/setup)
- [NFC Basis](https://developer.android.com/develop/connectivity/nfc/nfc)
- [Android application records](https://developer.android.com/develop/connectivity/nfc/nfc#aar)
- [Classic Bluetooth specification](https://www.bluetooth.com/learn-about-bluetooth/tech-overview)