from bs4 import BeautifulSoup
import requests
# URL = 'https://en.wikipedia.org/wiki/Cheetah'
# https://en.wikipedia.org/wiki/Fod
wiki_url =  input('Enter your URL: ')
print('Fetching main wiki article: %s' % wiki_url)
print('----------------------------')
response= requests.get(wiki_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")
    table = soup.find_all('p')[1]
    links = table.findAll('a')
    print('Done extracting links. About to fetch: %s links..' % len(links))

    for link in links:
        print(link.get_text())
        if link.get('href') != None:
            if 'https://' in link.get('href'):
                print(link.get('href'))
            else:
                # Convert relative URL to absolute URL
                print('https://en.wikipedia.org' + link.get('href'))

        print('----------------------------')  # Just a line break
else:
    print("Wikipedia does not have an article with this exact name.")