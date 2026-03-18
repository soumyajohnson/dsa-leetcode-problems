from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        email_to_name={}

        def find(email):
            if parent[email]!=email:
                parent[email]=find(parent[email])
            return parent[email]

        def union(e1,e2):
            r1=find(e1)
            r2=find(e2)
            if r1!=r2:
                parent[r2]=r1

        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email]=email
                email_to_name[email]=name
        
        for acc in accounts:
            first=acc[1]
            for email in acc[2:]:
                union(first,email)
        
        groups=defaultdict(list)
        for email in parent:
            root=find(email)
            groups[root].append(email)
        
        res=[]
        for root,email in groups.items():
            name=email_to_name[root]
            res.append([name]+sorted(email))
        
        return res