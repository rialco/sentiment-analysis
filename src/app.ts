import { Server } from './server.js';

export class App {
  private server?: Server;

  async start() {
    const port = process.env.PORT || '3000';
    this.server = new Server(port);
    return this.server.listen();
  }

  async stop() {
    if (this.server) {
      return this.server.stop();
    }
  }

  get httpServer() {
    if (this.server) {
      return this.server.getHttpServer();
    }
  }
}