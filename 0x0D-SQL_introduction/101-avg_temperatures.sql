-- This SQL query displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending).
-- The database name is passed as an argument to the mysql command.
SELECT city , AVG(value) as avg_temp FROM temperatures GROUP BY city
ORDER BY avg_temp DESC;
