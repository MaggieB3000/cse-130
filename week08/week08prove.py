# 1. Name:
#      Margaret Binns
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program reads a json file into a list, sorts it, and then prints it out to the user.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was both figuring where to put asserts and what to check for, as well as wrapping my brain around the sorting code.
# 5. How long did it take for you to complete the assignment?
#      2 hours

import json

def read_file(filename):
    assert filename, "Filename cannot be empty"

    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        for item in data['array']:
            assert isinstance(item, str), f"All items must be strings, found {type(item)}"

        return data['array']

    except json.JSONDecodeError:
        assert False, f"Invalid JSON format in file '{filename}'"
        return []
    
def sort_list(items):
    assert isinstance(items, list), "Input must be a list"

    for i in range(1, len(items)):
        current_value = items[i]
        position = i
            
        while position > 0 and items[position - 1] > current_value:
            items[position] = items[position - 1]
            position -= 1
                
        items[position] = current_value

    assert len(items) == len(items), "Sorted list must have the same length as the original list"

    return items

def main():
    filename = input ("Type the file name: ")

    try:
        items = read_file(filename)
        sorted_items = sort_list(items)
        
        print(f"The values in {filename} are:")
        for item in sorted_items:
            print(f"\t{item}")
            
    except AssertionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

