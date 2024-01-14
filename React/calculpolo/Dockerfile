## Fichier : ./react-docker/Dockerfile
FROM node:18.10.0-alpine3.15

WORKDIR /React/calculpolo

COPY package*.json ./
COPY . ./

RUN npm install
RUN npm install axios
EXPOSE 3000

CMD ["npm", "start"]