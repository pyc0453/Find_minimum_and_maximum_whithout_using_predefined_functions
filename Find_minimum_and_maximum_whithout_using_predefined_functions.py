l=[4,2,5,3,8,7,6,9,1]

maximum = l[0]
minimum = l[0]
for i in l :
    if i>maximum:
        maximum = i
    if i<minimum:
        minimum = i
print(maximum)
print(minimum)
