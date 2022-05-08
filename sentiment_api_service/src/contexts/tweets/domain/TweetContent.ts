import { StringValueObject } from "../../../contexts/shared/domain/value-object/StringValueObject.js";

export class TweetContent extends StringValueObject {
  constructor(value: string) {
    super(value);
  }
}