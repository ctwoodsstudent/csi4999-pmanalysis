from Bio import phenotype
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from Bio.phenotype.pm_fitting import gompertz
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

def main():
    plates, file = getFile()
    mainMenu(plates, file)

def getFile():
    filename = input('Please name of microarray file (must have extension .csv or .json): ')
    if filename.lower() == 'q': exit()
    #if len(filename.split('.')) == 1:
    #    filename += '.'
    extension = filename.split('.')[1]
    try:
        if extension == 'csv':
            print('\nPlate\tNumber of wells')
            for plate in phenotype.parse(filename, 'pm-csv'):
                print('%s\t%d'%(plate.id, len(plate)))
            print()
            file = phenotype.parse(filename, 'pm-csv')
            plates = list(phenotype.parse(filename, 'pm-csv'))
            return plates, file
        elif extension == 'json':
            print('Plate\tNumber of wells')
            for plate in phenotype.parse(filename, 'pm-json'):
               print('%s\t%d'%(plate.id, len(plate)))
            file = phenotype.parse(filename, 'pm-json')
            plates = list(phenotype.parse(filename, 'pm-json'))
            return plates, file
        else:
            print('Not valid file format!')
            getFile()
    except IOError:
        print('Could not read file.')
        getFile()
    except:
        print('Unexpected error!')
        getFile()

def mainMenu(plates, file):
    menu = {'1' : '[1] Open Plate Data',
            '2' : '[2] Write Plate Data',
            '3' : '[3] Plot Area under the Curve',
            '4' : '[4] Plot Simple Growth',
            '5' : '[5] Plot Parameter Correlations',
            '6' : '[6] Plot Well Cluster',
            '7' : '[7] Plot Single Wells by Cluster',
            'q' : '[q] Quit'}
    for value in menu.values():
        print(value)
    opt = input('Enter an option: ')
    print()
    if opt.lower() in menu.keys():
        if opt == '1':
            openPlate(plates, file)
        elif opt == '2':
            writePlate(plates, file)
        elif opt == '3':
            plotAuC(plates, file)
        elif opt == '4':
            plotGrowth(plates, file)
        elif opt == '5':
            plotParameters(plates, file)
        elif opt == '6':
            plotWellCluster(plates, file)
        elif opt == '7':
            plotSingleWells(plates, file)
        else: exit()
    else:
        print('Enter valid option!')
        mainMenu()

def openPlate(plates, file):
    plate_options = {}
    counter = 1
    for plate in plates:
        plate_options[str(counter)] = '[' + str(counter) + ']\t' + plate.id
        counter += 1
    for value in plate_options.values():
        print(value)
    plate_key = input('Choose Plate to open: ')
    if plate_key in plate_options.keys():
        plate = plates[int(plate_key)-1]
        print('Plate\tWell\tNumber of Time Points')
        for well in plate:
            print('%s\t%s\t%d'%(plate.id, well.id, len(well)))
        menu = {'1' : '[1] Print Complete Well',
                '2' : '[2] Print Well Data Summary',
                '3' : '[3] Back to Main Menu'}
        for value in menu.values():
            print(value)
        opt = ''
        while opt not in menu.keys():
            opt = input('Enter an option: ')
            if opt in menu.keys():
                if opt == '1':
                    printWell(plate, plates, file)
                elif opt == '2':
                    printWellData(plate, plates, file)
                elif opt == '3':
                    mainMenu(plates, file)
                elif opt.lower() == 'q': exit()
            elif opt.lower() == 'q': exit()
            else: print('Enter valid option!')
    elif plate_key.lower() == 'q': exit()
    else:
        print('Invalid Plate option!')
        openPlate(plates, file)
           
def printWell(plate, plates, file):
    print('Option\tWell\tNumber of Time Points')
    well_options = {}
    counter = 1
    for well in plate:
        well_options[str(counter)] = well.id
        print('%s\t%s\t%d'%('['+str(counter)+']', well.id, len(well)))
        counter += 1
    opt = ''
    while opt not in well_options.keys():
        opt = input('Choose Well to open: ')
        if opt in well_options.keys():
            well = plate[well_options[opt]]
            print('Time\tSignal')
            for time, signal in well:
                print(str(time) + '\t' + str(signal))
            input()
        elif opt.lower == 'q': exit()
        else: print('Invalid Well option!')
    mainMenu(plates, file)

