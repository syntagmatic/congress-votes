import urllib2
import os
from time import sleep

year_max = {
  1990: 536,
  1991: 444,
  1992: 488,
  1993: 615,
  1994: 507,
  1995: 885,
  1996: 455,
  1997: 640,
  1998: 547,
  1999: 611,
  2000: 603,
  2001: 512,
  2002: 484,
  2003: 677,
  2004: 544,
  2005: 671,
  2006: 543,
  2007: 1186,
  2008: 690,
  2009: 991,
  2010: 664,
  2011: 949,
  2012: 4,
}

def getpage(url):
    try:
        print url
        data = urllib2.urlopen(url, None, 15).read()
        return data
    except:
        print 'failed, trying again'
        return getpage(url)

for year, max_roll in year_max.iteritems():
    try:
        os.mkdir(str(year))
    except:
        pass
    for roll_url in range(1,max_roll+1,1):
        if roll_url < 1000:
            name = str(year) + '/roll' + str(roll_url).zfill(3) + '.xml'
        else:
            name = str(year) + '/roll' + str(roll_url).zfill(4) + '.xml'

        data = getpage('http://clerk.house.gov/evs/' + name)

        file = open('data/' + name, 'w')
        file.write(data)
