import re
import database
import operator

data = database.database()

def parse(line):
    l = line.split('.')
    match("final", l[0])
    l = l[1]
    operation = l[:l.index('(')]
    if operation == "query":
        query(l[l.find('(') + 1:(l.find(')'))])


def match(expected, real):
    if expected != real:
        print("query semantic error")
        return False
    return True


def query(queries):
    tmp = re.findall("\[([A-Za-z0-9_<>=,\d*]+)\]", queries)
    if len(tmp) > 1:
        qs = tmp[0]
        qs = qs.split(',')
        select = tmp[1]
        select = select.split(',')
        db = parsequery(qs)
        print(select)
        data.printdb(select, db)



def parsequery(queries):
    db = data.db
    for query in queries:
        if '>=' in query:
            query = query.split('>=')
            print(query)
            db = data.lookup(operator.ge, query[0], query[1], db)
        elif '<=' in query:
            query = query.split('<=')
            db = data.lookup(operator.le, query[0], query[1], db)
        elif '<>' in query:
            query = query.split('<>')
            db = data.lookup(operator.ne, query[0], query[1], db)
        elif '>' in query:
            query = query.split('>')
            db = data.lookup(operator.gt, query[0], query[1], db)
        elif '<' in query:
            query = query.split('<')
            db = data.lookup(operator.lt, query[0], query[1], db)
        elif '=' in query:
            query = query.split('=')
            print(query)
            db = data.lookup(operator.eq, query[0], query[1], db)

    return db



