from distutils.core import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="ttspy",
    version="1.0",
    decription="Multi-platform Text-To-Speech module based on Google Translate engine",
    long_description=long_description,
    author="Robin David",
    author_email="dev.robin.david@gmail.com",
    license="LGPL",
    url="https://github.com/RobinDavid/pytts",
    packages=['pytts'],
    package_dir={"pytts":"."},
    py_modules=['gst','gobject','urllib2'])
