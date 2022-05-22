import fetch from 'node-fetch';

import { Tweet } from '../domain/Tweet.js';
import { getLocalTweets } from '../utils/localTweets.js';
import { getCleanedTweet } from '../utils/tweetCleaner.js';

interface tweetAPIResponse {
  created_at: string;
  id: string;
  text: string;
  user: {
    screen_name: string;
    followers_count: number;
  };
  place: {
    name: string;
    country: string;
  };
  retweet_count: number;
  favorite_count: number;
  extended_tweet: {
    full_text: string;
  };
}

interface TwitterAPIResponse {
  results: tweetAPIResponse[];
  next: string;
}

interface fetchResponse {
  tweets: Tweet[];
  next: string;
}

export class TweetFetcher {
  parseTweets(res: TwitterAPIResponse, mention: string): fetchResponse {
    const tweets = res.results.map((t: tweetAPIResponse) => {
      const content = t.extended_tweet?.full_text || t.text;
      const cleanedContent = getCleanedTweet(t);

      const tweet = Tweet.fromPrimitives({
        id: t.id,
        author: t.user.screen_name,
        mention: mention,
        content: content,
        city: t.place.name,
        followerCount: t.user.followers_count,
        retweetCount: t.retweet_count,
        favoriteCount: t.favorite_count,
        tweetDate: t.created_at,
        cleanedContent: cleanedContent,
      });
      return tweet;
    });

    return {
      tweets: tweets,
      next: res.next,
    };
  }

  async fetchByUsername(
    username: string,
    nextToken?: string,
  ): Promise<fetchResponse> {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(@${username}) place_country:CO lang:es`,
      next: nextToken,
    };

    const environment = process.env.ENVIRONMENT;

    if (environment === 'PRODUCTION') {
      console.log('Twitter api called');
      const res = await fetch(searchUrl, {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
          'Content-type': 'application/json',
          Authorization: bearerToken,
        },
      });
      const tweets = (await res.json()) as TwitterAPIResponse;
      return this.parseTweets(tweets, username);
    }

    const localTweets = (await getLocalTweets()) as TwitterAPIResponse;
    return this.parseTweets(localTweets, username);
  }

  async fetchByTopic(
    topic: string,
    nextToken?: string,
  ): Promise<fetchResponse> {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(#${topic}) place_country:CO lang:es`,
      next: nextToken,
    };

    const environment = process.env.ENVIRONMENT;

    if (environment === 'PRODUCTION') {
      console.log('Twitter api called');
      const res = await fetch(searchUrl, {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
          'Content-type': 'application/json',
          Authorization: bearerToken,
        },
      });
      const tweets = (await res.json()) as TwitterAPIResponse;
      return this.parseTweets(tweets, topic);
    }

    const localTweets = (await getLocalTweets()) as TwitterAPIResponse;
    return this.parseTweets(localTweets, topic);
  }
}
