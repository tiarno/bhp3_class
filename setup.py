import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bhp3_class",
    version = "1.0.0",
    author = "Tim Arnold",
    author_email = "tim@reachtim.com",
    description = ("Class material for Raleigh ISSA web course inspired by the book 'Black Hat Python' by Jason Seitz"),
    license = "MIT",
    keywords = "hack sniff python blackhat",
    url = "http://packages.python.org/bhp3_class",
    packages=['bhp3_class', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)