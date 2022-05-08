import { Router } from 'express';
import { registerSentimentRoutes } from './sentiment/index.js';

export function registerRoutes(router: Router) {
  registerSentimentRoutes(router);
}
