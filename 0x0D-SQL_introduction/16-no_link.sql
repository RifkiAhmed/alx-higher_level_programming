-- Lists all records of the table second_table.
-- The database name is passed as an argument to the mysql command.
-- This SQL query doesn’t list rows without a name value,
-- display the score and the name (in this order),
-- listed by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score desc;
