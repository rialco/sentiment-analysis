import { PostgreRepository } from "../../../contexts/shared/infrastructure/postgre/PostgreRepository.js";
import { Tweet } from "../domain/Tweet.js";
import { TweetRepository } from "../domain/TweetRepository.js";

export class PgTweetRepository extends PostgreRepository<Tweet> implements TweetRepository {
  public save(tweet: Tweet): Promise<void> {
    return this.persist(tweet.id.value, tweet);
  }
}