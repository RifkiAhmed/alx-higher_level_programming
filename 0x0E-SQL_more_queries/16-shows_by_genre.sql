-- Script that lists all shows, and all genres linked to that show
-- from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, NULL is displayed in the genre column.
-- Each record display: tv_shows.title - tv_genres.name, sorted in ascending
-- order by the show title and genre name, using only one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT tv_shows.title AS title, IFNULL(tv_genres.name, NULL) AS name
FROM tv_shows LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;