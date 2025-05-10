import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Set the URL of the website page you want to translate
url = "https://www.gutenberg.org/files/58025/58025-h/58025-h.htm"

# Get the HTML content of the website page
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element with a summary attribute
table = soup.find('table', {'summary': ''})

# Find all the links within the table element
links = []
for link in table.find_all('a'):
    href = link.get('href')
    if href is not None and href[0] != '#':
        links.append(href)

# Print the links
for a in links:
    print(a)