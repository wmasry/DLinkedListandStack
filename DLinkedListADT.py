#!/usr/bin/python3.6

# Developed by Wael Bahloul

# The code below have two classes "Node" and "DlinkedListADT"
# with some functionalities to add, remove, traverse ... etc

class Node:
  def __init__(self, n):
    self.next = None
    self.prev = None
    self.num = n

class DlinkedListADT:
   def __init__(self):
     self.start = None
     self.end = None
     self.size = 0

   def addFirst(self, num):
     n = Node(num)

     if(self.start == None):
       self.start = n
       self.end = n
       self.size = self.size + 1
     else:
       n.next = self.start
       self.start.prev = n
       self.start = n
       self.size = self.size + 1

   def addLast(self, num):
      n = Node(num)
      if(self.start == None):
          self.start = n
          self.end = n
          self.size = self.size + 1
      else:
        self.end.next  = n
        n.prev = self.end
        self.end = n
        self.size = self.size + 1


   def deleteFirst(self):
     n = self.start
     if (self.start == None):
          print ("There are no elements to delete")
     if ( self.start == self.end ):
          x = self.start.num
          self.start = None
          self.end = None
          self.size = self.size - 1
     else:
       x = self.start.num
       self.start = self.start.next
       self.start.prev = None
       self.size = self.size - 1
     return(x)

   def deleteLast(self):
      n = self.end
      if (self.start == None):
          print ("Nothing to be deleted")
      if ( self.start == self.end):
        print ("One element in the linked list")
        print ("Element will be delted")
        x = self.start.num
        self.start = None
        self.end = None
        self.size = self.size - 1
      else:
        x = self.end.num
        print ("One element will be deleted")
        self.end = self.end.prev
        self.end.next = None
        self.size = self.size - 1
      return(x)



   def printNextList(self):
     print ("Iterate forward through the Linked List\n")
     n = self.start
     while(n is not None):
        print (n.num)
        n = n.next

   def count(self):
     #print ("The current count of the DLinkedList is")
     x = self.size
     return x


   def printPrevList(self):
     print ("Iterate through the Linked List reversably")
     n = self.end
     while(n is not None):
        print (n.num)
        n = n.prev

   def getstart(self):
      print ("print the first Node")
      n = self.start
      print (n.num)

   def getend(self):
     print ("Print the last Node")
     n = self.end
     print (n.num)

   def DeleteFirstInstance(self, num):
     n = self.start
     while ( n is not None ):
       if n.num == num:
        if n.prev == None:
          self.deleteFirst()
          break
        if n.next == None:
          self.deleteLast()
          break
        else:
          print ("Deleting the Element")
          n.prev.next = n.next
          n.next.prev = n.prev
          self.size = self.size - 1
          break
       else:
          #continue the loop
          n = n.next


def main():
  pass

if __name__ == "__main__":
  main()

