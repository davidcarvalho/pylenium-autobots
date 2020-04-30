def test_challenge7(py, copart):
    list_cars = []
    for car in py.find('[ng-repeat*="popularSearch"]>a'):
        list_cars.append([car.text, car.get_attribute('href')])

    for i in range(len(list_cars)):
        py.visit(list_cars[i][1])
        assert py.get('h1[data-uname="searchResultsHeader"]').contains(list_cars[i][0].replace(' ', '-').lower())