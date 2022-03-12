s= open ('inf_22_10_20_24.txt').readline ()
c=1
for i in range (1,len(s)):
    if s.count('E') > s.count ('A'):
        c+=1
print(c)