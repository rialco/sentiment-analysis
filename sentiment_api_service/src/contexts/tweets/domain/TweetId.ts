import { BigNumberValueObject } from '../../shared/domain/value-object/BigIntValueObject.js';

export class TweetId extends BigNumberValueObject {
  constructor(value: string) {
    super(value);
  }
}
