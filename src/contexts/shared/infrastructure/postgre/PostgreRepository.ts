import { Pool } from 'pg';

export abstract class PostgreRepository<T> {
  constructor(private _pool: Promise<Pool>) {}

  protected pool(): Promise<Pool> {
    return this._pool;
  }

  protected async persist(id: string, obj: T): Promise<void> {
    (await this._pool).query("SELECT 1 + 1");
  }
}