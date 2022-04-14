from decimal import Decimal as d
# a=d(0.5+0.3)
# a=d(0.5)+d(0.3)
# a=d('0.5')+d('0.3')
# print(a)

# a=0.5 ; b=0.3
# c=a+b
# print(c)
# print("%.1f" %c)

# print(5/0)    # Zero division error

from fractions import Fraction as f
# a=f(2,0)
# a=f(2,2)
# print(a)
# a=f(1,6)
# print(a)
# a=f(2)
# print(a)
# d=f(0,5)
# print(d)
# a=f(6,36)
# print(a)

# a=4_560
# print(a,type(a))

# a=156.0
# print(a,type(a))

# a=1_.35
# a=1._56

# a=6;b=5.6
# print(a,type(a))
# print(b,type(b))
# print(isinstance(a,int))
# print(isinstance(a,float))
# print(isinstance(a,bool))
# print(isinstance(b,int))
# print(isinstance(b,float))

a=4j
print(a,type(a))
print(isinstance(a,complex))
c=4+5j
print(c,type(c))
print(isinstance(c,complex))
