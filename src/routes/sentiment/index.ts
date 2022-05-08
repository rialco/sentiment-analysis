import { Router } from 'express';
import { registerAnalysisRoutes } from './analysis.js';
import { registerTweetsRoutes } from './tweets.js';

const route = Router();

export function registerSentimentRoutes(router: Router) {
  router.use('/sentiment', route);
  
  registerTweetsRoutes(route);
  registerAnalysisRoutes(route);
}
