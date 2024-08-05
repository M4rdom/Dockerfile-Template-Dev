# {{app-name}} parametro de entrada para el nombre de la app

FROM node:22

RUN npm install -g @angular/cli

RUN ng new app

WORKDIR /app

EXPOSE 4200

CMD ["ng", "serve"]

