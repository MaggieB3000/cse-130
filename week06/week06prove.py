# 1. Name:
#      Margaret Binns

# 2. Assignment Name:
#      Lab 06: Advanced Search

# 3. Assignment Description:
#      This program takes a json file and converts it into a list before asking the user for input and doing a binary search for that item in the list.

# 4. Algorithmic Efficiency
#      This program is a O(log n) because the graph for the data matches the diagnoal line that curves into a horizontal line.

#       The list of data from the counter is:
#       1 - 0
#       11 - 3
#       196 - 7
#       

# 5. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out the binary search part because I didn't realize that python can compare two strings; I thought you could only compare ints and floats. Once I figured that out though it was fine. The other hard part was getting this file to find the json files.Lab

# 6. How long did it take for you to complete the assignment?
#      3.5 hours

import json

def read_json_file(filename):
    '''
    Reads and parses a json file into a list.

    Parameters:
        filename (string): the name of the file to be read.

    Returns:
        list: contents of the json file.
    '''
    

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("array")
        
    except FileNotFoundError:
        print(f"Error: Unable to open {filename}")
        return None
    
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON data")
        return None
    
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return None
    

def binary_search(data, target):
    '''
    Performs an iterative search using only the less than operator.
    
    Parameters:
        data (list): the list from the json.
        target (string): word that user is searching for

    Returns:
        bool: whether the target matches with an item in the list or not.
        
    '''

    counter = 0

    if len(data) == 0:
        return False, counter

    left = 0
    right = len(data) - 1

    while left < right:

        counter = counter + 1

        mid = (left + right) // 2

        if target < data[mid]:
            right = mid - 1

        elif data[mid] < target:
            left = mid + 1

        else:
            return True, counter
        
        
    return data[left] == target, counter


def main():

    filename = input("Enter the name of the file: ")

    data = read_json_file(filename)
    if data is None:
        return
    
    number_of_inputs = len(data)

    search_name = input("Enter the name to search for: ")

    found, counter = binary_search(data, search_name)

    if found == True:
        print(f'Your item ({search_name}) was found in {filename}.')

    else:
        print(f'Your item ({search_name}) was not found in {filename}.')

    #print(f"{number_of_inputs} - {counter}")


if __name__ == "__main__":
    main()