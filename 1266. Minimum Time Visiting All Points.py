points = [[1, 1], [3, 4], [-1, 0]]

total_time = 0

for i in range(1, len(points)):
    time = max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
    total_time += time

print(total_time)
