#Quadratic Calculator
a = int(input('Please put the value of a'))
b = int(input('Please put the value of b'))
c = int(input('Please put the value of c'))
#this is for negative b
negativeb = (-b)
#this is for bsquared
bsquared = (b * b)
d = (4*a*c)
e = (2 * a)
f = (bsquared - d)
sof = (f**0.5)
x1 = ((negativeb + sof)/e)
x2 = ((negativeb - sof)/e)
print(x1,x2)

