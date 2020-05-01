import requests


def test_challenge8():
    url = "https://www.copart.com/public/lots/search"
    headers = {
        'Cookie': 'visid_incap_242093=T6T1qhpIQXaFutz76m9ro9NFq14AAAAAQUIPAAAAAAARPIQkb6ro0/jgjw/zaWoT;'
                  ' g2usersessionid=6e26e86c9d293415fecd71ce3d64f555; '
                  'incap_ses_1221_242093=jXHwGZERzyqpTsTxjt3xEMR2rF4AAAAA9rKVTWrHXKQXnphD4VYiwg==; '
                  'G2JSESSIONID=3A3A9C7565B9C9FEE03F1F3FB73F5AFE-n1'
    }
    cars_i_like = ['toyota corolla', 'toyota elantra', 'toyota acura', 'dodge charger', 'PORSCHE PANAMERA',
                   'PORSCHE CAYENNE', 'HONDA PRIUS', 'HONDA ACCORD', 'Nissan maxima', 'nissan rogue']

    for car in cars_i_like:
        payload = {'query': car}
        response = requests.request("POST", url, headers=headers, data=payload)

        print(f'\n{payload}')
        print(response.status_code)
        print(response.text)