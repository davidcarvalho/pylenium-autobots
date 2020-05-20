import requests
import json


def test_challenge9(py):
    url = "https://www.copart.com/public/lots/search"

    py.visit(url)
    cookies = ''
    for cookie in py.get_cookies():
        cookies += cookie["name"] + '=' + cookie["value"] + ';'
    py.quit()
    headers = {
        'Cookie': cookies
    }
    # cars_i_like = ['toyota corolla', 'toyota elantra', 'toyota acura', 'dodge charger', 'PORSCHE PANAMERA',
    #                'PORSCHE CAYENNE', 'HONDA PRIUS', 'HONDA ACCORD', 'Nissan maxima', 'nissan rogue']
    cars_i_like = ['toyota camry']

    for car in cars_i_like:
        payload = {'query': car}
        response = requests.request("POST", url, headers=headers, data=payload)

        print(f'\n{payload}')
        assert response.status_code == 200
        json_response = json.loads(response.text)
        assert type(json_response['data']['results']['content'][0]["lotNumberStr"]) == str
        assert type(json_response['data']['results']['content'][0]["ln"]) == int
        assert type(json_response['data']['results']['content'][0]["sbf"]) == bool