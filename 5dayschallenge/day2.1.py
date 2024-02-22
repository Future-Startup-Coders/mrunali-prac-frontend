# Give a list, program to swap first and last element of the list.
def swap_num(lst):
    if lst:
        lst[0],lst[-1]=lst[-1],lst[0]
    return(lst)

enter_list = list(input("Enter numbers"))
print("ORIGINAL LIST: ", enter_list )
print("After swaping : ",swap_num(enter_list))


