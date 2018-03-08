import csv

def parser(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, skipinitialspace=True):
        if line:
            yield line

def listerTab(flst):
    samples = {}   
    for filename in flst:
        with open(filename) as f:
            for line in f:
                    try:
                    	probeid, intensity = line.split("\t")
                    	probeid, intensity = str(probeid), float(intensity.strip('\n'))
                    	if probeid in samples.keys():
                            samples[probeid] += [intensity,]
                        else:
                            samples[probeid] = [intensity,]
                    except ValueError: pass
        f.close()
    return samples

def listerComma(filename):
    samples = {}   
    for filename in flst:
        with open(filename) as f:
            for line in f:
                    try:
                    	probeid, intensity = line.strip.split(",")
                    	probeid, intensity = str(probeid), float(intensity.strip('\n'))
                    	if probeid in samples.keys():
                            samples[probeid] += [intensity,]
                        else:
                            samples[probeid] = [intensity,]
                    except ValueError: pass
        f.close()
    return samples
