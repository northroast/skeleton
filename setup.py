try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	"description": "Guru",
	"author": "Rich",
	"url": "www.northroast.com",
	"download_url": "localhost",
	"author_email": "northroast@icloud.com",
	"version": "0.1",
	"install_requires": ["nose"],
	"package": ["NAME"],
	"scripts": [],
	"name": "projectname"
}

setup(**config)