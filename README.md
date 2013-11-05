## magnetscrape.py

magnetscrape.py provides a way to easily scrape magnet information from a desired URL using Python, and then use this gather data to activate the 
local default magnet application.

## Python Dependencies:

* urllib2
* re
* os
* subprocess
* sys
* BeautifulSoup4 http://www.crummy.com/software/BeautifulSoup/#Download

## Functional Description

The 'scrape(url)' function within the project will take in as a parameter the requested internet URL,
and will attempt to scrape the URL for any and all magnet links that exist. It will collect each magnet link, break apart its contents by the parameters set forth by the Magnet URI Scheme, and store these contents as a dictionary structure. These dictionary structures are then collected together in a list, which is then returned to the user.

The 'activate(magnet_list)' function goes through the parametered list of magnets, and activates the links for the local machine's default application.

**Note:** The activate function expects the magnets contained to be of the same
design as the scrape function output. If you want to only do a subset of magnets
from the scrape output, make sure to adjust the list accordingly before bringing
it over to the activate function.

**Also Note:** I've included an extra function dn\_clean\_up(dn) which will clean up the readability of any inputted dn. You would use this if you wanted to get the magnet's original title.
## Dictionary Parameters 

See http://en.wikipedia.org/wiki/Magnet_URI_scheme#Parameters for an understanding of each magnet paramter's purpose; and here is a list of each included magnet parameter:

* as
* dn
* kt
* magnet
* mt
* tr
* xl
* xs
* xt

**Note:** The *magnet* parameter is the full magnet as a whole.

**Also Note:** Due to the structure of the Magnet URI Scheme, each dictionary subset has the potential to in turn have multiple subsections. For example, a magnet could have more then one tracker (tr). Therefore, each dictionary member is in turn is a list which either contains None (if this magnet provider does not support a certain parameter), list\[0\] (where this parameter has only a single data point i.e. dn), or more then one member ex. list\[0\], list\[1\], list\[2\] etc. (very likely for tr). 

## Example Usage:

```python
import mangetscrape

url = 'your url here'
magnet_list = magnetscrape.scrape(url)

magnetscrape.activate(magnet_list)

```
