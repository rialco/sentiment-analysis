import { TweetFetcher } from './TwitterApiFetcher.js';
import { TweetRepository } from './TweetRepository.js';

const twitterAPIFetcher = new TweetFetcher();
const tweetRepository = new TweetRepository();

export async function getTweetsByUsernameFromTwitter(
  username: string,
  nextToken: string,
) {
  const fetchedTweets = await twitterAPIFetcher.fetchByUsername(
    username,
    nextToken as string,
  );
  await tweetRepository.persistBatch(fetchedTweets.tweets);
  const tweetsJson = fetchedTweets.tweets.map((t) => t.toPrimitives());
  return {
    nextToken: fetchedTweets.next,
    tweets: tweetsJson,
  };
}

export async function getTweetsByTopicFromTwitter(
  hashtag: string,
  nextToken: string,
) {
  const fetchedTweets = await twitterAPIFetcher.fetchByTopic(
    hashtag,
    nextToken as string,
  );
  await tweetRepository.persistBatch(fetchedTweets.tweets);
  const tweetsJson = fetchedTweets.tweets.map((t) => t.toPrimitives());
  return {
    nextToken: fetchedTweets.next,
    tweets: tweetsJson,
  };
}

export async function getAnalyzedTweets(subject: string) {
  return tweetRepository.getJoinQuery('tweets', 'tweets_analysis', {
    table1Fields: [
      'content',
      'city',
      'country',
      'username',
      'follower_count',
      'favorite_count',
      'retweet_count',
    ],
    table2Fields: ['sentiment'],
    operator: '=',
    t1Column: 'id',
    t2Column: 'tweet_id',
    whereValue: subject,
    whereKey: 'mention',
  });
}
