from requests_html import HTMLSession
from definitions.uavars import getRandomUserAgent
from definitions.settingsvars import JAGEX_URL
from bs4 import BeautifulSoup

def canCreateAccounts(proxy):
    session = HTMLSession()
    headers = {'User-Agent':getRandomUserAgent()}
    proxy = {'http' : 'http://'+str(proxy), 'https' : 'http://'+str(proxy)}
    r = session.get(JAGEX_URL, headers=headers, proxies=proxy)
    soup = BeautifulSoup(r.content, "html.parser")

    searchedVal = soup.find('form', id='create-email-form')


    if(searchedVal != None):
        return True, "Successfully loaded account creation page."

    searchedVal = None
    searchedVal = soup.find('ul', class_='cferror_details')

    if(searchedVal != None):
        return False, "IP is blocked by Jagex/Cloudflare."
        
    searchedVal = None
    searchedVal = soup.find('h1', id='cloudflare_title')

    if(searchedVal != None and searchedVal.text == 'Too many requests'):
        return True, "Too many accounts created on the ip in a short period. Wait to create more."

    return False, "No scenario was hit... manually check this proxy."
