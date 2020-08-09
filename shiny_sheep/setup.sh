#!/bin/bash

set -e

PERM_PREFIX="sudo"
if [ "$(expr substr $(uname -s) 1 5)" == "MINGW" ]; then
    echo "MinGW environment detected, not using sudo..."
    unset PERM_PREFIX
fi

echo "Installing webpack..."
$PERM_PREFIX npm install -g webpack webpack-cli

cd shiny_sheep/frontend
echo "Install frontend dependencies..."
npm install
echo "Building frontend..."
npm run dev

echo "Building docker images..."
cd ../..
docker-compose -f local.yml build
