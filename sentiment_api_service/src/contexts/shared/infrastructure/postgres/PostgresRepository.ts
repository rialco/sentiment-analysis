import { DatabaseError } from 'pg';
import { pgPool } from './PostgresPool.js';
import format from 'pg-format';

export abstract class PostgresRepository<T> {
  protected async persist(table: string, obj: T): Promise<void> {
    const params = obj as unknown as Record<string, unknown>;
    const sql = `
    INSERT INTO ${table}
    (${Object.keys(params).toString()})
    VALUES (${Object.keys(params)
      .map((k, i) => '$' + (i + 1))
      .toString()})
    RETURNING *;
    `;
    try {
      await pgPool.query(sql, Object.values(params));
    } catch (error) {
      const { code, detail } = error as DatabaseError;
      console.log(`(ERROR CODE: ${code}) ==> ${detail}`);
    }
  }

  protected async persistBatch(table: string, obj: T[]): Promise<void> {
    const params = obj as unknown as Record<string, unknown>[];
    const sql = format(`
    INSERT INTO ${table}
    (${Object.keys(params[0]).toString()})
    
    `);
    try {
      await pgPool.query(sql, Object.values(params));
    } catch (error) {
      const { code, detail } = error as DatabaseError;
      console.log(`(ERROR CODE: ${code}) ==> ${detail}`);
    }
  }
}
