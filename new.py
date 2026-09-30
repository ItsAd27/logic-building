num=(input("Enter the number"))
flag=0
for i in range(2,num//2+1):
   if (num%i==0):
      flag=1
      break  
if (flag==1):
   print("num is not prime")

else:
   print("num is prime ")


   

