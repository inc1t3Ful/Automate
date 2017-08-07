""" read input file and automatically replace codewords with selected functions
    and creates new output file

  written by: Anthony Lee
              github.com/inc1t3Ful

  Last edit: 6 Aug 2017

"""
# 1st iteration
in_file = open("testfile.txt", "rt")    # open input file and Read Text
contents = in_file.read()               # read entire file into string variable
in_file.close()                         # close file
print(contents)                         # print


# open input file and Read Text, then close. Print contents
with open('testfile.txt', 'rt') as in_file:
    # store each line in string variable "line"
    for line in in_file:
        # print line
        print(line)

# 2nd iteration working with lists to read data into variables
# declare empty list called 'lines'
lines = []
with open('testfile.txt', 'rt') as in_file:
    # for each line in string variable 'line'
    for line in in_file:
        # add line to list of lines
        lines.append(line)
        print(lines)
