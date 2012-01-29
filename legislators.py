from BeautifulSoup import BeautifulSoup
import os 
import json

# settings for this file
extension = '.xml'
years = [
  1990,
  1991,
  1992,
  1993,
  1994,
  1995,
  1996,
  1997,
  1998,
  1999,
  2000,
  2001,
  2002,
  2003,
  2004,
  2005,
  2006,
  2007,
  2008,
  2009,
  2010,
  2011,
  2012
]

### Utility Functiosn ###

# only scan xml files
def isValid(f):
    if f.endswith(extension) and not f.startswith('.'):
        return True

# merge two lists
def merge(a,b):
    return list(set(a+b))

### End Utility Functiosn ###

# make stats directory
if not os.path.exists('stats'):
    os.makedirs(stats)

for year in years:
    print year
    legislators = []

    # get valid files
    fnames = filter(isValid, os.listdir('data/' + str(year)))

    # get statistics for each file
    for fname in fnames:
        f = open('data/' + str(year) + '/' + fname, 'r')
        soup = BeautifulSoup(f.read())
        legs = soup('legislator')
        new_legs = map(lambda leg: leg.string, legs)
        legislators = merge(legislators, new_legs)
    
    legislators.sort()
    f = open('stats/' + str(year) + '-legislators', 'w')
    f.write(json.dumps(legislators))
