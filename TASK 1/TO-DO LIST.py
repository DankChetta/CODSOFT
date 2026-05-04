tasks = []
def show():
    print("\n----TO-DO LIST----")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Mark Task as Complete")
    print("5.Exit")

def add():
    t=input("Enter task: ")
    tasks.append({"task":t,"status":False})
    print(f"Task'{t}' added.")
    
def view():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "Done" if t["status"] else "Pending"
            print(f"{i}. {t['task']} - {status}")

def done():
    view()
    if not tasks:
        return
    try:
        i=int(input("Enter task number to mark as complete: "))-1
        if 0 <= i < len(tasks):
            tasks[i]["status"]=True
            print(f"Task '{tasks[i]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove():
    view()
    if not tasks:
        return
    try:
        i=int(input("Enter task number to remove: "))-1
        if 0 <= i < len(tasks):
            removed=tasks.pop(i)
            print(f"Task '{removed['task']}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
while True:
    show()
    choice=input("Choose an option: (1-5) ")
    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        remove()
    elif choice=="4":
        done()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")