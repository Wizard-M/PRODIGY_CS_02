# PRODIGY_CS_02

Here’s a Python program to implement a basic image encryption tool using pixel manipulation. This tool encrypts an image by applying a simple mathematical operation on each pixel’s RGB values. It also allows decryption by reversing the operation. This example uses the Pillow library to handle image processing.

# Prerequisites
You’ll need the Pillow library, which can be installed using:
pip install pillow

# Explanation:
encrypt_image: This function loads an image and applies an operation to each pixel’s RGB values. The pixel value is incremented by a key (and wrapped around with % 256 for values beyond the RGB range).
decrypt_image: This function reverses the encryption by subtracting the key from each pixel’s RGB values, again using % 256 for wrapping.
main: This function prompts the user to select encryption or decryption, specify the image paths, and enter a key.

# Notes
Image Format: Make sure the input image is in a format compatible with Pillow (e.g., PNG, JPEG).
Key Consistency: The same key used for encryption is required for decryption.
