-- Lists the number of records with the same score in the table second_table.
-- The database name is passed as an argument to the mysql command.
-- This SQL query the score and the number of records for this score
-- with the label 'number'.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
