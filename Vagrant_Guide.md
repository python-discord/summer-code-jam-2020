# Vagrant Devoplement Guide
Provides a linux VM to allow a Windows 10 Home user to develop some what seemlessly.

### Prerequisites
- Minimum 2GB of free disk space
- [Virtualbox](https://www.virtualbox.org/) installed
- [Vagrant](https://www.vagrantup.com/downloads) installed
- You have permission to create symlinks. [Here](https://superuser.com/a/125981) is guide to get this permission. 

### Usage
Open cmd and run 
```
cd $PROJECT_DIR
vargant up
vargrant ssh
cd /vagrant
run.sh
```

After a little you should be able to go [http://127.0.0.1:8000](http://127.0.0.1:8000) and see the webapp.
