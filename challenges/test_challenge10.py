import requests
import json
import csv
import pytest


def get_test_data():
    test_data = []
    with open('C:/Users/David.Carvalho/Desktop/dev/python-autobots/data/tc10_test_data.csv') as csvfile:
        read_csv = csv.reader(csvfile)
        print(type(read_csv))
        # skip header
        next(read_csv, None)
        for row in read_csv:
            test_data.append((row[0], row[1], row[2]))
    return test_data


@pytest.mark.parametrize('make,model,year', get_test_data())
def test_challenge10(py, make, model, year):
    post_url = "https://www.copart.com/public/lots/search"
    py.visit(post_url)
    cookies = ''
    for cookie in py.get_cookies():
        cookies += cookie["name"] + '=' + cookie["value"] + ';'
    py.quit()
    headers = {
        'Cookie': cookies
    }

    payload = {'query': f'{make} {model} {year}'}
    response = requests.request("POST", post_url, headers=headers, data=payload)

    print(f'\n{payload}')
    assert response.status_code == 200
    json_response = json.loads(response.text)
    print(response.text)
    assert type(json_response['data']['results']['content'][0]["lotNumberStr"]) == str
    assert type(json_response['data']['results']['content'][0]["ln"]) == int
    assert type(json_response['data']['results']['content'][0]["sbf"]) == bool
