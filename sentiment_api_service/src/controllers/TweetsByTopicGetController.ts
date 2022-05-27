import { Request, Response } from 'express';
import { getTweetsByTopicFromTwitter } from '../contexts/tweets/application/TweetsInteractor.js';

import { Controller } from './Controller.js';

export class TweetsByTopicGetController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    try {
      const { hashtag } = req.params;
      const { nextToken } = req.query;
      const result = await getTweetsByTopicFromTwitter(
        hashtag,
        nextToken as string,
      );
      res.send(result);
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets');
    }
  }
}
