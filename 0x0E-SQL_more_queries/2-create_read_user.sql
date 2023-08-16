-- Script that creates the database hbtn_0d_2 and the user user_0d_2,
-- user_0d_2 have only SELECT privilege in the database hbtn_0d_2,
-- The user_0d_2 password set to user_0d_2_pwd.
-- If the database hbtn_0d_2 or user_0d_2 already exists, script not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'hostname';