/* eslint-disable @typescript-eslint/naming-convention */
import { MigrationBuilder } from 'node-pg-migrate';

export const shorthands = undefined;

export const up = (pgm: MigrationBuilder): void => {
  pgm.sql(`
    CREATE TABLE tweets (
        id BIGINT PRIMARY KEY,
        content TEXT,
        cleaned_content TEXT,
        mention TEXT,
        city TEXT,
        country TEXT,
        username TEXT,
        follower_count INTEGER,
        retweet_count INTEGER,
        favorite_count INTEGER,
        tweeted_at TIMESTAMP,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
  `);
};

export const down = (pgm: MigrationBuilder): void => {
  pgm.sql(`
    DROP TABLE tweets;
  `);
};
