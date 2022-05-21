export class TweetUser {
  readonly username: string;
  readonly followerCount: number;

  constructor(username: string, followerCount: number) {
    this.username = username;
    this.followerCount = followerCount;
  }
}
