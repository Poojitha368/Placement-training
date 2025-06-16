from collections import defaultdict
graph = [(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
# graph = [(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
def print_all_possible_paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
        path.pop()
        return
    for i in d[u]:
        if i not in path:
            print_all_possible_paths(i,v,path)
    path.pop()
    return

'''def count_all_possible_paths(u,v,path=[],c=0):
    path.append(u)
    if(u==v):
        c=c+1
    else:
       for i in d[u]:
           if(i not in path):
              c=count_all_possible_paths(i,v,path,c)
    path.pop()
    return c'''

'''def check_if_path_exists(u,v,path=[]):
    path.append(u)
    if u==v:
        return True
    else:
        for i in d[u]:
            if i not in path:
                if check_if_path_exists(i,v,path):
                    return True
        path.pop()
        return False'''

'''def bfs(u):
    v=set()
    l = []
    l.append(u)
    v.add(u)
    while l:
        curr = l.pop(0)
        print(curr)
        for i in d[curr]:
            if i not in v and i not in l:
                l.append(i)
                v.add(i)'''

'''def path_exist_or_not_bfs(u,v,d):
    l = []
    l.append(5)
    v.add(5)
    while l :
        curr = l.pop(0)
        if curr == v:
            return True
        for i in d[curr]:
            if i not in l and i not in v:
                l.append(i)
                v.add(i)
    return False'''

'''def print_all_paths_weighted(u,v,path=[],cost=0):
    path.append(u)
    if u==v:
        print(path,cost)
        path.pop()
        return
    for i,w in d[u]:
        if i not in path:
            cost += w
            print_all_paths_weighted(i,v,path,cost)
            cost = cost-w
    path.pop()
    return'''

        

        





#unweighted graph
d=defaultdict(list)
for i,j in graph:
    d[i].append(j)
    d[j].append(i)
print(d)
print_all_possible_paths(5,3)
# print(count_all_possible_paths(5,3))
# print(check_if_path_exists(5,3))
# print(bfs(5))


# #weighted graph
# d = defaultdict(list)
# for i,j,w in graph:
#     d[i].append([j,w])
#     d[j].append([i,w])
# print(d)

# print(print_all_paths_weighted(5,3))



