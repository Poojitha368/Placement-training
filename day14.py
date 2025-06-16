class node:
    def __init__(self,d):
        self.data = d
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t = self.head
        while t.next != None:
            t = t.next
        t.next = node(x)
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,"->",end=" ")
            t=t.next
        print(None)
    def check_loop(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    def start_loop(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow= slow.next
            fast = fast.next
        print("Start of loop is:", slow.data)
    def no_of_nodes_in_loop(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        cnt=1
        slow = slow.next
        while slow != fast:
            cnt+=1
            slow = slow.next
        print(cnt)
    def remove_cycle(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        slow = self.head
        #start of loop
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        fast = fast.next
        while fast.next != slow:
            fast = fast.next
        fast.next = None

    def rev_linked_list_stack(self):
        #10->20->30->40->50->None , 
        # reverse linked list using stack
        stack = []
        t = self.head
        while t!=None:
            stack.append(t.data)
            t=t.next
        t=self.head
        while t!=None:
            t.data = stack.pop()
            t=t.next
    def rev_linked_list_no_stack(self):
        c = self.head
        n = self.head.next
        prev = None
        while c!=None: #first p,c,n moves
            c.next = prev
            prev = c
            c = n
            if c!=None:
                n = c.next #store as link breaks when c.next = prev, so to move c need n
        self.head=prev
    # def check_palindrome(self):
        #i/p: 10->20->30->20->10->None, o/p: palindrome list or not
    def reverse_second_half_linked_list(self):
        # i/p: 10->20->30->40->50->60->None
        # o/p: 10->20->30->60->50->40->None
        fast = self.head
        slow = self.head
        while fast!=None and fast.next!=None:
            p = slow
            slow = slow.next
            fast = fast.next.next
        curr = slow
        n = slow.next
        prev = None
        while curr!=None:
            curr.next = prev
            prev = curr
            curr = n
            if curr!=None:
                n = curr.next
        p.next = prev
    def check_palindrome(self):
        #i/p: 10->20->20->10->None
        #o/p: 10->20->10->20->None
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            p = slow
            slow = slow.next
            fast  = fast.next.next

        #reverse second part
        curr = slow
        prev = None
        while curr != None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        p.next = prev

        #10->20->10->20
        slow = self.head
        fast = self.head
        while fast!=None:
            fast = fast.next.next
            slow = slow.next
        t = self.head
        while slow!=None:
            if t.data != slow.data:
                print(False)
                break
            t=t.next
            slow = slow.next
        else:
            print(True)
        
    # def find_junction_point(self):
    #     #i/p: 

l2 = linked()
l2.head = node(100)
l2.head.next = node(200)
l2.head.next.next = node(300)
l2.head.next.next.next = node(400)
l2.head.next.next.next.next = node(500)
l2.head.next.next.next.next.next = l2.head.next.next 
if l2.check_loop():
    l2.start_loop()
l2.no_of_nodes_in_loop()
l2.remove_cycle()
l2.display()
l2.rev_linked_list_stack()
l2.display()
l2.rev_linked_list_no_stack()
l2.display()
l2.reverse_second_half_linked_list()
l2.display()

l3 = linked()
l3.head = node(10)
l3.add_back(20)
l3.add_back(20)
l3.add_back(10)
l3.display()
l3.check_palindrome()