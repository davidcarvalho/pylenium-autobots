from bs4 import BeautifulSoup
import requests
import re


def test_challenge11(py):
    url = 'https://www.copart.com/'
    py.visit("https://www.copart.com/public/lots/search")
    cookies = ''
    for cookie in py.get_cookies():
        cookies += cookie["name"] + '=' + cookie["value"] + ';'
    headers = {
        'Cookie': cookies
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.content, 'html.parser')
    list_links = []
    for tag in soup.find_all('a', attrs={'href': re.compile("^http")}):
        list_links.append(tag.get('href'))

    for link in list_links:
        py.visit(link)