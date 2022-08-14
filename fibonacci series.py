num=10
a,b=0,1
print(b,end=(" "))
for i in range(2,10):
       c = a + b
       a = b
       b = c
       print(c,end=(" "))

