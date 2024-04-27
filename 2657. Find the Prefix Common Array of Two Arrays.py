A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
C = []

# Iterate through indices of A
for i in range(len(A)):
    # Extract slices of A and B up to index i
    slice_A = A[:i+1]
    slice_B = B[:i+1]
    # Find the intersection of the slices to get common elements
    common_elements = set(slice_A) & set(slice_B)
    # Append the count of common elements to C
    C.append(len(common_elements))

print(C)
