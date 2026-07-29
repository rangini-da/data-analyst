list program1
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
fruits.insert(1, 'kiwi')
fruits.remove('banana')
print (fruits)
program2
numbers = [1, 2, 3, 4, 5]
numbers[2] = 6
numbers.extend([7, 8, 9])
print("Modified and Extended List:", numbers)
program3
numbers = [1, 2, 3, 4, 5]
sq_num = [num ** 2 for num in numbers]
print("Squared Numbers:", sq_num)
program4
courses = ["hdfd", "hdpd", "hdjd", "hdwd"]
print("Courses:")
for course in courses:
 print(course)
Tuples program1
courses = ("hdfd", "hdpd", "hdjd", "hdwd")
print ("First course:", courses [0])
print ("Last course:", courses [-1])
print ("Second and third courses:", courses [1:3])
program2
Course = ("HDFD", 30000, "C C++ Java Python")
crs, fees, syll = Course
print ("Course:", crs)
print ("Fees:", fees)
print ("Syllabus:", syll)
program3
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print (tuple1)
print (tuple2)
c_t = tuple1 + tuple2
print ("Concatenated Tuple:", c_t)
program4
courses = ("hdfd", "hdpd", "hdjd", "hdwd")
print("Courses:")
for course in courses:
 print(course)
Dictionary program1
dict1={1:"one",2:"two",3:"Three"}
print dict1
program2
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
program3
dict2={"Name":"RCS","Course":"Big Data","timing":"Evening"}
dict1={2:"a",1:"b",5:"bb"}
print (dict2)
print (dict2.keys())
print (dict2.values())
print (dict2.items())
print (sorted(dict2))
print (sorted(dict1))
print (len(dict2))
program4
book_prices = {
 "Python Crash Course": 25,
 "Deep Learning": 40,
 "Algorithms Unlocked": 30
}
print("Book Prices:")
for book, price in book_prices.items():
 print(f"{book}: ${price}")
print("\nAvailable Books:")
for book in book_prices.keys():
 print(book)
print("\nBook Prices:")
for price in book_prices.values():
 print(f"${price}")
Sets program1
ms= {1, 2, 3, 3, 4}
print(ms)
program2
ms = {1, 2, 3, 4}
print(2 in ms)
program3
ms = {1, 2, 3}
ms.add(4)
print(ms)
ms.update({5, 6})
print(ms)
ms.remove(2)
print(ms)
ms.discard(5)
print(ms)
program4
a={1,2,3,4,50,45}
print (a)
b={5,6,7,8,1,2,3,4}
print (b)
print ("union of a& b:", a|b)
print ("union of a & b by function:",a.union(b))
print ("union of a & b by union function:",b.union(a))
print ("Intersection of a & b:",a &b)
print ("Intersection of a & b by function:",a.intersection(b))
print ("Set Difference in a & b:",a-b)
print ("Set Difference in a & b:",b-a)
print ("Set Difference in a & b:",a.difference(b))
print ("Set Symmetric Difference in a & b:",a^b)
print ("Set Symmetric Difference in a & b:",a.symmetric_difference(b))
Frozenset Syntax 
frozen_fruits = frozenset(['apple', 'banana', 'orange']) 
Program 1. Frozenset Operations 
frozen_set1 = frozenset({1, 2, 3}) 
frozen_set2 = frozenset({3, 4, 5}) 
union_frozen = frozen_set1.union(frozen_set2) 
intersection_frozen = frozen_set1.intersection(frozen_set2) 
When to Use Sets vs. Frozensets: 


completed sets_py

