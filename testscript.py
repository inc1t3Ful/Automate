# testscript
import re

a = ['m34d34f', 'q6wa890', '4s5c8re', '---', '8n6d3eo', 'm6wapoz', '987c4k3']
print("Original array")
print(a)
print('')

# don't forget to convert to string for the input for findall
# the correct format for the chracter search is found below here
b = re.findall(r"\w\w\wd\w\w\w", str(a))

print("This is re.findall method for d:")
print(b)
print('')

# test regex sub for 'a' keywords
c = re.sub(r"\w\w\wa\w\w\w", "add", str(a))

print("This is re.sub method for a:")
print(c)
print('')

# test regex sub for '---' keywords
d = re.sub(r"\w\w\w---\w\w\w", "add", str(a))

print("This is re.sub method for ---")
print(d)
print('')
