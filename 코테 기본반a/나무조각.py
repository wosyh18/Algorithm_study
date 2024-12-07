tree = list(map(int,input().split()))
n=len(tree)
for i in range(n) :
   for j in range (0,n-i-1):
      if tree[j] > tree [j+1]:
         tree[j],tree[j+1] = tree[j+1] , tree[j]
         print ( *tree )  