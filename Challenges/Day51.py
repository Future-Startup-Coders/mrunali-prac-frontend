def reverseList(head):
    left = 0
    right = len(head)-1
    while left < right:
        head[left], head[right] = head[right], head[left]
        left +=1
        right -=1
    return head


head = [1,2,3,4,5]
print(reverseList(head))
