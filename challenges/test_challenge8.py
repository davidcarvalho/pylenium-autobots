import requests


def test_challenge8(py):
    url = "https://www.copart.com/public/lots/search"
    py.visit(url)
    cookies = ''
    for cookie in py.get_cookies():
        cookies += cookie["name"]+'='+cookie["value"]+';'
    py.quit()
    headers = {
        'Cookie': cookies
    }

    cars_i_like = ['toyota corolla', 'toyota elantra', 'toyota acura', 'dodge charger', 'PORSCHE PANAMERA',
                   'PORSCHE CAYENNE', 'HONDA PRIUS', 'HONDA ACCORD', 'Nissan maxima', 'nissan rogue']

    for car in cars_i_like:
        payload = {'query': car}
        response = requests.post(url, headers=headers, data=payload)

        print(f'\n{payload}')
        print(response.status_code)
        print(response.text)