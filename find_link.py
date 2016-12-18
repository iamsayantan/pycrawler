'''
extract links form page
'''

from my_url import get_page

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

def union(list_1, list_2):
    '''
    returns the union of two lists
    '''
    for element in list_2:
        if element not in list_1:
            list_1.append(element)
    return list_1

def crawl_web(seed):
    '''
    Starts crawling from the seed url given and continues crawling
    to all the url found there.
    '''
    to_crawl = [seed]
    crawled = []

    # until there is links availabe in to_crawl list, continue the processs
    while to_crawl:
        # take the last element of the list to crawl, this would remove the
        # url from the list also
        web_url = to_crawl.pop()
        # nedd to make sure the url is not already scanned
        # by checking if it exists in crawled list
        if web_url not in crawled:
            print('Crawling ' + web_url + '...')
            union(to_crawl, get_all_links(web_url))
            crawled.append(web_url)

    return crawled

def main():
    '''
    main entry point to the script
    '''
    seed = input('Enter a url to start crawling..\n')
    print(crawl_web(seed))

main()
