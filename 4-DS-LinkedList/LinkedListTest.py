from LinkedList import LinkedList

print("Creating a list with 5 values")
newl = LinkedList()
for i in range(5):
    newl.__append__(i+1)
newl.__print__()

print("Insert 3 at 3rd position")
newl.__insertAtPos__(3, 3)
newl.__print__()

print("Remove 3 from SLL")
newl.__remove__(3)
newl.__print__()
