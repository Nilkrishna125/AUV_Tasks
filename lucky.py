print("hello")
val=input("give number ")
r=int(val)
j=0

while r>0:
    g=r%10
    r=r//10
    if g==7 or g==4:
        j=j+1
i=0
while j>0:
    g=j%10
    j=j//10
    if g!=4 and g!=7:
        i=1
        break
if i==0:
    print("yes")
else:
    print("no")



