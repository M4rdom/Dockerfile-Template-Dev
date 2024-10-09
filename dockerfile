# ------------------ Build Stage -----------------------#

# Angular Aplication Dockerfile

# Avoid using latest tag in production
FROM node:latest AS build 

WORKDIR /app/

COPY package*.json ./ 

RUN --mount=type=cache,target=/root/.npm npm install \
    npm run build --prod

COPY . .

RUN npm run build --prod
# ------------------ Production Stage ------------------#

# Nginx WebServer Dockerfile

# Avoid using latest tag in production
FROM nginx:latest AS prod 

COPY --from=build /app/dist/autodocker/browser /usr/share/nginx/html/

EXPOSE 80
