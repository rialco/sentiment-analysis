import { Request, Response, Router } from 'express';

import { TweetsByTopicGetController } from '../../controllers/TweetsByTopicGetController.js';
import { TweetsByUsernameGetController } from '../../controllers/TweetsByUsernameGetController.js';

const route = Router();

export function registerTweetsRoutes(router: Router) {
  router.use('/tweets', route);

  const tweetsByUserGetController = new TweetsByUsernameGetController();
  const tweetsByTopicGetController = new TweetsByTopicGetController();

  route.get('/topic/:hashtag', (req: Request, res: Response) => tweetsByTopicGetController.run(req, res));

  route.get('/user/:username', (req: Request, res: Response) => tweetsByUserGetController.run(req, res));
}
