import json
def load_todos():
    try:
        with open("todos.json","r")as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_todos(todos):
    with open("todos.json","w")as f:
        return json.dump(todos,f,indent=2)
todos=load_todos()        
while True:
    print("\n1.Add a task")
    print("2.show tasks")
    print("3.Delete a task")
    print("4.Quit")
    choice = input("choice:")
    if choice == "1":
        task=input("Enter task:")
        todos.append(task)
        save_todos(todos)
        print("Task added")
    elif choice =="2":
        if len(todos) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(todos, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        if len(todos) == 0:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(todos, start=1):
                print(f"{i}. {t}")
            try:
                number = int(input("Task number to delete: "))
                if 1 <= number <= len(todos):
                    removed = todos.pop(number - 1)
                    save_todos(todos)
                    print(f"Deleted: {removed}")
                else:
                    print("That number is not in the list.")
            except ValueError:
                print("Please type a number.")
       