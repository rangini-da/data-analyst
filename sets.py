#Program 1. Creating List 
fruits = ['apple', 'banana', 'orange']
fruits.append('grape') 
fruits.insert(1, 'kiwi') 
fruits.remove('banana') 
print (fruits)

#Program 2. Modifying and Extending 
numbers = [1, 2, 3, 4, 5] 
numbers[2] = 6 
numbers.extend([7, 8, 9]) 
print("Modified and Extended List:", numbers) 

#Program 3. List Comprehensions 
numbers = [1, 2, 3, 4, 5] 
sq_num = [num ** 2 for num in numbers] 
print("Squared Numbers:", sq_num) 

#Program 4. Iterating 
courses = ["hdfd", "hdpd", "hdjd", "hdwd"] 
print("Courses:") 
for course in courses: 
  print(course) 

#Program 1. Accessing 
courses = ("hdfd", "hdpd", "hdjd", "hdwd") 
print ("First course:", courses [0]) 
print ("Last course:", courses [-1]) 
print ("Second and third courses:", courses [1:3]) 

#Program 2. Unpacking 
Course = ("HDFD", 30000, "C C++ Java Python") 
crs, fees, syll = Course 
print ("Course:", crs) 
print ("Fees:", fees) 
print ("Syllabus:", syll)

#Program 3. Concatenating 
tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6) 
print (tuple1) 
print (tuple2) 
c_t = tuple1 + tuple2 
print ("Concatenated Tuple:", c_t) 

#Program 4. Iterating 
courses = ("hdfd", "hdpd", "hdjd", "hdwd") 
print("Courses:") 
for course in courses: 
  print(course)

#Program 1. Integer Key values 
dict1={1:"one",2:"two",3:"Three"} 
print dict1

#Program 2. Mixed Key values 
dict2={"Name":"RCS","Course":"Ethical Hacking","timing":"Evening"} 
print (dict2) 
print dict2.get('Name') 
print dict1.get(1) 
print (dict2['Course']) 
dict2['timing']="morning"#alter the values 
print (dict2) 
dict2['fees']=10000 #to add a new item 
print (dict2) 
print("The values are:" , dict2.values()) 
dict3={11:"a",12:"b",13:"c"} 
print (dict3) 
dict3.pop (12) 
print (dict3) 
dict3.popitem() 
print (dict3) 
dict3.clear()
print (dict3) 
dict3={11:"a",12:"b",13:"c",14:"d"} 
print (dict3) 
del dict3[13] 
print (dict3) 
del dict3  
print (dict3) 

#Program 3. Manipulation 
dict2={"Name":"RCS","Course":"Big Data","timing":"Evening"} 
dict1={2:"a",1:"b",5:"bb"} 
print (dict2) 
print (dict2.keys()) 
print (dict2.values()) 
print (dict2.items()) 
print (sorted(dict2)) 
print (sorted(dict1)) 
print (len(dict2))

completed sets_py
