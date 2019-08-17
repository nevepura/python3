'''
How to call an API.
'''

import urllib
from urllib.request import urlopen
from urllib.error import URLError
import json

API_URL = "http://openlibrary.org/search.json?author=haruki+murakami"

def get_author_and_title(data):
    '''
    Gather and print data from the 'data' dictionary. See the dictionary format here: https://openlibrary.org/dev/docs/api/search
    '''
    docs = data['docs']
    for doc in docs:
        print (f"{doc.get('author_name')}, {doc.get('title')} ")

def main():
    '''
    Try to access the url of the API and get some data
    '''
    try:
        request = urllib.request.urlopen(API_URL)
        data = json.load(request)
        get_author_and_title(data)
    except URLError as err:
        print(f'A URLError occurred while invoking the API: {API_URL}\nReason: {err.reason}.')
    except ValueError as err:
        print(f'ValueError occurred. Check if the API_URL: {API_URL} is well formatted.')

if __name__ == '__main__':
    main()

#print(data)
# print(type(response))
# print(response)
# print(response.read())

