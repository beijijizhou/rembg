from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for front-end integration

@app.route('/test', methods=['GET'])
def test():
    return {"message": "Flask app is running!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)