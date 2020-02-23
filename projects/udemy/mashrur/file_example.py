file_name = './data.txt'

# not recommended way
f = open(file_name)
# f_contents = f.read() # read all
# f_contents = f.readline() # just read first line
for line in f:
    # print(line)
    print(line.strip()) # remove empty line
f.close()  # definitely close file when you open a file

# recommended way !!
with open(file_name) as f: # this is context manager no need to close when using with !!
    for line in f:
        print(line.strip())


record_to_add = 'even,choi:python,javascript,c++'

# w option will overwrite all the contents in file
# r is default option for reading a file
# a+ option appends data
with open(file_name, "a+") as to_write:
    to_write.write(record_to_add + "\n")

