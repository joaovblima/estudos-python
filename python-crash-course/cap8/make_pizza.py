def make_pizza(size, *toppings):

    print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)


make_pizza(12, "peperoni")
make_pizza(17, "chicken", "cheddar cheese", "chocolate")
