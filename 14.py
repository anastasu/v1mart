x = 2*216**6 + 3*36**9 -432
k=0
while x>0:
    if x%6==5:k=k+1
    x = x//6
print (k)