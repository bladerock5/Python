#Числа, кратные 3 или 5
#b = 0
#for i in range(1, 1000):
#    a = i % 3
#    c = i % 5
#    if (a == 0) | (c == 0):
#        #print (i)
#        b = b + i
#print(b)

#Четные числа Фибоначчи
#def fib(n):
#    a = 0
#    b = 1
#    for __ in range(n):
#        a, b = b, a + b
#    return a
#
#i = 0
#sum = 0
#c = 0
#while c < 4000000:
#    c = fib(i)
#    d = c % 2
#    if d == 0:
#        sum = sum + c        
#    i += 1
#print(sum)

#Наибольший простой делитель
f = 0
y = 600851475143
for i in range((y - 1), 0, -1):
    b = y % i
    if b == 0:
        print(i)
        f = i
        break
print(f)