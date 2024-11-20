#  capitalize() method


a = "machine Learning"
print(a.capitalize())

a = "artificial Inteligence"
capitalize = a.capitalize()
print(capitalize)


g ="Pawan kalyan"
print(g.capitalize())



#casefold

m = "MaChine Learning"
print(m.casefold())

g ="PawaN kalyan"
print(g.casefold())


#center

m="machine learning"
print(m.center(30))
print(m.center(30,'#'))

print(g.center(30,'$'))


#count

m = "machine learning,machine learning"
print(m.count("machine"))
print(m.count("machine",0,27))

g = "pawan kalyan,pawan,pawan"
print(g.count("pawan",6,60))

#encode()

a = "machine learning ~"
print(a.encode(encoding="utf-8",errors="ignore"))
print(a.encode(encoding="utf-8",errors="strict"))
print(a.encode(encoding="utf-8",errors="replace"))
print(a.encode())