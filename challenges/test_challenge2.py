from selenium.webdriver.common.keys import Keys


def test_challenge2(py, copart):
    py.get('#input-search').type('exotics', Keys.ENTER)
    print(py.title)
    assert py.contains('PORSCHE')