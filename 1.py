
num=float(input("Введите количество чисел в массиве: "))
while num-num//1!=0 or num<=0:
    if num-num//1!=0:
        print("Введите целое число!")
        num=float(input("Введите количество чисел в массиве: "))
    if num<=0:
        print("Введите число больше 0!")
        num=float(input("Введите количество чисел в массиве: "))



def fun(n):
    n=int(n)   
    m=[]
    for x in range(n):
        m.append(float(input("Введите число из массива ")))
    max=m[0]
    for i in m:
        if i>max:
            max=i
    m=m[:m.index(max) + 1] + [0]*(len(m)- len(m[:m.index(max) + 1]))
    print(m)

fun(num)
