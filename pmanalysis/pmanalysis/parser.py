import csv

def parser(filename, separator):
    for line in csv.reader(open(Pfile), delimiter=separator, skipinitialspace=True):
        if line:
            yield line



def listerTab(filename):
    sample = []
    with open(filename) as f:
	for line in f:
		try:
			probeid, intensity = line.split("\t")
			sample.append( (str(probeid), float(intensity.strip('\n'))) )
		except ValueError: pass
    return sample

def listerComma(filename):
    sample = []
    with open(filename) as f:
	for line in f:
		try:
			probeid, intensity = line.strip.split(",")
			sample.append( (str(probeid), float(intensity.strip('\n'))) )
		except ValueError: pass
    return sample
