import express, { Express, Request, Response, Router } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import helmet from 'helmet';
import * as http from 'http';
import httpStatus from 'http-status';
import { registerRoutes } from './routes/index.js';

export class Server {
  private express: Express;
  private port: string;
  private httpServer?: http.Server;
  // Sets the CORS options
  // 1. Enable the use of credentials/authorization in the Header
  // 2. Sets from which endpoints the request can be made
  private corsOptions = {
    credentials: true,
    origin: process.env.INCOMING_URL || '*',
  };

  constructor(port: string) {
    dotenv.config();
    this.port = port;
    this.express = express();
    this.express.use(helmet());

    this.express.use(cors(this.corsOptions));
    this.express.use(express.json());
    this.express.use(express.urlencoded({ extended: true }));
    const router = Router();

    this.express.use(router);
    registerRoutes(router);

    // Catch not defined routes
    this.express.use((req: Request, res: Response) => {
      res.status(httpStatus.NOT_FOUND).json('Not found');
    });

    // Catch server related errors
    this.express.use((err: Error, req: Request, res: Response) => {
      res.status(httpStatus.INTERNAL_SERVER_ERROR).send(err.message);
    });
  }

  async listen(): Promise<void> {
    return new Promise((resolve) => {
      this.httpServer = this.express.listen(this.port, () => {
        console.log(`Server listening on port ${this.port}`);
        resolve();
      });
    });
  }

  getHttpServer() {
    return this.httpServer;
  }

  async stop(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (this.httpServer) {
        this.httpServer.close((err) => {
          if (err) {
            return reject();
          }
          return resolve();
        });
      }
      // There is no http server to close.
      return resolve();
    });
  }
}
