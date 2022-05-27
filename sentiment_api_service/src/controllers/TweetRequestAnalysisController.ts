import { Request, Response } from 'express';
import Redis from 'ioredis';

import { Controller } from './Controller.js';

const redis = new Redis({
  host: process.env.REDIS_HOST || 'redis',
  port: parseInt(process.env.REDIS_PORT || '6379'),
  db: 0,
});

export class TweetRequestAnalysisController implements Controller {
  async run(req: Request, res: Response): Promise<void> {
    try {
      const { username } = req.params;
      await redis.xadd('events', '*', 'username', username);
      console.log('Published event to redis.');
      res.status(204).send();
    } catch (error) {
      res.status(400).send('(ERROR) ==> Fail to publish event to redis.');
    }
  }
}
