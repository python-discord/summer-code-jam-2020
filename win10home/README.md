# Win10 Home Survival Kit

**tl;dr Event judges don't need to use this. It's for developer benefit.**

## Why?

We have limited time in the codejam, and the recommended ways of getting docker to work on win10 home seem to be causing issues for team members.


## What is this?

A [Vagrantfile](https://www.vagrantup.com/intro) based on [ubuntu/bionic64](https://app.vagrantup.com/ubuntu/boxes/bionic64) that tries to provide the same functionality that boot2docker used to before it was deprecated and downloads for it disabled.

Forwards the following ports:
* 8000, the port used by the django development server
* 8080, docker-cli client controlling daemon

The following software is installed:
* build tools like GCC and some helpful headers
* support for installing from repos signed with gpg keys
* stable [docker-ce](https://docs.docker.com/engine/)

## How to

### Prereqs ###
1. ~10gb free HD space
2. [Virtualbox](https://www.virtualbox.org/) installed
3. [Vagrant](https://www.vagrantup.com/downloads) installed

### 1. Install Chocolatey ###
Chocolatey is a package manager for windows. Install it by following the [guide](https://chocolatey.org/install).

### 2. Set up docker-cli ###
This a command line client that can control docker daemons. We'll be using it to control the docker daemon on another system.
First, [open a PowerShell instance as Administrator](https://miro.medium.com/max/875/1*BpqdHtStbA9r8ZTA7tlocA.png). ([source article](https://medium.com/@remisharoon/the-smartest-way-to-run-docker-on-windows-10-home-441c4dd215d), don't follow its instructions, they don't work due to Boot2Docker no longer being served from github.)
Install it as follows:
```
choco install docker-cli -y
```

### 3. Set up the VM ###
2. Edit the RAM field in the Vagrantfile to fit inside your system's RAM size
3. cd to the directory where you put the Vagrantfile in cmd or powershell
4. vagrant up
6. Find the GUI window for the VM or bring it up in VirtualBox
6. login with vagrant/vagrant

The local directory should now be mounted at /vagrant in the virtual machine.
