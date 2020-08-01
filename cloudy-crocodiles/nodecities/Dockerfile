# Current version. See the following:
# https://nodejs.org/en/about/releases/
ARG NODE_VERSION=node:14-buster

ARG NGINX_VERSION=nginx:1.18-alpine

## Base image for dev and build stages
FROM ${NODE_VERSION} AS quasar-base
RUN npm install -g @quasar/cli
RUN mkdir /nodecities && chown -R node /nodecities/
USER node
WORKDIR /nodecities/


## Development stage
FROM quasar-base AS quasar-dev
# Temporary entrypoint to allow me to docker exec bash and start a quasar app
ENTRYPOINT ["sleep", "1000000000"]
# ENTRYPOINT ["quasar", "dev"]
