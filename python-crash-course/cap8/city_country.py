def city_country(city, country):
    city_formatted_name = country.title() + ", " + city.title()
    return city_formatted_name


city_full_name = city_country(city="Uniao dos palmares", country="Brasil")
print(city_full_name)
