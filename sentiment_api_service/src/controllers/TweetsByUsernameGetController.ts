import { Request, Response } from "express";

import { Controller } from "./Controller.js";
import { TweetFetcher } from "../contexts/tweets/application/TweetFetcher.js";
import { TweetSaver } from "../contexts/tweets/application/TweetSaver.js";

export class TweetsByUsernameGetController implements Controller {

  async run(req: Request, res: Response): Promise<void> {
    const tweetFetcher = new TweetFetcher();
    const tweetSaver = new TweetSaver();
    
    try {
      const { username } = req.params;
      const tweets = await tweetFetcher.fetchByUsername(username);
      console.log('Esto llego aqui en el controaldor');
      console.log(tweets[0]);
      await tweetSaver.run(tweets[0]);
      res.send(tweets);
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to fetch tweets');
    }
  }
}