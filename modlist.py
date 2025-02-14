unprinted_designs = ['model plane', 'robot', 'phone case']
completed_models= []

while unprinted_designs:
    unprinted_designs.sort()
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("The following models have been completed: ")
for complete_models in completed_models:
    print(complete_models.title())
