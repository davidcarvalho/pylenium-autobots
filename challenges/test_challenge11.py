from bs4 import BeautifulSoup
import requests
import re


def test_challenge11():
    url = 'https://www.copart.com/'
    headers = {
        'Cookie': 'G2JSESSIONID=75739723A012C1AFDB92961C94276997-n2;'
                  'incap_ses_1221_242093=it5QPc9n3n/rPyHyjt3xEOvtrV4AAAAAr+ZIvSAtqf7T4XEXBTw/Ew==;'
                  'visid_incap_242093=1jCaSNqwRz6Bj+uncspiZOvtrV4AAAAAQUIPAAAAAADw2ryXoug0vVn6SY6hgdu3;'
                  'g2usersessionid=e969aeb8b3517b2967639ea6c5ab1a58'
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.content, 'html.parser')
    list_links = []
    for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
        list_links.append(link.get('href'))