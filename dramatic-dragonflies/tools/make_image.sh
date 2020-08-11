#!/usr/bin/env bash

ROOT="/rom"
set -e

mkdir $ROOT

mkdir -pv /mnt/iso
mount -o loop ./arch.iso /mnt/iso
cp -r /mnt/iso/* $ROOT/

rm -v $ROOT/var
mkdir -pv $ROOT/var/lib/pacman
touch $ROOT/var/lib/pacman/pacman.db

cd $ROOT/arch
sed 's/pacman -A -r/pacman -A -r -f/' ./installworld > /dev/null

OLD_PATH=$PATH
PATH=$ROOT/usr/bin:$PATH

echo "> Installing system"
./installworld $ROOT > /dev/null

PATH=$OLD_PATH

cat > $ROOT/etc/resolv.conf << EOL
nameserver 8.8.8.8
nameserver 8.8.4.4
EOL

echo "> Creating artifact"
tar -czf /rom.tar.gz $ROOT