def printWellData(plate, plates, file):
    print('Option\tWell\tNumber of Time Points')
    well_options = {}
    counter = 1
    for well in plate:
        well_options[str(counter)] = well.id
        print('%s\t%s\t%d'%('['+str(counter)+']', well.id, len(well)))
        counter += 1
    opt = ''
    while opt not in well_options.keys():
        opt = input('Choose Well to analyze: ')
        if opt in well_options.keys():
            well = plate[well_options[opt]]
            well.fit()
            print('Function fitted: %s\n'%well.model)
            print('Parameter\tValue')
            for param in ['area', 'average_height',
                          'lag', 'max', 'min',
                          'plateau', 'slope']:
                print('%s\t\t%.2f'%(param, getattr(well, param)))
            input()
        elif opt.lower == 'q': exit()
        else: print('Invalid Well option!')
    mainMenu(plates, file)
                
def writePlate(plates, file):
    plate_options = {}
    counter = 1
    for plate in plates:
        plate_options[str(counter)] = '[' + str(counter) + '] ' + plate.id
        counter += 1
    for value in plate_options.values():
        print(value)
    plate_key = ''
    while plate_key not in plate_options:
        plate_key = input('Choose Plate to write to JSON file: ')
        if plate_key in plate_options:
            plate = plates[int(plate_key)-1]
            filename = input('Enter name for file: ')
            filename += '.json'
            phenotype.write(plate, filename, 'pm-json')
            print('File created in default directory\n')
        elif plate_key.lower() == 'q': exit()
        else: print('Invalid Plate option!')
    mainMenu(plates, file)

def plotAuC(plates, file):
    params = []
    for plate in file:
        for well in plate:
            try:
                well.fit()
            except RuntimeError:
                pass
            params.append((plate.id,
                       well.id,
                       well.model,
                       well.area,
                       well.average_height,
                       well.slope,
                       well.lag,
                       well.min,
                       well.max,
                       well.plateau))
    params = pd.DataFrame(params)
    params.columns = ['plate', 'well',
                  'model',
                  'area', 'avg. height',
                  'slope', 'lag',
                  'min', 'max',
                  'plateau']
    #sns.set_style('white')
    #plt.rc('font', size=15)
    #plt.rc('xtick', labelsize=15)
    #plt.rc('ytick', labelsize=15)
    #plt.rc('axes', labelsize=16, titlesize=16)
    #plt.rc('legend', fontsize=15)
    #plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    vmax = params.area.max()
    for plateid, i in zip(sorted(set(params.plate)), range(1, len(set(params.plate))+1)):
        plt.subplot(len(set(params.plate))/2, 2, i)
        sns.heatmap(params[params.plate == plateid]['area'].as_matrix().reshape(16, 12), #8, 12, #16, 12
                    vmin=0,
                    vmax=vmax,
                    cmap=plt.get_cmap('Reds'),
                    xticklabels=[str(x) for x in range(1, 13)],
                    yticklabels=[x for x in 'ABCDEFGHIJKLMNOP']) #ABCDEFGHIJKLMNOP
        plt.title(plateid)
    plt.show()
    mainMenu(plates, file)

def plotGrowth(plates, file):
    params = []
    for plate in file:
        for well in plate:
            try:
                well.fit()
            except RuntimeError:
                pass
            params.append((plate.id,
                       well.id,
                       well.model,
                       well.area,
                       well.average_height,
                       well.slope,
                       well.lag,
                       well.min,
                       well.max,
                       well.plateau))
    params = pd.DataFrame(params)
    params.columns = ['plate', 'well',
                  'model',
                  'area', 'avg. height',
                  'slope', 'lag',
                  'min', 'max',
                  'plateau']
    #sns.set_style('white')
    #plt.rc('font', size=15)
    #plt.rc('xtick', labelsize=15)
    #plt.rc('ytick', labelsize=15)
    #plt.rc('axes', labelsize=16, titlesize=16)
    #plt.rc('legend', fontsize=15)
    #plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    threshold = 8000
    params['growth'] = params.area > threshold
    plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    for plateid, i in zip(sorted(set(params.plate)), range(1, len(set(params.plate))+1)):
        plt.subplot(len(set(params.plate))/2, 2, i)
        sns.heatmap(params[params.plate == plateid]['growth'].as_matrix().reshape(8, 12),
                    vmin=0,
                    vmax=1,
                    cmap=plt.get_cmap('Greens'),
                    xticklabels=[str(x) for x in range(1, 13)],
                    yticklabels=[x for x in 'ABCDEFGH'],
                    cbar=False)
        plt.title(plateid)
    plt.show()
    mainMenu(plates, file)

