def test_challenge3(py, copart):
    for car in py.find("[ng-repeat*='popularSearch'] > a"):
        print(f'{car.text} - {car.get_attribute("href")}')
