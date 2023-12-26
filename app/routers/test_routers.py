import io
import logging
from io import BytesIO

from flask import Blueprint, request, send_file

from app.handle.app_error import FileUnreachable
from app.services.test.face_location_test import FaceLocationDrawer
from app.services.test.img_test import BinaryToImage
from app.services.test.numb_face_name_test import Plot

test_router = Blueprint('test_router', __name__)


@test_router.route('/draw_face_locations', methods=['POST'])
def draw_face_locations():
    try:
        image_file = request.files['image']
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    face_locations = request.form['face_location']
    zoom_factor = request.form['zoom']
    # Draw face locations with zoom
    drawer = FaceLocationDrawer()
    result_image_bytes = drawer.draw_face_locations(image_file, face_locations, zoom_factor)
    # Return the zoomed image data as part of the response
    return send_file(io.BytesIO(result_image_bytes), mimetype='image/jpeg')


@test_router.route('/binary_to_image', methods=['POST'])
def get_binary_to_image():
    try:
        binary_file = request.files['binary_image']
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable
    zoom_factor = request.form['zoom']
    bin_file = BinaryToImage()
    image = bin_file.binary_to_image(binary_file, zoom_factor)
    return send_file(BytesIO(image), mimetype='image/jpeg')


@test_router.route('/plot_face_names_histogram', methods=['GET'])
def plot_face_names_histogram():
    plotter = Plot()
    img_stream = plotter.plot_face_names_histogram()
    return send_file(img_stream, mimetype='image/png')
