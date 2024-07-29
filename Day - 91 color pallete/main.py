from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
from collections import Counter
import base64
import io
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the Flask app and set the template folder
app = Flask(__name__, template_folder=os.path.join(current_dir, 'python bootcamp',
            'Python-boot-camp', 'Day - 91 color pallete'))


def get_top_colors(image, num_colors=10):
    # Resize image to speed up processing
    img = image.copy()
    img.thumbnail((100, 100))

    # Convert image to numpy array
    arr = np.array(img)

    # Reshape the array to 2D
    reshaped_arr = arr.reshape(-1, 3)

    # Get unique colors and their counts
    unique_colors, counts = np.unique(reshaped_arr, axis=0, return_counts=True)

    # Sort colors by count (most common first)
    sorted_indices = np.argsort(-counts)
    top_colors = unique_colors[sorted_indices][:num_colors]

    # Convert to hex
    hex_colors = ['#' + ''.join([f'{int(c):02x}' for c in color])
                  for color in top_colors]

    return hex_colors


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/extract_colors', methods=['POST'])
def extract_colors():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file).convert('RGB')

    top_colors = get_top_colors(image)

    # Convert image to base64 for display
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'colors': top_colors, 'image': img_str})


if __name__ == '__main__':
    app.run(debug=True)
