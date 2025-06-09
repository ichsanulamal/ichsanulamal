import requests
from bs4 import BeautifulSoup

# Set up the DeepL API endpoint and authentication key
api_endpoint = 'https://api-free.deepl.com/v2/translate'
auth_key = 'your-authentication-key-here'

# Load the HTML file
with open('example.html', 'r') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the text content from the HTML
text = soup.get_text()

# Translate the text to Indonesian using the DeepL API
params = {
    'auth_key': auth_key,
    'text': text,
    'target_lang': 'ID'
}
response = requests.post(api_endpoint, data=params)
translated_text = response.json()['translations'][0]['text']

# Replace the English text with the translated text in the HTML
soup.body.string = translated_text

# Save the translated HTML to a new file
with open('example_id.html', 'w') as f:
    f.write(str(soup))


import os

# Create the docs directory if it doesn't exist
if not os.path.exists('docs'):
    os.mkdir('docs')

# Load the translated HTML file
with open('example_id.html', 'r') as f:
    html = f.read()

# Create the Markdown content for the new page
markdown = f'''
# Example Translated Page

Translated content:

{html}
'''

# Write the Markdown content to a new file
with open('docs/example_id.md', 'w') as f:
    f.write(markdown)
