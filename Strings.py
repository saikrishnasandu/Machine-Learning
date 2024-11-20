  
'''#Quotation

print("Hello ML")
print('Hello Ml')  # Both are same.


#Quotes inside Quotes

print("Hello world")
print("Hello's ML")
print('Hello "ML"')


# creating or assigni a string to variable.

a = " hello"
print(a)

#Multiline string

a = """ I will bocome a
    machine learning engineer in 6 months"""
print(a)


#Strings are arrays

# We can access characters of a string by positions and starts from 0

a = "machine larning"
print(a[1]) # to print the position 1 character in the string


#Looping through a String

# Loop through the letters in the word " Banana":

for x in "banana":
    print(x)



# Length function len() used to print length of a string
Q = " Machine learning"
print(len(Q))



# check String by using   in keyword

a = "machine learnig is very interesting"
print("machine" in a)


# using it in if statement

a = "machine learnig is unique"
if "unique" in a:
   print("yes,'unique' is present ")

    
#not in
   
text = "machine learning is free"
print("expensive" not in text)
text = "machine learning is free"
if "expnesive" not in text:
    print('"expensive" is not present')'''

a = "machine Learning"
print(a[1])

print(len(a))
print("Learn" in a)
print("nut" not in a)


print(a[2:7])

