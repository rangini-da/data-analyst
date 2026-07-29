String Function 
str1="good evening
str2="        WELCOME       "
str3="        I Am A B.E Student" 
a="1234"
sp="     " 
print str1 
print ("Capital of str1=",str1.capitalize()) 
print ("Center of str1=",str1.center(20,'*')) 
print ("Count of e in str1=",str1.count('e')) 
print ("Substring of str3=",str3.count("B.E",0,len(str3))) 
print ("Substring of str3=",str3.find("B.E",0,len(str3))) 
print ("Replace the B.E to ECE in str3=",str3.replace("B.E","E.C.E")) 
print ("Is alpha or not in str1=",str1.isalpha()) 
print ("IS lower case str1=", str2.lower()) 
print ("IS upper case str2=", str1.upper()) 
print ("Space=",sp.isspace()) 
print ("Space=", str1.isspace()) 
print ("Length str1=", len(str1)) 
print ("Title of str3=", str3.istitle()) 
print ("Title of str2=", str2.istitle()) 
print ("Lstrip in str3=", str3.lstrip()) 
print ("Rstrip in str3=", str1.rstrip()) 
print ("strip in str3=", str2.strip()) 
print ("lower str2=", str2.lower()) 
print ("upper str1=", str1.upper()) 
print ("Swap str3=", str3.swapcase()) 
print ("split str3=", str3.split()) 
print ("Join str1 and str2=", str1.join(str2)) 
print (' '.join (['hai','welcome','to','csc'])) 

#String Embedding 
h1 = "CSC Computer Education" 
h2 = "Medavakkam Branch" 
msg = "Hi Welcome to {} and you have visited {}. ".format(h1, h2) 
print(msg) 

#String Formatting Python 3.6 introduced f-strings, a more concise way of formatting strings. 
h1 = "Anigra Training Academy" 
h2 = "Medavakkam" 
msg = "Hi Welcome to" ,{h1}, "and you have visited", {h2} 
print(msg) 


completed string_py
