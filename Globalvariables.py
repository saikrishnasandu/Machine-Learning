

# Golbal variables can be used by everyone both inside and outside function

# create a variable outside a function use it inside a function

x = " Machine Learning"

def myfunc():
    print("python " + x)
myfunc()

# creating  variables with same name in and out function

x = " python"

def myfunc():
    x="machine learning"
    print("python is " + x)
myfunc()

print(x)


# to create a global variable inside a function use the global keyword

def myfunc():
    global x
    x = "machine learning"
myfunc()

print("python " + x)

#also use the global keyword if you want to change a global variable inside a function

x = " sai krishna"

def myfunc():
    global x
    x = "machine learning"
myfunc()

print("python " + x)
