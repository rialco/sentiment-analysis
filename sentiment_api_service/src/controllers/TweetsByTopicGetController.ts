import { Request, Response } from 'express';

import { Controller } from './Controller.js';
import { TweetFetcher } from '../contexts/tweets/application/TweetFetcher.js';
import { TweetSaver } from '../contexts/tweets/application/TweetSaver.js';

export class TweetsByTopicGetController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    const tweetFetcher = new TweetFetcher();
    const tweetSaver = new TweetSaver();

    try {
      const { hashtag } = req.params;
      const { nextToken } = req.query;
      const fetchedTweets = await tweetFetcher.fetchByTopic(
        hashtag,
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
