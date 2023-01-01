transction=[]
bnc=0
while True:
      op=input("please enter the transaction(enter 'Exit' for stop ) :-")
      if op=="Exit":
          break
      transction.append(op.split())
def deposite(a):
       global bnc
       bnc=bnc+a

def withdraw(b):
       global bnc
       if(bnc>0):
             bnc=bnc-b
       else:
            print("Sorry !! , Low balance")

print("The total transctions are :-",transction)
for i in transction:
      if i[0]=="D":
           deposite(int(i[1]))
      elif i[0]=="W":
           withdraw(int(i[1]))
print("The net balanc is :-",bnc)