from schema import Schema,And

# Define the schema for the input data
input_schema = Schema({
    "image": And(bytes, error="Invalid image data"),
})
