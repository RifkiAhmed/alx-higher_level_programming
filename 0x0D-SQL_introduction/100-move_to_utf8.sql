-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci.
-- These SQL queries convert all of the following to UTF8.
ALTER DATABASE hbtn_0c_0 COLLATE = utf8mb4_unicode_ci CHARACTER SET = utf8mb4;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
