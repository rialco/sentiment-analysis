import { App } from './app.js';

try {
  new App().start();
} catch (error) {
  console.log("App didn't start");
  process.exit(1);
}

process.on('uncaughtException', (err) => {
  console.log('uncaught exception', err);
  process.exit(1);
});
