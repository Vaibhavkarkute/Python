#n!= 1*2*3*4*5.......*n
# Factorial Program
'''
product=1
n=5
for i in range(n):
    product = product *(i+1)
print(product)
'''
'''
def fractorial_ither(n):
    product = 1
    for i in range(n):
        product = product *( i+1)
    return product
f=fractorial_ither(5) # calling function call

print(f)
'''


def fractorial_recursive(n):
    if n==1 or n==0: # base codition which does not call the fuction and further
        return 1
    return n * fractorial_recursive(n-1) # function calling itself
k=fractorial_recursive(5) # calling function call

print(k)