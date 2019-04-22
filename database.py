class database:
    docid = 0
    db = {}

    def __init__(self):
        self.db = self.parsefile("data.txt")

    def parsefile(self, filename):
        db = {}
        datafile = open(filename, "r")
        lines = datafile.readlines()
        for line in lines:
            tmp = {}
            spl = line.split()
            for x in spl:
                x = x.split(':')
                tmp[x[0]] = x[1]

            id = tmp["DocID"]
            intid = int(id)
            if intid > self.docid:
                self.docid = intid
            del tmp["DocID"]
            db[id] = tmp
        return db

    def lookup(self, compare, key, value, db):
        retdb = {}
        for i in range(self.docid):
            if str(i) in db.keys():
                row = db[str(i)]
                if key in row.keys():
                    lookup = row[key]
                    if compare(lookup, value):
                        retdb[str(i)] = row

        return retdb


    def printdb(self, select, db):
        for i in range(self.docid):
            if str(i) in db.keys():
                row = db[str(i)]

                if "DocID" in select:
                    print("DocID" + ':' + str(i), end=' ')

                for key in select:
                    if key in row.keys():
                        print(key + ':' + row[key], end=' ')
                    elif key != "DocID":
                        print(key + ':' + "NA", end=' ')
                print()
