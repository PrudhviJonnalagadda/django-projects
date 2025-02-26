"""
Name: Neerukonda Santhi Vardhan
LU ID: L20606091
CPSC 4330/5330
Assignment Number: 3
Questions Number: 3.1
Due: 10/07/2024
Submitted: 10/07/2024
"""
from PIL import Image
import matplotlib.pyplot as plt

def gray_scale(image):
    # Convert the image from RGB to grayscale
    gray_image = image.convert('L')
    return gray_image

def one_fourth_black(image):
    # Change one-fourth of the image to black
    black_image = image.copy()
    width, height = black_image.size
    # Define the region to be blacked out (top-left quarter in this case)
    region = (0, 3 * height // 4, width, height)
    black_region = Image.new('RGB', (width, height // 4), (0, 0, 0))
    black_image.paste(black_region, region)
    return black_image

def process_image(image_path: str) -> None:
    # Load the image
    image = Image.open(image_path)

    gray_image = gray_scale(image)

    black_image = one_fourth_black(image)

    # Plot the images
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Original image
    axs[2].imshow(image)
    axs[2].set_title('Original Image')
    axs[2].axis('off')

    # Grayscale image
    axs[1].imshow(gray_image, cmap='gray')
    axs[1].set_title('Grayscale Image')
    axs[1].axis('off')

    # Image with one-fourth black
    axs[0].imshow(black_image)
    axs[0].set_title('One-Fourth Black Image')
    axs[0].axis('off')

    plt.show()


process_image(image_path='flower.jpg') #relative path
