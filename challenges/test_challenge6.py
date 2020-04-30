from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


def test_challenge6(py, copart):
    py.get('#input-search').type('NISSAN')
    py.get('[ng-click="search()"]').click()
    py.wait(use_py=True).sleep(3)
    py.get('input[type="search"]').type('SKYLINE555')
    py.wait(use_py=True).sleep(3)
    try:
        py.get('tbody span[data-uname="lotsearchLotmodel"]')
    except TimeoutException:
        py.screenshot('../screenshots/tc6_model_not_found.png')
