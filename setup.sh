#!/bin/bash

cd shiny_sheep/frontend
npm install
npm run dev

docker-compose -f local.yml build
