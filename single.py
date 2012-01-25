import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://clerk.house.gov/evs/2001/roll342.xml'
soup = BeautifulSoup(urllib2.urlopen(url))

roll = {}

for vote in soup('recorded-vote'):
    roll[vote.legislator.string] = vote.vote.string

print roll
