FROM node:16.15.0-alpine3.15

ENV DATABASE_URL=postgres://pf:pf@postgres:5432/sentiments

WORKDIR /app
COPY . .
RUN npm install -g npm@8.10.0
RUN npm install 
COPY modules_fix/runner.js ./node_modules/node-pg-migrate/dist/runner.js
RUN npm run build
COPY twitter-response.json /app/dist/src/contexts/tweets/application/twitter-response.json