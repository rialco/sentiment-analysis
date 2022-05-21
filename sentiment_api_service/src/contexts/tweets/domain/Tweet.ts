import { TweetCity } from './TweetCity.js';
import { TweetContent } from './TweetContent.js';
import { TweetId } from './TweetId.js';
import { TweetUser } from './TweetUser.js';

export class Tweet {
  readonly id: TweetId;
  readonly author: TweetUser;
  readonly mention: TweetUser;
  readonly content: TweetContent;
  readonly cleanedContent: string;
  readonly city: TweetCity;
  readonly country: string;
  readonly retweetCount: number;
  readonly favoriteCount: number;
  readonly tweetDate: Date;
  readonly createdAt: Date;

  constructor(
    id: TweetId,
    author: TweetUser,
    mention: TweetUser,
    content: TweetContent,
    city: TweetCity,
    retweetCount: number,
    favoriteCount: number,
    tweetDate: Date,
    createdAt: Date,
    cleanedContent: string,
  ) {
    this.id = id;
    this.author = author;
    this.mention = mention;
    this.content = content;
    this.city = city;
    this.country = 'Colombia';
    this.retweetCount = retweetCount;
    this.favoriteCount = favoriteCount;
    this.tweetDate = tweetDate;
    this.createdAt = createdAt;
    this.cleanedContent = cleanedContent;
  }

  static fromPrimitives(plainData: {
    id: string;
    author: string;
    content: string;
    mention: string;
    city: string;
    followerCount: number;
    retweetCount: number;
    favoriteCount: number;
    tweetDate: string;
    cleanedContent: string;
  }): Tweet {
    return new Tweet(
      new TweetId(plainData.id),
      new TweetUser(plainData.author, plainData.followerCount),
      new TweetUser(plainData.mention, 0),
      new TweetContent(plainData.content),
      new TweetCity(plainData.city),
      plainData.retweetCount,
      plainData.favoriteCount,
      new Date(plainData.tweetDate),
      new Date(),
      plainData.cleanedContent,
    );
  }

  toPrimitives() {
    return {
      id: this.id.value.toString(),
      author: this.author.username,
      mention: this.mention.username,
      content: this.content.value,
      city: this.city.value,
      country: this.country,
      retweetCount: this.retweetCount,
      favoriteCount: this.favoriteCount,
      tweetDate: this.tweetDate.toDateString(),
      createdAt: this.createdAt.toDateString(),
      cleanedContent: this.cleanedContent,
    };
  }
}
