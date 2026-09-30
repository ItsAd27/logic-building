print("1,addition")
print("2,substraction")
print("3,multiplication")
print("4,division")


while True:
    choice=int(input("Enter the choice:"))

    if choice>4:
        print("Enter valid input")

    elif choice==1:
        a=int(input("Enter no:"))
        b=int(input("Enter no:"))
        z=a+b
        print("addition=",z)  
    elif choice==2:
        a=int(input("Enter no:"))
        b=int(input("Enter no:"))
        z=a-b
        print("substraction=",z)
    elif choice==3:
        a=int(input("Enter no:"))
        b=int(input("enter no:"))
        z=a*b
        print("multiplication=",z)
    elif choice==4:
        a=int(input("Enter no:"))
        b=int(input("Enter no:"))
        z=a/b
        print("division=",z) 

    elif choice==5:
        print("thank you")
        break