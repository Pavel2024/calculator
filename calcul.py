
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK)
print( Back.GREEN)
what = input ("Выполнить действие?(+,-,/): ")

print(Back.CYAN)

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print(Back.YELLOW
    )
if what =="+":
    c = a + b
    print("Результат: " + str(c))
elif what =="-":
    c = a - b
    print("результат: " + str(c))
elif what =="-":
    c = a - b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))

else:
    print("Неверное действие!!!")