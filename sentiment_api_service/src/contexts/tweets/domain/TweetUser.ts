import { StringValueObject } from "../../../contexts/shared/domain/value-object/StringValueObject.js";

export class TweetUser extends StringValueObject{
  constructor(value: string) {
    super(value);
  }
}