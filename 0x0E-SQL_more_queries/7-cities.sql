-- Script that creates the database hbtn_0d_usa and the table cities
-- in the database hbtn_0d_usa on my MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key;
-- state_id INT, can’t be null and a FOREIGN KEY that references
-- to id of the states table;
-- name VARCHAR(256) can’t be null.
-- If the database hbtn_0d_usa or table cities already exists, script not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id));