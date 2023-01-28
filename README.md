# Python Fundamentals

This is my first Github repository. I am in the process of learning Python and I want to apply what I see in courses and tutorials. For this reason, I share some of the projects that I am making with Python fundamentals.

## Guess the Number

**1.** I start by importing the random module in my Python script.

**2.** I create a variable called "answer" that stores a random number generated by the randint function of the random module.

**3.** I use a while loop to allow the user to guess the number. Inside the loop, I ask the user to enter a number and store it in a variable called "guess".

**4.** I use an if statement to compare guess with answer. If they are equal, I print a congratulations message and break the loop. If guess is greater or less than answer, I print a message indicating if the guessed number is greater or less than the correct number and ask for a number again.

**5.** I add a counter to keep track of the attempts and show it to the user.

**6.** I add an option for the user to exit the game.

```python

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
        
```

## Task List

*1.* Start by importing the Tkinter library.

*2.* Create a main window using the Tk() class.

*3.* Use the Label class to create labels to describe the application.

*4*. Use the Entry class to create an input field where the user can enter a new task.

*5.* Use the Button class to create buttons to add, delete, and update tasks.

*6.* Use the Listbox class to create a drop-down list where the tasks will be displayed.

*7.* Use a text file or a database to store the tasks entered by the user.

*8.* Create functions to add, delete, and update tasks, associated with the corresponding buttons.

*9.* Use a while loop to keep the window open while the user uses the application.


```python

import tkinter as tk

def add_task():
    task = task_input.get()
    tasks.append(task)
    task_input.delete(0, "end")
    update_task_list()

def update_task_list():
    clear_task_list()
    for task in tasks:
        task_list.insert("end", task)

def clear_task_list():
    task_list.delete(0, "end")

root = tk.Tk()
root.title("Lista de Tareas")

tasks = []

task_label = tk.Label(root, text="Ingresa una nueva tarea:")
task_label.pack()

task_input = tk.Entry(root)
task_input.pack()

add_button = tk.Button(root, text="Agregar", command=add_task)
add_button.pack()

add_button = tk.Button(root, text="Tarea completada", command=update_task_list)
add_button.pack()

add_button = tk.Button(root, text="Borrar Lista", command=clear_task_list)
add_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

root.mainloop()


