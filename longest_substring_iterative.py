s=input()
n=len(s)
c=""
maxx=0
for i in range(n):
    if s[i] in s and s[i] not in c:
        c+=s[i]
    else:
        maxx=max(len(c),maxx)
        c=s[i]

print(maxx)
