import { StringValueObject } from '../../../contexts/shared/domain/value-object/StringValueObject.js';

export class TweetCity extends StringValueObject {
  constructor(value: string) {
    super(value);
  }
}
