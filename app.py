from flask import Flask, render_template, send_from_directory, request
import os
import socket
import urllib

raindrop = Flask(__name__)

ip = socket.gethostbyname(socket.gethostname())
response = urllib.urlopen("http://api.hostip.info/get_html.php?ip={}&position=true".format(ip)).read()
lines = response.splitlines()
location = (lines[1])[6:]
print(location)

@raindrop.route('/')
def home():

    return render_template('index.html', location=location)


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
