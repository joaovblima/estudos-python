def city_country(city, country, population=""):
    if population:
        city_and_country = city + ", " + country + ", População: " + population
    else:
        city_and_country = city + ", " + country

    return city_and_country.title()
