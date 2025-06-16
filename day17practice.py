from collections import defaultdict
graph = [(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=defaultdict(list)
for u,v in graph:
    d[u].append(v)
    d[v].append(u)
print(d)


def dfs(u,visited=set()):
    if u in visited:
        return
    print(u)
    visited.add(u)
    for i in d[u]:
        dfs(i)
    return visited
print(dfs(5))

d={5: [2, 7, 8], 2: [5, 7, 8, 3], 7: [5, 2, 8], 8: [5, 2, 7, 3], 3: [8, 2]}
def print_all_paths(u,v,path):
    if u == v:
        print(path)
        return
    for i in d[u]:
        print_all_paths(i,v,path+[i])

print_all_paths(0,4,[0])


d={0:[4,3,1],1:[3,2,4],3:[4],2:[3],4:[]}
def count_all_paths(u,v,cnt):
    if u==v:
        cnt[0]+=1
        return
    for i in d[u]:
        count_all_paths(i,v,cnt)
cnt = [0]
count_all_paths(0,4,cnt)
print(cnt)


d={0:[4,3,1],1:[3,2,4],3:[4],2:[3],4:[]}
def if_path_exist_or_not(u,v):
    if u == v:
        return True
    for i in d[u]:
        if if_path_exist_or_not(i,v):
            return True
    return 
    

print(if_path_exist_or_not(0,4))








    