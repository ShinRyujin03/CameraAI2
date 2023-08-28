from schema import Schema, And
import imghdr

# Define the accepted image formats
ACCEPTED_IMAGE_FORMATS = ["jpeg", "png"]

# Define the schema for the input data
input_schema = Schema({
    "image": And(bytes, lambda value: imghdr.what(None, value) in ACCEPTED_IMAGE_FORMATS, error="Invalid image data or format"),
})