def plotParameters(plates, file):
    params = []
    for plate in file:
        for well in plate:
            try:
                well.fit()
            except RuntimeError:
                pass
            params.append((plate.id,
                       well.id,
                       well.model,
                       well.area,
                       well.average_height,
                       well.slope,
                       well.lag,
                       well.min,
                       well.max,
                       well.plateau))
    params = pd.DataFrame(params)
    params.columns = ['plate', 'well',
                  'model',
                  'area', 'avg. height',
                  'slope', 'lag',
                  'min', 'max',
                  'plateau']
    #sns.set_style('white')
    #plt.rc('font', size=15)
    #plt.rc('xtick', labelsize=15)
    #plt.rc('ytick', labelsize=15)
    #plt.rc('axes', labelsize=16, titlesize=16)
    #plt.rc('legend', fontsize=15)
    #plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    params = params[(params.lag > 0) &
                    (params.lag < well.get_times()[-1]) &
                    (params.slope > 0) &
                    (params.plateau > 0)].dropna()
    standardized = preprocessing.scale(params[params.columns[3:-1]])
    standardized = pd.DataFrame(standardized)
    standardized.columns = params.columns[3:-1]
    plt.figure(figsize=(10, 10))
    pairplot = sns.pairplot(standardized,
                        plot_kws=dict(alpha=0.66),
                        diag_kws=dict(shade=True),
                        diag_kind='kde')
    plt.show()
    mainMenu(plates, file)

def plotWellCluster(plates, file):
    params = []
    for plate in file:
        for well in plate:
            try:
                well.fit()
            except RuntimeError:
                pass
            params.append((plate.id,
                       well.id,
                       well.model,
                       well.area,
                       well.average_height,
                       well.slope,
                       well.lag,
                       well.min,
                       well.max,
                       well.plateau))
    params = pd.DataFrame(params)
    params.columns = ['plate', 'well',
                  'model',
                  'area', 'avg. height',
                  'slope', 'lag',
                  'min', 'max',
                  'plateau']
    #sns.set_style('white')
    #plt.rc('font', size=15)
    #plt.rc('xtick', labelsize=15)
    #plt.rc('ytick', labelsize=15)
    #plt.rc('axes', labelsize=16, titlesize=16)
    #plt.rc('legend', fontsize=15)
    #plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    standardized = preprocessing.scale(params[params.columns[3:-1]])
    standardized = pd.DataFrame(standardized)
    standardized.columns = params.columns[3:-1]
    kmeans = KMeans(n_clusters=3).fit(standardized[['area', 'slope', 'lag', 'plateau']])
    standardized['cluster'] = kmeans.labels_
    params['cluster'] = kmeans.labels_
    pairplot = sns.pairplot(standardized,
                        vars=['area', 'slope', 'lag', 'plateau'],
                        plot_kws=dict(alpha=0.66),
                        diag_kws=dict(shade=True),
                        diag_kind='kde',
                        hue='cluster')
    plt.show()
    mainMenu(plates, file)

def plotSingleWells(plates, file):
    params = []
    for plate in file:
        for well in plate:
            try:
                well.fit()
            except RuntimeError:
                pass
            params.append((plate.id,
                       well.id,
                       well.model,
                       well.area,
                       well.average_height,
                       well.slope,
                       well.lag,
                       well.min,
                       well.max,
                       well.plateau))
    params = pd.DataFrame(params)
    params.columns = ['plate', 'well',
                  'model',
                  'area', 'avg. height',
                  'slope', 'lag',
                  'min', 'max',
                  'plateau']
    #sns.set_style('white')
    #plt.rc('font', size=15)
    #plt.rc('xtick', labelsize=15)
    #plt.rc('ytick', labelsize=15)
    #plt.rc('axes', labelsize=16, titlesize=16)
    #plt.rc('legend', fontsize=15)
    #plt.figure(figsize=(14, 5*len(set(params.plate))/2))
    standardized = preprocessing.scale(params[params.columns[3:-1]])
    standardized = pd.DataFrame(standardized)
    standardized.columns = params.columns[3:-1]
    kmeans = KMeans(n_clusters=3).fit(standardized[['area', 'slope', 'lag', 'plateau']])
    plt.figure(figsize=(7, 7))
    colors = {x:sns.color_palette(n_colors=len(set(kmeans.labels_)))[x]
        for x in range(len(set(kmeans.labels_)))}
    for plate in file:
        for well in plate:
            tmp = params[(params.plate == plate.id) &
                 (params.well == well.id)]
            if tmp.shape[0] == 0:
                continue
            cluster = tmp.cluster.as_matrix()[0]
            color = colors.get(cluster, 'grey')
            five_minutes = np.arange(0, max(well.get_times()), 0.083)
            plt.plot(five_minutes,
                     well[::0.083],
                     '-',
                     color=color,
                     lw=3,
                     alpha=0.3)
    plt.xlabel('Time (hours)')
    plt.ylabel('Signal')
    plt.axis('auto')
    sns.despine()
    plt.show()
    mainMenu(plates, file)
