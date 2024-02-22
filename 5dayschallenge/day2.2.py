# write a python program of reverse string

def my_string(str):
    return str[-1::-1]

input_string = str(input("Enter String : "))
print("Reverse String is : ",my_string(input_string))