def main():
    # Define a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # clear() - Removes all the elements from the dictionary
    my_dict.clear()
    print("After clear():", my_dict)

    # Define a new dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # copy() - Returns a copy of the dictionary
    copy_dict = my_dict.copy()
    print("Copy of dictionary:", copy_dict)

    # fromkeys() - Returns a dictionary with the specified keys and value
    keys = ['x', 'y', 'z']
    value = 0
    new_dict = dict.fromkeys(keys, value)
    print("Dictionary from keys:", new_dict)

    # get() - Returns the value of the specified key
    print("Value of 'a':", my_dict.get('a'))

    # items() - Returns a list containing a tuple for each key value pair
    print("Items:", my_dict.items())

    # keys() - Returns a list containing the dictionary's keys
    print("Keys:", my_dict.keys())

    # pop() - Removes the element with the specified key
    my_dict.pop('a')
    print("After pop('a'):", my_dict)

    # popitem() - Removes the last inserted key-value pair
    my_dict.popitem()
    print("After popitem():", my_dict)

    # setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    print("Using setdefault('d', 4):", my_dict.setdefault('d', 4))
    print("Updated dictionary:", my_dict)

    # update() - Updates the dictionary with the specified key-value pairs
    my_dict.update({'e': 5, 'f': 6})
    print("After update():", my_dict)

    # values() - Returns a list of all the values in the dictionary
    print("Values:", my_dict.values())


if __name__ == "__main__":
    main()
