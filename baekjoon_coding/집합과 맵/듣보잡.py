n,m= map(int, input().split())
person_list=set(input() for _ in range(n))
search_list=set(input() for _ in range(m))
result_list=[]
for person in search_list:
    if person in person_list:
        result_list.append(person)
result_list.sort()
print(len(result_list))
print("\n".join(map(str, result_list)))