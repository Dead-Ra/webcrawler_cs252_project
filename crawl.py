import sys
import urllib2,urllib
from HTMLParser import HTMLParser
#import Queue
#from Queue import Queue
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
wordsearch = ['important','date','submission','deadline','timeline','time','calender'] #event
url_list = list()
url_list_all = []
priority_list = list()
result_list = list()
found = 0;
curr_page_url = "";
curr_depth = 0;max_depth=3;		#max limit 3
flag2=0;

#date

# "^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$" for dd-mm-yyyy
# "^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$" for yyyy-mm-dd

# get the first url

#enque first link
#url_list.put('http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=24592&copyownerid=2');
#url_list.put('http://2011.comad.in/');
#url_list.append('http://groups.drupal.org/node/290703');
#url_list.append('https://webmail.iitk.ac.in')......................still not working
#url_list.put('http://www.conferencealerts.com/show-event?id=116000')
#url_list.put('http://www.conferencealerts.com/topic-listing?topic=Anthropology')
#url_list.append('http://www.baidu.com/s?wd=google&rsv_bp=0&ch=&tn=baidu&bar=&rsv_spt=3&ie=utf-8&rsv_sug3=4&inputT=887')
url_list.append('http://www.vldb.org/2013/')
url_list.append('-----c-----');
#print url_list
url_list_all.append('http://www.vldb.org/2013/');


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
							url_list.append(url)
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
			for w in wordsearch:
				if (w in data.lower()):
					a=9
					#move from normal list to priority list
					#print "Data------->", data
					#priority_list.append(url_list.pop())
					

#if keywords are in link then don't mark the current page. Mark them only when it is in this page and not in hypertext way
		else:
			flag_res=0
			for w in wordsearch:
				if w in data.lower():
					flag_res=1
					print data.lower()
			if(flag_res ==1 and (curr_page_url not in result_list)):
				result_list.append(curr_page_url)
				print result_list;
			#	sys.exit()

##############################################################

parser = MyHTMLParser()


while(len(url_list) != 0 and curr_depth < max_depth):

	curr_page_url = url_list.pop(0)
	#print '___________',curr_page_url,'___________'
	if(curr_page_url == '-----c-----'):
		#print "PPPPPPPPPRRRRRRRRRRRIIIIIIIIIIIOOOOOOOOOOOOOOOORRRRRRRRRRRR"
		#print result_list
		url_list.insert(len(url_list),'-----c-----')
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
#				print line
#				try:
				parser.feed(line)
#				except:
			#	parser.feed(line.decode('utf-8'))
