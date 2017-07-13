# News Database Log Report Generator

A program for gathering information from database logs

Basic useful feature list:

 * Report 3 most popular articles and viewcount
 * Reoport 3 most popular authors and viewcount
 * Report high connection error days (>1%)

## Installation

* Fork guthub repo and dowload files
* Place files in the shared folder of your VM if using virtual machine
* Create views in the database:
` psql -d news -f logsproject.sql`

Manual view creation syntax:

`create view parsedlog (titles, hits)
as
select initcap(replace(substr(log.path,10), '-', ' ')) as titles,
count(*)
from log
where length(log.path)>1
group by titles
order by count(*) desc;`

`create view striptitles (title) as
select initcap(replace(replace(articles.title, '''', ''),',','')), articles.author
from articles;`

* Run program: ` python3 logsproject.py `

## Output

The program should execute and print to Terminal in the following format:

Most Popular Articles:  
"Candidate Is Jerk Alleges Rival" - 338647 views  
"Bears Love Berries Alleges Bear" - 253801 views  
"Bad Things Gone Say Good People" - 170098 views

Most Popular Authors:  
Ursula La Multa - 424242 views  
Rudolf von Treppenwitz - 424033 views  
Anonymous Contributor - 170386 views

High Error Days: 
July 17, 2016 - 2.26% error

