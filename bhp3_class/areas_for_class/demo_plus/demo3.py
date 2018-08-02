from lxml import etree

def get_links(tree):
    links = dict()
    
    for elem in tree.findall('//a'):
        if elem.get('href'):
            links[elem.get("href")] = elem.text
    return links

if __name__ == '__main__':
    url = 'http://www.textfiles.com/hacking/INTERNET'
    parser = etree.HTMLParser()
    tree = etree.parse(url, parser=parser)
    headelem = tree.find('//h1')

    if headelem is not None:
        print('Analysis for: ')
        print(headelem.text.upper())
        input('\nPress return to continue.')
    
    for key, val in get_links(tree).items():
        print(f'{val:<20} {url}/{key}')