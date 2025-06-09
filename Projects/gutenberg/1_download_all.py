import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# download html and return parsed doc or None on error
def download_url(urlpath):
    try:
        # open a connection to the server
        with urlopen(urlpath, timeout=3) as connection:
            # read the contents of the html doc
            return connection.read()
    except:
        # bad url, socket timeout, http forbidden, etc.
        return None

# decode downloaded html and extract all <a href=""> links
def get_urls_from_html(content):
    # decode the provided content as ascii text
    html = content.decode('utf-8')
    # parse the document as best we can
    soup = BeautifulSoup(html, 'html.parser')
    # find all all of the <a href=""> tags in the document
    atags = soup.find_all('a')
    # get all links from a tags

    res = []
    for tag in atags:
        if tag.get('href') is not None and "#" not in tag.get('href'):
            regexp = re.compile(r'htm')
            if regexp.search(tag.get('href')):
                res.append(tag.get('href'))
    return res

def get_ebook_id(url="https://www.gutenberg.org/files/58025"):
    return url.split("/")[4]

# download one book from project gutenberg
def download_books(ebook_ids, format='.epub'):
    # construct the download url
    urls = []
    for e_id in ebook_ids:
        urls.append(f'https://www.gutenberg.org/cache/epub/{e_id}/pg{e_id}{format}')
    
    for url, filename in zip(urls, ebook_ids):
        r = requests.get(url, stream=True)
        with open("books/"+filename+format, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=256):
                fd.write(chunk)
    print(f"file {filename} downloaded succesfully")
    
# download all books from project gutenberg
def download_all_books(url, save_path, format='.epub'):
    # download the page that lists top books
    data = download_url(url)
    print(f'.downloaded {url}')
    # extract all links from the page
    urls = get_urls_from_html(data)
    ebook_ids = [ get_ebook_id(url) for url in urls ]
    download_books(ebook_ids, format)

# entry point
URL = 'https://www.gutenberg.org/files/58025/58025-h/58025-h.htm#N51548'
DIR = 'books'

if __name__ == "__main__":
    # download top books
    download_all_books(URL, DIR)