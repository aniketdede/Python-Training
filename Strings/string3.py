# STRING MANIPULATION - using string methods

# 1) center(): put the text in the middle and fill the extra space with a character
from collections import deque


text = "easy"
print("original string:", text)
print("centered string:", text.center(10, "@"))

# 2) endswith(): check if the text ends with a specific suffix
text = "open softwares"
print(text.endswith("softwares"))
print(text.endswith("Softwares"))

# 3) startswith(): check if the text begins with a specific prefix
text = "Open softwares"
print(text.startswith("open"))
print(text.startswith("Open"))

# 4) find(): search for a substring and return its index position
text = "we can learn python easily"
print(text.find("python"))        # search for "python" in the whole string
print(text.find("python", 10))    # search for "python" starting from index 10
print(text.find("python", 15))    # search for "python" starting from index 15
print(text.find("can", 3, 10))    # search for "can" only between index 3 and 10




#placeholder => identified by '{}'
A = "Tom"
B = "Pune"

print("I am {} from {}".format(A,B))

#Alphanumber 

str1 = "easy@123"
str2 = "easy123"

print(str1.isalnum())
print(str2.isalnum())


#isDigit 


str1 = "123"
str2 = "easy"

print(str1.isdigit())
print(str2.isdigit())


#isIdentifier

str1 = "easy"
str2 = "123"
str5 = "abc"
str3 = "@abe23"
str4 = "abc123"

print(str1.isidentifier())
print(str2.isidentifier())
print(str3.isidentifier())
print(str4.isidentifier())
print(str5.isidentifier())



 #lists
 
my_list = [8,1,0,8,6,5,9]
my_list.sort()
print(my_list)
print(my_list.index(8))
a=my_list.count(8)
print(a)
my_list.reverse()
print(my_list)
 

#stack


stack = [3,4,5]
stack.append(8)
stack.append(0)
print(stack)
x=stack.pop()
print(x)



# queue

queue = deque(["yash", "krishna","sahil", "shivtej"])
queue.append("swati")
queue.append("xyz")
print(queue)
a=queue.pop()
print(a)


#TOUPLE

my_touple=()
print(my_touple)

my_touple=(4,5,8,9)
print(my_touple)


my_touple=(4,"python",3.31)
print(my_touple)  

my_tuple=['p','e','w','i','t']
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-4])


n_touple=('mouse',[2,4,9,0],(52,65,85))
print(n_touple[0][3])
print(n_touple[0][1])



from os import remove


my_set = {4,5,8,0}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([45,6,9,44])
print(my_set)
x = my_set.union({50,60,80,90})
print(x)

x.remove(80)
print(x)



setA = {4,5,6,7}
setB ={8,9,10,6}
if setA&setB == set():
  print("true")
else :
 print("false")
 
 
print("union:",setA|setB) 



#dictionary

student = {
    "name": "Aniket",
    "age": 20,
    "courses": ["math", "science"]
}
print(student.pop("courses"))
print(student)
print(student.popitem())