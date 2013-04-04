import urllib
from HTMLParser import HTMLParser

#f = urllib.urlopen("http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=24592&copyownerid=2")
#f = urllib.urlopen("http://www.iitk.ac.in");
#of = open('web1','w')
#of.write(f.read())
#of.close()

fin = open('web1','r') 

class MyHTMLParser(HTMLParser):

	def handle_starttag(self,tag,attrs):

		if tag == "a":
			for attr in attrs:
            			if attr[0] == "href":
					print attr

	#def handle_endtag(self, tag):
        #	print "End tag  :", tag

	#def handle_data(self, data):
        #	print "Data     :", data

parser = MyHTMLParser()

for line in fin.readlines():
	parser.feed(line)


#	step 0:
#		checking the page for specific keywords


	
'''
	step 1:
		getting all absolute fresh urls from the page and save them in a stack(BFS)
	step 2:
		recursive calls to all urls till a certain depth
'''
