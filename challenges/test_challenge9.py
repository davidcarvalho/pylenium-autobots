import requests
import json


def test_challenge9():
    url = "https://www.copart.com/public/lots/search"

    headers = {
        'Cookie': 'visid_incap_242093=T6T1qhpIQXaFutz76m9ro9NFq14AAAAAQUIPAAAAAAARPIQkb6ro0/jgjw/zaWoT; g2usersessionid=6e26e86c9d293415fecd71ce3d64f555; G2JSESSIONID=5CF12588837413444F3F821F7EDAA79F-n1; incap_ses_1221_242093=AJZEO3JqL0D7zMfxjt3xEEKXrF4AAAAAgHcviJsteEK2bBiK79J1rA=='
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