'''
#1
import math
r = eval(raw_input("Enter the length form the center to a vertex:"))
s = 2 * r * math.sin(math.pi / 5)
Area = (5 * pow(s,2)) / (4 * math.tan(math.pi / 5))
print('The area of the pentagon is {:.2f}'.format(Area))

#2
import math
x1,y1 = eval(raw_input("Enter point 1 (latitude and longitude) in degrees:"))
x2,y2 = eval(raw_input("Enter point 2 (latitude and longitude) in degrees:"))
a = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
b = math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1) - math.radians(y2))
d = 6371.01 * math. acos(a + b)
print('The distance between the two points is {} km. '.format(d))

#3
import math
s = eval(raw_input("Enter the side:"))
a = 5 * pow(s,2)
b = 4 * math.tan(math.pi / 5)
Area = a / b
print('The area of the pentagon is {}'.format(Area))

#4
import math
n = eval(raw_input("Enter the number of sides:"))
s = eval(raw_input("Enter the side:"))
a = n * pow(s,2)
b = 4 * math.tan(math.pi / n)
Area = a / b
print('The area of the polygon is {}'.format(Area))

#5
n = eval(raw_input("Enter ACSII code(0~127):"))
m = chr(n)
print('The character is {}'.format(m))

#6
a = raw_input("Enter employee's name:")
b = eval(raw_input("Enter number of hours worked in a week:"))
c = eval(raw_input("Enter hourly pay rate:"))
d = eval(raw_input("Enter federal tax withholding rate:"))
e = eval(raw_input("Enter state tax withholding rate:"))
f = b * c
g = (b * c) * 0.2
h = (b * c) *0.09
i = g + h
j = f - i
print('Employee Name: {}'.format(a))
print('Hours Worked: {}'.format(b))
print('Pay Rate: {}'.format(c))
print('Gross Pay: {}'.format(f))
print('Deductions:')
print('Federal Withholding(20.0%) {}:'.format(g))
print('State Withholding(9.0%) {}:'.format(h))
print('Total Deduction {}:'.format(i))
print('Net Pay: {}'.format(j))

#7
n = int(raw_input("Enter an integer:"))
q = n // 1000
b = (n // 100) % 10
s = (n // 10) % 10
g = n % 10
print(str('The reversed number is ')+str(g)+str(s)+str(b)+str(q))

#8
for i in "asdfghjkl":
    res = chr(ord(i) + 2)
    print(res)

#1
import math
a,b,c = eval(raw_input("Enter a, b, c:"))
n = pow(b ,2) - 4 * a * c
if n > 0:
    r1 = (-b + math.sqrt(n)) / 2 * a
    r2 = (-b - math.sqrt(n)) / 2 * a
    print(str('The roots are '+ str(r1) + str(' and ') + str(r2)))
elif n == 0:
    r = (-b + math.sqrt(n)) / 2 * a
    print(str('The root is ')+str(r))
else:
    print(str('The equation has no real roots'))

#2
import random
n = random.randint(0,100)
m = random.randint(0,100)
print('n = {}'.format(n))
print('m = {}'.format(m))
a = eval(raw_input("Enter add :"))
if a == n + m:
    print("true")
else:
    print("false")

#3
n = eval(raw_input("Enter today's day:"))
m = eval(raw_input("Enter the number of days elapsed since today:"))
a = m % 7

#4
a,b,c = eval(raw_input("Enter a , b , c :"))
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(a,b,c)

#5
a,b = eval(raw_input("Enter weight and prive for package 1:"))
c,d = eval(raw_input("Enter weight and prive for package 2:")) 
n = b / a
m = d / c
if n > m:
    print("Package 2 has the better price.")
else:
    print("Package 1 has the better price.")

#6
#7
#8
'''
#10
import random
n = str(random.randint(Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King))
m = str(random.randint(meihua,hongtao,fangkuai,heitao))
print(str('The card you picked is the ')+str(n)+str(' of ')+str(m))
'''
#11
n = int(raw_input("Enter a three-digit integer:"))
b = n // 100
g = n % 10
if b == g:
    print("{} is a palindrome.".format(n))
else:
    print("{} is not a palindrome.".format(n))

#12
a,b,c =eval(raw_input("Enter three edges:"))
if a + b > c or a + c > b or b + c > a:
    n = a + b + c
    print("The perimeter is {} ".format(n))
else:
    print("false")
'''
