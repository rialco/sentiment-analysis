import { Uuid } from "../../../contexts/shared/domain/value-object/Uuid.js";
import { TweetContent } from "./TweetContent.js";
import { TweetId } from "./TweetId.js";
import { TweetUser } from "./TweetUser.js";

export class Tweet {
  readonly id: TweetId;
  readonly author: TweetUser;
  readonly content: TweetContent;
  readonly mention: TweetUser;

  constructor(id: TweetId, content: TweetContent, author: TweetUser, mention: TweetUser) {
    this.id = id;
    this.content = content;
    this.author = author;
    this.mention = mention;
  }

  static fromPrimitives( plainData: {id: string, author: string, content: string, mention: string}): Tweet {
    return new Tweet(
      new Uuid(plainData.id),
      new TweetUser(plainData.author),
      new TweetContent(plainData.content),
      new TweetUser(plainData.mention)
    );
  }

  toPrimitives() {
    return {
      id: this.id.value,
      author: this.author.value,
      content: this.content.value,
      mention: this.mention.value
    };
  }
}