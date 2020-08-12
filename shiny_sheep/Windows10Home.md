# Docker Toolbox Development Guide
*(aka How To Survive Windows 10 Home When WSL2 Won't @#&!ing Work)*

## Who should use this?
Ideally, nobody. Don't run this if you can use the normal WSL2 way. It's meant
for team members stuck on Windows 10 Home and having trouble with WSL & Docker.

It uses unmaintained software that may conflict with Win10's normal Hyper-V 
hypervisor. It (probably) won't break anything other than itself if you try to
run it when WSL2 & Hyper-V are enabled, but that hasn't and won't be tested. 
¯\_(ツ)_/¯

## Usage

### Getting Work Done

The good news is that changes to the project directory will cause the django server
to shut down and reload. This should take a second or two at most.

However, if you want to have syntax completion and other nice things in your
IDE, you'll need to have a local python environment with all the packages 
installed as well as the docker images. It's not great, but it works.

#### Quickstart terminal, not CMD or Powershell
It will install a terminal shortcut on your desktop that you'll use for 
accessing docker. The terminal uses MINGW and it's a unix/linux emulator
userspace emulator for windows. Stuff like sed and awk should be there.

Don't use CMD and powershell to try to interact with docker. There might
be a way that to use them. I might have seen one mentioned for a fraction
 of a second on first launch, but:
* the MINGW-based quickstart terminal seems to work reliably
* the screen cleared quickly
* it's buried somewhere in the documentation
* we don't have time to mess with configs anymore

#### Docker-machine ip, NOT localhost
This method uses bridged networking to assign a new LAN IP address to your VM,
and yes it's accessible on the network.

**You can't use localhost, you have to fetch the IP to access it as follows:**

    $docker-machine ip default
    192.168.1.100

#### How do I connect my debugger to this?
I don't know yet. At the moment, you still have django error reporting to help
you. 

There might be a way to get VSCode to connect to it. If we can't do that, maybe
ask our team leader to offer an SQLite config option for the db and run
redis/etc inside docker? 

It's better than where we were before though. 

#### ^M in logs: Resolving an Issue People Had in the Past

This might show up if you edit a script that runs inside a container rather 
than inside the MINGW quickstart terminal.

`^M` at the end of line in the output means that there are windows-style line
endings in the shell scripts. For example, it may look like this:
```
    default: Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
    default: Executing: /lib/systemd/systemd-sysv-install enable docker
    default: /tmp/vagrant-shell: ./setup.sh: /bin/bash^M: bad interpreter: No such file or directory
```
If you get something like this, try running the following on the named file
from the MINGW quickstart terminal, not :

    sed -i -e 's/\r$//' start.sh

Then resume running whatever script you were trying to run.

### Installing
 
#### Prerequisites
- Minimum 2GB of free disk space, and quite possibly a lot more.
- A recent [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- Git for windows
- A recent Nodejs & NPM installed locally
- Have admin rights on Windows.
- Have run `git config --local core.autocrlf input` in this directory.

Setting `autocrlf` to `input` is important because it will remove windows-style
 line breaks that are introduced when committing, but never add them into source.

This will ensure that scripts work by default unless you change them.

#### 1. Download, but don't run the installer yet 
**You probably won't be using the standard install procedure. Download it and
 keep the guide link below as reference**

* [Install Guide for reference](https://docs.docker.com/toolbox/toolbox_install_windows/)
* [Docker Toolbox Download link](https://github.com/docker/toolbox/releases/download/v19.03.1/DockerToolbox-19.03.1.exe)

This is old and unmaintained, but it has the important parts:
* it still seems to work
* it mounts things in predictable places

I've tested it. It (mostly) builds and launches the docker compose folder, with
some Django permissions errors. You might be able to fix that yourself by
googling.

#### 2. Uncheck VirtualBox and Git for Windows when you run the installer

You should have already installed a recent Virtualbox and git for windows. 
Uncheck the boxes for those when you get there. You don't need to install
them again.

#### 3. Enable Symlinks (?)

**You might not need to do this but the author has it enabled and it works.**

Given how little time we have, you might want to do this too rather than test
different configurations.

You can either give all users the ability to create symlinks, or only yourself.
Granting to all members of the Users group seems to work best. Some users have
 reported trouble when they granted it only to themselves.
  
 The following instructions are an expanded version of
[this stack overflow response](https://superuser.com/questions/124679/how-do-i-create-a-link-in-windows-7-home-premium-as-a-regular-user/148926#148926).

To grant all members of the Users group permission to create symlinks, do the following:
1. run `secpol.msc`
2. In the lefth-and panel, choose **Local Policies** > **User Rights Assignment**
3. In the right-hand list, find Create Symbolic Links
4. Double-click it
5. In the **Enter the object names to select** text box at the bottom, type `Users`
6. Click the **Check Names** button to the right
7. A **Name Not Found** box should pop up.
8. Click the **Object Types** button
9. In the dialog that pops up, check the box for **Groups**
10. Click **OK** to close the **Object Types** dialog
11. Click **OK** to close the **Name Not Found** dialog and search
12. The group should be auto-entered in the form `HOSTNAME\Users`
13. Click **OK** on the **Add User Or Group** dialog.
14. Click **Apply** and close the **Create Symbolic Link Properties** dialog.
15. Close any remaining dialogs and the security policy editor.

If you **really** want to try granting only yourself permissions, try entering
your account name alone instead before pressing **Check Names**. Note that some
 people may have issues with this. I'm not familiar enough with windows to tell
 you why.

#### 4. Build your images

In the quickstart terminal, run `./setup.sh`. It will build the frontend JS. You
need to run this if you alter JS or update it from git.

#### 5. Start the server

`./run.sh` or if you want to manually run docker-compose:

    docker-compose -f local.yaml

It may take a while to build the first time. Once it does, you should be able
to use `docker-machine ip` to get the LAN address of your server. Go to 
`http://dockermachineip_output:8000` to see the site.
