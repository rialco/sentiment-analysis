import { DatabaseError } from 'pg';
import { pgPool } from './PostgresPool.js';

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
    const sql = `
    INSERT INTO tweets
    (${Object.keys(params[0]).toString()})
    VALUES
    ${params.map((p, idx) => {
      return `(${Object.keys(p)
        .map((k, i) => '$' + (Object.keys(p).length * idx + i + 1))
        .toString()})`;
    })}
    ON CONFLICT DO NOTHING
    RETURNING *;
    `;

    const values = params.map((p) => Object.values(p)).flat();

    try {
      await pgPool.query(sql, values);
    } catch (error) {
      const { code, detail } = error as DatabaseError;
      console.log(`(ERROR CODE: ${code}) ==> ${detail}`);
    }
  }
}
