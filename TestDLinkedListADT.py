#!/usr/bin/python3.6

# Developed by Wael Bahloul

'''
The code below is used to demonstrate all the function created in
the DLinkedListADT, the actualy implementation of the linkedlist is
located in the file/class DLinkedListADT
It demonstrate all the functionalities
'''

from DLinkedListADT import DlinkedListADT

class TestDLinkedList:
  def testDLinkedList(self):
    d = DlinkedListADT()
    count1 = d.count()
    print("Current Count is:")
    print (count1, "\n")
    print ("Adding 2 with addFirst")
    d.addFirst(2)
    print ("Adding 1 with addFirst")
    d.addFirst(1)
    print ("Adding 3 with addLast")
    d.addLast(3)
    print ("Adding 3 again with addLast 3")
    d.addLast(3)
    print("Adding 4 with addLast")
    d.addLast(4)
    print ("Adding 5 with addLast 5")
    d.addLast(5)
    print ("Adding 6 with addLast 6")
    d.addLast(6)
    print ("Addng 7 with addLast 7")
    d.addLast(7)
    print ("")

    d.printNextList()
    print("\n")
    print ("Deleting First Occurence of 3:\n")
    d.DeleteFirstInstance(3)
    print("\n")
    d.printNextList()
    print("\n")
    print("Print the total Count")
    count2 = d.count()
    print(count2)

    d.getstart()
    d.getend()

    print("Delete the First Element \n")
    d.deleteFirst()
    print("\n")
    d.printNextList()
    print("\n")

    print("Delete the Last Element \n")
    d.deleteLast()
    print("\n")
    d.printNextList()
    print("\n")

    print("Print Previous List \n ")
    d.printPrevList() 


def main():
  testcases = TestDLinkedList()
  testcases.testDLinkedList()

if __name__ == "__main__":
    main()

