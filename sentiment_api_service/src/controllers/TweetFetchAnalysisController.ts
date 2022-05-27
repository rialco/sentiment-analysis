import { Request, Response } from 'express';
import { getAnalyzedTweets } from '../contexts/tweets/application/TweetsInteractor.js';

import { Controller } from './Controller.js';

export class TweetFetchAnalysisController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    try {
      const { subject } = req.params;
      const result = await getAnalyzedTweets(subject);
      res.status(200).send(result.rows);
    } catch (error) {
      res
        .status(400)
        .send(
          `(ERROR) ==> Fail to retrieve analysis for ${req.params.username}.`,
        );
    }
  }
}
