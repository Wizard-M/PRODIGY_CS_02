from PIL import Image

# Function to encrypt the image by adjusting pixel values
def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Encrypt each pixel by applying a key-based transformation
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image by reversing the pixel manipulation
def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Decrypt by reversing the transformation
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to allow user input for encryption and decryption
def main():
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the path to save the output image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    elif choice == 'd':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

# Run the main function
if __name__ == "__main__":
    main()
