a=int(input("a"))
b=int(input("b"))
sum=a+b
sub=a-b
div=a/b
mul=a*b
opr=(input("sum,mul,div or sub?"))
print(opr)
if(opr=="sum"):
    print(a+b)
elif(opr=="sub"):
    print(a-b)
elif(opr=="mul"):
    print(a*b)
elif(opr=="div"):
    print(a/b)
else:
    print("INVALID OPERATION")


