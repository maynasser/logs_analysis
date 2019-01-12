#logs analysis project#

import psycopg2

#connecting to db & run query#
def db_connection(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

#What are the most popular three articles of all time?#
def q1_answer():
    a1="select title, slug, path, count(*) from articles a, log b where a.slug = substring(b.path, 10) group by title, a.slug, b.path order by count desc limit 3;"
    popular_articles= db_connection(a1)
    print('the most popular three articles of all time are: ')
    count = 1
    for i in popular_articles:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1
    pass

# Who are the most popular article authors of all time? #
def q2_answer():
    a2 = "select name, count(*) as v from authors a, articles b, log c where b.slug = substring(c.path, 10) and a.id = b.author group by name order by v desc;"
    popular_authors= db_connection(a2)
    print("the most popular article authors of all time is:")
    count = 1
    for i in popular_authors:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1
    pass 

# On which days did more than 1% of requests lead to errors? #
def q3_answer():
    a3 = """
    select allReqeusts.date, round( ((errs.err404 *100 ) / allReqeusts.req), 2) as errPercent from
    (select to_char(date_trunc('day', time), 'Month dd,  yyyy') as date, count(*) as err404 
    from log where status like '404%' group by date) as errs
    join (select to_char(date_trunc('day', time), 'Month dd,  yyyy') as date, count(*) as req from log group by date) as allReqeusts 
    on errs.date = allReqeusts.date 
    where ((round( ((errs.err404 * 100) / allReqeusts.req), 2)) > 1) order by errPercent  desc;
    """
    errors= db_connection(a3)
    print("Days did more than '1%' of requests lead to errors are: ")
    for i in errors:
        print(str(i[0]) + " -- "+ str(i[1]) + " %" + " errors" )
    pass

q1_answer()
q2_answer()
q3_answer()

"""
Sources and references:
https://www.w3schools.com/
https://www.postgresql.org/docs/9.4/app-psql.html
https://github.com/michellejl/log_analysis/blob/master/loganalysisdb.py
https://github.com/br3ndonland/udacity-fsnd-p3-sql/blob/master/logs-methods.md
https://stackoverflow.com/questions/44223807/postgresql-finding-the-3-most-popular-articles-in-a-news-database
http://www.geeksengine.com/database/basic-select/arithmetic-operations.php
https://stackoverflow.com/questions/770579/how-to-calculate-percentage-with-a-sql-statement
https://www.dofactory.com/sql/subquery
https://www.dofactory.com/sql/join
"""