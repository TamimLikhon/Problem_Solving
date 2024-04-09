def groupThePeople(groupSizes):
    groups = {}  # Create an empty dictionary to store groups
    result = []  # Create an empty list to store the final result

    for i, size in enumerate(groupSizes):  # Iterate over each person's group size
        if size in groups:  # If a group of this size already exists
            groups[size].append(i)  # Add the index of the person to the corresponding group
        else:  # If this is the first person of this group size
            groups[size] = [i]  # Create a new group with this person as the first member

        if len(groups[size]) == size:  # If the group is now complete
            result.append(groups[size])  # Add the group to the final result
            groups[size] = []  # Reset the group for the next iteration

    return result  # Return the final result containing groups of people

# Example usage:
groupSizes1 = [3, 3, 3, 3, 3, 1, 3]
print(groupThePeople(groupSizes1))  # Output: [[5], [0, 1, 2], [3, 4, 6]] - Explanation provided in the problem statement


