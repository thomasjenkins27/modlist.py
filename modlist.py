#Goal is to create 2 lists called unprinted_list and printed_list.  
#Create 2 funtions. Modify/copy 1 list into the next.
def incomplete_tasks(unprinted_list, printed_list):
#Sort list to show in alphabetical order.
    unprinted_list.sort(reverse=True)
    while unprinted_list:
        current_task = unprinted_list.pop()
        print(f"Currently printing: {current_task.title()}")
        printed_list.append(current_task)

def show_completed_task(printed_list):
    print("\nThe following items have been printed: ")
    for completed_list in printed_list:
        print(completed_list.title())

unprinted_list = ['airplane', 'quadcopter', 'dog']
printed_list = []

#Make a copy of the list to keep the original list
incomplete_tasks(unprinted_list[:], printed_list)
show_completed_task(printed_list)

#Proof that the original list is left unchanged.
print("\nThis is the original list: ")
print(unprinted_list)
