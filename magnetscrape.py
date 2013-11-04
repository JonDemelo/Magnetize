import urllib2
import re
from bs4 import BeautifulSoup

# Magnet URI Scheme Parameters as per
# http://en.wikipedia.org/wiki/Magnet_URI_scheme#Parameters
magnet_params = ('dn', 'tr', 'xl', 'xt', 'as', 'xs', 'kt', 'mt')

# Used to clean up the display names of magnets to their original state. 
def dn_clean_up(dn):
	dn = dn.replace("+", " ")
	dn = dn.replace("%5B", "[")
	dn = dn.replace("%5D", "]")
	dn = dn.replace("%28", "(")
	dn = dn.replace("%29", ")")
	return dn

# Used internally to grab each magnet parameter set from the full magnet
def __regex(magnet_param, content):
	pattern = r"(?<=" + magnet_param + "\=)(.*?)(?=&|$)"
	regex = re.compile(pattern)
	return regex.findall(content)

# Main utility of the module. Scrapes any magnet links from the selected URL
# and breaks each magnet as a dictionary of its parameters, all stored 
# together in a list
def scrape(url):
	soup = BeautifulSoup(urllib2.urlopen(url))
	magnet_list = []

	for link in soup.find_all('a'):
		if link.get('href') is not None and "magnet:?" in (link.get('href')):
			content = link.get('href')
			magnet_dict = {}
			for param in magnet_params:
				magnet_dict[param] = __regex(param, content)
			magnet_dict['magnet'] = content

			magnet_list.append(magnet_dict)
	return magnet_list