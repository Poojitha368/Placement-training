# accounts merge
'''class Solution(object):
    from collections import defaultdict
    def accountsMerge(self, accounts):
        rank = [0]*len(accounts)
        parent = [i for i in range(len(accounts))]
        def findUParent(u):
            if u==parent[u]:
                return u
            parent[u]=findUParent(parent[u])
            return parent[u]
        def findUnion(u,v):
            U = findUParent(u)
            V = findUParent(v)
            if rank[U]==rank[V]:
                parent[V]=U
                rank[U]+=1
            elif rank[U]>rank[V]:
                parent[V]=U
            else:
                parent[U]=V
        mailMap = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in mailMap:
                    mailMap[accounts[i][j]]=i
                else:
                    findUnion(mailMap[accounts[i][j]],i)
        
        merged = defaultdict(list)
        for email,idx in mailMap.items():
            I = findUParent(idx)
            merged[I].append(email)
        
        res = []
        for idx,emails in merged.items():
            res.append([accounts[idx][0]] + sorted(emails))
        return res'''