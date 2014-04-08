from flask import Flask, render_template, send_from_directory

raindrop = Flask(__name__)

@raindrop.route('/')
def home():

    return render_template('index.html')


@raindrop.route('/stream/<condition>')
def stream(condition):

    return send_from_directory('sounds', condition + '.mp3')

if __name__ == "__main__":

	  raindrop.run(port=8000)
