M=100
fa=[]
def ini(n,l=[]):
    for i in range(n+1):
        l.append(i)

def find(a):
    if fa[a]==a:
        return a
    else:
        fa[a]=find(fa[a])
        return fa[a] 

def union(a,b):
    f_a=find(a)
    f_b=find(b)
    fa[f_a]=f_b

n,m=map(int,input().split())
ini(n,fa)
print(fa[0])
for i in range(m):
    a,b=map(int,input().split())
    union(a,b)
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    if find(a)==find(b):
        print("Yes!")
    else:
        print("No!")

