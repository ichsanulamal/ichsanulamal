import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def translate_html(url, source_lang='en', target_lang='id'):
    """Translate the HTML content of a web page from the source language to the target language."""
    # Get the HTML content of the website page
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the text elements in the HTML content and translate them
    for text_elem in soup.find_all(text=True):
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text_elem) 
            text_elem.replace_with(translated)
        except:
            print(len(text_elem))
            

    # Return the translated HTML content as a string
    return str(soup)

if __name__ == '__main__':
    # Set the URL of the website page you want to translate
    url = "https://www.gutenberg.org/files/52190/52190-h/52190-h.htm"
    
    # Translate the HTML content of the web page
    translated_html = translate_html(url, source_lang='en', target_lang='id')

    # Export the translated HTML content to a file
    with open('translated.html', 'w', encoding='utf-8') as f:
        f.write(translated_html)
