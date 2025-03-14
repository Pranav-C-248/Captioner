from flask import Flask, request, jsonify, send_from_directory
import os
import requests
from dotenv import dotenv_values

app = Flask(__name__, static_folder="../frontend", static_url_path="")
key = dotenv_values(".envv")


# API Endpoint for caption generation
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
HEADERS = {"Authorization": f"Bearer {"key"}

@app.route("/")
def serve_frontend():
    return send_from_directory("../frontend", "index.html")

@app.route("/generate_caption", methods=["POST"])
def generate_caption():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_data = image.read()

    response = requests.post(API_URL, headers=HEADERS, files={"file": image_data})
    
    if response.status_code == 200:
        caption = response.json()[0]["generated_text"]
        print(caption)
        return jsonify({"caption": caption})
    
    return jsonify({"error": "Failed to generate caption"}), 500

if __name__ == "__main__":
    app.run(debug=True)
