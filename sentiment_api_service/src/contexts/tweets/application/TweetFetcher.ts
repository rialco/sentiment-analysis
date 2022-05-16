import fetch from 'node-fetch';
import { Tweet } from '../domain/Tweet.js';
import fs from 'fs/promises';

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

    if (environment !== 'TESTING') {
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

    try {
      console.log('Local tweets called');
      const tweetsFile = await fs.readFile('./twitter-response.json', 'utf-8');
      const res = JSON.parse(tweetsFile);
      return this.mapTweets(res.results, username) as unknown as Tweet[];
    } catch(e) {
      console.log(e);
      return [];
    }
  }
  
  async fetchByTopic(topic: string): Promise<Tweet[]> {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(#${topic}) place_country:CO lang:es`
    };

    const environment = process.env.ENVIRONMENT;

    if (environment !== 'TESTING') {
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

    try {
      console.log('Local tweets called');
      const tweetsFile = await fs.readFile('./twitter-response.json', 'utf-8');
      const res = JSON.parse(tweetsFile);
      return res.results as unknown as Tweet[];
    } catch(e) {
      console.log(e);
      return [];
    }
  } 
}