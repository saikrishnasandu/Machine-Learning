
# isalpha()

x="machineLearning"
print(x.isalpha())


#isascii()

y="machine learning ^ $ *@ #"
print(y.isascii())


#isdecimal()  0 to 9 no comma or alphabets or fullstop nothing 

z ="45"
print(z.isdecimal())


# isdigit()

c="123460"
f="82"
print(c.isdigit())
print(f.isdigit())

#isidentifier

a = "Machinelearning"
b="machine learning"
print(a.isidentifier())
print("b is  identifier",b.isidentifier())



# islower()

c="machine Learning"
d="machine123"
e="123"
print(c.islower(),"\n",d.islower(),"\n e is lower",e.lower())


# isnumeric()

f="\u0030"
g='\u00B2'
h='1.2'
print(f.isnumeric(),"\n",g.isnumeric(),"\n",h.isnumeric())


# isprintable()

i="machinelearning"
j=" machine \rlearning"
print(i.isprintable(),j.isprintable())

# isspace()

k= "    "
l="   d \n "
m="\n"
print(k.isspace(),l.isspace(),m.isspace())



# istitle()

n="Machine Learning"
o="dawson"
p="HELLO"
print(n.istitle(),o.istitle(),p.istitle())



# isupper()

q ="MY NAME IS DAWSON"
r="hello"
print(q.isupper(),r.isupper())
