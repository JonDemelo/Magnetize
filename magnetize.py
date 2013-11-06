import urllib2
import re
import subprocess
import os
import sys
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process

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


# Scrapes any magnet links from the selected URL and breaks each magnet as a
# dictionary of its parameters, all stored together in a list
def scrape(url):
    soup = BeautifulSoup(urllib2.urlopen(url))
    magnet_list = []

    for link in soup.find_all('a'):
        content = link.get('href')
        if content is not None and "magnet:?" in content:
            magnet_dict = {}
            for param in magnet_params:
                magnet_dict[param] = __regex(param, content)
            magnet_dict['magnet'] = content

            magnet_list.append(magnet_dict)
    return magnet_list


# Targets a specific magnet title, and scrapes the most similar candiate
# from the target url. Activates magnet
def target(url, title):
    link_list = []
    magnet_list = scrape(url)

    for magnet in magnet_list:
        link_list.append(magnet["magnet"])

    if link_list is not None:
        result = process.extractOne(title, link_list)

    magnet_dict = {}
    for param in magnet_params:
        magnet_dict[param] = __regex(param, result[0])
    magnet_dict['magnet'] = result[0]
    activate([magnet_dict])


# Takes the chosen list of dictionary-held magnets generated through the scrape
# function, and open each magnet connection to the machine's designated magnet
# application.
#
# Note: Cygwin-Windows not supported.
def activate(magnet_list):
    if magnet_list is not None:
        for magnet_dict in magnet_list:
            magnet_link = magnet_dict["magnet"]
            if magnet_link is not None:
                if sys.platform.startswith('darwin'):  # OSX
                    print magnet_link
                    subprocess.call(('open', magnet_link))
                elif os.name == 'nt':  # Windows
                    os.startfile(magnet_link)
                elif os.name == 'posix':  # UNIX-based
                    subprocess.call(('xdg-open', magnet_link))
