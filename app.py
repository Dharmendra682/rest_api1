from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

# Initialize the Flask application
app = Flask(__name__)

# Initialize the translator
translator = Translator()

# Define a route for the translate endpoint
@app.route('/translate', methods=['POST'])
def translate_text():
    # Check if the request contains JSON data
    if not request.is_json:
        # If not, return an error response
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Get the JSON data from the request body
    data = request.get_json()
    
    # Check if the 'text' key is present in the JSON data
    if 'text' not in data:
        # If not, return an error response
        return jsonify({"error": "Missing 'text' in request body"}), 400
    
    # Get the text to be translated
    text = data['text']
    
    try:
        # Perform the translation from English to French
        translation = translator.translate(text, src='en', dest='fr')
        # Return the translated text in a JSON response
        return jsonify({"translation": translation.text}), 200
    except Exception as e:
        # If an error occurs, return an error response with the exception message
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)
