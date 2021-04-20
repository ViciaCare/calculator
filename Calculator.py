def minus(anonimys, nomer):
    return anonimys - nomer


def multiple(vvv, ppp):
    return vvv * ppp


def division(bbb, mmm):
    return bbb / mmm


def plus(coc, pop):
    return coc + pop


d = "yes"
while d == "yes":
    print("введите число")
    a = int(input())
    print("введите знак")
    b = input()
    print("введите число")
    c = int(input())
    print("ваш ответ:")

    if b == '-':
        print(minus(a, c))
    elif b == '/':
        if c == 0:
            print(0)
        else:
            print(division(a, c))
    elif b == '*':
        print(multiple(a, c))
    elif b == '+':
        print(plus(a, c))

    print("если хотите продолжить напишите yes,если нет то no")
    d = input()




