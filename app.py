from flask import Flask, render_template

raindrop = Flask(__name__)

@raindrop.route('/')
def home():

    return render_template('index.html')

if __name__ == "__main__":

	  raindrop.run(port=8000)
