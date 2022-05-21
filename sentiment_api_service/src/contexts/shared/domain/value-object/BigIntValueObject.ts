export abstract class BigNumberValueObject {
  readonly value: BigInt;
  
  constructor(value: string) {
    this.value = BigInt(value);
  }
  
  equalsTo(other: BigNumberValueObject): boolean {
    return this.value === other.value;
  }
  
  isBiggerThan(other: BigNumberValueObject): boolean {
    return this.value > other.value;
  }
}
  