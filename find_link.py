'''
extract links form page
'''

from my_url import get_page
from datetime import datetime

def find_links(page):
    '''
    Finds urls on a string. It searches for an anchor tag and extracts the url
    form that.
    '''
    # Look for an anchor tag that contains the link
    start_link = page.find('<a href=')

    # If no anchor tag is found then no need to look further
    if start_link == -1:
        return None, 0

    # The actual url is in a double quotation after the href attribute
    # so just find the starting and endig double quote and the string in
    # between those would be the url
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)

    link = page[start_quote + 1: end_quote]

    return link, end_quote


def get_all_links(url):
    '''
    store all the links provided by find_links() method as a list.
    '''
    page = get_page(url)
    url_list = []
    # Loop through until there are links in the string
    while True:
        url, endpos = find_links(page)
        if url is None:
            break

        page = page[endpos:]
        url_list.append(url)

    return url_list

def main():
    '''
    main entry point to the script
    '''
    web_url = input('Enter an url to scan..\n')

    #measure the execution time
    start = datetime.now()

    urls = get_all_links(web_url)
    for url in urls:
        print(url)

    end = datetime.now()
    execution_time = end - start
    print(execution_time)

main()
