'''
get the content of a web page
'''
from urllib.request import urlopen

def get_page(url):
    '''
    Open the given url and return the content of the page.
    '''
    data = urlopen(url)
    html = data.read()

    # utf-8 decoding is necessary because data returned
    # by read() is is binary
    return html.decode('utf-8')
    