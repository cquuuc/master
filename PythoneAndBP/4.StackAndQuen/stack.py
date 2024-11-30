class Stack:

   def __init__(this):
     this.items=[]

   def push(this,input):
    #  this.items[-1]=input
     this.items.append(input)

   def print(this):
     print(this.items)
    
   def pop(this):
     try:
       res=this.items.pop()
       return res
     except:
       print('Empty')
       
   def peek(this):
     try:
       res=this.items[-1]
       return res
     except:
       print('Empty')
     


def calc(op,a,b):
  match op:
    case '+':return a+b
 
stack1=Stack()
# stack1.push(1)
# stack1.push(1)
# stack1.push(1)
# stack1.print()
# print(stack1.pop())
# print(stack1.pop())
exp='3 4 * 2 + 2 1 * 10 2 / + /'
for e in exp.split(' '):
  if e in '+-*/'
