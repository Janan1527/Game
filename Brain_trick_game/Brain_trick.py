
from time import sleep 
print("***\t\t\t\t**  WELCOME TO MIND TRICK GAME  **\t\t\t\t***\n")
name=input("\nEnter your name to play the game :\t")
sleep(1)
 
print("Hai ",name,"\n""Wait three second to start the game")

ls = ["1", "\t2", "\t\t3","\t\t\tGame starts now...."]
for i in ls:
    print(i)
    sleep(1) 
sleep(3)    
print("Do the following steps carefully\n\n")
sleep(2)
print("step 1: \tThink of a number\n")
sleep(4)
a=input("\nIf you think any number enter 'yes' to move step 2 :  ").upper()
if a=='YES':
    sleep(1)
    print("\n\nstep 2: \tDouble it\n")
    sleep(3)
    b=input("\nif you double it enter 'yes'to move step 3 :  ").upper()
    if b=="YES":
        sleep(1)
        print("\n\nstep 3: \tAdd 6 to step 2 ans \n")
        c=input("\nif you add it enter 'yes':  ").upper()
        if c=="YES":
            sleep(2)
            value=int(input("\n\nEnter the value you got in step 3 : "))
            print("\n\nWait two seconds")
            d=(value/2)
            original=(d-3)
            sleep(2)
            print("\n",name," The number you thought is ",round(original))
        
print("\t\t***Game End***")           
          
    
    