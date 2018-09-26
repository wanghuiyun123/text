#1
celsius = raw_input("Enter a degree in Celsius:")
celsius = float (celsius)
fahrenheit = (9.0 / 5.0) * celsius + 32
print(fahrenheit)
#2
radius = raw_input("Enter the radius and length of a cylinder:")
length = raw_input(">>")
radius = float (radius)
length = float (length)
area = radius * radius * 3.14
volume = area * length
print(area)
print(volume)
#3
n = raw_input("Enter a value feet:")
n = float (n)
m = 0.305 * n
print(m)
#4
m = raw_input("Enter the amount of water in kilograms:")
n = raw_input("Enter the initial temperature:")
w = raw_input("Enter the final temperature:")
m = float (m)
n = float (n)
w = float (w)
q = m * (w - n) * 4184
print(q)
#5
m,n = eval(raw_input("Enter balance and interest rate(e.g.,3 for 3%):"))
i = m * (n/1200)
print(i)
#6
v0,v1,t = eval(raw_input("Enter v0, v1, and t:"))
a = (v1 - v0) / t
print(a)
#7
n = float(raw_input("Enter the monthly saving amount:"))
x = 0
for i in range(6):
    y = n * (1 + 0.00417)
    x = x + y
print(x)
#8
n =int(raw_input("Enter a number between 0 and 1000:"))
i = n // 100
j = (n % 100) // 10
m = n % 10
add = i + j +m
print(add)

