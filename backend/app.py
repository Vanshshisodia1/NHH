from flask import Flask, request, jsonify
from ocr import digitize_prescription
from translator import translate_text
from speech_to_text import speech_to_text
from blockchain_storage import store_prescription_on_blockchain

app = Flask(__name__)

@app.route('/api/ocr', methods=['POST'])
def ocr_endpoint():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    text = digitize_prescription(file)
    return jsonify({"text": text})

@app.route('/api/translate', methods=['POST'])
def translate_endpoint():
    data = request.json
    text = data.get('text')
    target_language = data.get('language')
    if not text or not target_language:
        return jsonify({"error": "Missing parameters"}), 400
    translated_text = translate_text(text, target_language)
    return jsonify({"translated_text": translated_text})

@app.route('/api/speech-to-text', methods=['POST'])
def speech_to_text_endpoint():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    text = speech_to_text(file)
    return jsonify({"text": text})

@app.route('/api/store-prescription', methods=['POST'])
def store_prescription_endpoint():
    data = request.json
    prescription_data = data.get('prescription_data')
    if not prescription_data:
        return jsonify({"error": "No data provided"}), 400
    tx_hash = store_prescription_on_blockchain(prescription_data)
    return jsonify({"transaction_hash": tx_hash})

if __name__ == '__main__':
    app.run(debug=True)
