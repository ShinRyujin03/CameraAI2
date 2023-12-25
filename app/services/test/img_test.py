from PIL import Image
from io import BytesIO

class BinaryToImage:
    def binary_to_image(self, binary_file, zoom_factor):
        binary_data = binary_file.read()

        # Convert binary data to an image
        image = Image.open(BytesIO(binary_data)).convert('RGB')
        if not zoom_factor:
            zoom_factor = 1.0
        else:
            zoom_factor = float(zoom_factor)
            if zoom_factor == 0:
                zoom_factor = 1.0
        width, height = image.size
        new_size = (int(width * float(zoom_factor)), int(height * float(zoom_factor)))
        image = image.resize(new_size, Image.LANCZOS)  # Use Image.LANCZOS for antialiasing

        # Convert the PIL image to bytes
        image_bytes = BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes = image_bytes.getvalue()
        return image_bytes
