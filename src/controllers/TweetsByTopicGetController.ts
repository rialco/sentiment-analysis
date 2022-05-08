import { Request, Response } from "express";
import fetch from 'node-fetch';

import { Controller } from "./Controller.js";

export class TweetsByTopicGetController implements Controller {

  async run(req: Request, res: Response): Promise<void> {
    try {
      const { username } = req.params;
      const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
      const searchUrl = baseUrl + 'rialco';
      const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
      const query = {
        query: `(@${username}) place_country:CO lang:es`
      };

      const response = await fetch(searchUrl, {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
          'Content-type': 'application/json',
          'Authentication': bearerToken
        }
      });

      res.send(await response.json());

    } catch (error) {
            
    }
  }
}