## ALX AFRICA SE Program

### **0x0D. SQL - Introduction <sup>`` SQL `` `` MySQL ``</sup>**

### **Learning objectives:**
 - What’s a database
 - What’s a relational database
 - What does ``SQL`` stand for
 - What’s MySQL
 - How to create a database in MySQL
 - What does ``DDL`` and ``DML`` stand for
 - How to __CREATE__ or __ALTER__ a table
 - How to __SELECT__ data from a table
 - How to __INSERT__, __UPDATE__ or __DELETE__ data
 - What are subqueries
 - How to use MySQL functions


#### [0-list_databases.sql](0-list_databases.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all databases of my MySQL server.

#### [1-create_database_if_missing.sql](1-create_database_if_missing.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates the database __hbtn_0c_0__.
> - If the database __hbtn_0c_0__ already exists, the script not fail.

#### [2-remove_database.sql](2-remove_database.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that deletes the database __hbtn_0c_0__.
> - If the database __hbtn_0c_0__ doesn’t exist, the script not fail

#### [3-list_tables.sql](3-list_tables.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all the tables of a database.

#### [4-first_table.sql](4-first_table.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates a table called __first_table__ in the current database.
> - If the table __first_table__ already exists, script not fail

#### [5-full_table.sql](5-full_table.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that prints the full description of the table __first_table__ from the database __hbtn_0c_0__.

#### [6-list_values.sql](6-list_values.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all rows of the table __first_table__ from the database __hbtn_0c_0__.

#### [7-insert_value.sql](7-insert_value.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that inserts a new row in the table __first_table__ from the database __hbtn_0c_0__


#### [8-count_89.sql](8-count_89.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that displays the number of records with id = 89 in the table __first_table__ of the database __hbtn_0c_0__.

#### [9-full_creation.sql](9-full_creation.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that creates a table __second_table__ in the database __hbtn_0c_0__ and add multiples rows.
> - If the table __second_table__ already exists, the script not fail

#### [10-top_score.sql](10-top_score.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all records of the table __second_table__ of the database __hbtn_0c_0__.
> - Results display both the score and the name in this order, sorted by score, top first.

#### [11-best_score.sql](11-best_score.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all records with a score >= 10 in the table __second_table__ of the database __hbtn_0c_0__.
> - Results display both the score and the name in this order, sorted by score, top first.

#### [12-no_cheating.sql](12-no_cheating.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that updates the score of Bob to 10 in the table __second_table__, using only the ``name`` field.

#### [13-change_class.sql](13-change_class.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that removes all records with a score <= 5 in the table __second_table__ of the database __hbtn_0c_0__.

#### [14-average.sql](14-average.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that computes the score average as **_average_** of all records in the table __second_table__ of the database __hbtn_0c_0__.

#### [15-groups.sql](15-groups.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists the number of records with the same score in the table __second_table__ of the database __hbtn_0c_0__.
> - Results display the score and the number of records for this score with the label **_number_**, sorted by descending number of records.

#### [16-no_link.sql](16-no_link.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that lists all records of the table __second_table__ of the database __hbtn_0c_0__, rows without a name value not listed.
> - Results display the score and the name in this order, sorted by descending score

#### [100-move_to_utf8.sql](100-move_to_utf8.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that converts __hbtn_0c_0__ database and __first_table__ to UTF8 (CHARCTER SET _utf8mb4_, COLLATE *utf8mb4_unicode_ci*).

#### [101-avg_temperatures.sql]() <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that displays the average temperature by city from the table __temperatures__ of the database __hbtn_0c_0__
sorted by descending temperature.

#### [102-top_city.sql](102-top_city.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that displays the top 3 of cities temperature from the table __temperatures__ of the database __hbtn_0c_0__ during July and August sorted by descending temperature.

#### [103-max_state.sql](103-max_state.sql) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Script that displays the max temperature of each state from the table __temperatures__ of the database __hbtn_0c_0__ sorted by State name.

### AUTHOR:
#### **Ahmed RIFKI** <sup>[@AhmedSeeker](https://github.com/AhmedSeeker)</sup>
