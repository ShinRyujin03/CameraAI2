from PIL import Image
from io import BytesIO

def binary_to_image(binary_data, output_path):
    # Assuming binary_data contains the image data in RGBA mode
    image = Image.open(BytesIO(binary_data)).convert('RGB')
    image.save(output_path)

# Example usage:
with open('/Users/macbookairm1/Desktop/image-image_file.bin', 'rb') as file:
    binary_data = file.read()

# Specify the path for the output image
output_image_path = 'image.jpg'

# Convert binary data to an image and save it
binary_to_image(binary_data, output_image_path)
