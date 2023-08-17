## ALX AFRICA SE Program

### **0x0E. SQL - More queries <sup>`` SQL `` `` MySQL ``</sup>**

### **Learning objectives:**
 - How to create a new MySQL __user__
 - How to manage privileges for a user to a database or table
 - What’s a _PRIMARY KEY_
 - What’s a _FOREIGN KEY_
 - How to use _NOT NULL_ and _UNIQUE_ constraints
 - How to retrieve datas from multiple tables in one request
 - What are subqueries
 - What are _JOIN_ and _UNION_

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="">
  <source media="(prefers-color-scheme: light" srcset="">
  <img alt="" src="">
</picture>

#### [0-privileges.sql](0-privileges.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all privileges of the MySQL users *user_0d_1* and *user_0d_2* on my server (localhost).

#### [1-create_user.sql](1-create_user.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the MySQL server user *user_0d_1*.

#### [2-create_read_user.sql](2-create_read_user.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the database _hbtn_0d_2_ and the user *user_0d_2*.

#### [3-force_name.sql](3-force_name.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the table *force_name* on my MySQL server.

#### [4-never_empty.sql](4-never_empty.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the table *id_not_null* on my MySQL server.

#### [5-unique_id.sql](5-unique_id.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the table *unique_id* on my MySQL server.

#### [6-states.sql](6-states.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the database *hbtn_0d_usa* and the table *states* (in the database hbtn_0d_usa) on my MySQL server.

#### [7-cities.sql](7-cities.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the database *hbtn_0d_usa* and the table *cities* (in the database hbtn_0d_usa) on my MySQL server.

#### [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all the cities of *California* that can be found in the database *hbtn_0d_usa*.

#### [9-cities_by_state_join.sql](9-cities_by_state_join.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all cities contained in the database *hbtn_0d_usa*.

#### [10-genre_id_by_show.sql](10-genre_id_by_show.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows contained in *hbtn_0d_tvshows* that have at least one genre linked.

#### [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows contained in the database *hbtn_0d_tvshows*.

#### [12-no_genre.sql](12-no_genre.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows contained in *hbtn_0d_tvshows* without a genre linked.

#### [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all genres from *hbtn_0d_tvshows* and displays the number of shows linked to each.

#### [14-my_genres.sql](14-my_genres.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that uses the *hbtn_0d_tvshows* database to lists all genres of the show Dexter.

#### [15-comedy_only.sql](15-comedy_only.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all Comedy shows in the database *hbtn_0d_tvshows*.

#### [16-shows_by_genre.sql](16-shows_by_genre.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows, and all genres linked to that show, from the database *hbtn_0d_tvshows*.

#### [100-not_my_genres.sql](100-not_my_genres.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that uses the *hbtn_0d_tvshows* database to list all genres not linked to the show *Dexter*.

#### [101-not_a_comedy.sql](101-not_a_comedy.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows without the genre Comedy in the database *hbtn_0d_tvshows*.

#### [102-rating_shows.sql](102-rating_shows.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all shows from *hbtn_0d_tvshows_rate* by their rating.

#### [103-rating_genres.sql](103-rating_genres.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all genres in the database *hbtn_0d_tvshows_rate* by their rating.

### AUTHOR:
#### **Ahmed RIFKI** <sup>[@AhmedSeeker](https://github.com/AhmedSeeker)</sup>
