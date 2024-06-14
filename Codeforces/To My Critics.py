num_tests = int(input())

for _ in range(num_tests):
    a, b, c = map(int, input().split())

    if (a + b >= 10) or (a + c >= 10) or (b + c >= 10):
        print("YES")
    else:
        print("NO")
