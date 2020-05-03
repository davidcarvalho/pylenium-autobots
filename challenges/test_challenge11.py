from bs4 import BeautifulSoup
import requests
import re


def test_challenge11(py):
    url = 'https://www.copart.com/'
    headers = {
        'Cookie': 'G2JSESSIONID=0181F6E52894C6D4719D580CC5EDB878-n2;'
                  'incap_ses_1221_242093=cXQzMKUUDnpwmFDyjt3xEPLhrl4AAAAA99VZpDO5D8jOYs/InHdhUA==;'
                  'visid_incap_242093=1jCaSNqwRz6Bj+uncspiZOvtrV4AAAAAQUIPAAAAAADw2ryXoug0vVn6SY6hgdu3;'
                  'g2usersessionid=6cfeeb1fc99e48746940221b14e3a43e'
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.content, 'html.parser')
    list_links = []
    for tag in soup.find_all('a', attrs={'href': re.compile("^http")}):
        list_links.append(tag.get('href'))

    for link in list_links:
        py.visit(link)