import { DatabaseError } from 'pg';
import { pgPool } from './PostgresPool.js';

export interface Conditions {
  table1Fields: string[];
  table2Fields: string[];
  operator: string;
  t1Column: string;
  t2Column: string;
  whereValue: string;
  whereKey: string;
}

export abstract class PostgresRepository<T> {
  protected async getQuery(table: string, fields: string[]): Promise<void> {
    const sql = `
    SELECT ${fields.toString()} 
    FROM ${table};
    `;
    try {
      await pgPool.query(sql);
    } catch (error) {
      const { code, detail } = error as DatabaseError;
      console.log(`(ERROR CODE: ${code}) ==> ${detail}`);
    }
  }

  protected async getJoinedQuery(
    table: string,
    table2: string,
    conditions: Conditions,
  ): Promise<any> {
    const sql = `
    SELECT ${conditions.table1Fields
      .map((f) => table + '.' + f)
      .toString()}, ${conditions.table2Fields
      .map((f) => table2 + '.' + f)
      .toString()} 
    FROM ${table}
    JOIN ${table2} ON ${table + '.' + conditions.t1Column} ${
      conditions.operator
    } ${table2 + '.' + conditions.t2Column}
    WHERE ${conditions.whereKey} = '${conditions.whereValue}'
    `;
    try {
      return pgPool.query(sql);
    } catch (error) {
      const { code, detail } = error as DatabaseError;
      console.log(`(ERROR CODE: ${code}) ==> ${detail}`);
    }
  }

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
