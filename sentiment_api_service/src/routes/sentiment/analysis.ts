import { Request, Response, Router } from 'express';
import { TweetAnalysisController } from '../../controllers/TweetAnalysisController.js';

const route = Router();

export function registerAnalysisRoutes(router: Router) {
  router.use('/analysis', route);

  const tweetAnalysisController = new TweetAnalysisController();

  route.post('/:username', (req: Request, res: Response) => tweetAnalysisController.run(req, res));
}
