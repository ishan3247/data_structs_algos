class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    # specify an additional parameter if you want to add at a specfiic index
    def add(self, val, index = None):
        if index == None:
            if not self.head:
                self.head = Node(val)
            else:
                curr = self.head
                while curr:
                    if curr.next != None:
                        curr = curr.next
                    else: break
                curr.next = Node(val)
        else:
            counter = 0
            prev = None
            curr = self.head
            while counter < index:
                prev = curr
                curr = curr.next
                counter +=1
            # when we come out of this, curr is at the node where we want to put our node
            new = Node(val)
            if counter:
                new.next = curr
                prev.next = new
            else:
                # if 0 and the head node
                new.next = curr
                self.head = new

            


    def remove(self, goal):
        prev = None
        curr = self.head

        while curr:
            if curr.val == goal and curr!=self.head:
                prev.next = curr.next
            if curr.val == goal and curr == self.head:
                self.head = curr.next

            prev = curr
            curr = curr.next
            


list1 = SinglyLinkedList()

list1.add(1)
list1.add(2)

list1.print_list()

list1.remove(2)

print('oof')
list1.print_list()

list1.remove(1)
print('oooof')
list1.print_list()
print('yikes')

list1.add(1)
list1.add(2)
list1.add(3)
list1.add(4)


list1.add(9, 2)

list1.print_list()

list1.remove(9)

list1.print_list()




