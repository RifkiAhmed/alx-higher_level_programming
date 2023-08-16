-- This SQL query displays the max temperature of each state
-- ordered by State name.
-- The database name is passed as an argument to the mysql command.
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state ASC;
