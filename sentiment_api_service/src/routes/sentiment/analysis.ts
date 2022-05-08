import { Request, Response, Router } from 'express';
import Redis from 'ioredis';

const route = Router();
const redis = new Redis({
  host: process.env.REDIS_HOST || 'redis',
  port: parseInt(process.env.REDIS_PORT || '6379'),
  db: 0
});

export function registerAnalysisRoutes(router: Router) {
  router.use('/analysis', route);

  route.post('/', (req: Request, res: Response) => {
    const { username } = req.body;
    redis.xadd('events', '*', 'username', 'prueba');
    console.log('Published event to redis.');
    res.send('success');
  });
}
