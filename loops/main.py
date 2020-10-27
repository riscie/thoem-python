from car import car

if __name__ == '__main__':
    # create some car objects
    c1 = car("Audi")
    c2 = car("VW")
    c3 = car("Porsche")

    # create a list of all car objects
    cars = [c1, c2, c3]

    # loop over each car and print its brand
    print('Printing all cars:')
    for car in cars:
        print(f'- This is a {car.brand}')

    print('\nPrinting the first two cars:')
    # 'slice' the list: Returns a new list from beginning until index 2 [c1, c2, c3]  => [c1, c2]
    first_two_cars = cars[:2]
    for car in first_two_cars:
        print(f'- This is a {car.brand}')
