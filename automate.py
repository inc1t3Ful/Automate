"""
    read input file and automatically replace codewords with selected functions
    and creates new output file

  written by: Anthony Lee
              github.com/inc1t3Ful

  Last edit: 6 Jan 2018

"""
# import python regular expression module to strengthen search capabilities
import re

# 3rd iteration working with lists to read data into variables
# A list object is an iterator, so to print every element of the list, we can iterate over it
# declare empty list called 'lines'
lines = []
# test = open('testfile2.txt', 'rw')
# read testfile2.txt
with open('testscript_input.txt', 'rtw') as in_file:
    # for each line in string variable 'line'
    for line in in_file:
    # add line to list of lines, strip \n (newlines)
    # removing rstrip for \n does not work for better formatting [22 Sep 2017 edit10]
        lines.append(line.rstrip('\n'))

    d_occur = re.sub(r"\w\w\wd\w\w\w", "delete\n", str(lines))
    a_occur = re.sub(r"\w\w\wa\w\w\w", "add\n", str(d_occur))
    c_occur = re.sub(r"\w\w\wc\w\w\w", "remove\n", str(a_occur))
    minus_occur = re.sub(r"---", "add\n", str(c_occur))

# test output for minus_occur (22 Sep 2017 edit12)
test = open("testscript_output.txt", "w")
test.write(minus_occur)
test.close()

print(d_occur)
# testjoin = ''.join(filter(str.isalnum, minus_occur))
# print(testjoin)
print(" ")
# print(''.join(minus_occur))
pattern = re.sub(r'([^\s\w]|_)+', '', minus_occur)
# strippedList = pattern.sub('', minus_occur)
print pattern

            # self note: what we want to do is
            # 1. open file
            # 2. convert text file into an entire string(?) is there more efficient way?
            # 3. find all /and/or replace all required codewords with correct terms
            # 4. print out new text file/ same one with changes
