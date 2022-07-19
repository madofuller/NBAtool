import mechanize as mc
from bs4 import BeautifulSoup as bs


br = mc.Browser()

br.set_handle_robots(False) 
br.open('https://invistavisibility.lightning.force.com/lightning/r/SalesAgreementAggregate__c/a0U4V00000GT6nOUAT/view')
html = br.read()
test = open('test.html', 'wb')
print >> test, "%s" % (bs(html).prettify())  
test.close()