tasks= []

while True:
    print()
    print("1. Add a task here")
    print("2. view task")
    print("3. Quit")
    choice= input("choose 1, 2 or 3:")

    if choice =="1":
        task = input("Type a task here:").strip()
        if task:
            tasks.append(task)
            print("saved.")
        else:
            print("Nothing typed.")

    elif  choice == "2":
        if not tasks:
            print("No task yet.")
        else:
            for number, task in enumerate(tasks, start =1):
                print(f"{number}. {task}")
    elif choice== "3":
        print("Goodbye.")
        break
    else:
        print("pick 1, 2 or 3.")

        

