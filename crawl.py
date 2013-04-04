import urllib

f = urllib.urlopen("http://www.google.com")
of = open('web1','w')
of.write(f.read())


#	step 0:
#		checking the page for specific keywords

	
'''
	step 1:
		getting all absolute fresh urls from the page and save them in a stack(BFS)
	step 2:
		recursive calls to all urls till a certain depth
'''
