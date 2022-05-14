import { Router } from 'express';
import { registerAnalysisRoutes } from './analysis.js';

const route = Router();

export function registerSentimentRoutes(router: Router) {
  router.use('/sentiment', route);
  
  registerAnalysisRoutes(route);
}
