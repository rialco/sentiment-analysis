import type { PoolConfig, QueryResultRow } from 'pg';
import pg from 'pg';

export class PostgresPool {
  private pool;

  constructor(options: PoolConfig) {
    this.pool = new pg.Pool(options);
  }

  async close(): Promise<boolean> {
    try {
      await this.pool.end();
      return true;
    } catch (e) {
      console.log('Error ending pool');
      return false;
    }
  }

  query(SQL: string, params?: unknown[]): Promise<QueryResultRow> {
    return this.pool.query(SQL, params);
  }
}

export const pgPool = new PostgresPool({
  connectionString: process.env.DATABASE_URL,
  ssl: false
});
