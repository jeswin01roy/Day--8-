a=[11,12,13,14,15,16,17,18,19,20]
first=[]
sec=[]
count=0
for i in a:
    count=count+1
print(count)
s=count//2
print(s)
for i in range(0,count,1):
    if(i<s):
        first.append(a[i])
    else:
        sec.append(a[i])

print(first)
print(sec)