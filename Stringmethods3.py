# format_map()

data = {"name":"machine","age":"Learning"}
txt="my name is {name} i am {age}"
print(txt.format_map(data))


#index()

txt="Machine learning"
x=txt.index("learn")
print(x)


txt1="machine learning"
x2=txt1.index("c",1,5)
print(x2)

'''txt2="machine learning"
x3=txt2.index("k")
print(x3)'''

#isalnum

isallnumm="machinelearning6474"
isnotallnum=" - machine learning"
x=isallnumm.isalnum()
x1=isnotallnum.isalnum()
print(x1)

print(x)


