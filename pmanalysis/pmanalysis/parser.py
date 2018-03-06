import csv

def parser(Pfile, separator):
    for line in csv.reader(open(Pfile), delimiter=separator, skipinitialspace=True):
        if line:
            yield line



def listerTab(Pfile):
    for data in parser(Pfile, '    '):
        lst1 = []
        lst2 = []
        counter = 0
        if counter % 2 == 0:
            lst1.append(data)
        if counter % 2 == 1:
            lst2.append(data)
        counter += 1
    return lst1, lst2

def listerComma(Pfile):
    for data in parser(Pfile, ','):
        lst1 = []
        lst2 = []
        counter = 0
        if counter % 2 == 0:
            lst1.append(data)
        if counter % 2 == 1:
            lst2.append(data)
        counter += 1
        return lst1, lst2
