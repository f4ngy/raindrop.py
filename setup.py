from setuptools import setup

setup(
	name = 'raindrop.py',
	version = '0.1',
	packages = ['raindrop'],
	description = "Ambient music based on the current weather",
	long_description = "A python/flask application that will play ambient music based on your current weather. The project does not come with music, as the user will set the ambient music tracks themselves. Music files need to be in .mp3 format.",
	include_package_data = True,
	zip_safe = False,
	scripts = [ "raindrop/bin/raindrop" ],
	install_requires = [
		'flask',
		'requests'
	]
)
