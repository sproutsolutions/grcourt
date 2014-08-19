import csv, os, re, urllib2, urllib
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
os.chdir("C:\Users\TPB\Desktop\scrape")
print "We are in the right spot"
site = urllib.urlopen('http://grcourt.org/CourtPayments/loadCase.do?caseSequence=1')
print site.read()
print type(site)


req = urllib2.Request('http://grcourt.org/CourtPayments/loadCase.do?caseSequence=1')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page