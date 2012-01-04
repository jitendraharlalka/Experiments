#! /usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import locale
import sys
import simplejson,urllib,urllib2

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

possibleValues=["Nepal","Nepali","Kathmandu","Pokhara", "Chitwan","नेपाल","पोखरा","चितवन","काठमाडौं","काठमाण्डू"]
lines=[]
try:
	frd=open('since_id.txt','r')
	lines=frd.readlines()
	frd.close()
except IOError:
	pass

fwr=open('since_id.txt','w')

urlbase="http://search.twitter.com/search.json"

x=unicode('')
for p in range(len(possibleValues)):
	try:
		sinceId=lines[p]
	except IndexError:
		sinceId=0
	values={'since_id':sinceId,'q':possibleValues[p]}
	data=urllib.urlencode(values)
	req=urllib2.Request(urlbase,data)
	response=urllib2.urlopen(req)
	page=simplejson.load(response)	
	print "\n"

	since=page['max_id_str']
	fwr.write(since+"\n")
	results=page['results']
	for i in range(len(results)):
		x=x+unicode(results[i]['text'])+"\n"
		print '\"@'+results[i]['from_user']+": "+unicode(results[i]['text'])+'\"\n'

fwr.close()

