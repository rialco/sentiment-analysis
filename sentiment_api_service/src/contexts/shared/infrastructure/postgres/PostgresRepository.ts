import { pgPool } from "./PostgresPool.js";

export abstract class PostgresRepository<T> {
  protected async persist(queryString: string, obj: T): Promise<void> {
    const params = obj as unknown as Record<string, unknown>;
    console.log(Object.values(params));
    pgPool.query(queryString, Object.values(params));
  }
}