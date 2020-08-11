# FROM node:14-alpine as builder

# # install and cache app dependencies
# COPY frontend/code-jam/package.json frontend/code-jam/package-lock.json ./
# RUN npm install && mkdir /frontend && mv ./node_modules ./frontend && mv package.json ./frontend && mv package-lock.json ./frontend

# WORKDIR /frontend

# COPY . .

# RUN npm run build



# # ------------------------------------------------------
# # Production Build
# # ------------------------------------------------------
# FROM nginx:1.16.0-alpine
# COPY --from=builder /frontend/build /usr/share/nginx/html
# RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx/nginx.conf /etc/nginx/conf.d
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]


# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:14-alpine as build-stage
WORKDIR /app
COPY frontend/code-jam/package*.json /app/
RUN npm install
COPY ./frontend/code-jam/ /app/
ARG configuration=production
RUN npm run build -- --output-path=./dist/out --configuration $configuration
# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15

COPY --from=build-stage /app/dist/out/ /usr/share/nginx/html
# Copy the default nginx.conf provided by tiangolo/node-frontend
RUN rm /etc/nginx/conf.d/default.conf
COPY frontend/nginx.conf /etc/nginx/conf.d

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME