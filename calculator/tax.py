print("Привет! Как тебя зовут?")
name = str(input())
print("Откуда ты?")
born = str(input())
print("Сколько ты зарабатываешь?")
earn = int(input())


a= int(earn*43)
tax=str(int(a/100))
print(name + " из " + born + " ты платишь " + tax + " рублей налогов!")
