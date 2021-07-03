import sys
print(sys.getrefcount(1000))
x=1000
print(sys.getrefcount(1000))
y=1000
print(sys.getrefcount(1000))

print(x is y)# If you want to print 'x is y', you should write codes like "print('x is y')

