from setuptools import setup, find_packages
setup(
    url = "http://www.pybeat.org",
    name = "PyBeat",
    version = "0.1",
    packages = ['pybeat'],
    package_dir = {'pybeat': 'pybeat'},
    scripts = ['pybeat-server.py', 'pybeat-client.py'],
    author = "Christian Joergensen",
    author_email = "christian.joergensen@gmta.info",
    description = "A light-weight streaming server for MP3 and OGG files.",
    long_description = "This is a very light-weight streaming server for MP3 and OGG files designed to work in environments where resources are limited.",
    license = "",
    keywords = "mp3 ogg streaming",
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Multimedia :: Sound/Audio']
)
