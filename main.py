import parser



def main():
    queries = open("queries.txt", "r")
    lines = queries.readlines()
    for line in lines:
        par = parser.parser
        par.parse(par, line)


main()

