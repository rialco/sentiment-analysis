import { Request, Response } from "express";

import { Controller } from "./Controller.js";
import { TweetFetcher } from "../contexts/tweets/application/TweetFetcher.js";

export class TweetsByUsernameGetController implements Controller {

  async run(req: Request, res: Response): Promise<void> {
    const tweetFetcher = new TweetFetcher();
    
    try {
      const { username } = req.params;
      res.send(await tweetFetcher.fetchByUsername(username));
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets');
    }
  }
}