-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum, sorted in
-- descending order by the rating, using only one SELECT statement.
-- The database name is passed as an argument of the mysql command.
SELECT title, SUM(tv_show_ratings.rate) as rating FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;