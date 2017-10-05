def computeHCF(x, y):
   "This function implements the Euclidian algorithm to find H.C.F. of two numbers"
   while(y!=0):
       x, y = y, x % y

   return x
a=input()
b=input()
print computeHCF(a, b)
