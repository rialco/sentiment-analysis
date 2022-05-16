import { Tweet } from "../domain/Tweet.js";
import { PgTweetRepository } from "../infrastructure/PgTweetRepository.js";

export class TweetSaver {
  private repository: PgTweetRepository;

  constructor() {
    this.repository = new PgTweetRepository();
  }

  async run(tweet: Tweet): Promise<void> {
    await this.repository.save(tweet);
  }
}