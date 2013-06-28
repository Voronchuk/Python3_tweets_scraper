import csv, ast

with open("linkWD.csv") as csvfile:
    userreader = csv.reader(csvfile, delimiter=';')
    reweightedLinks = {}
    Weight = {}
    maxWeigthTolerance = 2
    maxWeigth = 0
    for row in userreader:
        link = row[0]
        wd = row[1]
        WD = ast.literal_eval(wd)
        W = WD[0]
        if (maxWeigth < W):
            maxWeigth = W
        Weight[link] = W
        
BigWeight = {}
levelOfFiltration = maxWeigth - maxWeigthTolerance
if (levelOfFiltration) < 2:
    levelOfFiltration = 2
for link in Weight:
    w = Weight[link]
    if w >= levelOfFiltration:
        BigWeight[link] = w
        
print(BigWeight)
