#!/bin/bash

set -e

echo "Installing webpack..."
sudo npm install -g webpack webpack-cli 

cd shiny_sheep/frontend
echo "Install frontend dependencies..."
npm install
echo "Building frontend..."
npm run dev

echo "Building docker images..."
cd ../..
docker-compose -f local.yml build
