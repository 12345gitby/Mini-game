"""import random as rd;

a =int(input("enter any no :  "))
random= rd.randint(0,67)

if(a>random) :
        print("you winn")
else:
        print("you fail")"""

import random as r 
n= r.randint(0,5)
if n==0:
        n='s'
elif n==1:
        n ='p'      
elif n==2:
   n=='c'

use=( input("enter input :"))
if use== n:
       print("tie")
elif use==1 and n==1:
       print("you win")

elif use==0 and n==0:
       print("you win")

elif use==2 and n==2:
       print("you win")
elif use==3 and n==3:
       print("you win")
elif use==4 and n==4:
       print("you win")
elif use==5 and n==5:
       print("you win")

else:       print("you fail")