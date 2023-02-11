#first pattern
'''
*
**
***
****
'''
n=5

for i in range(n): 
    for j1 in range(0,i+1):
        print(" * ", end ="")
    print(" " )

'''
     *     
    * *
   * * *
  * * * *

'''
n=5

k=n-1 # number of spaces
for i in range (0,n): #outer loop to handle number of spaces
    for j1 in range(0,k):
        print(end=" ") # spacing outer side 
    k=k-1 # decrement of k after each loop
    for j1 in range(0,i+1): # inner loop to handle number of columns 
        print(" * ",end ="")
    print("\r") # end with each rows

