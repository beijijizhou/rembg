from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the front-end

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    file = request.files['image']
    input_image = Image.open(file.stream)
    
    # Remove background using rembg
    output_image = remove(input_image)
    
    # Save the output image to a BytesIO object
    img_io = BytesIO()
    output_image.save(img_io, format='PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)