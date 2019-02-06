#!/usr/bin/python3.6

# Developed by Wael Bahloul

# The code below is used to test the functionlity of the StackADT,
# the StackADT itself is available on the file/class StackADT

from StackADT import StackADT

class TestStack:
  def testStack(self):
    sadt = StackADT(5)
    print("Printing the Current Size")
    count1 = sadt.size()
    print (count1, "\n")
    print("Question, is it empty ?")
    x = sadt.isEmpty()
    print(x, "\n")
    print('Begin Iteration \n')
    sadt.items.printNextList()
    print("Start to push items to qeueue \n")
    print("Push Item 1 ")
    sadt.push(1)
    print("Push Item 2 ")
    sadt.push(2)
    print("Push Item 3 ")
    sadt.push(3)
    print("Push Item 4 ")
    sadt.push(4)
    print("Push Item 5 \n")
    sadt.push(5)
    print("Question, is it empty ? ")
    x = sadt.isEmpty()
    print(x, "\n")
    print("Question, is it Full ? ")
    x = sadt.isFull()
    print(x, "\n")
    print('Begin "Next" Iteration')
    sadt.items.printNextList()
    print ("\n") 
    print("Is it full? ")
    y = sadt.isFull()
    print (y, "\n")
    print("Printing the Current Size ")
    count1 = sadt.size()
    print (count1, "\n")
    
     
    print("Removing one item")
    x = sadt.pop()
    print ("Removed Items is")
    print (x, "\n")
    print ("The curent size is ")
    h = sadt.size()
    print (h, "\n")    

    print('Begin "Next" Iteration')
    sadt.items.printNextList()

    '''
    print("Removing one item \n")
    x = sadt.pop()
    print ("Removed Items is")
    print (x, "\n")
    print ("The curent size is \n")
    h = sadt.size()
    print (h)

    print('Begin "Next" Iteration \n')
    sadt.items.printNextList()

    print("Removing one item \n")
    x = sadt.pop()
    print ("Removed Items is")
    print (x, "\n")
    print ("The curent size is \n")
    h = sadt.size()
    print (h)

    print('Begin "Next" Iteration \n')
    sadt.items.printNextList()

    
    print("Removing one item \n")
    x = sadt.pop()
    print ("Removed Items is")
    print (x, "\n")
    print ("The curent size is \n")
    h = sadt.size()
    print (h)

    print('Begin "Next" Iteration \n')
    sadt.items.printNextList()


    print("Removing one item \n")
    x = sadt.pop()
    print ("Removed Items is")
    print (x, "\n")
    print ("The curent size is \n")
    h = sadt.size()
    print (h)

    print('Begin "Next" Iteration \n')
    sadt.items.printNextList()

    '''
 
def main():
  test = TestStack()
  test.testStack()

if __name__ == "__main__":
  main()

