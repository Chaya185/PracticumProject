from flask import render_template
from flask import Flask
import random


app = Flask(__name__)

def getRandomNumber():
    # Generate a random integer between 0 and 100 (inclusive)
    random_number = random.randint(0, 100)
    print("Random number:", random_number)

    # Generate a random float between 0 and 1
    #random_float = random.random()
    #print("Random float:", random_float)
    random_number_str = str(random_number)
    return random_number_str


@app.route('/')
def index():
    user = {'username': 'Chayki'}
    return render_template('index.html', title = 'Home', user = user, randomnumber= getRandomNumber())










