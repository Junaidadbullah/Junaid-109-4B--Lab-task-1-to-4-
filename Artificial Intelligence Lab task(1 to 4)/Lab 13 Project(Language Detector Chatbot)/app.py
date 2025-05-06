from flask import Flask, render_template, request, jsonify
from langdetect import detect, DetectorFactory
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from datetime import datetime
import csv
import os


DetectorFactory.seed = 0


nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)


try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')


os.makedirs('data', exist_ok=True)
if not os.path.exists('data/chat_logs.csv'):
    with open('data/chat_logs.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'user_message', 'detected_language', 'bot_response'])

def process_text(text):
    try:
        
        tokens = word_tokenize(text)
        
        stop_words = set(stopwords.words('english'))
        tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
        return tokens
    except Exception as e:
        print(f"Error processing text: {e}")
        return []

def get_response(lang):
    responses = {
        'en': "I detected English! ",
        'es': "¡Detecté español!",
        'fr': "J'ai détecté le français ! ",
        'de': "Ich habe Deutsch erkannt!",
        'it': "Ho rilevato l'italiano! ",
        'pt': "Detectei português! ",
        'ur': "میں نے اردو کا پتہ لگایا ",
        'ar': "لقد اكتشفت اللغة العربية",
        'default': "I detected a different language!"
    }
    return responses.get(lang, responses['default'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_language():
    data = request.get_json()
    message = data.get('message', '')
    
    if not message or len(message.strip()) < 3:
        return jsonify({'error': 'Message too short for language detection'}), 400
    
    try:
        
        detected_lang = detect(message) 
        print(f"Debug: Message: '{message}', Detected Language: {detected_lang}")   
        processed_tokens = process_text(message)   
        response = get_response(detected_lang)  
        with open('data/chat_logs.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                           message, detected_lang, response])
        return jsonify({
            'language': detected_lang,
            'response': response,
            'processed_tokens': processed_tokens
        })
    
    except Exception as e:
        print(f"Error in detection: {e}")
        return jsonify({'error': f"Language detection failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)