FROM node:16.14.2-alpine3.15

WORKDIR /app
COPY . .
RUN npm i 
RUN npm run build