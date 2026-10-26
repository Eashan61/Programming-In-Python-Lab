resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(resources):
    print('All Resources:')

    if len(resources) == 0:
        print('Resources list are empty.')
        return

    for item in resources:
        res_id = item[0]
        name = item[1]
        category = item[2]
        quantity = item[3]
        
        if quantity < 0:
            print('Invalid Quantity!')
        else:
            print(f"ID: {res_id}, Name: {name}, Category: {category}, Quantity: {quantity} \n")

display_resources(resources)


#task 2 catagory

def search_by_category(resources, category):
    print("Searching Category:", category, ":")
    if len(resources) == 0:
        print("The resource list is empty.")
        return

    found = False
    for item in resources:
        if item[2].lower() == category.lower():
            print("ID:", item[0], "Name:", item[1], "Quantity:", item[3])
            found = True

    if not found:
        print("No resources found in category:", category)

search_by_category(resources, "Electronics")

#task 3 identifying zero quantity
def find_unavailable(resources):
    print("\n Unavailable Resources (Quantity = 0)")
    if len(resources) == 0:
        print("The resource list is empty.")
        return

    found = False
    for item in resources:
        if item[3] == 0:
            print("ID:", item[0], "Name:", item[1], "Category:", item[2])
            found = True

    if not found:
        print("All resources are currently available.")

def search_by_id(resources, target_id):
    print("\nSearching for Resource ID:", target_id, ":")
    if len(resources) == 0:
        print("The resource list is empty.")
        return

    for item in resources:
        if item[0] == target_id:
            print("Found -> Name:", item[1], " Category:", item[2], " Quantity:", item[3])
            return

    print("Resource ID", target_id, "not found!")

find_unavailable(resources)

#testing case
search_by_id(resources, 999)
resources_with_negative = [
    [106, "Speaker", "Audio", -3]
]
display_resources(resources_with_negative)
empty_list = []
display_resources(empty_list)