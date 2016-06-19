from sys import argv

script,filename = argv

txt = open(filename,'w')

print("Here's your file %r:" % filename)
#print(txt.read())

# print("Type the filename again:")
# filename_again = input(">")
# txt_again = open(filename_again)

# txt.close()

# txt.truncate()
# txt.write("abc")
#txt.close

txt = open(filename)


## print(txt.read())
indata = txt.read()

#txt.write("abc")


print("len(txt.read()) = %r " % len(txt.read())) # 0
print("len(indata) = %r " % len(indata))      # 3("abc")
print("len(\"oh my god\") = %r" % len("oh my god"))

print(indata)

txt = open(filename)
print(txt.read())