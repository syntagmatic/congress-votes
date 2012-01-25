from BeautifulSoup import BeautifulSoup
import os 
import json

# settings for this file
extension = '.xml'

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

vote_key = {
  'No': 0,
  'Nay': 0,
  'Aye': 1,
  'Yea': 1,
  'Not Voting': 3,
  'Present': 4
}

### Utility Functiosn ###

# only scan xml files
def isValid(f):
    if f.endswith(extension) and not f.startswith('.'):
        return True

### End Utility Functiosn ###

for year, max_roll in year_max.iteritems():
    legislators = json.load(open('stats/' + str(year) + '-legislators', 'r'))
    print year, len(legislators)

    votes = {}
    for leg in legislators:
        votes[leg] = [None]*max_roll

    # get statistics for each file
    for roll_url in range(1,max_roll+1,1):
        print roll_url
        if roll_url < 1000:
            fname = str(year) + '/roll' + str(roll_url).zfill(3) + '.xml'
        else:
            fname = str(year) + '/roll' + str(roll_url).zfill(4) + '.xml'
        f = open('data/' +  fname, 'r')
        soup = BeautifulSoup(f.read())
        roll_votes = soup('recorded-vote')
        for roll_vote in roll_votes:
            leg = roll_vote('legislator')[0].string
            vote = roll_vote('vote')[0].string
            if vote in vote_key:
                votes[leg][int(roll_url)-1] = vote_key[vote]
            else:
                votes[leg][int(roll_url)-1] = vote

    f = open('stats/' + str(year) + '-matrix', 'w')
    f.write(json.dumps(votes))
