#accessing item is O(n) since you have to go throug entire list
#but insertion and deletion are easier. O(1) since you just modify the links
#in arrays (dynamic arrays), when you're out of initial memory capacity, you'll end up
#creating more space and copying everything you had initially into it. Too much overhead
#when you want to insert at an index, you'll have to shift all the other items, O(n). Same for deletion

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
    
        itr = self.head

        llstr = ""
        while itr:
            llstr += str(itr.data) + "->"
            itr = itr.next

        print(llstr)

if __name__ == "__main__":

    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    ll.insert_values(["banana","mango","grapes","oranges"])
    ll.remove_at(3)
    ll.print()

    ll.insert_at(0, "figs")

    ll.insert_at(2, "jackfruit")
    ll.print()