interface TweetFromSource {
    extended_tweet?: {
        full_text: string
    };
    text: string;
}

const cleanTweet = (tweet: string) => {
  let t = '';
  t = tweet.replace(/(@\w*)/g, '');
  t = t.replace(/(https:\/\/\w+\.\w+\/*\w+)/g, '');
  t = t.replace(/(#\w+)/g, '');
  t = t.replace(/[\r\n]/gm, '');
  t = t.replace(/([\u2700-\u27BF]|[\uE000-\uF8FF]|\uD83C[\uDC00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|[\u2011-\u26FF]|\uD83E[\uDD10-\uDDFF])/g, '')
    .replace(/\s+/g, ' ');
  return t.toLowerCase().trim();
};

export const getCleanedTweets = (tweets: TweetFromSource[]) => {
  return tweets.map((t: TweetFromSource) => {
    if (t.extended_tweet) {
      const temp = cleanTweet(t.extended_tweet.full_text);
      return [temp];
    } else {
      const temp = cleanTweet(t.text);
      return [temp];
    }
  });
};