file_name = './data.txt'

record_to_read = 'james,choi:python,javascript,c'

# not recommended way
f = open(file_name)

# f_contents = f.readline()
# marshrur,hossain:python,ruby,javascript

# f_contents = f.read()
"""
john,doe:java,c,c++
paige,choi:ruby,rails,java
harry,kim:python,javascript,c
"""

for line in f:
    print(line.strip())

f.close()  # definitely close file when you open a file

# when using open, do not need to think about closing a file
with open(file_name) as f:
    for line in f:
        print(line.strip())

# w option will overwrite all the contents in file
# r is default option for reading a file
# a+ option appends data
with open(file_name, 'a+') as to_write:
    to_write.write(record_to_read + '\n')
