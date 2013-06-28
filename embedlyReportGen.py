from embedly import Embedly
import csv
eKey = "e32471062181449a9fb1b7d0987fe894"
client = Embedly(eKey)
f = open('LinksFromTwitter.html', 'w', )
with open("linkWD.csv") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    L = {}
    print('<html>', file=f)
    print(' <head>', file=f)
    print(' <title>' + "Description of most popular links from Twitter" + '</title>', file=f)
    print('</head>', file=f)
    print(' <body>', file=f)
    for row in csvReader:
        obj = client.oembed(row[0])
        Title = obj['title']
        Descr = obj['description']
        print('  <hr>', file=f)
        sTitle = str(Title.encode("ascii", "xmlcharrefreplace"))
        print('   <p>', file=f)
        print(sTitle[2:-1], file=f)
        print('   </p>', file=f)
        sDescr = str(Descr.encode("ascii", "xmlcharrefreplace"))
        print('   <p>', file=f)
        print(sDescr[2:-1], file=f)
        print('   </p>', file=f)
        if 'thumbnail_url' in obj:
            Thumb = obj['thumbnail_url']
            print('   <img src="%s">' % Thumb, file=f)
    print(' </body>', file=f)
    print('</html>', file=f)
f.close()