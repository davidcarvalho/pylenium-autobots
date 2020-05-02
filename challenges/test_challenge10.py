import requests
import json
import csv
import pytest


def get_test_data():
    test_data = []
    with open('../data/tc10_test_data.csv') as csvfile:
        read_csv = csv.reader(csvfile)
        print(type(read_csv))
        # skip header
        next(read_csv, None)
        for row in read_csv:
            test_data.append((row[0], row[1], row[2]))
    return test_data


@pytest.mark.parametrize('make,model,year', get_test_data())
def test_challenge10(make, model, year):
    get_url = 'https://www.copart.com/public/lotSearchResultsPage'
    post_url = "https://www.copart.com/public/lots/search"

    headers = {
        'Cookie': 'G2JSESSIONID=75739723A012C1AFDB92961C94276997-n2;'
                  'visid_incap_242093=fO1CeoSIRBuo5II0F7ssrmG/rV4AAAAAQUIPAAAAAADAp/JqZFnKI2NY1chEmisI;'
                  'incap_ses_1221_242093=TnEaI06LEX5KWB/yjt3xEEndrV4AAAAA0QNYsE8WWBLjUKI/fpEEAg==;'
                  'g2usersessionid=e969aeb8b3517b2967639ea6c5ab1a58'
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
