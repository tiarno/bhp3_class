Black Hat Python for Python3
==============================

*Using Python to build your own hacking toolbox.*

**bhp3_class** is a repo for my interpretation and rewrite of the code in
*Black Hat Python* by Justin Seitz.  

I put all credit for the usefulness of the code to Justin.

Every programmer has a style and this rewrite from Python2 to Python3
reflects both the porting of the code to Python3 as well as my own style.

This repo is being used during the summer of 2018 as a web-based course on
hacking with Python for Raleigh ISSA.

The book *Black Hat Python* is the textbook used for the class.

I have no connection with the book except as a fan. You can see it here:
https://www.amazon.com/Black-Hat-Python-Programming-Pentesters/dp/1593275900

Comments or questions, `tim@reachtim.com`

Dependencies:

  - paramiko
  - lxml
  - requests
  - scapy

Structure of this Repository
================================

This repo is structured as follows::

    bhp3_class/
        Install.md
        README.md
        setup.py
        bhp3_class/
          areas_for_class/
          networking/
          packets/
          web/

The `areas_for_class` folder is where you'll find the class materials.
As our class goes forward, I will add updates to the corresponding subdirectories.

Our first classes will be on web hacking, so you'll find
the first class materials under the `areas_for_class/web` folder. 

The other *top-level* folders (`networking`, `packets`, and `web`)
are where you will put your own code you write for class. 

By the end of the class, you'll have your own python package named `bhp3_class` as 
your starting toolbox of Python tools for hacking.


Getting the Materials
==========================

If you have a GitHub account, fork my repo from `https://github.com/tiarno/bhp3_class.git`.
Use `git clone` to clone it in to your home directory on the machine you'll be using for class.

If you don't have a GitHub account, you can download the zip file from `https://github.com/tiarno/bhp3_class/archive/master.zip`
Unzip the file in your home directory on the machine you'll be using for class.


Preparing for class
======================
I'll be using Kali Linux with Python3.6 and the Visual Studio Code IDE.

I'll be using Git locally and updating code on GitHub as well. 

I highly recommend using Git for version control.

You can use whatever you like, but you definitely need these three things:
 - Linux-based OS
 - Python 3.x
 - a text editor or IDE.
 
 If you want to install Kali, Python3.6, and Visual Studio Code,
follow the instructions in `Install.md` in this repository.

Install Python3 packages
---------------------------

We will use the `pipenv` tool to manage our virtual environments.

- apt-get install -y python3-pip
- pip3 install pipenv
- cd bhp3_class # where you cloned or unzipped the github repo for class.
- pipenv install scapy
- pipenv install lxml
- pipenv install requests
- pipenv install paramiko
- pipenv install pylint
- pipenv install -e .
