import { Router } from 'express';
import { registerSentimentRoutes } from './sentiment/index.js';
import { registerTweetsRoutes } from './tweets/index.js';

export function registerRoutes(router: Router) {
  registerSentimentRoutes(router);
  registerTweetsRoutes(router);
}
