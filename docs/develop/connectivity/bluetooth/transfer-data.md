---
title: https://developer.android.com/develop/connectivity/bluetooth/transfer-data
url: https://developer.android.com/develop/connectivity/bluetooth/transfer-data
source: md.txt
---

# Transfer Bluetooth data

After you have successfully[connected to a Bluetooth device](https://developer.android.com/develop/connectivity/bluetooth/connect-bluetooth-devices), each one has a connected[`BluetoothSocket`](https://developer.android.com/reference/android/bluetooth/BluetoothSocket). You can now share information between devices. Using the`BluetoothSocket`, the general procedure to transfer data is as follows:

1. Get the[`InputStream`](https://developer.android.com/reference/java/io/InputStream)and[`OutputStream`](https://developer.android.com/reference/java/io/OutputStream)that handle transmissions through the socket using[`getInputStream()`](https://developer.android.com/reference/android/bluetooth/BluetoothSocket#getInputStream())and[`getOutputStream()`](https://developer.android.com/reference/android/bluetooth/BluetoothSocket#getOutputStream()), respectively.

2. Read and write data to the streams using[`read(byte[])`](https://developer.android.com/reference/java/io/InputStream#read(byte%5B%5D))and[`write(byte[])`](https://developer.android.com/reference/java/io/OutputStream#write(byte%5B%5D)).

There are, of course, implementation details to consider. In particular, you should use a dedicated thread for reading from the stream and writing to it. This is important because both the`read(byte[])`and`write(byte[])`methods are blocking calls. The`read(byte[])`method blocks until there is something to read from the stream. The`write(byte[])`method doesn't usually block, but it can block for flow control if the remote device isn't calling`read(byte[])`quickly enough and the intermediate buffers become full as a result. So, you should dedicate your main loop in the thread to reading from the`InputStream`. You can use a separate public method in the thread to initiate writes to the`OutputStream`.

## Example

The following is an example of how you can transfer data between two devices connected over Bluetooth:  

### Kotlin

```kotlin
private const val TAG = "MY_APP_DEBUG_TAG"

// Defines several constants used when transmitting messages between the
// service and the UI.
const val MESSAGE_READ: Int = 0
const val MESSAGE_WRITE: Int = 1
const val MESSAGE_TOAST: Int = 2
// ... (Add other message types here as needed.)

class MyBluetoothService(
       // handler that gets info from Bluetooth service
       private val handler: Handler) {

   private inner class ConnectedThread(private val mmSocket: BluetoothSocket) : Thread() {

       private val mmInStream: InputStream = mmSocket.inputStream
       private val mmOutStream: OutputStream = mmSocket.outputStream
       private val mmBuffer: ByteArray = ByteArray(1024) // mmBuffer store for the stream

       override fun run() {
           var numBytes: Int // bytes returned from read()

           // Keep listening to the InputStream until an exception occurs.
           while (true) {
               // Read from the InputStream.
               numBytes = try {
                   mmInStream.read(mmBuffer)
               } catch (e: IOException) {
                   Log.d(TAG, "Input stream was disconnected", e)
                   break
               }

               // Send the obtained bytes to the UI activity.
               val readMsg = handler.obtainMessage(
                       MESSAGE_READ, numBytes, -1,
                       mmBuffer)
               readMsg.sendToTarget()
           }
       }

       // Call this from the main activity to send data to the remote device.
       fun write(bytes: ByteArray) {
           try {
               mmOutStream.write(bytes)
           } catch (e: IOException) {
               Log.e(TAG, "Error occurred when sending data", e)

               // Send a failure message back to the activity.
               val writeErrorMsg = handler.obtainMessage(MESSAGE_TOAST)
               val bundle = Bundle().apply {
                   putString("toast", "Couldn't send data to the other device")
               }
               writeErrorMsg.data = bundle
               handler.sendMessage(writeErrorMsg)
               return
           }

           // Share the sent message with the UI activity.
           val writtenMsg = handler.obtainMessage(
                   MESSAGE_WRITE, -1, -1, mmBuffer)
           writtenMsg.sendToTarget()
       }

       // Call this method from the main activity to shut down the connection.
       fun cancel() {
           try {
               mmSocket.close()
           } catch (e: IOException) {
               Log.e(TAG, "Could not close the connect socket", e)
           }
       }
   }
}
```

### Java

```java
public class MyBluetoothService {
   private static final String TAG = "MY_APP_DEBUG_TAG";
   private Handler handler; // handler that gets info from Bluetooth service

   // Defines several constants used when transmitting messages between the
   // service and the UI.
   private interface MessageConstants {
       public static final int MESSAGE_READ = 0;
       public static final int MESSAGE_WRITE = 1;
       public static final int MESSAGE_TOAST = 2;

       // ... (Add other message types here as needed.)
   }

   private class ConnectedThread extends Thread {
       private final BluetoothSocket mmSocket;
       private final InputStream mmInStream;
       private final OutputStream mmOutStream;
       private byte[] mmBuffer; // mmBuffer store for the stream

       public ConnectedThread(BluetoothSocket socket) {
           mmSocket = socket;
           InputStream tmpIn = null;
           OutputStream tmpOut = null;

           // Get the input and output streams; using temp objects because
           // member streams are final.
           try {
               tmpIn = socket.getInputStream();
           } catch (IOException e) {
               Log.e(TAG, "Error occurred when creating input stream", e);
           }
           try {
               tmpOut = socket.getOutputStream();
           } catch (IOException e) {
               Log.e(TAG, "Error occurred when creating output stream", e);
           }

           mmInStream = tmpIn;
           mmOutStream = tmpOut;
       }

       public void run() {
           mmBuffer = new byte[1024];
           int numBytes; // bytes returned from read()

           // Keep listening to the InputStream until an exception occurs.
           while (true) {
               try {
                   // Read from the InputStream.
                   numBytes = mmInStream.read(mmBuffer);
                   // Send the obtained bytes to the UI activity.
                   Message readMsg = handler.obtainMessage(
                           MessageConstants.MESSAGE_READ, numBytes, -1,
                           mmBuffer);
                   readMsg.sendToTarget();
               } catch (IOException e) {
                   Log.d(TAG, "Input stream was disconnected", e);
                   break;
               }
           }
       }

       // Call this from the main activity to send data to the remote device.
       public void write(byte[] bytes) {
           try {
               mmOutStream.write(bytes);

               // Share the sent message with the UI activity.
               Message writtenMsg = handler.obtainMessage(
                       MessageConstants.MESSAGE_WRITE, -1, -1, mmBuffer);
               writtenMsg.sendToTarget();
           } catch (IOException e) {
               Log.e(TAG, "Error occurred when sending data", e);

               // Send a failure message back to the activity.
               Message writeErrorMsg =
                       handler.obtainMessage(MessageConstants.MESSAGE_TOAST);
               Bundle bundle = new Bundle();
               bundle.putString("toast",
                       "Couldn't send data to the other device");
               writeErrorMsg.setData(bundle);
               handler.sendMessage(writeErrorMsg);
           }
       }

       // Call this method from the main activity to shut down the connection.
       public void cancel() {
           try {
               mmSocket.close();
           } catch (IOException e) {
               Log.e(TAG, "Could not close the connect socket", e);
           }
       }
   }
}
```

After the constructor acquires the necessary streams, the thread waits for data to come through the`InputStream`. When`read(byte[])`returns with data from the stream, the data is sent to the main activity using a member[`Handler`](https://developer.android.com/reference/android/os/Handler)from the parent class. The thread then waits for more bytes to be read from the`InputStream`.

To send outgoing data, you call the thread's`write()`method from the main activity and pass in the bytes to be sent. This method calls`write(byte[])`to send the data to the remote device. If an[`IOException`](https://developer.android.com/reference/java/io/IOException)is thrown when calling`write(byte[])`, the thread sends a toast to the main activity, explaining to the user that the device couldn't send the given bytes to the other (connected) device.

The thread's`cancel()`method allows you to terminate the connection at any time by closing the`BluetoothSocket`. Always call this method when you're done using the Bluetooth connection.

For a demonstration of using the Bluetooth APIs, see the[Bluetooth Chat sample app](https://github.com/android/connectivity-samples/tree/master/BluetoothChat)on GitHub.