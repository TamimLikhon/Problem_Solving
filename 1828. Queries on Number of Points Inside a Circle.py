points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

counts = []

for query in queries:
    count = 0
    for point in points:
        if (point[0] - query[0]) ** 2 + (point[1] - query[1]) ** 2 <= query[2] ** 2:
            count += 1
    counts.append(count)

print(counts)
