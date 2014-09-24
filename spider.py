## Program Spider.py
#Jack 
#9.22.14
#start on command line with URL argument 
# Finds pages within a website
###################

import sys 
import urllib2
import urlparse
import htmllib, formatter
from cStringIO import StringIO

def log_stdout(msg):
	#Print message
	print msg
	
def get_page(url, log):
	try:
		page = urllib2.urlopen(url)
	except urllib2.URLError:
		log("Error retrieving: " + url)
		return ''
	body = page.read()
	page.close()
	return body
	
def find_links(html):
	"""return list of links in HTML"""
	writer = formatter.DumbWriter(StringIO())
	f = formatter.AbstractFormatter(writer)
	parser = htmllib.HTMLParser(f)
	parser.feed(html)
	parser.close()
	return parser.anchorlist
	
class Spider:



	def __init__(self, startURL, log=None):
		#set values
		self.URLs = set()
		self.URLs.add(startURL)
		self.include = startURL
		self._links_to_process = [startURL]
		if log is None:
			self.log = log_stdout
		else:
			self.log = log
		
	def run(self):
		while self._links_to_process:
			url = self._links_to_process.pop()
		self.log("Retrieving: " + url)
		self.process_page(url)
	
	def url_in_site(self, link):
		html = get_page(url, self.log)
		for link in find_links(html):
			link = urlparse.urljoin(url, link)
		self.log("Checking: " + link)
		if link not in self.URLs and self.url_in_site(link):
			self.URLs.add(link)
			self._links_to_process.append(link)

if __name__ == '__main__':
	startURL = sys.argv
	spider = Spider(startURL)
	spider.run()
	for URL in sorted(spider.URLs):
		print URL











