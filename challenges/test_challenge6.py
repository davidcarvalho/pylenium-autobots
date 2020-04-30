from selenium.common.exceptions import TimeoutException


def test_challenge6(py, copart):
    py.get('#input-search').type('NISSAN')
    py.get('[ng-click="search()"]').click()
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    py.get('input[type="search"]').type('SKYLINE555')
    py.get('#serverSideDataTable_processing').\
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    try:
        py.get('tbody span[data-uname="lotsearchLotmodel"]')
    except TimeoutException:
        py.screenshot('../screenshots/tc6_model_not_found.png')
