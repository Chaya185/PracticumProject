from flask import render_template, Flask
import requests

app = Flask(__name__)

def getRandomWord():
    # Make a GET request to the Random Word API
    response = requests.get("https://random-word-api.herokuapp.com/word")
    
    # Parse JSON response
    word = response.json()[0]
    return word

@app.route('/')
def index():
    user = {'username': 'Rivka & Chayki'}
    random_word = getRandomWord()
    return render_template('index.html', title='Home', user=user, random_word=random_word)

if __name__ == '__main__':
    app.run(debug=True)
