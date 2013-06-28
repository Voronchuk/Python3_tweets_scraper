import csv, ast, datetime

dateFormat = '%a %b %d %H:%M:%S %z %Y'
now = datetime.datetime.now(tz=datetime.timezone.utc)
reweightedLinks = {}

with open('linkWD.csv') as csvfile:
    weightreader = csv.reader(csvfile, delimiter=';')
    header = weightreader
    print("header=", header)
    
    for row in weightreader:
        link = row[0]
        wd = row[1]
        WD = ast.literal_eval(wd)
        W = WD[0]
        D = WD[1]
        
        date = datetime.datetime.strptime(D, dateFormat)
        delta = now - date
        seconds = delta.total_seconds()
        h = seconds / 3600
        w = int(W)
        w1 = (w - 1) / pow(h + 2, 1.4)
        
        print('current weigth is ', W, ' current data is ', D)
        print(link)
        
        reweightedLinks[link] = w1
        
print("Reweighted Links:")
print(reweightedLinks)
