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

