def hero_win_possible(ve,H,v,h):
    i=0
    curr_health = H
    while i<len(ve):
        if h==0:
            return "not possible"
        if ve[i]<curr_health:
            curr_health -= ve[i]
            i+=1
        elif ve[i]>curr_health:
            i+=1
            h-=1
            curr_health=H
        else:
            h-=1
            i+=1
            curr_health=H
    return "possible"
        

v = int(input()) #4
h = int(input()) #4
H = int(input()) #3
ve=[]
for _ in range(v):
    ve.append(int(input()))
print(ve) # 3 1 3 3
print(hero_win_possible(ve,H,v,h))