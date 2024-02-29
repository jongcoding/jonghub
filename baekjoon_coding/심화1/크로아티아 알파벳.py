a=input()
croatian_alp=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alp in croatian_alp:

    a=a.replace(alp,'*')
print(len(a))

