a=[11,12,-10,15,17,200,13]
print(sorted(a))

# or
l=len(a)
temp=0
for i in range(0,l,1):
    for j in range(i+1,l,1):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)