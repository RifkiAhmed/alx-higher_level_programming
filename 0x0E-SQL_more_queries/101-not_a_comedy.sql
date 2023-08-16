-- Script that lists all shows without the genre Comedy in
-- the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy
-- (but the id can be different).
-- Each record display: tv_shows.title, sorted in ascending order by
-- the show title, usins a maximum of two SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT title FROM tv_shows WHERE tv_shows.id
NOT IN (
    SELECT tv_shows.id FROM tv_shows JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
    )
ORDER BY title;