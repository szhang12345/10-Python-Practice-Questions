'''
Q1：Fibonacci Sequence
'''


def Q1():
    l = [0, 1]


for i in range(10):
    arr = l[-2:]
    l.append(arr[0] + arr[1])
print(l)

'''
Q2：Pause one second output and format current time。
'''


def Q2():


import time

a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(a)
time.sleep(1)
b = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(b)

'''
Q3：print date and time as required format。
'''


def Q3():


import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

st = time.localtime(time.time())
st = time.strptime('2018/1/23', '%Y/%m/%d')
print(date)

'''
    Q4：
    Print the following picture:
    *
    ** *
    ** ** *
    ** ** ** *
    ** ** *
    ** *
    *
    '''


def Q4():
    num = 7


for i in range(num):
    blank = abs(num // 2 - i)
    print(' ' * blank + '*' * (num - 2 * blank) + ' ' * blank)

'''
    Q5：a sequence of number：2 / 1，3 / 2，5 / 3，8 / 5，13 / 8，21 / 13...sum the first 20 items
    '''


def Q5():


a, b, num = 2, 1, 0
for i in range(20):
    num += a / b
    a = a + b
    b = a - b
print(num)

'''
    Q6：get the sum of 1 + 2!+3!+... + 20!.
    '''


def Q6():


s, t = 0, 1
for n in range(1, 21):
    t *= n
    s += t
print(s)

'''
    Q7：print out the five numbers in reverse order
    '''


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


def Q7_2():


s = input('Input a string:')
l = len(s)
output(s, l)

'''
    Q8：provide a positive number <=100,000, print out the number in reverse order.
    '''


def Q8():
    num = 12345


s = str(num)
print(len(s))
print(s[::-1])

'''
    Q9：confirm if a number is a palindrome number.
    '''


def Q9():


num = int(input("number: "))
s = str(num)
for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        print(False)
        break
else:
    print(True)

'''
    Q10：input the first letter of a date to decide it is which weekday.
    '''


def Q10():


week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
inp = ''
while 1:
    arr = []
    inp = inp + input('INPUT A LETTER:')
    for day in week:
        if inp == day[:len(inp)]:
            arr.append(day)
    if len(arr) == 1:
        print('Word starting with %s:%s' % (inp, arr[0]))
        inp = ''
    elif len(arr) == 0:
        print('no word starting with %s' % inp)
        inp = ''
        
        
      import itertools
    temp_arr = list(itertools.permutations([1, 2, 3, 4], 3)) # 排列  # A_4^3 = (4)!/(4-3)! = (4*3*2*1)/1 = 24
    arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
    print(len(arr),arr)
