def main():
    # Define two sets
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # add() - Adds an element to the set
    set1.add(5)
    print("After add(5) to set1:", set1)

    # clear() - Removes all the elements from the set
    set1.clear()
    print("After clear() set1:", set1)

    # copy() - Returns a copy of the set
    set1 = {1, 2, 3, 4}
    copy_set = set1.copy()
    print("Copy of set1:", copy_set)

    # difference() - Returns a set containing the difference between two or more sets
    print("Difference between set1 and set2:", set1.difference(set2))

    # difference_update() - Removes the items in this set that are also included in another, specified set
    set1.difference_update(set2)
    print("After difference_update() set1:", set1)

    # discard() - Remove the specified item
    set2.discard(4)
    print("After discard(4) from set2:", set2)

    # intersection() - Returns a set, that is the intersection of two other sets
    print("Intersection of set1 and set2:", set1.intersection(set2))

    # intersection_update() - Removes the items in this set that are not present in other, specified set(s)
    set1.intersection_update(set2)
    print("After intersection_update() set1:", set1)

    # isdisjoint() - Returns whether two sets have an intersection or not
    print("Is set1 disjoint with set2:", set1.isdisjoint(set2))

    # issubset() - Returns whether another set contains this set or not
    print("Is set1 a subset of set2:", set1.issubset(set2))

    # issuperset() - Returns whether this set contains another set or not
    print("Is set1 a superset of set2:", set1.issuperset(set2))

    try:
        # pop() - Removes an element from the set
        popped_element = copy_set.pop()
        print("Popped element from set1:", popped_element)
    except KeyError:
        print("Cannot pop from an empty set")

    # remove() - Removes the specified element
    set2.remove(3)
    print("After removing 3 from set2:", set2)

    # symmetric_difference() - Returns a set with the symmetric differences of two sets
    print("Symmetric difference between set1 and set2:", set1.symmetric_difference(set2))

    # symmetric_difference_update() - Inserts the symmetric differences from this set and another
    set1.symmetric_difference_update(set2)
    print("After symmetric_difference_update() set1:", set1)

    # union() - Return a set containing the union of sets
    print("Union of set1 and set2:", set1.union(set2))

    # update() - Update the set with the union of this set and others
    set1.update(set2)
    print("After update() set1:", set1)


if __name__ == "__main__":
    main()
