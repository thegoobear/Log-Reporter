create view parsedlog (titles, hits)
as
select initcap(replace(substr(log.path,10), '-', ' ')) as titles,
count(*)
from log
where length(log.path)>1
group by titles
order by count(*) desc;

create view striptitles (title) as
select initcap(replace(replace(articles.title, '''', ''),',','')), articles.author
from articles;
