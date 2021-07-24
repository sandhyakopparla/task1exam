n1=int(input("enter the num"))
even=[]
odd=[]
def check(n1):
    if n1%2==0:
        even.append(n1)
    else:
        odd.append(n1)
check(n1)
if(len(even)>0 and len(odd)<=0):
    print(even,"even no")
else:
    print(odd,"odd no")
    