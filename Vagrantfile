# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile hacked together to give a current Docker version since
# boot2docker, the last Windows 10 option that worked cleanly with
# Home Edition, was deprecated a while ago. Based on default config file
# and configuration options found on blogs and stack overflow.
#
# Don't change "2", it's the Vagrantfile version specifier.
Vagrant.configure("2") do |config|
  # Official vagrant 
  # https://docs.vagrantup.com.

  # based off of the official ubuntu vagrant base box.
  config.vm.box = "ubuntu/bionic64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Forward 8000 so we can see django from outside the VM
  config.vm.network "forwarded_port", guest: 8000, host: 8000 # Django server

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096" #4 GB ram
    vb.customize ["modifyvm", :id, "--cpus", "2"] # use 2 cpu cores
  end

$toinstall = <<-SHELL
# update apt & upgrade packages
sudo apt-get update && sudo apt-get upgrade -y

# Setup APT for Nodejs 
curl -sL https://rpm.nodesource.com/setup_lts.x | sudo bash -

# Docker Setup
sudo apt remove docker docker-engine docker.io
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update

sudo apt install -y docker-ce nodejs npm python3-pip

# Install docker-compose using pip
sudo pip3 install docker-compose

sudo systemctl enable docker
sudo systemctl start docker

sudo usermod -aG docker $USER
newgrp docker

# dirty hack to deal with windows clobbering line endings in shellscripts,
# also do something useful while we wait for docker to start up
sudo apt-get install -y dos2unix

echo "Waiting for Docker to start..."
while [ ! -e /var/run/docker.sock ]; do sleep 1; done
echo "Done."

cd /vagrant
./setup.sh

SHELL
	#actually run the above script during provisioning.
config.vm.provision "shell", inline: $toinstall, privileged: false

  # shouldn't need to do this, it should auto-mount the local
  # directory to /vagrant
  # config.vm.synced_folder "./", "/shinysheep"
  
end
