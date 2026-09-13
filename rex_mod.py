import re

# match method in Python's re module is used to determine if the RE matches at the beginning of the string. It returns a match object if there is a match, or None if there isn't.

# match() - checks whether the pattern exists at the beginning of the string

text = "The rain in Spain"
result = re.match("hello", text)
# print(result)  # Output: None, since "hello" is not at the beginning of the string
if result:
    print("Match found:")
else:
    print("No match found.")  # Output: No match found.
 
    
text = "The rain in Spain"
result = re.match("The", text)
# print(result)  # Output: None, since "hello" is not at the beginning of the string
if result:
    print("Match found:")
else:
    print("No match found.")  # Output: No match found.
    
    
# search method in Python's re module is used to search for a pattern anywhere in the string. It returns a match object if there is a match, or None if there isn't.
# re.search() - for whole string search
text = "The rain in Spain"
result = re.search("rain", text)
if result:
    print("Match found:")  # Output: Match found:   
else:
    print("No match found.")
    
    
    
    
    
    



    