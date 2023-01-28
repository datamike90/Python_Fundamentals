import random

answer = random.randint(1, 100)
guess = None
tries = 0

while guess != answer:
    guess = int(input("Adivina el número de 1 a 100: "))
    tries += 1
    if guess < answer:
        print("El número es mayor")
    elif guess > answer:
        print("El número es menor")
    else:
        print("Bien hecho! Adivinaste el número {} intentos.".format(tries))
