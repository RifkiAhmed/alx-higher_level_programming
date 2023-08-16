-- Script that creates the table unique_id on mu MySQL server.
-- id INT with the default value 1 and unique;
-- name VARCHAR(256).
-- The database name is passed as an argument of the mysql command.
-- If the table unique_id already exists, script not fail.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256));