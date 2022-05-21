if __name__ == '__main__':
    # latitude and longitude of the Los Angeles International Airport
    airport_coordinates = (33.9425, -118.408056)

    # data about Tokyo: name, year, population (millions), population change (%), area (km²)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

    # a list of tuples of the form (country_code, passport_number)
    travelers_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

    # print each traveler id
    # the % formatting operator understands tuples and treats each item as a separate field
    print('Passports:')
    for traveler_id in sorted(travelers_ids):
        print('%s/%s' % traveler_id)

    # the for loop knows how to retrieve the items of a tuple separately — this is called “unpacking”
    # here we are not interested in the second item, so it’s assigned to a dummy variable "_"
    print('Countries:')
    for country, _ in travelers_ids:
        print(country)
