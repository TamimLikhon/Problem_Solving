seats = [3, 1, 5]
students = [2, 7, 4]

sorted_seats = sorted(seats)
print(sorted_seats)
sorted_stu = sorted(students)
print(sorted_stu)

difference = []

for seat, student in zip(sorted_seats, sorted_stu):
    if seat > student:
        difference.append(seat - student)
    else:
        difference.append(student - seat)  # No negative differences, assuming 0 empty seats if students exceed seats

print(sum(difference))
