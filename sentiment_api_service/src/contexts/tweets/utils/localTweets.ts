import fs from 'fs/promises';

import { Tweet } from '../domain/Tweet.js';

export const getLocalTweets = async () => {
  try {
    console.log('Local tweets called');
    const tweetsFile = await fs.readFile('./twitter-response.json', 'utf-8');
    const res = JSON.parse(tweetsFile);
    return res.results as unknown as Tweet[];
  } catch(e) {
    console.log(e);
    return [];
  }
};

