# N = 7
Nlist = [-1, 3, -2, -4, 1, -5, 3]

sum_Nlist = sum(Nlist)
previous = sum_Nlist

for i in range(len(Nlist)):
    for j in range(i ,len(Nlist)):
        sumV = 0
        print(f"sublist : {Nlist[i:j+1]}")         

        for v in Nlist[i:j+1]:
            v *= -1
            sumV += v
        
        sumV = sumV * 2
        total_sum = sum_Nlist + sumV

        print(f"previous : {previous} , total_sum : {total_sum}")
        if previous < total_sum:
            previous = total_sum
            
print(previous)
