import { Request, Response } from 'express';

import { Controller } from './Controller.js';
import { TweetFetcher } from '../contexts/tweets/application/TweetFetcher.js';
import { TweetSaver } from '../contexts/tweets/application/TweetSaver.js';

export class TweetsByUsernameGetController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    const tweetFetcher = new TweetFetcher();
    const tweetSaver = new TweetSaver();

    try {
      const { username } = req.params;
      const { nextToken } = req.query;
      const fetchedTweets = await tweetFetcher.fetchByUsername(
        username,
        nextToken as string,
      );
      await tweetSaver.runBatch(fetchedTweets.tweets);
      const tweetsJson = fetchedTweets.tweets.map((t) => t.toPrimitives());
      res.send({ nextToken: fetchedTweets.next, tweets: tweetsJson });
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets');
    }
  }
}
