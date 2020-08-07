# Vagrant Development Guide
*(aka How To Survive Windows 10 Home when WSL breaks)*

Judges probably don't need this. It's meant for team members stuck on Windows 10 Home and having trouble
with WSL & Docker.

## Prerequisites
- Minimum 2GB of free disk space, and quite possibly a lot more.
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads) installed
- [Vagrant](https://www.vagrantup.com/downloads) installed
- Have admin rights on Windows.
- Have run `git config --local core.autocrlf input` in this directory.

Setting `autocrlf` to `input` is important because it will remove windows-style line breaks
that are introduced when committing, but never add them into source.

This will ensure that scripts work by default unless you change them.

**You may need to run dos2unix on any shell script you change from inside the VM.**

## Usage 

### 1. Enable Symlinks
#### 1.1 Install Group Policy Editor 
Download **and read** [this installer batch file](https://www.majorgeeks.com/mg/getmirror/add_gpedit_msc_with_powershell,1.html)
 from majorgeeks.
Its contents should read as follows:
```bat
@echo off 
@echo "This batch file from MajorGeeks.Com will enable Group Policy Editor (Gpedit.msc) on Windows 10 Home."
@echo "If this method fails, there are other methods to try at https://tinyurl.com/majorgeeksgpedit"
pushd "%~dp0" 

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt 
dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt 

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i" 
pause
```
It appears to read a list of packages related to group policy extensions into a list, then install all of them.
If the contents match the above, run it as administrator.

#### 1.2 Enable Symlinks 

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

If you want to try granting only yourself permissions, try entering your account
 name alone instead before pressing **Check Names**. Note that some people may have
 issues with this. I'm not familiar enough with windows to tell you why.

### 2. Set up VM
Open cmd and run 
```
cd $PROJECT_DIR
vagrant up
```
If all goes well, you should return to a prompt with no errors. 

#### 2.1 ^M in logs

`^M` at the end of line in the output means that there are windows-style line endings in the shell scripts.
For example, it may look like this:
```
    default: Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
    default: Executing: /lib/systemd/systemd-sysv-install enable docker
    default: /tmp/vagrant-shell: ./setup.sh: /bin/bash^M: bad interpreter: No such file or directory
```
If you get something like this, enter the VM with `vagrant ssh` and run the following:

    cd /vagrant
    dos2unix setup.sh run.sh

Then resume running whatever script you were trying to run. If you edit the scripts, you may need to run `dos2unix` on them from within the VM to make sure
that there are unix-style line endings rather than windows ones.

#### 2.2 Docker daemon not found
This may happen during setup. If it does, reboot the machine with `vagrant reload` on the host.
Afterwards, you can `vagrant ssh` and re-run the interrupted script.

### 3. Running the development server
All you need to do is use `run.sh`. It will run all dependency containers such as databases and queues.
```
vagrant ssh
cd /vagrant
run.sh
```
It may take a while to build the first time. Once it does, you should be able to go to
 [http://127.0.0.1:8000](http://127.0.0.1:8000) on your host system and see the webapp.
 
 Changes to the project directory will cause the django server to shut down and reload.
 This should take a second or two at most.

As with `setup.sh`,  you can use `dos2unix run.sh` if you get an error mentioning `^M` at the end of a line,

For now, `run.sh` is only `docker-compose -f local.yml up`, so you can use that instead if you want.

