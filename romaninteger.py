a={'I': 1,'II': 2 ,'III': 3 ,'IV': 4 ,'V': 5 ,'VI': 6 ,'VII': 7 ,'VIII': 8 , 'IX': 9 ,'X': 10,'C':100,'L':50 ,'D':500,'M':1000 }
roman = input("enter the roman alphabet:").upper()
l=len(roman)
if roman in a.keys():
    print("the integer nummer is:",a[roman])

            # or

a={'I': 1,'II': 2 ,'III': 3 ,'IV': 4 ,'V': 5 ,'VI': 6 ,'VII': 7 ,'VIII': 8 , 'IX': 9 ,'X': 10,'C':100,'L':50 ,'D':500,'M':1000 }
roman = input("enter the roman alphabet:").upper()
l=len(roman)
total=0
for i in range(l):
    if(i < (l-1) and a[roman[i]] < a[roman[i + 1]]):
        total=total - a[roman[i]]
    else:
        total=total + a[roman[i]]
print(f"the integer equelent of the {roman} is :",total)



