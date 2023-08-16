-- Script that lists all shows contained in hbtn_0d_tvshows
-- without a genre linked.
-- Each record display: tv_shows.title - tv_show_genres.genre_id, sorted in
-- ascending order by tv_shows.title and tv_show_genres.genre_id, using only
-- one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;