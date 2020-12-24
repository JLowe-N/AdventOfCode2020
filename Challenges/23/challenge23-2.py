import collections
from pprint import pprint
import sys
import timeit
import time

def time_it(f):
    time_it.active = 0

    def tt(*args, **kwargs):
        time_it.active += 1
        t0 = time.time()
        tabs = '\t'*(time_it.active - 1)
        name = f.__name__
        print('{tabs}Executing <{name}>'.format(tabs=tabs, name=name))
        res = f(*args, **kwargs)
        print('{tabs}Function <{name}> execution time: {time:.3f} seconds'.format(
            tabs=tabs, name=name, time=time.time() - t0))
        time_it.active -= 1
        return res
    return tt

def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data.append(line)
            linenum += 1
    return data


class CrabbyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.currentcup = None
        self.lookup = {}
        self.max = float("-inf")
        self.length = 0

    def get_list_order(self):
        visited ={}
        node = self.head
        next_order_cw = []
        while node not in visited:
            visited[node] = True
            next_order_cw.append(str(node.value))
            node = node.next
        print(" ".join(next_order_cw))

    
    def build(self, node):
        self.length += 1
        self.lookup[node.value] = node
        if node.value > self.max:
            self.max = node.value
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def complete_circle(self):
        self.head.prev = self.tail
        self.tail.next = self.head
        self.currentcup = self.head

    def test_circle(self):
        node = self.head
        visited = {}
        test_length = 0
        while node not in visited:
            visited[node] = True
            test_length += 1
            node = node.next
        if test_length != self.length:
            print("Next direction not set up correctly.")
        visited = {}
        test_length = 0
        while node not in visited:
            visited[node] = True
            test_length += 1
            node = node.prev
        if test_length != self.length:
            print("Next direction not set up correctly.")
        print("Tests complete!")

    @time_it
    def crab_shuffle(self):
        # self.get_list_order()
        # Pick 3
        pickupval = []
        pickednodes = []
        pickupnode = self.currentcup.next
        for _ in range(3):
            pickupval.append(pickupnode.value)
            pickednodes.append(pickupnode)
            pickupnode = pickupnode.next
        
        # Pick Destination
        destination = self.currentcup.value - 1
        while destination <= 0 or destination in pickupval:
            if destination <= 0:
                destination = self.max
            else:
                destination -= 1
        
        # Move 3
        # Pluck out 3, reconnect
        left = self.currentcup
        right = self.currentcup.next.next.next.next # skip over 3
        left.next = right
        right.prev = left

        # now make room for inserted cups
        left = self.lookup[destination]
        right = left.next
        prev_cup = left
        for _ in range(3):
            inserted_cup = pickednodes.pop(0)
            prev_cup.next = inserted_cup
            inserted_cup.prev = prev_cup
            prev_cup = inserted_cup
        prev_cup.next = right
        right.prev = prev_cup

        # finally update current cup to it's next cup
        self.currentcup = self.currentcup.next
        # print(f'current: {self.currentcup.value}')
        # print(f'pick up: {pickupval}')
        # print(f'destination: {destination}')


class CrabbyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def crabcups1mil(crabby_llist):
    for move in range(10000000):
        start = timeit.default_timer()
        if move % 1000000 == 1:
            end = timeit.default_timer()
            print(f'1000000 cycles took {end - start}')
            start = timeit.default_timer()
        # print(f'-- move {move+1} --')
        crabby_llist.crab_shuffle()
    # print('-- final --')
    # crabby_llist.get_list_order()
    one_node = crabby_llist.lookup[1]
    print(one_node.next.value)
    print(one_node.next.next.value)
    

    
example = [3,8,9,1,2,5,4,6,7]
input = [3,2,7,4,6,5,1,8,9]
crabby_input = input + [num for num in range(1000000 + 1) if num > 9]  
# print(crabby_input)  
crabby_llist = CrabbyLinkedList()
start = timeit.default_timer()
for num in crabby_input:
    crabby_llist.build(CrabbyNode(num))
end = timeit.default_timer()
print(f'build took {end - start}')
crabby_llist.complete_circle()
# print(crabby_llist.lookup)

crabcups1mil(crabby_llist)