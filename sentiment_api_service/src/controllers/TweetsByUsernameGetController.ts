import { Request, Response } from 'express';
import { getTweetsByUsernameFromTwitter } from '../contexts/tweets/application/TweetsInteractor.js';

import { Controller } from './Controller.js';

export class TweetsByUsernameGetController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    try {
      const { username } = req.params;
      const { nextToken } = req.query;
      const result = await getTweetsByUsernameFromTwitter(
        username,
        nextToken as string,
      );
      res.send(result);
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets');
    }
  }
}
