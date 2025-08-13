from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for front-end integration

@app.route('/test', methods=['GET'])
def test():
    return {"message": "Flask app is running!"}

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400
    
    file = request.files['image']
    try:
        input_image = Image.open(file.stream)
        # Remove background using rembg
        output_image = remove(input_image)
        # Save output to BytesIO
        img_io = BytesIO()
        output_image.save(img_io, format='PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)