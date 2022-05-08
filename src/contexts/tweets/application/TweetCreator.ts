import { Tweet } from "../domain/Tweet.js";
import { PgTweetRepository } from "../infrastructure/PgTweetRepository.js";

export class TweetCreator {
  private repository: PgTweetRepository;

  constructor(repository: PgTweetRepository) {
    this.repository = repository;
  }

  async run(tweet: Tweet): Promise<void> {
    await this.repository.save(tweet);
  }
}