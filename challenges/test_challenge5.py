from selenium.webdriver.common.keys import Keys


def test_challenge5(py, copart):
    py.get('#input-search').type('PORSCHE')
    py.get('[ng-click="search()"]').click()
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    py.get('select[name="serverSideDataTable_length"]').select('100')
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    dict_count = {}
    for model in py.find('tbody span[data-uname="lotsearchLotmodel"]'):
        if model.text not in dict_count:
            dict_count[model.text] = 1
        else:
            dict_count[model.text] = dict_count.get(model.text) + 1
    print('\n')
    for item in dict_count:
        print(f'x{dict_count.get(item)} {item}')


def test_challenge5_2(py, copart):
    py.get('#input-search').type('PORSCHE')
    py.get('[ng-click="search()"]').click()
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    py.get('select[name="serverSideDataTable_length"]').select('100')
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    dict_count = {}
    # damages
    for damage in py.find('tbody span[data-uname="lotsearchLotdamagedescription"]'):
        if damage.text in ['REAR END', 'FRONT END', 'MINOR DENT/SCRATCHES', 'UNDERCARRIAGE']:
            if damage.text not in dict_count:
                dict_count[damage.text] = 1
            else:
                dict_count[damage.text] = dict_count.get(damage.text) + 1
        else:
            if 'MISC' not in dict_count:
                dict_count['MISC'] = 1
            else:
                dict_count['MISC'] = dict_count.get('MISC') + 1
    print('\n')
    print(dict_count)
