from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def parse_url(before_url):
	bad_tags = ["fees"]
	
	privacy_tags = ["privacy"]	
	
	url = before_url
	hdr = {'User-Agent': 'Mozilla/5.0'}
	
	req = Request(url,headers=hdr)
	page = urlopen(req)

	soup = BeautifulSoup(page, features="html.parser")
	
	bad_urls = []
	
	for line in soup.get_text().split("."):
		for tag in bad_tags:
			if tag.strip() in line.strip() and "[" not in line and "{" not in line and "/" not in line and line.strip() not in bad_urls:
				bad_urls.append(line.strip())
	
	context_list = []
	
	for url in bad_urls:
		context_list.append({
			"title": "Fee Notice",
			"category": "fee",
			"snippet": url
		})
	
	return context_list

def sample_info():
	context = {
		"data": [{
				"title": "This service may collect, use, and share location data Discussion Generated through the annotate view",
				"category": "privacy",
				"snippet": "...Your location information We collect information about your location when you use our services, which helps us offer..."
			},
			{
				"title": "There is a big fee",
				"category": "fee",
				"snippet": "...If you use our service, you must pay a $1000 fee..."
			}
			]
	}
	return context