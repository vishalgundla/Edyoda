#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
# 

# In[1]:


from itertools import combinations

def findPairs(lst, K):

    return [pair for pair in combinations(lst, 2) if sum(pair) == K]


lst=list(map(int,input("Enter integer element of an array separated by comma").split(",")))
K = int(input("Enter the sum value"))
print(findPairs(lst, K))


# # Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[1]:


def reverseArray(A):
    print( A[::-1])

A = list(map(int,input("Enter element of an array separated by comma").split(",")))
print("Original array is")
print(A)
print("Reversed array is")
reverseArray(A)


# In[ ]:





# # Q3. Write a program to check if two strings are a rotation of each other?

# In[2]:


def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
    
    temp = string1 + string1

    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")


# # Q4. Write a program to print the first non-repeated character from a string?

# In[3]:


from collections import Counter

def printNonrepeated(string):
    
    freq = Counter(string)

    for i in string:
        if(freq[i] == 1): 
            print(i)
            break

string = "Hello Everyone"

printNonrepeated(string)


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[4]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods


# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[7]:


# function to check if
# character is operator or not


def isOperator(x):
    
    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True
    
    if x == "*":
        return True

    return False

# Convert postfix to Prefix expression


def postToPre(post_exp):

    s = []

    # length of expression
    length = len(post_exp)

    # reading from right to left
    for i in range(length):

        # check if symbol is operator
        if (isOperator(post_exp[i])):

            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            # concat the operands and operator
            temp = post_exp[i] + op2 + op1

            # Push string temp back to stack
            s.append(temp)

        # if symbol is an operand
        else:

            # push the operand to the stack
            s.append(post_exp[i])


    ans = ""
    for i in s:
        ans += i
    return ans


# Driver Code
if __name__ == "__main__":

    post_exp = "AB+CD-"
    
    # Function call
    print("Prefix : ", postToPre(post_exp))


# # Q7. Write a program to convert prefix expression to infix expression.

# In[8]:


def prefixToInfix(prefix):
    stack = []

    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
            i -= 1
        else:
            
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/DEB"
    print(prefixToInfix(str))


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[9]:


def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# # Q9. Write a program to reverse a stack.

# In[10]:


class Stack:
 
    # create empty list
    def __init__(self):
        self.Elements = []
         
    # push() for insert an element
    def push(self, value):
        self.Elements.append(value)
       
    # pop() for remove an element
    def pop(self):
        return self.Elements.pop()
     
    # empty() check the stack is empty of not
    def empty(self):
        return self.Elements == []
     
    # show() display stack
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
# Insert_Bottom() insert value at bottom
def BottomInsert(s, value):
   
    # check the stack is empty or not
    if s.empty():
         
        # if stack is empty then call
        # push() method.
        s.push(value)
         
    # if stack is not empty then execute
    # else block
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
# Reverse() reverse the stack
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 
# create object of stack class
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# # Q10. Write a program to find the smallest number using a stack.

# In[11]:


class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)

    # __repr__ is same as __str__
    __repr__ = __str__


class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))

    # __repr__ is same as __str__
    __repr__=__str__

    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))



    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
        # If top not equal to None then stack is empty
            return False

    # This method returns length of stack	
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count

    # This method returns top of stack	
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))

    # This method is used to add node to stack
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))

    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print ("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))


# Driver program 
stack = Stack()

stack.push(3)
stack.push(5)
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()
stack.pop()
stack.getMin()
stack.pop()
stack.peek()

