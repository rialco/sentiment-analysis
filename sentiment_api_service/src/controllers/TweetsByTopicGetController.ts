import { Request, Response } from "express";

import { Controller } from "./Controller.js";
import { TweetFetcher } from "../contexts/tweets/application/TweetFetcher.js";

export class TweetsByTopicGetController implements Controller {

  async run(req: Request, res: Response): Promise<void> {
    const tweetFetcher = new TweetFetcher();
    
    try {
      const { hashtag } = req.params;
      res.send(await tweetFetcher.fetchByTopic(hashtag));
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets by topic');
    }
  }
}