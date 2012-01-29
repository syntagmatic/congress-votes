from BeautifulSoup import BeautifulSoup
import os 
import json

# settings for this file
extension = '.xml'

year_max = {
#  1990: 536,
#  1991: 444,
#  1992: 488,
#  1993: 615,
#  1994: 507,
#  1995: 885,
#  1996: 455,
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

def legislation_info(year, roll_url):
    leg_info = {}
    print roll_url
    if roll_url < 1000:
        fname = str(year) + '/roll' + str(roll_url).zfill(3) + '.xml'
    else:
        fname = str(year) + '/roll' + str(roll_url).zfill(4) + '.xml'
    f = open('data/' +  fname, 'r')
    soup = BeautifulSoup(f.read())('vote-metadata')[0].extract()
    leg_info = {
        'roll': soup('rollcall-num')[0].string,
        'majority': soup('majority')[0].string,
        'question': soup('vote-question')[0].string,
        'vote-type': soup('vote-type')[0].string,
        'vote-result': soup('vote-result')[0].string,
        'action-date': soup('action-date')[0].string,
        'action-time': soup('action-time')[0].string,
        'vote-desc': soup('vote-desc')[0].string,
    }
    if len(soup('legis-num')) < 1:
        leg_info['totals-by-candidate'] = {}
        for totals in soup('totals-by-candidate'):
            candidate = totals('candidate')[0].string
            votes = totals('candidate-total')[0].string
            leg_info['totals-by-candidate'][candidate] = votes
    else:
        leg_info['legis-num'] = soup('legis-num')[0].string
        leg_info['yea-total'] = soup('yea-total')[0].string
        leg_info['nay-total'] = soup('nay-total')[0].string
        leg_info['present-total'] = soup('present-total')[0].string
        leg_info['not-voting-total'] = soup('not-voting-total')[0].string
        leg_info['totals-by-party'] = {}
        for totals in soup('totals-by-party'):
            party = totals('party')[0].string
            leg_info['totals-by-party'][party] = {
                'yea-total': totals('yea-total')[0].string,
                'nay-total': totals('nay-total')[0].string,
                'present-total': totals('present-total')[0].string,
                'not-voting-total': totals('not-voting-total')[0].string,
            }
    del soup
    return leg_info

for year, max_roll in year_max.iteritems():
    print '---'
    print year
    print '---'
    legislation = {}

    for roll_url in range(1,max_roll+1,1):
        legislation[roll_url] = legislation_info(year, roll_url)

    f = open('stats/' + str(year) + '-legislation', 'w')
    f.write(json.dumps(legislation))
