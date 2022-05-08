import { Uuid } from "../../../contexts/shared/domain/value-object/Uuid.js";

export class TweetId extends Uuid {
  constructor(value: string) {
    super(value);
  }
}