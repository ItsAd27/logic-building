num=int(input("Enter the total num "))
l=[]
for i in range(num):
n=int(input("Enter the num"))
    l.append(n)

mul=1
for i in range(0,len(l)):
        
        mul=mul*l[i]

print(mul)                                                 
name=int(input("Enter the name"))
age=int(input("Enter the age"))
print("agter 20 year your age",age+20)
print(type,name)
print(type,age)



