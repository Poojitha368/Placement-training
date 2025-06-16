class node:
    def __init__(self,d):
        self.data = d
        self.next = None
class linked:
    def __init__(self):
        self.head = None
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
    def sum_nodes(self):
        t=self.head
        tot_sum = 0
        while t!=None:
            tot_sum += t.data
            t=t.next
        print(tot_sum)
    def sum_even_nos(self):
        t=self.head
        even_sum = 0
        while t!=None:
            if t.data % 2 == 0:
                even_sum += t.data
            t=t.next
        print(even_sum)
    def sum_nos_in_even_position(self):
        pos = 1
        t=self.head
        even_pos_sum = 0
        while t!=None:
            if pos % 2 == 0:
                even_pos_sum += t.data
            t=t.next
            pos+=1
        print(even_pos_sum)
    def second_largest(self):
        largest = 0
        second_largest = 0
        t=self.head
        while t!=None:
            if t.data > largest:
                second_largest = largest
                largest = t.data
            elif t.data < largest and t.data>second_largest:
                second_largest = t.data
            t=t.next
        print("largest",largest)
        print("second largest",second_largest)
    def count_consecutive_pairs_with_lessthan_sumk(self):
        #1->2->4->5->8 , k=10
        prev = self.head
        curr = self.head.next
        k=10
        cnt=0
        while curr!=None:
            if curr.data + prev.data < k :
                cnt+=1
            prev = prev.next
            curr = curr.next
        print(cnt)
    def consecutive_pairs_with_lessthan_sumk(self):
        #5->2->4->7->3->6->5->8->None
        k=10 #o/p:
        prev = self.head
        curr = self.head.next
        while prev.next.next!=None:
            while curr.next!=None:
                if curr.data + prev.data <= k :
                    print('(',prev.data,curr.data,')')
                curr = curr.next
            prev = prev.next
            curr = prev.next
    def print_second_linkedList(self):
        #10 20 30 40 50 60 70 80 , o/p:  50 60 70 80
        slow = self.head
        fast = self.head
        while fast!=None: #find the middle element
            slow = slow.next
            fast = fast.next.next
        while slow != None:
            print(slow.data)
            slow = slow.next
    def print_kth_node_from_last(self):
        slow = self.head
        fast = self.head
        k=3
        while k>0:
            fast = fast.next
            k-=1
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
        print(slow.data)
    def del_kth_node_from_last(self):
        slow = self.head
        fast = self.head
        k=3
        while k>0:
            if fast!=None:
                fast=fast.next
            k-=1
        prev = None
        while fast!=None:
            prev=slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
    def swap_pairs(self):
        #i/p:10 -> 20 -> 30 -> 40 -> 50 -> 70 -> 80 ->None , 
        #o/p:20 -> 10 -> 40 -> 30 -> 70 -> 50 -> 80 ->None
        t=self.head
        while t.next!=None:
            t.data,t.next.data= t.next.data,t.data
            t = t.next.next
    def sort_array_bubblesort(self):
        # i/p: 9->3->10->11->2->5->6->4->1->none
        # o/p: 1 ->2-> 3-> 4-> 5-> 6-> 9-> 19-> 11->none
        t=self.head
        while t.next!=None:
            t1 = self.head
            while t1.next != None:
                if t1.data > t1.next.data:
                    t1.next.data,t1.data=t1.data,t1.next.data
                t1 = t1.next
            t=t.next


    def check_loop(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            fast = fast.next
            slow = slow.next
            if slow == fast:
                print("loop")
                break
        else:
            print("no loop")

l1 = linked()
l1.head = node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.add_back(60)
l1.add_back(70)
l1.add_back(80)
l1.display()
l1.sum_nodes()
l1.sum_even_nos()
l1.sum_nos_in_even_position()
l1.second_largest()
l1.count_consecutive_pairs_with_lessthan_sumk()
l1.consecutive_pairs_with_lessthan_sumk()
l1.print_second_linkedList()
l1.display()
l1.print_kth_node_from_last()
l1.display()
l1.del_kth_node_from_last()
l1.display()
l1.swap_pairs()
l1.display()
l1.sort_array_bubblesort()
l1.display()

l2 = linked()
l2.head = node(100)
l2.head.next = node(200)
l2.head.next.next = node(300)
l2.head.next.next.next = node(400)
l2.head.next.next.next = l2.head.next.next
l2.check_loop()

