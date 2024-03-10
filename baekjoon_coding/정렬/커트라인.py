n,k = map(int, input().split())
test_list=list(map(int, input().split()))
test_list.sort()
print(test_list[-k])