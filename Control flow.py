#Program 1. if 
a=int(input("Enter the value for a:")) 
b=int(input("Enter the value for b:")) 
if a>b: 
   print("A is greater") 
if b>a: 
   print("B is greater")

#Program 2. if else 
a=int(input("enter a number")) 
if a>=0:
   print("positive") 
else: 
   print("negative")

#Program 3. elif(Multiple if) 
a=input("Enter the value for a:") 
b=input("Enter the value for b:") 
c=input("Enter the value for c:") 
if a>b and a>c: 
   print("A is greater") 
elif b>c: 
   print("B is greater") 
else: 
   print("C is greater")

#Program 4. elif 
mark=int(input("Enter ur mark:")) 
if mark>90 and mark<=100: 
     print("O grade") 
elif mark>80 and mark<=90: 
     print("A grade") 
elif mark>70 and mark<=80: 
     print("B grade") 
elif mark>60 and mark<=70: 
     print("C grade") 
elif mark>40 and mark<=60: 
     print("D Grade") 
else: 
     print("Fail") 


     completed python control flow