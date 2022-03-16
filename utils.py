from bs4 import BeautifulSoup
import requests

def processQuery(service, apikey, engineID, relation, threshold, query, numtuples):
    res = service.cse().list(q = query, cx = engineID,).execute()
    list_of_urls = []

    for result in res.get('items'):
        currentUrl = result.get('formattedUrl')
        list_of_urls.append(currentUrl)

    for url in list_of_urls:
        req = requests.get(url)
        soup = BeautifulSoup(req.text)
        print(soup.text)
    

    
