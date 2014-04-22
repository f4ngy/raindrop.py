from flask import Flask, render_template, send_from_directory, request
import os
import glob
import requests
raindrop = Flask(__name__)

ip = requests.get('http://canihazip.com/s').text
geo = requests.get('http://freegeoip.net/json/'+ip).json()

@raindrop.route('/')
def home():

    conditions = [condition.replace('sounds/','').replace('.mp3', '') for condition in glob.glob('sounds/*.mp3')]

    return render_template('index.html', location=geo['city']+', '+geo['region_code'], conditions=conditions)


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
