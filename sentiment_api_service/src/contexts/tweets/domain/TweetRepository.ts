import { Tweet } from './Tweet.js';

export interface TweetRepository {
  save(tweet: Tweet): Promise<void>;
}
