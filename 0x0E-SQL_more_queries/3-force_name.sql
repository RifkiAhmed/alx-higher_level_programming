-- Script that creates the table force_name on my MySQL server.
-- The database name is passed as an argument of the mysql command.
-- If the table force_name already exists, script not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);