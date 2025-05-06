from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello World</h1> <p>Visit <a href='/joke'>/joke</a> for a random joke</p>"

@app.route('/joke')
def joke():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
        joke_data = response.json()
        
        if response.status_code == 200 and not joke_data.get('error', False):
            return f"""
            <h1>Here's a joke for you!</h1>
            <p>{joke_data['joke']}</p>
            <p><a href='/joke'>Get another joke</a> | <a href='/'>Go home</a></p>
            """
        else:
            return "Couldn't fetch a joke. Try again later!"
    except:
        return "Joke service unavailable. Try again later!"

if __name__ == '__main__':
    app.run(debug=True)