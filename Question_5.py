"""
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from the
end". You should copy/paste the Node class below to use as a representation of
a node in the linked list. Return the value of the node at that position.

e.g. 10->20->30->40->50
"""
global ll
ll = None

class Element(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def add(new_data):
    global ll
    node = Element(new_data)
    node.next = ll
    ll = node

def Question5(ll, m):
    element1 = ll
    element2 = ll
    c = 0
    
    if(ll is not None):
        while(c < m):
            element2 = element2.next
            c += 1

    while(element2 is not None):
        element1 = element1.next
        element2 = element2.next

    return element1.data

add("0")
add("9 WXYZ")
add("8 TUV")
add("7 PQRS")
add("6 MNO")
add("5 JKL")
add("4 GHI")
add("3 DEF")
add("2 ABC")
add("1")

assert (Question5(ll, 4) == '7 PQRS')
assert (Question5(ll, 8) == '3 DEF')
assert (Question5(ll, 1) == '0')

print('Tests passed for question 5')


