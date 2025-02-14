def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        unprinted_designs.sort()
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been completed: ")
    for complete_models in completed_models:
        print(complete_models.title())

unprinted_designs = ['model plane', 'robot', 'phone case']
completed_models= []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
