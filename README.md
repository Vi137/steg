# Secure Data Hiding in Images using Steganography (Python)
  
# Description:
This script is a basic implementation of image-based encryption and decryption using **LSB (Least Significant Bit) steganography**. It hides a secret message within an image and allows decryption of the message when the correct password is entered.

# Features:

1. Message Encryption:
   - The secret message is encrypted by converting each character into its ASCII value and then embedding this value into the image's pixel data (using LSB).
   - The encryption process modifies the pixel values to encode the message into the image.
   - The encrypted image is saved as `Encryptedmsg.jpg` and opened automatically.

2. Decryption:
   - The user must input the correct password to decrypt the message.
   - If the password is correct, the message is retrieved by reading the altered pixel values in the image and converting them back into characters (ASCII values).

3. Security:
   - The encryption and decryption processes require a correct password for successful operation.
   - Without the correct password, the message cannot be decrypted, providing some level of security.
     

# Requirements:
1. Python 3.x: The script is written in Python, so Python 3.x must be installed.
   
2. OpenCV Library:
   - The script uses the `cv2` module, which is part of the OpenCV library. Install it with the following command:
     ```bash
     pip install opencv-python
     ```

3. Basic Python Libraries:
   - The script also uses the `os` and `string` modules, both of which are part of the standard Python library, so they do not need to be installed.

4. Image File:
   - You need an image file (e.g., `.jpg`, `.png`) for hiding the message.

5. Command-Line/Terminal Access:
   - The script prompts for input through the command line or terminal, so it should be run in an environment that supports user input.


# Example:
1. Input Image: `mypic.jpg`
2. Secret Message: `"This is a secret message!"`
3. Password: `"my_password"`
4. Encrypted Image: `Encryptedmsg.jpg` (will be saved and opened).
5. For decryption, the user needs to input the correct password to reveal the hidden message.

