import { Tweet } from '../domain/Tweet.js';
import { PgTweetRepository } from '../infrastructure/PgTweetRepository.js';

export class TweetRepository {
  private repository: PgTweetRepository;

  constructor() {
    this.repository = new PgTweetRepository();
  }

  async getJoinQuery(
    table: string,
    table2: string,
    options: Record<string, unknown>,
  ) {
    return this.repository.fetch(table, table2, options);
  }

  async persist(tweet: Tweet): Promise<void> {
    await this.repository.save(tweet);
  }

  async persistBatch(tweets: Tweet[]): Promise<void> {
    await this.repository.saveBatch(tweets);
  }
}
