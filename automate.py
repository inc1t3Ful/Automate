"""
    read input file and automatically replace codewords with selected functions
    and creates new output file

  written by: Anthony Lee
              github.com/inc1t3Ful

  Last edit: 13 Aug 2017

"""

# 3rd iteration working with lists to read data into variables
# A list object is an iterator, so to print every element of the list, we can iterate over it
# declare empty list called 'lines'
lines = []
with open('testfile.txt', 'rt') as in_file:
    # for each line in string variable 'line'
    for line in in_file:
        # add line to list of lines, strip \n (newlines)
        lines.append(line.rstrip('\n'))

    # code below here is used to print everything
    """
    # for every element in our list
    for element in lines:
        # print it
        # another possibility instead of stripping newline char is to also just
        # have it print a '' instead by specifying end parameter
        # print(element, end= '')
        print(element)

    """
    # find() method finds the first 'e' in line 0. result is the # character
    # find can accept two additional parameters: integers representing indexes where it should start and stop its search
    # print(lines[0].find("e", 4)) means find 'e' starting at index 4 and onwards
    # not finding anything results in -1 result
    """
    print(lines[0].find("e", 25, 35))
    """

    # searching for substring using string's find() function
    """
    index = 0
    # string to run search on
    str = lines[0]
    # substring to search (what we're looking for)
    searchTerm = "e"

    # while index is less than length of the string
    while index < len(str):
        # set index to location of last occurence of search term
        index = str.find(searchTerm, index)

        # if there is no occurence, stop
        if index == -1:
            break

        # print the indexes of occurences of term found
        print(index)
        # increment index  by number of characters in searchTerm and repeat
        index += len(searchTerm)
    """

    # enumerate() takes another sequential object (such as a list), and returns an enumerate object.
    # The enumerate object creates a sequence of tuples from our list.
    # Each of these tuples comprises two pieces of data: an index number, and the data at that index
    # for...in, which we've already used, can keep track of multiple variables as it iterates.
    """
    print(list(enumerate(lines)))
    """

    # now have line numbers
    # for...in iterates over our enumerate object, which is created by iterating over lines
    # it places those values into the variables linenum and line, respectively
    """
    for linenum, line in enumerate(lines):
        print(linenum, line)
    """

    # Create enumerate object to track line number and character index for search term
    searchTerm = "e"

    for linenum, line in enumerate(lines):
        # cannot set index = 0 outside loop otherwise, it is static
        index = 0
        # store line in str variable str
        str = lines[linenum]

        while index < len(str):
            index = str.find(searchTerm, index)

            if index == -1:
                break

            print("line: ", linenum, "index: ", index)
            index += len(searchTerm)
