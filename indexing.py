
def add_to_index(index, keyword, url):
    """
    adds keyword to the index provided, if the keyword
    exists then append the url to it
    """
    for entries in index:
        if entries[0] == keyword:
            if url not in entries[1]:
                entries[1].append(url)
                return index
            return index

    index.append([keyword, [url]])
    return index


def add_page_to_index(index, url, content):
    """
    Adds the content of a web page to an index
    :param index: The main index where everything will be added
    :param url: The url from where the content is added
    :param content: The content being added
    :return:
    """
    word_list = content.split()
    for keyword in word_list:
        add_to_index(index, keyword, url)

    return index


def lookup(index, keyword):
    """
    lookup for an keyword in the given index and returns the urls
    where it was found. If not found, returns an empty list
    :param index: The index to search in
    :param keyword: The keyword to search
    :return: list
    """
    for entries in index:
        if entries[0] == keyword:
            return entries[1]

    return []


def main():
    """
    starting point of the script
    """
    index = []
    my_index = add_page_to_index(index, 'first.link', 'Adds the content of a web page to an index')
    my_index = add_page_to_index(my_index, 'second.link', 'adds keyword to the index provided, if the keyword exists then append the url to it')

    urls = lookup(my_index, 'the')
    print(urls)

main()
