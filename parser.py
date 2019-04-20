class parser:

    def parse(self, line):
        l = line.split('.')
        if l[0] != "final":
            print("Wrong collection name")
            return

        l = l[1]
        operation = l[:l.index('(')]
        print(operation)
