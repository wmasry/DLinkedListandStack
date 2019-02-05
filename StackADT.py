#!/usr/bin/python3.6

# Developed by Wael Bahloul

'''
The code below has only one class "StackADT", the code demonstrate the
functionality of the stack while by the using DLinkedListADT class
'''

from DLinkedListADT import DlinkedListADT

#items = DlinkedList()

class StackADT:
    def __init__(self, max):
        if ( max <= 0 ):
           raise Exception("The Max value must be bigger than 0")
        self.capacity = max
        self.items = DlinkedListADT()
    
    def isEmpty(self):
        x = self.items.count()
        if x == 0:
                return True
        else:
                return False

    def isFull(self):
      if self.items.count() == self.capacity:
        return True
      else:
        return False

    def push(self, item):
        if self.items.count() ==  self.capacity:
          raise Exception ("Maximum capacity reached \n")
        else:
          self.items.addFirst(item)
          x = self.items.count()

    def pop(self):
        if self.items.count == 0:
          raise Exception ("Stack is Empty \n")
        else:
          d_item = self.items.deleteFirst()
        return(d_item)


    def size(self):
        x = self.items.count()
        return x

def main():
  pass

if __name__ == "__main__":
  main()

