
## Kali. 
I'm using a virtual machine for Kali. If you already have Kali, skip this step.

I already have VirtualBox installed. You can use VMWare or VirtualBox.
If you don't have either, you can download VirtualBox here:
https://www.virtualbox.org/wiki/Downloads

First, download the Kali image for your machine: this will take a while.
I'm downloading the kali-linux-2018.1-amd64.iso image from here:
http://www.kali.org/downloads/

This online guide isn't too annoying. Toward the end, say yes to the network mirror.
https://geekviews.tech/how-to-install-kali-linux-on-virtualbox/

- login as root
- apt-get update
- apt-get -y upgrade # this takes a while
    (I had to remove a couple of lock files to do that last one.)

Once this is finished, you should get something like this when you give
the command 'python3'::

    Python 3.6.5rc1 (default Mar 14 2018, 06:54:23)
    [GCC 7.3.0] on linux
    Type "help", "copyright", "credits", or "license" for more information.

## Install Visual Studio code

Download the *.deb file into your Kali machine from here and follow their instructions:
https://code.visualstudio.com/docs/setup/linux

- sudo dpkg -i `filename`.deb
- sudo apt-get install -f
- curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
- sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
- sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

- sudo apt-get update
- sudo apt-get install code


## Create a normal user.
See this page for details: https://debian-administration.org/article/2/Adding_new_users

## Finally

- login as that user
- cd bhp3_class/bhp3_class # where you cloned or unzipped the github repo for class.
- code

The bhp3_class directory will be our working directory for class.
