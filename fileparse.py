class fileparse:

    @staticmethod
    def parsefile(filename):
        db = {}
        datafile = open(filename, "r")
        lines = datafile.readlines()
        for line in lines:
            tmp = {}
            spl = line.split()
            for x in spl:
                x = x.split(':')
                tmp[x[0]] = x[1]

            docid = tmp["DocID"]
            del tmp["DocID"]
            db[docid] = tmp
        return db



