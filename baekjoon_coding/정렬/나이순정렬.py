n=int(input())
person_list=[]
for i in range(n):
    a,b= input().split()
    person_list.append([int(a),b,i])
sorted_person=sorted(person_list, key=lambda x: (x[0],x[2]))
for i in range(n):
    print(sorted_person[i][0],sorted_person[i][1])