nums = [1, 13, 10, 12, 31]

reverse = [int(str(num)[::-1]) for num in nums]

final_array = nums + reverse

distinct_integers = set(final_array)

print(len(distinct_integers))



can = int(input())

print(sum(can))