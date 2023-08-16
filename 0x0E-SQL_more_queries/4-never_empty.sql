-- Script that creates the table id_not_null on my MySQL server.
-- id INT with the default value 1.
-- name VARCHAR(256).
-- The database name is passed as an argument of the mysql command.
-- If the table id_not_null already exists, script not fail.
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));