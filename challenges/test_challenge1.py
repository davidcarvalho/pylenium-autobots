def test_challenge1(py):
    py.visit('https://google.com')
    py.get('input[name=q]').type('puppies').submit()
    print(py.title)
    assert 'puppies' in py.title
