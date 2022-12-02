import amritdb
ROOT =    amritdb.getRoot()
LogFP = f"{ROOT}/Log"
check =    amritdb.pathCheck(LogFP)

#print(check)
if check ==    True:
    amritdb.chdir(f"{ROOT}/Log")
else:
    amritdb.createLogFolder("Log",ROOT)

NAME =    []
DB = {}
B = 0
print(amritdb.getTime())
time =    amritdb.getTimeNS()
print(ROOT)
def vote():
         
         print(f"candidate list {NAME}")
         IN = input("CAST YOUR VOTE: ").lower()
         
         if IN in DB:
             DB.update({IN : DB.get(IN)+1})
         else:
             vote()
             
         ASK =    input("more voters ?(y/n) :    ").lower()
         if ASK ==    "y":
             vote()
         elif ASK ==    "n":
             print("logging not work on android 11 until permission btw ")
             print(DB)
             amritdb.TouchWrite(f"{time}.txt",str(DB))
             exit()
         else:
             vote()
 
def create():
     A =    input("which voter to register: ")
     NAME.append(A)
     print(NAME) 
     DB[A] =    0
     B =    input("do you have more(y/n): ")
     if B == "y":
         B = 0
         create()
     elif B ==    "n":
         vote()
     else:
         vote()
create()