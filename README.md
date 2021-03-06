raindrop.py
===========

A python/flask application that will play ambient music based on your current weather. The project does not come with music, as the user will set the ambient music tracks themselves. Music files need to be in .mp3 format. Instructions on adding music can be found below.

Installing
===========

Either run

    $ pip install raindrop.py
  
or 

    $ git clone https://github.com/lle6138/raindrop.py.git
    $ cd raindrop.py
    $ python setup.py install
    

Contributing
===========

Clone the repo and submit a pull request.

Adding/Changing Audio
===========

When a new weather condition is encountered when the app is running, it will automatically appear on the website and you can drag a file to it. If an audio file has been set previously, you can do this to change the audio as well.

To manually add additional weather types, find the name on https://developer.yahoo.com/weather/#codes and add it to the conditions list in index.html, then run the application and drag the mp3 onto the new button on the site.

So you have the option of declaring weather conditions ahead of time, or waiting until they occur and letting the application add it for you. 
