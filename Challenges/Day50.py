def mergeTwoLists(list1, list2):

    sortedlist = []
    i , j = 0, 0
    while i < len(list1) and j <len(list2):
        if list1[i] < list2[j]:
            sortedlist.append(list1[i])
            i +=1
        else:
            sortedlist.append(list2[j])
            j +=1

    while i < len(list1):
        sortedlist.append(list1[i])
        i+=1
    
    while j < len(list2):
        sortedlist.append(list2[j])
        j+=1
    
    return sortedlist


list1 = [1,2,4,6]
list2 = [1,3,5]
print(mergeTwoLists(list1, list2))