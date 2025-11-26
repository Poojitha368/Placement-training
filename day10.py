'''def can_reach_last_bunk(petrol_bunks):
    petrol = 0
    n = len(petrol_bunks)
    for i in range(n - 1): 
        petrol+=petrol_bunks[i]  # Gain petrol at current bunk
        petrol-=1  # Spend 1 unit to move to the next
        if petrol<0:
            return "Not Possible"
    return "Possible"
petrol_bunks = [2,3,1,0,1,3,0]
print(can_reach_last_bunk(petrol_bunks))'''

#i/p: [5,5,10,20,5,20,10], o/p: True/False
#item cost 5 rupees and if 10 or 20 given we have to give the 5 or 10 rupee change,
#if not possinble return False, else true
'''def coinChange(a):


    c5=0
    c10=0
    for i in a:
        if i==5:
            c5+=1
        elif i==10:
            if c5!=0:
                c5-=1
                c10+=1
            else:
                return False
        else:
            if c5!=0 and c10!=0:
                c5-=1
                c10-=1
            elif c5>=3:
                c5-=3
            else:
                return False
a=[5,5,10,20,5,20,10]
print(coinChange(a))'''

#i/p:[4,3,7,1,6,2], 
# wt:[0,4,7,14,15,21]
#find the min average waiting time
'''def min_average_time(a):
    wt_sum = 0
    total_sum=0
    for i in range(len(a)):
        if i==0:
            continue
        # print(wt_sum)
        wt_sum+=a[i-1]
        total_sum+=wt_sum
        print(total_sum)
    return total_sum//len(a)

a=[4,3,7,1,6,2]
a.sort() #as 
print(min_average_time(a))'''

#people = [1,6,2,3,4,5], bundle = [4,2,3,1,1,2]
#people[i]<= any bundle[i], increase count
#find the max count
'''def max_satisfactory(people,bundle):
    people.sort()
    bundle.sort()
    i,j=0,0
    while i<len(people) and j<len(bundle):
        if people[i]<=bundle[j]:
            i+=1
        j+=1
    return i
people=[1,6,2,3,4,5]
bundle=[4,2,3,1,1,2]
print(max_satisfactory(people,bundle))'''


'''def canJump(nums):
    n=0
    for i in range(len(nums)):
        if i>n:
            return False
        n=max(n,i+nums[i]) #further jump that can we can move from index i
    return True
nums=[3,2,1,0,4]
print(canJump(nums))'''
