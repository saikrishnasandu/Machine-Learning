txt = "machine learning {price:.2f}"
print(txt.format(price =50))
txt1="machine learning {name}age is{num}".format(name="intresting",num=100)
print(txt1)
txt2="aritifcial intelligence{1},machine learning is{0}".format("primary","secondary")
print(txt2)
txt3="machine{},deep{}".format("learning","artificial")
print(txt3)

txt4="machine learning {:<8}  artificial intelligence"
print(txt4.format("and"))
txt5="machine learning {:>9} artifficial intelligence"
print(txt5.format("and"))
txt6="machine learning {:^9} artificial intelligence"
print(txt6.format("and"))
txt7="machine learning {:+} artificial intelligence"
print(txt7.format(5))
txt8="The temperature is {:+} and {:+} degrees celsius"
print(txt8.format(-3,5))
txt9="the temperature is {: } and {:} degres celsius"
print(txt9.format(-3,7))
txt10="Earth is {:,} years old"
print(txt10.format(13000000000))
txt11="Earth is {:_} years old"
print(txt11.format(130000000000))
txt12="the binary of {0} is {0:b}"
print(txt12.format(5))
txt13="the unicode character {:c} "

print(txt13.format(2665))
txt14="\u2665"
print(txt14)
txt15="\u263A"
print(txt15)
emoji="\U0001F600"
print(emoji)
txt16="decimal format {:d}"
print(txt16.format(0b101))
txt17="the price is {:f} dollars"
print(txt17.format(12))
txt18="the price is {:.3f} dollars"
print(txt18.format(12))
a=float("inf")
txt19="the price is {:F},{:f} dollars "
print(txt19.format(a,a))

txt20="The America{:G}"
print(txt20.format(20000000))

txt21="The America {:g}"
print(txt21.format(393930330993))

txt22="the octal version of {0} is {0:o}"
print(txt22.format(25))

txt23="the hexadecimal version of {0} is {0:x}"
print(txt23.format(255))
z="I scored {:%}"
print(z.format(99))


