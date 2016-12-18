'''
get the content of a web page
'''
from urllib.request import urlopen

def get_page(url):
    '''
    Open the given url and return the content of the page.
    '''
    try:
        data = urlopen(url)
        html = data.read()
        # decoding is necessary because data returned
        # by read() is is binary
        return html.decode('ISO-8859-1')
    except:
        return ''
