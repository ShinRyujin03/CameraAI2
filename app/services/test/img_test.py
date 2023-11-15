from PIL import Image
import io

def binary_to_image(bin_data, output_path):
    # Create a BytesIO object from the binary data
    byte_stream = io.BytesIO(bin_data)

    # Use PIL to open the image from the BytesIO stream
    image = Image.open(byte_stream)

    # Save the image to the specified output path
    image.save(output_path)

# Example usage:
with open('/Users/macbookairm1/Desktop/face_metadata-image_file.bin', 'rb') as file:
    binary_data = file.read()

# Specify the path for the output image
output_image_path = 'image.jpg'

# Convert binary data to an image and save it
binary_to_image(binary_data, output_image_path)
