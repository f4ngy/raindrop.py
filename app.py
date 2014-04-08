from flask import Flask, render_template, send_from_directory, request
import os

raindrop = Flask(__name__)

@raindrop.route('/')
def home():

    return render_template('index.html')


@raindrop.route('/stream/<condition>', methods=['GET', 'POST'])
def stream(condition):

    if request.method == 'GET':

        return send_from_directory('sounds', condition + '.mp3')

    elif request.method == 'POST':

        file = request.files['clip']

        if file:

            file.save(os.path.join('sounds', condition + '.mp3'))

        return ''


if __name__ == "__main__":

	  raindrop.run(port=8000)
