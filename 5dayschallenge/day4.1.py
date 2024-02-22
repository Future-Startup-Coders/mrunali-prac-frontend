# Takes a string as input and returns a dictionary containing the frequency of each character in the string.
def return_dict(dict):
    frequency={}   # {} this is called dictionary
    for char in dict:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char] =1
    return frequency

str = str(input("Enter String : ",))
print("Dictionary containing the frequency of each character: ", return_dict(str))