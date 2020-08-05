# Win10 Home Survival Kit

**tl;dr Event judges don't need to use this. It's for developer benefit.**

## Why?

We have limited time in the codejam, so we'd rather try to deal with familiar technology wherever possible.  Consider:
* None of us are familiar with WSL2 or windows development quirks with docker
* Most of the team is familiar with Linux and VirtualBox
* One member of the team had issues with WSL2 and the version of docker desktop that supports win10 home

## What is this?

A [Vagrantfile](https://www.vagrantup.com/intro) based on [ubuntu/bionic64](https://app.vagrantup.com/ubuntu/boxes/bionic64) that tries to provide reasonable pre-installed defaults
for working on win10 home without using WSL.
The following settings are automatically changed for the user:
* Forwards 8000, the port used by the django development server
* Sets a more reasonable amount of Video Ram & enables 3d acceleration in hopes of better video performance.

The following software is installed:
* build tools like GCC and some helpful headers
* support for installing from repos signed with gpg keys
* The latest stable [nodejs](https://nodejs.org/en/)
* stable [docker-ce](https://docs.docker.com/engine/)
* [git](https://git-scm.com/)
* [Google Chrome](https://www.google.com/chrome/)
* [Visual Studio Code](https://code.visualstudio.com/)
* lubuntu-desktop, an [LXDE](https://en.wikipedia.org/wiki/LXDE) package that also sets up an X server.

## How to

### Prereqs ###
1. ~10gb free HD space
2. [Virtualbox](https://www.virtualbox.org/) installed
3. [Vagrant](https://www.vagrantup.com/downloads) installed

You may need to restart cmd/powershell after installing these and possibly the system as well.

### Set up the VM ###
1. This file should be in a directory of your choice
2. Edit the RAM field in the Vagrantfile to fit inside your system's RAM size
3. cd to the directory where you put the Vagrantfile in cmd or powershell
4. vagrant up
5. wait ~20 minutes, this will install a ton of stuff & restart the system
6. Find the GUI window for the VM or bring it up in VirtualBox
6. login with vagrant/vagrant

The local directory should now be mounted at /vagrant in the virtual machine.
