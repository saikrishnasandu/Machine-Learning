#endswith()

txt="machine Learning"
print(txt.endswith("Learning"))


txt = "example.jpg"
txt1="rmp.pdf"
print(txt.endswith((".jpg",".pdf")),txt1.endswith(".txt"))

r="siva sankara satyanarayana vara prasad"
print(r.endswith("prasad",0,))

#expandtabs()

h ="hello\tworld"
print(h.expandtabs(25))


#find()

j = "Machine learning"
fd=j.find("in")  #op  4
print(fd)

fd=j.find("in",0,3)  # output -1
print(fd)

#fd=j.index("f") index raises an exception if the charcter not found 

print(fd)
