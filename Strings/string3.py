# STRING MANIPULATION - using string methods

# 1) center(): put the text in the middle and fill the extra space with a character
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

# function to check if a number is even or odd

 