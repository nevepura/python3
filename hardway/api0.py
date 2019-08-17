from urllib.request import urlopen
import sys

API_SEARCH = "http://openlibrary.org/search.json?author=tolkien"

response = urlopen(API_SEARCH)

print(type(response))

