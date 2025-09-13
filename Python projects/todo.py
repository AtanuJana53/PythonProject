def task():
    tasks=[]
    print("-----WELCOME TO TASKS MANAGEMENT SYSTEM-----")
    total_task=int(input("Enter the total number of tasks: "))
    for i in range(1,total_task+1):
        tasks_name=input(f"Enter the task: {i} = ")
        tasks.append(tasks_name)

    print("Total tasks: ",tasks)
    while True:
        operation=int(input("Enter the operation:{ 1.Add 2.Update 3.Delete 4.View 5.Exit}\n"))
        if operation==1:
             add=input("Enter tasks to add: ")
             tasks.append(add)
             print("Tasks added :",tasks)
        elif operation==2:
            update=input("Enter the task which you want to update: ")
            if update in tasks:
                up=input("Enter new task to update: ")
                index=tasks.index(update)
                tasks[index]=up
                print("Task updated :",tasks)
            else:
                print("Task not found")
        elif operation==3:
             delete=input("Enter the task which you want to delete: ")
             if delete in tasks:
                  index=tasks.index(delete)
                  del tasks[index]
                  print("Task deleted :",tasks)
             else:
                print("Task not found")

        elif operation==4:
            print("Total tasks:",tasks)
        elif operation==5:
            print("Exiting...")
            break
        else:
            print("Invalid operation... please try again")

task()