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
        for i, task in enumerate(tasks, 1):
            print(f"{i}.task")

def complete_task(): 
    #delete the task from storage 
    pass 
    
def main():
    #ask the user for input and call the functions. 
    tasks = []
    pass 