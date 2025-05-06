from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

def get_joke(category=None):
    params = {}
    if category:
        params['category'] = category
    
    # Blacklist some categories to keep jokes clean
    params['blacklistFlags'] = 'nsfw,religious,political,racist,sexist,explicit'
    
    try:
        response = requests.get(JOKE_API_URL, params=params)
        return response.json()
    except:
        return {"error": "Failed to fetch joke"}

@app.route('/')
def home():
    # Get available categories
    categories = ["Programming", "Misc", "Pun", "Spooky", "Christmas"]
    return render_template('index.html', categories=categories)

@app.route('/get-joke/<category>')
def fetch_joke(category):
   
    joke_data = get_joke(category)
    return jsonify(joke_data)

if __name__ == '__main__':
    app.run(debug=True) 