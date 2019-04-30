class database:
    docid = 0
    db = {}
    def __init__(self, filename):
        self.db = self.parsefile(filename)

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
        for i in range(self.docid + 1):
            if str(i) in db.keys():
                row = db[str(i)]
                if key in row.keys():
                    lookup = row[key]
                    if compare(lookup, value):
                        retdb[str(i)] = row

        return retdb


    def printdb(self, select, db):
        for i in range(self.docid+1):
            if str(i) in db.keys():
                row = db[str(i)]

                if "DocID" in select:
                    print("DocID" + ':' + str(i), end=' ')
                    for key in select:
                        if key in row.keys():
                            print(key + ':' + row[key], end=' ')
                        elif key != "DocID":
                            print(key + ':' + "NA", end=' ')

                elif len(select) == 0:
                    for key in row.keys():
                        if key != "DocID":
                            print(key + ':' + row[key], end=' ')

                else:
                    for key in select:
                        if key in row.keys():
                            print(key + ':' + row[key], end=' ')
                        elif key != "DocID":
                            print(key + ':' + "NA", end=' ')
                print()
        print()

    def insertrow(self, row):
        if "DocID" in row.keys():
            dcid = row["DocID"]
            if dcid in self.db.keys():
                print("Duplicate DocID Error")
                return
            if int(dcid) > self.docid:
                self.docid = int(dcid)
            del row["DocID"]
            self.db[str(dcid)] = row
            return dcid
        else:
            dcid = self.docid + 1
            self.docid += 1
            self.db[str(dcid)] = row
            return dcid