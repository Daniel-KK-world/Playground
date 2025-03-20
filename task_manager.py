#create(add) task show task  complete task/delete task. 

def add_task(tasks):
    #add in the task 
    task = input("Please input your task ")
    tasks.append(task)

def show_task(tasks):
    #we are going to display all the tasks we have. 
    if not tasks:
        print("No tasks yet")
    else:
        print("Your Tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.task")

def complete_task(tasks): 
    #delete the task from storage 
    show_task()
    
    try:
        index = int(input("Please the Enter the id of the task you have completed: ")) - 1 
        if 0<= index <= len(tasks):
            remove_tasks = tasks.pop(index)
            print('Task removed')
        else:
            print("Invalid Id ):")
    except ValueError 
        print("Please enter a valid number")
         
    
def main():
    #calling the functions 
    tasks = []
    
    while True:
        print("\nOptions: 1) Add Task  2) View Tasks  3) Complete Task  4) Exit")
        choice = input("Choose an option: ")
        
        