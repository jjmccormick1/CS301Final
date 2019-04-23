import re
import database
import operator

data = database.database("data.txt")

def parse(line):
    print(line)
    l = line.split('.')
    match("final", l[0])
    l = l[1]
    operation = l[:l.index('(')]
    if operation == "query":
        query(l[l.find('(') + 1:(l.find(')'))])
    elif operation == "count":
        count(l[l.find('(') + 1:(l.find(')'))])
    elif operation == "insert":
        insert(l[l.find('(') + 1:(l.find(')'))])


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
        data.printdb(select, db)
    elif len(tmp) > 0:
        if '=' in tmp[0] or '>' in tmp[0] or '<' in tmp[0]:
            qs = tmp[0]
            qs = qs.split(',')
            db = parsequery(qs)
            data.printdb({}, db)
        else:
            select = tmp
            data.printdb(select, data.db)
    else:
        data.printdb({}, data.db)


def parsequery(queries):
    db = data.db
    for query in queries:
        if '>=' in query:
            query = query.split('>=')
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
            db = data.lookup(operator.eq, query[0], query[1], db)

    return db

def count(counts):
    tmp = re.findall("\[([A-Za-z0-9_<>=,\d*]+)\]", counts)
    key = tmp[0]
    unique = tmp[1]
    cnt = 0
    isin = []
    for i in range(data.docid):
        if str(i) in data.db.keys():
            row = data.db[str(i)]
            if unique == str(0):
                if key in row.keys():
                    cnt = cnt + 1
            elif unique == str(1):
                if key in row.keys() and isin is None:
                    cnt = cnt + 1
                    isin = [row[key]]
                elif key in row.keys() and row[key] not in isin:
                    cnt = cnt + 1
                    isin.extend([row[key]])

    print(cnt)

def insert(line):
    tmp = {}
    spl = line.split()
    dcid=0
    for x in spl:
        x = x.split(':')
        tmp[x[0]] = x[1]

    data.insertrow(tmp)
    print(data.db)
    print("DocID:" + str(dcid), end= ' ')
    for key in tmp.keys():
        print(key + ':' + tmp[key], end=' ')
    print()
