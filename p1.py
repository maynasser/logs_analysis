# !/usr/bin/env python3

import psycopg2
# connecting to db & run query'


def db_connection(query):
    try:
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        return results
    except psycopg2.DatabaseError as e:
        print('Sorry, there is an error : %s' % e)
    finally:
        db.close()


# What are the most popular three articles of all time?


def q1_answer():
    a1 = """select title as Title, count(*) as Views from articles a,
    log b where a.slug = substring(b.path, 10)
    group by title, a.slug, b.path order by Views desc limit 3"""
    popular_articles = db_connection(a1)
    print('the most popular three articles of all time are: ')
    count = 1
    for (Title, Views) in popular_articles:
        print("({})  {} -- {} views.".format(count, Title, Views))
        count += 1
    print("-" * 70)
    pass


# Who are the most popular article authors of all time?


def q2_answer():
    a2 = """select name, count(*) as v from authors a, articles b,
    log c where b.slug = substring(c.path, 10) and a.id = b.author
    group by name order by v desc;"""
    popular_authors = db_connection(a2)
    print("the most popular article authors of all time are:")
    count = 1
    for (name, v) in popular_authors:
        print("({})  {} with {} views.".format(count, name, v))
        count += 1
    print("-" * 70)
    pass


# On which days did more than 1% of requests lead to errors?


def q3_answer():
    a3 = """
    select allReqeusts.date as d,
    round( ((errs.err404 *100.0 ) / allReqeusts.req), 2) as errPercent
    from (select to_char(date_trunc('day', time), 'Month dd,  yyyy') as date,
    count(*) as err404
    from log where status like '404%' group by date) as errs
    join (select to_char(date_trunc('day', time), 'Month dd,  yyyy') as date,
    count(*) as req from log group by date) as allReqeusts
    on errs.date = allReqeusts.date
    where ((round( ((errs.err404 * 100.0) / allReqeusts.req), 2)) > 1)
    order by errPercent  desc;
    """
    errors = db_connection(a3)
    print("Days did more than '1%' of requests lead to errors are: ")
    for (d, errPercent) in errors:
        print("{} -- {} % errors".format(d, errPercent))
    pass


if __name__ == '__main__':
    q1_answer()
    q2_answer()
    q3_answer()
else:
    print("Please try to import the program as module.")


"""Sources and references:
https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
https://www.programcreek.com/python/example/66935/psycopg2.DatabaseError
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
https://www.w3schools.com/
https://www.postgresql.org/docs/9.4/app-psql.html
https://github.com/michellejl/log_analysis/blob/master/loganalysisdb.py
https://github.com/br3ndonland/udacity-fsnd-p3-sql/blob/master/logs-methods.md
https://stackoverflow.com/questions/44223807/postgresql-finding-the-3-most-popular-articles-in-a-news-database
http://www.geeksengine.com/database/basic-select/arithmetic-operations.php
https://stackoverflow.com/questions/770579/how-to-calculate-percentage-with-a-sql-statement
https://www.dofactory.com/sql/subquery
https://www.dofactory.com/sql/join"""
