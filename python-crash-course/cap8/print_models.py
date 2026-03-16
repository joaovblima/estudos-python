
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current = unprinted_models.pop()
        print("Printing model:", current)
        completed_models.append(current)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for complete_model in completed_models:
        print(complete_model)


unprinted_models = ["iphone case", "robot pendantla", "dodecahedron"]
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
