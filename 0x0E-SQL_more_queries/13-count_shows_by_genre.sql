-- Script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
-- Each record display: <TV Show genre> - <Number of shows linked to this genre>
-- First column called genre, Second column called number_of_shows.
-- a genre that doesn’t have any shows linked not displayed.
-- Results sorted in descending order by the number of shows linked,
-- using only one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY genre
ORDER BY number_of_shows DESC;