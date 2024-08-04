Nlist = [1, 2, 3, 4, 5]
# Nlist = [-1, 3, -2, -4, 1, -5, 3]
totalsum = 0
previous = sum(Nlist)

for i in range(len(Nlist)):
    for j in range(i ,len(Nlist)):
        totalsum = sum(Nlist) + sum(Nlist[i:j+1]) * -2
        print(f"totalsum : {totalsum}, previous : {previous}")
        if totalsum > previous:
            previous = totalsum 

print(previous)
