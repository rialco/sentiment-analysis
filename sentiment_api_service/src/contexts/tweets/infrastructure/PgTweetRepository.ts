import { PostgresRepository } from "../../shared/infrastructure/postgres/PostgresRepository.js";
import { Tweet } from "../domain/Tweet.js";
import { TweetRepository } from "../domain/TweetRepository.js";

export class PgTweetRepository extends PostgresRepository<Tweet> implements TweetRepository {
  public save(tweet: Tweet): Promise<void> {
    return this.persist(`
    INSERT INTO tweets 
    (content, mention, city, country, username, follower_count, 
    retweet_count, favorite_count, external_id, tweeted_at, created_at)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
    RETURNING *;`, tweet);
  }
}