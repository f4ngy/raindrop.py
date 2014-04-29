from setuptools import setup

setup(
	name = 'raindrop.py',
	version = '0.1',
	packages = ['raindrop'],
	include_package_data = True,
	zip_safe = False,
	install_requires = [
		'flask',
		'requests'
	]
)
