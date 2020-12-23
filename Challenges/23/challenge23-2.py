import collections
from pprint import pprint
import sys

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
    ''' All values are unique '''
    def __init__(self):
        self.head = None
        self.tail = None 
        self.currentcup = None
        self.pickedup = []
        self.pickedupval = []
        self.destinationcup = None
        self.maxvalue = float("-inf")
        self.lookup = {}
    
    def build(self, node):
        self.lookup[node.value] = node
        if node.value > self.maxvalue:
            self.maxvalue = node.value
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)
        self.tail = node
        # Crabby class circular LL change

    def complete_circle(self):
        self.tail.next = self.head
        self.head.prev = self.tail
        self.currentcup = self.head.value
        visited = {}
        node = self.head

    def pickup_3(self):
        self.pickedup = []
        self.pickedupval = []
        start_node = self.lookup[self.currentcup].next
        target_node = start_node
        for _ in range(3):
            print(target_node.value)
            next_target = target_node.next
            self.remove(target_node)
            self.pickedup.append(target_node)
            self.pickedupval.append(target_node.value)
            target_node = next_target
        end_node = target_node
        start_node.next = end_node
        end_node.prev = start_node
        print(f'cups in pickedup nodes {len(self.pickedup)}')
        print(self.pickedupval)

    def set_destinationcup(self):
        self.destinationcup = None
        destination = self.lookup[self.currentcup].value - 1
        while destination <= 0 or destination in self.pickedupval:
            if destination <= 0:
                destination = self.maxvalue
            else:
                destination -= 1
        print(f'destination: {destination}')
        self.destinationcup = destination
    
    def move_3(self):
        insertion_pos = self.lookup[self.destinationcup]
        for step in range(3):
            cup_to_move = self.pickedup.pop(0)
            if step == 0:
                final_node = insertion_pos.next
                insertion_pos.next = cup_to_move
                cup_to_move.prev = insertion_pos
            else:
                prev_cup.next = cup_to_move
                cup_to_move.prev = prev_cup
            prev_cup = cup_to_move
        prev_cup.next = final_node
        final_node.prev = prev_cup
        print(f'cups left after moving {len(self.pickedup)}')

    # def setTail(self, node):
    #     self.lookup[node.value] = node
    #     if self.tail is None:
    #         self.setHead(node)
    #         return
    #     self.insertAfter(self.tail, node)
    #     # Crabby class circular LL change
    #     self.tail.next = self.head
    
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        self.lookup[nodeToInsert.value] = nodeToInsert
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
    
    def removeNodesWithValue(self, value):
        node = self.head
        while node.next is not self.head:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
        self.lookup.pop(value, None)
    
    def remove(self, node):
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next= None


class CrabbyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def crabcups1mil(crabby_llist):
    for move in range(10000000 + 1):
        print(f'-- move {move + 1} --')
        visited = {}
        current_order = []
        node = crabby_llist.lookup[3]
        while node not in visited:
            visited[node] = True
            if node.value == crabby_llist.currentcup:
                current_order.append(f'({node.value})')
            else:
                current_order.append(node.value)
            node = node.prev
        print(current_order)
        crabby_llist.pickup_3()
        crabby_llist.set_destinationcup()
        crabby_llist.move_3()
        crabby_llist.currentcup = crabby_llist.lookup[crabby_llist.currentcup].next.value
        print(crabby_llist.lookup[crabby_llist.currentcup].value)
    target = crabby_llist.lookup[1]
    onebefore = target.prev
    twobefore = target.prev.prev
    print(onebefore)
    print(twobefore)

    
example = [3,8,9,1,2,5,4,6,7]
input = [3,2,7,4,6,5,1,8,9]
# crabby_input = input + [num for num in range(100 + 1) if num > 9]  
crabby_input = example
# print(crabby_input)  
crabby_llist = CrabbyLinkedList()
for num in crabby_input:
    crabby_llist.build(CrabbyNode(num))
crabby_llist.complete_circle()
# print(crabby_llist.lookup)

crabcups1mil(crabby_llist)