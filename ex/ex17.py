from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

input1 = open(from_file)
# print(input1.read())

indata = input1.read()

# print("abc",indata)

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file) )
print("Ready, hit RETURN to continur, CRTL-C to abort.")

input()

output = open(to_file, 'w')
output.write(indata)
print("Alright, all done")

output.close()
input1.close()