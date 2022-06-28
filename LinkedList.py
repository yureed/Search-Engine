from re import search
from bs4 import BeautifulSoup
import timeit
import os

class Node:
    def __init__(self):
        self.data = None
        self.next = None


class CircularList:
    def __init__(self):
        self.head = None
    
    def add(self,item):
        temp = self.head
        if temp is None:
            node = Node()
            node.data = item
            self.head = node
            self.head.next = self.head
            return

        else:
            while temp.next != self.head:
                temp = temp.next
            new = Node()
            new.data = item
            temp.next = new 
            new.next = self.head
            return
    
 
    def remove(self,item):
        temp = self.head
        if self.head.data == item:
            if self.head.next != self.head:
                self.head = self.head.next
            else:
                self.head = None
            return
        else:
            while temp.next.data != item:
                temp = temp.next
            if temp.next.next == self.head:
                temp.next = temp.next.next
                temp.next.next = self.head
            else:
                temp.next = temp.next.next
    def check(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data)
            temp = temp.next
        print(temp.data)

    def search(self,item):
        temp = self.head
        count = 0
        while temp.next != self.head:
            if temp.data == item:
                count += 1
            else:
                temp = temp.next
        if temp.data == item:
            count += 1
        return count
     
    def is_empty(self):
        return self.head == None
        
    def size(self):
        temp = self.head
        total = 0
        if self.head != None:
            if temp.next == self.head:
                total = 1
                return total
            while temp.next != self.head:
                total +=1
                temp = temp.next
        return total
            
    def append(self,item):
        temp = self.head 
        n = Node()
        n.data = item
        if temp != None:
            if temp.next == self.head:
                self.head.next = n
                n.next = self.head
                return
            else:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = n
                n.next = self.head
        else:
            self.head = n
            n.next = self.head
    def index(self,item):
        temp = self.head
        index = 0
        if_found = False
        while temp.next != self.head and not if_found:
            if temp.data == item:
                if_found = True
            else:
                temp = temp.next
                index += 1
        if temp.data == item:
            if_found = True
        return index 
    
    def insert(self,pos,item):
        temp = self.head
        n = Node()
        n.data = item
        total = 0
        if temp != None:
            if  pos == 0:
                n.next = self.head
                self.head = n 
            elif pos == 1:
                n.next = temp.next
                temp.next = n
            else:
                while pos != total:
                    total += 1
                    s = temp
                    temp = temp.next
                if temp.next == self.head:
                    temp.next = n 
                    n.next = self.head
                else:
                    s.next = n 
                    n.next = temp
        
    
    def pop(self):
        temp = self.head
        if temp != None:
            if  temp.next == self.head:
                self.head = None
            else:
                while temp.next.next != self.head:
                    temp = temp.next
                temp.next = self.head

    def pop_pos(self,position):
        temp = self.head
        total = 0
        if temp != None:
            if  position == 0:
                self.head = self.head.next
            elif position == 1:
                self.head.next = self.head.next.next
            else:
                while position == total:
                    total += 1
                    s = temp
                    temp = temp.next
                if temp.next == self.head:
                    s.next = self.head
                else:
                    s.next = temp.next
                    
                    