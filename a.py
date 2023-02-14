arr=[3,2,6,5,1,4,8,9]
su=0
s=''
for i in arr:
    if i in range(5,9):
        s+=str(i)
    else:
        su+=i

print(su,' ',s)
