import os

def list_file_movies():
    directory = os.listdir(".")
    for fl in directory:
        if fl[-4:] == ".lst":
            print("Listing movies ... File {0}".format(fl))
            c = 1
            arq = open(fl)
            if  len(arq.read()) > 0:
                for line in arq:
                    print("{0}: {1}".format(c, line), end="")
                    c += 1
            else:
                print("-- no items are in the list --")
            print("\n", end=" ")

def create_file(filename):
    fl = open(filename)
    c = 1
    for line in fl:
        if line: 
            print("{0}: {1}".format(c, line), end="")
            c += 1
        else:
            print("-- no items are in the list --")
    print("\n", end=" ")

def main():
    list_file_movies()
    create_file(input("Choose filename: "))
        
#def get_string():


main()