a=int(input("Enter First Number - "))
op=input("Enter Operation (+-*/) = ")
b=int(input("Enter First Number - "))
if op=="+":
    print("Total value =",a+b)
elif op=="-":
    print("Total value =",a-b)
elif op=="*":
    print("Total value =",a*b)
elif op=="/":
    print("Total value =",a/b)
else:
    print("Something Invalid")
