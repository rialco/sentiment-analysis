interface TweetFromSource {
  extended_tweet?: {
    full_text: string;
  };
  text: string;
}

const cleanTweet = (tweet: string) => {
  let t = '';
  t = tweet.replace(/(@\w*)/g, '');
  t = t.replace(/(https:\/\/\w+\.\w+\/*\w+)/g, '');
  t = t.replace(/(#\w+)/g, '');
  t = t.replace(/[\r\n]/gm, '');
  t = t
    .replace(
      /([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g,
      '',
    )
    .replace(/\s+/g, ' ');
  t = t.replace(/[^\p{L}\p{N}\p{P}\p{Z}^$\n]/gu, '');
  return t.toLowerCase().trim();
};

export const getCleanedTweets = (tweets: TweetFromSource[]) => {
  return tweets.map((t: TweetFromSource) => {
    getCleanedTweet(t);
  });
};

export const getCleanedTweet = (tweet: TweetFromSource) => {
  if (tweet.extended_tweet) {
    const temp = cleanTweet(tweet.extended_tweet.full_text);
    return temp;
  } else {
    const temp = cleanTweet(tweet.text);
    return temp;
  }
};
