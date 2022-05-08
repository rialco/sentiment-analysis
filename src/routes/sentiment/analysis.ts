import { Request, Response, Router } from 'express';

const route = Router();

export function registerAnalysisRoutes(router: Router) {
  router.use('/analysis', route);

  route.post('/', (req: Request, res: Response) => {
    const { tweets } = req.body;
    res.send(tweets);
  });
}
