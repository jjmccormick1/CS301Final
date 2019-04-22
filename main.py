import parser



def main():
    queries = open("queries.txt", "r")
    lines = queries.readlines()
    for line in lines:
        parser.parse(line)


main()

