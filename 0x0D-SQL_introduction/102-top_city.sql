-- This SQL query displays the top 3 of cities temperature during July
-- and August ordered by temperature (descending).
-- The database name is passed as an argument to the mysql command.
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month >=7 and month <=8 GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
