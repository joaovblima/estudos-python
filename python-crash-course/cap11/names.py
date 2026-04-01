from name_function import get_formated_name

print("Enter 'q' anytime for quit")
while True:
    first = input("\nFirst name? ")
    if first == 'q':
        break
    last = input("\nLast name? ")
    if last == "q":
        break

    formatted_name = get_formated_name(first, last)
    print("\nNeatly formatted name: " + formatted_name)
