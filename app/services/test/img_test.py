from PIL import Image
from io import BytesIO

class BinaryToImage:
    def binary_to_image(self,binary_file):
        binary_data = binary_file.read()

        # Convert binary data to an image
        image = Image.open(BytesIO(binary_data)).convert('RGB')

        # Convert the PIL image to bytes
        image_bytes = BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes = image_bytes.getvalue()
        return image_bytes
