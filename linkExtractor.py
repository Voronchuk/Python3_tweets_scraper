from twitter import *
import re, csv, datetime, urllib
from collections import defaultdict
OAUTH_TOKEN = "1513204759-h9ZZ9CogfwusWs1UtYgsoOCroVeROnZUGMQuyVa"
OAUTH_SECRET = "4mv0MweDD1Bv32pm3bfNLVVlPL0W4MWYEhSL93YXF08"
CONSUMER_KEY = "nrugycAyJrzQRqTkbOHWQ"
CONSUMER_SECRET = "XW4x4VLqVCFrCuVWCCyXrq6Pt5ky1SvukaOTRq9OU"
t = Twitter(
    auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET)
)
httpLinkPattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
dateFormat = '%a %b %d %H:%M:%S %z %Y'
WD = defaultdict(list)
maxWeigth = 0
csvUrlPref = 'https://twitter.com/'
lenOfcsvUrlPref = len(csvUrlPref)
with open('user.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')
    for row in csvReader:
        csvurl = row[1]
        suffix = csvurl[lenOfcsvUrlPref:]
        sName = suffix
        tCount = 1000
        r = t.statuses.user_timeline(screen_name=sName, count=tCount)
        for tweet in r:
            text = tweet['text']
            h = re.findall(httpLinkPattern, text)
            if h:
                for tweetLink in h:
                    try:
                        httpObj = urllib.request.urlopen(tweetLink)
                        url = httpObj.geturl()
                        headers = httpObj.getheaders()
                    except Exception as exc:
                        continue;
                    url = httpObj.geturl()
                    for hItems in headers:
                        if 'text/html' in hItems:
                            dateStr = tweet['created_at']
                            date = datetime.datetime.strptime(dateStr, dateFormat)
                            if url in WD:
                                WD[url][0] += 1
                                edate = datetime.datetime.strptime(WD[url][1], dateFormat)
                                delta = edate - date
                                seconds = delta.total_seconds()
                                if (seconds > 0):
                                    WD[url][1] = dateStr
                            else:
                                WD[url] = [1, dateStr]
                            if (maxWeigth < WD[url][0]):
                                maxWeigth = WD[url][0]
with open('linkWD.csv', 'w') as csvfile:
    csvWriter = csv.writer(csvfile, lineterminator=';\n', delimiter=";")
    for key, value in WD.items():
        csvWriter.writerow([key, value])