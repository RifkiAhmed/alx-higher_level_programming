-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = 'Comedy'
-- (but the id can be different).
-- Each record display: tv_shows.title, sorted in ascending order by
-- the show title, using only one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT tv_shows.title AS title
FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;