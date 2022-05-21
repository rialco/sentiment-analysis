import { PostgresRepository } from '../../shared/infrastructure/postgres/PostgresRepository.js';
import { Tweet } from '../domain/Tweet.js';
import { TweetRepository } from '../domain/TweetRepository.js';

interface mappedTweet {
  id: BigInt;
  username: string;
  mention: string;
  content: string;
  cleaned_content: string;
  city: string;
  country: string;
  follower_count: number;
  retweet_count: number;
  favorite_count: number;
  tweeted_at: Date;
}

export class PgTweetRepository
  extends PostgresRepository<mappedTweet>
  implements TweetRepository
{
  private mapTweets(tweets: Tweet[]) {
    return tweets.map((tweet) => {
      return {
        id: tweet.id.value,
        username: tweet.author.username,
        mention: tweet.mention.username,
        content: tweet.content.value,
        cleaned_content: tweet.cleanedContent,
        city: tweet.city.value,
        country: tweet.country,
        follower_count: tweet.author.followerCount,
        retweet_count: tweet.retweetCount,
        favorite_count: tweet.favoriteCount,
        tweeted_at: tweet.tweetDate,
      };
    });
  }

  public save(tweet: Tweet): Promise<void> {
    const mappedTweet = this.mapTweets([tweet]);
    return this.persist('tweets', mappedTweet[0]);
  }

  public saveBatch(tweets: Tweet[]): Promise<void> {
    const mappedTweets = this.mapTweets(tweets);
    return this.persistBatch('tweets', mappedTweets);
  }
}
