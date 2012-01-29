import urllib2
from BeautifulSoup import BeautifulSoup

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

for year, max_roll in year_max.iteritems():
  for roll_url in range(0,max_roll+1,100):
    if roll_url < 1000:
      url = 'http://clerk.house.gov/evs/' + str(year) + '/ROLL_' + str(roll_url).zfill(3) + '.asp'
    else:
      url = 'http://clerk.house.gov/evs/' + str(year) + '/ROLL_' + str(roll_url).zfill(4) + '.asp'
    soup = BeautifulSoup(urllib2.urlopen(url))
    print soup
