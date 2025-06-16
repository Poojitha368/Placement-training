def min_no_exercises(energy,ec):
    ec.sort(reverse = True)
    curr_sum = 0
    cnt=0
    for i in ec:
        if i>energy:
            return 1
        if curr_sum+(2*i) <= energy:
            curr_sum += 2*i
            cnt += 2
        if curr_sum == energy:
            return cnt
    return -1

energy = int(input())
n = int(input())
ec=[]
for _ in range(n):
    ec.append(int(input()))
print("min no of exercises",min_no_exercises(energy,ec))

