#program 1
Tfile=open("samp.txt","w") 
Tfile.write("hai\n") 
Tfile.write("welcome\n") 
Tfile.write("to\n") 
Tfile.write("python program\n") 
Tfile.close() 
print ("\n"*20) 
Tfile=open("samp.txt","r") 
for line in Tfile: 
  print (line) 
Tfile.tell() 
print (Tfile) 
Tfile.seek(6) 
print (Tfile) 
print(Tfile.read()) 
Tfile.close()

#Program 2 
Tfile=open("samp.txt","r") 
x=Tfile.readlines() 
print (x) 
'''x1=Tfile.readline() 
print (x1) 
x1=Tfile.readline() 
print (x1) 
Tfile.close() 

#Program 3 
T=open("sample.txt","w") 
T.writelines("hai\n welcome\n to \n csc\n computer\n center") 
T.write("\nHello!.......") 
T.close() 
T=open("sample.txt","r") 
a=T.readlines() 
print (a) 
b=T.read() 
print (b) 
T.close() 

#Program 4 
Tfile=open("samp.txt","write") 
Tfile.write("hii\n") 
Tfile.write("Welcome to\n") 
Tfile.write("CSC Computer Education\n") 
Tfile.write("Medavakkam Branch\n") 
Tfile.close() 
Tfile=open("samp.txt","read") 
for line in Tfile: 
  print (line) 
Tfile.tell() 
print (Tfile) 
Tfile.seek(2) 
print (Tfile) 
print (Tfile.read()) 
Tfile.close() 

#Program 5 
tfile=open("details.txt","w") 
a=raw_input("enter a name:") 
tfile.write(a) 
print (a) 
tfile.close()


completed text and binary python