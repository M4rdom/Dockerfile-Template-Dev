# ------------------ Build Stage -----------------------#

# Angular Aplication Dockerfile

FROM node:latest AS build

WORKDIR /app/

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build --prod
# ------------------ Production Stage ------------------#

# Nginx WebServer Dockerfile

FROM nginx AS prod

COPY --from=build /app/dist/angular-conduit/ /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80


