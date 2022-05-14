import fetch from 'node-fetch';

export class TweetFetcher {

  async fetchByUsername(username: string) {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(@${username}) place_country:CO lang:es`
    };

    const res = await fetch(searchUrl, {
      method: 'POST',
      body: JSON.stringify(query),
      headers: {
        'Content-type': 'application/json',
        'Authorization': bearerToken
      }
    });

    return res.json();
  }
  
  async fetchByTopic(topic: string) {
    const baseUrl = 'https://api.twitter.com/1.1/tweets/search/30day/';
    const searchUrl = baseUrl + 'rialco.json';
    const bearerToken = 'Bearer ' + process.env.BEARER_TOKEN;
    const query = {
      query: `(#${topic}) place_country:CO lang:es`
    };

    const res = await fetch(searchUrl, {
      method: 'POST',
      body: JSON.stringify(query),
      headers: {
        'Content-type': 'application/json',
        'Authorization': bearerToken
      }
    });

    return res.json();
  } 
}