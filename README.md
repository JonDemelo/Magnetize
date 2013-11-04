## magnetscrape.py

MagnetScrap.py provides a way to easily scrape magnet information from a desired URL using Python.

## Python Dependencies:

urllib2
re
BeautifulSoup4 http://www.crummy.com/software/BeautifulSoup/#Download

## Functional Description

The 'scrape(url)' function within the project will take in as a parameter the requested internet URL,
and will attempt to scrape the URL for any and all magnet links that exist. It will collect each magnet link, break apart its contents by the parameters set forth by the Magnet URI Scheme, and store these contents as a dictionary structure. These dictionary structures are then collected together in a list, which is then returned to the user.

## Dictionary Parameters 

See http://en.wikipedia.org/wiki/Magnet_URI_scheme#Parameters for an understanding of each magnet paramter's purpose; and here is a list of each included magnet parameter:

* as
* dn
* kt
* magnet - Note: The magnet parameter is the full magnet as a whole.
* mt
* tr
* xl
* xs
* xt


## Example Usage:

```python
import mangetscrape.py

url = 'your url here'
list_of_magnet_dictionaries = scrape(url)
```
