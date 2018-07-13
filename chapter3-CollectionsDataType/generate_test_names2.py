import random

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"),(surnames, "data/surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
    return forenames, surnames

fornames, surnames = get_forenames_and_surnames()
fh = open("data/text-names2.txt","w",encoding="utf8")
limit = 100
years = list(range(1970, 2018)) * 3
for year, forname, surname in zip(
        random.sample(years,limit), 
        random.sample(fornames,limit), 
        random.sample(surnames,limit- 30)):
    name = "{0} {1}".format(forname,surname)
    fh.write("{0:.<25}.{1}\n".format(name, year))