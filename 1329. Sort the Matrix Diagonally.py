from collections import defaultdict


def digaonalSort(self, mat):

    n = len(mat)
    m = len(mat[0])

    map = defaultdict(list)
    for i in range(n):
        for j in range(m):
            digonal_index = i - j
            element =  mat[i][j]
            map[diagonal_index].append(element)

    
    for key in map:
        map[key].sort(reverse=True)
    
        for j in range(m):
            digonal_index = i - j
            element = map[digonal_index].pop()
            mat[i][j] = element
    
    return mat
    