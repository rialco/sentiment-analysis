import fetch from 'node-fetch';

import { Tweet } from '../domain/Tweet.js';
import { getLocalTweets } from '../utils/localTweets.js';

interface twitterAPIResponse {
  results: Tweet[];
}

export class TweetFetcher {

  mapTweets(tweets: unknown[], username: string) {
    return tweets.map((tweet) => {
      const parsedTweet = tweet as Record<string, string>;
      return {
        id: parsedTweet.id,
        content: parsedTweet.text,
        username: 'user',
        mention: username
      };
    });
  }

  async fetchByUsername(username: string): Promise<Tweet[]> {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(@${username}) place_country:CO lang:es`
    };

    const environment = process.env.ENVIRONMENT;

    if (environment === 'PRODUCTION') {
      console.log('Twitter api called');
      const res = await fetch(searchUrl, {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
          'Content-type': 'application/json',
          'Authorization': bearerToken
        }
      });
      const tweets = await res.json() as twitterAPIResponse;
      return tweets.results;
    }

    return getLocalTweets();
  }
  
  async fetchByTopic(topic: string): Promise<Tweet[]> {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(#${topic}) place_country:CO lang:es`
    };

    const environment = process.env.ENVIRONMENT;

    if (environment === 'PRODUCTION') {
      console.log('Twitter api called');
      const res = await fetch(searchUrl, {
        method: 'POST',
        body: JSON.stringify(query),
        headers: {
          'Content-type': 'application/json',
          'Authorization': bearerToken
        }
      });
      const tweets = await res.json() as twitterAPIResponse;
      return tweets.results;
    }

    return getLocalTweets();
  } 
}