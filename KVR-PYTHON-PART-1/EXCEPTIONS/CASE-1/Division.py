#program for Calculating division of Two Numbers
#Here Two Number are coming Different Program
#Division.py<---File Name and Module Name
from Hyd import DivsionByZeroError
def divop(a,b):
   if(b==0):
       raise DivsionByZeroError
   else:
       return(a/b)
#Phase-2: We Develop Business Logic (Problem Solving logic)
        # and we Hit Exception if Possible  in the case of Wrong Input
        # we give Output in the case of Valid Input