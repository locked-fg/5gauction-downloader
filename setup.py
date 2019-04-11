from setuptools import setup

setup(
   name='onedrive',
   version='1',
   description='5G Auction Downloader',
   author='Franz',
   author_email='code@locked.de',
   packages=['auction'],
   install_requires=['requests', 'beautifulsoup4']
)
