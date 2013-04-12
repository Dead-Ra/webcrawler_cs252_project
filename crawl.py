import urllib2,urllib
from HTMLParser import HTMLParser
import Queue
from Queue import Queue
import urlparse
from urlparse import urljoin

###########functions#######################

#### complete_url(url)----> checks for the validity of the url and return the complete url
#	thigs to be checked:-
#		1) '#'
#		2) 'mailto' 
#		3) relative url
#		4) complete url
#-----> can be done by urljoin(base,link) function provided by urlparse module

#### check_dup(url)-----> checks if url is already present or not in url_list

#setting proxy connection
proxy = urllib2.ProxyHandler({'https': 'http://dibya:dibya78@proxy.iitk.ac.in:3128',
			      'http': 'http://dibya:dibya78@proxy.iitk.ac.in:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler,urllib2.HTTPSHandler,urllib2.HTTPRedirectHandler)
urllib2.install_opener(opener)
#proxy connection made

#declaring variables
wordsearch = ['important','date','submission','deadline']
url_list = Queue()
url_list_all = []
priority_list = Queue()
found = 0;
curr_page_url = "";
curr_depth = 0;max_depth=3		#max limit 3


# get the first url

#enque first link
#url_list.put('http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=24592&copyownerid=2');
#url_list.put('http://2011.comad.in/');
#url_list.put('http://groups.drupal.org/node/290703');
#url_list.put('https://webmail.iitk.ac.in')......................still not working
url_list.put('http://www.baidu.com/s?wd=fuck&rsv_bp=0&ch=&tn=baidu&bar=&rsv_spt=3&ie=utf-8&rsv_sug3=10&rsv_sug=0&rsv_sug4=1154&inputT=3537')
url_list.put('-----c-----');
print url_list.queue
url_list_all.append('http://groups.drupal.org/node/290703');


############################################################
class MyHTMLParser(HTMLParser):

	def handle_starttag(self,tag,attrs):

		if tag == "a":
			for attr in attrs:
            			if attr[0] == "href":
					url = urljoin(curr_page_url,attr[1])	#to take care of relativ links
					if (url not in url_list_all):#check for duplicate.
						print url						
						url_list.put(url)
						url_list_all.append(url)
		if tag == "frame":
			for attr in attrs:
				if attr[0] == "src":
					url = urljoin(curr_page_url,attr[1])
					if (url not in url_list_all):
						print url
						url_list.put(url)
						url_list_all.append(url)


	#def handle_data(self, data):
        #	print "Data     :", data

##############################################################

parser = MyHTMLParser()


while(url_list.empty() == 0 and curr_depth < max_depth):

	curr_page_url = url_list.get()
	print '___________',curr_page_url,'___________'
	if(curr_page_url == '-----c-----'):
		 url_list.put('-----c-----')
		 curr_depth = curr_depth+1
	else:
		#fetching link
		curr_page_url = urlparse.urlsplit(curr_page_url)
		curr_page_url = curr_page_url.geturl()

		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

		req = urllib2.Request(curr_page_url, headers=hdr)
		try:
    			f = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
    			print e.fp.read()
		except urllib2.URLError, e2:
    			print "There was an error:", e2


		#storing html page in temporary web1 file
		of = open('web1','w')
		of.write(f.read())
		of.close()

		#opening saved html page for parsing
		fin = open('web1','r')

		#parsing the page for hrefs only
		for line in fin.readlines():

				parser.feed(line.decode('utf-8'))
	
#	step 0:
#		checking the page for specific keywords
