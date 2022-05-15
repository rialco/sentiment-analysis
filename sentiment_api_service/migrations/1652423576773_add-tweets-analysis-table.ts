/* eslint-disable @typescript-eslint/naming-convention */
import { MigrationBuilder } from 'node-pg-migrate';

export const shorthands = undefined;

export const up = (pgm: MigrationBuilder): void => {
  pgm.sql(`
    CREATE TABLE tweets-analysis (
        id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        tweet_id BIGINT REFERENCES tweets(id),
        sentiment TEXT,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  `);
};

export const down = (pgm: MigrationBuilder): void => {
  pgm.sql(`
    DROP TABLE tweets-analysis;
  `);
};
