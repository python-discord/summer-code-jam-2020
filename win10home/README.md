# Vagrant Devoplement Guide
Provides a linux VM to allow a Windows 10 Home user to develop some what seemlessly. 

## What is this?
A [Vagrantfile](https://www.vagrantup.com/intro) based on [ubuntu/bionic64](https://app.vagrantup.com/ubuntu/boxes/bionic64) that tries to provide the same functionality that boot2docker used to before it was deprecated and downloads for it disabled.

### Prerequisites ###
1. Minimum 5GB of free disk space
2. [Virtualbox](https://www.virtualbox.org/) installed
3. [Vagrant](https://www.vagrantup.com/downloads) installed

### Usage
Open cmd and run 
```
vargant up
vargrant ssh
cd /vagrant
run.sh
```

After a little you should be able to go [http://127.0.0.1:8000](http://127.0.0.1:8000) and see the webapp.
