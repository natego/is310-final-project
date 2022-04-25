import bs4
from bs4 import BeautifulSoup
import requests

urls = open('C:,/Users/nate/is310-final-project/IS310assignments/updated_raw_text_script_urls.txt, 'r', encoding='ISO-8859-1')

links = []
dictionary_text = {}
dictionary_text['Text'] = []

for text in urls:
    fixed = text.split(' +++$+++ ')
    link.append((fixed[2].strip()))
    print(link)
    
def Url(text):
    response = requests.get(text)
    soup = BeautifulSoup(response.text, features='html.parser')
    lines = soup.find_all('pre')

    for line in lines:
        line = lines.get_text()
        dictionary_text[line[0]] = lines

    if response.status_code == requests.codes.ok: 
      return response.text

for add in text[0:25]:
    Url(add)

print(dictionary_text)

new_file = open('new_raw_scripts_urls.txt', 'w+')
new_file.writelines(str(dictionary_text))
new_file.close()

