-- Script that uses the hbtn_0d_tvshows database to lists all genres
-- of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter
-- (but the id can be different)
-- Each record display: tv_genres.name, sorted in ascending order by
-- the genre name, using only one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT tv_genres.name AS name
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;