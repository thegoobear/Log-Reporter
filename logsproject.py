#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on
Mon Jul 10 19:46:45 2017

A reporting program for the "news" database

Prints the most popular articles with hitcount,
most popular authors with aggregated hitcount,
and days with connection error rate > 1%

@author: Tripp Green
"""

import psycopg2


def getpopart(cursor):
    '''Prints the most popular articles and their number of hits.

    Args: a cursor object

    Returns: Void
    '''

    # SQL matches log path to titles substring the length of the log path
    cursor.execute('''select articles.title, count(log.path) as views
    from log, articles
    where log.path=concat('/article/', articles.slug)
    group by title, log.path
    order by views desc
    limit 3;''')

    articles = cursor.fetchall()

    for pair in articles:
        title = pair[0]
        hits = pair[1]
        print ("\"" + title + "\"", "-", hits, "views")


def getpopauth(cursor):
    '''Prints the most popular authors and their number of hits on all articles

    Args: a cursor object

    Returns: Void
    '''

    # SQL matches on logpath, article title, and author
    cursor.execute('''select authors.name, count(*) as views
    from log, articles, authors
    where log.path=concat('/article/', articles.slug)
    and authors.id = articles.author
    group by authors.name
    order by views desc;''')

    authors = cursor.fetchall()

    for pair in authors:
        author = pair[0]
        hits = pair[1]
        print (author, "-", hits, "views")


def geterrordays(cursor):
    '''Prints days with connection error rate > 1%

    Args: a cursor object

    Returns: Void
    '''

    # SQL two subquerys, one of "bad" hits and one of all hits, then finding
    # the pertange of errors
    cursor.execute('''select good.time,
    (100.0*bad.count/good.count)::decimal(5,2) as errors from
    (select log.time::date, count(log.time::date)
    from log
    where status <> '200 OK'
    group by log.time::date) as bad
    join
    (select log.time::date, count(log.time::date)
    from log
    group by log.time::date) as good
    on good.time = bad.time
    where (100.0*bad.count/good.count)::decimal(5,2) > 1;''')

    errors = cursor.fetchall()

    for pair in errors:
        date = pair[0]
        percentage = str(pair[1])
        print (date.strftime("%B %d, %Y") + " -", percentage + "% error\n")


if __name__ == '__main__':

    # Connect to Postgres database "news" and create cursor
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    print ("\nMost Popular Articles: ")
    getpopart(c)
    print ("\nMost Popular Authors: ")
    getpopauth(c)
    print ("\nHigh Error Days: ")
    geterrordays(c)

    db.close()
