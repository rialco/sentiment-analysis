import { Request, Response, Router } from 'express';
import { TweetFetchAnalysisController } from '../../controllers/TweetFetchAnalysisController.js';
import { TweetRequestAnalysisController } from '../../controllers/TweetRequestAnalysisController.js';

const route = Router();

export function registerAnalysisRoutes(router: Router) {
  router.use('/analysis', route);

  const tweetRequestAnalysisController = new TweetRequestAnalysisController();
  const tweetFetchAnalysisController = new TweetFetchAnalysisController();

  route.post('/:username', (req: Request, res: Response) =>
    tweetRequestAnalysisController.run(req, res),
  );

  route.get('/:subject', (req: Request, res: Response) =>
    tweetFetchAnalysisController.run(req, res),
  );
}
