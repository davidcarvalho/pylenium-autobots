
def test_challenge2(py, copart):
    py.get('#input-search').type('exotics')
    py.get('[ng-click="search()"]').click()
    py.get('#serverSideDataTable_processing'). \
        should().have_attr('style', 'display: block;').should().have_attr('style', 'display: none;')
    print(py.title)
    assert py.contains('PORSCHE')