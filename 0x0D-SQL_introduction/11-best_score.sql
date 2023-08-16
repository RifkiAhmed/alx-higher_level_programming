-- Lists all records with a score >= 10 in the table second_table of the
-- database hbtn_0c_0 in my MySQL server.
-- The database name is passed as an argument of the mysql command.
-- This SQL query lists the score and the name (in this order),
-- ordered by score (top first).
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
