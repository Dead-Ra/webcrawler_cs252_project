import sys
import urllib2,urllib
from HTMLParser import HTMLParser
import urlparse
from urlparse import urljoin
import re
import json

sys.stderr = sys.stdout

#setting proxy connection
proxy = urllib2.ProxyHandler({'https': 'http://dibya:dibya78@proxy.iitk.ac.in:3128',
			      'http': 'http://dibya:dibya78@proxy.iitk.ac.in:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler,urllib2.HTTPSHandler,urllib2.HTTPRedirectHandler)
urllib2.install_opener(opener)
#proxy connection made

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


#declaring variables
wordsearch = ['submission deadline','deadline','timeline','important date','calender'] #event,important,event,date,time
linksearch = ['submission','deadline','timeline','calender','important','event','date']
url_list = list()
url_list_all = []
priority_list = list()
fav_list= list()
found = 0;
curr_page_url = "";
curr_depth = 0;max_depth=2;		#max limit 3
flag2=0;
flag_res=0;
word_found=0;
loc = 0;
word = "";
count = 0;
#date

date1 = "(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d" # mm-dd-yyyy
date2 = "[0123]*[0-9][- /.](0[1-9]|1[012])[- /.](19|20)\d\d" # dd-mm-yyyy ([1-9]|0[1-9]|[12][0-9]|3[01])
date3 = "[0-9]+(st|nd|rd|th|)[- /.](jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|may|june|july|august|septempber|october|november|december)[- /.,][\s]*(19|20)\d\d" #dd{..}-{march}-,yyyy
date4 = "(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|may|june|july|august|septempber|october|november|december)[- /.,]([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd| |th|)(,| )[\s]*(19|20)\d\d"
data5 = "(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|may|june|july|august|septempber|october|november|december)[- /.,](0[1-9]|[12][0-9]|3[01]|[1-9])(st|nd|rd| |th|)"


#date6 = "( jan| feb| mar| apr| may| jun| jul| aug| sep| oct| nov| dec| january| february| march| april| may| june| july| august| septempber| october| november| december)[, -/,][\s]*([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd| |th|)"
year = "(2013]|13)"

d1 = re.compile(date1)
d2 = re.compile(date2)
d3 = re.compile(date3) 
d4 = re.compile(date4)
d5 = re.compile(data5)

#Google api search----first go"
query=sys.argv[1]
query1=query.split()
q='+'.join(query1)
gg="https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=large&q="
google=gg+q
#print google
req = urllib2.Request(google, headers=hdr)
try:
	f = urllib2.urlopen(req)
except urllib2.HTTPError, e:
	a=9
        #print e.fp.read()
except urllib2.URLError, e2:
	a=9
	#print "There was an error:", e2


                #storing html page in temporary web1 file
data = json.load(f)
url_to_visit = list()
for i in range(8):
	q1=data["responseData"]["results"][i]["unescapedUrl"]
	url_to_visit.append(q1)
# get the first url

#enque first link
uuu = "";
#o=0;
for o in range(len(url_to_visit)):
	if( ("youtube" not in url_to_visit[o]) and ("pdf" not in url_to_visit[o]) ):
		uuu = url_to_visit[o]
		break
		
url_list.append(uuu)
url_list.append('-----c-----');
#print url_list
print "FIRST LINK"
print uuu
url_list_all.append(uuu);

#function to search for useful data
def search_date(data):
	global d1
	global d2
	global d3
	global d4
	global d5
	m1=d1.search(data);
	m2=d2.search(data);
	m3=d3.search(data);
	m4=d4.search(data);
	m5=d5.search(data);

	if(m1):
		return m1.group()
	elif(m2):
		return m2.group()
	elif(m3):
		return m3.group()
	elif(m4):
		return m4.group()
	elif(m5):
		return m5.group()
	else:
		return 0	

############################################################
class MyHTMLParser(HTMLParser):

	def handle_starttag(self,tag,attrs):

		global flag2

		if tag == "a":
			for attr in attrs:
            			if attr[0] == "href":
					url = urljoin(curr_page_url,attr[1])	#to take care of relativ links
					if (url not in url_list_all):#check for duplicate.
						flag=0
						flag2=1
						for w in wordsearch:
							if w in url:
								flag=1
						if(flag==1):
							priority_list.append(url)
							#url_list.append(url)
							flag2=0
						else:						
							url_list.append(url)
						#print url
						url_list_all.append(url)

		if (tag == "frame" or tag == "iframe"):
			for attr in attrs:
				if attr[0] == "src":
					url = urljoin(curr_page_url,attr[1])
					if (url not in url_list_all):
						flag=0
						flag2=1		# i think this needs to be done........
                                                for w in wordsearch:
                                                        if w in url:
                                                                flag=1
                                                if(flag==1):
                                                        priority_list.append(url)
							flag2=0
                                                else:    
                                                        url_list.append(url)
                                                #print url
                                                url_list_all.append(url)

	def handle_endtag(self, tag):
		global flag2
		if (tag == "a") :
			flag2 = 0

	def handle_data(self, data):
		global flag2
		if (flag2==1):
			#print "link------>",data
			for w in linksearch:
				if (w in data.lower()):
					#move from normal list to priority list
					priority_list.append(url_list.pop())
					break
					

#if keywords are in link then don't mark the current page. Mark them only when it is in this page and not in hypertext way
		else:
		#	global flag_res;
		#	for w in wordsearch:
		#		datal = data.lower()
		#		if w in datal:
		#			flag_res=1
					#print datal
		#	if(flag_res ==1 and (curr_page_url not in result_list)):
		#		match_res = search_date(datal)
		#		if(match_res==1):
		#			print "<h4>"+data+"</h4>"
		#			result_list.append(curr_page_url)
		#			#print curr_page_url
		#			print "IMPORTAT LINKS TO BE DISPLAYED"
		#			#print curr_page_url
		#			for u in fav_list:
		#				print u
		#			sys.exit()
			global flag_res;
			global word_found;
			global word;
			for w in wordsearch:
				datal = data.lower()
				if w in datal:
					#print w+"--->"
					word = w
					word_found=1

##############################################################

parser = MyHTMLParser()

while 1:
	#sys.exit()
	count = count+1
	if(count >= 50):
		print "Sorry, no result found";
                print "IMPORTANT LINKS TO LIST";
                for u in fav_list:
                       print u
                sys.exit();

	while(len(priority_list)!=0):
		curr_page_url = priority_list.pop(0)
		fav_list.insert(0, curr_page_url);
		#print "prior---->"+curr_page_url+"<br>"
		#fetching link
		curr_page_url = urlparse.urlsplit(curr_page_url)
		curr_page_url = curr_page_url.geturl()
	
		req = urllib2.Request(curr_page_url, headers=hdr)
		try:
    			f = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			a=9
    		#	print e.fp.read()
		except urllib2.URLError, e2:
			a=9
    		#	print "There was an error:", e2


		#storing html page in temporary web1 file
		of = open('web1','w')
		of.write(f.read())
		of.close()

		#opening saved html page for parsing
		fin = open('web1','r')

		lines = fin.readlines();
		#print len(lines);
		for x in range(len(lines)):
			try:
				parser.feed(lines[x])
			except:
				pass
			flagte = 0;
			if(word_found==1):
				if (word =="important date" or word =="timeline" or word =="calender"):
					for i in range(0,25):
						line2 = lines[x+i]
						line2=line2.lower()
						#print line2
						if(("submission" in line2) or ("call for" in line2)):
							flagte=1
						if(flagte==1):
							match_res = search_date(line2)
							if(match_res):
								print match_res;
								print "IMPORTANT LINKS TO LIST";
								for u in fav_list:
                			                               print u
								sys.exit();

				elif (word =="deadline" or word =="submission deadline"):
					for i in range(0,5):
						line2 = lines[x+i]
						#print line2
						line2=line2.lower()
						match_res = search_date(line2)
						if(match_res):
							print match_res;
							print "IMPORTANT LINKS TO LIST";
                                                        for u in fav_list:
                                                        	print u
							sys.exit();
				word_found=0;

	if(len(url_list) != 0 and curr_depth < max_depth):

		curr_page_url = url_list.pop(0)
		#print "norm---->"+curr_page_url+"<br>"
		if(curr_page_url == '-----c-----'):
			url_list.insert(len(url_list),'-----c-----')
			curr_depth = curr_depth+1
		else:
			#fetching link
			curr_page_url = urlparse.urlsplit(curr_page_url)
			curr_page_url = curr_page_url.geturl()

		
			req = urllib2.Request(curr_page_url, headers=hdr)
			try:
	    			f = urllib2.urlopen(req)
			except urllib2.HTTPError, e:
				a=9
	    		#	print e.fp.read()
			except urllib2.URLError, e2:
				a=9
	    		#	print "There was an error:", e2


			#storing html page in temporary web1 file
			of = open('web1','w')
			of.write(f.read())
			of.close()

			#opening saved html page for parsing
			fin = open('web1','r')

			#parsing the page for hrefs only
			lines = fin.readlines();
			#print len(lines);
			for x in range(len(lines)):
				try:
					parser.feed(lines[x])
				except:
					pass
				flagte = 0;
				if(word_found==1):
					if (word =="important date" or word =="timeline" or word =="calender"):
						for i in range(0,25):
							line2 = lines[x+i]
							line2=line2.lower()
							#print line2
							if(("submission" in line2) or ("call for" in line2)):
								flagte=1
							if(flagte==1):
								match_res = search_date(line2)
								if(match_res):
									print match_res;
									print "IMPORTANT LINKS TO LIST";
                                                                	for u in fav_list:
                                                                       		print u
									sys.exit();

					elif (word == "deadline" or word == "submission deadline"):
						for i in range(0,5):
							line2 = lines[x+i]
							#print line2
							line2=line2.lower()
							match_res = search_date(line2)
							if(match_res):
								print match_res;
								print "IMPORTANT LINKS TO LIST";
                                                                for u in fav_list:
                                                                       print u
								sys.exit();
					word_found=0;
