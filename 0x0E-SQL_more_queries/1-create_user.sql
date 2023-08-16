-- Script that creates the MySQL server user user_0d_1.
-- user_0d_1 have all privileges, password set to user_0d_1_pwd
-- If the user user_0d_1 already exists, script not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED WITH 'user_0d_1_pwd';