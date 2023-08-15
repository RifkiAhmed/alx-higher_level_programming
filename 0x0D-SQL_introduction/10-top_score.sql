-- Lists all records of the table second_table of the database hbtn_0c_0
-- in my MySQL server.
-- The database name is passed as an argument of the mysql command.
-- This SQL query display both the score and the name (in this order),
-- ordered by score (top first).
SELECT score, name FROM second_table ORDER BY score desc
