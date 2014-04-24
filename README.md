raindrop.py
===========

A python/flask application that will play ambient music based on your current weather. Music files need to be in .mp3 format.

Default tracks used under Creative Commons, created by Matti Paalanen (http://www.mattipaalanen.com/projects.html)

To change the song that is used for a certain weather type, run the application and open the site.  Drag your audio file onto the button with the name of the weather type you're targeting. 

To add additional weather types, find the name on https://developer.yahoo.com/weather/#codes and add it to the conditions list in index.html, then run the application and drag the mp3 onto the new button on the site.

Alternatively, if a new weather condition is encountered when the app is running, it will automatically appear on the website and you can drag a file to it. So you have the option of declaring weather conditions ahead of time, or waiting until they occur and letting the application add it for you. 
