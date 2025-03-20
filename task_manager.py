#create(add) task show task  complete task/delete task. 

def add_task(tasks):
    #add in the task 
    task = input("Please input your task ")
    tasks.append(task)
    print(f"Task '{task}' added ")   

def show_task(tasks):
    #we are going to display all the tasks we have. 
    if not tasks:
        print("No tasks yet")
    else:
        print("Your Tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def complete_task(tasks): 
    #delete the task from storage 
    show_task(tasks)
    
    try:
        index = int(input("Please the Enter the id of the task you have completed: ")) - 1 
        if 0<= index <= len(tasks):
            remove_tasks = tasks.pop(index)
            print('Task removed')
        else:
            print("Invalid Id ):")
    except ValueError: 
        print("Please enter a valid number")
         
    
def main():
    #calling the functions 
    running = True
    tasks = []
    
    while running:
        print("\nOptions: 1) Add Task  2) View Tasks  3) Complete Task  4) Exit")
        choice = int((input("Choose an option: ")))   
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            show_task(tasks)
        elif choice == 3: 
            complete_task(tasks)
        elif choice == 4:
            print("Goodbye lazy! ")
            running = False 
        else:
            print("Please choode a valid option")
            
main()